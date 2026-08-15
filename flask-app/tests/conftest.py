"""فیکسچرهای مشترک برای تست‌ها — app، DB، و نمونه‌های کاربر.

هر تست از یک DB خالی در حافظه استفاده می‌کند (TestingConfig).
"""
import pytest

from app import create_app, db
from app.models import User


@pytest.fixture()
def app():
    """اپلیکیشن Flask با TestingConfig — DB در حافظه."""
    application = create_app("app.config.TestingConfig")
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """کلاینت تست Flask — بدون login."""
    return app.test_client()


@pytest.fixture()
def admin_user(app):
    """کاربر ادمین پیش‌فرض در DB."""
    from werkzeug.security import generate_password_hash
    user = User(
        username="admin",
        password_hash=generate_password_hash("adminpw"),
        is_admin=True,
        xp=100,
        streak=3,
    )
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture()
def student_user(app):
    """یک دانش‌آموز معمولی در DB."""
    from werkzeug.security import generate_password_hash
    user = User(
        username="ali",
        password_hash=generate_password_hash("studentpw"),
        is_admin=False,
        xp=50,
        streak=2,
    )
    db.session.add(user)
    db.session.commit()
    return user
