---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۸ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۸
title_en: Summing Up
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; quick-review table and outlook are authored. Designed to replace the English official summary on /kb/week/8 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/8/#summing-up
source_refs:
- src-notes-8#summing-up
- src-week-8#week-8-html-css-javascript
- src-anzali-authored-8
prev: w08-n15
next: w08-sec
order: 16
replaces_official_summary_for: week-8
---

# خلاصهٔ هفتهٔ ۸: HTML، CSS و جاوااسکریپت

> **منبع رسمی:** بخش [Summing Up](https://cs50.harvard.edu/x/2026/notes/8/#summing-up) درس‌نامهٔ هفتهٔ ۸. بخش اول بازنویسی فارسی آن است. جدول مرور سریع و «بعد از این هفته» **تألیفی** هستند.

## در این هفته چه یاد گرفتی؟

در این درس یاد گرفتی فایل‌های HTML خودت را بسازی، به آن‌ها سبک بدهی، از چارچوب‌های آماده استفاده کنی و جاوااسکریپت را به کار ببری. به‌طور مشخص دربارهٔ این‌ها صحبت کردیم:

- اینترنت (Internet)
- مسیریاب‌ها (Routers)
- DNS
- DHCP
- HTTPS
- HTML
- عبارت‌های باقاعده (Regular expressions)
- CSS
- چارچوب‌ها (Frameworks)
- جاوااسکریپت (JavaScript)

## مرور سریع

> **تألیفی:** یک جملهٔ کلیدی برای هر مبحث، با پیوند به یادداشت.

| مبحث | جملهٔ کلیدی | یادداشت |
|---|---|---|
| مسیریاب و IP | بسته‌ها با نشانی IP مقصد، گام‌به‌گام از مسیریاب‌ها می‌گذرند؛ IPv4 ۳۲ بیت و IPv6 ۱۲۸ بیت است. | [یادداشت ۲](/kb/d/w08-n02) |
| TCP | شمارهٔ درگاه خدمت را مشخص می‌کند (۸۰ برای HTTP و ۴۴۳ برای HTTPS) و بستهٔ گم‌شده دوباره فرستاده می‌شود. | [یادداشت ۳](/kb/d/w08-n03) |
| DNS | نام دامنه را به نشانی IP ترجمه می‌کند. | [یادداشت ۴](/kb/d/w08-n04) |
| DHCP | نشانی IP، دروازهٔ پیش‌فرض و سرورهای DNS را به دستگاه می‌دهد. | [یادداشت ۵](/kb/d/w08-n05) |
| HTTP و HTTPS | مرورگر `GET` یا `POST` می‌فرستد و سرور با کد وضعیت و سرآیندها پاسخ می‌دهد. | [یادداشت ۶](/kb/d/w08-n06) |
| HTML | تگ‌ها و ویژگی‌ها سندی می‌سازند که مرورگر آن را درخت می‌کند. | [یادداشت ۷](/kb/d/w08-n07) |
| عنصرهای HTML | فهرست، جدول، تصویر با `alt`، ویدئو و پیوند با `href`. | [یادداشت ۸](/kb/d/w08-n08) |
| فرم | `name` هر ورودی کلید پارامتر در رشتهٔ پرس‌وجوست. | [یادداشت ۹](/kb/d/w08-n09) |
| عبارت باقاعده | `pattern` باید با کل مقدار جور شود؛ اعتبارسنجی مرورگر را می‌شود دور زد. | [یادداشت ۱۰](/kb/d/w08-n10) |
| CSS | ویژگی: مقدار، با انتخابگر نوع، کلاس (`.`) و شناسه (`#`). | [یادداشت ۱۱](/kb/d/w08-n11) |
| چارچوب‌ها | Bootstrap با کلاس‌های آماده ظاهر حرفه‌ای می‌دهد. | [یادداشت ۱۲](/kb/d/w08-n12) |
| رویدادها | `addEventListener` و `DOMContentLoaded`؛ `===` نوع را هم می‌سنجد. | [یادداشت ۱۳](/kb/d/w08-n13) |
| DOM | `innerHTML`، `style`، `keyup` و `setInterval` صفحه را پویا می‌کنند. | [یادداشت ۱۴](/kb/d/w08-n14) |
| تکمیل خودکار | حلقه روی واژه‌ها، `startsWith` و ساختن رشتهٔ `<li>`. | [یادداشت ۱۵](/kb/d/w08-n15) |

## بعد از این هفته

> **تألیفی:** نگاهی به هفتهٔ بعد.

این هفته همهٔ کارها سمت مرورگر بود: صفحه‌ها ثابت بودند و جاوااسکریپت فقط همان صفحه را تغییر می‌داد. فرم‌هایت داده را به سایت دیگری، مثل گوگل، می‌فرستادند. هفتهٔ ۹ با **Flask** سرور خودت را با پایتون می‌نویسی تا فرم‌ها به برنامهٔ خودت برسند، و با SQL هفتهٔ ۷ داده را ذخیره کنی.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
