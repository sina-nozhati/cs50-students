"""سرویس ماژول‌های تعاملی پایگاه دانش: فلش‌کارت‌های لایتنر، کوییزها، واژه‌نامه و پرسش‌وپاسخ."""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from app import db
from app.models import FlashcardProgress, ExerciseAttempt, WeekProgress, QuizAttempt
from app.content import kb_repo
from app.services import xp as xp_service
from app.services import events as event_service
from app.services import diagnostics as diag_service


FAQS_BY_WEEK: dict[int, list[dict[str, str]]] = {
    0: [
        {
            "q": "آیا در انجام تمرین اسکرچ استفاده از چت‌بات‌های هوش مصنوعی مثل ChatGPT یا Claude مجاز است؟",
            "a": "خیر؛ طبق سیاست صداقت علمی دوره CS50، تنها دستیار مجاز هوش مصنوعی CS50 Duck (cs50.ai) است که به عنوان راهنما عمل می‌کند و کد کامل را برای شما تولید نمی‌کند.",
            "tag": "هوش مصنوعی و صداقت علمی"
        },
        {
            "q": "برای ثبت پروژه Problem Set 0 چگونه باید لینک اسکرچ را تحویل دهیم؟",
            "a": "باید در سایت scratch.mit.edu پروژه خود را Share کنید و سپس لینک عمومی پروژه را در فرم تحویل ثبت نمایید. حتماً چک کنید که لینک در حالت Incognito بدون لاگین باز شود.",
            "tag": "ارسال تمرین"
        },
        {
            "q": "چرا در اسکرچ و علوم کامپیوتر شمارش یا دستگاه مختصات از صفر (0, 0) شروع می‌شود؟",
            "a": "در مبنای دودویی (باینری) و معماری سخت‌افزار، مقادیر صفر حالت پایه هستند. همچنین در صحنه اسکرچ، نقطه (x:0, y:0) دقیقاً مرکز صفحه نمایش است.",
            "tag": "مفاهیم پایه"
        },
        {
            "q": "تفاوت بین ASCII و Unicode چیست و چرا ایموجی‌ها به وجود آمدند؟",
            "a": "اَسکی فقط از ۷ یا ۸ بیت برای ۱۲۸ الی ۲۵۶ کاراکتر انگلیسی استفاده می‌کرد، در حالی که یونیکد بیش از ۱۴۰,۰۰۰ کاراکتر را برای تمام زبان‌های جهان (از جمله خط فارسی) و هزاران ایموجی پوشش می‌دهد.",
            "tag": "داده‌ها و کاراکترها"
        }
    ]
}


def load_flashcards_for_week(week: int, user_id: int | None = None) -> list[dict[str, Any]]:
    """بارگذاری فلش‌کارت‌های هفته به همراه وضعیت لایتنر کاربر."""
    path = kb_repo.get_anzali_week_dir(week) / "flashcards.json"
    if not path.is_file():
        return []

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    cards = data.get("cards", [])
    if not cards:
        return []

    user_states: dict[str, FlashcardProgress] = {}
    if user_id:
        rows = FlashcardProgress.query.filter_by(user_id=user_id, week=week).all()
        user_states = {r.card_id: r for r in rows}

    out = []
    now = datetime.utcnow()
    for c in cards:
        cid = c.get("id")
        st = user_states.get(cid)
        box = st.box_number if st else 1
        is_due = (st.next_review <= now) if st else True
        reps = st.repetitions if st else 0

        out.append({
            "id": cid,
            "concept_id": c.get("concept_id"),
            "note_id": c.get("note_id"),
            "front_fa": c.get("front_fa"),
            "back_fa": c.get("back_fa"),
            "difficulty": c.get("difficulty", 1),
            "tags": c.get("tags", []),
            "source_ref": c.get("source_ref"),
            "box_number": box,
            "is_due": is_due,
            "repetitions": reps,
            "reviewed": st is not None,
        })
    return out


