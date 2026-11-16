"""سرویس مدیریت نشان‌ها و دستاوردهای آموزشی (Badges & Achievements Engine).

این سرویس ارزیابی رویدادمحور دستاوردها، ثبت در دیتابیس، اعطای پاداش XP ایدمپوتنت
و ارسال اعلان‌های تبریک را به صورت یکپارچه بر عهده دارد.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app import db
from app.models import (
    Achievement,
    Notification,
    QuizAttempt,
    StreakFreeze,
    StudentMistake,
    Submission,
    User,
    UserAchievement,
    UserDailyQuest,
    XPLog,
    utc_now,
)
from app.content.kb_repo import kb_root
from app.services.xp import award

GLOBAL_ACHIEVEMENTS: list[dict[str, Any]] = [
    {
        "id": "streak-3-days",
        "title_fa": "جرقه اولیه",
        "description_fa": "حفظ استریک به مدت ۳ روز مداوم.",
        "icon": "zap",
        "badge_variant": "warning",
        "tier": "bronze",
        "xp_bonus": 10,
        "week": None,
        "basis": "consistency",
    },
    {
        "id": "streak-7-days",
        "title_fa": "اراده فولادین",
        "description_fa": "حفظ استریک به مدت ۷ روز مداوم.",
        "icon": "flame",
        "badge_variant": "crimson",
        "tier": "silver",
        "xp_bonus": 25,
        "week": None,
        "basis": "consistency",
    },
    {
        "id": "streak-14-days",
        "title_fa": "عادت پایدار",
        "description_fa": "حفظ استریک به مدت ۱۴ روز مداوم.",
        "icon": "target",
        "badge_variant": "success",
        "tier": "gold",
        "xp_bonus": 50,
        "week": None,
        "basis": "consistency",
    },
    {
        "id": "streak-30-days",
        "title_fa": "افسانه استریک",
        "description_fa": "حفظ استریک به مدت ۳۰ روز مداوم.",
        "icon": "trophy",
        "badge_variant": "crimson",
        "tier": "platinum",
        "xp_bonus": 100,
        "week": None,
        "basis": "consistency",
    },
    {
        "id": "mistake-conqueror",
        "title_fa": "فاتح خطاها",
        "description_fa": "حل و رفع ۵ اشتباه در جعبه اشتباهات آموزشی.",
        "icon": "shield-check",
        "badge_variant": "success",
        "tier": "silver",
        "xp_bonus": 20,
        "week": None,
        "basis": "mastery",
    },
    {
        "id": "perfect-quiz",
        "title_fa": "نمره صد",
        "description_fa": "کسب نمره کامل ۱۰۰٪ در آزمون تسلط یک هفته.",
        "icon": "award",
        "badge_variant": "crimson",
        "tier": "gold",
        "xp_bonus": 30,
        "week": None,
        "basis": "mastery",
    },
    {
        "id": "flashcard-50",
        "title_fa": "استاد حافظه",
        "description_fa": "مرور موفق ۵۰ فلش‌کارت در جعبه‌های لایتنر.",
        "icon": "brain",
        "badge_variant": "warning",
        "tier": "silver",
        "xp_bonus": 25,
        "week": None,
        "basis": "mastery",
    },
    {
        "id": "streak-freeze-shield",
        "title_fa": "سپر یخی",
        "description_fa": "خرید یا فعال‌سازی اولین محافظ استریک برای روزهای اضطراری.",
        "icon": "shield",
        "badge_variant": "muted",
        "tier": "bronze",
        "xp_bonus": 10,
        "week": None,
        "basis": "engagement",
    },
    {
        "id": "quest-champion",
        "title_fa": "قهرمان روزانه",
        "description_fa": "تکمیل تمام مأموریت‌های روزانه در یک روز.",
        "icon": "check-circle",
        "badge_variant": "success",
        "tier": "silver",
        "xp_bonus": 20,
        "week": None,
        "basis": "engagement",
    },
    {
        "id": "first-submission",
        "title_fa": "اولین پرواز",
        "description_fa": "ارسال نخستین تکلیف یا پروژه در سامانه.",
        "icon": "send",
        "badge_variant": "muted",
        "tier": "bronze",
        "xp_bonus": 15,
        "week": None,
        "basis": "mastery",
    },
    {
        "id": "quiz-champion",
        "title_fa": "کوییزباز",
        "description_fa": "قبولی در ۳ آزمون تسلط هفتگی با نمره قبولی.",
        "icon": "star",
        "badge_variant": "crimson",
        "tier": "gold",
        "xp_bonus": 40,
        "week": None,
        "basis": "mastery",
    },
]


def ensure_default_achievements() -> int:
    """بارگذاری و کاشت اولیه تمام ۲۳ نشان استاندارد در پایگاه داده."""
    count = 0

    # ۱. بارگذاری نشان‌های محلی هفته ۰ از JSON
    try:
        root = kb_root()
        path = root / "anzali-fa" / "gamification" / "achievements.json"
        if path.is_file():
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            for item in data.get("achievements", []):
                aid = item.get("id")
                if not aid:
                    continue
                exist = db.session.get(Achievement, aid)
                if not exist:
                    ach = Achievement(
                        id=aid,
                        title_fa=item.get("title_fa", ""),
                        description_fa=item.get("description_fa", ""),
                        icon=item.get("icon", "award"),
                        badge_variant=item.get("badge_variant", "crimson"),
                        tier="bronze" if item.get("badge_variant") == "muted" else "silver",
                        criteria_json=item.get("criteria"),
                        xp_bonus=item.get("xp_bonus", 0),
                        week=item.get("week", 0),
                        basis=item.get("basis", "mastery"),
                    )
                    db.session.add(ach)
                    count += 1
    except Exception:
        pass

    # ۲. بارگذاری نشان‌های عمومی سراسری
    for item in GLOBAL_ACHIEVEMENTS:
        aid = item["id"]
        exist = db.session.get(Achievement, aid)
        if not exist:
            ach = Achievement(
                id=aid,
                title_fa=item["title_fa"],
                description_fa=item["description_fa"],
                icon=item["icon"],
                badge_variant=item["badge_variant"],
                tier=item["tier"],
                criteria_json={"type": "event_trigger", "event": aid},
                xp_bonus=item["xp_bonus"],
                week=item["week"],
                basis=item["basis"],
            )
            db.session.add(ach)
            count += 1

    if count > 0:
        db.session.commit()
    return count


def unlock_achievement(user_id: int, achievement_id: str) -> bool:
    """بازگشایی یک نشان برای کاربر، اعطای پاداش XP و ارسال نوتیفیکیشن.

    عملیات ایدمپوتنت است: در صورت بازگشایی قبلی، هیچ تغییری رخ نمی‌دهد.
    """
    user = db.session.get(User, user_id)
    achievement = db.session.get(Achievement, achievement_id)
    if not user or not achievement:
        return False

    already = (
        UserAchievement.query.filter_by(user_id=user_id, achievement_id=achievement_id).first()
    )
    if already:
        return False

    # ثبت نشان
    unlock_rec = UserAchievement(
        user_id=user_id,
        achievement_id=achievement_id,
        unlocked_at=utc_now(),
    )
    db.session.add(unlock_rec)

    # پاداش XP (ایدمپوتنت)
    if achievement.xp_bonus > 0:
        award(user_id, achievement.xp_bonus, f"achievement:{achievement_id}:unlock")

    # ارسال اعلان به کاربر
    notif = Notification(
        user_id=user_id,
        title="دستاورد جدید باز شد! 🏆",
        body=f"تبریک! شما نشان «{achievement.title_fa}» را کسب کردید: {achievement.description_fa}",
        link="/dashboard",
        created_at=utc_now(),
    )
    db.session.add(notif)
    db.session.commit()
    return True


def evaluate_achievements(
    user_id: int, event_name: str, context: dict[str, Any] | None = None
) -> list[str]:
    """ارزیابی هوشمند شروط نشان‌ها بر اساس رویداد رخ‌داده.

    رویدادهای پشتیبانی‌شده:
      - 'streak_updated': استریک کاربر تغییر کرده
      - 'quiz_completed': کوییز با نمره به اتمام رسیده
      - 'flashcard_reviewed': فلش‌کارت مرور شده
      - 'challenge_completed': چالش کدنویسی حل شده
      - 'mistake_resolved': اشتباهی در کلینیک حل شده
      - 'submission_accepted': تکلیفی تحویل شده
      - 'streak_freeze_bought': محافظ استریک خریداری شده
      - 'daily_quests_all_claimed': همه کوئست‌های امروز دریافت شده
    """
    ctx = context or {}
    user = db.session.get(User, user_id)
    if not user:
        return []

    unlocked_now: list[str] = []

    if event_name == "streak_updated":
        s = user.streak or 0
        if s >= 3 and unlock_achievement(user_id, "streak-3-days"):
            unlocked_now.append("streak-3-days")
        if s >= 7 and unlock_achievement(user_id, "streak-7-days"):
            unlocked_now.append("streak-7-days")
        if s >= 14 and unlock_achievement(user_id, "streak-14-days"):
            unlocked_now.append("streak-14-days")
        if s >= 30 and unlock_achievement(user_id, "streak-30-days"):
            unlocked_now.append("streak-30-days")

    elif event_name == "quiz_completed":
        score = ctx.get("score", 0)
        total = ctx.get("total", 0)
        week = ctx.get("week", 0)
        pct = (score / total) if total > 0 else 0.0

        if pct >= 1.0 and unlock_achievement(user_id, "perfect-quiz"):
            unlocked_now.append("perfect-quiz")

        if week == 0 and pct >= 0.8 and unlock_achievement(user_id, "w00-ach-week-mastery"):
            unlocked_now.append("w00-ach-week-mastery")

        # کوییزباز: حداقل ۳ آزمون با درصد بالای ۷۰٪
        passed_attempts = (
            QuizAttempt.query.filter_by(user_id=user_id, is_completed=True)
            .filter(QuizAttempt.score >= (QuizAttempt.total_questions * 0.7))
            .count()
        )
        if passed_attempts >= 3 and unlock_achievement(user_id, "quiz-champion"):
            unlocked_now.append("quiz-champion")

    elif event_name == "flashcard_reviewed":
        fc_logs = XPLog.query.filter_by(user_id=user_id).filter(XPLog.reason.like("flashcard:%:reviewed")).count()
        if fc_logs >= 50 and unlock_achievement(user_id, "flashcard-50"):
            unlocked_now.append("flashcard-50")

    elif event_name == "challenge_completed":
        # نخستین گام: حل اولین واحد
        if unlock_achievement(user_id, "w00-ach-first-unit"):
            unlocked_now.append("w00-ach-first-unit")

        cid = ctx.get("challenge_id", "")
        if "binary" in cid.lower() or "bit" in cid.lower():
            if unlock_achievement(user_id, "w00-ach-binary"):
                unlocked_now.append("w00-ach-binary")

    elif event_name == "mistake_resolved":
        resolved_cnt = (
            StudentMistake.query.filter_by(user_id=user_id, is_resolved=True).count()
        )
        if resolved_cnt >= 5 and unlock_achievement(user_id, "mistake-conqueror"):
            unlocked_now.append("mistake-conqueror")

    elif event_name == "submission_accepted":
        if unlock_achievement(user_id, "first-submission"):
            unlocked_now.append("first-submission")

    elif event_name == "streak_freeze_bought":
        if unlock_achievement(user_id, "streak-freeze-shield"):
            unlocked_now.append("streak-freeze-shield")

    elif event_name == "daily_quests_all_claimed":
        if unlock_achievement(user_id, "quest-champion"):
            unlocked_now.append("quest-champion")

    return unlocked_now


def get_user_achievements(user_id: int) -> dict[str, Any]:
    """دریافت کل کاتالوگ دستاوردها همراه با وضعیت بازگشایی برای کاربر."""
    ensure_default_achievements()

    all_achs = Achievement.query.order_by(Achievement.week.asc().nullsfirst(), Achievement.id.asc()).all()
    user_unlocks = {
        rec.achievement_id: rec.unlocked_at
        for rec in UserAchievement.query.filter_by(user_id=user_id).all()
    }

    tier_order = {"platinum": 4, "gold": 3, "silver": 2, "bronze": 1}

    items = []
    unlocked_count = 0
    for ach in all_achs:
        unlocked = ach.id in user_unlocks
        if unlocked:
            unlocked_count += 1
        items.append({
            "id": ach.id,
            "title_fa": ach.title_fa,
            "description_fa": ach.description_fa,
            "icon": ach.icon,
            "badge_variant": ach.badge_variant,
            "tier": ach.tier,
            "xp_bonus": ach.xp_bonus,
            "week": ach.week,
            "basis": ach.basis,
            "is_unlocked": unlocked,
            "unlocked_at": user_unlocks.get(ach.id).isoformat() if unlocked else None,
            "tier_rank": tier_order.get(ach.tier, 1),
        })

    # مرتب‌سازی: اول بازشده‌ها، سپس بالاترین سطح (Tier)
    items.sort(key=lambda x: (not x["is_unlocked"], -x["tier_rank"], x["title_fa"]))

    return {
        "unlocked_count": unlocked_count,
        "total_count": len(items),
        "percentage": round((unlocked_count / len(items) * 100), 1) if items else 0.0,
        "achievements": items,
    }
