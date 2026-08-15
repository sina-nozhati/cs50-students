"""مدیریت تکالیف برای پنل ادمین."""
from datetime import datetime
from flask import abort

from app import db
from app.models import Assignment, Submission

def list_all() -> list[Assignment]:
    """تمام تکالیف را به ترتیب تاریخ مهلت نزولی برمی‌گرداند."""
    return Assignment.query.order_by(Assignment.due_date.desc()).all()

def create_assignment(title: str, week: int, due_date: datetime, xp_reward: int = 20, 
                      github_template_url: str | None = None, description: str | None = None) -> Assignment:
    """یک تکلیف جدید ایجاد می‌کند."""
    assignment = Assignment(
        title=title,
        week=week,
        due_date=due_date,
        xp_reward=xp_reward,
        github_template_url=github_template_url,
        description=description
    )
    db.session.add(assignment)
    db.session.commit()
    return assignment

def update_assignment(assignment_id: int, **kwargs) -> Assignment:
    """فیلدهای یک تکلیف را آپدیت می‌کند."""
    assignment = db.session.get(Assignment, assignment_id)
    if not assignment:
        abort(404)
        
    for key, value in kwargs.items():
        if hasattr(assignment, key):
            setattr(assignment, key, value)
            
    db.session.commit()
    return assignment

def toggle_active(assignment_id: int) -> bool:
    """وضعیت فعال بودن تکلیف را تغییر می‌دهد."""
    assignment = db.session.get(Assignment, assignment_id)
    if not assignment:
        abort(404)
        
    assignment.is_active = not assignment.is_active
    db.session.commit()
    return assignment.is_active

def get_submission_stats(assignment_id: int) -> dict:
    """آمار تحویل‌های یک تکلیف را برمی‌گرداند."""
    assignment = db.session.get(Assignment, assignment_id)
    if not assignment:
        abort(404)
        
    from app.models import User
    total_students = User.query.filter_by(is_admin=False).count()
    
    submissions = Submission.query.filter_by(assignment_id=assignment_id).all()
    submitted_count = len(submissions)
    
    graded = [s for s in submissions if s.grade is not None]
    graded_count = len(graded)
    
    avg_grade = sum(s.grade for s in graded) / graded_count if graded_count > 0 else 0
    
    return {
        "total_students": total_students,
        "submitted_count": submitted_count,
        "graded_count": graded_count,
        "avg_grade": round(avg_grade, 2)
    }
