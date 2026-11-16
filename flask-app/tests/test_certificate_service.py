"""آزمون‌های اعتبارسنجی سرویس گواهینامه معتبر و فرمول سنجش تسلط (Mastery Certification)."""
from datetime import datetime, timedelta
import pytest
from app import db
from app.models import (
    Assignment,
    Certificate,
    Submission,
    User,
    WeekProgress,
    utc_now,
)
from app.services import certificate as cert_service


def test_calculate_week_mastery_formula(app, student_user):
    with app.app_context():
        # ۱. ابتدا بدون هیچ فعالیتی: نمره ۰ و عدم تسلط
        m0 = cert_service.calculate_week_mastery(student_user.id, 0)
        assert m0["week_total_score"] == 0.0
        assert m0["is_mastered"] is False

        # ۲. مطالعه درسنامه: ۲۰ امتیاز
        wp = WeekProgress(user_id=student_user.id, week=0, kb_read=True)
        db.session.add(wp)
        db.session.commit()

        m1 = cert_service.calculate_week_mastery(student_user.id, 0)
        assert m1["kb_score"] == 20.0
        assert m1["is_mastered"] is False

        # ۳. قبولی در آزمون تسلط با نمره ۱۰۰٪:
        wp.quiz_score = 5
        wp.quiz_total = 5
        wp.quiz_completed = True
        db.session.commit()

        # اگر برای این هفته تکلیفی در دیتابیس نباشد، سهم کوئیز ۸۰٪ و هفته کامل است:
        m2 = cert_service.calculate_week_mastery(student_user.id, 0)
        assert m2["week_total_score"] == 100.0
        assert m2["is_mastered"] is True

        # ۴. افزودن یک تکلیف فعال برای این هفته:
        assign = Assignment(
            title="Scratch Project",
            week=0,
            due_date=utc_now() + timedelta(days=7),
            is_active=True,
        )
        db.session.add(assign)
        db.session.commit()

        # اکنون تکلیف وزن ۴۰٪ دارد و چون ارسال نشده، نمره ۶۰٪ است:
        m3 = cert_service.calculate_week_mastery(student_user.id, 0)
        assert m3["week_total_score"] == 60.0  # 20 KB + 40 Quiz
        assert m3["is_mastered"] is False
        assert "تحویل تکلیف گیت‌هاب با نمره پذیرش حداقل ۷۰٪" in m3["missing_requirements"]

        # ۵. تحویل تکلیف با نمره ۹۰:
        sub = Submission(
            student_id=student_user.id,
            assignment_id=assign.id,
            github_url="https://github.com/cs50/test",
            grade=90,
            graded_at=utc_now(),
        )
        db.session.add(sub)
        db.session.commit()

        m4 = cert_service.calculate_week_mastery(student_user.id, 0)
        assert m4["week_total_score"] == 100.0
        assert m4["is_mastered"] is True


def test_issue_certificate_prevents_unearned(app, student_user):
    with app.app_context():
        # کاربری که تسلط ندارد نباید بتواند مدرک بگیرد
        success, msg, cert = cert_service.issue_certificate(student_user.id)
        assert success is False
        assert cert is None
        assert "شرایط تسلط هنوز تکمیل نشده است" in msg


def test_issue_certificate_success_and_qr(app, student_user):
    with app.app_context():
        # صدور اجباری (force=True) برای تست ساختار خروجی و امضا
        success, msg, cert = cert_service.issue_certificate(
            student_user.id, student_name="علی انزلی‌چی", force=True
        )
        assert success is True
        assert cert is not None
        assert cert.cert_id.startswith("CS50X-ANZ-")
        assert cert.student_name == "علی انزلی‌چی"
        assert len(cert.signature_hash) == 64  # SHA256 hex string
        assert "<svg" in cert.qr_svg

        # استعلام مجدد باید همان گواهینامه را برگرداند (ایدمپوتنت)
        success2, msg2, cert2 = cert_service.issue_certificate(student_user.id, force=True)
        assert success2 is True
        assert cert2.id == cert.id


def test_verify_certificate_tamper_detection(app, student_user):
    with app.app_context():
        _, _, cert = cert_service.issue_certificate(
            student_user.id, student_name="سارا حسینی", force=True
        )

        # استعلام سالم
        v_ok = cert_service.verify_certificate(cert.cert_id)
        assert v_ok["is_valid"] is True
        assert v_ok["student_name"] == "سارا حسینی"

        # جعل نام دانشجو بدون تغییر امضا -> باید تقلب را شناسایی کند
        cert.student_name = "مهاجم دستکاری‌کننده"
        db.session.commit()

        v_tampered = cert_service.verify_certificate(cert.cert_id)
        assert v_tampered["is_valid"] is False
        assert v_tampered["error"] == "tampered"

        # گواهینامه باطل‌شده
        cert.student_name = "سارا حسینی"
        cert.is_revoked = True
        cert.revocation_reason = "درخواست ابطال توسط دانشجو"
        db.session.commit()

        v_revoked = cert_service.verify_certificate(cert.cert_id)
        assert v_revoked["is_valid"] is False
        assert v_revoked["error"] == "revoked"


def test_public_verify_http_route(client, app, student_user):
    with app.app_context():
        _, _, cert = cert_service.issue_certificate(
            student_user.id, student_name="رضا رضایی", force=True
        )
        cid = cert.cert_id

    # کاربر لاگین‌نکرده (عمومی) باید بتواند استعلام بگیرد
    res = client.get(f"/verify/{cid}")
    assert res.status_code == 200
    assert "رضا رضایی".encode("utf-8") in res.data
    assert "CS50x Anzali".encode("utf-8") in res.data

    # استعلام کد نامعتبر
    res_invalid = client.get("/verify/CS50X-INVALID-ID")
    assert res_invalid.status_code == 200
    assert "یافت نشد".encode("utf-8") in res_invalid.data
