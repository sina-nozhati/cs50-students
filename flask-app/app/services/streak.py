"""منطق استریک روزانه — توابع خالص و قابل تست.

استریک = تعداد روزهای متوالی که دانشآموز فعالیتی داشته (کوییز/درس/تحویل).
ما یک «روز فعالیت» را با داشتن حداقل یک رکورد XPLog در آن روز تعریف میکنیم.
این رویکرد تقلب‌پذیر نیست (XPLog هرگز پاک نمیشود) و به زمان‌بندی سرور وابسته نیست.

منطق به‌روزرسانی (وقتی کاربر XP میگیرد):
    - اگر آخرین فعالیت = امروز → تغییری نیست (همان روز).
    - اگر آخرین فعالیت = دیروز → streak + 1.
    - در غیر این صورت → streak = 1 (شروع دوباره).

نکته‌ی مهم: همه‌ی مقایسه‌ها با UTC انجام می‌شود چون XPLog
با datetime.utcnow() ثبت می‌شود. استفاده از date.today() (محلی)
در سرورهایی با timezone متفاوت باعث باگ off-by-one می‌شود.
"""
from datetime import datetime, date, timedelta, timezone

from app import db
from app.models import User, XPLog


def _utc_today() -> date:
    """تاریخ امروز در UTC — برای هماهنگی با XPLog timestamps."""
    return datetime.now(timezone.utc).date()


def _latest_activity_date(user_id: int) -> date | None:
    """آخرین تاریخی که کاربر در آن XP گرفته را برمیگرداند (یا None)."""
    latest = (
        db.session.query(XPLog.timestamp)
        .filter_by(user_id=user_id)
        .order_by(XPLog.timestamp.desc())
        .first()
    )
    if latest is None:
        return None
    # SQLAlchemy tuple را برمیگرداند: (timestamp,)
    # timestamp ذخیره‌شده naive UTC است (از datetime.utcnow)
    return latest[0].date()


def update_streak(user_id: int) -> int:
    """استریک کاربر را بر اساس آخرین فعالیت در XPLog به‌روزرسانی میکند.

    باید بعد از هر award() صدا زده شود. award() قبلاً XPLog امروز
    را ثبت کرده، بنابراین آخرین فعالیت = امروز است. بنابراین:
      - اگر streak از قبل > 0 و هیچ XPLog قبلی نبود → اولین روز = 1
      - اگر فعالیت قبلی = دیروز → ادامه زنجیره
      - در غیر این صورت → شروع مجدد

    برای این کار باید **قبل از XPLog امروز** آخرین فعالیت را ببینیم.
    پس XPLog امروز را موقتاً نادیده می‌گیریم.

    Returns:
        مقدار جدید streak.
    """
    user = db.session.get(User, user_id)
    if user is None:
        return 0

    today = _utc_today()

    # آخرین فعالیت **قبل از امروز** (نه خود امروز)
    prev = (
        db.session.query(XPLog.timestamp)
        .filter_by(user_id=user_id)
        .filter(XPLog.timestamp < datetime.combine(today, datetime.min.time()))
        .order_by(XPLog.timestamp.desc())
        .first()
    )

    if prev is None:
        # هیچ فعالیت قبلی → اولین روز
        user.streak = 1
    else:
        prev_date = prev[0].date()
        if prev_date == today - timedelta(days=1):
            # دیروز فعالیت داشته → ادامه زنجیره
            # اگر streak از قبل 0 بود (مثلاً ریست شده)، حداقل ۱ در نظر بگیر
            user.streak = max(user.streak or 0, 1) + 1
        else:
            # فاصله‌ی بیش از ۱ روز → شروع مجدد
            user.streak = 1

    db.session.commit()
    return user.streak


def get_streak(user_id: int) -> int:
    """مقدار فعلی streak کاربر را برمیگرداند (بدون تغییر)."""
    user = db.session.get(User, user_id)
    return user.streak if user else 0


def get_streak_history(user_id: int, days: int = 7) -> list[dict]:
    """تاریخچه‌ی n روز اخیر را برای نمایش بصری برمیگرداند.

    Returns:
        لیستی از dict با کلیدهای date (date)، label (نام روز فارسی)، studied (bool).
        مرتب از قدیمی به جدید.
    """
    persian_weekdays = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه"]
    today = _utc_today()

    # مجموعه‌ی تاریخ‌هایی که کاربر فعالیت داشته (UTC)
    start_datetime = datetime.combine(today - timedelta(days=days - 1), datetime.min.time())
    activity_dates = {
        row[0].date()
        for row in db.session.query(XPLog.timestamp)
        .filter_by(user_id=user_id)
        .filter(XPLog.timestamp >= start_datetime)
        .all()
    }

    history = []
    for i in range(days - 1, -1, -1):
        d = today - timedelta(days=i)
        label = persian_weekdays[d.weekday()]
        history.append(
            {
                "date": d,
                "label": label,
                "studied": d in activity_dates,
                "is_today": d == today,
            }
        )
    return history
