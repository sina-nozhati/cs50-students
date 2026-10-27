---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-ps-mario-more
type: problem-set-guide
title: راهنمای ماریو (نسخهٔ چالشی‌تر)
title_fa: ماریو (نسخهٔ چالشی‌تر)
title_en: Mario (Feeling More Comfortable)
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/psets/1/mario/more/
source_refs:
- src-pset-1-mario-more#problem-to-solve
- src-anzali-authored-1
- src-pset-1#what-to-do
concept_ids:
- w01-c-get-int
- w01-c-do-while
- w01-c-input-validation
- w01-c-logical-operators
- w01-c-nested-loops
- w01-c-helper-function
problem_set_ref: weeks/week-01/problem-sets/mario-more.json
prev: w01-ps-mario-less
next: w01-ps-cash
order: 31
submission: one-of-mario
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای ماریو (نسخهٔ چالشی‌تر)

> **منبع رسمی:** [Mario (Feeling More Comfortable)](https://cs50.harvard.edu/x/psets/1/mario/more/) از پرابلم‌ست ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از دو نسخهٔ Mario را تحویل بده (اگر هر دو، نمرهٔ بالاتر حساب می‌شود). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

در آغاز مرحلهٔ ۱-۱، ماریو باید از روی **دو هرم کنار هم** بپرد. برنامه‌ای در `mario.c` (پوشهٔ `mario-more`) بنویس که این دو هرم را با `#` بسازد؛ بین دو هرم فاصلهٔ دوتایی است.

ارتفاع را از کاربر بپرس: یک `int` مثبت بین ۱ تا ۸ (با خود ۱ و ۸).

## خواسته‌های رسمی

1. فایل `mario.c` در پوشهٔ `mario-more`
2. دو هرم کنار هم از `#`
3. ارتفاع: int مثبت بین ۱ و ۸، با خود ۱ و ۸

## شروع کار

پوشهٔ `mario-more` را بساز، واردش شو و `code mario.c` را اجرا کن.

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: ارتفاع ۸:

```text
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

نمونهٔ رسمی: ارتفاع ۴:

```text
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

نمونهٔ رسمی: ارتفاع ۲:

```text
$ ./mario
Height: 2
 #  #
##  ##
```

نمونهٔ رسمی: ارتفاع ۱:

```text
$ ./mario
Height: 1
#  #
```

نمونهٔ رسمی: ورودی‌های نامعتبر و درخواست دوباره:

```text
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- get_int — [یادداشت](/kb/d/w01-n13) · درس کوتاه `w01-l07` (واحد `w01-l07-u03`)
- حلقهٔ do while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- اعتبارسنجی ورودی و درخواست دوباره — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- عملگرهای منطقی && || ! — [یادداشت](/kb/d/w01-n14) · درس کوتاه `w01-l08` (واحد `w01-l08-u02`)
- حلقه‌های تودرتو — [یادداشت](/kb/d/w01-n18) · درس کوتاه `w01-l11` (واحد `w01-l11-u02`)
- تابع کمکی برای زیرمسئله — [یادداشت](/kb/d/w01-n18) · درس کوتاه `w01-l11` (واحد `w01-l11-u04`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. شرط «نامعتبر» دو طرف دارد: کمتر از ۱ یا بیشتر از ۸. کدام عملگر منطقی؟
2. هر ردیف را چهار تکه ببین و هر تکه را برای ارتفاع ۴ روی کاغذ بشمار.
3. یک تابع کمکی که «n بار یک نویسه» چاپ کند می‌تواند چند بار به کار برود.

## اشتباه‌های رایج

- فاصلهٔ اضافه بعد از هرم راست
- یک فاصله یا سه فاصله به‌جای دو فاصله
- پذیرفتن 9 یا 0

## چک‌لیست خودآزمایی

1. برای -1، 0، 9 و بالاتر دوباره پرسیده می‌شود.
2. برای حروف و ورودی خالی دوباره پرسیده می‌شود.
3. برای 1 تا 8 خروجی با نمونه‌های رسمی یکی است.
4. بین دو هرم دقیقاً دو فاصله است.
5. بعد از آخرین `#` هر ردیف فاصلهٔ اضافه نیست.
6. check50 و style50 را اجرا کرده‌ام.
7. با submit50 تحویل داده‌ام (یا نسخهٔ less را).

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/mario/more
```

سبک با style50:

```bash
style50 mario.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/mario/more
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [ویدئوی walkthrough](https://www.youtube.com/watch?v=FzN9RAjYG_Q): توضیح مسئله

## ویدئو و نمایش

- [ویدئوی معرفی](https://youtu.be/cWOkHQXw0JQ)
- [راهنمای گام‌به‌گام](https://youtu.be/FzN9RAjYG_Q)

## پیوند رسمی

- [Mario (Feeling More Comfortable)](https://cs50.harvard.edu/x/psets/1/mario/more/)
- [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
