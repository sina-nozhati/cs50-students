# انتشار و Rollback — CS50x Anzali

## مسیر پروداکشن

- دامنه: `cs50xanzali.ir`
- مسیر: `/var/www/cs50hub`
- اپ: Gunicorn → `wsgi:app` روی `127.0.0.1:5000` (`cs50hub.service`)
- پروکسی: Nginx (`deploy/nginx.conf`)
- Webhook اختیاری: پورت ۹۰۰۰ (`cs50hub-webhook.service`)

## پیش از انتشار

1. بک‌آپ DB (`deploy/backup_db.sh`)
2. اطمینان از سبز بودن CI روی PR/branch
3. مرور تغییر migration/ستون‌های جدید (`_ensure_sqlite_columns`)

## انتشار دستی (پیشنهادی)

```bash
cd /var/www/cs50hub
git fetch origin
git checkout <tag-or-sha>   # ترجیحاً نه کورکورانه main
source flask-app/.venv/bin/activate
pip install -r flask-app/requirements.txt
sudo systemctl restart cs50hub
curl -sS http://127.0.0.1:5000/health
```

## Webhook auto-deploy

پس از push به `main` اسکریپت `deploy/deploy.sh` اجرا می‌شود. این الگو **بدون gate تست** است؛ مطلوب نهایی نیست. تا اصلاح کامل، برای تغییرات حساس از انتشار دستی استفاده کنید.

## Rollback

1. `git checkout <sha-قبلی>`
2. `pip install -r flask-app/requirements.txt` در صورت نیاز
3. در صورت خرابی داده: بازیابی از بک‌آپ (نگاه کنید به `BACKUP_RESTORE.md`)
4. `systemctl restart cs50hub`
5. چک `/health` و یک مسیر دانش‌آموز (ورود → KB → تکلیف)

## Health check

`GET /health` → `{"status":"ok","service":"anzali-cs50-hub"}`
