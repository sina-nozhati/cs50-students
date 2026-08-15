"""منطق گیمیفیکیشن XP — توابع خالص و قابل تست.

هر تابع فقط با دیتابیس کار می‌کند و به request یا session وابسته نیست،
پس در pytest بهراحتی قابل آزمون است.
"""
from app import db
from app.models import User, XPLog


def award(user_id: int, amount: int, reason: str) -> None:
    """یک مقدار XP به کاربر میدهد و در XPLog ثبت میکند (audit trail).

    همچنین استریک روزانه را به‌روزرسانی میکند (یک روز فعالیت محسوب میشود).

    Args:
        user_id: شناسه کاربر.
        amount: مقدار XP (مثبت).
        reason: دلیل کسب XP (مثلاً "Read KB Week 6").
    """
    user = db.session.get(User, user_id)
    if user is None:
        return
    user.xp = (user.xp or 0) + amount
    db.session.add(XPLog(user_id=user_id, amount=amount, reason=reason))
    db.session.commit()

    # به‌روزرسانی استریک روزانه — import محلی برای جلوگیری از import دایره‌ای.
    from app.services import streak as streak_service
    streak_service.update_streak(user_id)


def get_total(user_id: int) -> int:
    """مجموع XP یک کاربر را برمیگرداند."""
    user = db.session.get(User, user_id)
    return user.xp if user else 0


def leaderboard(limit: int = 10) -> list[User]:
    """n نفر برتر کلاس را بر اساس XP برمیگرداند — یک کوئری، بدون N+1.

    Returns:
        لیست User مرتب شده از بیشترین XP.
    """
    return User.query.filter_by(is_admin=False).order_by(User.xp.desc()).limit(limit).all()
