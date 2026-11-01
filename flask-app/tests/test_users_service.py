"""تست‌های سرویس مدیریت کاربران."""
import pytest
from werkzeug.security import check_password_hash

from app import create_app, db
from app.models import User, XPLog
from app.services import users as users_service


@pytest.fixture
def app():
    """ساخت اپ تست با دیتابیس in-memory."""
    app = create_app("app.config.TestingConfig")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


class TestCreateUser:
    """تست ایجاد کاربر جدید."""

    def test_create_user_success(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "pass1234")
            assert user.id is not None
            assert user.username == "ali"
            assert check_password_hash(user.password_hash, "pass1234")
            assert user.is_admin is False
            assert user.xp == 0

    def test_create_duplicate_raises(self, app):
        with app.app_context():
            users_service.create_user("ali", "pass1234")
            with pytest.raises(ValueError):
                users_service.create_user("ali", "otherpass")

    def test_create_user_with_full_features(self, app):
        from app.models import Cohort, Enrollment
        with app.app_context():
            cohort = Cohort.query.first()
            if not cohort:
                from app.models import Course
                course = Course(code="test_c", title="Test Course")
                db.session.add(course)
                db.session.commit()
                cohort = Cohort(course_id=course.id, name="Cohort 1", code="c1")
                db.session.add(cohort)
                db.session.commit()

            user = users_service.create_user(
                username="reza",
                password="pass",
                telegram_id="@reza_cs50",
                is_admin=True,
                is_active=True,
                initial_xp=50,
                initial_streak=3,
                cohort_id=cohort.id,
                cohort_role="ta",
            )
            assert user.id is not None
            assert user.username == "reza"
            assert user.telegram_id == "reza_cs50"
            assert user.is_admin is True
            assert user.is_active is True
            assert user.xp == 50
            assert user.streak == 3

            enr = Enrollment.query.filter_by(user_id=user.id, cohort_id=cohort.id).first()
            assert enr is not None
            assert enr.role == "ta"

    def test_create_user_duplicate_telegram_raises(self, app):
        with app.app_context():
            users_service.create_user("u1", "pass1", telegram_id="tg_user")
            with pytest.raises(ValueError) as exc:
                users_service.create_user("u2", "pass2", telegram_id="@tg_user")
            assert "Telegram" in str(exc.value)


class TestListStudents:
    """تست لیست دانش‌آموزان."""

    def test_excludes_admins(self, app):
        with app.app_context():
            # ساخت ادمین و دانش‌آموز
            admin = User(username="admin", password_hash="x", is_admin=True)
            student = User(username="student1", password_hash="x", is_admin=False, xp=50)
            db.session.add_all([admin, student])
            db.session.commit()

            students = users_service.list_all_students()
            assert len(students) == 1
            assert students[0]["username"] == "student1"
            assert students[0]["xp"] == 50

    def test_includes_last_activity(self, app):
        with app.app_context():
            user = User(username="s1", password_hash="x", xp=10)
            db.session.add(user)
            db.session.commit()

            # بدون XPLog → last_activity = None
            students = users_service.list_all_students()
            assert students[0]["last_activity"] is None

            # با XPLog → last_activity != None
            db.session.add(XPLog(user_id=user.id, amount=5, reason="test"))
            db.session.commit()
            students = users_service.list_all_students()
            assert students[0]["last_activity"] is not None


class TestUpdateUser:
    """تست ویرایش کاربر."""

    def test_update_password(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "oldpass")
            users_service.update_user(user.id, password="newpass")
            refreshed = db.session.get(User, user.id)
            assert check_password_hash(refreshed.password_hash, "newpass")

    def test_adjust_xp_positive(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "pass")
            users_service.update_user(user.id, xp_adjustment=25)
            refreshed = db.session.get(User, user.id)
            assert refreshed.xp == 25

    def test_adjust_xp_negative(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "pass")
            user.xp = 50
            db.session.commit()
            users_service.update_user(user.id, xp_adjustment=-30)
            refreshed = db.session.get(User, user.id)
            assert refreshed.xp == 20

    def test_adjust_xp_negative_floor_zero(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "pass")
            user.xp = 10
            db.session.commit()
            users_service.update_user(user.id, xp_adjustment=-100)
            refreshed = db.session.get(User, user.id)
            assert refreshed.xp == 0


class TestDeleteUser:
    """تست حذف کاربر."""

    def test_delete_user(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "pass")
            uid = user.id
            users_service.delete_user(uid)
            assert db.session.get(User, uid) is None


class TestGetUserDetail:
    """تست جزئیات کاربر."""

    def test_returns_detail(self, app):
        with app.app_context():
            user = users_service.create_user("ali", "pass")
            detail = users_service.get_user_detail(user.id)
            assert detail["user"].username == "ali"
            assert isinstance(detail["submissions"], list)
            assert isinstance(detail["week_progress"], list)
            assert isinstance(detail["xp_logs"], list)
