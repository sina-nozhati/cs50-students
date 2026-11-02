---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-pr-temps
type: practice-guide
title: راهنمای میانگین دمای بیشینه (Temps)
title_fa: میانگین دمای بیشینه (Temps)
title_en: Average High Temperatures
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/temps/
source_refs:
- src-practice-temps#implementation-details
- src-practice-temps#how-to-test-your-code
- src-anzali-authored-3
concept_ids:
- w03-c-struct
- w03-c-array-of-structs
- w03-c-selection-sort
- w03-c-bubble-sort
- w03-c-swap
problem_set_ref: weeks/week-03/problem-sets/temps.json
prev: w03-pr-atoi
next: w03-pr-max
order: 33
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای میانگین دمای بیشینه (Temps)

> **منبع رسمی:** [Average High Temperatures](https://cs50.harvard.edu/x/2026/practice/temps/) از مسئله‌های تمرینی هفتهٔ ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

دانشمندان اقلیم میانگین‌های سی‌ساله را «نرمال‌های تازه» می‌نامند. در این تمرین میانگین دمای بیشینهٔ ماه ژوئیه برای ۱۰ شهر آمریکا را به ترتیب **نزولی** مرتب می‌کنی.

هدف‌های یادگیری رسمی: تمرین کار با `struct` و به کار بستن الگوریتم‌های مرتب‌سازی. `main` آرایه را مقداردهی و چاپ می‌کند؛ تو تابع `sort_cities` را کامل می‌کنی.

## خواسته‌های رسمی

1. `sort_cities` را با یک الگوریتم مرتب‌سازی O(n²) به انتخاب خودت (مثلاً حبابی، انتخابی یا درجی) کامل کن.
2. مرتب‌سازی بر اساس دما و نزولی باشد.
3. خروجی مثل نمونهٔ رسمی باشد.

## شروع کار

فایل آغازین را با فرمان رسمی دانلود و از حالت فشرده خارج کن. این تمرین check50 و تحویل ندارد.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/3/temps.zip
unzip temps.zip
rm temps.zip
```

## نمونه‌های رسمی ورودی و خروجی

خروجی رسمی:

```text
temps/ $ ./temps

Average July Temperatures by City

Phoenix: 107
Las Vegas: 105
Austin: 97
Miami: 97
Denver: 90
Chicago: 85
New York: 85
Boston: 82
Los Angeles: 82
San Francisco: 66
temps/ $
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- ساختار داده با typedef struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- آرایه‌ای از struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- مرتب‌سازی انتخابی — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u01`)
- مرتب‌سازی حبابی — [یادداشت](/kb/d/w03-n11) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)
- جابه‌جا کردن دو خانه با متغیر موقت — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. کدام الگوریتم این هفته را بهتر می‌فهمی؟ همان را انتخاب کن؛ صفحهٔ رسمی هر الگوریتم O(n²) را می‌پذیرد.
2. مقایسه روی دما انجام می‌شود، ولی جابه‌جایی باید کل struct را جابه‌جا کند تا نام شهر از دمایش جدا نشود.
3. صفحهٔ رسمی یادآوری می‌کند که یک struct را می‌شود با یک دستور انتساب کامل کپی کرد.
4. برای نزولی کردن، کدام علامت مقایسه را باید برعکس کنی؟

## اشتباه‌های رایج

- جابه‌جا کردن فقط دما و جدا شدن نام شهر از دمایش
- مرتب‌سازی صعودی
- خواندن بیرون از مرز آرایه در حلقهٔ حبابی

## چک‌لیست خودآزمایی

1. فقط `sort_cities` را کامل کرده‌ام.
2. ترتیب نزولی است، نه صعودی.
3. خروجی با نمونهٔ رسمی یکی است.
4. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

سبک با style50:

```bash
style50 temps.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: Which of the sorting algorithms did you choose and why?

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/g0UzJMsFC2x5o2KwRHYxJqTs5)

## پیوند رسمی

- [Average High Temperatures](https://cs50.harvard.edu/x/2026/practice/temps/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
