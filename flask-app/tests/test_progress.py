"""تست منطق داشبورد و پیشرفت — services/progress.py.

پوشش‌ها:
    - get_user_stats: XP، streak، تکالیف فعال
    - get_certificate_progress: درصد، هفته‌ی فعلی
    - get_upcoming_assignments: وضعیت تحویل
    - get_class_rank: محاسبه‌ی رتبه
"""
from datetime import datetime, timedelta

import pytest

from app import db
from app.models import User, WeekProgress, Assignment, Submission, XPLog
from app.services import progress as progress_service


class TestGetUserStats:
    """آمار کلی کاربر."""

    def test_basic_stats(self, app, student_user):
        """فیلدهای پایه موجود باشند."""
        stats = progress_service.get_user_stats(student_user.id)
        assert stats["username"] == "ali"
        assert stats["xp"] == 50
        assert stats["streak"] == 2
        assert stats["is_admin"] is False

    def test_active_assignments_count(self, app, student_user):
        """شمارش تکالیف فعال."""
        # یک تکلیف آینده
        a = Assignment(
            title="Pset 1",
            week=0,
            due_date=datetime.utcnow() + timedelta(days=7),
            is_active=True,
        )
        db.session.add(a)
        db.session.commit()

        stats = progress_service.get_user_stats(student_user.id)
        assert stats["active_assignments"] == 1

    def test_expired_assignments_not_counted(self, app, student_user):
        """تکالیف گذشته شمارش نشوند."""
        a = Assignment(
            title="Old Pset",
            week=0,
            due_date=datetime.utcnow() - timedelta(days=7),
            is_active=True,
        )
        db.session.add(a)
        db.session.commit()

        stats = progress_service.get_user_stats(student_user.id)
        assert stats["active_assignments"] == 0


class TestGetCertificateProgress:
    """پیشرفت مدرک."""

    def test_zero_progress(self, app, student_user):
        """بدون WeekProgress → صفر درصد."""
        cert = progress_service.get_certificate_progress(student_user.id)
        assert cert["percent"] == 0
        assert cert["completed_weeks"] == 0
        assert cert["total_weeks"] == 10
        assert cert["current_week"] == 0

    def test_partial_progress(self, app, student_user):
        """۳ هفته تکمیل → ۳۰٪."""
        for w in range(3):
            wp = WeekProgress(
                user_id=student_user.id,
                week=w,
                kb_read=True,
            )
            db.session.add(wp)
        db.session.commit()

        cert = progress_service.get_certificate_progress(student_user.id)
        assert cert["completed_weeks"] == 3
        assert cert["percent"] == 30  # int((3/10)*100)
        assert cert["current_week"] == 3  # هفته‌ی بعدی

    def test_full_progress(self, app, student_user):
        """تمام ۱۰ هفته تکمیل → ۱۰۰٪."""
        for w in range(10):
            wp = WeekProgress(
                user_id=student_user.id,
                week=w,
                kb_read=True,
            )
            db.session.add(wp)
        db.session.commit()

        cert = progress_service.get_certificate_progress(student_user.id)
        assert cert["percent"] == 100
        assert cert["current_week"] == 9  # آخرین هفته (0-based)


class TestGetUpcomingAssignments:
    """تکالیف نزدیک."""

    def test_no_assignments(self, app, student_user):
        """بدون تکلیف → لیست خالی."""
        upcoming = progress_service.get_upcoming_assignments(student_user.id)
        assert upcoming == []

    def test_with_submission(self, app, student_user):
        """تکلیف + تحویل → submitted=True."""
        a = Assignment(
            title="Pset 2",
            week=1,
            due_date=datetime.utcnow() + timedelta(days=5),
            is_active=True,
        )
        db.session.add(a)
        db.session.flush()

        sub = Submission(
            student_id=student_user.id,
            assignment_id=a.id,
            github_url="https://github.com/test/pset2",
            grade=85,
        )
        db.session.add(sub)
        db.session.commit()

        upcoming = progress_service.get_upcoming_assignments(student_user.id)
        assert len(upcoming) == 1
        assert upcoming[0]["submitted"] is True
        assert upcoming[0]["grade"] == 85

    def test_limit_respected(self, app, student_user):
        """حد تعداد رعایت شود."""
        for i in range(5):
            a = Assignment(
                title=f"Pset {i}",
                week=i,
                due_date=datetime.utcnow() + timedelta(days=i + 1),
                is_active=True,
            )
            db.session.add(a)
        db.session.commit()

        upcoming = progress_service.get_upcoming_assignments(student_user.id, limit=3)
        assert len(upcoming) == 3


class TestGetClassRank:
    """رتبه‌ی کلاس."""

    def test_single_student(self, app, student_user):
        """تنها دانش‌آموز → رتبه ۱."""
        rank = progress_service.get_class_rank(student_user.id)
        assert rank["rank"] == 1

    def test_multiple_students(self, app, student_user, admin_user):
        """ادمین XP بیشتر در رتبه‌بندی دانش‌آموز تأثیری ندارد (ادمین فیلتر می‌شود) → رتبه ۱."""
        # admin XP=100 (is_admin=True), student XP=50 (is_admin=False)
        rank = progress_service.get_class_rank(student_user.id)
        assert rank["rank"] == 1
        assert rank["total_students"] == 1  # admin شمارش نمیشود
