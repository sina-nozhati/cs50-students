---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۳ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۳
title_en: Summing Up
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; the Omega/Theta/struct/call-stack line is from the lecture and shorts; quick-review table is authored. Designed to replace the English official summary on /kb/week/3 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/3/#summing-up
source_refs:
- src-notes-3#summing-up
- src-week-3#week-3-algorithms
- src-transcript-3
- src-short-call-stacks
- src-anzali-authored-3
prev: w03-n14
next: w03-sec
order: 20
replaces_official_summary_for: week-3
---

# خلاصهٔ هفتهٔ ۳: الگوریتم‌ها

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۳](https://cs50.harvard.edu/x/notes/3/#summing-up) و فهرست مباحث [صفحهٔ هفته](https://cs50.harvard.edu/x/weeks/3/) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس دربارهٔ تفکر الگوریتمی و ساختن نوع‌های دادهٔ خودت یاد گرفتی. به‌طور مشخص یاد گرفتی:

- الگوریتم‌ها.
- نماد O بزرگ.
- جست‌وجوی دودویی و جست‌وجوی خطی.
- الگوریتم‌های گوناگون مرتب‌سازی، از جمله حبابی، انتخابی و ادغامی.
- بازگشت.

> **از سخنرانی و Shorts:** نماد Ω و Θ، `struct` و پشتهٔ فراخوانی هم این هفته آمدند، هرچند فهرست «Summing Up» فقط O را نام می‌برد.

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| الگوریتم | ورودی، گام‌های دقیق، خروجی؛ کیفیتش را با رشد زمان اجرا می‌سنجیم. | [خوش‌آمد](/kb/d/w03-n01) |
| جست‌وجوی خطی | از چپ به راست تا پیدا شود؛ «پیدا نشد» فقط بعد از دیدن همه. | [جست‌وجوی خطی](/kb/d/w03-n02) |
| جست‌وجوی دودویی | هر بار نصف کن؛ فقط روی دادهٔ مرتب. | [جست‌وجوی دودویی](/kb/d/w03-n03) |
| O بزرگ | کران بالا؛ خطی O(n)، دودویی O(log n). | [زمان اجرا](/kb/d/w03-n04) |
| Ω و Θ | Ω کران پایین است؛ اگر O و Ω یکی باشند، Θ. | [Ω و Θ](/kb/d/w03-n05) |
| جست‌وجو در C | حلقه روی آرایه و `return 0` یا `return 1` از main. | [search.c](/kb/d/w03-n06) |
| strcmp | رشته‌ها را با `==` نسنج؛ `strcmp` برای برابر بودن ۰ برمی‌گرداند. | [رشته‌ها](/kb/d/w03-n07) |
| struct | `typedef struct` چند فیلد مرتبط را یک نوع می‌کند؛ دسترسی با نقطه. | [ساختارها](/kb/d/w03-n09) |
| انتخابی | کوچک‌ترین را پیدا کن و جابه‌جا کن؛ Θ(n²). | [انتخابی](/kb/d/w03-n10) |
| حبابی | جفت‌های کنار هم را جابه‌جا کن؛ O(n²) و Ω(n) با توقف زودهنگام. | [حبابی](/kb/d/w03-n11) |
| بازگشت | حالت پایه + حالت بازگشتی که مسئله را کوچک‌تر می‌کند. | [بازگشت](/kb/d/w03-n12) |
| ادغامی | نیمهٔ چپ، نیمهٔ راست، ادغام؛ Θ(n log n) با حافظهٔ بیشتر. | [ادغامی](/kb/d/w03-n14) |

## گام بعدی

- اگر هنوز نگذرانده‌ای، [آزمون تسلط هفته](/kb/d/w03-fa) را بده.
- سپس به [پرابلم‌ست ۳](https://cs50.harvard.edu/x/psets/3/) برو. راهنماهای فارسی از [نمای کلی هفته](/kb/d/w03-fa) در دسترس‌اند.

> **پیوند رسمی:** متن کامل انگلیسی در [cs50.harvard.edu/x/notes/3](https://cs50.harvard.edu/x/notes/3/) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
