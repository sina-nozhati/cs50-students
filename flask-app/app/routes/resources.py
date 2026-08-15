"""ماژول منابع — ۹ کارت هفته + لیست فایلهای هر هفته برای دانلود.

روتها:
    /resources                       — صفحه‌ی ۹ کارت هفته
    /resources/week/<n>              — لیست فایلهای هفته n
    /resources/file/<id>/download    — دانلود مستقیم یک فایل
"""
import os

from flask import (
    Blueprint,
    render_template,
    abort,
    current_app,
    send_from_directory,
)
from flask_login import login_required

from app.services import resources as res_service

bp = Blueprint("resources", __name__, url_prefix="/resources")


@bp.before_request
@login_required
def _require_login():
    """همه‌ی روت‌های /resources نیاز به لاگین دارند (طبق سیاست دسترسی)."""
    pass

from app.models import Week

@bp.route("/")
def index():
    """صفحه‌ی کارت‌های هفته — اطلاعات هر هفته از DB خوانده میشود."""
    db_weeks = Week.query.order_by(Week.number).all()
    weeks = []
    for w in db_weeks:
        weeks.append(
            {
                "week": w.number,
                "title": w.title,
                "file_count": res_service.count_for_week(w.number),
                "is_published": w.is_published
            }
        )
    return render_template("resources/index.html", weeks=weeks)


@bp.route("/week/<int:week>")
def week_files(week: int):
    """
    ریدایرکت به صفحه یکپارچه هفته در پایگاه دانش.
    این مسیر قدیمی برای سازگاری حفظ شده تا به مسیر جدید و کامل‌تر هدایت شود.
    """
    from flask import redirect, url_for
    return redirect(url_for('kb.week_page', week=week))


@bp.route("/file/<int:resource_id>/download")
def download(resource_id: int):
    """دانلود مستقیم فایل از static/downloads/weekN/FILENAME.

    send_from_directory امن است و از path traversal جلوگیری میکند.
    """
    res = res_service.get_or_404(resource_id)
    directory = os.path.join(current_app.config["UPLOAD_FOLDER"], f"week{res.week}")
    # download_name با display_name فارسی تا مرورگر نام زیبا نشان دهد
    ext = res.filename.rsplit(".", 1)[-1] if "." in res.filename else "bin"
    return send_from_directory(
        directory,
        res.filename,
        as_attachment=True,
        download_name=f"{res.display_name}.{ext}",
    )
