"""سرویس مدیریت چنددوره‌ای، نوبت‌های برگزاری (Cohorts) و عضویت دانش‌آموزان (Enrollments).

این ماژول ساختار آموزشی سامانه را از تک‌دوره‌ای به چنددوره‌ای ارتقا می‌دهد:
- مدیریت دوره‌های آموزشی کلان (Course مانند CS50x)
- مدیریت نوبت‌های فصلی و سالانه (Cohort مانند پاییز ۱۴۰۴ یا زمستان ۱۴۰۵)
- مدیریت وضعیت و سوابق عضویت هر دانش‌آموز (Enrollment)
- مهاجرت امن داده‌های جاری بدون ریزش اطلاعات
"""
from __future__ import annotations

from datetime import datetime, date
from typing import Any
from flask import abort

from app import db
from app.models import Course, Cohort, Enrollment, User, WeekProgress, Week


DEFAULT_COURSE_CODE = "cs50x"
DEFAULT_COHORT_CODE = "cs50x-winter-1405"


def ensure_default_course_and_cohort() -> tuple[Course, Cohort]:
    """تضمین وجود دوره کلان و نوبت برگزاری پایه و انتساب دانش‌آموزان موجود.

    این تابع تضمین می‌کند که داده‌های موجود هرگز بی‌پدر یا یتیم نشوند.
    تمام دانش‌آموزان قبلی به‌صورت خودکار در دوره فعال پایه عضو می‌شوند.
    """
    course = Course.query.filter_by(code=DEFAULT_COURSE_CODE).first()
    if not course:
        course = Course(
            code=DEFAULT_COURSE_CODE,
            title="مبانی علوم کامپیوتر CS50x انزلی",
            description="دوره جامع و رسمی مبانی علوم کامپیوتر و برنامه‌نویسی CS50x دانشگاه هاروارد در بندر انزلی.",
            is_active=True,
            created_at=datetime.utcnow(),
        )
        db.session.add(course)
        db.session.commit()

    cohort = Cohort.query.filter_by(code=DEFAULT_COHORT_CODE).first()
    if not cohort:
        cohort = Cohort(
            course_id=course.id,
            name="CS50x — دوره زمستان ۱۴۰۵",
            code=DEFAULT_COHORT_CODE,
            year=1405,
            season="زمستان",
            status="active",
            capacity=100,
            description="نوبت برگزاری حضوری و آنلاین زمستان ۱۴۰۵ در انزلی به همراه منتورینگ و پروژه‌محور.",
            created_at=datetime.utcnow(),
        )
        db.session.add(cohort)
        db.session.commit()

    # انتساب دانش‌آموزان موجود به نوبت برگزاری پایه در صورت عدم عضویت
    students = User.query.filter_by(is_admin=False).all()
    for s in students:
        existing = Enrollment.query.filter_by(user_id=s.id, cohort_id=cohort.id).first()
        if not existing:
            # بررسی اینکه آیا در دوره دیگری primary است یا نه
            has_primary = Enrollment.query.filter_by(user_id=s.id, is_primary=True).first() is not None
            enrollment = Enrollment(
                user_id=s.id,
                cohort_id=cohort.id,
                status="active",
                role="student",
                is_primary=not has_primary,
                enrolled_at=datetime.utcnow(),
            )
            db.session.add(enrollment)

    db.session.commit()
    return course, cohort


def get_active_cohort_for_user(user_id: int, requested_cohort_id: int | None = None) -> Cohort | None:
    """تشخیص نوبت برگزاری فعال کاربر بر اساس درخواست صریح یا اولویت عضویت."""
    if requested_cohort_id:
        enr = Enrollment.query.filter_by(
            user_id=user_id, cohort_id=requested_cohort_id
        ).first()
        if enr and enr.status in ("active", "completed"):
            return enr.cohort

    # بررسی عضویت primary فعال
    primary_enr = (
        Enrollment.query.filter_by(user_id=user_id, is_primary=True, status="active")
        .first()
    )
    if primary_enr:
        return primary_enr.cohort

    # هر عضویت فعال دیگر
    any_enr = (
        Enrollment.query.filter_by(user_id=user_id, status="active")
        .order_by(Enrollment.enrolled_at.desc())
        .first()
    )
    if any_enr:
        return any_enr.cohort

    # اگر کاربر عضو فعال ندارد ولی عضو دوره‌های تکمیل‌شده است
    completed_enr = (
        Enrollment.query.filter_by(user_id=user_id)
        .order_by(Enrollment.enrolled_at.desc())
        .first()
    )
    if completed_enr:
        return completed_enr.cohort

    # اگر کاربر ادمین است، نوبت فعال سیستم را برمی‌گردانیم
    user = db.session.get(User, user_id)
    if user and user.is_admin:
        active_c = Cohort.query.filter_by(status="active").first()
        if active_c:
            return active_c

    return None


