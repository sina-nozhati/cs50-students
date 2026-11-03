"""پایگاه دانش — بارگذاری از docs/cs50x-kb."""
import json
from flask import Blueprint, render_template, abort, redirect, url_for, flash
from flask_login import login_required, current_user

from app.services import xp as xp_service
from app.services import progress as progress_service
from app.services import weeks as weeks_service
from app.services import kb_content as kb_service
from app.services import resources as res_service
from app.services import exercises as exercise_service
from app.services import events as event_service
from app.services import kb_interactive
from app.services import practice as practice_service
from app import db
from datetime import datetime
from app.models import WeekProgress, XPLog
from flask import request, jsonify, make_response, send_file
from urllib.parse import quote
from app.services import downloads as downloads_service
import re

bp = Blueprint("kb", __name__, url_prefix="/kb")


@bp.before_request
@login_required
def _require_login():
    pass


def _get_visible_week_or_404(week: int):
    week_obj = weeks_service.get_week_by_number(week)
    if week_obj is None or not week_obj.is_published:
        abort(404)
    return week_obj


@bp.route("/")
def index():
    cert = kb_service.certificate()
    catalog = kb_service.catalog()
    published = []
    for item in catalog:
        db_week = weeks_service.get_week_by_number(item["number"])
        if db_week and db_week.is_published:
            published.append({**item, "db_title": db_week.title})
    return render_template(
        "kb/index.html",
        weeks=published,
        certificate=cert,
    )


@bp.route("/week/<int:week>")
def week_page(week: int):
    week_obj = _get_visible_week_or_404(week)
    week_data = kb_service.week_payload(week)
    if week_data is None and not (week_obj.content_html or week_obj.content_url):
        abort(404)

    already_read = (
        WeekProgress.query.filter_by(
            user_id=current_user.id, week=week, kb_read=True
        ).first()
        is not None
    )
    can_mark_read = week_data is not None or bool(
        week_obj.content_html or week_obj.content_url
    )
    files = res_service.list_for_week(week)
    exercises = exercise_service.get_exercises_for_week(week)
    exercise_attempts = {
        ex["id"]: exercise_service.get_user_attempt(current_user.id, ex["id"])
        for ex in exercises
    }

    # بارگذاری ماژول‌های تعاملی جدید (فلش‌کارت، آزمون تسلط، واژه‌نامه و پرسش‌وپاسخ)
    flashcards = kb_interactive.load_flashcards_for_week(week, current_user.id)
    quizzes = kb_interactive.load_quizzes_for_week(week, current_user.id)
    glossary = kb_interactive.load_glossary_for_week(week)
    faqs = kb_interactive.load_faqs_for_week(week)
    interactive_summary = kb_interactive.get_week_interactive_summary(current_user.id, week)
    quiz_meta = interactive_summary.get("attempt_meta", {})
    has_practice = practice_service.has_practice_session(week)
    dynamic_downloads = downloads_service.get_week_manifest(week)

    return render_template(
        "kb/week.html",
        week=week,
        title=week_obj.title,
        week_data=week_data,
        content_html=week_obj.content_html,
        content_url=week_obj.content_url,
        already_read=already_read,
        can_mark_read=can_mark_read,
        files=files,
        dynamic_downloads=dynamic_downloads,
        exercises=exercises,
        exercise_attempts=exercise_attempts,
        flashcards=flashcards,
        quizzes=quizzes,
        glossary=glossary,
        faqs=faqs,
        interactive_summary=interactive_summary,
        quiz_meta=quiz_meta,
        has_practice=has_practice,
        certificate=kb_service.certificate(),
    )


@bp.route("/week/<int:week>/quiz/retake", methods=["POST"])
@login_required
def retake_quiz(week: int):
    """شروع تلاش مستقل جدید برای کوییز هفتگی (تا سقف ۵ تلاش)."""
    _get_visible_week_or_404(week)
    res = kb_interactive.start_new_quiz_attempt(current_user.id, week)
    if not res.get("success"):
        flash(res.get("message", "امکان شروع تلاش جدید وجود ندارد."), "warning")
    else:
        flash(res.get("message", "تلاش جدید برای آزمون آغاز شد."), "success")
    return redirect(url_for("kb.week_page", week=week, _anchor="tab-quiz"))


@bp.route("/week/<int:week>/quiz/submit", methods=["POST"])
@login_required
def submit_quiz_answer(week: int):
    """ثبت پاسخ کوییز چهارگزینه‌ای یا جای خالی و به‌روزرسانی نمره."""
    _get_visible_week_or_404(week)
    question_id = request.form.get("question_id") or ""
    answer_value = request.form.get("answer") or ""

    res = kb_interactive.submit_quiz_question(
        user_id=current_user.id,
        week=week,
        question_id=question_id,
        answer_value=answer_value
    )

    if request.headers.get("HX-Request"):
        # بازگرداندن وضعیت به‌صورت فرگمنت HTMX
        return render_template(
            "kb/_partials/_quiz_result.html",
            res=res,
            week=week,
            question_id=question_id
        )
    return jsonify(res)


