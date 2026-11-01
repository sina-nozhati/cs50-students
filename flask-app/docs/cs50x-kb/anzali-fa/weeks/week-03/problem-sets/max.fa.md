---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-pr-max
type: practice-guide
title: راهنمای بیشینه (Max)
title_fa: بیشینه (Max)
title_en: Max
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/max/
source_refs:
- src-practice-max#implementation-details
- src-practice-max#how-to-test-your-code
- src-anzali-authored-3
concept_ids:
- w03-c-linear-search
- w03-c-big-o
- w03-c-omega
problem_set_ref: weeks/week-03/problem-sets/max.json
prev: w03-pr-temps
next: w03-pr-snackbar
order: 34
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای بیشینه (Max)

> **منبع رسمی:** [Max](https://cs50.harvard.edu/x/2026/practice/max/) از مسئله‌های تمرینی هفتهٔ ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

C تابع آماده‌ای برای پیدا کردن بیشینهٔ یک آرایه ندارد، پس خودت یکی می‌سازی. `main` آرایه را می‌سازد، مقدارها را از کاربر می‌گیرد و آرایه و تعداد عضوها را به تابع `max` می‌دهد.

هدف‌های یادگیری رسمی: فرستادن آرایه به تابع و ساختن یک تابع کمکی که بیشینه را پیدا می‌کند.

## خواسته‌های رسمی

1. تابع `max` همهٔ عضوهای آرایه را پیمایش کند و بیشینه را برگرداند.
2. خروجی مثل نمونه‌های رسمی باشد.

## شروع کار

فایل آغازین را با فرمان رسمی دانلود و از حالت فشرده خارج کن. این تمرین check50 دارد ولی تحویل ندارد.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/3/max.zip
unzip max.zip
rm max.zip
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی ۱:

```text
max/ $ ./max
Number of elements: 3
Element 0: 2
Element 1: 10
Element 2: -1
The max value is 10.
```

نمونهٔ رسمی ۲: همه منفی:

```text
max/ $ ./max
Number of elements: 4
Element 0: -100
Element 1: -200
Element 2: -3
Element 3: -5000
The max value is -3.
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- جست‌وجوی خطی — [یادداشت](/kb/d/w03-n02) · درس کوتاه `w03-l01` (واحد `w03-l01-u02`)
- نماد O بزرگ: کران بالا یا بدترین حالت — [یادداشت](/kb/d/w03-n04) · درس کوتاه `w03-l02` (واحد `w03-l02-u01`)
- نماد Ω: کران پایین یا بهترین حالت — [یادداشت](/kb/d/w03-n05) · درس کوتاه `w03-l02` (واحد `w03-l02-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. پیدا کردن بیشینه شبیه جست‌وجوی خطی است: باید به همهٔ خانه‌ها نگاه کنی. O و Ω این کار چیست؟
2. صفحهٔ رسمی دو راه برای مقدار اولیه می‌گوید و هشدار می‌دهد که از صفر شروع نکنی. نمونهٔ دوم رسمی چرا این هشدار را نشان می‌دهد؟

## اشتباه‌های رایج

- شروع از صفر و شکست روی آرایهٔ همه‌منفی
- حلقه با `<=` و خواندن بیرون از آرایه

## چک‌لیست خودآزمایی

1. تابع همهٔ عضوها را می‌بیند.
2. نمونهٔ همه‌منفی رسمی `-3` می‌دهد.
3. check50 همه را سبز نشان می‌دهد.
4. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/max
```

سبک با style50:

```bash
style50 max.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: What types of programs can you think of that might benefit from a `max` helper function?

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/TSe2Z5ZlnpuN3Od14jNKerLqM)

## پیوند رسمی

- [Max](https://cs50.harvard.edu/x/2026/practice/max/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
