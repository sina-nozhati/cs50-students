"""منطق گیمیفیکیشن XP — توابع خالص و قابل تست.

هر تابع فقط با دیتابیس کار می‌کند و به request یا session وابسته نیست،
پس در pytest بهراحتی قابل آزمون است.

قانون ایدمپوتنسی: برای هر (user_id, reason) حداکثر یک بار XP داده می‌شود.
"""
from app import db
from app.models import User, XPLog, utc_now


def award(user_id: int, amount: int, reason: str) -> bool:
    """یک مقدار XP به کاربر میدهد و در XPLog ثبت میکند (audit trail).

    اگر قبلاً همان reason برای همین کاربر ثبت شده باشد، هیچ XP اضافه‌ای
    داده نمی‌شود (جلوگیری از رویداد تکراری).

    Returns:
        True اگر XP جدید اعطا شد، False اگر تکراری بود یا کاربر نبود.
    """
    user = db.session.get(User, user_id)
    if user is None:
        return False

    existing = XPLog.query.filter_by(user_id=user_id, reason=reason).first()
    if existing is not None:
        return False

    user.xp = (user.xp or 0) + amount
    db.session.add(XPLog(user_id=user_id, amount=amount, reason=reason))
    db.session.commit()

    # به‌روزرسانی استریک روزانه — import محلی برای جلوگیری از import دایره‌ای.
    from app.services import streak as streak_service
    streak_service.update_streak(user_id)
    return True


def deduct(user_id: int, amount: int, reason: str) -> bool:
    """کسر مقدار مشخصی XP از کاربر و ثبت در XPLog (با مقدار منفی)."""
    user = db.session.get(User, user_id)
    if user is None:
        return False
    current_xp = user.xp or 0
    if current_xp < amount:
        return False
    user.xp = current_xp - amount
    from app.models import utc_now
    stamp = utc_now().strftime("%Y%m%d%H%M%S%f")
    db.session.add(XPLog(user_id=user_id, amount=-amount, reason=f"{reason}:{stamp}"))
    db.session.commit()
    return True


def get_total(user_id: int) -> int:
    """مجموع XP یک کاربر را برمیگرداند."""
    user = db.session.get(User, user_id)
    return user.xp if user else 0


def leaderboard(limit: int = 10) -> list[User]:
    """n نفر برتر کلاس را بر اساس XP برمیگرداند — یک کوئری، بدون N+1.

    Returns:
        لیست User مرتب شده از بیشترین XP.
    """
    return User.query.filter_by(is_admin=False, is_active=True).order_by(User.xp.desc()).limit(limit).all()


def weekly_leaderboard(limit: int = 10) -> list[dict]:
    """n نفر برتر هفته اخیر (۷ روز گذشته) بر اساس مجموع XP کسب‌شده.

    انگیزه رقابت را برای کاربران جدید بدون غرق شدن در امتیاز کاربران قدیمی زنده نگه می‌دارد.
    """
    from datetime import timedelta
    from sqlalchemy import desc, func
    seven_days_ago = utc_now() - timedelta(days=7)

    results = (
        db.session.query(
            User.id,
            User.username,
            func.sum(XPLog.amount).label("week_xp")
        )
        .join(XPLog, User.id == XPLog.user_id)
        .filter(XPLog.timestamp >= seven_days_ago, User.is_admin == False, User.is_active == True)
        .group_by(User.id, User.username)
        .order_by(desc("week_xp"))
        .limit(limit)
        .all()
    )

    return [
        {"id": row[0], "username": row[1], "week_xp": int(row[2] or 0)}
        for row in results
    ]
