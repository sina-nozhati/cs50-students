---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۵ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۵
title_en: Summing Up
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; the note about Trees and ADTs comes from the week page topic list (Summing Up omits Trees); quick-review table is authored. Designed to replace the English official summary on /kb/week/5 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/5/#summing-up
source_refs:
- src-notes-5#summing-up
- src-week-5#week-5-data-structures
- src-anzali-authored-5
prev: w05-n12
next: w05-sec
order: 13
replaces_official_summary_for: week-5
---

# خلاصهٔ هفتهٔ ۵: ساختمان‌های داده

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۵](https://cs50.harvard.edu/x/notes/5/#summing-up) و فهرست مباحث [صفحهٔ هفته](https://cs50.harvard.edu/x/weeks/5/) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس دربارهٔ استفاده از اشاره‌گرها برای ساختن ساختمان‌های دادهٔ تازه یاد گرفتی. به‌طور مشخص این‌ها را دیدی:

- ساختمان‌های داده.
- پشته‌ها و صف‌ها.
- فهرست‌های پیوندی.
- درهم‌سازی و جدول‌های درهم‌سازی.
- ترای‌ها.

> **از صفحهٔ هفته:** فهرست مباحث صفحهٔ هفته «درخت‌ها و درخت‌های جست‌وجوی دودویی» و «نوع‌های دادهٔ انتزاعی» را هم دارد. بخش «Summing Up» درخت‌ها را نام نمی‌برد، هرچند درس‌نامه بخشی کامل برای آن‌ها دارد (ناهمخوانی ثبت‌شده در `sources.json`).

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| ساختمان داده و نوع انتزاعی | نوع انتزاعی رفتار را می‌گوید؛ ساختمان داده چیدمان در حافظه را. | [ساختمان‌های داده](/kb/d/w05-n02) |
| صف | FIFO: اول وارد، اول خارج؛ enqueue و dequeue. | [صف‌ها](/kb/d/w05-n03) |
| پشته | LIFO: آخر وارد، اول خارج؛ push و pop. | [پشته‌ها](/kb/d/w05-n04) |
| آرایهٔ پویا | تکهٔ بزرگ‌تر بگیر، کپی کن، تکهٔ قدیمی را آزاد کن؛ با `tmp` و بررسی `NULL`. | [آرایه‌ها](/kb/d/w05-n05) |
| realloc | بزرگ می‌کند یا جابه‌جا و کپی می‌کند؛ نتیجه را اول در `tmp` بگذار. | [realloc](/kb/d/w05-n06) |
| عملگر `->` | `n->number` همان `(*n).number` است. | [گره‌ها](/kb/d/w05-n07) |
| فهرست پیوندی | گره‌هایی با داده و `next`، تا `NULL`؛ پویا ولی بدون اندیس. | [گره‌ها](/kb/d/w05-n07) |
| افزودن به ابتدا | `n->next = list;` بعد `list = n;`؛ O(1) ولی ترتیب برعکس. | [افزودن به ابتدا](/kb/d/w05-n08) |
| افزودن به انتها و درج مرتب | هر دو O(n)؛ چهار حالت: خالی، ابتدا، انتها، وسط. | [افزودن، مرتب‌سازی، آزادسازی](/kb/d/w05-n09) |
| آزاد کردن فهرست | پیش از هر `free` نشانی بعدی را نگه دار؛ یک `free` برای هر `malloc`. | [افزودن، مرتب‌سازی، آزادسازی](/kb/d/w05-n09) |
| درخت جست‌وجوی دودویی | چپ کوچک‌تر، راست بزرگ‌تر؛ اگر متوازن باشد O(log n). | [درخت‌ها](/kb/d/w05-n10) |
| جدول درهم‌سازی | آرایه‌ای از اشاره‌گرها به گره‌ها؛ تابع درهم‌ساز سطل را تعیین می‌کند. | [جدول‌های درهم‌سازی](/kb/d/w05-n11) |
| برخورد | دو مقدار در یک سطل؛ با زنجیره‌سازی در همان فهرست می‌مانند. | [جدول‌های درهم‌سازی](/kb/d/w05-n11) |
| ترای | درختی از آرایه‌ها؛ جست‌وجو مستقل از تعداد واژه‌ها، با حافظهٔ زیاد. | [ترای‌ها](/kb/d/w05-n12) |

## گام بعدی

- اگر هنوز نگذرانده‌ای، [آزمون تسلط هفته](/kb/d/w05-fa) را بده.
- سپس به [پرابلم‌ست ۵](https://cs50.harvard.edu/x/psets/5/) برو. راهنماهای فارسی از [نمای کلی هفته](/kb/d/w05-fa) در دسترس‌اند.

> **پیوند رسمی:** متن کامل انگلیسی در [cs50.harvard.edu/x/notes/5](https://cs50.harvard.edu/x/notes/5/) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
