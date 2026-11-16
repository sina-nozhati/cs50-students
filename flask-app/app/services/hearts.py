"""سرویس مدیریت قلب‌ها و استمرار یادگیری در تمرینات (Hearts Engine).

قوانین سیستم:
- دانشجو حداکثر ۵ قلب دارد.
- هر پاسخ غلط در تمرینات ۱ قلب کسر می‌کند.
- پس از اتمام قلب‌ها (hearts = 0):
  - شارژ خودکار: پس از ۶ ساعت (۲۱۶۰۰ ثانیه) هر ۵ قلب رایگان بازمی‌گردند.
  - شارژ فوری: با پرداخت ۲۰ XP تمام ۵ قلب بلافاصله شارژ می‌شوند.
  - چالش بازیابی: با حل موفق چالش مفهومی، ۱ قلب احیا می‌شود.
- تمام مقادیر در دیتابیس (مدل User) به صورت اتمیک ذخیره می‌شوند.
"""
from __future__ import annotations

from typing import Any
from app import db
from app.models import User, XPLog, utc_now

COOLDOWN_SECONDS: int = 6 * 3600  # ۶ ساعت کول‌داون شارژ خودکار
REFILL_XP_COST: int = 20           # هزینه شارژ فوری ۵ قلب


def get_user_hearts(user_id: int) -> dict[str, Any]:
    """دریافت تعداد قلب‌ها و زمان باقی‌مانده کول‌داون دانشجو به همراه شارژ خودکار."""
    user = db.session.get(User, user_id)
    if not user:
        return {"hearts": 5, "cooldown_seconds": 0, "is_out_of_hearts": False}

    current_hearts = user.hearts if user.hearts is not None else 5
    last_drain = user.last_heart_drain

    # بررسی شارژ خودکار پس از گذشت ۶ ساعت
    if current_hearts < 5 and last_drain is not None:
        now = utc_now()
        elapsed = (now - last_drain).total_seconds()
        if elapsed >= COOLDOWN_SECONDS:
            # زمان کول‌داون تمام شده -> شارژ مجدد ۵ قلب
            user.hearts = 5
            user.last_heart_drain = None
            db.session.commit()
            return {"hearts": 5, "cooldown_seconds": 0, "is_out_of_hearts": False}
        else:
            remaining = max(0, int(COOLDOWN_SECONDS - elapsed))
            return {
                "hearts": current_hearts,
                "cooldown_seconds": remaining,
                "is_out_of_hearts": (current_hearts <= 0),
            }

    return {
        "hearts": current_hearts,
        "cooldown_seconds": 0,
        "is_out_of_hearts": (current_hearts <= 0),
    }


def drain_user_heart(user_id: int) -> dict[str, Any]:
    """کسر یک قلب از دانشجو به دلیل پاسخ غلط. در صورت صفر شدن، تایمر ۶ ساعته فعال می‌شود."""
    user = db.session.get(User, user_id)
    if not user:
        return {"hearts": 0, "cooldown_seconds": COOLDOWN_SECONDS, "is_out_of_hearts": True}

    status = get_user_hearts(user_id)
    current_hearts = status["hearts"]
    new_hearts = max(0, current_hearts - 1)
    user.hearts = new_hearts

    now = utc_now()
    if new_hearts == 0 and user.last_heart_drain is None:
        user.last_heart_drain = now

    db.session.commit()
    return get_user_hearts(user_id)


def refill_user_hearts_with_xp(user_id: int, reason_prefix: str = "practice:hearts:refill:global") -> tuple[bool, str, int]:
    """شارژ کامل ۵ قلب با کسر ۲۰ XP.

    Returns:
        (موفقیت, پیام فارسی, موجودی جدید XP)
    """
    user = db.session.get(User, user_id)
    if not user:
        return False, "کاربر یافت نشد.", 0

    user_xp = user.xp or 0
    if user_xp < REFILL_XP_COST:
        return False, f"برای احیای قلب‌ها حداقل به {REFILL_XP_COST} XP نیاز داری. موجودی فعلی: {user_xp} XP", user_xp

    user.xp = user_xp - REFILL_XP_COST
    user.hearts = 5
    user.last_heart_drain = None

    stamp = utc_now().strftime("%Y%m%d%H%M%S%f")
    log = XPLog(
        user_id=user.id,
        amount=-REFILL_XP_COST,
        reason=f"{reason_prefix}:{stamp}",
    )
    db.session.add(log)
    db.session.commit()

    return True, "قلب‌های شما با موفقیت شارژ شدند!", user.xp


def restore_one_heart(user_id: int) -> dict[str, Any]:
    """احیای یک قلب با انجام موفق چالش مفهومی."""
    user = db.session.get(User, user_id)
    if not user:
        return {"hearts": 1, "cooldown_seconds": 0, "is_out_of_hearts": False}

    current = user.hearts if user.hearts is not None else 0
    new_hearts = min(5, current + 1)
    user.hearts = new_hearts
    if new_hearts > 0:
        user.last_heart_drain = None

    db.session.commit()
    return get_user_hearts(user_id)
