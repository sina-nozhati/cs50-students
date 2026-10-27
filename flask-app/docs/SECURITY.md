# امنیت — CS50x Anzali

## کنترل‌های فعلی

- ساخت حساب فقط توسط ادمین (بدون ثبت‌نام عمومی)
- Flask-Login + CSRF (Flask-WTF)
- هش رمز با Werkzeug
- rate-limit ساده روی `/login` (حافظهٔ پروسه)
- فلگ `User.is_active` برای قطع دسترسی بدون حذف
- دانلود منابع: لاگین + `is_published`؛ مسیر Nginx برای `/static/downloads/` مسدود
- آپلود: allowlist `pdf`/`zip` + `secure_filename` + سقف ۳۰MB

## Webhook

- `WEBHOOK_SECRET` باید فقط از محیط خوانده شود؛ مقدار پیش‌فرض در کد وجود ندارد.
- واحد systemd از `EnvironmentFile=/etc/cs50hub/webhook.env` استفاده می‌کند (خارج از git).
- اگر secret قبلاً در مخزن/unit قدیمی افشا شده: **روی سرور rotate کنید**، فایل env را بسازید، webhook گیت‌هاب را به‌روز کنید. این کار نیاز به تأیید صریح production دارد.

## پاسخ به رخداد (خلاصه)

1. قطع دسترسی مشکوک (غیرفعال‌سازی حساب / چرخش secret)
2. بررسی لاگ Nginx و journal سرویس‌ها
3. بک‌آپ فوری DB قبل از هر تغییر
4. مستند کردن زمان، اثر، و اقدام اصلاحی در `DECISIONS.md` (در صورت ایجاد)

## کارهای باز production

- تأیید HTTPS واقعی روی دامنه
- حداقل دسترسی کاربر systemd
- بررسی دوره‌ای وابستگی‌ها (`pip audit` یا معادل)