def get_user_enrollments(user_id: int) -> list[dict[str, Any]]:
    """فهرست تمام دوره‌هایی که دانش‌آموز در آنها عضو است با درصد پیشرفت."""
    enrollments = (
        Enrollment.query.filter_by(user_id=user_id)
        .order_by(Enrollment.is_primary.desc(), Enrollment.enrolled_at.desc())
        .all()
    )

    total_weeks = Week.query.count() or 13
    completed_weeks = WeekProgress.query.filter_by(user_id=user_id, kb_read=True).count()
    overall_progress_pct = int((completed_weeks / total_weeks) * 100) if total_weeks > 0 else 0

    result = []
    for enr in enrollments:
        c = enr.cohort
        result.append({
            "enrollment_id": enr.id,
            "cohort_id": c.id,
            "cohort_name": c.name,
            "cohort_code": c.code,
            "course_title": c.course.title if c.course else "CS50x",
            "year": c.year,
            "season": c.season or "عمومی",
            "status": enr.status,  # active, completed, dropped, pending
            "cohort_status": c.status,  # active, completed, archived, enrollment, draft
            "is_primary": enr.is_primary,
            "role": enr.role,
            "enrolled_at": enr.enrolled_at,
            "completed_at": enr.completed_at,
            "start_date": c.start_date,
            "end_date": c.end_date,
            "progress_percent": overall_progress_pct,
            "completed_weeks": completed_weeks,
            "total_weeks": total_weeks,
        })
    return result


def switch_user_active_cohort(user_id: int, cohort_id: int) -> bool:
    """تغییر دوره فعال دانش‌آموز و علامت‌زدن آن به عنوان is_primary."""
    target_enr = Enrollment.query.filter_by(user_id=user_id, cohort_id=cohort_id).first()
    if not target_enr:
        return False

    # تغییر تمام عضویت‌های کاربر به is_primary=False
    Enrollment.query.filter_by(user_id=user_id).update({"is_primary": False})
    target_enr.is_primary = True
    db.session.commit()
    return True


# ──────────────────────────────────────────────────────────────────────────────
# توابع مدیریتی پنل ادمین
# ──────────────────────────────────────────────────────────────────────────────

def list_all_courses() -> list[Course]:
    """فهرست تمام برنامه‌های آموزشی کلان."""
    return Course.query.order_by(Course.created_at.desc()).all()


def list_all_cohorts(status_filter: str | None = None) -> list[dict[str, Any]]:
    """فهرست تمام نوبت‌های برگزاری با شمارش دانش‌آموزان و آمار تحلیلی."""
    query = Cohort.query
    if status_filter and status_filter != "all":
        query = query.filter_by(status=status_filter)

    cohorts = query.order_by(Cohort.year.desc(), Cohort.created_at.desc()).all()
    results = []

    for c in cohorts:
        total_enrolled = Enrollment.query.filter_by(cohort_id=c.id).count()
        active_students = Enrollment.query.filter_by(cohort_id=c.id, status="active").count()
        completed_students = Enrollment.query.filter_by(cohort_id=c.id, status="completed").count()

        results.append({
            "id": c.id,
            "name": c.name,
            "code": c.code,
            "course_title": c.course.title if c.course else "CS50x",
            "course_id": c.course_id,
            "year": c.year,
            "season": c.season or "نامشخص",
            "status": c.status,
            "capacity": c.capacity,
            "start_date": c.start_date,
            "end_date": c.end_date,
            "description": c.description,
            "total_enrolled": total_enrolled,
            "active_students": active_students,
            "completed_students": completed_students,
            "created_at": c.created_at,
        })
    return results


