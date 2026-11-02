---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-ps-credit
type: problem-set-guide
title: راهنمای کارت اعتباری (Credit)
title_fa: کارت اعتباری (Credit)
title_en: Credit
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/psets/1/credit/
source_refs:
- src-pset-1-credit#problem-to-solve
- src-pset-1-credit#implementation-details
- src-anzali-authored-1
- src-pset-1#what-to-do
concept_ids:
- w01-c-data-types
- w01-c-type-sizes
- w01-c-cs50-library
- w01-c-arithmetic-operators
- w01-c-while-loop
- w01-c-logical-operators
- w01-c-else-if-chain
- w01-c-function-definition
problem_set_ref: weeks/week-01/problem-sets/credit.json
prev: w01-ps-cash
next: w01-pr-debug
order: 33
submission: one-of-cash-credit
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای کارت اعتباری (Credit)

> **منبع رسمی:** [Credit](https://cs50.harvard.edu/x/psets/1/credit/) از پرابلم‌ست ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از Cash یا Credit را تحویل بده (اگر هر دو، نمرهٔ بالاتر حساب می‌شود). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

هر شمارهٔ کارت اعتباری ساختار دارد. American Express پانزده رقمی است و با 34 یا 37 شروع می‌شود. بیشتر MasterCardها شانزده رقمی‌اند و با 51 تا 55 شروع می‌شوند. Visa سیزده یا شانزده رقمی است و با 4 شروع می‌شود.

علاوه بر این، شماره یک «رقم کنترلی» دارد که با **الگوریتم Luhn** بررسی می‌شود. صفحهٔ رسمی الگوریتم را گام‌به‌گام با مثال کارت Visa دیوید (4003600000000014) شرح می‌دهد. خواندن دقیق همان بخش بخشی از مسئله است.

برنامه در `credit.c` (پوشهٔ `credit`) شماره را با `get_long` می‌گیرد و در خط آخر خروجی یکی از `AMEX\n`، `MASTERCARD\n`، `VISA\n` یا `INVALID\n` را چاپ می‌کند.

## خواسته‌های رسمی

1. فایل `credit.c` در پوشهٔ `credit`
2. شماره را بگیرد و نوع کارت معتبر را گزارش کند.
3. خط آخر خروجی یکی از AMEX، MASTERCARD، VISA یا INVALID با `\n` باشد.
4. ورودی کاملاً عددی و بدون صفر ابتدایی فرض می‌شود؛ get_long را به کار ببر.

## شروع کار

پوشهٔ `credit` را بساز، واردش شو و `code credit.c` را اجرا کن.

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: کارت معتبر:

```text
$ ./credit
Number: 4003600000000014
VISA
```

نمونهٔ رسمی: get_long خط تیره و حروف را رد می‌کند:

```text
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

نمونهٔ رسمی: عدد نامعتبر:

```text
$ ./credit
Number: 6176292929
INVALID
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- انواع داده در C — [یادداشت](/kb/d/w01-n10) · درس کوتاه `w01-l05` (واحد `w01-l05-u01`)
- اندازهٔ انواع (بایت) و بازه — [یادداشت](/kb/d/w01-sh-data-types) · درس کوتاه `w01-l05` (واحد `w01-l05-u02`)
- کتابخانهٔ CS50 و توابع get_* — [یادداشت](/kb/d/w01-n06) · درس کوتاه `w01-l03` (واحد `w01-l03-u02`)
- عملگرهای حسابی و باقی‌مانده % — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u01`)
- حلقهٔ while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u01`)
- عملگرهای منطقی && || ! — [یادداشت](/kb/d/w01-n14) · درس کوتاه `w01-l08` (واحد `w01-l08-u02`)
- زنجیرهٔ else if و شاخه‌های ناسازگار — [یادداشت](/kb/d/w01-n09) · درس کوتاه `w01-l07` (واحد `w01-l07-u02`)
- تعریف تابع — [یادداشت](/kb/d/w01-n16) · درس کوتاه `w01-l10` (واحد `w01-l10-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. چرا int برای شمارهٔ کارت کافی نیست؟ یادداشت سرریز را ببین.
2. با `%` و `/` می‌توان رقم آخر یک عدد را جدا کرد و آن را از عدد حذف کرد. روی کاغذ با عدد 1234 امتحان کن.
3. مسئله را بشکن: شمردن رقم‌ها، دو رقم اول، و بررسی Luhn. هر کدام را جداگانه آزمایش کن.

## اشتباه‌های رایج

- نگه‌داشتن شماره در int
- جمع‌کردن خود حاصل‌ضرب‌ها به‌جای رقم‌هایشان
- چاپ متن اضافه در خط آخر
- شروع شمارش «یکی در میان» از رقم اشتباه

## چک‌لیست خودآزمایی

1. مثال رسمی 4003600000000014 را با دست و الگوریتم Luhn بررسی کرده‌ام.
2. برای هر سه نوع کارت با شماره‌های آزمایشی PayPal امتحان کرده‌ام.
3. طول نادرست یا پیشوند نادرست INVALID می‌دهد.
4. شماره‌ای که از Luhn رد می‌شود INVALID می‌دهد.
5. خط آخر خروجی فقط یکی از چهار کلمهٔ مجاز است.
6. check50 و style50 را اجرا کرده‌ام.
7. با submit50 تحویل داده‌ام (یا Cash را).

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/credit
```

سبک با style50:

```bash
style50 credit.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/credit
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [شماره‌های آزمایشی PayPal](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards): پیوند رسمی صفحهٔ Credit برای آزمون.
- [مثال گام‌به‌گام Luhn با رقم‌های زیرخط‌دار](https://cs50.harvard.edu/x/psets/1/credit/#luhns-algorithm): زیرخط‌ها در استخراج متن از بین رفته‌اند؛ مثال را در صفحهٔ رسمی ببین.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام](https://youtu.be/dF7wNjsRBjI)

## پیوند رسمی

- [Credit](https://cs50.harvard.edu/x/psets/1/credit/)
- [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