@bp.route("/week/<int:week>/flashcard/review", methods=["POST"])
@login_required
def review_flashcard_card(week: int):
    """ثبت نتیجه مرور فلش‌کارت در جعبه لایتنر (again/good/easy)."""
    _get_visible_week_or_404(week)
    card_id = request.form.get("card_id") or ""
    rating = request.form.get("rating") or "good"

    res = kb_interactive.review_flashcard(
        user_id=current_user.id,
        week=week,
        card_id=card_id,
        rating=rating
    )

    if request.headers.get("HX-Request"):
        return render_template(
            "kb/_partials/_flashcard_result.html",
            res=res,
            week=week,
            card_id=card_id
        )
    return jsonify(res)


@bp.route("/week/<int:week>/interactive-summary")
@login_required
def week_interactive_summary_api(week: int):
    """استعلام زنده درصد پیشرفت و نمرات هفته."""
    _get_visible_week_or_404(week)
    summary = kb_interactive.get_week_interactive_summary(current_user.id, week)
    return jsonify(summary)


@bp.route("/exercise/<exercise_id>/submit", methods=["POST"])
@login_required
def submit_code_exercise(exercise_id: str):
    """ثبت پاسخ دانش‌آموز برای چالش کدنویسی به صورت HTMX fragment."""
    answer = request.form.get("answer", "")
    try:
        hints_used = int(request.form.get("hints_used", 0))
    except ValueError:
        hints_used = 0

    res = exercise_service.submit_exercise(
        user_id=current_user.id,
        exercise_id=exercise_id,
        answer=answer,
        hints_used=hints_used
    )

    event_service.log_event(
        user_id=current_user.id,
        event_type="exercise_attempt",
        payload={
            "exercise_id": exercise_id,
            "is_correct": res["is_correct"],
            "xp_awarded": res.get("xp_awarded", 0)
        }
    )

    exercise = exercise_service.get_exercise(exercise_id)
    attempt = exercise_service.get_user_attempt(current_user.id, exercise_id)

    return render_template(
        "kb/_partials/_exercise_card.html",
        exercise=exercise,
        attempt=attempt,
        error_message=None if res["is_correct"] else res["explanation"]
    )


@bp.route("/d/<doc_id>")
def doc_page(doc_id: str):
    """نمایش یک سند از درخت KB (lecture، pset، practice، …)."""
    doc = kb_service.get_document(doc_id)
    if doc is None:
        abort(404)

    # اگر به هفته‌ای وصل است، باید published باشد
    site_n = doc.get("site_number")
    if site_n is not None:
        week_obj = weeks_service.get_week_by_number(site_n)
        if week_obj is None or not week_obj.is_published:
            abort(404)

    pset_downloads = None
    if site_n is not None:
        slug = downloads_service.resolve_week_slug(site_n)
        manifest = downloads_service.get_week_manifest(slug)
        if manifest:
            for it in manifest.get("items", []):
                if it.get("kind") == "pset-guide":
                    p_id = it.get("pset_id") or ""
                    p_slug = it.get("pset_slug") or ""
                    if p_id == doc_id or (p_slug and p_slug in doc_id) or it.get("id") == doc_id:
                        pset_downloads = {
                            "slug": slug,
                            "item": it,
                            "formats": {f["format"]: f for f in it.get("formats", [])}
                        }
                        break

    return render_template(
        "kb/doc.html",
        doc=doc,
        pset_downloads=pset_downloads,
        certificate=kb_service.certificate(),
    )


@bp.route("/downloads/<week_slug>/<item_and_fmt>")
@login_required
def download_item(week_slug: str, item_and_fmt: str):
    """سرو امن فایل‌های دانلودی پایگاه دانش با ETag، هدرهای استاندارد و مهار Path Traversal."""
    if "." not in item_and_fmt:
        abort(404)
    item_id, fmt = item_and_fmt.rsplit(".", 1)

    # بررسی دسترسی انتشار هفته
    slug = downloads_service.resolve_week_slug(week_slug)
    m_week = re.search(r"week-(\d+)", slug)
    if m_week:
        w_num = int(m_week.group(1))
        _get_visible_week_or_404(w_num)
    elif slug == "week-ai":
        _get_visible_week_or_404(71)
    elif slug == "final-project":
        _get_visible_week_or_404(99)

    file_info = downloads_service.get_download_file(slug, item_id, fmt)
    if not file_info:
        abort(404)

    # پشتیبانی از ETag و پاسخ 304 Not Modified
    etag = f'"{file_info["sha256"]}"'
    client_etag = request.headers.get("If-None-Match")
    if client_etag and client_etag.strip() == etag:
        res = make_response("", 304)
        res.headers["ETag"] = etag
        res.headers["Cache-Control"] = "private, max-age=31536000, immutable"
        return res

    abs_path = str(file_info["abs_path"])
    mime_type = file_info["mime_type"]
    ascii_name = file_info["ascii_filename"]
    utf8_name = file_info["utf8_filename"]
    is_inline = file_info["is_inline"]

    disposition_type = "inline" if is_inline else "attachment"
    encoded_utf8 = quote(utf8_name.encode("utf-8"))
    content_disp = f'{disposition_type}; filename="{ascii_name}"; filename*=UTF-8\'\'{encoded_utf8}'

    response = send_file(
        abs_path,
        mimetype=mime_type,
        as_attachment=False,
    )
    response.headers["Content-Disposition"] = content_disp
    response.headers["ETag"] = etag
    response.headers["Cache-Control"] = "private, max-age=31536000, immutable"
    response.headers["X-Content-Type-Options"] = "nosniff"

    if is_inline:
        response.headers["Content-Security-Policy"] = (
            "default-src 'self' 'unsafe-inline' data:; "
            "style-src 'self' 'unsafe-inline' data:; "
            "font-src 'self' data:; img-src 'self' data:;"
        )

    return response


