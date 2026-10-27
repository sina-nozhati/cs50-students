---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-ps-me
type: problem-set-guide
title: راهنمای سلام، منم
title_fa: سلام، منم
title_en: Hello, It's Me
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/psets/1/me/
source_refs:
- src-pset-1-me#problem-to-solve
- src-anzali-authored-1
- src-pset-1#what-to-do
concept_ids:
- w01-c-cs50-library
- w01-c-get-string
- w01-c-variable-declaration
- w01-c-placeholder
- w01-c-printf
- w01-c-header-file
problem_set_ref: weeks/week-01/problem-sets/me.json
prev: w01-ps-world
next: w01-ps-mario-less
order: 29
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای سلام، منم

> **منبع رسمی:** [Hello, It's Me](https://cs50.harvard.edu/x/psets/1/me/) از پرابلم‌ست ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

برنامه‌ای در `hello.c` (پوشهٔ `me`) که نام کاربر را بپرسد و به او سلام کند؛ مثلاً اگر نام Adele باشد، `hello, Adele\n` چاپ شود.

این اولین مسئلهٔ تحویلی هفته است. ابزارهای لازم را در درس‌نامه دیده‌ای: گرفتن رشته از کاربر، ذخیره در متغیر و چاپ با جای‌نگهدار.

> **توجه:** برنامهٔ `hello.c` در یادداشت «سلام به تو» بسیار نزدیک به خواستهٔ این مسئله است. تفاوت‌ها کوچک‌اند ولی برای check50 مهم‌اند. پیشنهاد: آن یادداشت را ببند و برنامه را از حافظه بنویس.

## خواسته‌های رسمی

1. فایل `hello.c` در پوشهٔ `me`
2. نام کاربر را بپرسد.
3. به همان کاربر سلام کند، مثلاً `hello, Adele\n`.

## شروع کار

ابتدا `cd` را تنها اجرا کن.

فرمان‌های رسمی:

```bash
mkdir me
cd me
code hello.c
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- کتابخانهٔ CS50 و توابع get_* — [یادداشت](/kb/d/w01-n06) · درس کوتاه `w01-l03` (واحد `w01-l03-u02`)
- get_string و مقدار بازگشتی — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u02`)
- اعلان متغیر با نوع — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u03`)
- جای‌نگهدار %s — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u03`)
- تابع printf — [یادداشت](/kb/d/w01-n05) · درس کوتاه `w01-l02` (واحد `w01-l02-u01`)
- فایل سرآیند و #include — [یادداشت](/kb/d/w01-n06) · درس کوتاه `w01-l03` (واحد `w01-l03-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی سه یادآوری دارد: get_string در cs50.h، printf در stdio.h، و %s برای قالب‌بندی رشته.
2. اگر به‌جای نام، کلمهٔ نام متغیر چاپ شد، یادداشت «سلام به تو» را دوباره ببین.

## اشتباه‌های رایج

- نوشتن نام متغیر داخل نقل‌قول
- جاانداختن `#include <cs50.h>`
- `Hello` با H بزرگ به‌جای `hello`
- فاصله یا کامای اضافه یا جاافتاده

## چک‌لیست خودآزمایی

1. هر دو فایل سرآیند لازم را include کرده‌ام.
2. نام را در متغیری با نوع درست ذخیره کرده‌ام.
3. خروجی با حرف کوچک `hello, ` شروع می‌شود و با `\n` تمام می‌شود.
4. با چند نام مختلف (مثلاً یک کلمه‌ای و دوکلمه‌ای) امتحان کرده‌ام.
5. check50 همه را سبز نشان می‌دهد.
6. style50 تغییری پیشنهاد نمی‌کند.
7. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/me
```

سبک با style50:

```bash
style50 hello.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/me
```

## ویدئو و نمایش

- [ویدئوی معرفی](https://youtu.be/YQHsXMglC9A)
- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/wSk1KSDUEYA)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/Jn4egWrG0Rvuzo9d2Rs0qpkcL)

## پیوند رسمی

- [Hello, It's Me](https://cs50.harvard.edu/x/psets/1/me/)
- [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
