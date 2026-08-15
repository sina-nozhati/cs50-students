"""ماژول تکالیف (الهام از taklifinow — «الان چه تکلیفی دارم؟»).

روتها:
    /assignments                 — لیست تکالیف فعال + مهلت
    /assignments/<id>/submit     — (POST) ثبت لینک گیت‌هاب بهعنوان تحویل
"""
from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.models import Assignment, Submission
from app.services import submissions as sub_service

bp = Blueprint("assignments", __name__, url_prefix="/assignments")


from app.models import Week

@bp.route("/")
@login_required
def index():
    """لیست تکالیف دسته‌بندی شده بر اساس هفته."""
    db_weeks = Week.query.order_by(Week.number).all()
    weeks = []
    
    for w in db_weeks:
        # Count active assignments for this week
        assign_count = Assignment.query.filter_by(week=w.number, is_active=True).count()
        weeks.append({
            "week": w.number,
            "title": w.title,
            "assignment_count": assign_count,
            "is_published": w.is_published
        })
        
    return render_template("assignments/index.html", weeks=weeks)

@bp.route("/week/<int:week>")
@login_required
def week_assignments(week: int):
    """تکالیف فعال یک هفته خاص."""
    db_week = Week.query.filter_by(number=week).first()
    if not db_week or not db_week.is_published:
        flash("این هفته هنوز منتشر نشده است.", "warning")
        return redirect(url_for('assignments.index'))

    assignments = (
        Assignment.query.filter_by(week=week, is_active=True).order_by(Assignment.due_date).all()
    )
    # یک lookup از assignment_id به آخرین Submission کاربر — برای نمایش وضعیت
    submitted_ids = {
        s.assignment_id: s
        for s in Submission.query.filter_by(student_id=current_user.id).all()
    }
    return render_template(
        "assignments/week.html",
        week=week,
        title=db_week.title,
        assignments=assignments,
        submitted=submitted_ids,
    )


@bp.route("/<int:assignment_id>/submit", methods=["POST"])
@login_required
def submit(assignment_id: int):
    """ثبت لینک گیت‌هاب بهعنوان تحویل تکلیف.

    امنیت: قبل از ثبت، بررسی می‌کنیم که این کاربر قبلاً این تکلیف را تحویل نکرده باشد.
    این جلوی تحویل چندباره و کسب بی‌نهایت XP را می‌گیرد.
    """
    # بررسی تحویل قبلی — جلوگیری از تقلب XP
    existing = Submission.query.filter_by(
        student_id=current_user.id, assignment_id=assignment_id
    ).first()
    if existing is not None:
        flash("شما قبلاً این تکلیف را تحویل داده‌اید.", "warning")
        return redirect(url_for("assignments.index"))

    github_url = request.form.get("github_url", "").strip()
    # اعتبارسنجی بهتر: باید با آدرس گیت‌هاب شروع شود و شامل نام کاربری و مخزن باشد (حداقل دو بخش بعد از اسلش)
    import re
    if not re.match(r"^https://github\.com/[\w.-]+/[\w.-]+/?.*$", github_url):
        flash("لینک گیت‌هاب معتبر نیست. لطفاً لینک دقیق مخزن را وارد کنید.", "error")
        return redirect(url_for("assignments.index"))

    sub_service.create_submission(
        student_id=current_user.id,
        assignment_id=assignment_id,
        github_url=github_url,
    )
    flash("تحویل با موفقیت ثبت شد! ۲۰ XP گرفتید.", "success")
    return redirect(url_for("assignments.index"))
