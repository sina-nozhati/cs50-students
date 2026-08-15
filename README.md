# CS50x Anzali - Student Panel

پلتفرم آموزشی و مدیریت دانشجویان CS50x انزلی. این پروژه با استفاده از معماری سبک و سریع Flask، HTMX، TailwindCSS و دیتابیس SQLite ساخته شده است و برای استقرار روی سرور لینوکس (Ubuntu 24.04) بهینه‌سازی شده است.

## ویژگی‌ها

- سیستم احراز هویت (مدیریت توسط ادمین، بدون ثبت‌نام عمومی)
- پنل دانش‌آموز (مشاهده پیشرفت، تکالیف، رتبه‌بندی، منابع آموزشی)
- سیستم امتیازدهی و استریک (XP & Streak) برای گیمیفیکیشن
- پنل ادمین اختصاصی (مدیریت کاربران، تکالیف، آپلود فایل، آمار و گزارش‌ها)
- رابط کاربری واکنش‌گرا و سریع (با HTMX بدون نیاز به رفرش صفحه)

## تکنولوژی‌ها

- **بک‌اند:** Python 3.12+, Flask, SQLAlchemy, Flask-WTF
- **فرانت‌اند:** HTML5, Jinja2, TailwindCSS v4, HTMX v2
- **پایگاه داده:** SQLite
- **تست:** Pytest

## راه‌اندازی برای توسعه (Development)

1. کلون کردن پروژه:
   ```bash
   git clone https://github.com/sina-nozhati/cs50-students.git
   cd cs50-students/flask-app
   ```

2. ساخت محیط مجازی و نصب وابستگی‌ها:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # در ویندوز: .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. تنظیم متغیرهای محیطی:
   - فایل `.env.example` را به `.env` تغییر نام دهید و مقادیر آن را تنظیم کنید.

4. مقداردهی اولیه دیتابیس:
   ```bash
   python init_db.py
   ```
   *نکته: اطلاعات ورود ادمین پیش‌فرض در خروجی این اسکریپت نمایش داده می‌شود.*

5. اجرای سرور توسعه:
   ```bash
   python run.py
   ```

## راه‌اندازی برای پروداکشن (Production)

پروژه شامل اسکریپت‌های استقرار خودکار برای Ubuntu 24.04 است:
- `deploy/setup.sh`: نصب پیش‌نیازها (Nginx, Python, Gunicorn)
- `deploy/cs50hub.service`: فایل سرویس Systemd برای Gunicorn
- `deploy/cs50hub.conf`: فایل پیکربندی Nginx

برای اطلاعات بیشتر در مورد استقرار، به مستندات [SKILL.md](.agents/skills/fullstack-engineer/SKILL.md) مراجعه کنید.
