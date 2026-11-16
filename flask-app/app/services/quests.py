"""سرویس مأموریت‌های روزانه (Daily Quests Engine).

تولید، رهگیری پیشرفت، اعطای پاداش روزانه و همگام‌سازی با چرخه گیمیفیکیشن.
تمام تاریخ‌ها بر مبنای تقویم UTC سنجیده می‌شوند تا ریسک تداخل ساعت و تقلب حذف شود.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Any

from app import db
from app.models import User, UserDailyQuest, utc_now
from app.services.hearts import restore_one_heart
from app.services.xp import award

DAILY_QUEST_TEMPLATES = [
    {
        "quest_type": "flashcard_review",
        "title_fa": "مرور ۵ فلش‌کارت در جعبه لایتنر",
        "target_count": 5,
        "xp_reward": 10,
        "hearts_reward": 0,
    },
    {
        "quest_type": "practice_challenge",
        "title_fa": "تکمیل ۱ چالش یا کوئیز آموزشی",
        "target_count": 1,
        "xp_reward": 15,
        "hearts_reward": 0,
    },
    {
        "quest_type": "learn_or_resolve",
        "title_fa": "مطالعه ۱ درسنامه یا حل اشتباه در کلینیک",
        "target_count": 1,
        "xp_reward": 20,
        "hearts_reward": 1,
    },
]


def _utc_today() -> date:
    """دریافت تاریخ امروز بر پایه تقویم استاندارد UTC."""
    return datetime.now(timezone.utc).date()


def get_or_create_daily_quests(user_id: int) -> list[dict[str, Any]]:
    """دریافت یا ایجاد خودکار ۳ مأموریت روزانه برای کاربر در روز جاری UTC."""
    today = _utc_today()
    quests = (
        UserDailyQuest.query.filter_by(user_id=user_id, quest_date=today)
        .order_by(UserDailyQuest.id.asc())
        .all()
    )

    if not quests:
        # ساخت مأموریت‌های امروز
        for tmpl in DAILY_QUEST_TEMPLATES:
            q = UserDailyQuest(
                user_id=user_id,
                quest_date=today,
                quest_type=tmpl["quest_type"],
                title_fa=tmpl["title_fa"],
                target_count=tmpl["target_count"],
                current_count=0,
                xp_reward=tmpl["xp_reward"],
                hearts_reward=tmpl["hearts_reward"],
                is_completed=False,
                is_claimed=False,
            )
            db.session.add(q)
        db.session.commit()
        quests = (
            UserDailyQuest.query.filter_by(user_id=user_id, quest_date=today)
            .order_by(UserDailyQuest.id.asc())
            .all()
        )

    out = []
    for q in quests:
        pct = min(100, int((q.current_count / q.target_count) * 100)) if q.target_count > 0 else 0
        out.append({
            "id": q.id,
            "quest_type": q.quest_type,
            "title_fa": q.title_fa,
            "target_count": q.target_count,
            "current_count": q.current_count,
            "progress_pct": pct,
            "xp_reward": q.xp_reward,
            "hearts_reward": q.hearts_reward,
            "is_completed": q.is_completed,
            "completed_at": q.completed_at.isoformat() if q.completed_at else None,
            "is_claimed": q.is_claimed,
        })
    return out


def track_quest_progress(
    user_id: int, quest_type: str, increment: int = 1
) -> list[int]:
    """افزایش پیشرفت مأموریت‌های منطبق روز جاری کاربر.

    Returns:
        شناسه‌های مأموریت‌هایی که با این اکشن تکمیل شدند.
    """
    today = _utc_today()
    quests = UserDailyQuest.query.filter_by(
        user_id=user_id, quest_date=today, quest_type=quest_type
    ).all()

    completed_ids = []
    for q in quests:
        if q.is_completed:
            continue
        q.current_count = min(q.target_count, q.current_count + increment)
        if q.current_count >= q.target_count:
            q.is_completed = True
            q.completed_at = utc_now()
            completed_ids.append(q.id)

    if quests:
        db.session.commit()
    return completed_ids


def claim_quest_reward(user_id: int, quest_id: int) -> dict[str, Any]:
    """دریافت پاداش یک مأموریت تکمیل‌شده (ایدمپوتنت)."""
    quest = db.session.get(UserDailyQuest, quest_id)
    if not quest or quest.user_id != user_id:
        return {"success": False, "error": "quest_not_found", "message": "مأموریت یافت نشد."}

    if not quest.is_completed:
        return {
            "success": False,
            "error": "not_completed",
            "message": "این مأموریت هنوز تکمیل نشده است.",
        }

    if quest.is_claimed:
        return {
            "success": False,
            "error": "already_claimed",
            "message": "پاداش این مأموریت قبلاً دریافت شده است.",
        }

    # اعطای XP
    award(user_id, quest.xp_reward, f"quest:{quest.id}:claim")

    # اعطای قلب در صورت وجود
    if quest.hearts_reward > 0:
        restore_one_heart(user_id)

    quest.is_claimed = True
    db.session.commit()

    # بررسی تکمیل همه مأموریت‌های امروز برای مدال quest-champion
    today = _utc_today()
    all_today = UserDailyQuest.query.filter_by(user_id=user_id, quest_date=today).all()
    if all_today and all(q.is_claimed for q in all_today):
        from app.services.achievements import evaluate_achievements
        evaluate_achievements(user_id, "daily_quests_all_claimed")

    user = db.session.get(User, user_id)
    return {
        "success": True,
        "message": f"پاداش دریافت شد: {quest.xp_reward} XP" + (f" و {quest.hearts_reward} قلب!" if quest.hearts_reward else "."),
        "xp_reward": quest.xp_reward,
        "hearts_reward": quest.hearts_reward,
        "new_xp": user.xp if user else 0,
        "new_hearts": user.hearts if user else 5,
    }
