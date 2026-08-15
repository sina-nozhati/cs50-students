"""منطق تحویل تکالیف — ایجاد و نمره‌دهی."""
from datetime import datetime

from flask import abort

from app import db
from app.models import Submission, Assignment, User
from app.services import xp as xp_service


def create_submission(student_id: int, assignment_id: int, github_url: str) -> Submission:
    """یک تحویل جدید ثبت میکند و در صورت تحویل به‌موقع ۲۰ XP میدهد."""
    assignment = db.session.get(Assignment, assignment_id)
    if assignment is None:
        abort(404)

    submission = Submission(
        student_id=student_id,
        assignment_id=assignment_id,
        github_url=github_url,
    )
    db.session.add(submission)
    db.session.commit()

    # پاداش تحویل به‌موقع — مقدار XP از تنظیمات تکلیف خوانده میشود
    if assignment.due_date >= datetime.utcnow():
        xp_service.award(
            student_id,
            amount=assignment.xp_reward or 20,
            reason=f"Submitted {assignment.title} on time",
        )

    return submission


def grade(submission_id: int, grade: int, feedback: str = "") -> Submission:
    """به یک تحویل نمره میدهد."""
    submission = db.session.get(Submission, submission_id)
    if submission is None:
        abort(404)
    submission.grade = grade
    submission.feedback = feedback
    db.session.commit()
    return submission
