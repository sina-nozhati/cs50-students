"""آزمون‌های اعتبارسنجی محافظ استریک (Streak Freeze)."""
from datetime import datetime, date, timedelta, timezone
import pytest
from app import db
from app.models import User, StreakFreeze, XPLog, utc_now
from app.services import streak as streak_service
from app.services import xp as xp_service


def test_buy_streak_freeze_success(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.xp = 150
        db.session.commit()
        initial_xp = user.xp

        res = streak_service.buy_streak_freeze(user.id)
        assert res["success"] is True
        assert res["freezes_count"] == 1
        assert res["new_xp"] == initial_xp - 50

        updated = db.session.get(User, user.id)
        assert updated.xp == initial_xp - 50
        assert updated.streak_freezes_count == 1


def test_buy_streak_freeze_insufficient_xp(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.xp = 30
        db.session.commit()

        res = streak_service.buy_streak_freeze(user.id)
        assert res["success"] is False
        assert res["error"] == "insufficient_xp"
        assert user.streak_freezes_count == 0


def test_buy_streak_freeze_max_limit(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.xp = 200
        db.session.commit()

        # خرید ۲ فریز
        res1 = streak_service.buy_streak_freeze(user.id)
        assert res1["success"] is True

        res2 = streak_service.buy_streak_freeze(user.id)
        assert res2["success"] is True

        user_reloaded = db.session.get(User, user.id)
        assert user_reloaded.streak_freezes_count == 2

        # تلاش برای خرید سوم باید رد شود
        res3 = streak_service.buy_streak_freeze(user.id)
        assert res3["success"] is False
        assert res3["error"] == "limit_reached"


def test_update_streak_consumes_freeze_on_missed_day(app, student_user):
    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.xp = 100
        user.streak = 5
        db.session.commit()

        # خرید ۱ فریز
        streak_service.buy_streak_freeze(user.id)
        assert user.streak_freezes_count == 1

        today = datetime.now(timezone.utc).date()
        # فعالیت ۲ روز قبل (یعنی دیروز غیبت داشته)
        two_days_ago = datetime.combine(today - timedelta(days=2), datetime.min.time())

        log = XPLog(
            user_id=user.id,
            amount=10,
            reason="test:activity",
            timestamp=two_days_ago,
        )
        db.session.add(log)
        db.session.commit()

        # کاربر امروز فعالیت جدید می‌کند و award صدا می‌زند
        xp_service.award(user.id, 5, "test:today:award")

        updated = db.session.get(User, user.id)
        # به جای ریست شدن به ۱، استریک باید ادامه یافته باشد: 5 + 1 = 6
        assert updated.streak == 6
        # فریز باید مصرف شده باشد
        assert updated.streak_freezes_count == 0
        used_freeze = StreakFreeze.query.filter_by(user_id=user.id).first()
        assert used_freeze.used_on == today - timedelta(days=1)