def review_flashcard(user_id: int, week: int, card_id: str, rating: str) -> dict[str, Any]:
    """ثبت نتیجه مرور فلش‌کارت در جعبه لایتنر (again, good, easy)."""
    now = datetime.utcnow()
    st = FlashcardProgress.query.filter_by(user_id=user_id, card_id=card_id).first()
    if not st:
        st = FlashcardProgress(
            user_id=user_id,
            week=week,
            card_id=card_id,
            box_number=1,
            repetitions=0,
            interval_days=1,
            ease_factor=2.5,
            next_review=now,
            last_reviewed=now,
        )
        db.session.add(st)

    # الگوریتم جعبه لایتنر (۱ تا ۵)
    old_box = st.box_number
    if rating == "again":
        st.box_number = 1
        st.interval_days = 1
        st.next_review = now + timedelta(days=1)
    elif rating == "easy":
        st.box_number = min(st.box_number + 2, 5)
        st.repetitions += 1
        st.interval_days = st.box_number * 3
        st.next_review = now + timedelta(days=st.interval_days)
    else:  # good
        st.box_number = min(st.box_number + 1, 5)
        st.repetitions += 1
        st.interval_days = max(1, st.box_number * 2)
        st.next_review = now + timedelta(days=st.interval_days)

    st.last_reviewed = now
    db.session.commit()

    # علامت‌زدن مرور فلش‌کارت در پیشرفت هفته
    wp = WeekProgress.query.filter_by(user_id=user_id, week=week).first()
    if not wp:
        wp = WeekProgress(user_id=user_id, week=week, flashcards_reviewed=True)
        db.session.add(wp)
    else:
        wp.flashcards_reviewed = True
    db.session.commit()

    xp_amount = 2
    awarded = xp_service.award(user_id, xp_amount, f"flashcard_{week}_{card_id}")
    xp_awarded = xp_amount if awarded else 0
    event_service.log_event(user_id, "flashcard_review", {
        "week": week,
        "card_id": card_id,
        "rating": rating,
        "old_box": old_box,
        "new_box": st.box_number,
    })

    if rating == "again":
        diag_service.record_mistake(
            user_id=user_id,
            week=week,
            source="flashcard",
            item_id=card_id,
            item_title=f"فلش‌کارت هفته {week} ({card_id})",
            concept_tag=f"مفاهیم و تعاریف هفته {week}",
            user_answer="again (نیاز به یادآوری مجدد)",
            expected_answer="good / easy (پاسخ مطمئن)",
            explanation="این کارت در جعبه لایتنر به خانه اول برگشت تا در فواصل کوتاه‌تر مرور شود.",
        )
    elif rating in ("good", "easy"):
        diag_service.resolve_mistake(user_id=user_id, item_id=card_id)

    return {
        "success": True,
        "card_id": card_id,
        "box_number": st.box_number,
        "repetitions": st.repetitions,
        "interval_days": st.interval_days,
        "xp_awarded": xp_awarded,
    }


MAX_QUIZ_ATTEMPTS = 5


def get_quiz_attempt_meta(user_id: int, week: int, total_questions: int = 5) -> dict[str, Any]:
    """دریافت متادیتای تلاش‌های کاربر در آزمون هفتگی شامل شماره تلاش و فرصت‌های باقی‌مانده."""
    attempts = (
        QuizAttempt.query.filter_by(user_id=user_id, week=week)
        .order_by(QuizAttempt.attempt_number.asc())
        .all()
    )
    if not attempts:
        return {
            "attempt_number": 1,
            "attempts_used": 0,
            "remaining_attempts": MAX_QUIZ_ATTEMPTS,
            "can_retake": False,
            "is_completed": False,
            "score": 0,
            "total_questions": total_questions,
            "has_attempts": False,
        }

    latest = attempts[-1]
    attempts_used = len(attempts)
    remaining = max(0, MAX_QUIZ_ATTEMPTS - attempts_used)

    return {
        "attempt_number": latest.attempt_number,
        "attempts_used": attempts_used,
        "remaining_attempts": remaining,
        "can_retake": latest.is_completed and remaining > 0,
        "is_completed": latest.is_completed,
        "score": latest.score,
        "total_questions": latest.total_questions or total_questions,
        "has_attempts": True,
    }


def get_or_create_active_quiz_attempt(
    user_id: int, week: int, total_questions: int = 5
) -> QuizAttempt:
    """دریافت تلاش فعال جاری یا ایجاد تلاش شماره یک."""
    latest = (
        QuizAttempt.query.filter_by(user_id=user_id, week=week)
        .order_by(QuizAttempt.attempt_number.desc())
        .first()
    )
    if not latest:
        latest = QuizAttempt(
            user_id=user_id,
            week=week,
            attempt_number=1,
            score=0,
            total_questions=total_questions,
            answers_json={},
            is_completed=False,
            created_at=datetime.utcnow(),
        )
        db.session.add(latest)
        db.session.commit()
    return latest


