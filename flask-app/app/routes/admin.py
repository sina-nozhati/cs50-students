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
)
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app import db
from app.models import Resource, Submission, Assignment
from app.services import resources as res_service
from app.services import weeks as weeks_service
from app.services import users as users_service
from app.services import assignments_admin as assignments_service
from app.services import analytics as analytics_service
from app.services import submissions as sub_service
from app.services import progress as progress_service

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
    """داشبورد تحلیلی — آمار کلی، هشدارها، وضعیت هفته‌ها."""
    overview = analytics_service.get_overview()
    assignment_stats = analytics_service.get_assignment_stats()
    weekly_progress = analytics_service.get_weekly_progress_overview()
    low_engagement = analytics_service.get_low_engagement_students(days=3)
    top_performers = analytics_service.get_top_performers(limit=5)

    # تعداد تحویل‌های بدون نمره
    ungraded_count = Submission.query.filter(Submission.grade.is_(None)).count()

    return render_template(
        "admin/index.html",
        overview=overview,
        assignment_stats=assignment_stats,
        weekly_progress=weekly_progress,
        low_engagement=low_engagement,
        top_performers=top_performers,
        ungraded_count=ungraded_count,
    )


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
    """ثبت دانش‌آموز جدید."""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            flash("نام کاربری و رمز عبور الزامی است.", "error")
            return redirect(request.url)

        if len(password) < 4:
            flash("رمز عبور باید حداقل ۴ کاراکتر باشد.", "error")
            return redirect(request.url)

        try:
            users_service.create_user(username, password)
            flash(f"دانش‌آموز «{username}» با موفقیت ثبت شد.", "success")
            return redirect(url_for("admin.users_list"))
        except ValueError:
            flash("این نام کاربری قبلاً استفاده شده.", "error")
            return redirect(request.url)

    return render_template("admin/user_form.html", user=None, edit_mode=False)


@bp.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
@admin_required
def users_edit(user_id: int):
    """ویرایش اطلاعات دانش‌آموز."""
    from app.models import User
    user = db.session.get(User, user_id)
    if not user:
        flash("کاربر یافت نشد.", "error")
        return redirect(url_for("admin.users_list"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip() or None
        xp_adj = request.form.get("xp_adjustment", 0, type=int)

        try:
            users_service.update_user(user_id, username=username, password=password, xp_adjustment=xp_adj)
            flash(f"اطلاعات کاربر به‌روزرسانی شد.", "success")
            return redirect(url_for("admin.users_list"))
        except ValueError as e:
            flash("این نام کاربری قبلاً توسط شخص دیگری ثبت شده است.", "error")
            return redirect(url_for("admin.users_edit", user_id=user_id))

    return render_template("admin/user_form.html", user=user, edit_mode=True)


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
    return render_template(
        "admin/user_detail.html",
        user=detail["user"],
        submissions=detail["submissions"],
        week_progress=detail["week_progress"],
        xp_logs=detail["xp_logs"],
        rank=rank,
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
