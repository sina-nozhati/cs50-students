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
