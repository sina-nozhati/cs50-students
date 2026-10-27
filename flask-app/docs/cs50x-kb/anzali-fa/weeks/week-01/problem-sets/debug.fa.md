---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-pr-debug
type: practice-guide
title: راهنمای اشکال‌زدایی (Debug)
title_fa: اشکال‌زدایی (Debug)
title_en: Debug
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/practice/debug/
source_refs:
- src-practice-debug#background
- src-practice-debug#how-to-test-your-code
- src-anzali-authored-1
concept_ids:
- w01-c-debugging-errors
- w01-c-syntax
- w01-c-header-file
- w01-c-variable-declaration
- w01-c-get-string
- w01-c-placeholder
problem_set_ref: weeks/week-01/problem-sets/debug.json
prev: w01-ps-credit
next: w01-pr-half
order: 34
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای اشکال‌زدایی (Debug)

> **منبع رسمی:** [Debug](https://cs50.harvard.edu/x/practice/debug/) از مسئله‌های تمرینی هفتهٔ ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

تمرین اختیاری برای آشنایی با نحو C و پیام‌های خطای کامپایلر. فایل آغازین (distribution code) را دانلود می‌کنی که چند خطای نحوی دارد؛ باید با `make` کامپایل کنی، پیام‌های خطا را بخوانی و یکی‌یکی رفعشان کنی.

صفحهٔ رسمی می‌گوید اولین خطا احتمالاً `debug.c:9:5: error: use of undeclared identifier 'name'` است؛ عدد ۹ یعنی مشکل در خط ۹ است. اشکال‌زدایی فرایندی تکراری است: رفع، کامپایل، دوباره.

## خواسته‌های رسمی

1. خطاهای نحوی debug.c را رفع کن تا کامپایل شود.
2. برنامه طبق نمونه‌ها نام و شهر را بپرسد و سلام کند.

## شروع کار

`cd` را اجرا کن، بعد `mkdir debug` و `cd debug`، سپس فایل آغازین را با wget بگیر و `make debug` بزن.

فایل آغازین رسمی را دانلود کن:

```bash
wget https://cdn.cs50.net/2022/fall/labs/1/debug.c
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی ۱:

```text
debug/ $ ./debug
What is your name? Carter
Where do you live? Cambridge
Hello, Carter, from Cambridge!
```

نمونهٔ رسمی ۲:

```text
debug/ $ ./debug
What is your name? Margaret
Where do you live? New York
Hello, Margaret, from New York!
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- خواندن پیام خطای کامپایلر — [یادداشت](/kb/d/w01-n04) · درس کوتاه `w01-l01` (واحد `w01-l01-u04`)
- نحو C: نقطه‌ویرگول، پرانتز، آکولاد و نقل‌قول — [یادداشت](/kb/d/w01-n05) · درس کوتاه `w01-l02` (واحد `w01-l02-u01`)
- فایل سرآیند و #include — [یادداشت](/kb/d/w01-n06) · درس کوتاه `w01-l03` (واحد `w01-l03-u01`)
- اعلان متغیر با نوع — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u03`)
- get_string و مقدار بازگشتی — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u02`)
- جای‌نگهدار %s — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی پیشنهاد می‌کند دنبال نمادهای جاافتاده، کتابخانه‌های جاافتاده و اعلان‌های جاافتادهٔ متغیر بگردی.
2. اگر گیر کردی، زیر پیام خطا را ببین: help50 راهنمایی زرد می‌دهد، یا دکمهٔ help50 را بزن تا از اردک بپرسی.

## اشتباه‌های رایج

- رفع چند خطا با هم بدون کامپایل دوباره
- نادیده گرفتن شمارهٔ خط در پیام خطا

## چک‌لیست خودآزمایی

1. پیام خطا را خوانده‌ام و شمارهٔ خط و ستون را پیدا کرده‌ام.
2. بعد از هر اصلاح دوباره make کرده‌ام.
3. برنامه بدون خطا کامپایل می‌شود.
4. خروجی با دو نمونهٔ رسمی یکی است.
5. check50 و style50 را اجرا کرده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/debug
```

سبک با style50:

```bash
style50 debug.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چرا فکر می‌کنی C (و زبان‌های دیگر) قواعد نحوی این‌قدر دقیقی دارند؟

## پیوند رسمی

- [Debug](https://cs50.harvard.edu/x/practice/debug/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
