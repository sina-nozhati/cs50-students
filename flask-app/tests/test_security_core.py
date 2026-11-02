"""تست‌های حیاتی امنیت و مسیر LEARN — فاز ۱/۲ Master PRD."""
from datetime import datetime, timedelta

from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Assignment, Submission, Resource, Week, XPLog
from app.services import xp as xp_service
from app.services import submissions as sub_service
from app.services import progress as progress_service
from app.services import resources as res_service
from app.services import notifications as notif_service
from app.services import analytics as analytics_service


def _student(username="stu"):
    u = User(
        username=username,
        password_hash=generate_password_hash("pw"),
        is_admin=False,
        xp=0,
        streak=0,
        is_active=True,
    )
    db.session.add(u)
    db.session.commit()
    return u


class TestXpIdempotency:
    def test_award_same_reason_once(self, app):
        with app.app_context():
            u = _student()
            assert xp_service.award(u.id, 5, "kb:read:week:0") is True
            assert xp_service.award(u.id, 5, "kb:read:week:0") is False
            db.session.refresh(u)
            assert u.xp == 5
            assert XPLog.query.filter_by(user_id=u.id).count() == 1


class TestSubmissionResubmit:
    def test_create_awards_once_and_resubmit_no_xp(self, app):
        with app.app_context():
            u = _student()
            a = Assignment(
                title="P0",
                week=0,
                due_date=datetime.utcnow() + timedelta(days=3),
                xp_reward=20,
                is_active=True,
            )
            db.session.add(a)
            db.session.commit()

            sub = sub_service.create_submission(
                u.id, a.id, "https://github.com/u/repo"
            )
            db.session.refresh(u)
            assert u.xp == 20

            updated = sub_service.update_submission_url(
                u.id, a.id, "https://github.com/u/repo2"
            )
            assert updated.github_url.endswith("repo2")
            db.session.refresh(u)
            assert u.xp == 20
            assert XPLog.query.filter_by(user_id=u.id).count() == 1


class TestCertificateUsesKbRead:
    def test_progress_without_quiz(self, app):
        with app.app_context():
            u = _student()
            db.session.add(Week(number=0, title="W0", is_published=True))
            db.session.add(Week(number=1, title="W1", is_published=True))
            db.session.commit()
            assert progress_service.mark_kb_read(u.id, 0) is True
            cert = progress_service.get_certificate_progress(u.id)
            assert cert["completed_weeks"] == 1
            assert cert["criterion"] == "kb_read"
            assert cert["current_week"] == 1


class TestResourceAccess:
    def test_unpublished_404(self, app):
        with app.app_context():
            r = Resource(
                week=0,
                filename="notes.pdf",
                display_name="جزوه",
                category="notes",
                is_published=False,
            )
            db.session.add(r)
            db.session.commit()
            try:
                res_service.get_published_or_404(r.id)
                assert False, "expected 404"
            except Exception as e:
                assert getattr(e, "code", None) == 404


class TestNotificationsOnGrade:
    def test_grade_creates_notification(self, app):
        with app.app_context():
            u = _student()
            a = Assignment(
                title="P0",
                week=0,
                due_date=datetime.utcnow() + timedelta(days=1),
                xp_reward=10,
            )
            db.session.add(a)
            db.session.commit()
            sub = sub_service.create_submission(
                u.id, a.id, "https://github.com/u/p0"
            )
            sub_service.grade(sub.id, 90, "خوب بود")
            assert notif_service.unread_count(u.id) == 1
            assert sub.graded_at is not None


class TestAnalyticsFr10:
    def test_timing_and_median(self, app):
        with app.app_context():
            u = _student()
            due = datetime.utcnow() + timedelta(days=2)
            a = Assignment(title="A", week=0, due_date=due, xp_reward=10)
            db.session.add(a)
            db.session.commit()
            sub = Submission(
                student_id=u.id,
                assignment_id=a.id,
                github_url="https://github.com/u/a",
                submitted_at=datetime.utcnow(),
                grade=80,
                feedback="ok",
                graded_at=datetime.utcnow() + timedelta(hours=4),
            )
            db.session.add(sub)
            db.session.commit()
            overview = analytics_service.get_overview()
            assert overview["on_time_count"] >= 1
            assert overview["median_feedback_hours"] == 4.0


class TestInactiveUserLogin:
    def test_inactive_cannot_login(self, app, client):
        with app.app_context():
            u = User(
                username="blocked",
                password_hash=generate_password_hash("secret"),
                is_active=False,
            )
            db.session.add(u)
            db.session.commit()

        resp = client.post(
            "/login",
            data={"username": "blocked", "password": "secret"},
            follow_redirects=True,
        )
        assert resp.status_code == 200
        assert "اشتباه".encode("utf-8") in resp.data or b"login" in resp.data.lower()


class TestDownloadRouteRequiresLogin:
    def test_download_redirects_when_anonymous(self, app, client):
        with app.app_context():
            r = Resource(
                week=0,
                filename="x.pdf",
                display_name="x",
                category="notes",
                is_published=True,
            )
            db.session.add(r)
            db.session.commit()
            rid = r.id
        resp = client.get(f"/resources/file/{rid}/download")
        assert resp.status_code in (302, 401)