@bp.route("/week/<int:week>/read", methods=["POST"])
@login_required
def mark_read(week: int):
    week_obj = _get_visible_week_or_404(week)
    week_data = kb_service.week_payload(week)

    if not (week_data or week_obj.content_html or week_obj.content_url):
        flash("این هفته هنوز محتوایی ندارد.", "error")
        return redirect(url_for("kb.week_page", week=week))

    is_first_read = progress_service.mark_kb_read(current_user.id, week)
    if is_first_read:
        xp_service.award(current_user.id, amount=5, reason=f"kb:read:week:{week}")

    return render_template(
        "kb/_read_button.html", awarded=True, week=week, first_read=is_first_read
    )


@bp.route("/week/<int:week>/practice")
@login_required
def practice_page(week: int):
    """صفحه رانر تمرین تعاملی تمام‌صفحه شبیه دولینگو."""
    week_obj = _get_visible_week_or_404(week)
    session_data = practice_service.load_practice_session(week, current_user.id)
    if not session_data or not session_data.get("challenges"):
        flash("تمرین تعاملی فعالی برای این هفته یافت نشد.", "warning")
        return redirect(url_for("kb.week_page", week=week))

    # ثبت رویداد شروع جلسه تمرین
    event_service.log_event(
        current_user.id,
        "session_start",
        {"week": week, "type": "practice_runner"}
    )

    return render_template(
        "kb/practice_runner.html",
        week=week,
        is_global=False,
        session_id="",
        week_title=week_obj.title,
        session_data=session_data,
        challenges_json=json.dumps(session_data["challenges"], ensure_ascii=False),
        user_xp=current_user.xp,
        user_streak=current_user.streak,
    )


@bp.route("/week/<int:week>/practice/submit", methods=["POST"])
@login_required
def submit_practice_challenge(week: int):
    """بررسی و اعتبارسنجی پاسخ یک چالش خاص و اعطای XP."""
    _get_visible_week_or_404(week)
    data = request.get_json(silent=True) or request.form.to_dict() or {}
    challenge_id = data.get("challenge_id") or data.get("question_id")
    user_answer = data.get("answer") if "answer" in data else data.get("answer_value")
    hints_used = int(data.get("hints_used", 0))

    if not challenge_id or user_answer is None:
        return jsonify({"success": False, "message": "اطلاعات ارسالی ناقص است."}), 400

    result = practice_service.submit_challenge_attempt(
        user_id=current_user.id,
        week=week,
        challenge_id=challenge_id,
        user_answer=user_answer,
        hints_used=hints_used,
    )
    return jsonify(result)


@bp.route("/week/<int:week>/practice/complete", methods=["POST"])
@login_required
def complete_practice(week: int):
    """ثبت اتمام کل جلسه تمرین، محاسبه احتمال بازگشت و ثبت لاگ."""
    _get_visible_week_or_404(week)
    summary = request.get_json(silent=True) or {}
    result = practice_service.complete_practice_session(
        user_id=current_user.id,
        week=week,
        summary=summary,
    )
    return jsonify(result)


@bp.route("/week/<int:week>/practice/refill-hearts", methods=["POST"])
@login_required
def refill_practice_hearts(week: int):
    """احیای کامل قلب‌های تمرین هفته با کسر ۲۰ XP."""
    _get_visible_week_or_404(week)
    REFILL_COST = 20
    user_xp = current_user.xp or 0
    if user_xp < REFILL_COST:
        return jsonify({
            "success": False,
            "message": f"برای احیای قلب‌ها حداقل به {REFILL_COST} XP نیاز داری. موجودی فعلی: {user_xp} XP"
        }), 400

    current_user.xp = user_xp - REFILL_COST
    stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    log = XPLog(
        user_id=current_user.id,
        amount=-REFILL_COST,
        reason=f"practice:hearts:refill:w{week}:{stamp}",
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "قلب‌های شما با موفقیت شارژ شدند!",
        "hearts": 5,
        "current_xp": current_user.xp,
    })
