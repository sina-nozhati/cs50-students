# نقشهٔ راه اجرایی — CS50x Anzali

منبع حقیقت محصول: [`CS50x_Anzali_Master_PRD_v1.0.md`](CS50x_Anzali_Master_PRD_v1.0.md)  
`TODOLIST.md` قدیمی است؛ برای فازبندی فعلی از این فایل استفاده کنید.

## وضعیت فازها

| فاز | نام | وضعیت |
|-----|-----|--------|
| 0 | شناخت واقعیت و کاهش ریسک | انجام‌شده (baseline ۱۸ اکتبر ۲۰۲۶) |
| 1 | امنیت و انتشار قابل اعتماد | در حال انجام در repo |
| 2 | سخت‌کردن مسیر یادگیری | در حال انجام در repo |
| 3 | سنجش و استمرار | در حال انجام در repo |
| 4 | پروژه و جامعه | منتظر معیار ورود |
| 5 | AI Mentor محدود | آینده |
| 6 | Credits محلی | آینده |
| 7 | گسترش منطقه‌ای | آینده |

## فاز 0 — Baseline (ثبت‌شده)

- **pytest baseline اولیه:** ۳۹ تست پاس؛ پس از پیاده‌سازی فاز ۱–۳: **۴۷ تست پاس**.
- **Production audit:** بدون دسترسی SSH در این چرخه انجام نشد — فقط ریسک‌های گزارش‌شده در PRD §9.
- **ریسک‌های P0 شناسایی‌شده:**
  1. سرو مستقیم `static/downloads` توسط Nginx
  2. secret پیش‌فرض webhook در کد
  3. نبود CI روی PR
  4. نامشخص بودن HTTPS روی VPS زنده
  5. deploy مستقیم پس از push بدون gate تست

## فاز 1 — اقدامات repo

- مسدودسازی `/static/downloads/` در Nginx + چک `is_published` در روت دانلود
- حذف default از `WEBHOOK_SECRET` (چرخش واقعی روی سرور نیاز به تأیید جدا دارد)
- GitHub Actions: فقط `pytest` روی PR/push — بدون deploy خودکار
- مستندات SECURITY / DEPLOYMENT / BACKUP_RESTORE
- rate-limit ورود + فلگ `User.is_active`

## فاز 2 — مسیر LEARN

- مسیر مدرک بر اساس `kb_read` (بدون وابستگی به کوییز)
- resubmit لینک GitHub تا قبل از نمره؛ بدون XP مجدد
- ایدمپوتنسی `award(user_id, reason)`
- تست‌های مجوز، فایل، XP تکراری، تحویل

## فاز 3 — سنجش

- شاخص‌های FR-10: به‌موقع/دیر، میانه زمان بازخورد
- اعلان داخل‌پنل + هدف هفتگی روی داشبورد
- اعداد هدف North Star بعد از baseline واقعی کلاس تعیین می‌شوند

## پایگاه دانش CS50x 2026

- منبع حقیقت: `docs/cs50x-kb/` (درخت markdown + `index.json`) از طریق `app/content/kb_repo.py`
- سرویس/رندر: `app/services/kb_content.py` + `app/content/md_render.py`
- سازگاری: `app/content/loader.py` و `app/content/cs50x_2026.py` (thin) — دادهٔ هاردکد ندارند
- UI: `/kb/`، `/kb/week/<n>`، `/kb/d/<doc_id>` با prose، OFFICIAL/GENERATED، TOC، mark-read
- شماره‌ها: 0–10 · AI=`71` · Final=`99` (ترتیب نمایش: 0–7 → AI → 8–10 → Final) — پس از pull یک‌بار `python init_db.py` برای seed هفته‌ها

## معیار ورود به فاز 4

هسته امن، مسیر LEARN پایدار، حداقل یک چرخه بازخورد از دانش‌آموز/TA.
