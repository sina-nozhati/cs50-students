"""مدیریت کاربران (دانش‌آموزان) در پنل ادمین."""
from datetime import datetime
from flask import abort
from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Submission, WeekProgress, XPLog
from app.services import xp as xp_service

def list_all_students() -> list[dict]:
    """تمام دانش‌آموزان (غیر ادمین) را با آمار برمی‌گرداند."""
    students = User.query.filter_by(is_admin=False).all()
    result = []
    for s in students:
        last_log = XPLog.query.filter_by(user_id=s.id).order_by(XPLog.timestamp.desc()).first()
        result.append({
            "id": s.id,
            "username": s.username,
            "xp": s.xp or 0,
            "streak": s.streak or 0,
            "is_active": getattr(s, "is_active", True),
            "submissions_count": Submission.query.filter_by(student_id=s.id).count(),
            "last_activity": last_log.timestamp if last_log else None
        })
    return result

def create_user(
    username: str,
    password: str,
    telegram_id: str | None = None,
    is_admin: bool = False,
    is_active: bool = True,
    initial_xp: int = 0,
    initial_streak: int = 0,
    cohort_id: int | None = None,
    cohort_role: str = "student",
    cohort_status: str = "active",
) -> User:
    """کاربر جدید ایجاد می‌کند با پشتیبانی از تلگرام، نقش، وضعیت و عضویت در دوره."""
    existing = User.query.filter_by(username=username).first()
    if existing:
        raise ValueError("Username already exists")

    clean_tg = None
    if telegram_id:
        clean_tg = telegram_id.strip().lstrip("@")
        if clean_tg:
            existing_tg = User.query.filter_by(telegram_id=clean_tg).first()
            if existing_tg:
                raise ValueError("Telegram ID already exists")
        else:
            clean_tg = None

    user = User(
        username=username,
        password_hash=generate_password_hash(password),
        telegram_id=clean_tg,
        is_admin=is_admin,
        is_active=is_active,
        xp=max(0, initial_xp),
        streak=max(0, initial_streak),
    )
    db.session.add(user)
    db.session.commit()

    if initial_xp > 0:
        stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        log = XPLog(
            user_id=user.id,
            amount=initial_xp,
            reason=f"admin:initial:+:{stamp}",
        )
        db.session.add(log)
        db.session.commit()

    if cohort_id:
        from app.services import cohorts as cohort_service
        try:
            cohort_service.enroll_student_in_cohort(
                user_id=user.id,
                cohort_id=cohort_id,
                role=cohort_role or "student",
                is_primary=True,
            )
        except Exception:
            pass

    return user

def update_user(
    user_id: int,
    username: str | None = None,
    password: str | None = None,
    telegram_id: str | None = None,
    is_admin: bool | None = None,
    is_active: bool | None = None,
    xp_adjustment: int = 0,
    cohort_id: int | None = None,
) -> User:
    """رمز عبور، نام کاربری، تلگرام، نقش یا XP کاربر را آپدیت می‌کند."""
    user = db.session.get(User, user_id)
    if not user:
        abort(404)
        
    if username and username != user.username:
        existing = User.query.filter_by(username=username).first()
        if existing:
            raise ValueError("Username already exists")
        user.username = username

    if telegram_id is not None:
        clean_tg = telegram_id.strip().lstrip("@") if telegram_id else None
        if clean_tg and clean_tg != user.telegram_id:
            existing_tg = User.query.filter_by(telegram_id=clean_tg).first()
            if existing_tg:
                raise ValueError("Telegram ID already exists")
            user.telegram_id = clean_tg
        elif not clean_tg:
            user.telegram_id = None

    if is_admin is not None:
        user.is_admin = is_admin

    if is_active is not None:
        user.is_active = is_active
        
    if password:
        user.password_hash = generate_password_hash(password)
        
    if xp_adjustment != 0:
        # reason یکتا تا award ایدمپوتنت مانع تنظیمات متوالی ادمین نشود
        stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        if xp_adjustment > 0:
            xp_service.award(user.id, xp_adjustment, f"admin:adjust:+:{stamp}")
        else:
            user.xp = max(0, (user.xp or 0) + xp_adjustment)
            log = XPLog(
                user_id=user.id,
                amount=xp_adjustment,
                reason=f"admin:adjust:-:{stamp}",
            )
            db.session.add(log)

    if cohort_id:
        from app.models import Enrollment
        from app.services import cohorts as cohort_service
        existing_enr = Enrollment.query.filter_by(user_id=user.id, cohort_id=cohort_id).first()
        if not existing_enr:
            try:
                cohort_service.enroll_student_in_cohort(
                    user_id=user.id,
                    cohort_id=cohort_id,
                    role="student",
                    is_primary=True,
                )
            except Exception:
                pass

    db.session.commit()
    return user


def set_active(user_id: int, active: bool) -> User:
    """فعال/غیرفعال کردن حساب بدون حذف داده."""
    user = db.session.get(User, user_id)
    if not user:
        abort(404)
    user.is_active = active
    db.session.commit()
    return user


def delete_user(user_id: int) -> None:
    """کاربر را حذف می‌کند (وابستگی‌ها توسط دیتابیس کسکید حذف می‌شوند)."""
    user = db.session.get(User, user_id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()

def get_user_detail(user_id: int) -> dict:
    """جزئیات کامل یک دانش‌آموز را برمی‌گرداند."""
    user = db.session.get(User, user_id)
    if not user:
        abort(404)
        
    submissions = Submission.query.filter_by(student_id=user.id).all()
    week_progress = WeekProgress.query.filter_by(user_id=user.id).order_by(WeekProgress.week.asc()).all()
    xp_logs = XPLog.query.filter_by(user_id=user.id).order_by(XPLog.timestamp.desc()).limit(20).all()
    
    return {
        "user": user,
        "submissions": submissions,
        "week_progress": week_progress,
        "xp_logs": xp_logs
    }
