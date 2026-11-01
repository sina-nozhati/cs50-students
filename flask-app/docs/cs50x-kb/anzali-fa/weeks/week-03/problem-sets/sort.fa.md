---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-ps-sort
type: problem-set-guide
title: راهنمای تشخیص الگوریتم مرتب‌سازی (Sort)
title_fa: تشخیص الگوریتم مرتب‌سازی (Sort)
title_en: Sort
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/3/sort/
source_refs:
- src-pset-3-sort#problem-to-solve
- src-pset-3-sort#distribution-code
- src-anzali-authored-3
- src-pset-3#what-to-do
concept_ids:
- w03-c-selection-sort
- w03-c-bubble-sort
- w03-c-merge-sort
- w03-c-big-o
- w03-c-omega
- w03-c-early-exit-no-swaps
- w03-c-time-command
problem_set_ref: weeks/week-03/problem-sets/sort.json
prev: w03-sh-merge-sort
next: w03-ps-plurality
order: 28
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای تشخیص الگوریتم مرتب‌سازی (Sort)

> **منبع رسمی:** [Sort](https://cs50.harvard.edu/x/2026/psets/3/sort/) از پرابلم‌ست ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

در سخنرانی سه الگوریتم مرتب‌سازی دیدیم: انتخابی، حبابی و ادغامی. در این مسئله سه برنامهٔ **از پیش کامپایل‌شده** به نام‌های `sort1`، `sort2` و `sort3` داری؛ هر کدام یکی از این سه الگوریتم را پیاده می‌کند، ولی نه لزوماً به همین ترتیب.

کار تو تحلیل است، نه نوشتن کد: باید با اجرای برنامه‌ها روی فایل‌های ورودی تشخیص بدهی کدام برنامه کدام الگوریتم است و پاسخ‌ها را همراه با توضیح در `answers.txt` (پوشهٔ `sort`) به‌جای `TODO`ها بنویسی.

## خواسته‌های رسمی

1. پاسخ‌ها در فایل `answers.txt` در پوشهٔ `sort` نوشته شوند.
2. برای هر برنامه، الگوریتمش را همراه با یک توضیح به‌جای `TODO` بنویس.
3. هر یک از `sort1`، `sort2` و `sort3` یکی از انتخابی، حبابی یا ادغامی است، نه لزوماً به همین ترتیب.

## شروع کار

در ترمینال cs50.dev اول `cd` را تنها اجرا کن، بعد فایل‌های آغازین را دانلود و باز کن. این مسئله کد C ندارد که بنویسی؛ فقط `answers.txt` را پر می‌کنی، برای همین style50 هم ندارد.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/3/sort.zip
unzip sort.zip
rm sort.zip
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- مرتب‌سازی انتخابی — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u01`)
- مرتب‌سازی حبابی — [یادداشت](/kb/d/w03-n11) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)
- مرتب‌سازی ادغامی — [یادداشت](/kb/d/w03-n14) · درس کوتاه `w03-l07` (واحد `w03-l07-u01`)
- نماد O بزرگ: کران بالا یا بدترین حالت — [یادداشت](/kb/d/w03-n04) · درس کوتاه `w03-l02` (واحد `w03-l02-u01`)
- نماد Ω: کران پایین یا بهترین حالت — [یادداشت](/kb/d/w03-n05) · درس کوتاه `w03-l02` (واحد `w03-l02-u02`)
- توقف زودهنگام وقتی جابه‌جایی رخ نداد — [یادداشت](/kb/d/w03-n11) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)
- سنجیدن زمان اجرا با time — [یادداشت](/kb/d/w03-n04)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. پیش از اجرا، برای هر الگوریتم پیش‌بینی کن: روی ورودی از قبل مرتب چه می‌کند؟ روی ورودی برعکس؟ جدول O و Ω یادداشت‌های ۱۰، ۱۱ و ۱۴ را کنار دستت بگذار.
2. صفحهٔ رسمی پیشنهاد می‌کند هر برنامه را با `time` اجرا کنی. یک ورودی بزرگ انتخاب کن تا اختلاف‌ها به چشم بیاید.
3. کدام الگوریتم «بهترین حالت» متفاوتی با «بدترین حالت» دارد؟ چه ورودی‌ای آن تفاوت را نشان می‌دهد؟
4. اگر دو برنامه روی یک نوع ورودی شبیه هم‌اند، نوع دیگری از ورودی را امتحان کن تا از هم جدا شوند.
5. توضیحت را بر اساس شاهد بنویس: «روی فلان فایل، زمان فلان بود، که با O یا Ω فلان الگوریتم جور است.»

## اشتباه‌های رایج

- قضاوت از روی یک اجرای تنها؛ زمان‌ها کمی نوسان دارند
- استفاده از ورودی‌های خیلی کوچک که اختلاف را نشان نمی‌دهند
- فراموش کردن `cd` به پوشهٔ `sort` پیش از اجرای `./sort1`
- نوشتن فقط نام الگوریتم بدون توضیح

## چک‌لیست خودآزمایی

1. هر سه برنامه را روی فایل‌های مرتب، برعکس و تصادفی اجرا کرده‌ام.
2. برای سنجش از `time` استفاده کرده‌ام و به زمان `real` نگاه کرده‌ام.
3. سه الگوریتم متفاوت به سه برنامه نسبت داده‌ام.
4. برای هر برنامه یک توضیح نوشته‌ام، نه فقط نام الگوریتم.
5. فایل `answers.txt` در پوشهٔ `sort` است.
6. check50 همه را سبز نشان می‌دهد.
7. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/sort
```

این مسئله کد C برای نوشتن ندارد، پس صفحهٔ رسمی style50 نمی‌خواهد.

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/sort
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [ویدئوی راهنمای گام‌به‌گام](https://video.cs50.io/-Bhxxw6JKKY): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/-Bhxxw6JKKY)

## پیوند رسمی

- [Sort](https://cs50.harvard.edu/x/2026/psets/3/sort/)
- [پرابلم‌ست ۳](https://cs50.harvard.edu/x/psets/3/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
