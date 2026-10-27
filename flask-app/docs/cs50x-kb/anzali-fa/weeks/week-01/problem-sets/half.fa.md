---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-pr-half
type: practice-guide
title: راهنمای نصف صورت‌حساب (Half)
title_fa: نصف صورت‌حساب (Half)
title_en: Half
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/practice/half/
source_refs:
- src-practice-half#getting-started
- src-practice-half#implementation-details
- src-anzali-authored-1
concept_ids:
- w01-c-data-types
- w01-c-type-casting
- w01-c-truncation
- w01-c-arithmetic-operators
- w01-c-parameter
- w01-c-return-value
- w01-c-format-codes
problem_set_ref: weeks/week-01/problem-sets/half.json
prev: w01-pr-debug
next: w01-pr-prime
order: 35
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای نصف صورت‌حساب (Half)

> **منبع رسمی:** [Half](https://cs50.harvard.edu/x/practice/half/) از مسئله‌های تمرینی هفتهٔ ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

تمرین اختیاری: با یک دوست در رستوران هستی و می‌خواهی صورت‌حساب را نصف کنید. باید تابع `half` را در فایل آغازین کامل کنی تا سهم هر نفر را بر اساس مبلغ، مالیات و انعام حساب کند و برگرداند.

مالیات و انعام به‌صورت درصد وارد می‌شوند. صفحهٔ رسمی می‌گوید مالیات **پیش از** محاسبهٔ انعام به مبلغ اضافه می‌شود و در پایان دقیقاً نصف کل برگردانده می‌شود.

## خواسته‌های رسمی

1. تابع half را کامل کن تا نصف کل (با مالیات و انعام) را برگرداند.
2. مالیات پیش از انعام اضافه شود.

## شروع کار

`cd`، `mkdir half`، `cd half`، سپس فایل آغازین را با wget بگیر.

فایل آغازین رسمی را دانلود کن:

```bash
wget https://cdn.cs50.net/2022/fall/labs/1/half.c
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی ۱:

```text
half/ $ ./half
Bill before tax and tip: 12.50
Sale Tax Percent: 8.875
Tip percent: 20
You will owe $8.17 each!
```

نمونهٔ رسمی ۲:

```text
half/ $ ./half
Bill before tax and tip: 23.50
Sale Tax Percent: 7  
Tip percent: 15
You will owe $14.46 each!
```

نمونهٔ رسمی ۳:

```text
half/ $ ./half
Bill before tax and tip: 100
Sale Tax Percent: 6.25
Tip percent: 18
You will owe $62.69 each!
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- انواع داده در C — [یادداشت](/kb/d/w01-n10) · درس کوتاه `w01-l05` (واحد `w01-l05-u01`)
- تبدیل نوع (casting) — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u03`)
- بریدن بخش اعشاری در تقسیم صحیح — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u03`)
- عملگرهای حسابی و باقی‌مانده % — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u01`)
- پارامتر تابع در C — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u02`)
- مقدار بازگشتی و return — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u03`)
- کدهای قالب — [یادداشت](/kb/d/w01-n11) · درس کوتاه `w01-l05` (واحد `w01-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی یادآوری می‌کند: انعام به‌صورت int وارد می‌شود و تقسیم int بر int نتیجهٔ int می‌دهد.
2. ترتیب عملیات مثل جبر است: ضرب و تقسیم پیش از جمع و تفریق.
3. یادداشت «بریدن و تبدیل نوع» را مرور کن.

## اشتباه‌های رایج

- تقسیم صحیح درصد انعام
- محاسبهٔ انعام روی مبلغ بدون مالیات
- برگرداندن کل به‌جای نصف

## چک‌لیست خودآزمایی

1. درصدها را پیش از محاسبه به مقدار اعشاری مناسب تبدیل کرده‌ام.
2. مالیات را پیش از انعام اضافه کرده‌ام.
3. مراقب تقسیم int بر int بوده‌ام.
4. هر سه نمونهٔ رسمی را بازتولید کرده‌ام.
5. check50 و style50 را اجرا کرده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/half
```

سبک با style50:

```bash
style50 half.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چرا فکر می‌کنی در C انواع دادهٔ مختلف وجود دارد؟

## ویدئو و نمایش

- [ویدئوی معرفی](https://youtu.be/EYb9jnt2cv4)

## پیوند رسمی

- [Half](https://cs50.harvard.edu/x/practice/half/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
