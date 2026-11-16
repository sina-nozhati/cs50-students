"""سرویس گواهینامه معتبر مهارتی و ارزیابی تسلط (Mastery Certification Engine).

این سرویس فرمول سه‌گانه سنجش تسلط:
  (۲۰٪ مطالعه نوت) + (۴۰٪ آزمون تسلط بالای ۸۰٪) + (۴۰٪ تکلیف با نمره بالای ۷۰٪)
را ارزیابی نموده، گواهینامه دیجیتال با امضای HMAC-SHA256 صادر کرده و قابلیت استعلام
عمومی از طریق شناسه یکتا و QR Code را فراهم می‌سازد.
"""
from __future__ import annotations

import hashlib
import hmac
import secrets
from datetime import date, datetime, timezone
from typing import Any

from flask import current_app

from app import db
from app.content.loader import week_numbers
from app.models import (
    Assignment,
    Certificate,
    Cohort,
    Course,
    Submission,
    User,
    Week,
    WeekProgress,
    utc_now,
)


def _get_signing_key() -> bytes:
    """دریافت کلید امضای دیجیتال از تنظیمات اپلیکیشن."""
    secret = current_app.config.get("SECRET_KEY") or "cs50x-anzali-default-secret-key"
    return secret.encode("utf-8")


def sign_certificate_payload(
    cert_id: str, user_id: int, student_name: str, completion_date: str, score: float
) -> str:
    """تولید امضای دیجیتال HMAC-SHA256 بر اساس متادیتای غیرقابل جعل گواهینامه."""
    key = _get_signing_key()
    payload = f"{cert_id}:{user_id}:{student_name}:{completion_date}:{score:.1f}".encode("utf-8")
    return hmac.new(key, payload, hashlib.sha256).hexdigest()


def verify_signature(cert: Certificate) -> bool:
    """اعتبارسنجی ریاضی امضای دیجیتال ذخیره‌شده بر روی مدرک."""
    expected = sign_certificate_payload(
        cert.cert_id,
        cert.user_id,
        cert.student_name,
        cert.completion_date.strftime("%Y-%m-%d"),
        cert.mastery_score,
    )
    return hmac.compare_digest(cert.signature_hash, expected)


def generate_qr_svg(url: str) -> str:
    """تولید کد QR برداری (SVG) خالص در پایتون جهت درج در مدرک و استعلام سریع."""
    try:
        import qrcode
        import qrcode.image.svg

        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(url, image_factory=factory, box_size=10, border=1)
        return img.to_string().decode("utf-8")
    except Exception:
        return ""


