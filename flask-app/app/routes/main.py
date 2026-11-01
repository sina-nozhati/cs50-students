"""صفحه‌ی اصلی (لندینگ عمومی)، داشبورد دانش‌آموز، و health check.

معماری دسترسی (طبق تصمیم کاربر):
    /            — لندینگ عمومی (بدون داده‌ی شخصی، دکمه‌ی ورود)
    /dashboard   — داشبورد دانش‌آموز (login_required)
    /health      — uptime monitoring (عمومی)
"""
from flask import Blueprint, render_template, jsonify, redirect, url_for, flash, request, session
from flask_login import login_required, current_user

from app.services import progress as progress_service
from app.services import notifications as notif_service
from app.services import streak as streak_service
from app.services import events as event_service
from app.services import diagnostics as diag_service
from app.services import cohorts as cohort_service

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
