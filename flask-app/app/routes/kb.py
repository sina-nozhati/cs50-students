"""ماژول پایگاه دانش (Knowledge Base).

روتها:
    /kb/week/<n>        — صفحه‌ی هفته n با محتوای آموزشی
    /kb/week/<n>/read   — (POST) دکمه‌ی «من خواندم» → +5 XP با HTMX

مدیریت دسترسی (طبق فاز A):
    - دانش‌آموز فقط هفته‌های **منتشرشده** را می‌بیند؛ در غیر این صورت 404.
    - XP فقط وقتی داده میشود که هفته منتشر باشد **و** محتوای آموزشی داشته باشد.
      این از تقلب رایگان گرفتن XP برای هفته‌ی خالی جلوگیری میکند.
"""
from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.services import xp as xp_service
from app.services import progress as progress_service
from app.services import weeks as weeks_service
from app.models import WeekProgress

bp = Blueprint("kb", __name__, url_prefix="/kb")


@bp.before_request
@login_required
def _require_login():
    """همه‌ی روت‌های /kb نیاز به لاگین دارند (طبق سیاست دسترسی)."""
    pass


def _get_visible_week_or_404(week: int) -> "weeks_service.Week":
    """هفته را برمیگرداند؛ اگر وجود ندارد یا منتشر نشده → 404.

    این تابع کنترل دسترسی مرکزی برای دانش‌آموز است.
    """
    week_obj = weeks_service.get_week_by_number(week)
    if week_obj is None or not week_obj.is_published:
        abort(404)
    return week_obj


@bp.route("/week/<int:week>")
def week_page(week: int):
    week_obj = _get_visible_week_or_404(week)

    # آیا این کاربر قبلاً خوانده؟ از DB می‌خوانیم
    already_read = (
        WeekProgress.query.filter_by(
            user_id=current_user.id, week=week, kb_read=True
        ).first()
        is not None
    )
    # دکمه‌ی «من خواندم» فقط اگر هفته محتوا داشته باشد نمایش داده میشود
    can_mark_read = bool(week_obj.content_html or week_obj.content_url)

    # دریافت منابع هفته برای نمایش در همان صفحه
    from app.services import resources as res_service
    files = res_service.list_for_week(week)

    return render_template(
        "kb/week.html",
        week=week,
        title=week_obj.title,
        content_html=week_obj.content_html,
        content_url=week_obj.content_url,
        already_read=already_read,
        can_mark_read=can_mark_read,
        files=files,
    )


@bp.route("/week/<int:week>/read", methods=["POST"])
@login_required
def mark_read(week: int):
    """دکمه‌ی «من خواندم» — idempotent: فقط اولین بار ۵ XP میدهد.

    نکته آموزشی: چون HTMX این روت را صدا میزند، ما کل صفحه را رفرش نمیکنیم،
    بلکه فقط fragment دکمه را برمیگردانیم.

    امنیت (سه لایه):
      ۱. هفته باید منتشر باشد — وگرنه 404.
      ۲. هفته باید محتوای آموزشی داشته باشد — وگرنه XP نمیده (جلوگیری از رایگان‌گرفتن).
      ۳. WeekProgress.kb_read چک میشود تا کاربر نتواند با کلیک چندباره بی‌نهایت XP بگیرد.
    """
    week_obj = _get_visible_week_or_404(week)

    # اگر هفته محتوا ندارد، XP نمیده — کاربر باید واقعاً چیزی خوانده باشد.
    if not (week_obj.content_html or week_obj.content_url):
        flash("این هفته هنوز محتوایی ندارد — نمی‌توانید آن را «خوانده» علامت بزنید.", "error")
        return redirect(url_for("kb.week_page", week=week))

    # mark_kb_read فقط اولین بار True برمی‌گرداند — بقیه‌ی دفعات XP نمی‌دهد
    is_first_read = progress_service.mark_kb_read(current_user.id, week)
    if is_first_read:
        xp_service.award(current_user.id, amount=5, reason=f"Read KB Week {week}")

    return render_template(
        "kb/_read_button.html", awarded=True, week=week, first_read=is_first_read
    )