def start_new_quiz_attempt(user_id: int, week: int, total_questions: int = 5) -> dict[str, Any]:
    """شروع تلاش مستقل جدید برای آزمون با سقف قطعی ۵ تلاش در سطح دیتابیس."""
    attempts = (
        QuizAttempt.query.filter_by(user_id=user_id, week=week)
        .order_by(QuizAttempt.attempt_number.asc())
        .all()
    )
    attempts_count = len(attempts)

    if attempts_count >= MAX_QUIZ_ATTEMPTS:
        return {
            "success": False,
            "error": "max_attempts_reached",
            "message": f"شما به سقف مجاز {MAX_QUIZ_ATTEMPTS} تلاش برای آزمون این هفته رسیده‌اید.",
            "attempts_used": attempts_count,
            "remaining_attempts": 0,
        }

    # در صورت وجود تلاش قبلی که کامل نشده، آن را با نمره فعلی نهایی می‌کنیم
    if attempts and not attempts[-1].is_completed:
        attempts[-1].is_completed = True
        attempts[-1].completed_at = datetime.utcnow()

    new_attempt_number = attempts_count + 1
    new_attempt = QuizAttempt(
        user_id=user_id,
        week=week,
        attempt_number=new_attempt_number,
        score=0,
        total_questions=total_questions,
        answers_json={},
        is_completed=False,
        created_at=datetime.utcnow(),
    )
    db.session.add(new_attempt)
    db.session.commit()

    return {
        "success": True,
        "attempt_number": new_attempt.attempt_number,
        "attempts_used": new_attempt_number,
        "remaining_attempts": max(0, MAX_QUIZ_ATTEMPTS - new_attempt_number),
        "message": f"تلاش شماره {new_attempt_number} از {MAX_QUIZ_ATTEMPTS} آغاز شد.",
    }


def get_quiz_type_label(q: dict[str, Any]) -> str:
    """تولید برچسب پویای نوع پرسش طبق جدول قرارداد CS50x Anzali v1.0.0."""
    if not isinstance(q, dict):
        return "پرسش"
    q_type = str(q.get("type", "mcq")).strip().lower()
    options = q.get("options") or []
    ans = q.get("answer") or {}
    correct_ids = ans.get("correct_option_ids") or []

    if q_type == "mcq":
        if len(correct_ids) > 1:
            return "چندپاسخی"
        n = len(options)
        if n == 2:
            return "دوگزینه‌ای"
        elif n == 3:
            return "سه‌گزینه‌ای"
        elif n == 4:
            return "چهارگزینه‌ای"
        elif n == 5:
            return "پنج‌گزینه‌ای"
        return "چندگزینه‌ای"
    elif q_type == "true_false":
        return "درست یا نادرست"
    elif q_type == "predict_output":
        return "پیش‌بینی خروجی"
    elif q_type in ("fill_blank", "fill_blank_code"):
        return "جای خالی"
    elif q_type == "token_tap":
        return "انتخاب توکن"
    elif q_type in ("parsons", "ordering"):
        return "مرتب‌سازی سطرها"
    elif q_type in ("spot_bug", "find_the_bug"):
        return "پیدا کردن اشکال"
    elif q_type == "short_answer":
        return "پاسخ کوتاه"
    return "چندگزینه‌ای"


