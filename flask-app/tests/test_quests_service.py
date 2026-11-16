"""آزمون‌های اعتبارسنجی سرویس مأموریت‌های روزانه (Daily Quests Engine)."""
import pytest
from app import db
from app.models import User, UserDailyQuest
from app.services import quests as quest_service


def test_get_or_create_daily_quests(app, student_user):
    with app.app_context():
        quests = quest_service.get_or_create_daily_quests(student_user.id)
        assert len(quests) == 3

        types = {q["quest_type"] for q in quests}
        assert "flashcard_review" in types
        assert "practice_challenge" in types
        assert "learn_or_resolve" in types

        # فراخوانی دوم در همان روز باید دقیقاً همان ۳ رکورد را برگرداند
        quests2 = quest_service.get_or_create_daily_quests(student_user.id)
        assert len(quests2) == 3
        assert quests[0]["id"] == quests2[0]["id"]


def test_track_quest_progress(app, student_user):
    with app.app_context():
        quest_service.get_or_create_daily_quests(student_user.id)

        # فلش‌کارت تارگت ۵ دارد: ۲ بار مرور
        completed = quest_service.track_quest_progress(student_user.id, "flashcard_review", 2)
        assert completed == []  # هنوز تکمیل نشده

        quests = quest_service.get_or_create_daily_quests(student_user.id)
        fc_quest = next(q for q in quests if q["quest_type"] == "flashcard_review")
        assert fc_quest["current_count"] == 2
        assert fc_quest["is_completed"] is False

        # ۳ بار دیگر مرور -> رسیدن به ۵ و تکمیل
        completed = quest_service.track_quest_progress(student_user.id, "flashcard_review", 3)
        assert len(completed) == 1

        quests_after = quest_service.get_or_create_daily_quests(student_user.id)
        fc_after = next(q for q in quests_after if q["quest_type"] == "flashcard_review")
        assert fc_after["current_count"] == 5
        assert fc_after["is_completed"] is True


def test_claim_quest_reward_and_hearts(app, student_user):
    with app.app_context():
        quests = quest_service.get_or_create_daily_quests(student_user.id)
        learn_quest = next(q for q in quests if q["quest_type"] == "learn_or_resolve")

        # تلاش برای دریافت مأموریت تکمیل‌نشده
        res_fail = quest_service.claim_quest_reward(student_user.id, learn_quest["id"])
        assert res_fail["success"] is False
        assert res_fail["error"] == "not_completed"

        # تکمیل مأموریت
        quest_service.track_quest_progress(student_user.id, "learn_or_resolve", 1)

        user = db.session.get(User, student_user.id)
        user.hearts = 4
        db.session.commit()
        initial_xp = user.xp
        initial_hearts = user.hearts

        # دریافت پاداش
        res_ok = quest_service.claim_quest_reward(user.id, learn_quest["id"])
        assert res_ok["success"] is True
        assert res_ok["xp_reward"] == 20
        assert res_ok["hearts_reward"] == 1

        updated_user = db.session.get(User, user.id)
        assert updated_user.xp == initial_xp + 20
        assert updated_user.hearts == initial_hearts + 1

        # دریافت مجدد باید رد شود (ایدمپوتنت)
        res_repeat = quest_service.claim_quest_reward(user.id, learn_quest["id"])
        assert res_repeat["success"] is False
        assert res_repeat["error"] == "already_claimed"
