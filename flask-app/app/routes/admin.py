"""پنل ادمین — مدیریت کامل کلاس.

روت‌ها (همه نیاز به نقش ادمین دارند):
    /admin/                            — داشبورد تحلیلی
    /admin/users                       — لیست دانش‌آموزان
    /admin/users/create                — (GET/POST) ثبت دانش‌آموز
    /admin/users/<id>/edit             — (GET/POST) ویرایش کاربر
    /admin/users/<id>/delete           — (POST) حذف کاربر
    /admin/users/<id>/detail           — جزئیات کامل دانش‌آموز
    /admin/assignments                 — لیست تکالیف
    /admin/assignments/create          — (GET/POST) ایجاد تکلیف
    /admin/assignments/<id>/edit       — (GET/POST) ویرایش تکلیف
    /admin/assignments/<id>/toggle     — (POST) فعال/غیرفعال تکلیف
    /admin/submissions                 — لیست تحویل‌ها + نمره‌دهی
    /admin/submissions/<id>/grade      — (GET/POST) نمره‌دهی یک تحویل
    /admin/upload                      — (GET/POST) آپلود فایل
    /admin/resources                   — لیست منابع
    /admin/resources/<id>/toggle       — (POST) تغییر وضعیت منبع
    /admin/weeks                       — لیست هفته‌ها
    /admin/weeks/<n>/edit              — (GET/POST) ویرایش هفته
    /admin/weeks/<n>/toggle            — (POST) انتشار/مخفی هفته
"""
import os
import tempfile
from pathlib import Path
from datetime import datetime
from functools import wraps

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app,
    jsonify,
)
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app import db
from app.models import Resource, Submission, Assignment, User, Course, Cohort, Enrollment, KBPackageInstall
from app.services import resources as res_service
from app.services import weeks as weeks_service
from app.services import users as users_service
from app.services import assignments_admin as assignments_service
from app.services import analytics as analytics_service
from app.services import submissions as sub_service
from app.services import progress as progress_service
from app.services import engagement as engagement_service
from app.services import notifications as notif_service
from app.services import kb_admin
from app.services import diagnostics as diag_service
from app.services import cohorts as cohort_service
from app.services import downloads as downloads_service
from app.services import events as event_service

bp = Blueprint("admin", __name__, url_prefix="/admin")


def admin_required(f):
    """Decorator: فقط کاربر ادمین اجازه‌ی دسترسی دارد.

    نکته: login_required اول اجرا میشود تا current_user مقدار داشته باشد.
    """

    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash("دسترسی ادمین لازم است.", "error")
            return redirect(url_for("main.dashboard"))
        return f(*args, **kwargs)

    return decorated


def _allowed_file(filename: str) -> bool:
    """allowlist پسوندها — امنیت در برابر آپلود فایل مخرب.

    فقط pdf و zip مجاز هستند (طبق ALLOWED_EXTENSIONS در config).
    """
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]
    )


# ──────────────────────────────────────────────────────────────────────────────
# داشبورد تحلیلی ادمین
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/")
@admin_required
def index():
    """داشبورد تحلیلی — آمار کلی، هشدارها، وضعیت هفته‌ها و ریسک ریزش."""
    overview = analytics_service.get_overview()
    assignment_stats = analytics_service.get_assignment_stats()
    weekly_progress = analytics_service.get_weekly_progress_overview()
    low_engagement = analytics_service.get_low_engagement_students(days=3)
    top_performers = analytics_service.get_top_performers(limit=5)
    students_at_risk = engagement_service.get_students_at_risk()

    # تعداد تحویل‌های بدون نمره
    ungraded_count = Submission.query.filter(Submission.grade.is_(None)).count()
    cohort_diagnostics = diag_service.get_cohort_diagnostic_overview()

    return render_template(
        "admin/index.html",
        overview=overview,
        assignment_stats=assignment_stats,
        weekly_progress=weekly_progress,
        low_engagement=low_engagement,
        top_performers=top_performers,
        ungraded_count=ungraded_count,
        students_at_risk=students_at_risk,
        cohort_diagnostics=cohort_diagnostics,
    )


@bp.route("/engagement/message", methods=["POST"])
@admin_required
def send_mentor_message():
    """ارسال پیام تشویقی و راهنمایی مستقیم از طرف مدرس به دانش‌آموز (کاملاً دستی، بدون ارسال خودکار)."""
    user_id = request.form.get("user_id", type=int)
    title = request.form.get("title", "پیام راهنمایی از طرف مدرس 💡")
    body = request.form.get("body", "").strip()

    if not user_id or not body:
        flash("متن پیام و شناسه دانش‌آموز الزامی است.", "error")
        return redirect(url_for("admin.index"))

    notif_service.create(
        user_id=user_id,
        title=title,
        body=body,
        link="/dashboard"
    )
    flash("پیام راهنمایی با موفقیت برای دانش‌آموز ارسال شد.", "success")
    return redirect(url_for("admin.index"))