def calculate_week_mastery(user_id: int, week: int) -> dict[str, Any]:
    """ارزیابی تسلط یک هفته بر اساس فرمول سه‌گانه رسمی:

    Week Completion = (KB Read * 20%) + (Mastery Quiz >= 80% * 40%) + (Homework Accepted >= 70% * 40%)
    در هفته‌های مفهومی بدون تکلیف، سهم آزمون تسلط به ۸۰٪ ارتقا می‌یابد تا سقف ۱۰۰٪ حفظ شود.
    """
    wp = WeekProgress.query.filter_by(user_id=user_id, week=week).first()

    # ۱. بخش مطالعه پایگاه دانش (۲۰٪)
    kb_read = bool(wp and wp.kb_read)
    kb_score = 20.0 if kb_read else 0.0

    # ۲. بخش آزمون تسلط هفتگی (۴۰٪)
    quiz_passed = False
    quiz_pct = 0.0
    if wp and wp.quiz_total and wp.quiz_total > 0:
        quiz_pct = float(wp.quiz_score or 0) / float(wp.quiz_total)
        quiz_passed = quiz_pct >= 0.8 or bool(wp.quiz_completed)
    elif wp and wp.quiz_completed:
        quiz_passed = True
        quiz_pct = 1.0

    # ۳. بخش تکلیف و پروژه گیت‌هاب (۴۰٪)
    assignments = (
        Assignment.query.filter_by(week=week, is_active=True).all()
    )
    has_homework = len(assignments) > 0
    hw_passed = False
    best_hw_grade = None

    if has_homework:
        assignment_ids = [a.id for a in assignments]
        best_sub = (
            Submission.query.filter(
                Submission.student_id == user_id,
                Submission.assignment_id.in_(assignment_ids),
                Submission.grade.isnot(None),
            )
            .order_by(Submission.grade.desc())
            .first()
        )
        if best_sub and best_sub.grade is not None:
            best_hw_grade = best_sub.grade
            hw_passed = best_sub.grade >= 70
        else:
            hw_passed = False
        quiz_weight = 40.0
        hw_weight = 40.0
    else:
        # هفته‌های بدون تکلیف: آزمون تسلط ۸۰٪ سهم دارد
        quiz_weight = 80.0
        hw_weight = 0.0
        hw_passed = True  # نیازی به تکلیف نیست

    quiz_score = quiz_weight if quiz_passed else (quiz_pct * quiz_weight)
    hw_score = hw_weight if hw_passed else 0.0

    week_total = kb_score + quiz_score + hw_score
    is_mastered = (week_total >= 80.0) and kb_read and quiz_passed and (hw_passed or not has_homework)

    missing = []
    if not kb_read:
        missing.append("مطالعه نوت و اسلایدهای پایگاه دانش")
    if not quiz_passed:
        missing.append("قبولی در آزمون تسلط با نمره حداقل ۸۰٪")
    if has_homework and not hw_passed:
        missing.append("تحویل تکلیف گیت‌هاب با نمره پذیرش حداقل ۷۰٪")

    return {
        "week": week,
        "kb_read": kb_read,
        "kb_score": kb_score,
        "quiz_passed": quiz_passed,
        "quiz_score": quiz_score,
        "quiz_pct": round(quiz_pct * 100, 1),
        "has_homework": has_homework,
        "hw_passed": hw_passed,
        "best_hw_grade": best_hw_grade,
        "hw_score": hw_score,
        "week_total_score": round(week_total, 1),
        "is_mastered": is_mastered,
        "missing_requirements": missing,
    }


def evaluate_certification_eligibility(user_id: int) -> dict[str, Any]:
    """ارزیابی جامع شرایط صدور گواهینامه برای کل دوره ۱۳ هفته‌ای."""
    user = db.session.get(User, user_id)
    if not user:
        return {"is_eligible": False, "error": "user_not_found"}

    # فهرست هفته‌های استاندارد دوره
    weeks = list(week_numbers()) if callable(week_numbers) else list(range(13))
    total_weeks = len(weeks)

    details = {}
    completed_count = 0
    total_scores = 0.0
    missing_by_week = []

    for w in weeks:
        res = calculate_week_mastery(user_id, w)
        details[w] = res
        total_scores += res["week_total_score"]
        if res["is_mastered"]:
            completed_count += 1
        else:
            missing_by_week.append({
                "week": w,
                "missing": res["missing_requirements"],
            })

    overall_mastery = round(total_scores / total_weeks, 1) if total_weeks > 0 else 0.0
    is_eligible = (completed_count == total_weeks)

    return {
        "is_eligible": is_eligible,
        "total_weeks": total_weeks,
        "completed_weeks": completed_count,
        "overall_mastery_pct": overall_mastery,
        "missing_by_week": missing_by_week,
        "weeks_detail": details,
    }


