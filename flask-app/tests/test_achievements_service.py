"""آزمون‌های اعتبارسنجی سرویس نشان‌ها و دستاوردها (Achievements Engine)."""
import pytest
from app import db
from app.models import User, Achievement, UserAchievement, XPLog
from app.services import achievements as ach_service


def test_ensure_default_achievements_seeds_database(app):
    with app.app_context():
        count = ach_service.ensure_default_achievements()
        assert count >= 11
        total = Achievement.query.count()
        assert total >= 11

        # بارگذاری مجدد نباید رکوردهای تکراری بسازد (ایدمپوتنت)
        count2 = ach_service.ensure_default_achievements()
        assert count2 == 0
        assert Achievement.query.count() == total


def test_unlock_achievement_idempotent(app, student_user):
    with app.app_context():
        ach_service.ensure_default_achievements()
        aid = "streak-3-days"

        initial_xp = student_user.xp
        unlocked = ach_service.unlock_achievement(student_user.id, aid)
        assert unlocked is True

        # بررسی ثبت در دیتابیس
        rec = UserAchievement.query.filter_by(user_id=student_user.id, achievement_id=aid).first()
        assert rec is not None

        # بررسی اعطای پاداش XP (۱۰ امتیاز برای streak-3-days)
        updated_user = db.session.get(User, student_user.id)
        assert updated_user.xp == initial_xp + 10

        # تلاش مجدد نباید قفل جدید یا XP اضافی ایجاد کند
        unlocked_again = ach_service.unlock_achievement(student_user.id, aid)
        assert unlocked_again is False
        assert updated_user.xp == initial_xp + 10


def test_evaluate_achievements_streak(app, student_user):
    with app.app_context():
        ach_service.ensure_default_achievements()
        user = db.session.get(User, student_user.id)
        user.streak = 3
        db.session.commit()

        unlocked = ach_service.evaluate_achievements(user.id, "streak_updated")
        assert "streak-3-days" in unlocked

        user.streak = 7
        db.session.commit()
        unlocked7 = ach_service.evaluate_achievements(user.id, "streak_updated")
        assert "streak-7-days" in unlocked7


def test_evaluate_achievements_perfect_quiz(app, student_user):
    with app.app_context():
        ach_service.ensure_default_achievements()
        unlocked = ach_service.evaluate_achievements(
            student_user.id, "quiz_completed", {"score": 5, "total": 5, "week": 1}
        )
        assert "perfect-quiz" in unlocked


def test_get_user_achievements_payload(app, student_user):
    with app.app_context():
        ach_service.ensure_default_achievements()
        ach_service.unlock_achievement(student_user.id, "streak-3-days")

        data = ach_service.get_user_achievements(student_user.id)
        assert data["unlocked_count"] >= 1
        assert data["total_count"] >= 11
        assert data["percentage"] > 0

        first = data["achievements"][0]
        assert first["is_unlocked"] is True
        assert first["id"] == "streak-3-days"
