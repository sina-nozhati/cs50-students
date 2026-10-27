"""سرویس ماژول‌های تعاملی پایگاه دانش: فلش‌کارت‌های لایتنر، کوییزها، واژه‌نامه و پرسش‌وپاسخ."""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from app import db
from app.models import FlashcardProgress, ExerciseAttempt, WeekProgress
from app.content import kb_repo
from app.services import xp as xp_service
from app.services import events as event_service


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
    root = kb_repo.kb_root()
    path = root / "anzali-fa" / "weeks" / f"week-{week:02d}" / "flashcards.json"
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

    return {
        "success": True,
        "card_id": card_id,
        "box_number": st.box_number,
        "repetitions": st.repetitions,
        "interval_days": st.interval_days,
        "xp_awarded": xp_awarded,
    }


def load_quizzes_for_week(week: int, user_id: int | None = None) -> list[dict[str, Any]]:
    """بارگذاری آزمون‌های هفته (چهارگزینه‌ای و جای خالی)."""
    root = kb_repo.kb_root()
    path = root / "anzali-fa" / "weeks" / f"week-{week:02d}" / "quizzes.json"
    if not path.is_file():
        return []

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    items = data.get("items", [])
    user_attempts: dict[str, ExerciseAttempt] = {}
    if user_id:
        rows = ExerciseAttempt.query.filter_by(user_id=user_id, week=week).all()
        user_attempts = {r.exercise_id: r for r in rows}

    out = []
    # انتخاب حداکثر ۱۰ سوال اول با تنوع تستی
    selected_items = items[:10]
    for q in selected_items:
        qid = q.get("id")
        att = user_attempts.get(qid)
        q_type = q.get("type", "mcq")

        # برای آزمون، گزینه‌ها را آماده می‌کنیم
        options = q.get("options") or []
        if q_type == "true_false" and not options:
            options = [
                {"id": "true", "text_fa": "درست"},
                {"id": "false", "text_fa": "نادرست"},
            ]

        out.append({
            "id": qid,
            "type": q_type,
            "prompt_fa": q.get("prompt_fa", ""),
            "explanation_fa": q.get("explanation_fa", ""),
            "options": options,
            "difficulty": q.get("difficulty", 1),
            "lesson_id": q.get("lesson_id"),
            "attempted": att is not None,
            "is_correct": att.is_correct if att else False,
            "submitted_answer": att.submitted_answer if att else None,
        })
    return out


def submit_quiz_question(
    user_id: int, week: int, question_id: str, answer_value: str
) -> dict[str, Any]:
    """تصحیح خودکار یک سوال کوییز و ثبت اسکور."""
    root = kb_repo.kb_root()
    path = root / "anzali-fa" / "weeks" / f"week-{week:02d}" / "quizzes.json"
    if not path.is_file():
        return {"success": False, "error": "quiz_not_found"}

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {"success": False, "error": "quiz_read_error"}

    target = next((item for item in data.get("items", []) if item.get("id") == question_id), None)
    if not target:
        return {"success": False, "error": "question_not_found"}

    q_type = target.get("type", "mcq")
    ans_obj = target.get("answer", {})
    explanation = target.get("explanation_fa", "")

    clean_ans = str(answer_value or "").strip()
    is_correct = False

    if q_type == "mcq":
        correct_ids = [str(x).strip().lower() for x in ans_obj.get("correct_option_ids", [])]
        is_correct = clean_ans.lower() in correct_ids
    elif q_type == "true_false":
        val = bool(ans_obj.get("value"))
        user_val = clean_ans.lower() in ("true", "1", "درست")
        is_correct = user_val == val
    elif q_type in ("short_answer", "predict_output"):
        accept_list = ans_obj.get("accept", [])
        if isinstance(accept_list, str):
            accept_list = [accept_list]
        normalized_accepts = [str(x).strip().lower() for x in accept_list]
        is_correct = clean_ans.lower() in normalized_accepts

    # ثبت تلاش در دیتابیس
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
        att.created_at = datetime.utcnow()
    db.session.commit()

    # محاسبه امتیاز کل آزمون این هفته
    all_week_attempts = ExerciseAttempt.query.filter_by(
        user_id=user_id, week=week, is_correct=True
    ).count()

    wp = WeekProgress.query.filter_by(user_id=user_id, week=week).first()
    if not wp:
        wp = WeekProgress(user_id=user_id, week=week, quiz_total=5, quiz_score=0)
        db.session.add(wp)

    wp.quiz_score = all_week_attempts
    wp.quiz_total = max(wp.quiz_total or 5, 5)
    # حد قبولی ۸۰ درصد (تصمیم تصویب‌شده)
    if wp.quiz_total > 0 and (wp.quiz_score / wp.quiz_total) >= 0.8:
        wp.quiz_completed = True

    db.session.commit()

    xp_awarded = 0
    if is_correct:
        quiz_xp = 10
        awarded = xp_service.award(user_id, quiz_xp, f"quiz_{week}_{question_id}")
        xp_awarded = quiz_xp if awarded else 0

    event_service.log_event(user_id, "quiz_submit", {
        "week": week,
        "question_id": question_id,
        "is_correct": is_correct,
        "quiz_score": wp.quiz_score,
        "quiz_completed": wp.quiz_completed,
    })

    return {
        "success": True,
        "question_id": question_id,
        "is_correct": is_correct,
        "explanation": explanation,
        "xp_awarded": xp_awarded,
        "current_score": wp.quiz_score,
        "total_score": wp.quiz_total,
        "quiz_completed": wp.quiz_completed,
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
    }
