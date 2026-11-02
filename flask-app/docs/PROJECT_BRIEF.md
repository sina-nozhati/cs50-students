# خلاصهٔ معماری — Anzali-CS50-Hub

## استک

Flask 3 + SQLAlchemy + Flask-Login + CSRF · Jinja2 + Tailwind CDN + HTMX · SQLite · Nginx + Gunicorn

## ساختار

```
flask-app/
  app/__init__.py      # Application Factory
  app/models.py
  app/routes/          # blueprints نازک
  app/services/        # منطق تجاری
  templates/  static/
deploy/                # nginx, systemd, webhook, backup
```

## قراردادها

1. منطق در `services/`؛ route فقط HTTP.
2. بدون SPA / npm build مگر تصمیم مستند.
3. RTL، Crimson `#A51C30`، موبایل‌محور.
4. دانلود فایل فقط از روت مجوزدار؛ Nginx `/static/downloads/` را سرو نمی‌کند.
5. secrets فقط از محیط؛ در کد/لاگ چاپ نشوند.

## نقش‌ها

فعلاً: دانش‌آموز و ادمین (`is_admin`). حساب با `is_active` غیرفعال می‌شود. TA/Mentor آینده است.