def get_mastery_quiz_info(week: int) -> dict[str, Any]:
    """استخراج اطلاعات آزمون تسلط هفته شامل فهرست پرسش‌ها، آستانه قبولی و زمان انتظار."""
    path = kb_repo.get_anzali_week_dir(week) / "quizzes.json"
    if not path.is_file():
        return {
            "items": [],
            "item_ids": [],
            "total_questions": 5,
            "pass_threshold": 0.8,
            "cooldown_hours": 0,
            "mastery_qz": None,
        }
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {
            "items": [],
            "item_ids": [],
            "total_questions": 5,
            "pass_threshold": 0.8,
            "cooldown_hours": 0,
            "mastery_qz": None,
        }

    items = data.get("items", [])
    items_by_id = {it["id"]: it for it in items if isinstance(it, dict) and "id" in it}
    quizzes = data.get("quizzes", [])
    mastery_qz = next((qz for qz in quizzes if qz.get("kind") == "mastery_test"), None)

    if mastery_qz:
        item_ids = mastery_qz.get("item_ids", [])
        selected = [items_by_id[iid] for iid in item_ids if iid in items_by_id]
        retake = mastery_qz.get("retake", {})
        return {
            "items": selected,
            "item_ids": item_ids,
            "total_questions": len(selected) or len(items[:5]) or 5,
            "pass_threshold": float(mastery_qz.get("pass_threshold", 0.8)),
            "cooldown_hours": int(retake.get("cooldown_hours", 0)),
            "mastery_qz": mastery_qz,
        }

    # در صورت نبود آزمون تسلط صریح، سوالات اولیه به کار می‌روند
    fallback_items = items[:5] if len(items) >= 5 else items
    return {
        "items": fallback_items,
        "item_ids": [it["id"] for it in fallback_items],
        "total_questions": len(fallback_items) or 5,
        "pass_threshold": 0.8,
        "cooldown_hours": 0,
        "mastery_qz": None,
    }


def load_quizzes_for_week(week: int, user_id: int | None = None) -> list[dict[str, Any]]:
    """بارگذاری آزمون تسلط هفته طبق quizzes[kind=='mastery_test'].item_ids با قرارداد D90."""
    path = kb_repo.get_anzali_week_dir(week) / "quizzes.json"
    if not path.is_file():
        return []

    mastery_info = get_mastery_quiz_info(week)
    selected_items = mastery_info.get("items", [])
    if not selected_items:
        return []

    active_attempt = None
    if user_id:
        active_attempt = (
            QuizAttempt.query.filter_by(user_id=user_id, week=week)
            .order_by(QuizAttempt.attempt_number.desc())
            .first()
        )

    answers_map = dict(active_attempt.answers_json or {}) if active_attempt else {}
    is_attempt_finalized = bool(active_attempt and active_attempt.is_completed)

    out = []
    for q in selected_items:
        qid = q.get("id")
        q_type = q.get("type", "mcq")

        recorded_ans = answers_map.get(qid)
        attempted = recorded_ans is not None
        is_correct = bool(recorded_ans and recorded_ans.get("is_correct"))
        sub_answer = recorded_ans.get("answer") if recorded_ans else None

        raw_options = q.get("options") or []
        if q_type == "true_false" and not raw_options:
            raw_options = [
                {"id": "true", "text_fa": "درست"},
                {"id": "false", "text_fa": "نادرست"},
            ]

        # پشتیبانی قرارداد D90 برای گزینه‌های کدی (text_is_code)
        options = []
        for opt in raw_options:
            options.append({
                "id": opt.get("id"),
                "text_fa": opt.get("text_fa", ""),
                "feedback_fa": opt.get("feedback_fa", ""),
                "text_is_code": bool(opt.get("text_is_code", False)),
                "misconception": opt.get("misconception"),
            })

        # خطوط پارسونز (شامل خطوط اصلی و distractors)
        lines = q.get("lines") or []
        distractors = q.get("distractors") or []
        all_parsons_lines = []
        for l in lines:
            all_parsons_lines.append({"id": l.get("id"), "code": l.get("code")})
        for d in distractors:
            all_parsons_lines.append({"id": d.get("id"), "code": d.get("code"), "is_distractor": True})

        code_snippet = q.get("code") or ""
        code_lang = q.get("lang") or "c"
        type_lbl = get_quiz_type_label(q)

        out.append({
            "id": qid,
            "type": q_type,
            "type_label": type_lbl,
            "prompt_fa": q.get("prompt_fa", ""),
            "prompt_full_fa": q.get("prompt_full_fa", ""),
            "explanation_fa": q.get("explanation_fa", ""),
            "hint_fa": q.get("hint_fa") or "",
            "hints_fa": q.get("hints_fa") or [],
            "options": options,
            "lines": all_parsons_lines,
            "code": code_snippet,
            "lang": code_lang,
            "difficulty": q.get("difficulty", 1),
            "lesson_id": q.get("lesson_id"),
            "concept_ids": q.get("concept_ids") or [],
            "attempted": attempted,
            "is_correct": is_correct,
            "submitted_answer": sub_answer,
            "is_finalized": is_attempt_finalized,
        })
    return out


