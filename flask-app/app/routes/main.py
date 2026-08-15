"""صفحه‌ی اصلی (لندینگ عمومی)، داشبورد دانش‌آموز، و health check.

معماری دسترسی (طبق تصمیم کاربر):
    /            — لندینگ عمومی (بدون داده‌ی شخصی، دکمه‌ی ورود)
    /dashboard   — داشبورد دانش‌آموز (login_required)
    /health      — uptime monitoring (عمومی)
"""
from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

from app.services import progress as progress_service

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """لندینگ عمومی — معرفی کلاس، بدون داده‌ی شخصی.

    اگر کاربر از قبل لاگین کرده باشد، یک بنر «ورود به پنل» نمایش می‌دهیم
    تا مستقیم به /dashboard برود. اما خود محتوا عمومی است.
    """
    return render_template("index.html")


@bp.route("/dashboard")
@login_required
def dashboard():
    """داشبورد دانش‌آموز — فقط کاربران واردشده.

    خلاصه‌ی کامل: پیشرفت مدرک، آمار (XP/استریک/تکالیف)، تکالیف نزدیک، هفته‌ی فعلی.
    """
    stats = progress_service.get_user_stats(current_user.id)
    certificate = progress_service.get_certificate_progress(current_user.id)
    upcoming = progress_service.get_upcoming_assignments(current_user.id, limit=3)
    rank = progress_service.get_class_rank(current_user.id)

    # هفته‌های منتشرشده — برای نقشه راه (مسیر یادگیری)
    from app.models import Week
    all_weeks = Week.query.order_by(Week.number).all()
    weeks_data = [{"number": w.number, "title": w.title, "is_published": w.is_published} for w in all_weeks]

    return render_template(
        "dashboard/index.html",
        stats=stats,
        certificate=certificate,
        upcoming=upcoming,
        rank=rank,
        weeks_data=weeks_data,
    )


@bp.route("/health")
def health():
    """برای uptime monitoring — پاسخ سبک بدون تمپلیت."""
    return jsonify(status="ok", service="anzali-cs50-hub")
