"""داشبورد تحلیلی برای ادمین."""
from datetime import datetime, timedelta
from sqlalchemy import func

from app import db
from app.models import User, Assignment, Submission, XPLog, WeekProgress, Week

def get_overview() -> dict:
    """آمار کلی داشبورد را برمی‌گرداند."""
    total_students = User.query.filter_by(is_admin=False).count()
    active_assignments = Assignment.query.filter_by(is_active=True).count()
    
    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_week = today - timedelta(days=today.weekday())
    
    submissions_today = Submission.query.filter(Submission.submitted_at >= today).count()
    submissions_week = Submission.query.filter(Submission.submitted_at >= start_of_week).count()
    
    avg_xp_result = db.session.query(func.avg(User.xp)).filter(User.is_admin.is_(False)).scalar()
    avg_xp = int(avg_xp_result) if avg_xp_result else 0
    
    total_xp_awarded = db.session.query(func.sum(XPLog.amount)).scalar() or 0
    
    return {
        "total_students": total_students,
        "active_assignments": active_assignments,
        "submissions_today": submissions_today,
        "submissions_week": submissions_week,
        "avg_xp": avg_xp,
        "total_xp_awarded": total_xp_awarded
    }

def get_assignment_stats() -> list[dict]:
    """آمار هر تکلیف را برمی‌گرداند."""
    assignments = Assignment.query.order_by(Assignment.week.asc(), Assignment.id.asc()).all()
    total_students = User.query.filter_by(is_admin=False).count()
    
    result = []
    for a in assignments:
        submissions = Submission.query.filter_by(assignment_id=a.id).all()
        submitted_count = len(submissions)
        graded = [s for s in submissions if s.grade is not None]
        graded_count = len(graded)
        avg_grade = sum(s.grade for s in graded) / graded_count if graded_count > 0 else 0
        
        result.append({
            "title": a.title,
            "week": a.week,
            "submitted_count": submitted_count,
            "total_students": total_students,
            "graded_count": graded_count,
            "avg_grade": round(avg_grade, 2)
        })
    return result

def get_weekly_progress_overview() -> list[dict]:
    """نمای کلی پیشرفت کاربران در هفته‌های مختلف."""
    weeks = Week.query.order_by(Week.number.asc()).all()
    # اگر جدولی برای Week نداریم و فقط WeekProgress داریم، می‌توان از 0 تا 8 حلقه زد. 
    # در صورت وجود جدول Week از آن استفاده می‌کنیم. (طبق مدل موجود)
    
    result = []
    week_numbers = [w.number for w in weeks]
    
    for w_num in week_numbers:
        w = next((week for week in weeks if week.number == w_num), None)
        title = w.title if w else f"Week {w_num}"
        is_published = w.is_published if w else False
        
        kb_read_count = WeekProgress.query.filter_by(week=w_num, kb_read=True).count()
        quiz_done_count = WeekProgress.query.filter_by(week=w_num, quiz_completed=True).count()
        flashcard_done_count = WeekProgress.query.filter_by(week=w_num, flashcards_reviewed=True).count()
        
        result.append({
            "week": w_num,
            "title": title,
            "is_published": is_published,
            "kb_read_count": kb_read_count,
            "quiz_done_count": quiz_done_count,
            "flashcard_done_count": flashcard_done_count
        })
    return result

def get_low_engagement_students(days: int = 3) -> list[dict]:
    """دانش‌آموزانی که در روزهای اخیر فعالیتی نداشته‌اند."""
    cutoff = datetime.utcnow() - timedelta(days=days)
    students = User.query.filter_by(is_admin=False).all()
    
    result = []
    for s in students:
        last_log = XPLog.query.filter_by(user_id=s.id).order_by(XPLog.timestamp.desc()).first()
        last_activity = last_log.timestamp if last_log else None
        
        if last_activity is None or last_activity < cutoff:
            result.append({
                "username": s.username,
                "last_activity": last_activity,
                "xp": s.xp or 0
            })
    # مرتب‌سازی بر اساس آخرین فعالیت (کمترین به بیشترین)
    result.sort(key=lambda x: x["last_activity"] or datetime.min)
    return result

def get_top_performers(limit: int = 5) -> list[dict]:
    """دانش‌آموزان برتر بر اساس XP."""
    top_users = User.query.filter_by(is_admin=False).order_by(User.xp.desc()).limit(limit).all()
    return [{"username": u.username, "xp": u.xp or 0} for u in top_users]
