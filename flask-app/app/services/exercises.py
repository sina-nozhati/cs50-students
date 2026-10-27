"""مدیریت و بانک تمرین‌های هفتگی (مثل قطعه‌کد جاافتاده و پرسش‌های کدنویسی)."""
import json
from datetime import datetime
from app import db
from app.models import ExerciseAttempt
from app.services import xp as xp_service
from app.services import streak as streak_service

# بانک تمرین‌های هفتگی CS50x (هفته ۰ تا ۲ به عنوان نمونه‌های اول)
EXERCISES = {
    "w00-code-binary": {
        "id": "w00-code-binary",
        "week": 0,
        "title": "محاسبه ارزش بیت‌ها (دودویی)",
        "type": "fill_in_the_blank",
        "instruction": "کد زیر برای نمایش عدد ۵ در مبنای ۲ (۱۰۱) ناقص است. جای خالی ___ را کامل کنید:",
        "code_snippet": "# 5 in binary is 4 + 0 + 1\nbits = [1, 0, 1]\nvalue = (bits[0] * 4) + (bits[1] * ___) + (bits[2] * 1)\nprint(value)",
        "expected_answer": "2",
        "acceptable_answers": ["2", "2.0"],
        "hint": "در مبنای ۲، ارزش مکانی بیت‌ها به ترتیب از راست به چپ: ۲ به توان ۰ (۱)، ۲ به توان ۱ (۲) و ۲ به توان ۲ (۴) است.",
        "xp_reward": 5,
        "explanation": "آفرین! جایگاه دوم در مبنای دو ارزش ۲^۱ = ۲ دارد. بنابراین bits[1] در ۲ ضرب می‌شود."
    },
    "w01-code-mario": {
        "id": "w01-code-mario",
        "week": 1,
        "title": "حلقه پرینت پله‌های ماریو (C)",
        "type": "fill_in_the_blank",
        "instruction": "می‌خواهیم ۳ علامت # چاپ کنیم. شرط پایان حلقه for را مشخص کنید:",
        "code_snippet": "for (int i = 0; i ___ 3; i++)\n{\n    printf(\"#\");\n}\nprintf(\"\\n\");",
        "expected_answer": "<",
        "acceptable_answers": ["<", "<="],
        "hint": "حلقه از 0 شروع می‌شود، پس برای 3 بار تکرار باید تا وقتی i کمتر از 3 است ادامه یابد.",
        "xp_reward": 5,
        "explanation": "دقیقاً! وقتی i از 0 شروع می‌شود، با شرط i < 3 به ازای مقادیر 0 و 1 و 2 حلقه دقیقاً ۳ بار اجرا می‌شود."
    },
    "w02-code-caesar": {
        "id": "w02-code-caesar",
        "week": 2,
        "title": "فرمول رمز سزار",
        "type": "fill_in_the_blank",
        "instruction": "برای شیفت دادن کاراکتر c به اندازه key در الفبای ۲۶ حرفی انگلیسی، فرمول زیر را کامل کنید:",
        "code_snippet": "char cipher = ((c - 'A' + key) % ___) + 'A';",
        "expected_answer": "26",
        "acceptable_answers": ["26"],
        "hint": "تعداد حروف الفبای انگلیسی چند است؟ برای چرخش حروف از باقیمانده بر چه عددی استفاده می‌شود؟",
        "xp_reward": 5,
        "explanation": "عالیه! الفبای انگلیسی ۲۶ حرف دارد و با عملگر باقیمانده % 26 کاراکترها درون بازه ۰ تا ۲۵ می‌چرخند."
    }
}


def get_exercise(exercise_id: str) -> dict | None:
    return EXERCISES.get(exercise_id)


def get_exercises_for_week(week_num: int) -> list[dict]:
    return [ex for ex in EXERCISES.values() if ex["week"] == week_num]


def get_user_attempt(user_id: int, exercise_id: str) -> ExerciseAttempt | None:
    return ExerciseAttempt.query.filter_by(user_id=user_id, exercise_id=exercise_id).first()


def submit_exercise(user_id: int, exercise_id: str, answer: str, hints_used: int = 0) -> dict:
    ex = get_exercise(exercise_id)
    if not ex:
        return {"success": False, "message": "تمرین پیدا نشد."}

    norm_answer = answer.strip().replace(" ", "")
    correct = norm_answer in [a.strip().replace(" ", "") for a in ex["acceptable_answers"]]

    attempt = get_user_attempt(user_id, exercise_id)
    first_time_correct = False

    if attempt is None:
        attempt = ExerciseAttempt(
            user_id=user_id,
            week=ex["week"],
            exercise_id=exercise_id,
            is_correct=correct,
            submitted_answer=answer,
            hints_used=hints_used,
        )
        db.session.add(attempt)
        if correct:
            first_time_correct = True
    else:
        attempt.submitted_answer = answer
        attempt.hints_used = max(attempt.hints_used, hints_used)
        if not attempt.is_correct and correct:
            attempt.is_correct = True
            first_time_correct = True

    db.session.commit()

    xp_gained = 0
    if first_time_correct:
        reason = f"exercise:{exercise_id}:pass"
        # در صورت راهنمایی زیاد ۱ نمره کسر می‌شود ولی حداقل ۳ XP داده می‌شود
        earned = max(3, ex["xp_reward"] - (1 if hints_used > 1 else 0))
        if xp_service.award(user_id, earned, reason):
            xp_gained = earned
        streak_service.update_streak(user_id)

    return {
        "success": True,
        "is_correct": correct,
        "explanation": ex["explanation"] if correct else "پاسخ نادرست است. دوباره تلاش کن یا از راهنما استفاده کن.",
        "xp_awarded": xp_gained,
        "first_time": first_time_correct
    }
