"""سرویس موتور تمرین‌های تعاملی شبیه دولینگو (Duo-Style Practice Engine).

این سرویس چالش‌های آموزشی ساختاریافته (Token Tap, Parsons, Spot Bug, Predict Output)
را از فایلهای JSON هفته بارگذاری کرده و وضعیت تلاش‌ها، امتیاز XP، استریک و رویدادهای
یادگیری را به شکل اتمیک مدیریت میکند.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from app import db
from app.models import User, ExerciseAttempt, LearningEvent, WeekProgress
from app.content import kb_repo
from app.services import xp as xp_service
from app.services import streak as streak_service
from app.services import events as event_service
from app.services import engagement as engagement_service
from app.services import diagnostics as diag_service


def get_challenges_file_path(week: int) -> Path:
    """مسیر فایل challenges.json برای یک هفته مشخص."""
    return kb_repo.get_anzali_week_dir(week) / "challenges.json"


def has_practice_session(week: int) -> bool:
    """بررسی سریع وجود چالش‌های تمرینی معتبر برای یک هفته."""
    path = get_challenges_file_path(week)
    if not path.is_file():
        return False
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        challenges = data.get("challenges", [])
        return bool(challenges and isinstance(challenges, list) and len(challenges) > 0)
    except Exception:
        return False


def load_practice_session(week: int, user_id: int | None = None) -> dict[str, Any] | None:
    """بارگذاری داده‌های چالش‌های یک هفته به همراه وضعیت تکمیل کاربر."""
    path = get_challenges_file_path(week)
    if not path.is_file():
        return None

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return None

    challenges = data.get("challenges", [])
    if not challenges:
        return None

    # بررسی وضعیت حل چالش‌ها توسط کاربر
    user_attempts: dict[str, ExerciseAttempt] = {}
    if user_id:
        attempts = ExerciseAttempt.query.filter_by(user_id=user_id, week=week).all()
        user_attempts = {att.exercise_id: att for att in attempts}

    formatted_challenges = []
    for ch in challenges:
        cid = ch.get("id")
        attempt = user_attempts.get(cid)
        is_completed = bool(attempt and attempt.is_correct)

        ch_copy = dict(ch)
        ch_copy["is_completed"] = is_completed
        formatted_challenges.append(ch_copy)

    return {
        "week": week,
        "title": data.get("title", f"تمرین تعاملی هفته {week}"),
        "xp_reward_session": data.get("xp_reward_session", 20),
        "challenges": formatted_challenges,
        "total_challenges": len(formatted_challenges),
    }


def verify_challenge_answer(challenge: dict[str, Any], user_answer: Any) -> tuple[bool, str]:
    """اعتبارسنجی پاسخ کاربر با توجه به نوع چالش."""
    ch_type = challenge.get("type")
    explanation = challenge.get("explanation", "")

    if ch_type == "token_tap":
        expected = challenge.get("expected_answer", [])
        if isinstance(user_answer, list):
            # مقایسه لیست رشته‌ها با نادیده‌گرفتن فاصله‌های اضافی
            norm_user = [str(x).strip() for x in user_answer]
            norm_exp = [str(x).strip() for x in expected]
            return (norm_user == norm_exp, explanation)
        elif isinstance(user_answer, str):
            norm_user = [x.strip() for x in user_answer.split() if x.strip()]
            norm_exp = [str(x).strip() for x in expected]
            return (norm_user == norm_exp, explanation)

    elif ch_type == "parsons":
        expected_order = challenge.get("correct_order", [])
        if isinstance(user_answer, list):
            norm_user = [str(x).strip() for x in user_answer]
            norm_exp = [str(x).strip() for x in expected_order]
            return (norm_user == norm_exp, explanation)

    elif ch_type == "spot_bug":
        bug_index = challenge.get("bug_line_index")
        try:
            return (int(user_answer) == int(bug_index), explanation)
        except (ValueError, TypeError):
            return (False, explanation)

    elif ch_type == "predict_output":
        acceptable = [str(x).strip().lower() for x in challenge.get("acceptable_answers", [])]
        user_str = str(user_answer).strip().lower().replace("'", "").replace('"', "")
        # چک مستقیم یا با نادیده‌گرفتن کوتیشن
        matches = (user_str in acceptable) or any(user_str == acc.replace("'", "").replace('"', "") for acc in acceptable)
        return (matches, explanation)

    elif ch_type == "mcq":
        options = challenge.get("options", [])
        correct_id = None
        for opt in options:
            if opt.get("correct"):
                correct_id = opt.get("id")
                break
        return (str(user_answer).strip() == str(correct_id), explanation)

    return (False, "نوع چالش نامعتبر است.")


def submit_challenge_attempt(
    user_id: int,
    week: int,
    challenge_id: str,
    user_answer: Any,
    hints_used: int = 0
) -> dict[str, Any]:
    """ثبت تلاش پاسخ‌دهی به یک چالش، ثبت لاگ رویداد و اعطای XP."""
    session_data = load_practice_session(week, user_id)
    if not session_data:
        return {"success": False, "message": "جلسه تمرین یافت نشد."}

    target_challenge = None
    for ch in session_data["challenges"]:
        if ch["id"] == challenge_id:
            target_challenge = ch
            break

    if not target_challenge:
        return {"success": False, "message": "چالش مورد نظر یافت نشد."}

    is_correct, explanation = verify_challenge_answer(target_challenge, user_answer)

    # ثبت تلاش در ExerciseAttempt
    attempt = ExerciseAttempt.query.filter_by(user_id=user_id, exercise_id=challenge_id).first()
    first_time_correct = False

    str_answer = json.dumps(user_answer, ensure_ascii=False) if not isinstance(user_answer, str) else user_answer

    if attempt is None:
        attempt = ExerciseAttempt(
            user_id=user_id,
            week=week,
            exercise_id=challenge_id,
            is_correct=is_correct,
            submitted_answer=str_answer,
            hints_used=hints_used,
        )
        db.session.add(attempt)
        if is_correct:
            first_time_correct = True
    else:
        attempt.submitted_answer = str_answer
        attempt.hints_used = max(attempt.hints_used, hints_used)
        if not attempt.is_correct and is_correct:
            attempt.is_correct = True
            first_time_correct = True

    db.session.commit()

    xp_awarded = 0
    if first_time_correct:
        reward = target_challenge.get("xp_reward", 5)
        # در صورت راهنمایی بالا، ۱ امتیاز کسر شود اما حداقل ۳ XP داده شود
        if hints_used >= 2 and reward > 3:
            reward -= 1

        reason = f"practice:{challenge_id}:pass"
        xp_service.award(user_id, reward, reason)
        xp_awarded = reward

    # ثبت رویداد یادگیری در سیستم تله‌متری مجاز
    event_service.log_event(
        user_id,
        "exercise_attempt",
        {
            "week": week,
            "challenge_id": challenge_id,
            "is_correct": is_correct,
            "hints_used": hints_used,
            "first_time_correct": first_time_correct,
        }
    )

    # ثبت یا رفع خطا در جعبه اشتباهات و پروفایل تشخیصی
    if not is_correct:
        expected_ans = (
            target_challenge.get("expected_answer")
            or target_challenge.get("correct_order")
            or target_challenge.get("bug_line_index")
            or target_challenge.get("acceptable_answers")
        )
        diag_service.record_mistake(
            user_id=user_id,
            week=week,
            source="practice",
            item_id=challenge_id,
            item_title=target_challenge.get("title"),
            concept_tag=target_challenge.get("concept_tag") or target_challenge.get("type", "practice"),
            user_answer=user_answer,
            expected_answer=expected_ans,
            explanation=explanation,
        )
    else:
        diag_service.resolve_mistake(user_id=user_id, item_id=challenge_id)

    user = db.session.get(User, user_id)
    current_xp = user.xp if user else 0
    current_streak = user.streak if user else 0

    return {
        "success": True,
        "is_correct": is_correct,
        "xp_awarded": xp_awarded,
        "explanation": explanation,
        "current_xp": current_xp,
        "current_streak": current_streak,
    }


def complete_practice_session(
    user_id: int,
    week: int,
    summary: dict[str, Any]
) -> dict[str, Any]:
    """ثبت پایان سشن تمرین، لاگ رویداد session_end و محاسبه احتمال بازگشت."""
    completed_count = summary.get("completed_count", 0)
    incorrect_count = summary.get("incorrect_count", 0)
    time_spent = summary.get("time_spent_seconds", 0)
    entry_point = summary.get("entry_point", "direct")

    # ثبت رویداد session_end
    event_service.log_event(
        user_id,
        "session_end",
        {
            "week": week,
            "type": "practice_runner",
            "completed_count": completed_count,
            "incorrect_count": incorrect_count,
            "time_spent_seconds": time_spent,
            "entry_point": entry_point,
        }
    )

    # به‌روزرسانی امتیاز بازگشت و کاهش خطر ریزش
    engagement_service.compute_user_engagement(user_id)

    user = db.session.get(User, user_id)
    return {
        "success": True,
        "message": "جلسه تمرین با موفقیت تکمیل شد!",
        "current_xp": user.xp if user else 0,
        "current_streak": user.streak if user else 0,
    }