# ──────────────────────────────────────────────────────────────────────────────
# مدیریت کاربران
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/users")
@admin_required
def users_list():
    """لیست دانش‌آموزان با آمار."""
    students = users_service.list_all_students()
    return render_template("admin/users.html", students=students)


@bp.route("/users/create", methods=["GET", "POST"])
@admin_required
def users_create():
    """ثبت دانش‌آموز جدید با پشتیبانی چنددوره‌ای، تلگرام، نقش و گیمیفیکیشن اولیه."""
    cohorts = Cohort.query.filter_by(status="active").order_by(Cohort.year.desc(), Cohort.id.desc()).all()
    if not cohorts:
        cohorts = Cohort.query.order_by(Cohort.id.desc()).all()

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        telegram_id = request.form.get("telegram_id", "").strip() or None
        is_admin = request.form.get("is_admin") in ("true", "1", "on")
        is_active = request.form.get("is_active", "1") in ("true", "1", "on")
        initial_xp = request.form.get("initial_xp", 0, type=int) or 0
        initial_streak = request.form.get("initial_streak", 0, type=int) or 0
        cohort_id = request.form.get("cohort_id", type=int)
        cohort_role = request.form.get("cohort_role", "student")

        if not username or not password:
            flash("نام کاربری و رمز عبور الزامی است.", "error")
            return redirect(request.url)

        if len(password) < 4:
            flash("رمز عبور باید حداقل ۴ کاراکتر باشد.", "error")
            return redirect(request.url)

        try:
            users_service.create_user(
                username=username,
                password=password,
                telegram_id=telegram_id,
                is_admin=is_admin,
                is_active=is_active,
                initial_xp=initial_xp,
                initial_streak=initial_streak,
                cohort_id=cohort_id,
                cohort_role=cohort_role,
            )
            flash(f"کاربر «{username}» با موفقیت ثبت و به سامانه اضافه شد.", "success")
            return redirect(url_for("admin.users_list"))
        except ValueError as e:
            msg = str(e)
            if "Telegram" in msg:
                flash("این شناسه تلگرام قبلاً برای کاربر دیگری ثبت شده است.", "error")
            else:
                flash("این نام کاربری قبلاً استفاده شده است.", "error")
            return redirect(request.url)

    return render_template(
        "admin/user_form.html",
        user=None,
        edit_mode=False,
        cohorts=cohorts,
    )


@bp.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
@admin_required
def users_edit(user_id: int):
    """ویرایش اطلاعات دانش‌آموز با پشتیبانی تلگرام، نقش، وضعیت و دوره."""
    user = db.session.get(User, user_id)
    if not user:
        flash("کاربر یافت نشد.", "error")
        return redirect(url_for("admin.users_list"))

    cohorts = Cohort.query.order_by(Cohort.year.desc(), Cohort.id.desc()).all()
    current_enrollment = Enrollment.query.filter_by(user_id=user.id, is_primary=True).first()

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip() or None
        telegram_id = request.form.get("telegram_id", "").strip() or None
        is_admin = request.form.get("is_admin") in ("true", "1", "on")
        is_active = request.form.get("is_active") in ("true", "1", "on")
        xp_adj = request.form.get("xp_adjustment", 0, type=int)
        cohort_id = request.form.get("cohort_id", type=int)

        try:
            users_service.update_user(
                user_id,
                username=username,
                password=password,
                telegram_id=telegram_id,
                is_admin=is_admin,
                is_active=is_active,
                xp_adjustment=xp_adj,
                cohort_id=cohort_id,
            )
            flash(f"اطلاعات کاربر به‌روزرسانی شد.", "success")
            return redirect(url_for("admin.users_list"))
        except ValueError as e:
            msg = str(e)
            if "Telegram" in msg:
                flash("این شناسه تلگرام قبلاً برای کاربر دیگری ثبت شده است.", "error")
            else:
                flash("این نام کاربری قبلاً توسط شخص دیگری ثبت شده است.", "error")
            return redirect(url_for("admin.users_edit", user_id=user_id))

    return render_template(
        "admin/user_form.html",
        user=user,
        edit_mode=True,
        cohorts=cohorts,
        current_enrollment=current_enrollment,
    )


