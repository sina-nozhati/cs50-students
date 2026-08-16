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
            "submissions_count": Submission.query.filter_by(student_id=s.id).count(),
            "last_activity": last_log.timestamp if last_log else None
        })
    return result

def create_user(username: str, password: str) -> User:
    """کاربر جدید ایجاد می‌کند."""
    existing = User.query.filter_by(username=username).first()
    if existing:
        raise ValueError("Username already exists")
    
    user = User(
        username=username,
        password_hash=generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user_id: int, username: str | None = None, password: str | None = None, xp_adjustment: int = 0) -> User:
    """رمز عبور، نام کاربری یا XP کاربر را آپدیت می‌کند."""
    user = db.session.get(User, user_id)
    if not user:
        abort(404)
        
    if username and username != user.username:
        existing = User.query.filter_by(username=username).first()
        if existing:
            raise ValueError("Username already exists")
        user.username = username
        
    if password:
        user.password_hash = generate_password_hash(password)
        
    if xp_adjustment != 0:
        # برای تغییر XP، بهتر است از سرویس xp استفاده کنیم تا لاگ هم ثبت شود
        if xp_adjustment > 0:
            xp_service.award(user.id, xp_adjustment, "Admin adjustment")
        else:
            # فعلا متد کاهش نداریم در صورت نیاز می‌شود مستقیما کم کرد
            # فرض می‌کنیم متد جایگزین داریم یا مستقیم ویرایش می‌کنیم:
            user.xp = max(0, (user.xp or 0) + xp_adjustment)
            log = XPLog(user_id=user.id, amount=xp_adjustment, reason="Admin penalty")
            db.session.add(log)
            
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
