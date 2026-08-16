"""منطق داشبورد و پیشرفت — توابع خالص و قابل تست.

این ماژول داده‌های نمایشی داشبورد را آماده میکند: آمار کاربر، پیشرفت مدرک،
تکالیف نزدیک، و رتبه‌ی کلاس. هیچ رندر یا روت در اینجا نیست — فقط منطق داده.
"""
from datetime import datetime

from flask import abort

from app import db
from app.models import User, WeekProgress, Assignment, Submission, XPLog, Week

# تعداد پیش‌فرض کل هفته‌های دوره (در صورت خالی بودن DB)
TOTAL_WEEKS = 10


def get_user_stats(user_id: int) -> dict:
    """آمار کلی کاربر برای کارت‌های داشبورد را برمیگرداند.

    Returns:
        dict با کلیدهای: xp, streak, active_assignments, submissions_count, username.
    """
    user = db.session.get(User, user_id)
    if user is None:
        abort(404)

    active_assignments = (
        Assignment.query.filter_by(is_active=True)
        .filter(Assignment.due_date >= datetime.utcnow())
        .count()
    )
    submissions_count = (
        Submission.query.filter_by(student_id=user_id).count()
    )

    return {
        "username": user.username,
        "xp": user.xp or 0,
        "streak": user.streak or 0,
        "is_admin": user.is_admin,
        "active_assignments": active_assignments,
        "submissions_count": submissions_count,
    }


def get_certificate_progress(user_id: int) -> dict:
    """پیشرفت کاربر به سمت مدرک CS50 را محاسبه میکند.

    یک هفته «تکمیل‌شده» محسوب میشود وقتی quiz_completed=True باشد.
    درصد = (هفته‌های تکمیل‌شده / total_weeks) × ۱۰۰.

    Returns:
        dict: completed_weeks (int), total_weeks, percent, current_week.
    """
    total_weeks = Week.query.count() or TOTAL_WEEKS
    completed = WeekProgress.query.filter_by(
        user_id=user_id, kb_read=True
    ).count()

    percent = int((completed / total_weeks) * 100) if total_weeks else 0

    # هفته‌ی فعلی = اولین هفته‌ای که هنوز kb_read نیست
    last_completed = (
        WeekProgress.query.filter_by(user_id=user_id, kb_read=True)
        .order_by(WeekProgress.week.desc())
        .first()
    )
    current_week = (last_completed.week + 1) if last_completed else 0
    # محدود به بازه‌ی دوره
    if current_week > total_weeks - 1:
        current_week = total_weeks - 1

    return {
        "completed_weeks": completed,
        "total_weeks": total_weeks,
        "percent": percent,
        "current_week": current_week,
    }


def get_upcoming_assignments(user_id: int, limit: int = 3) -> list[dict]:
    """تکالیف فعال و نزدیک‌به‌مهلت را برمیگرداند.

    برای هر تکلیف، وضعیت تحویل کاربر فعلی را هم بررسی میکند.

    Returns:
        لیستی از dict: id, title, week, due_date, submitted (bool), grade (int|None).
    """
    assignments = (
        Assignment.query.filter_by(is_active=True)
        .order_by(Assignment.due_date.asc())
        .limit(limit)
        .all()
    )

    result = []
    for a in assignments:
        sub = (
            Submission.query.filter_by(student_id=user_id, assignment_id=a.id)
            .order_by(Submission.submitted_at.desc())
            .first()
        )
        result.append(
            {
                "id": a.id,
                "title": a.title,
                "week": a.week,
                "due_date": a.due_date,
                "submitted": sub is not None,
                "grade": sub.grade if sub else None,
            }
        )
    return result


def get_class_rank(user_id: int) -> dict:
    """رتبه‌ی کاربر در کلاس را محاسبه میکند.

    Returns:
        dict: rank (int، ۱‌پایه)، total_students, xp.
    """
    user = db.session.get(User, user_id)
    if user is None:
        abort(404)

    # تعداد دانش‌آموزانی که XP بیشتر از این کاربر دارند (ادمین‌ها فیلتر می‌شوند)
    higher = User.query.filter(User.is_admin.is_(False), User.xp > (user.xp or 0)).count()
    rank = higher + 1
    total = User.query.filter(User.is_admin.is_(False)).count() or 1

    return {"rank": rank, "total_students": total, "xp": user.xp or 0}


def get_xp_history(user_id: int, limit: int = 20) -> list[XPLog]:
    """آخرین n رکورد XPLog را برای نمایش سابقه‌ی XP برمیگرداند."""
    return (
        XPLog.query.filter_by(user_id=user_id)
        .order_by(XPLog.timestamp.desc())
        .limit(limit)
        .all()
    )


def get_or_create_week_progress(user_id: int, week: int) -> WeekProgress:
    """WeekProgress را پیدا میکند یا ایجاد می‌کند (get-or-create pattern).

    از UniqueConstraint(user_id, week) استفاده میکند.
    """
    wp = WeekProgress.query.filter_by(user_id=user_id, week=week).first()
    if wp is None:
        wp = WeekProgress(user_id=user_id, week=week)
        db.session.add(wp)
        db.session.flush()
    return wp


def mark_kb_read(user_id: int, week: int) -> bool:
    """خواندن KB هفته را ثبت می‌کند و True برمیگرداند اگر اولین بار باشد.

    اگر قبلاً kb_read=True بود، False برمیگرداند (برای جلوگیری از XP تکراری).
    """
    wp = get_or_create_week_progress(user_id, week)
    if wp.kb_read:
        return False  # قبلاً خوانده شده
    wp.kb_read = True
    wp.last_activity = datetime.utcnow()
    db.session.commit()
    return True


def mark_quiz_completed(user_id: int, week: int, score: int, total: int) -> None:
    """نتیجه‌ی کوییز را ثبت و quiz_completed=True می‌کند (برای فاز ۲)."""
    wp = get_or_create_week_progress(user_id, week)
    wp.quiz_score = score
    wp.quiz_total = total
    if score >= wp.quiz_total * 0.6:  # حداقل ۶۰٪ برای تکمیل
        wp.quiz_completed = True
    wp.last_activity = datetime.utcnow()
    db.session.commit()