@bp.route("/users/<int:user_id>/toggle-active", methods=["POST"])
@admin_required
def users_toggle_active(user_id: int):
    """فعال/غیرفعال کردن حساب بدون حذف داده."""
    from app.models import User
    user = db.session.get(User, user_id)
    if not user or user.is_admin:
        flash("کاربر یافت نشد.", "error")
        return redirect(url_for("admin.users_list"))
    new_state = not getattr(user, "is_active", True)
    users_service.set_active(user_id, new_state)
    flash(
        f"حساب «{user.username}» {'فعال' if new_state else 'غیرفعال'} شد.",
        "success",
    )
    return redirect(url_for("admin.users_list"))


@bp.route("/users/<int:user_id>/delete", methods=["POST"])
@admin_required
def users_delete(user_id: int):
    """حذف دانش‌آموز — با cascade."""
    from app.models import User
    user = db.session.get(User, user_id)
    if not user:
        flash("کاربر یافت نشد.", "error")
        return redirect(url_for("admin.users_list"))

    username = user.username
    users_service.delete_user(user_id)
    flash(f"کاربر «{username}» حذف شد.", "success")
    return redirect(url_for("admin.users_list"))


@bp.route("/users/<int:user_id>")
@admin_required
def users_detail_redirect(user_id: int):
    """ریدایرکت به مسیر صحیح جزئیات کاربر."""
    return redirect(url_for("admin.users_detail", user_id=user_id))


@bp.route("/users/<int:user_id>/detail")
@admin_required
def users_detail(user_id: int):
    """صفحه جزئیات کامل دانش‌آموز."""
    detail = users_service.get_user_detail(user_id)
    rank = progress_service.get_class_rank(user_id)
    diagnostics = diag_service.get_student_diagnostic_profile(user_id)
    return render_template(
        "admin/user_detail.html",
        user=detail["user"],
        submissions=detail["submissions"],
        week_progress=detail["week_progress"],
        xp_logs=detail["xp_logs"],
        rank=rank,
        diagnostics=diagnostics,
    )


# ──────────────────────────────────────────────────────────────────────────────
# مدیریت تکالیف
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/assignments")
@admin_required
def assignments_list():
    """لیست تکالیف با آمار تحویل."""
    assignments = assignments_service.list_all()
    # ساخت dict از تعداد تحویل‌ها برای هر تکلیف
    submission_counts = {}
    for a in assignments:
        submission_counts[a.id] = Submission.query.filter_by(assignment_id=a.id).count()
    return render_template(
        "admin/assignments_list.html",
        assignments=assignments,
        submission_counts=submission_counts,
    )


