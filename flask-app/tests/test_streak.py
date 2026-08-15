"""تست منطق استریک — services/streak.py.

پوشش‌ها:
    - استریک شروع از مقدار اولیه‌ی DB
    - افزایش استریک (فعالیت متوالی)
    - قطع استریک (فاصله‌ی بیش از ۱ روز)
    - همان روز (تغییر نکردن)
    - اولین فعالیت
"""
from datetime import datetime, date, timedelta, timezone

import pytest

from app import db
from app.models import User, XPLog
from app.services import streak as streak_service
from app.services import xp as xp_service


def _utcnow():
    """UTC-aware datetime برای جلوگیری از deprecation warning."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class TestUpdateStreak:
    """منطق update_streak — فرض:XPLog ثبت شده، سپس صدا زده میشود."""

    def test_get_streak_returns_db_value(self, app, student_user):
        """get_streak فقط مقدار DB را برمیگرداند بدون تغییر."""
        # student_user با streak=2 ساخته شده
        result = streak_service.get_streak(student_user.id)
        assert result == 2

    def test_first_activity_creates_streak(self, app):
        """اولین فعالیت → streak = 1."""
        from werkzeug.security import generate_password_hash
        user = User(
            username="newbie",
            password_hash=generate_password_hash("pw"),
            xp=0,
            streak=0,
        )
        db.session.add(user)
        db.session.commit()

        xp_service.award(user.id, 5, "first ever")
        db.session.refresh(user)
        assert user.streak == 1

    def test_consecutive_days_increments(self, app, student_user):
        """دو روز متوالی → streak باید افزایش یابد."""
        from app.services.streak import _utc_today
        today = _utc_today()

        # ریست streak
        student_user.streak = 0
        db.session.commit()

        # ثبت XPLog برای دیروز (UTC)
        db.session.add(XPLog(
            user_id=student_user.id, amount=5, reason="yesterday",
            timestamp=datetime.combine(today - timedelta(days=1), datetime.min.time()),
        ))
        db.session.commit()

        # ثبت فعالیت امروز
        xp_service.award(student_user.id, 5, "today")
        db.session.refresh(student_user)
        assert student_user.streak == 2

    def test_gap_resets_streak(self, app):
        """فاصله‌ی ۳ روز → streak = 1 (شروع مجدد)."""
        from werkzeug.security import generate_password_hash
        user = User(
            username="gap_user",
            password_hash=generate_password_hash("pw"),
            xp=0,
            streak=5,  # streak بالای قبلی
        )
        db.session.add(user)
        db.session.commit()

        # آخرین فعالیت ۳ روز پیش
        db.session.add(XPLog(
            user_id=user.id, amount=5, reason="old",
            timestamp=_utcnow() - timedelta(days=3),
        ))
        db.session.commit()

        # فعالیت امروز → streak = 1
        xp_service.award(user.id, 5, "new")
        db.session.refresh(user)
        assert user.streak == 1

    def test_same_day_no_double_increment(self, app):
        """دو فعالیت در همان روز → streak فقط ۱ بار زیاد شود."""
        from werkzeug.security import generate_password_hash
        user = User(
            username="same_day",
            password_hash=generate_password_hash("pw"),
            xp=0,
            streak=0,
        )
        db.session.add(user)
        db.session.commit()

        xp_service.award(user.id, 5, "activity 1")
        db.session.refresh(user)
        after_first = user.streak

        xp_service.award(user.id, 3, "activity 2")
        db.session.refresh(user)
        assert user.streak == after_first


class TestGetStreakHistory:
    """تست get_streak_history — ۷ روز اخیر."""

    def test_history_length(self, app, student_user):
        """تاریخچه باید ۷ عنصر داشته باشد (پیش‌فرض)."""
        history = streak_service.get_streak_history(student_user.id, days=7)
        assert len(history) == 7

    def test_history_order(self, app, student_user):
        """تاریخچه از قدیمی به جدید مرتب باشد."""
        history = streak_service.get_streak_history(student_user.id, days=7)
        dates = [h["date"] for h in history]
        assert dates == sorted(dates)

    def test_today_studied_after_xp(self, app, student_user):
        """بعد از گرفتن XP امروز → studied=True برای امروز."""
        # ریست streak
        student_user.streak = 0
        db.session.commit()

        xp_service.award(student_user.id, 5, "test")
        history = streak_service.get_streak_history(student_user.id, days=7)
        today_entries = [h for h in history if h["is_today"]]
        assert len(today_entries) == 1
        assert today_entries[0]["studied"] is True
