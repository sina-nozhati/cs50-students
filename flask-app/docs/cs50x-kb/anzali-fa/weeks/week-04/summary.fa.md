---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۴ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۴
title_en: Summing Up
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; the segfault/stack/heap/buffer-overflow line is from the week page topic list and shorts; quick-review table is authored. Designed to replace the English official summary on /kb/week/4 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/4/#summing-up
source_refs:
- src-notes-4#summing-up
- src-week-4#week-4-memory
- src-transcript-4
- src-short-file-pointers
- src-short-dynamic-memory-allocation
- src-anzali-authored-4
prev: w04-n15
next: w04-sec
order: 16
replaces_official_summary_for: week-4
---

# خلاصهٔ هفتهٔ ۴: حافظه

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۴](https://cs50.harvard.edu/x/notes/4/#summing-up) و فهرست مباحث [صفحهٔ هفته](https://cs50.harvard.edu/x/weeks/4/) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس دربارهٔ اشاره‌گرها یاد گرفتی، که به تو امکان می‌دهند به داده در جای مشخصی از حافظه دسترسی پیدا کنی و آن را تغییر بدهی. به‌طور مشخص این‌ها را دیدی:

- هنر پیکسلی.
- مبنای شانزده (هگزادسیمال).
- حافظه.
- اشاره‌گرها.
- رشته‌ها.
- حساب اشاره‌گرها.
- مقایسهٔ رشته‌ها.
- کپی کردن.
- `malloc` و Valgrind.
- مقدارهای زباله.
- جابه‌جایی (swap).
- سرریز.
- `scanf`.
- ورودی و خروجی فایل.

> **از صفحهٔ هفته و Shorts:** خطای قطعه‌بندی (segmentation fault)، پشته، هیپ و سرریز بافر در فهرست مباحث صفحهٔ هفته آمده‌اند؛ `fgetc` و `EOF` و قانون‌های `free` از ویدئوهای کوتاه هستند.

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| پیکسل و RGB | هر پیکسل سه عدد ۰ تا ۲۵۵ برای قرمز، سبز و آبی دارد. | [هنر پیکسلی](/kb/d/w04-n01) |
| هگزادسیمال | رقم‌های 0 تا F؛ دو رقم یک بایت است، مثل `0xFF` برابر ۲۵۵. | [مبنای شانزده](/kb/d/w04-n02) |
| نشانی | هر بایت حافظه نشانی دارد؛ نشانی را معمولاً با `0x` می‌نویسیم. | [حافظه](/kb/d/w04-n03) |
| اشاره‌گر | `int *p = &n;` نشانی `n` را نگه می‌دارد؛ `*p` یعنی برو به آن نشانی. | [اشاره‌گرها](/kb/d/w04-n04) |
| رشته | `string` همان `char *` است: نشانی اولین نویسه، تا `\0`. | [رشته‌ها](/kb/d/w04-n05) |
| حساب اشاره‌گر | `s + 1` نشانی نویسهٔ بعدی است؛ `s[i]` همان `*(s + i)`. | [حساب اشاره‌گرها](/kb/d/w04-n06) |
| مقایسهٔ رشته | `==` نشانی‌ها را می‌سنجد؛ برای محتوا `strcmp` را به کار ببر. | [مقایسهٔ رشته‌ها](/kb/d/w04-n07) |
| کپی | `t = s` فقط نشانی را کپی می‌کند؛ هر دو نام به یک رشته اشاره دارند. | [کپی کردن](/kb/d/w04-n08) |
| malloc و free | `strlen(s) + 1` بایت بگیر، `NULL` را بسنج، `strcpy` کن، در پایان `free`. | [malloc و free](/kb/d/w04-n09) |
| Valgrind | invalid write یعنی نوشتن بیرون از حافظهٔ گرفته‌شده؛ definitely lost یعنی نشت. | [Valgrind](/kb/d/w04-n10) |
| مقدار زباله | متغیر مقداردهی‌نشده هر چیزی می‌تواند باشد؛ اشاره‌گرش خطرناک‌تر است. | [مقدارهای زباله](/kb/d/w04-n11) |
| swap | تابع باید نشانی‌ها را بگیرد تا مقدارهای `main` را عوض کند. | [جابه‌جایی](/kb/d/w04-n12) |
| سرریز | پشته و هیپ به سمت هم رشد می‌کنند؛ بازگشت بی‌پایان پشته را سرریز می‌کند. | [سرریز](/kb/d/w04-n13) |
| scanf | `scanf("%i", &n)` نشانی می‌گیرد؛ برای رشته نمی‌داند چقدر جا لازم است. | [scanf](/kb/d/w04-n14) |
| فایل | `fopen`، بررسی `NULL`، `fprintf` یا `fread` و `fwrite`، و `fclose`. | [ورودی و خروجی فایل](/kb/d/w04-n15) |

## گام بعدی

- اگر هنوز نگذرانده‌ای، [آزمون تسلط هفته](/kb/d/w04-fa) را بده.
- سپس به [پرابلم‌ست ۴](https://cs50.harvard.edu/x/psets/4/) برو. راهنماهای فارسی از [نمای کلی هفته](/kb/d/w04-fa) در دسترس‌اند.

> **پیوند رسمی:** متن کامل انگلیسی در [cs50.harvard.edu/x/notes/4](https://cs50.harvard.edu/x/notes/4/) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