@bp.route("/assignments/create", methods=["GET", "POST"])
@admin_required
def assignments_create():
    """ایجاد تکلیف جدید."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        week = request.form.get("week", 0, type=int)
        due_date_str = request.form.get("due_date", "")
        xp_reward = request.form.get("xp_reward", 20, type=int)
        github_url = request.form.get("github_template_url", "").strip() or None
        description = request.form.get("description", "").strip() or None

        if not title:
            flash("عنوان تکلیف الزامی است.", "error")
            return redirect(request.url)

        try:
            due_date = datetime.fromisoformat(due_date_str)
        except (ValueError, TypeError):
            flash("تاریخ مهلت نامعتبر است.", "error")
            return redirect(request.url)

        assignments_service.create_assignment(
            title=title,
            week=week,
            due_date=due_date,
            xp_reward=xp_reward,
            github_template_url=github_url,
            description=description,
        )
        flash(f"تکلیف «{title}» ایجاد شد.", "success")
        return redirect(url_for("admin.assignments_list"))

    return render_template("admin/assignment_form.html", assignment=None, edit_mode=False)


@bp.route("/assignments/<int:assignment_id>/edit", methods=["GET", "POST"])
@admin_required
def assignments_edit(assignment_id: int):
    """ویرایش تکلیف."""
    assignment = db.get_or_404(Assignment, assignment_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        week = request.form.get("week", 0, type=int)
        due_date_str = request.form.get("due_date", "")
        xp_reward = request.form.get("xp_reward", 20, type=int)
        github_url = request.form.get("github_template_url", "").strip() or None
        description = request.form.get("description", "").strip() or None

        try:
            due_date = datetime.fromisoformat(due_date_str)
        except (ValueError, TypeError):
            flash("تاریخ مهلت نامعتبر است.", "error")
            return redirect(request.url)

        assignments_service.update_assignment(
            assignment_id,
            title=title,
            week=week,
            due_date=due_date,
            xp_reward=xp_reward,
            github_template_url=github_url,
            description=description,
        )
        flash(f"تکلیف «{title}» به‌روزرسانی شد.", "success")
        return redirect(url_for("admin.assignments_list"))

    return render_template(
        "admin/assignment_form.html", assignment=assignment, edit_mode=True
    )


@bp.route("/assignments/<int:assignment_id>/toggle", methods=["POST"])
@admin_required
def assignments_toggle(assignment_id: int):
    """فعال/غیرفعال‌سازی تکلیف."""
    is_active = assignments_service.toggle_active(assignment_id)
    if is_active:
        flash("تکلیف فعال شد.", "success")
    else:
        flash("تکلیف غیرفعال شد.", "info")
    return redirect(url_for("admin.assignments_list"))


# ──────────────────────────────────────────────────────────────────────────────
# نمره‌دهی تحویل‌ها
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/submissions")
@admin_required
def submissions_list():
    """لیست تحویل‌ها با فیلتر."""
    # فیلترها
    assignment_filter = request.args.get("assignment_id", type=int)
    status_filter = request.args.get("status", "all")

    query = (
        Submission.query
        .join(Submission.assignment)
        .join(Submission.student)
        .order_by(Submission.submitted_at.desc())
    )

    if assignment_filter:
        query = query.filter(Submission.assignment_id == assignment_filter)

    if status_filter == "ungraded":
        query = query.filter(Submission.grade.is_(None))
    elif status_filter == "graded":
        query = query.filter(Submission.grade.isnot(None))

    submissions = query.all()
    all_assignments = Assignment.query.order_by(Assignment.title).all()

    return render_template(
        "admin/submissions_list.html",
        submissions=submissions,
        assignments=all_assignments,
        current_filter={"assignment_id": assignment_filter, "status": status_filter},
    )


@bp.route("/submissions/<int:submission_id>/grade", methods=["GET", "POST"])
@admin_required
def submissions_grade(submission_id: int):
    """نمره‌دهی به یک تحویل."""
    submission = db.get_or_404(Submission, submission_id)

    if request.method == "POST":
        grade = request.form.get("grade", type=int)
        feedback = request.form.get("feedback", "").strip()

        if grade is None or grade < 0 or grade > 100:
            flash("نمره باید بین ۰ تا ۱۰۰ باشد.", "error")
            return redirect(request.url)

        sub_service.grade(submission_id, grade=grade, feedback=feedback)
        flash(
            f"نمره «{grade}» برای تحویل {submission.student.username} ثبت شد.",
            "success",
        )
        return redirect(url_for("admin.submissions_list"))

    return render_template("admin/grade_form.html", submission=submission)


# ──────────────────────────────────────────────────────────────────────────────
# آپلود فایل (بدون تغییر عمده)
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/upload", methods=["GET", "POST"])
@admin_required
def upload():
    """فرم آپلود فایل برای یک هفته مشخص.

    فایل با secure_filename امن‌سازی میشود و در static/downloads/weekN/ ذخیره،
    سپس در جدول Resource ثبت میگردد.
    """
    if request.method == "POST":
        week = request.form.get("week", type=int)
        category = request.form.get("category", "extra")
        display_name = request.form.get("display_name", "").strip() or "فایل بدون نام"
        file = request.files.get("file")

        # اعتبارسنجی
        if file is None or file.filename == "":
            flash("فایلی انتخاب نشده.", "error")
            return redirect(request.url)
        if not _allowed_file(file.filename):
            flash("پسوند مجاز نیست (فقط pdf یا zip).", "error")
            return redirect(request.url)
        valid_weeks = [w.number for w in weeks_service.get_all_weeks()]
        if week not in valid_weeks:
            flash("هفته نامعتبر است.", "error")
            return redirect(request.url)

        # secure_filename از path traversal جلوگیری میکند
        safe_name = secure_filename(file.filename) or "upload.bin"
        target_dir = os.path.join(current_app.config["UPLOAD_FOLDER"], f"week{week}")
        os.makedirs(target_dir, exist_ok=True)
        file.save(os.path.join(target_dir, safe_name))

        res_service.create_resource(
            week=week,
            filename=safe_name,
            display_name=display_name,
            category=category,
            uploaded_by=current_user.id,
        )
        flash(f"فایل «{display_name}» برای هفته {week} آپلود شد.", "success")
        return redirect(url_for("admin.resources_list"))

    all_week_numbers = [w.number for w in weeks_service.get_all_weeks()]
    return render_template("admin/upload.html", weeks=all_week_numbers)


# ──────────────────────────────────────────────────────────────────────────────
# مدیریت منابع (بدون تغییر)
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/resources")
@admin_required
def resources_list():
    """لیست همه‌ی منابع با دکمه‌ی انتشار/عدم انتشار."""
    all_resources = Resource.query.order_by(Resource.week, Resource.category).all()
    return render_template("admin/resources.html", resources=all_resources)


@bp.route("/resources/<int:resource_id>/toggle", methods=["POST"])
@admin_required
def toggle_publish(resource_id: int):
    """وضعیت انتشار یک منبع را تغییر میدهد (منتشر/مخفی)."""
    res = db.get_or_404(Resource, resource_id)
    res.is_published = not res.is_published
    db.session.commit()
    flash("وضعیت انتشار تغییر کرد.", "success")
    return redirect(url_for("admin.resources_list"))


# ──────────────────────────────────────────────────────────────────────────────
# مدیریت هفته‌ها (بدون تغییر عمده)
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/weeks")
@admin_required
def weeks_list():
    """لیست همه‌ی هفته‌ها با وضعیت انتشار و دکمه‌ی ویرایش/تغییر وضعیت."""
    weeks = weeks_service.get_all_weeks()
    return render_template("admin/weeks.html", weeks=weeks)


@bp.route("/weeks/create", methods=["GET", "POST"])
@admin_required
def weeks_create():
    """ایجاد هفته جدید."""
    if request.method == "POST":
        number_str = request.form.get("number")
        title = request.form.get("title")
        
        if not number_str or not title:
            flash("شماره هفته و عنوان الزامی است.", "error")
            return redirect(request.url)
            
        try:
            number = int(number_str)
        except ValueError:
            flash("شماره هفته باید یک عدد باشد.", "error")
            return redirect(request.url)
            
        from app.models import Week
        existing = Week.query.filter_by(number=number).first()
        if existing:
            flash("این شماره هفته قبلاً ثبت شده است.", "error")
            return redirect(request.url)
            
        new_week = Week(number=number, title=title, is_published=False)
        db.session.add(new_week)
        db.session.commit()
        
        flash("هفته جدید با موفقیت اضافه شد.", "success")
        return redirect(url_for("admin.weeks_list"))
        
    return render_template("admin/weeks_create.html")


@bp.route("/weeks/<int:week_number>/edit", methods=["GET", "POST"])
@admin_required
def weeks_edit(week_number: int):
    """ویرایش عنوان و محتوای HTML یک هفته.

    دو روش ورود محتوا:
      1. آپلود فایل .html → محتوای فایل جایگزین محتوای فعلی میشود.
      2. ویرایش مستقیم در textarea → برای اصلاح سریع بدون آپلود مجدد.

    اگر هر دو موجود باشند، آپلود فایل اولویت دارد (معمول‌تر و قطعی‌تر).
    """
    week = weeks_service.get_week_or_404(week_number)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content_textarea = request.form.get("content_html", "")
        content_url = request.form.get("content_url", "")
        uploaded_file = request.files.get("content_file")

        # اگر فایل آپلود شده، محتوای آن اولویت دارد
        if uploaded_file and uploaded_file.filename:
            safe_name = secure_filename(uploaded_file.filename) or "content.html"
            if not safe_name.lower().endswith((".html", ".htm")):
                flash("فقط فایل HTML مجاز است.", "error")
                return redirect(request.url)
            try:
                raw = uploaded_file.read().decode("utf-8", errors="replace")
            except Exception:
                flash("خطا در خواندن فایل HTML.", "error")
                return redirect(request.url)
            weeks_service.update_content(week_number, content_html=raw, title=title, content_url=content_url)
            flash("محتوای هفته از فایل آپلود شد.", "success")
        else:
            # وگرنه متن textarea
            weeks_service.update_content(week_number, content_html=content_textarea, title=title, content_url=content_url)
            flash("محتوای هفته ذخیره شد.", "success")

        return redirect(url_for("admin.weeks_list"))

    return render_template("admin/weeks_edit.html", week=week)


@bp.route("/weeks/<int:week_number>/toggle", methods=["POST"])
@admin_required
def weeks_toggle(week_number: int):
    """وضعیت انتشار یک هفته را تغییر میدهد (منتشر/مخفی).

    نکته: وقتی هفته‌ای نامنتشر باشد، دانش‌آموز به صفحه‌ی آن دسترسی ندارد
    و نمیتواند XP بگیرد — این کنترل واقعی دسترسی است.
    """
    is_now_published = weeks_service.toggle_publish(week_number)
    if is_now_published:
        flash("هفته منتشر شد — دانش‌آموزان اکنون میتوانند آن را ببینند.", "success")
    else:
        flash("هفته مخفی شد — دانش‌آموزان دیگر به آن دسترسی ندارند.", "info")
    return redirect(url_for("admin.weeks_list"))


@bp.route("/kb-packages")
@admin_required
def kb_packages_dashboard():
    """داشبورد مدیریت و وضعیت بسته‌های هفتگی پایگاه دانش (KB) با پشتیبانی چنددوره‌ای پویا."""
    courses = Course.query.filter_by(is_active=True).order_by(Course.id).all()
    selected_course_id = request.args.get("course_id", type=int)
    selected_course = None
    if selected_course_id:
        selected_course = db.session.get(Course, selected_course_id)
    if not selected_course and courses:
        selected_course = courses[0]

    weeks_status = kb_admin.get_all_weeks_kb_status()
    recent_installs = KBPackageInstall.query.order_by(KBPackageInstall.installed_at.desc()).limit(10).all()

    downloads_status = downloads_service.get_admin_downloads_status()

    return render_template(
        "admin/kb_packages.html",
        weeks_status=weeks_status,
        courses=courses,
        selected_course=selected_course,
        recent_installs=recent_installs,
        downloads_status=downloads_status,
    )


@bp.route("/kb-packages/upload", methods=["POST"])
@admin_required
def kb_packages_upload():
    """دریافت و استخراج فایل فشرده بسته هفته یا مستر و ادغام آن در پایگاه دانش دوره انتخابی (با پشتیبانی از AJAX و پروگرس بار)."""
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    course_id = request.form.get("course_id", type=int)

    uploaded = request.files.get("package_file")
    target_week_raw = request.form.get("target_week")
    target_week = int(target_week_raw) if target_week_raw and target_week_raw.strip().isdigit() else None

    if not uploaded or not uploaded.filename:
        err = "لطفاً یک فایل فشرده بسته آموزشی (.tar.gz یا .zip) انتخاب کنید."
        flash(err, "error")
        if is_ajax:
            return jsonify({"success": False, "error": err}), 400
        return redirect(url_for("admin.kb_packages_dashboard", course_id=course_id))

    filename = secure_filename(uploaded.filename) or "kb_package.tar.gz"
    lower_name = filename.lower()
    if not (lower_name.endswith(".tar.gz") or lower_name.endswith(".tgz") or lower_name.endswith(".tar") or lower_name.endswith(".zip")):
        err = "فرمت فایل معتبر نیست. لطفاً فایل با پسوند .tar.gz یا .zip آپلود کنید."
        flash(err, "error")
        if is_ajax:
            return jsonify({"success": False, "error": err}), 400
        return redirect(url_for("admin.kb_packages_dashboard", course_id=course_id))

    with tempfile.NamedTemporaryFile(suffix="_" + filename, delete=False) as tmp:
        uploaded.save(tmp.name)
        tmp_path = Path(tmp.name)

    try:
        result = kb_admin.install_kb_package(
            tmp_path,
            target_week=target_week,
            admin_id=current_user.id,
            course_id=course_id,
        )
        if result.get("success"):
            if result.get("is_master"):
                if result.get("already_installed"):
                    msg = result.get("message", "این بسته قبلاً نصب شده است.")
                    flash(msg, "info")
                else:
                    msg = result.get(
                        "message",
                        f"بسته نهایی نسخه {result.get('version', '')} با موفقیت تایید و ادغام شد!",
                    )
                    flash(msg, "success")
            else:
                w_disp = "۷.۵" if result.get("week") == 71 else ("۹.۵" if result.get("week") == 99 else str(result.get("week", "")))
                msg = (
                    f"بسته هفته {w_disp} با موفقیت نصب و ادغام شد! "
                    f"({result.get('notes_count', 0)} یادداشت درس، {result.get('flashcards_count', 0)} فلش‌کارت، "
                    f"{result.get('quiz_count', 0)} سوال آزمون، {result.get('glossary_count', 0)} اصطلاح واژه‌نامه)"
                )
                flash(msg, "success")

            if is_ajax:
                return jsonify({
                    "success": True,
                    "message": msg,
                    "redirect_url": url_for("admin.kb_packages_dashboard", course_id=course_id),
                })
        else:
            err = result.get("error", "خطای ناشناخته در نصب بسته")
            flash(err, "error")
            if result.get("error_list"):
                for e in result["error_list"][:5]:
                    flash(f"جزئیات خطا: {e}", "error")
            if is_ajax:
                return jsonify({
                    "success": False,
                    "error": err,
                    "error_list": result.get("error_list", []),
                }), 400
    finally:
        try:
            if tmp_path.exists():
                tmp_path.unlink()
        except Exception:
            pass

    return redirect(url_for("admin.kb_packages_dashboard", course_id=course_id))




@bp.route("/kb-packages/rebuild-downloads", methods=["POST"])
@admin_required
def kb_packages_rebuild_downloads():
    """تولید مجدد کلیه خروجی‌های دانلودی پویا (HTML / PDF / ZIP)."""
    course_id = request.form.get("course_id", type=int)
    try:
        res = downloads_service.build_all_downloads(force=True)
        event_service.log_event(
            user_id=current_user.id,
            event_type="admin_rebuild_downloads",
            data={
                "weeks_count": len(res.get("weeks", {})),
                "pdf_engine": res.get("pdf_engine"),
                "status": res.get("status"),
            },
        )
        if res.get("status") == "success":
            flash("کلیه فایل‌های دانلودی پویا با موفقیت تولید و جای‌گذاری شدند.", "success")
        elif res.get("status") == "partial":
            flash("تولید فایل‌های دانلودی با موفقیت نسبی انجام شد؛ لطفاً گزارش هفتگی را بررسی کنید.", "warning")
        else:
            flash(f"خطا در تولید فایل‌های دانلودی: {res.get('error', 'خطای نامشخص')}", "error")
    except Exception as e:
        flash(f"خطای سیستمی در بازتولید دانلودها: {e}", "error")

    return redirect(url_for("admin.kb_packages_dashboard", course_id=course_id))


# ──────────────────────────────────────────────────────────────────────────────
# مدیریت دوره‌ها و نوبت‌های برگزاری (Cohorts & Multi-Course Management)
# ──────────────────────────────────────────────────────────────────────────────
@bp.route("/cohorts")
@admin_required
def cohorts_list():
    """لیست تمام نوبت‌های برگزاری با قابلیت فیلتر وضعیت."""
    status_filter = request.args.get("status", "all")
    cohorts = cohort_service.list_all_cohorts(status_filter=status_filter)
    courses = cohort_service.list_all_courses()
    return render_template(
        "admin/cohorts/index.html",
        cohorts=cohorts,
        courses=courses,
        current_filter=status_filter,
    )


@bp.route("/cohorts/create", methods=["GET", "POST"])
@admin_required
def cohorts_create():
    """ایجاد نوبت برگزاری جدید."""
    courses = cohort_service.list_all_courses()
    if request.method == "POST":
        course_id = int(request.form.get("course_id", 1))
        name = request.form.get("name", "").strip()
        code = request.form.get("code", "").strip()
        year = int(request.form.get("year", 1405))
        season = request.form.get("season", "").strip()
        status = request.form.get("status", "active")
        capacity_raw = request.form.get("capacity")
        capacity = int(capacity_raw) if capacity_raw and capacity_raw.strip().isdigit() else None
        description = request.form.get("description", "").strip()

        if not name or not code:
            flash("نام و کد یکتای دوره الزامی هستند.", "error")
            return render_template("admin/cohorts/form.html", courses=courses, cohort=None)

        try:
            cohort = cohort_service.create_cohort(
                course_id=course_id,
                name=name,
                code=code,
                year=year,
                season=season,
                status=status,
                capacity=capacity,
                description=description,
            )
            flash(f"دوره '{cohort.name}' با موفقیت ایجاد شد.", "success")
            return redirect(url_for("admin.cohorts_detail", cohort_id=cohort.id))
        except ValueError as e:
            flash(str(e), "error")
            return render_template("admin/cohorts/form.html", courses=courses, cohort=None)

    return render_template("admin/cohorts/form.html", courses=courses, cohort=None)


@bp.route("/cohorts/<int:cohort_id>/edit", methods=["GET", "POST"])
@admin_required
def cohorts_edit(cohort_id: int):
    """ویرایش اطلاعات نوبت برگزاری."""
    cohort_data = cohort_service.get_cohort_detail(cohort_id)
    if not cohort_data:
        abort(404)
    cohort = cohort_data["cohort"]
    courses = cohort_service.list_all_courses()

    if request.method == "POST":
        name = request.form.get("name")
        year = int(request.form.get("year", cohort.year))
        season = request.form.get("season")
        status = request.form.get("status")
        capacity_raw = request.form.get("capacity")
        capacity = int(capacity_raw) if capacity_raw and capacity_raw.strip().isdigit() else None
        description = request.form.get("description")

        cohort_service.update_cohort(
            cohort_id=cohort.id,
            name=name,
            year=year,
            season=season,
            status=status,
            capacity=capacity,
            description=description,
        )
        flash("مشخصات دوره با موفقیت به‌روزرسانی شد.", "success")
        return redirect(url_for("admin.cohorts_detail", cohort_id=cohort.id))

    return render_template("admin/cohorts/form.html", courses=courses, cohort=cohort)


@bp.route("/cohorts/<int:cohort_id>")
@admin_required
def cohorts_detail(cohort_id: int):
    """صفحه جزئیات نوبت برگزاری، آمار و فهرست دانش‌آموزان عضو."""
    data = cohort_service.get_cohort_detail(cohort_id)
    if not data:
        abort(404)
    enrolled_user_ids = {s["user_id"] for s in data["students"]}
    all_students = User.query.filter_by(is_admin=False).all()
    available_students = [s for s in all_students if s.id not in enrolled_user_ids]

    return render_template(
        "admin/cohorts/detail.html",
        cohort=data["cohort"],
        course=data["course"],
        students=data["students"],
        stats=data["stats"],
        available_students=available_students,
    )


@bp.route("/cohorts/<int:cohort_id>/enroll", methods=["POST"])
@admin_required
def cohorts_enroll_student(cohort_id: int):
    """ثبت‌نام تکی یا گروهی دانش‌آموزان در دوره."""
    mode = request.form.get("enroll_mode", "single")
    if mode == "bulk":
        bulk_text = request.form.get("student_identifiers", "")
        lines = [line.strip() for line in bulk_text.replace(",", "\n").splitlines() if line.strip()]
        res = cohort_service.bulk_enroll_students(cohort_id, lines)
        msg = f"ثبت‌نام گروهی انجام شد: {res['enrolled']} دانش‌آموز افزوده شدند."
        if res["already_enrolled"]:
            msg += f" ({res['already_enrolled']} نفر از قبل عضو بودند)"
        if res["not_found"]:
            msg += f" — موارد یافت‌نشده: {', '.join(res['not_found'])}"
        flash(msg, "info")
    else:
        user_id_raw = request.form.get("user_id")
        if not user_id_raw or not user_id_raw.isdigit():
            flash("لطفاً یک دانش‌آموز معتبر انتخاب کنید.", "error")
        else:
            success, msg = cohort_service.enroll_student_in_cohort(int(user_id_raw), cohort_id)
            flash(msg, "success" if success else "warning")

    return redirect(url_for("admin.cohorts_detail", cohort_id=cohort_id))


@bp.route("/cohorts/<int:cohort_id>/enrollments/<int:enrollment_id>/status", methods=["POST"])
@admin_required
def cohorts_update_enrollment_status(cohort_id: int, enrollment_id: int):
    """تغییر وضعیت عضویت دانش‌آموز (active / dropped / completed)."""
    new_status = request.form.get("status", "active")
    success = cohort_service.update_enrollment_status(enrollment_id, new_status)
    if success:
        flash("وضعیت عضویت با موفقیت به‌روزرسانی شد.", "success")
    else:
        flash("عضویت مورد نظر یافت نشد.", "error")
    return redirect(url_for("admin.cohorts_detail", cohort_id=cohort_id))


@bp.route("/cohorts/<int:cohort_id>/enrollments/<int:enrollment_id>/remove", methods=["POST"])
@admin_required
def cohorts_remove_enrollment(cohort_id: int, enrollment_id: int):
    """حذف عضویت دانش‌آموز از دوره بدون حذف حساب کاربری."""
    success = cohort_service.remove_enrollment(enrollment_id)
    if success:
        flash("عضویت دانش‌آموز از این دوره حذف شد (حساب کاربری محفوظ ماند).", "success")
    else:
        flash("عضویت مورد نظر یافت نشد.", "error")
    return redirect(url_for("admin.cohorts_detail", cohort_id=cohort_id))


@bp.route("/cohorts/<int:cohort_id>/archive", methods=["POST"])
@admin_required
def cohorts_archive(cohort_id: int):
    """بایگانی‌کردن نوبت برگزاری بدون حذف هیچ‌گونه اطلاعات یا سابقه."""
    cohort_service.archive_cohort(cohort_id)
    flash("نوبت برگزاری با حفظ کلیه سوابق بایگانی شد.", "info")
    return redirect(url_for("admin.cohorts_list"))