def get_cohort_detail(cohort_id: int) -> dict[str, Any] | None:
    """دریافت اطلاعات تفصیلی یک نوبت برگزاری به همراه فهرست دانش‌آموزان عضو."""
    cohort = db.session.get(Cohort, cohort_id)
    if not cohort:
        return None

    enrollments = (
        Enrollment.query.filter_by(cohort_id=cohort.id)
        .join(User, Enrollment.user_id == User.id)
        .order_by(Enrollment.enrolled_at.desc())
        .all()
    )

    students_list = []
    for enr in enrollments:
        u = enr.user
        students_list.append({
            "enrollment_id": enr.id,
            "user_id": u.id,
            "username": u.username,
            "status": enr.status,
            "role": enr.role,
            "is_primary": enr.is_primary,
            "enrolled_at": enr.enrolled_at,
            "completed_at": enr.completed_at,
            "xp": u.xp or 0,
            "streak": u.streak or 0,
            "is_active_account": u.is_active,
        })

    total_count = len(students_list)
    active_count = sum(1 for s in students_list if s["status"] == "active")
    dropped_count = sum(1 for s in students_list if s["status"] == "dropped")
    completed_count = sum(1 for s in students_list if s["status"] == "completed")

    return {
        "cohort": cohort,
        "course": cohort.course,
        "students": students_list,
        "stats": {
            "total": total_count,
            "active": active_count,
            "dropped": dropped_count,
            "completed": completed_count,
            "capacity": cohort.capacity,
            "available_seats": max(0, (cohort.capacity or 0) - total_count) if cohort.capacity else None,
        }
    }


def create_cohort(
    course_id: int,
    name: str,
    code: str,
    year: int,
    season: str | None = None,
    status: str = "active",
    capacity: int | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    description: str | None = None,
) -> Cohort:
    """ایجاد نوبت برگزاری جدید در سامانه."""
    clean_code = code.strip().lower()
    existing = Cohort.query.filter_by(code=clean_code).first()
    if existing:
        raise ValueError(f"کد دوره '{clean_code}' قبلاً ثبت شده است. لطفاً یک کد یکتا انتخاب کنید.")

    cohort = Cohort(
        course_id=course_id,
        name=name.strip(),
        code=clean_code,
        year=year,
        season=season.strip() if season else None,
        status=status,
        capacity=capacity,
        start_date=start_date,
        end_date=end_date,
        description=description.strip() if description else None,
        created_at=datetime.utcnow(),
    )
    db.session.add(cohort)
    db.session.commit()
    return cohort


def update_cohort(
    cohort_id: int,
    name: str | None = None,
    year: int | None = None,
    season: str | None = None,
    status: str | None = None,
    capacity: int | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    description: str | None = None,
) -> Cohort:
    """ویرایش مشخصات یک نوبت برگزاری."""
    cohort = db.session.get(Cohort, cohort_id)
    if not cohort:
        abort(404)

    if name:
        cohort.name = name.strip()
    if year:
        cohort.year = year
    if season is not None:
        cohort.season = season.strip() if season else None
    if status:
        cohort.status = status
    if capacity is not None:
        cohort.capacity = capacity
    if start_date is not None:
        cohort.start_date = start_date
    if end_date is not None:
        cohort.end_date = end_date
    if description is not None:
        cohort.description = description.strip() if description else None

    db.session.commit()
    return cohort


def archive_cohort(cohort_id: int) -> Cohort:
    """بایگانی‌کردن یک نوبت برگزاری بدون حذف هیچ‌یک از سوابق آموزشی."""
    cohort = db.session.get(Cohort, cohort_id)
    if not cohort:
        abort(404)
    cohort.status = "archived"
    db.session.commit()
    return cohort


