---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۲ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۲
title_en: Summing Up
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; cryptography line is from the lecture transcript; quick-review table is authored. Designed to replace the English official summary on /kb/week/2 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/2/#summing-up
source_refs:
- src-notes-2#summing-up
- src-week-2#week-2-arrays
- src-transcript-2
- src-anzali-authored-2
prev: w02-n18
next: w02-sec
order: 20
replaces_official_summary_for: week-2
---

# خلاصهٔ هفتهٔ ۲: آرایه‌ها

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۲](https://cs50.harvard.edu/x/notes/2/#summing-up) و فهرست مباحث [صفحهٔ هفته](https://cs50.harvard.edu/x/weeks/2/) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس جزئیات بیشتری دربارهٔ کامپایل و شیوهٔ ذخیرهٔ داده در کامپیوتر یاد گرفتی. به‌طور مشخص یاد گرفتی:

- به‌طور کلی یک کامپایلر چطور کار می‌کند.
- چطور کدت را با چهار روش اشکال‌زدایی کنی.
- چطور از آرایه‌ها در کدت استفاده کنی.
- چطور آرایه‌ها داده را در بخش‌های پشت سر هم حافظه نگه می‌دارند.
- چطور رشته‌ها در واقع فقط آرایه‌هایی از نویسه‌اند.
- چطور در کدت با آرایه‌ها کار کنی.
- چطور آرگومان‌های خط فرمان به برنامه‌هایت فرستاده می‌شوند.

> **از سخنرانی:** سخنرانی با رمزنگاری تمام شد: متن ساده، کلید، الگوریتم رمز و متن رمز. درس‌نامه بخشی برای آن ندارد (ناهمخوانی d24). [یادداشت رمزنگاری](/kb/d/w02-n18) را ببین.

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| باگ | خطای کامپایل پیام دارد؛ خطای منطقی پیام ندارد اما رفتار را خراب می‌کند. | [باگ و خطاهای کامپایل](/kb/d/w02-n03) |
| اشکال‌زدایی | `printf` موقت، `debug50` با نقطهٔ توقف، و توضیح دادن برای اردک. | [debug50](/kb/d/w02-n05) |
| کامپایل | `make` در واقع `clang` را صدا می‌زند؛ چهار مرحله: پیش‌پردازش، کامپایل، اسمبل، پیوند. | [چهار مرحله](/kb/d/w02-n07) |
| حافظه | هر نوع داده تعداد معینی بایت می‌گیرد؛ مثلاً `int` چهار بایت. | [حافظه](/kb/d/w02-n08) |
| آرایه | مقدارهای هم‌نوع پشت سر هم؛ اندیس از ۰ تا n منهای ۱. | [آرایه‌ها](/kb/d/w02-n09) |
| ثابت و تابع | `const int N` برای اندازه؛ آرایه را می‌توان به تابع فرستاد. | [ثابت سراسری](/kb/d/w02-n10) |
| نویسه | هر `char` یک عدد ASCII است؛ `'A'` برابر ۶۵. | [نویسه‌ها](/kb/d/w02-n11) |
| رشته | آرایه‌ای از نویسه‌ها که با `\0` (NUL) تمام می‌شود. | [رشته و NUL](/kb/d/w02-n12) |
| طول رشته | شمردن تا `\0` یا `strlen` از `string.h`. | [strlen](/kb/d/w02-n14) |
| ctype.h | `islower` و `toupper` و دوستانشان. | [بزرگ‌کردن حروف](/kb/d/w02-n15) |
| خط فرمان | `int main(int argc, string argv[])`؛ `argv[0]` نام برنامه است. | [argc و argv](/kb/d/w02-n16) |
| وضعیت خروج | `return 1` یعنی خطا، `return 0` یعنی موفقیت؛ با `echo $?` ببین. | [وضعیت خروج](/kb/d/w02-n17) |
| رمزنگاری | متن ساده + کلید ← الگوریتم ← متن رمز. | [رمزنگاری](/kb/d/w02-n18) |

## گام بعدی

- اگر هنوز نگذرانده‌ای، [آزمون تسلط هفته](/kb/d/w02-fa) را بده.
- سپس به [پرابلم‌ست ۲](https://cs50.harvard.edu/x/psets/2/) برو. راهنماهای فارسی از [نمای کلی هفته](/kb/d/w02-fa) در دسترس‌اند.

> **پیوند رسمی:** متن کامل انگلیسی در [cs50.harvard.edu/x/notes/2](https://cs50.harvard.edu/x/notes/2/) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
