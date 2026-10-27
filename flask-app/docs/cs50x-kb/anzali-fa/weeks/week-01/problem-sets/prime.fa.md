---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-pr-prime
type: practice-guide
title: راهنمای عددهای اول (Prime)
title_fa: عددهای اول (Prime)
title_en: Prime
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/practice/prime/
source_refs:
- src-practice-prime#getting-started
- src-practice-prime#implementation-details
- src-anzali-authored-1
concept_ids:
- w01-c-for-loop
- w01-c-arithmetic-operators
- w01-c-function-definition
- w01-c-return-value
- w01-c-data-types
- w01-c-else-if-chain
problem_set_ref: weeks/week-01/problem-sets/prime.json
prev: w01-pr-half
next: null
order: 36
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای عددهای اول (Prime)

> **منبع رسمی:** [Prime](https://cs50.harvard.edu/x/practice/prime/) از مسئله‌های تمرینی هفتهٔ ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

تمرین اختیاری: عدد اول عدد طبیعی بزرگ‌تر از ۱ است که فقط بر ۱ و خودش بخش‌پذیر است؛ مثلاً ۳ اول است ولی ۴ نیست (۲ × ۲).

فایل آغازین بازه‌ای را از کاربر می‌گیرد و هر عدد را به تابع بولی `prime` می‌دهد. کار تو کامل‌کردن همین تابع است تا اگر عدد اول بود true و وگرنه false برگرداند. صفحهٔ رسمی ساده‌ترین روش بررسی را در بخش Implementation Details شرح می‌دهد.

## خواسته‌های رسمی

1. تابع بولی prime را کامل کن.
2. main بازه را با هر دو سر شامل بررسی می‌کند.

## شروع کار

`cd`، `mkdir prime`، `cd prime`، سپس فایل آغازین را با wget بگیر.

فایل آغازین رسمی را دانلود کن:

```bash
wget https://cdn.cs50.net/2022/fall/labs/1/prime.c
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: بازهٔ ۱ تا ۱۰۰:

```text
prime/ $ ./prime
Minimum: 1
Maximum: 100
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- حلقهٔ for — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u02`)
- عملگرهای حسابی و باقی‌مانده % — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u01`)
- تعریف تابع — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u01`)
- مقدار بازگشتی و return — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u03`)
- انواع داده در C — [یادداشت](/kb/d/w01-n10) · درس کوتاه `w01-l05` (واحد `w01-l05-u01`)
- زنجیرهٔ else if و شاخه‌های ناسازگار — [یادداشت](/kb/d/w01-n09) · درس کوتاه `w01-l07` (واحد `w01-l07-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی یادآوری می‌کند باقی‌مانده (`%`) به کار می‌آید.
2. طبق تعریف ۱ اول نیست و تنها عدد اول زوج ۲ است.
3. تابع بولی می‌تواند به محض یافتن یک مقسوم‌علیه، فوراً false برگرداند.

## اشتباه‌های رایج

- اول شمردن ۱
- بررسی تقسیم بر خود عدد
- برگرداندن true پیش از بررسی همهٔ مقسوم‌علیه‌ها

## چک‌لیست خودآزمایی

1. ۱ اول شمرده نمی‌شود.
2. ۲ اول شمرده می‌شود.
3. خروجی بازهٔ ۱ تا ۱۰۰ با نمونهٔ رسمی یکی است.
4. بازه‌ای کوچک مثل ۱۰ تا ۲۰ را هم با دست بررسی کرده‌ام.
5. check50 و style50 را اجرا کرده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/prime
```

سبک با style50:

```bash
style50 prime.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: آیا می‌توانی الگوریتم یافتن اعداد اول را کاراتر کنی؟ راه دیگری برای تولید اعداد اول به ذهنت می‌رسد؟

## پیوند رسمی

- [Prime](https://cs50.harvard.edu/x/practice/prime/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
