import pytest
from datetime import timedelta
from app import db
from app.models import User, XPLog, utc_now
from app.services import hearts as hearts_service


def test_default_hearts_and_drain(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        # پیش‌فرض ۵ قلب دارد
        status = hearts_service.get_user_hearts(user.id)
        assert status["hearts"] == 5
        assert status["cooldown_seconds"] == 0
        assert status["is_out_of_hearts"] is False

        # کسر ۱ قلب
        drained = hearts_service.drain_user_heart(user.id)
        assert drained["hearts"] == 4
        assert drained["is_out_of_hearts"] is False

        # کسر تا صفر
        hearts_service.drain_user_heart(user.id) # 3
        hearts_service.drain_user_heart(user.id) # 2
        hearts_service.drain_user_heart(user.id) # 1
        empty = hearts_service.drain_user_heart(user.id) # 0

        assert empty["hearts"] == 0
        assert empty["is_out_of_hearts"] is True
        assert empty["cooldown_seconds"] > 0
        assert empty["cooldown_seconds"] <= 6 * 3600


def test_auto_refill_after_cooldown(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.hearts = 0
        # شبیه‌سازی خالی شدن قلب در ۶ ساعت و ۵ ثانیه قبل
        user.last_heart_drain = utc_now() - timedelta(hours=6, seconds=5)
        db.session.commit()

        # فراخوانی وضعیت باید شارژ خودکار را فعال کند
        status = hearts_service.get_user_hearts(user.id)
        assert status["hearts"] == 5
        assert status["cooldown_seconds"] == 0
        assert status["is_out_of_hearts"] is False

        # در دیتابیس هم باید ذخیره شده باشد
        refreshed = db.session.get(User, user.id)
        assert refreshed.hearts == 5
        assert refreshed.last_heart_drain is None


def test_refill_with_xp(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.hearts = 0
        user.last_heart_drain = utc_now()
        user.xp = 50
        db.session.commit()

        success, msg, new_xp = hearts_service.refill_user_hearts_with_xp(user.id, "practice:hearts:refill:test")
        assert success is True
        assert new_xp == 30
        assert user.hearts == 5
        assert user.last_heart_drain is None

        # ثبت تراکنش کسر امتیاز در لاگ
        log = XPLog.query.filter_by(user_id=user.id).order_by(XPLog.id.desc()).first()
        assert log is not None
        assert log.amount == -20


def test_refill_with_insufficient_xp(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.hearts = 0
        user.xp = 10
        db.session.commit()

        success, msg, new_xp = hearts_service.refill_user_hearts_with_xp(user.id)
        assert success is False
        assert user.hearts == 0
        assert user.xp == 10


def test_restore_one_heart(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.hearts = 0
        user.last_heart_drain = utc_now()
        db.session.commit()

        status = hearts_service.restore_one_heart(user.id)
        assert status["hearts"] == 1
        assert status["is_out_of_hearts"] is False
        assert user.last_heart_drain is None
