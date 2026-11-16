"""صفحه‌ی اصلی (لندینگ عمومی)، داشبورد دانش‌آموز، و health check.

معماری دسترسی (طبق تصمیم کاربر):
    /            — لندینگ عمومی (بدون داده‌ی شخصی، دکمه‌ی ورود)
    /dashboard   — داشبورد دانش‌آموز (login_required)
    /health      — uptime monitoring (عمومی)
"""
import json
from flask import Blueprint, render_template, jsonify, redirect, url_for, flash, request, session
from flask_login import login_required, current_user

from app.services import progress as progress_service
from app.services import notifications as notif_service
from app.services import streak as streak_service
from app.services import events as event_service
from app.services import diagnostics as diag_service
from app.services import cohorts as cohort_service
from app.services import adaptive as adaptive_service
from app.services import hearts as hearts_service
from app import db
from datetime import datetime
from app.models import utc_now, XPLog

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """لندینگ عمومی — معرفی کلاس، بدون داده‌ی شخصی.

    اگر کاربر از قبل لاگین کرده باشد، یک بنر «ورود به پنل» نمایش می‌دهیم
    تا مستقیم به /dashboard برود. اما خود محتوا عمومی است.
    """
    from app.content import loader
    curriculum_weeks = loader.list_weeks()
    return render_template("index.html", curriculum_weeks=curriculum_weeks)


@bp.route("/dashboard")
@login_required
def dashboard():
    """داشبورد دانش‌آموز — فقط کاربران واردشده.

    خلاصه‌ی کامل: پیشرفت مدرک، آمار، تکالیف باز، بازخورد جدید، اعلان‌ها.
    """
    stats = progress_service.get_user_stats(current_user.id)
    certificate = progress_service.get_certificate_progress(current_user.id)
    upcoming = progress_service.get_open_assignments(current_user.id, limit=5)
    rank = progress_service.get_class_rank(current_user.id)
    recent_feedback = progress_service.get_recent_feedback(current_user.id, limit=5)
    notifications = notif_service.list_for_user(current_user.id, limit=8)
    unread_notifications = notif_service.unread_count(current_user.id)

    from app.models import Week
    from app.content.loader import list_weeks as content_weeks
    # ترتیب نمایش مانند کاتالوگ محتوا؛ فقط هفته‌های موجود در DB
    db_map = {w.number: w for w in Week.query.all()}
    weeks_data = []
    for item in content_weeks():
        w = db_map.get(item["number"])
        if w is None:
            continue
        weeks_data.append({
            "number": w.number,
            "title": item["title_fa"],
            "is_published": w.is_published,
            "has_pset": item.get("has_pset", True),
        })

    from app.models import WeekProgress
    wp = WeekProgress.query.filter_by(
        user_id=current_user.id, week=certificate["current_week"], kb_read=True
    ).first()
    weekly_goal = {
        "week": certificate["current_week"],
        "done": wp is not None,
        "label": f"مطالعهٔ پایگاه دانش هفته {certificate['current_week']}",
    }

    # ثبت رویداد ورود به داشبورد با تشخیص منبع ورود (اخلاقی و بدون ردگیری سخت‌افزاری)
    ref = request.args.get("ref", "direct")
    event_service.log_event(
        user_id=current_user.id,
        event_type="app_open",
        payload={"entry_point": ref}
    )

    streak_history = streak_service.get_streak_history(current_user.id, days=7)
    xp_history = progress_service.get_xp_history(current_user.id, limit=5)
    diag_summary = diag_service.get_student_diagnostic_profile(current_user.id)

    # مأموریت‌های روزانه و دستاوردها (Gamification Core)
    from app.services import achievements as achievement_service, quests as quest_service
    daily_quests = quest_service.get_or_create_daily_quests(current_user.id)
    achievements_data = achievement_service.get_user_achievements(current_user.id)

    # اطلاعات چنددوره‌ای کاربر (Multi-Cohort Context)
    active_cohort = cohort_service.get_active_cohort_for_user(
        current_user.id, session.get("active_cohort_id")
    )
    user_enrollments = cohort_service.get_user_enrollments(current_user.id)

    return render_template(
        "dashboard/index.html",
        stats=stats,
        certificate=certificate,
        upcoming=upcoming,
        rank=rank,
        weeks_data=weeks_data,
        recent_feedback=recent_feedback,
        notifications=notifications,
        unread_notifications=unread_notifications,
        weekly_goal=weekly_goal,
        streak_history=streak_history,
        xp_history=xp_history,
        diag_summary=diag_summary,
        daily_quests=daily_quests,
        achievements_data=achievements_data,
        active_cohort=active_cohort,
        user_enrollments=user_enrollments,
    )


