---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-ps-mario-less
type: problem-set-guide
title: راهنمای ماریو (نسخهٔ آسان‌تر)
title_fa: ماریو (نسخهٔ آسان‌تر)
title_en: Mario (Feeling Less Comfortable)
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/psets/1/mario/less/
source_refs:
- src-pset-1-mario-less#problem-to-solve
- src-anzali-authored-1
- src-pset-1#what-to-do
concept_ids:
- w01-c-get-int
- w01-c-do-while
- w01-c-input-validation
- w01-c-nested-loops
- w01-c-for-loop
- w01-c-helper-function
- w01-c-escape-sequence
problem_set_ref: weeks/week-01/problem-sets/mario-less.json
prev: w01-ps-me
next: w01-ps-mario-more
order: 30
submission: one-of-mario
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای ماریو (نسخهٔ آسان‌تر)

> **منبع رسمی:** [Mario (Feeling Less Comfortable)](https://cs50.harvard.edu/x/psets/1/mario/less/) از پرابلم‌ست ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از دو نسخهٔ Mario را تحویل بده (اگر هر دو، نمرهٔ بالاتر حساب می‌شود). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

در پایان مرحلهٔ ۱-۱ بازی Super Mario Bros.، ماریو باید از یک هرم **راست‌چین** بالا برود. برنامه‌ای در `mario.c` (پوشهٔ `mario-less`) بنویس که این هرم را با `#` بسازد.

ارتفاع هرم را از کاربر با یک `int` بگیر. اگر ورودی بزرگ‌تر از ۰ نبود یا اصلاً عدد صحیح نبود، دوباره و دوباره بپرس.

## خواسته‌های رسمی

1. فایل `mario.c` در پوشهٔ `mario-less`
2. هرم راست‌چین از `#`
3. ارتفاع را با `int` از کاربر بگیرد.
4. اگر ورودی بزرگ‌تر از ۰ نبود یا int نبود، دوباره بپرسد.

> **ناهمخوانی رسمی:** ویدئوی walkthrough از بازهٔ ۱ تا ۸ حرف می‌زند، ولی صفحهٔ رسمی می‌گوید مشخصات فقط درخواست دوباره برای ورودی کمتر از ۱ را لازم دارد. ملاک، متن صفحه و check50 است.

## شروع کار

پوشهٔ `mario-less` را بساز، واردش شو و `code mario.c` را اجرا کن (همان الگوی World و Me).

## نمونه‌های رسمی ورودی و خروجی

هرم رسمی با ارتفاع ۸:

```text
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

هرم رسمی با ارتفاع ۳:

```text
  #
 ##
###
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- get_int — [یادداشت](/kb/d/w01-n13) · درس کوتاه `w01-l07` (واحد `w01-l07-u03`)
- حلقهٔ do while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- اعتبارسنجی ورودی و درخواست دوباره — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- حلقه‌های تودرتو — [یادداشت](/kb/d/w01-n18) · درس کوتاه `w01-l11` (واحد `w01-l11-u02`)
- حلقهٔ for — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u02`)
- تابع کمکی برای زیرمسئله — [یادداشت](/kb/d/w01-n18) · درس کوتاه `w01-l11` (واحد `w01-l11-u04`)
- دنبالهٔ گریز — [یادداشت](/kb/d/w01-n05) · درس کوتاه `w01-l02` (واحد `w01-l02-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. مسئله در واقع دو زیرمسئله است: گرفتن ارتفاع و چاپ هرم. اول برای هر کدام توضیح (شبه‌کد) بنویس.
2. برای «بپرس تا معتبر شود» کدام حلقه دست‌کم یک بار اجرا می‌شود؟
3. هرم را روی کاغذ برای ارتفاع ۳ بکش و در هر ردیف دو چیز را بشمار: چند نویسه پیش از اولین `#` و چند `#`.
4. رابطهٔ این دو عدد با شمارهٔ ردیف و ارتفاع را پیدا کن. اول یک هرم چپ‌چین بساز، بعد راست‌چینش کن.

## اشتباه‌های رایج

- چاپ فاصله‌های اضافه در انتهای ردیف
- هرم چپ‌چین به‌جای راست‌چین
- استفاده از if به‌جای حلقه برای ورودی نامعتبر
- یک ردیف کم یا زیاد به‌خاطر شمارش از ۰ یا ۱

## چک‌لیست خودآزمایی

1. برای ورودی -1 و 0 دوباره پرسیده می‌شود.
2. برای ورودی غیرعددی (مثل حروف) و ورودی خالی دوباره پرسیده می‌شود.
3. برای 1 تا 8 هرم درست چاپ می‌شود.
4. هرم راست‌چین است: لبهٔ راست ردیف‌ها زیر هم است.
5. هیچ فاصلهٔ اضافه‌ای بعد از آخرین `#` هر ردیف نیست.
6. هر ردیف با `\n` تمام می‌شود.
7. check50 و style50 را اجرا کرده‌ام.
8. با submit50 تحویل داده‌ام (یا نسخهٔ more را).

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/mario/less
```

سبک با style50:

```bash
style50 mario.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/mario/less
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [بخش «Advice» صفحهٔ رسمی (گام‌های کد تا تابع print_row)](https://cs50.harvard.edu/x/psets/1/mario/less/#advice): این بخش تقریباً کل راه‌حل را مرحله‌به‌مرحله نشان می‌دهد؛ طبق سیاست «بدون راه‌حل» در این بسته بازتولید نشده است. اگر پس از تلاش جدی گیر کردی، از آنجا کمک بگیر.
- [ویدئوی walkthrough](https://www.youtube.com/watch?v=NAs4FIWkJ4s): توضیح مسئله؛ دربارهٔ بازهٔ ۱ تا ۸ تفاوتی با متن دارد (پایین را ببین).
- [کد mario.c جلسهٔ حل تمرین](https://cdn.cs50.net/2025/fall/sections/1/src1/): هرم چپ‌چین کامل؛ بسیار نزدیک به راه‌حل.

## ویدئو و نمایش

- [ویدئوی معرفی](https://youtu.be/cWOkHQXw0JQ)
- [راهنمای گام‌به‌گام](https://youtu.be/NAs4FIWkJ4s)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/WPrv7PFVLaLkJ2BU96uTEQKuA)

## پیوند رسمی

- [Mario (Feeling Less Comfortable)](https://cs50.harvard.edu/x/psets/1/mario/less/)
- [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
