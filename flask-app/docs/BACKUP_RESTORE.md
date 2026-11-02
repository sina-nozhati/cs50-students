# بک‌آپ و بازیابی

## بک‌آپ خودکار

اسکریپت: [`deploy/backup_db.sh`](../../deploy/backup_db.sh)

```cron
0 3 * * * /var/www/cs50hub/deploy/backup_db.sh
```

- مسیر DB: `/var/www/cs50hub/flask-app/instance/cs50.db`
- خروجی: `/var/www/cs50hub/backups/cs50_YYYY-MM-DD_HH-MM-SS.db.gz`
- نگه‌داری: ۷ روز اخیر

## بک‌آپ دستی

```bash
sqlite3 /var/www/cs50hub/flask-app/instance/cs50.db ".backup '/tmp/cs50_manual.db'"
gzip -c /tmp/cs50_manual.db > /var/www/cs50hub/backups/cs50_manual.db.gz
```

## بازیابی

1. توقف سرویس: `sudo systemctl stop cs50hub`
2. کپی ایمنی از DB فعلی
3. استخراج بک‌آپ و جایگزینی:

```bash
gunzip -c /var/www/cs50hub/backups/cs50_DESIRED.db.gz > /var/www/cs50hub/flask-app/instance/cs50.db
sudo systemctl start cs50hub
```

4. راستی‌آزمایی: `/health`، ورود ادمین، یک کوئری روی کاربران

## فایل‌های دانلود

پوشهٔ `flask-app/static/downloads/` را جداگانه بک‌آپ کنید (مثلاً `rsync` یا tar)؛ در git نیست.