def enroll_student_in_cohort(
    user_id: int,
    cohort_id: int,
    role: str = "student",
    is_primary: bool = False,
    notes: str | None = None,
) -> tuple[bool, str]:
    """ثبت‌نام یک دانش‌آموز در نوبت برگزاری با مدیریت ضدتکرار."""
    user = db.session.get(User, user_id)
    if not user:
        return False, "کاربر یافت نشد."

    cohort = db.session.get(Cohort, cohort_id)
    if not cohort:
        return False, "نوبت برگزاری یافت نشد."

    # اگر قبلاً عضویتی وجود داشته است
    existing = Enrollment.query.filter_by(user_id=user_id, cohort_id=cohort_id).first()
    if existing:
        if existing.status == "active":
            return False, "این دانش‌آموز از قبل عضو فعال این دوره است."
        else:
            existing.status = "active"
            existing.enrolled_at = datetime.utcnow()
            if is_primary:
                Enrollment.query.filter_by(user_id=user_id).update({"is_primary": False})
                existing.is_primary = True
            db.session.commit()
            return True, "عضویت دانش‌آموز با موفقیت فعال شد."

    # بررسی سقف ظرفیت در صورت تعیین
    if cohort.capacity:
        current_count = Enrollment.query.filter_by(cohort_id=cohort_id, status="active").count()
        if current_count >= cohort.capacity:
            return False, f"ظرفیت این دوره ({cohort.capacity} نفر) تکمیل شده است."

    has_primary = Enrollment.query.filter_by(user_id=user_id, is_primary=True).first() is not None
    should_be_primary = is_primary or (not has_primary)

    if should_be_primary:
        Enrollment.query.filter_by(user_id=user_id).update({"is_primary": False})

    enrollment = Enrollment(
        user_id=user_id,
        cohort_id=cohort_id,
        status="active",
        role=role,
        is_primary=should_be_primary,
        notes=notes,
        enrolled_at=datetime.utcnow(),
    )
    db.session.add(enrollment)
    db.session.commit()
    return True, f"دانش‌آموز {user.username} با موفقیت به دوره افزوده شد."


def bulk_enroll_students(cohort_id: int, identifier_list: list[str]) -> dict[str, Any]:
    """ثبت‌نام دسته‌جمعی دانش‌آموزان از روی نام کاربری یا شناسه."""
    cohort = db.session.get(Cohort, cohort_id)
    if not cohort:
        abort(404)

    enrolled = 0
    already_enrolled = 0
    not_found = []
    errors = []

    for raw in identifier_list:
        ident = raw.strip()
        if not ident:
            continue

        user = None
        if ident.isdigit():
            user = db.session.get(User, int(ident))
        if not user:
            user = User.query.filter_by(username=ident).first()

        if not user:
            not_found.append(ident)
            continue

        existing = Enrollment.query.filter_by(user_id=user.id, cohort_id=cohort_id, status="active").first()
        if existing:
            already_enrolled += 1
            continue

        success, msg = enroll_student_in_cohort(user.id, cohort_id)
        if success:
            enrolled += 1
        else:
            errors.append(f"{ident}: {msg}")

    return {
        "enrolled": enrolled,
        "already_enrolled": already_enrolled,
        "not_found": not_found,
        "errors": errors,
    }


def update_enrollment_status(enrollment_id: int, new_status: str) -> bool:
    """به‌روزرسانی وضعیت عضویت (active, dropped, completed)."""
    enr = db.session.get(Enrollment, enrollment_id)
    if not enr:
        return False

    enr.status = new_status
    if new_status == "completed":
        enr.completed_at = datetime.utcnow()
    db.session.commit()
    return True


def remove_enrollment(enrollment_id: int) -> bool:
    """لغو یا حذف عضویت یک دانش‌آموز در یک دوره (بدون حذف اکانت یا سایر دوره‌ها)."""
    enr = db.session.get(Enrollment, enrollment_id)
    if not enr:
        return False

    user_id = enr.user_id
    was_primary = enr.is_primary

    db.session.delete(enr)
    db.session.commit()

    # اگر این عضویت primary بود، یک عضویت فعال دیگر را primary می‌کنیم
    if was_primary:
        remaining = Enrollment.query.filter_by(user_id=user_id, status="active").first()
        if remaining:
            remaining.is_primary = True
            db.session.commit()

    return True
