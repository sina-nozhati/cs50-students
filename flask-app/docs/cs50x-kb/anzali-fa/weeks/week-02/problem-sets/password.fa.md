---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-pr-password
type: practice-guide
title: راهنمای گذرواژه (Password)
title_fa: گذرواژه (Password)
title_en: Password
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/password/
source_refs:
- src-practice-password#background
- src-practice-password#getting-started
- src-anzali-authored-2
concept_ids:
- w02-c-string-char-array
- w02-c-strlen
- w02-c-ctype
- w02-c-function-anatomy
- w02-c-char-ascii
problem_set_ref: weeks/week-02/problem-sets/password.json
prev: w02-pr-no-vowels
next: null
order: 34
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای گذرواژه (Password)

> **منبع رسمی:** [Password](https://cs50.harvard.edu/x/2026/practice/password/) از مسئله‌های تمرینی هفتهٔ ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

بسیاری از وب‌سایت‌ها گذرواژه‌ای می‌خواهند که فقط حرف نباشد و رقم و نماد هم داشته باشد. در این تمرین برنامه گذرواژه را می‌پرسد و تابعی که تو کامل می‌کنی آن را بررسی می‌کند.

اگر گذرواژه دست‌کم یک حرف بزرگ، یک حرف کوچک، یک رقم و یک نماد داشته باشد، تابع `true` برمی‌گرداند و در غیر این صورت `false`.

## خواسته‌های رسمی

1. دست‌کم یک حرف بزرگ، یک حرف کوچک، یک رقم و یک نماد ← true؛ وگرنه false.
2. تابع `valid` را کامل کن.

> **توجه:** صفحهٔ رسمی یک جا تابع را `check` و جای دیگر `valid` می‌نامد (ناهمخوانی d26). نام درست را از کد آغازین بخوان.

## شروع کار

ابتدا `cd`، بعد `mkdir password` و `cd password`.

فایل آغازین رسمی را دانلود کن:

```bash
wget https://cdn.cs50.net/2022/fall/labs/2/password.c
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: فقط حروف کوچک:

```text
password/ $ ./password
Enter your password: hello
Your password needs at least one uppercase letter, lowercase letter, number and symbol!
```

نمونهٔ رسمی: بدون حرف بزرگ:

```text
password/ $ ./password
Enter your password: h3ll(
Your password needs at least one uppercase letter, lowercase letter, number and symbol!
```

نمونهٔ رسمی: معتبر:

```text
password/ $ ./password
Enter your password: h3LL0!
Your password is valid!
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- رشته، آرایه‌ای از char — [یادداشت](/kb/d/w02-n12) · درس کوتاه `w02-l06` (واحد `w02-l06-u02`)
- strlen و string.h — [یادداشت](/kb/d/w02-n14) · درس کوتاه `w02-l07` (واحد `w02-l07-u02`)
- کتابخانهٔ ctype.h: islower و toupper — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u04`)
- اجزای اعلان تابع: نوع بازگشتی، نام، فهرست آرگومان‌ها — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)
- نویسه‌ها عددند: کدهای ASCII — [یادداشت](/kb/d/w02-n11) · درس کوتاه `w02-l06` (واحد `w02-l06-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی پیشنهاد می‌کند برای هر شرط یک متغیر bool داشته باشی که با false شروع شود.
2. کتابخانهٔ ctype.h توابع زیادی دارد که اینجا به کار می‌آیند؛ manual.cs50.io را ببین.

## اشتباه‌های رایج

- برگرداندن true به محض دیدن اولین شرط
- فراموش کردن نمادها
- استفاده از نام تابع متفاوت با کد آغازین

## چک‌لیست خودآزمایی

1. هر چهار شرط را جداگانه امتحان کرده‌ام.
2. نام تابع را با کد آغازین مطابقت داده‌ام (ناهمخوانی d26).
3. نمونه‌های رسمی همان خروجی را می‌دهند.
4. check50 همه را سبز نشان می‌دهد.
5. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/password
```

سبک با style50:

```bash
style50 password.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: با ۹۵ نویسهٔ چاپی ASCII، چند گذرواژهٔ ۸نویسه‌ای مختلف می‌توان ساخت؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد آغازین password.c](https://cdn.cs50.net/2022/fall/labs/2/password.c): با wget دانلود کن.
- [کلیپ Spaceballs](https://www.youtube.com/watch?v=B-NhD15ocwA): ویدئوی طنز صفحهٔ رسمی؛ برای حل لازم نیست.

## ویدئو و نمایش

- [کلیپ طنز دربارهٔ گذرواژه (برای حل لازم نیست)](https://youtu.be/B-NhD15ocwA)

## پیوند رسمی

- [Password](https://cs50.harvard.edu/x/2026/practice/password/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