@bp.route("/cohort/switch/<int:cohort_id>", methods=["POST"])
@login_required
def switch_cohort(cohort_id: int):
    """تغییر دوره فعال دانش‌آموز."""
    success = cohort_service.switch_user_active_cohort(current_user.id, cohort_id)
    if success:
        session["active_cohort_id"] = cohort_id
        flash("نوبت برگزاری فعال شما با موفقیت تغییر کرد.", "success")
    else:
        flash("شما در این دوره آموزشی عضویت ندارید.", "error")
    next_url = request.form.get("next") or url_for("main.dashboard")
    return redirect(next_url)


@bp.route("/my-courses")
@login_required
def my_courses():
    """صفحه اختصاصی دوره‌های من و مدیریت عضویت‌های چندگانه."""
    user_enrollments = cohort_service.get_user_enrollments(current_user.id)
    active_cohort = cohort_service.get_active_cohort_for_user(
        current_user.id, session.get("active_cohort_id")
    )
    return render_template(
        "dashboard/my_courses.html",
        user_enrollments=user_enrollments,
        active_cohort=active_cohort,
    )


@bp.route("/diagnostics")
@login_required
def diagnostics():
    """کلینیک یادگیری، رادار نقاط ضعف و جعبه اشتباهات دانش‌آموز."""
    profile = diag_service.get_student_diagnostic_profile(current_user.id)
    return render_template("learning/diagnostics.html", profile=profile)


@bp.route("/notifications/<int:notification_id>/read", methods=["POST"])
@login_required
def mark_notification_read(notification_id: int):
    notif_service.mark_read(notification_id, current_user.id)
    next_url = request.form.get("next") or url_for("main.dashboard")
    return redirect(next_url)


@bp.route("/notifications/read-all", methods=["POST"])
@login_required
def mark_all_notifications_read():
    count = notif_service.mark_all_read(current_user.id)
    flash(f"{count} اعلان به‌عنوان خوانده علامت خورد.", "info")
    return redirect(url_for("main.dashboard"))


@bp.route("/offline")
def offline():
    """صفحه حالت آفلاین برای Service Worker PWA."""
    return render_template("errors/offline.html")


@bp.route("/health")
def health():
    """برای uptime monitoring — پاسخ سبک بدون تمپلیت."""
    return jsonify(status="ok", service="anzali-cs50-hub")


@bp.route("/practice", methods=["GET"])
@login_required
def practice():
    """شروع یا ادامه نشست ۵ دقیقه‌ای تمرین تطبیقی."""
    session_data = adaptive_service.start_user_practice_session(current_user.id)
    if (
        request.is_json
        or request.headers.get("Accept") == "application/json"
        or request.args.get("format") == "json"
    ):
        return jsonify(session_data)

    bank = adaptive_service.load_question_bank_for_practice()
    bank_map = {item["id"]: item for item in bank}
    items = [bank_map[iid] for iid in session_data.get("item_ids", []) if iid in bank_map]

    heart_info = hearts_service.get_user_hearts(current_user.id)
    return render_template(
        "kb/practice_runner.html",
        week=None,
        is_global=True,
        session_id=session_data.get("session_id", ""),
        week_title="تمرین تطبیقی ۵ دقیقه‌ای (Adaptive Practice)",
        session_data=session_data,
        challenges_json=json.dumps(items, ensure_ascii=False),
        user_xp=current_user.xp,
        user_streak=current_user.streak,
        user_hearts=heart_info["hearts"],
        cooldown_seconds=heart_info["cooldown_seconds"],
        is_out_of_hearts=heart_info["is_out_of_hearts"],
    )


@bp.route("/practice/answer", methods=["POST"])
@login_required
def practice_answer():
    """ثبت پاسخ یک پرسش در نشست تطبیقی جاری."""
    data = request.get_json(silent=True) or request.form.to_dict() or {}
    session_id = data.get("session_id")
    question_id = data.get("question_id") or data.get("challenge_id")
    answer = data.get("answer") if "answer" in data else data.get("answer_value")

    if not session_id:
        state = adaptive_service.get_or_create_adaptive_state(current_user.id)
        current = state.get("current_session")
        if not current:
            current = adaptive_service.start_user_practice_session(current_user.id)
        if current:
            session_id = current.get("session_id")

    if not session_id or not question_id:
        return jsonify({"success": False, "error": "شناسه نشست یا شناسه سوال نامعتبر است."}), 400

    res = adaptive_service.submit_user_practice_answer(
        user_id=current_user.id,
        session_id=session_id,
        question_id=question_id,
        answer_value=answer,
    )
    if not res.get("is_correct", False):
        heart_info = hearts_service.drain_user_heart(current_user.id)
    else:
        heart_info = hearts_service.get_user_hearts(current_user.id)
    res["hearts"] = heart_info["hearts"]
    res["cooldown_seconds"] = heart_info["cooldown_seconds"]
    res["is_out_of_hearts"] = heart_info["is_out_of_hearts"]
    return jsonify(res)


