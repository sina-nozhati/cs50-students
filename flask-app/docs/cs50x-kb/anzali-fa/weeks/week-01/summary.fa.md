---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۱ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۱
title_en: Summing Up
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; quick-review table is authored. Designed to replace the English official summary on /kb/week/1 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/1/#summing-up
source_refs:
- src-notes-1#summing-up
- src-week-1#week-1-c
- src-anzali-authored-1
prev: w01-n19
next: w01-sec
order: 20
replaces_official_summary_for: week-1
---

# خلاصهٔ هفتهٔ ۱: C

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۱](https://cs50.harvard.edu/x/notes/1/#summing-up) و فهرست مباحث [صفحهٔ هفته](https://cs50.harvard.edu/x/weeks/1/) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس یاد گرفتی بلوک‌های سازنده‌ای را که در Scratch دیدی در زبان C به کار ببری. یاد گرفتی:

- چطور اولین برنامه‌ات را در C بسازی.
- چطور از خط فرمان (command line) استفاده کنی.
- دربارهٔ توابع ازپیش‌تعریف‌شده‌ای که همراه C می‌آیند.
- چطور از متغیرها، شرط‌ها و حلقه‌ها استفاده کنی.
- چطور توابع خودت را بسازی تا کدت ساده‌تر و بهتر شود.
- چطور کدت را روی سه محور بسنجی: درستی (correctness)، طراحی (design) و سبک (style).
- چطور توضیح (comment) را در کدت بگنجانی.
- چطور از انواع داده (types) و عملگرها (operators) استفاده کنی و پیامد انتخاب‌هایت چیست.

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| کامپایلر | کد منبع را به کد ماشین تبدیل می‌کند؛ با `make` صدا زده می‌شود. | [کد منبع](/kb/d/w01-n02) |
| چرخهٔ کار | `code hello.c` ← `make hello` ← `./hello`؛ پس از هر تغییر دوباره `make`. | [سلام دنیا](/kb/d/w01-n04) |
| `printf` و `\n` | چاپ متن؛ `\n` خط تازه است. | [از Scratch به C](/kb/d/w01-n05) |
| `#include` | فایل سرآیند کتابخانه را وارد می‌کند، مثل `stdio.h` و `cs50.h`. | [فایل‌های سرآیند](/kb/d/w01-n06) |
| متغیر و نوع | `string answer = get_string("What's your name? ");` | [سلام به تو](/kb/d/w01-n07) |
| کد قالب | `%s` رشته، `%i` عدد صحیح، `%c` نویسه، `%f` اعشاری، `%li` عدد صحیح بلند. | [کدهای قالب](/kb/d/w01-n11) |
| شرط | `if`، `else if`، `else`؛ `==` مقایسه است و `=` انتساب. | [شرط‌ها](/kb/d/w01-n09) |
| حلقه | `while`، `for`، و `do while` برای «دست‌کم یک بار». | [حلقه‌ها](/kb/d/w01-n15) |
| تابع | پیش‌نمونه، پارامتر، `return`؛ متغیر فقط در حوزهٔ خودش وجود دارد. | [توابع](/kb/d/w01-n16) |
| طراحی | حلقهٔ تودرتو، `const` و تابع کمکی. | [Mario](/kb/d/w01-n18) |
| محدودیت‌ها | سرریز، بریدن در تقسیم صحیح، تبدیل نوع، عدم دقت اعشاری. | [عملگرها](/kb/d/w01-n19) |
| سه محور | `check50`، `design50`، `style50`. | [درستی، طراحی و سبک](/kb/d/w01-n17) |

## گام بعدی

- اگر هنوز نگذرانده‌ای، [آزمون تسلط هفته](/kb/d/w01-fa) را بده.
- سپس به [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/) برو. راهنماهای فارسی از [نمای کلی هفته](/kb/d/w01-fa) در دسترس‌اند.

> **پیوند رسمی:** متن کامل انگلیسی در [cs50.harvard.edu/x/notes/1](https://cs50.harvard.edu/x/notes/1/) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
