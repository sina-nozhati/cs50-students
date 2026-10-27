"""سرویس محاسبه احتمال بازگشت به یادگیری و شناسایی دانش‌آموزان نیازمند راهنمایی.

تمام محاسبات شفاف، مبتنی بر قوانین عادلانه و بدون الگوریتم‌های قضاوت‌گر یا تنبیهی هستند.
"""
from datetime import datetime, timedelta
from app import db
from app.models import User, XPLog, EngagementScore, ExerciseAttempt, WeekProgress, Assignment, Submission


def compute_user_engagement(user_id: int) -> dict:
    """محاسبه احتمال بازگشت فردا و سطح ریسک ریزش."""
    user = db.session.get(User, user_id)
    if not user or not user.is_active or user.is_admin:
        return {"probability": 1.0, "risk_level": "low", "factors": []}

    factors = []
    prob = 0.5  # نقطه آغاز میانی

    now = datetime.utcnow()
    last_log = XPLog.query.filter_by(user_id=user_id).order_by(XPLog.timestamp.desc()).first()

    days_inactive = 0
    if last_log:
        days_inactive = (now - last_log.timestamp).days
    else:
        days_inactive = 7  # اگر اصلاً لاگی ندارد

    # فاکتور ۱: روزهای سپری‌شده از آخرین فعالیت
    if days_inactive == 0:
        prob += 0.35
        factors.append("امروز فعالیت داشته و زنجیره فعال است.")
    elif days_inactive == 1:
        prob += 0.20
        factors.append("دیروز فعالیت داشته است.")
    elif days_inactive <= 3:
        prob -= 0.10
        factors.append(f"{days_inactive} روز است که وارد کلاس نشده است.")
    else:
        prob -= 0.35
        factors.append(f"{days_inactive} روز عدم فعالیت متوالی.")

    # فاکتور ۲: وضعیت استریک
    streak = user.streak or 0
    if streak >= 3:
        prob += 0.15
        factors.append(f"استریک پایدار {streak} روزه دارد.")
    elif streak == 0 and days_inactive > 2:
        prob -= 0.10
        factors.append("استریک فعال ندارد.")

    # فاکتور ۳: وضعیت تکالیف
    active_assignments = Assignment.query.filter_by(is_active=True).all()
    overdue_assignments = 0
    for a in active_assignments:
        sub = Submission.query.filter_by(student_id=user_id, assignment_id=a.id).first()
        if not sub and a.due_date < now:
            overdue_assignments += 1
    if overdue_assignments > 0:
        prob -= 0.15
        factors.append(f"{overdue_assignments} تکلیف تحویل‌نشده از مهلت گذشته دارد.")

    # تعدیل نهایی بین 0.05 تا 0.95
    prob = max(0.05, min(0.95, round(prob, 2)))

    # تعیین سطح ریسک
    if prob >= 0.70:
        risk_level = "low"
    elif prob >= 0.40:
        risk_level = "medium"
    else:
        risk_level = "high"

    # ذخیره در جدول سوابق EngagementScore
    prev_score = (
        EngagementScore.query.filter_by(user_id=user_id)
        .order_by(EngagementScore.computed_at.desc())
        .first()
    )

    record = EngagementScore(
        user_id=user_id,
        latest_prob=prob,
        latest_risk=risk_level,
        previous_prob=prev_score.latest_prob if prev_score else None,
        previous_risk=prev_score.latest_risk if prev_score else None,
        computed_at=now,
        factors_json=factors,
    )
    db.session.add(record)
    db.session.commit()

    return {
        "probability": prob,
        "risk_level": risk_level,
        "factors": factors,
        "days_inactive": days_inactive
    }


def get_students_at_risk() -> list[dict]:
    """لیست دانش‌آموزان نیازمند توجه و راهنمایی برای داشبورد مدرس."""
    students = User.query.filter_by(is_admin=False, is_active=True).all()
    results = []

    for s in students:
        eng = compute_user_engagement(s.id)
        if eng["risk_level"] in ("medium", "high"):
            results.append({
                "user_id": s.id,
                "username": s.username,
                "risk_level": eng["risk_level"],
                "probability": eng["probability"],
                "factors": eng["factors"],
                "days_inactive": eng["days_inactive"],
                "streak": s.streak or 0,
                "xp": s.xp or 0
            })

    results.sort(key=lambda x: (x["risk_level"] != "high", x["probability"]))
    return results
