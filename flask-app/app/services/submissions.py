"""منطق تحویل تکالیف — ایجاد، به‌روزرسانی لینک، و نمره‌دهی."""
from datetime import datetime

from flask import abort

from app import db
from app.models import Submission, Assignment
from app.services import xp as xp_service


def create_submission(student_id: int, assignment_id: int, github_url: str) -> Submission:
    """یک تحویل جدید ثبت میکند و در صورت تحویل به‌موقع XP میدهد.

    reason یکتا است تا award ایدمپوتنت بماند حتی اگر مسیر دوباره صدا زده شود.
    """
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

    if assignment.due_date >= datetime.utcnow():
        xp_service.award(
            student_id,
            amount=assignment.xp_reward or 20,
            reason=f"submit:assignment:{assignment_id}",
        )

    return submission


def update_submission_url(
    student_id: int, assignment_id: int, github_url: str
) -> Submission:
    """به‌روزرسانی لینک GitHub یک تحویل موجود — بدون XP مجدد.

    سیاست resubmit: دانش‌آموز می‌تواند لینک را اصلاح کند تا وقتی نمره نگرفته.
    """
    submission = Submission.query.filter_by(
        student_id=student_id, assignment_id=assignment_id
    ).first()
    if submission is None:
        abort(404)
    if submission.grade is not None:
        abort(403)
    submission.github_url = github_url
    submission.submitted_at = datetime.utcnow()
    db.session.commit()
    return submission


def grade(submission_id: int, grade: int, feedback: str = "") -> Submission:
    """به یک تحویل نمره میدهد و اعلان داخل‌پنل برای دانش‌آموز می‌سازد."""
    submission = db.session.get(Submission, submission_id)
    if submission is None:
        abort(404)
    submission.grade = grade
    submission.feedback = feedback
    submission.graded_at = datetime.utcnow()
    db.session.commit()

    from app.services import notifications as notif_service
    title = f"بازخورد تکلیف: نمره {grade}"
    body = (feedback[:200] if feedback else "نمرهٔ شما ثبت شد.")
    notif_service.create(
        user_id=submission.student_id,
        title=title,
        body=body,
        link="/assignments",
    )
    return submission
