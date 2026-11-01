---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۹ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۹
title_en: Summing Up
parent: w09-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; quick-review table and outlook are authored. Designed to replace the English official summary on /kb/week/9 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/9/#summing-up
source_refs:
- src-notes-9#summing-up
- src-week-9#week-9-flask
- src-anzali-authored-9
prev: w09-n15
next: w09-sec
order: 16
replaces_official_summary_for: week-9
---

# خلاصهٔ هفتهٔ ۹: Flask

> **منبع رسمی:** بخش [Summing Up](https://cs50.harvard.edu/x/2026/notes/9/#summing-up) درس‌نامهٔ هفتهٔ ۹. بخش اول بازنویسی فارسی آن است. جدول مرور سریع و «بعد از این هفته» **تألیفی** هستند.

## در این هفته چه یاد گرفتی؟

در این درس یاد گرفتی با پایتون، SQL و Flask برنامهٔ وب بسازی. به‌طور مشخص دربارهٔ این‌ها صحبت کردیم:

- Flask
- فرم‌ها (Forms)
- قالب‌ها (Templates)
- روش‌های درخواست (Request methods)
- Flask و SQL
- کوکی و جلسه (Cookies and session)
- APIها
- JSON

## مرور سریع

> **تألیفی:** یک جملهٔ کلیدی برای هر مبحث، با پیوند به یادداشت.

| مبحث | جملهٔ کلیدی | یادداشت |
|---|---|---|
| ایستا و پویا | صفحهٔ پویا سمت سرور با کد و بر اساس ورودی ساخته می‌شود. | [یادداشت ۱](/kb/d/w09-n01) |
| Flask | `@app.route("/")` یک تابع را به یک مسیر وصل می‌کند و مقدار بازگشتی پاسخ است. | [یادداشت ۲](/kb/d/w09-n02) |
| قالب‌ها | `render_template` قالب را با متغیرها پر می‌کند و `{{ }}` خودکار escape می‌شود. | [یادداشت ۳](/kb/d/w09-n03) |
| فرم‌ها | `action` فرم داده را به مسیر دیگری مثل `/greet` می‌فرستد. | [یادداشت ۴](/kb/d/w09-n04) |
| layout | `{% extends %}` و `{% block %}` بخش مشترک صفحه‌ها را یک‌جا نگه می‌دارند. | [یادداشت ۵](/kb/d/w09-n05) |
| روش‌های درخواست | POST داده را در نشانی نمی‌گذارد؛ روش نامجاز خطای 405 می‌دهد. | [یادداشت ۶](/kb/d/w09-n06) |
| مقدار پیش‌فرض | پیش‌فرض `get` فقط وقتی کلید نیست به کار می‌رود، نه برای رشتهٔ خالی. | [یادداشت ۷](/kb/d/w09-n07) |
| اعتبارسنجی | هرگز به ورودی کاربر اعتماد نکن؛ سمت سرور با فهرست مجاز بسنج. | [یادداشت ۸](/kb/d/w09-n08) |
| ثبت‌نام‌ها | `redirect` پاسخ 302 می‌دهد؛ دیکشنری حافظه با خاموشی سرور پاک می‌شود. | [یادداشت ۹](/kb/d/w09-n09) |
| Flask و SQL | `db.execute` با `?` داده را ماندگار می‌کند؛ تغییر داده با POST. | [یادداشت ۱۰](/kb/d/w09-n10) |
| کوکی و جلسه | کوکی مثل مُهر روی دست است؛ جلسه کاربر را بین درخواست‌ها به یاد می‌آورد. | [یادداشت ۱۱](/kb/d/w09-n11) |
| ورود | ورود: نوشتن در `session`؛ خروج: `session.clear()`. | [یادداشت ۱۲](/kb/d/w09-n12) |
| سبد خرید | فهرست در `session` و `WHERE id IN (?)`. | [یادداشت ۱۳](/kb/d/w09-n13) |
| جست‌وجو و Ajax | `LIKE` با `if q`؛ `fetch` فقط فهرست نتایج را عوض می‌کند. | [یادداشت ۱۴](/kb/d/w09-n14) |
| JSON | `jsonify` داده می‌فرستد و مرورگر خودش HTML می‌سازد و باید escape کند. | [یادداشت ۱۵](/kb/d/w09-n15) |

## بعد از این هفته

> **تألیفی:** نگاهی به ادامهٔ راه.

این هفته همهٔ ابزارهای درس کنار هم نشستند: پایتون سمت سرور، SQL برای ماندگاری، HTML و CSS برای نما و جاوااسکریپت برای تعامل. Finance نخستین برنامهٔ وب کامل توست. پس از آن، با همین ابزارها می‌توانی پروژهٔ پایانی خودت را بسازی.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
