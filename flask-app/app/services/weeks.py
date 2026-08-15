"""منطق مدیریت هفته‌ها — انتشار، محتوا، و بازیابی.

این ماژول لایه‌ی نازکی بین routeها و مدل Week است:
  - دانش‌آموز فقط هفته‌های منتشرشده را می‌بیند (get_published_weeks).
  - ادمین میتواند انتشار، عنوان، و محتوای HTML هفته را مدیریت کند.

امنیت محتوا (B3): محتوای HTML قبل از ذخیره یک پاکسازی سبک می‌شود تا در صورت
اشتباه ادمین (یا آپلود فایل غیرقابل‌اعتماد)، خطر اجرای اسکریپت کاهش یابد.
این یک دفاع در عمق (defense in depth) است، نه جایگزین اعتماد به ادمین.
"""
import re
from datetime import datetime

from flask import abort

from app import db
from app.models import Week


# ──────────────────────────────────────────────────────────────────────────────
# پاکسازی سبک HTML — حذف <script> و on*= هندلرها (defense in depth).
# توجه: ادمین منبع معتبری است، اما اگر یک روز کسی فایل HTML آلوده آپلود کند،
# این لایه از اجرای خودکار اسکریپت جلوگیری میکند.
# ──────────────────────────────────────────────────────────────────────────────
_SCRIPT_RE = re.compile(r"<script\b[^>]*>.*?</script>", re.IGNORECASE | re.DOTALL)
_ONATTR_RE = re.compile(
    r"\s+(on\w+)\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+)", re.IGNORECASE
)
_IFRAME_RE = re.compile(r"<iframe\b[^>]*>.*?</iframe>", re.IGNORECASE | re.DOTALL)


def sanitize_html(html: str) -> str:
    """حذف تگ‌های خطرناک از HTML محتوای هفته.

    این تابع یک پاکساز سبک است نه یک sanitiser کامل (مثل bleach).
    برای محتوای ادمین کافی است، اما هرگز برای محتوای کاربر عادی استفاده نشود.
    """
    if not html:
        return ""
    html = _SCRIPT_RE.sub("", html)
    html = _ONATTR_RE.sub("", html)
    html = _IFRAME_RE.sub("", html)
    return html


# ──────────────────────────────────────────────────────────────────────────────
# کوئریها
# ──────────────────────────────────────────────────────────────────────────────
def get_published_weeks() -> list[Week]:
    """همه‌ی هفته‌های منتشرشده، مرتب بر اساس شماره — برای دانش‌آموز."""
    return (
        Week.query.filter_by(is_published=True)
        .order_by(Week.number.asc())
        .all()
    )


def get_all_weeks() -> list[Week]:
    """همه‌ی هفته‌ها (منتشر و نامنتشر) — فقط برای ادمین."""
    return Week.query.order_by(Week.number.asc()).all()


def get_week_by_number(number: int) -> Week | None:
    """یک هفته با شماره، یا None."""
    return Week.query.filter_by(number=number).first()


def get_week_or_404(number: int) -> Week:
    """یک هفته با شماره، یا 404 اگر وجود ندارد."""
    week = get_week_by_number(number)
    if week is None:
        abort(404)
    return week


# ──────────────────────────────────────────────────────────────────────────────
# تغییرات (mutations)
# ──────────────────────────────────────────────────────────────────────────────
def toggle_publish(week_number: int) -> bool:
    """وضعیت انتشار هفته را تغییر میدهد.

    Returns:
        مقدار جدید is_published.
    """
    week = get_week_or_404(week_number)
    week.is_published = not week.is_published
    db.session.commit()
    return week.is_published


def update_content(
    week_number: int, content_html: str | None, title: str | None = None, content_url: str | None = None
) -> Week:
    """محتوای HTML، لینک خارجی، و/یا عنوان هفته را به‌روزرسانی میکند.

    محتوا قبل از ذخیره با sanitize_html پاکسازی میشود.
    """
    week = get_week_or_404(week_number)
    if title is not None:
        title = title.strip()
        if title:
            week.title = title
    week.content_html = sanitize_html(content_html) if content_html else None
    
    if content_url is not None:
        week.content_url = content_url.strip() if content_url.strip() else None

    db.session.commit()
    return week


def import_html_from_text(week_number: int, raw_html: str) -> Week:
    """مستی HTML خام (مثلاً از آپلود فایل) را در هفته ذخیره میکند.

    نام مستعاری برای update_content با تمرکز بر آپلود فایل.
    """
    return update_content(week_number, content_html=raw_html)
