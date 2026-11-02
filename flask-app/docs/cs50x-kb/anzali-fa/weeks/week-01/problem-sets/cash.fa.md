---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-ps-cash
type: problem-set-guide
title: راهنمای پول خرد (Cash)
title_fa: پول خرد (Cash)
title_en: Cash
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/psets/1/cash/
source_refs:
- src-pset-1-cash#problem-to-solve
- src-anzali-authored-1
- src-pset-1#what-to-do
concept_ids:
- w01-c-get-int
- w01-c-do-while
- w01-c-input-validation
- w01-c-while-loop
- w01-c-arithmetic-operators
- w01-c-truncation
- w01-c-function-definition
- w01-c-return-value
problem_set_ref: weeks/week-01/problem-sets/cash.json
prev: w01-ps-mario-more
next: w01-ps-credit
order: 32
submission: one-of-cash-credit
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای پول خرد (Cash)

> **منبع رسمی:** [Cash](https://cs50.harvard.edu/x/psets/1/cash/) از پرابلم‌ست ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از Cash یا Credit را تحویل بده (اگر هر دو، نمرهٔ بالاتر حساب می‌شود). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

فرض کن صندوق‌دار فروشگاهی و باید «باقی پول» مشتری را با کمترین تعداد سکه بدهی. سکه‌ها quarter (۲۵ سنت)، dime (۱۰ سنت)، nickel (۵ سنت) و penny (۱ سنت) هستند. برنامه مقدار باقی پول را به سنت می‌گیرد و **کمترین تعداد سکه** را چاپ می‌کند.

صفحهٔ رسمی «الگوریتم حریصانه» (greedy algorithm) را معرفی می‌کند: در هر گام بهترین انتخاب فوری را انجام بده. برای پول آمریکا (و اتحادیهٔ اروپا) این روش کمترین تعداد سکه را هم می‌دهد.

ورودی نامعتبر (منفی یا غیرعددی) را رد کن و دوباره بپرس.

## خواسته‌های رسمی

1. فایل `cash.c` در پوشهٔ `cash`
2. کمترین تعداد سکه برای باقی پول را چاپ کند.
3. ورودی int به سنت؛ اگر بزرگ‌تر یا مساوی ۰ نبود یا int نبود، دوباره بپرسد.

> **ناهمخوانی رسمی:** متن صفحه یک بار می‌گوید «int بزرگ‌تر از ۰» و بار دیگر «اگر بزرگ‌تر یا مساوی ۰ نبود دوباره بپرس». فهرست آزمون رسمی ورودی ۰ را با خروجی ۰ می‌پذیرد. ملاک check50 است.

## شروع کار

پوشهٔ `cash` را بساز، واردش شو و `code cash.c` را اجرا کن.

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: ۲۵ سنت:

```text
Change owed: 25
1
```

نمونهٔ رسمی: ۷۰ سنت:

```text
Change owed: 70
4
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- get_int — [یادداشت](/kb/d/w01-n13) · درس کوتاه `w01-l07` (واحد `w01-l07-u03`)
- حلقهٔ do while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- اعتبارسنجی ورودی و درخواست دوباره — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- حلقهٔ while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u01`)
- عملگرهای حسابی و باقی‌مانده % — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u01`)
- بریدن بخش اعشاری در تقسیم صحیح — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u03`)
- تعریف تابع — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u01`)
- مقدار بازگشتی و return — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. با دست حل کن: برای ۴۱ سنت یک صندوق‌دار حریص اول کدام سکه را می‌دهد؟ بعد چه مقدار باقی می‌ماند؟
2. تقسیم صحیح و باقی‌مانده (`/` و `%`) را از یادداشت عملگرها مرور کن؛ جلسهٔ حل تمرین هم گفت این‌ها در Cash به کار می‌آیند.
3. کار تکراری برای هر نوع سکه را می‌توان در یک تابع با پارامتر و مقدار بازگشتی گذاشت.

## اشتباه‌های رایج

- فراموش‌کردن کم‌کردن ارزش سکه‌های داده‌شده از باقی پول
- پذیرفتن ورودی منفی
- چاپ متن اضافه همراه عدد

## چک‌لیست خودآزمایی

1. برای -1 دوباره پرسیده می‌شود.
2. برای حروف و ورودی خالی دوباره پرسیده می‌شود.
3. خروجی برای ۰ برابر 0 است.
4. همهٔ مقادیر فهرست «How to Test» صفحهٔ رسمی را امتحان کرده‌ام.
5. خروجی فقط یک عدد و `\n` است.
6. کد تکراری را با تابع یا حلقه کم کرده‌ام (طراحی).
7. check50 و style50 را اجرا کرده‌ام.
8. با submit50 تحویل داده‌ام (یا Credit را).

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/cash
```

سبک با style50:

```bash
style50 cash.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/cash
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [بخش «Advice» صفحهٔ رسمی (شبه‌کد هفت‌مرحله‌ای و تابع calculate_quarters)](https://cs50.harvard.edu/x/psets/1/cash/#advice): شبه‌کد و کد این بخش تقریباً کل راه‌حل را می‌دهند؛ در این بسته بازتولید نشده است.
- [فهرست مقادیر آزمون «How to Test»](https://cs50.harvard.edu/x/psets/1/cash/#how-to-test): خروجی‌های مورد انتظار برای چند ورودی؛ از صفحهٔ رسمی ببین تا با کد خودت مقایسه کنی.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/p6PlFqQgSWNWn4ggpIIaBOvIq)

## پیوند رسمی

- [Cash](https://cs50.harvard.edu/x/psets/1/cash/)
- [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