def submit_quiz_question(
    user_id: int, week: int, question_id: str, answer_value: Any
) -> dict[str, Any]:
    """تصحیح خودکار یک سوال کوییز و ثبت اسکور در تلاش جاری به همراه جلوگیری از تغییر پاسخ و سقف نمره."""
    path = kb_repo.get_anzali_week_dir(week) / "quizzes.json"
    if not path.is_file():
        return {"success": False, "error": "quiz_not_found", "message": "فایل آزمون یافت نشد."}

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {"success": False, "error": "quiz_read_error", "message": "خطا در بارگذاری فایل آزمون."}

    mastery_info = get_mastery_quiz_info(week)
    selected_items = mastery_info.get("items", [])
    total_quiz_questions = mastery_info.get("total_questions", len(selected_items) or 5)

    target = next((item for item in selected_items if item.get("id") == question_id), None)
    if not target:
        items = data.get("items", [])
        target = next((item for item in items if item.get("id") == question_id), None)
    if not target:
        return {"success": False, "error": "question_not_found", "message": "سوال یافت نشد."}

    attempt = get_or_create_active_quiz_attempt(user_id, week, total_questions=total_quiz_questions)
    if attempt.total_questions != total_quiz_questions and not attempt.is_completed:
        attempt.total_questions = total_quiz_questions

    # ۱. قفل تلاش نهایی‌شده: پاسخ‌ها پس از تکمیل آزمون غیرقابل تغییرند
    if attempt.is_completed:
        return {
            "success": False,
            "error": "attempt_finalized",
            "message": "این آزمون قبلاً نهایی شده است. برای شرکت دوباره از دکمه «شروع مجدد آزمون» استفاده کنید.",
            "is_finalized": True,
            "current_score": attempt.score,
            "total_score": attempt.total_questions,
            "is_correct": False,
        }

    # ۲. قفل سوال پاسخ‌داده‌شده در همین تلاش: جلوگیری از کلیک مجدد و تغییر پاسخ
    answers = dict(attempt.answers_json or {})
    if question_id in answers:
        prev = answers[question_id]
        return {
            "success": False,
            "error": "already_answered",
            "message": "پاسخ این سؤال قبلاً ثبت شده و قابل تغییر نیست.",
            "is_correct": prev.get("is_correct", False),
            "explanation": target.get("explanation_fa", ""),
            "current_score": attempt.score,
            "total_score": attempt.total_questions,
            "is_finalized": False,
        }

    q_type = target.get("type", "mcq")
    ans_obj = target.get("answer", {})
    explanation = target.get("explanation_fa", "")

    clean_ans = str(answer_value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    is_correct = False

    if q_type == "mcq":
        correct_ids = [str(x).strip().lower() for x in ans_obj.get("correct_option_ids", [])]
        is_correct = clean_ans.lower() in correct_ids

    elif q_type == "true_false":
        val = bool(ans_obj.get("value"))
        user_val = clean_ans.lower() in ("true", "1", "درست")
        is_correct = (user_val == val)

    elif q_type in ("short_answer", "predict_output", "fill_blank_code"):
        accept_list = ans_obj.get("accept", [])
        if isinstance(accept_list, str):
            accept_list = [accept_list]
        normalized_accepts = [str(x).strip().lower() for x in accept_list]
        if ans_obj.get("value") is not None:
            normalized_accepts.append(str(ans_obj.get("value")).strip().lower())
        is_correct = clean_ans.lower() in normalized_accepts

    elif q_type == "parsons":
        expected_order = ans_obj.get("order") or ans_obj.get("correct_order", [])
        user_order = []
        if isinstance(answer_value, list):
            user_order = [str(x).strip() for x in answer_value]
        elif isinstance(answer_value, str):
            if answer_value.startswith("[") and answer_value.endswith("]"):
                try:
                    user_order = [str(x).strip() for x in json.loads(answer_value)]
                except Exception:
                    user_order = [x.strip() for x in answer_value.strip("[]").split(",") if x.strip()]
            elif "," in answer_value:
                user_order = [x.strip() for x in answer_value.split(",") if x.strip()]
            else:
                user_order = [answer_value.strip()]
        expected_norm = [str(x).strip() for x in expected_order]
        is_correct = (user_order == expected_norm)

    # استخراج بازخورد گزینه یا سوال (feedback_fa)
    feedback_text = ""
    misconception_info = None
    if q_type == "mcq":
        for opt in target.get("options", []):
            if str(opt.get("id")).lower() == clean_ans.lower():
                feedback_text = opt.get("feedback_fa", "")
                if not is_correct and opt.get("misconception"):
                    misconception_info = {
                        "misconception": opt.get("misconception"),
                        "remediation_fa": opt.get("remediation_fa") or target.get("remediation_fa"),
                        "anchor": opt.get("anchor") or target.get("anchor"),
                    }
                break
    else:
        q_fb = target.get("feedback") or {}
        if is_correct:
            feedback_text = q_fb.get("correct_fa") or target.get("feedback_fa", "")
        else:
            feedback_text = q_fb.get("incorrect_fa") or target.get("feedback_fa", "")

    # ۳. ذخیره پاسخ در تلاش جاری
    answers[question_id] = {
        "answer": clean_ans,
        "is_correct": is_correct,
        "submitted_at": datetime.utcnow().isoformat(),
    }
    attempt.answers_json = answers

    # ۴. محاسبه دقیق نمره منحصراً از سوالات این آزمون (بازه قطعی [0, total_questions])
    correct_count = sum(1 for v in answers.values() if v.get("is_correct") is True)
    attempt.score = min(max(0, correct_count), attempt.total_questions)

    # نهایی شدن آزمون با پاسخ به همه سوالات
    if len(answers) >= total_quiz_questions:
        attempt.is_completed = True
        attempt.completed_at = datetime.utcnow()

    # ۵. به‌روزرسانی نمره نهایی در WeekProgress بر اساس آستانه قبولی آزمون تسلط
    mastery_info = get_mastery_quiz_info(week)
    pass_threshold = float(mastery_info.get("pass_threshold", 0.8))

    wp = WeekProgress.query.filter_by(user_id=user_id, week=week).first()
    if not wp:
        wp = WeekProgress(user_id=user_id, week=week, quiz_total=attempt.total_questions, quiz_score=0)
        db.session.add(wp)

    all_user_attempts = QuizAttempt.query.filter_by(user_id=user_id, week=week).all()
    best_score = max([a.score for a in all_user_attempts] + [attempt.score])
    wp.quiz_score = min(best_score, attempt.total_questions)
    wp.quiz_total = attempt.total_questions

    is_passed = (wp.quiz_total > 0 and (wp.quiz_score / wp.quiz_total) >= pass_threshold)
    if is_passed:
        wp.quiz_completed = True

    # ثبت تلاش در ExerciseAttempt برای حفظ backward compatibility و آمار کلی
    att = ExerciseAttempt.query.filter_by(user_id=user_id, exercise_id=question_id).first()
    if not att:
        att = ExerciseAttempt(
            user_id=user_id,
            week=week,
            exercise_id=question_id,
            is_correct=is_correct,
            submitted_answer=clean_ans,
            hints_used=0,
            created_at=datetime.utcnow(),
        )
        db.session.add(att)
    else:
        att.submitted_answer = clean_ans
        att.is_correct = is_correct

    db.session.commit()

    # اعطای ۲۵ XP فقط در صورت قبولی در آزمون تسلط به صورت ایدمپوتنت (تک‌پاسخ = ۰ XP)
    xp_awarded = 0
    if is_passed:
        reason = f"quiz:mastery:w{week:02d}:pass"
        if xp_service.award(user_id, 25, reason):
            xp_awarded = 25

    event_service.log_event(user_id, "quiz_submit", {
        "week": week,
        "question_id": question_id,
        "is_correct": is_correct,
        "attempt_number": attempt.attempt_number,
        "attempt_score": attempt.score,
        "quiz_score": wp.quiz_score,
        "quiz_completed": wp.quiz_completed,
        "is_finalized": attempt.is_completed,
    })

    if not is_correct:
        c_ids = target.get("concept_ids", [])
        tag = c_ids[0] if c_ids else f"کوییز هفته {week}"
        expected_val = (
            ans_obj.get("correct_option_ids")
            or ans_obj.get("value")
            or ans_obj.get("accept")
            or ans_obj.get("order")
        )
        diag_service.record_mistake(
            user_id=user_id,
            week=week,
            source="quiz",
            item_id=question_id,
            item_title=target.get("prompt_fa", f"سؤال کوییز {question_id}"),
            concept_tag=tag,
            user_answer=clean_ans,
            expected_answer=expected_val,
            explanation=explanation,
        )
    else:
        diag_service.resolve_mistake(user_id=user_id, item_id=question_id)

    return {
        "success": True,
        "question_id": question_id,
        "is_correct": is_correct,
        "feedback_fa": feedback_text,
        "explanation": explanation,
        "misconception": misconception_info.get("misconception") if misconception_info else None,
        "remediation_fa": misconception_info.get("remediation_fa") if misconception_info else None,
        "anchor": misconception_info.get("anchor") if misconception_info else None,
        "xp_awarded": xp_awarded,
        "current_score": attempt.score,
        "total_score": attempt.total_questions,
        "quiz_completed": wp.quiz_completed,
        "pass_threshold": pass_threshold,
        "is_finalized": attempt.is_completed,
        "attempt_number": attempt.attempt_number,
        "remaining_attempts": max(0, MAX_QUIZ_ATTEMPTS - attempt.attempt_number),
    }


def load_glossary_for_week(week: int) -> list[dict[str, str]]:
    """بارگذاری اصطلاحات تخصصی مربوط به هفته از glossary.fa.json."""
    root = kb_repo.kb_root()
    path = root / "anzali-fa" / "curriculum" / "glossary.fa.json"
    if not path.is_file():
        return []

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    terms = data.get("terms", [])
    week_prefix = f"w{week:02d}-"
    out = []
    for t in terms:
        cid = t.get("concept_id") or ""
        tid = t.get("id") or ""
        # اگر اصطلاح به این هفته وصل است یا تگ شده
        if week_prefix in cid or week_prefix in tid or week == 0:
            out.append({
                "id": tid,
                "fa": t.get("fa", ""),
                "en": t.get("en", ""),
                "concept_id": cid,
                "source_ref": t.get("source_ref", ""),
            })
    return out


def load_faqs_for_week(week: int) -> list[dict[str, str]]:
    """بارگذاری پرسش‌ها و پاسخ‌های پرتکرار هفته."""
    return FAQS_BY_WEEK.get(week, [
        {
            "q": f"سؤالات متداول هفته {week}",
            "a": "پاسخ به سوالات رایج و چالش‌های کدنویسی دانشجویان در این بخش قرار می‌گیرد.",
            "tag": "عمومی"
        }
    ])


def get_week_interactive_summary(user_id: int, week: int) -> dict[str, Any]:
    """خلاصه تجمیعی فعالیت‌ها و درصدهای پیشرفت هفته برای استاتوس‌بار و هدر."""
    wp = WeekProgress.query.filter_by(user_id=user_id, week=week).first()
    quiz_score = wp.quiz_score if wp else 0
    quiz_total = wp.quiz_total if wp else 5
    quiz_completed = wp.quiz_completed if wp else False
    kb_read = wp.kb_read if wp else False
    flashcards_reviewed = wp.flashcards_reviewed if wp else False

    # شمارش فلش‌کارت‌ها بر اساس جعبه‌ها
    fc_rows = FlashcardProgress.query.filter_by(user_id=user_id, week=week).all()
    boxes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for r in fc_rows:
        b = max(1, min(r.box_number, 5))
        boxes[b] = boxes.get(b, 0) + 1

    # درصد پیشرفت کل هفته: خواندن جزوه (۳۰٪) + مرور فلش‌کارت (۳۰٪) + آزمون (۴۰٪)
    progress_pct = 0
    if kb_read:
        progress_pct += 30
    if flashcards_reviewed or len(fc_rows) >= 5:
        progress_pct += 30
    if quiz_total > 0:
        progress_pct += int((min(quiz_score, quiz_total) / quiz_total) * 40)

    meta = get_quiz_attempt_meta(user_id, week, total_questions=quiz_total)

    return {
        "week": week,
        "progress_pct": min(progress_pct, 100),
        "kb_read": kb_read,
        "flashcards_reviewed": flashcards_reviewed,
        "cards_reviewed_count": len(fc_rows),
        "boxes": boxes,
        "quiz_score": quiz_score,
        "quiz_total": quiz_total,
        "quiz_completed": quiz_completed,
        "attempt_meta": meta,
    }
