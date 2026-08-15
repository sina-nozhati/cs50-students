"""تست‌های سرویس مدیریت تکالیف و تحلیل‌ها."""
import pytest
from datetime import datetime, timedelta

from app import create_app, db
from app.models import User, Assignment, Submission, XPLog, WeekProgress
from app.services import assignments_admin as assignments_service
from app.services import analytics as analytics_service


@pytest.fixture
def app():
    app = create_app("app.config.TestingConfig")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def seeded_app(app):
    """اپ با داده‌های اولیه: ۱ ادمین + ۳ دانش‌آموز + ۱ تکلیف."""
    with app.app_context():
        admin = User(username="admin", password_hash="x", is_admin=True, xp=0)
        s1 = User(username="s1", password_hash="x", xp=100, streak=5)
        s2 = User(username="s2", password_hash="x", xp=50, streak=2)
        s3 = User(username="s3", password_hash="x", xp=30, streak=0)
        db.session.add_all([admin, s1, s2, s3])
        db.session.commit()

        a1 = Assignment(
            title="Scratch Project",
            week=0,
            due_date=datetime.utcnow() + timedelta(days=7),
            xp_reward=25,
            is_active=True,
        )
        db.session.add(a1)
        db.session.commit()

        # دو تحویل
        sub1 = Submission(student_id=s1.id, assignment_id=a1.id, github_url="https://github.com/s1/scratch")
        sub2 = Submission(student_id=s2.id, assignment_id=a1.id, github_url="https://github.com/s2/scratch", grade=85, feedback="عالی")
        db.session.add_all([sub1, sub2])

        # XP logs
        db.session.add(XPLog(user_id=s1.id, amount=25, reason="Submitted Scratch"))
        db.session.add(XPLog(user_id=s2.id, amount=25, reason="Submitted Scratch"))
        db.session.commit()

        yield app


class TestAssignmentsCRUD:
    """تست ایجاد/ویرایش/تغییر وضعیت تکلیف."""

    def test_create_assignment(self, app):
        with app.app_context():
            a = assignments_service.create_assignment(
                title="Hello World",
                week=1,
                due_date=datetime(2026, 9, 1),
                xp_reward=30,
            )
            assert a.id is not None
            assert a.title == "Hello World"
            assert a.xp_reward == 30
            assert a.is_active is True

    def test_update_assignment(self, app):
        with app.app_context():
            a = assignments_service.create_assignment("Test", 0, datetime(2026, 9, 1))
            updated = assignments_service.update_assignment(a.id, title="Updated", xp_reward=50)
            assert updated.title == "Updated"
            assert updated.xp_reward == 50

    def test_toggle_active(self, app):
        with app.app_context():
            a = assignments_service.create_assignment("Test", 0, datetime(2026, 9, 1))
            assert a.is_active is True
            result = assignments_service.toggle_active(a.id)
            assert result is False
            result2 = assignments_service.toggle_active(a.id)
            assert result2 is True

    def test_list_all(self, app):
        with app.app_context():
            assignments_service.create_assignment("A", 0, datetime(2026, 9, 1))
            assignments_service.create_assignment("B", 1, datetime(2026, 9, 2))
            all_a = assignments_service.list_all()
            assert len(all_a) == 2

    def test_submission_stats(self, seeded_app):
        with seeded_app.app_context():
            a = Assignment.query.first()
            stats = assignments_service.get_submission_stats(a.id)
            assert stats["submitted_count"] == 2
            assert stats["graded_count"] == 1
            assert stats["avg_grade"] == 85.0


class TestAnalytics:
    """تست سرویس تحلیل‌ها."""

    def test_overview(self, seeded_app):
        with seeded_app.app_context():
            overview = analytics_service.get_overview()
            assert overview["total_students"] == 3
            assert overview["active_assignments"] >= 1

    def test_assignment_stats(self, seeded_app):
        with seeded_app.app_context():
            stats = analytics_service.get_assignment_stats()
            assert len(stats) >= 1
            assert stats[0]["submitted_count"] == 2

    def test_top_performers(self, seeded_app):
        with seeded_app.app_context():
            top = analytics_service.get_top_performers(limit=2)
            assert len(top) == 2
            # s1 has 100 XP, should be first
            assert top[0]["xp"] >= top[1]["xp"]

    def test_weekly_progress_overview(self, seeded_app):
        with seeded_app.app_context():
            # ساخت هفته‌ها
            from app.models import Week
            for i in range(9):
                if not Week.query.filter_by(number=i).first():
                    db.session.add(Week(number=i, title=f"Week {i}"))
            db.session.commit()

            progress = analytics_service.get_weekly_progress_overview()
            assert len(progress) == 9

    def test_low_engagement(self, seeded_app):
        with seeded_app.app_context():
            # s3 has no XPLog → should be low engagement
            low = analytics_service.get_low_engagement_students(days=1)
            usernames = [s["username"] for s in low]
            assert "s3" in usernames