def issue_certificate(
    user_id: int, student_name: str | None = None, force: bool = False
) -> tuple[bool, str, Certificate | None]:
    """صدور رسمی گواهینامه دیجیتال دارای امضای امنیتی و کد QR برای دانشجو.

    در حالت عادی تنها پس از احراز ۱۰۰٪ تسلط (DoD فاز ۳) صادر می‌شود.
    """
    user = db.session.get(User, user_id)
    if not user:
        return False, "کاربر یافت نشد.", None

    # بررسی وجود گواهینامه فعال قبلی
    existing = Certificate.query.filter_by(user_id=user_id, is_revoked=False).first()
    if existing:
        return True, "گواهینامه قبلاً صادر شده است.", existing

    eval_res = evaluate_certification_eligibility(user_id)
    if not force and not eval_res.get("is_eligible", False):
        completed = eval_res.get("completed_weeks", 0)
        total = eval_res.get("total_weeks", 13)
        return (
            False,
            f"شرایط تسلط هنوز تکمیل نشده است ({completed} از {total} هفته پاس شده). آزمون‌های تسلط و تکالیف باقی‌مانده را تکمیل کنید.",
            None,
        )

    name = student_name or user.username
    comp_date = utc_now().date()
    mastery_score = eval_res.get("overall_mastery_pct", 100.0)

    # شناسه یکتا به فرمت: CS50X-ANZ-2026-XXXX
    year = comp_date.year
    token = secrets.token_hex(4).upper()
    cert_id = f"CS50X-ANZ-{year}-{token}"

    sig = sign_certificate_payload(
        cert_id, user_id, name, comp_date.strftime("%Y-%m-%d"), mastery_score
    )

    verify_url = f"/verify/{cert_id}"
    qr_svg = generate_qr_svg(verify_url)

    # انتساب به اولین دوره فعال در صورت وجود
    default_cohort = Cohort.query.filter_by(status="active").first()
    default_course = Course.query.filter_by(is_active=True).first()

    cert = Certificate(
        cert_id=cert_id,
        user_id=user_id,
        course_id=default_course.id if default_course else None,
        cohort_id=default_cohort.id if default_cohort else None,
        student_name=name,
        completion_date=comp_date,
        mastery_score=mastery_score,
        signature_hash=sig,
        qr_svg=qr_svg,
        issued_at=utc_now(),
        is_revoked=False,
    )
    db.session.add(cert)
    db.session.commit()

    return True, "گواهینامه CS50x Anzali با موفقیت صادر شد!", cert


def verify_certificate(cert_id: str) -> dict[str, Any]:
    """استعلام عمومی اصالت گواهینامه برای کارفرمایان و مراجع آموزشی."""
    cert = Certificate.query.filter_by(cert_id=cert_id).first()
    if not cert:
        return {
            "is_valid": False,
            "error": "not_found",
            "message": "گواهینامه‌ای با شناسه مورد نظر در پایگاه داده ثبت نشده است.",
        }

    if cert.is_revoked:
        return {
            "is_valid": False,
            "error": "revoked",
            "message": "این گواهینامه توسط مدیریت دوره ابطال شده است.",
            "reason": cert.revocation_reason or "نقض سیاست صداقت علمی یا درخواست دانشجو",
            "cert_id": cert.cert_id,
            "student_name": cert.student_name,
        }

    # اعتبارسنجی یکپارچگی امضای دیجیتال
    is_signature_valid = verify_signature(cert)
    if not is_signature_valid:
        return {
            "is_valid": False,
            "error": "tampered",
            "message": "امضای دیجیتال گواهینامه با مشخصات ذخیره‌شده تطابق ندارد و فاقد اعتبار است.",
            "cert_id": cert.cert_id,
        }

    return {
        "is_valid": True,
        "cert_id": cert.cert_id,
        "student_name": cert.student_name,
        "completion_date": cert.completion_date.strftime("%Y-%m-%d"),
        "completion_date_fa": f"{cert.completion_date.year}/{cert.completion_date.month:02d}/{cert.completion_date.day:02d}",
        "mastery_score": cert.mastery_score,
        "issued_at": cert.issued_at.isoformat(),
        "qr_svg": cert.qr_svg,
        "course_title": cert.course.title if cert.course else "CS50x Anzali: Computer Science & Programming",
        "cohort_name": cert.cohort.name if cert.cohort else "نوبت رسمی زمستان ۱۴۰۵",
        "institution": "CS50x Anzali Community",
        "is_official_harvard": False,
        "disclaimer_fa": "این گواهی‌نامه اثبات تسلط مهارتی بر مباحث دوره CS50x در جامعه CS50x انزلی است و مستقل از گواهی رسمی دانشگاه هاروارد صادر شده است.",
    }