@bp.route("/practice/finish", methods=["POST"])
@login_required
def practice_finish():
    """پایان نشست تمرین تطبیقی و به‌روزرسانی استریک."""
    data = request.get_json(silent=True) or request.form.to_dict()
    session_id = data.get("session_id")

    if not session_id:
        state = adaptive_service.get_or_create_adaptive_state(current_user.id)
        current = state.get("current_session")
        if current:
            session_id = current.get("session_id")

    if not session_id:
        return jsonify({"success": False, "error": "نشست فعالی یافت نشد."}), 400

    res = adaptive_service.complete_user_practice_session(
        user_id=current_user.id,
        session_id=session_id,
    )
    return jsonify(res)


@bp.route("/practice/refill-hearts", methods=["POST"])
@login_required
def practice_refill_hearts():
    """احیای کامل ۵ قلب در تمرین تطبیقی با کسر ۲۰ XP."""
    success, msg, new_xp = hearts_service.refill_user_hearts_with_xp(
        current_user.id, "practice:hearts:refill:global"
    )
    if not success:
        return jsonify({"success": False, "message": msg}), 400
    return jsonify({
        "success": True,
        "message": msg,
        "hearts": 5,
        "current_xp": new_xp,
    })


@bp.route("/practice/restore-one-heart", methods=["POST"])
@login_required
def practice_restore_one_heart():
    """احیای یک قلب با انجام موفق چالش مفهومی."""
    status = hearts_service.restore_one_heart(current_user.id)
    return jsonify({
        "success": True,
        "hearts": status["hearts"],
        "cooldown_seconds": status["cooldown_seconds"],
        "is_out_of_hearts": status["is_out_of_hearts"],
    })


@bp.route("/quests/claim/<int:quest_id>", methods=["POST"])
@login_required
def claim_quest(quest_id: int):
    """دریافت پاداش مأموریت روزانه تکمیل‌شده."""
    from app.services import quests as quest_service
    res = quest_service.claim_quest_reward(current_user.id, quest_id)
    status_code = 200 if res.get("success") else 400
    return jsonify(res), status_code


@bp.route("/streak-freeze/buy", methods=["POST"])
@login_required
def buy_streak_freeze():
    """خرید محافظ استریک با ۵۰ XP."""
    res = streak_service.buy_streak_freeze(current_user.id)
    status_code = 200 if res.get("success") else 400
    return jsonify(res), status_code


@bp.route("/api/quests", methods=["GET"])
@login_required
def api_daily_quests():
    """استعلام مأموریت‌های روز جاری کاربر."""
    from app.services import quests as quest_service
    quests = quest_service.get_or_create_daily_quests(current_user.id)
    return jsonify({"success": True, "quests": quests})


@bp.route("/api/achievements", methods=["GET"])
@login_required
def api_achievements():
    """استعلام فهرست دستاوردها و وضعیت بازگشایی کاربر."""
    from app.services import achievements as achievement_service
    data = achievement_service.get_user_achievements(current_user.id)
    return jsonify({"success": True, **data})


@bp.route("/api/leaderboard/weekly", methods=["GET"])
@login_required
def api_weekly_leaderboard():
    """استعلام رتبه‌بندی ۷ روز اخیر کلاس."""
    from app.services import xp as xp_service
    items = xp_service.weekly_leaderboard(limit=10)
    return jsonify({"success": True, "leaderboard": items})


@bp.route("/verify/<string:cert_id>", methods=["GET"])
def verify_certificate_page(cert_id: str):
    """صفحه عمومی استعلام و تایید اصالت گواهینامه برای کارفرمایان."""
    from app.services import certificate as cert_service
    res = cert_service.verify_certificate(cert_id)
    return render_template("certificate/verify.html", res=res, cert_id=cert_id)


@bp.route("/certificate", methods=["GET"])
@login_required
def certificate_view():
    """مشاهده وضعیت گواهینامه و نقشه تسلط دانشجو."""
    from app.models import Certificate
    from app.services import certificate as cert_service
    cert = Certificate.query.filter_by(user_id=current_user.id, is_revoked=False).first()
    eval_res = cert_service.evaluate_certification_eligibility(current_user.id)
    return render_template(
        "certificate/student_view.html",
        cert=cert,
        eval_res=eval_res,
        is_eligible=eval_res.get("is_eligible", False),
    )


@bp.route("/certificate/claim", methods=["POST"])
@login_required
def claim_certificate():
    """صدور رسمی گواهینامه پس از احراز شرایط تسلط."""
    from app.services import certificate as cert_service
    success, msg, cert = cert_service.issue_certificate(current_user.id)
    if success:
        flash(msg, "success")
    else:
        flash(msg, "error")
    return redirect(url_for("main.certificate_view"))
