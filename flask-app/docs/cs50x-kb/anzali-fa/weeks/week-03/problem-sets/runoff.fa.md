---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-ps-runoff
type: problem-set-guide
title: راهنمای انتخابات دومرحله‌ای فوری (Runoff)
title_fa: انتخابات دومرحله‌ای فوری (Runoff)
title_en: Runoff
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/3/runoff/
source_refs:
- src-pset-3-runoff#distribution-code
- src-pset-3-runoff#hints
- src-anzali-authored-3
- src-pset-3#what-to-do
concept_ids:
- w03-c-struct
- w03-c-array-of-structs
- w03-c-search-strings
- w03-c-linear-search
- w03-c-pseudocode-precision
problem_set_ref: weeks/week-03/problem-sets/runoff.json
prev: w03-ps-plurality
next: w03-ps-tideman
order: 30
submission: one-of-runoff-tideman
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای انتخابات دومرحله‌ای فوری (Runoff)

> **منبع رسمی:** [Runoff](https://cs50.harvard.edu/x/2026/psets/3/runoff/) از پرابلم‌ست ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از Runoff یا Tideman را تحویل بده (طبق صفحهٔ رسمی، اگر هر دو را تحویل بدهی نمرهٔ بالاتر ثبت می‌شود؛ Tideman اختیاری ولی چالش‌برانگیز است). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

رأی اکثریت نسبی ضعف دارد: ممکن است تساوی پیش بیاید یا برنده‌ای انتخاب شود که اکثر رأی‌دهنده‌ها او را نمی‌خواهند. در رأی‌گیری **ترجیحی** (ranked-choice) هر رأی‌دهنده نامزدها را به ترتیب ترجیح رتبه‌بندی می‌کند.

در روش **رقابت دوم فوری** (instant runoff)، اگر نامزدی بیش از ۵۰٪ ترجیح اول را داشت برنده است؛ وگرنه کم‌رأی‌ترین نامزد حذف می‌شود و رأی طرفدارانش به ترجیح بعدی‌شان می‌رسد، و این تکرار می‌شود. برنامه‌ات را در `runoff.c` (پوشهٔ `runoff`) کامل می‌کنی.

## خواسته‌های رسمی

1. فقط توابع `vote`، `tabulate`، `print_winner`، `find_min`، `is_tie` و `eliminate` را کامل کن (افزودن سرآیند مجاز است).
2. `vote` اگر نام معتبر بود، ترجیح را در آرایهٔ `preferences` ثبت کند و `true` برگرداند؛ وگرنه `false`.
3. `tabulate` رأی هر رأی‌دهنده را به بالاترین ترجیحِ حذف‌نشده‌اش بدهد.
4. `print_winner` اگر کسی بیش از نصف رأی‌ها را داشت نامش را چاپ کند و `true` برگرداند؛ وگرنه `false`.
5. `find_min` کمترین رأی میان نامزدهای باقی‌مانده را برگرداند.
6. `is_tie` اگر همهٔ باقی‌مانده‌ها رأی برابر داشتند `true` برگرداند.
7. `eliminate` نامزد یا نامزدهایی را که `min` رأی دارند حذف کند.

## شروع کار

فایل آغازین را با فرمان‌های رسمی دانلود کن و وارد پوشه شو. صفحهٔ رسمی `main` را مفصل توضیح می‌دهد؛ اول آن را با کد مقایسه کن تا بفهمی `preferences[i][j]` دقیقاً چه نگه می‌دارد.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/3/runoff.zip
unzip runoff.zip
rm runoff.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd runoff
ls
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- ساختار داده با typedef struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- آرایه‌ای از struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- جست‌وجو در آرایهٔ رشته‌ها با strcmp — [یادداشت](/kb/d/w03-n07) · درس کوتاه `w03-l03` (واحد `w03-l03-u02`)
- جست‌وجوی خطی — [یادداشت](/kb/d/w03-n02) · درس کوتاه `w03-l01` (واحد `w03-l01-u02`)
- دقیق‌تر کردن شبه‌کد: از «هر در» تا doors[i] — [یادداشت](/kb/d/w03-n02) · درس کوتاه `w03-l01` (واحد `w03-l01-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. قبل از کد، یک انتخابات کوچک (سه نامزد، پنج رأی‌دهنده) را روی کاغذ دور به دور اجرا کن. هر دور کدام تابع‌ها صدا زده می‌شوند؟
2. `preferences[i][j]` اندیس نامزد را نگه می‌دارد، نه نامش. در `vote` نام را به چه چیزی تبدیل می‌کنی؟
3. در `tabulate` برای هر رأی‌دهنده فقط یک رأی شمرده می‌شود. صفحهٔ رسمی یادآوری می‌کند کجا `break` به کار می‌آید.
4. «بیش از نصف» را با تقسیم صحیح چطور بیان می‌کنی؟ با تعداد رأی‌دهندهٔ زوج و فرد امتحان کن.
5. `is_tie` و `eliminate` هر دو `min` را می‌گیرند. فیلد `eliminated` در هر دو چه نقشی دارد؟
6. هر تابع را جدا آزمایش کن؛ check50 هم هر تابع را جدا می‌سنجد.

## اشتباه‌های رایج

- شمردن رأی برای نامزد حذف‌شده
- ادامه دادن روی برگهٔ رأی بعد از ثبت یک رأی
- استفاده از «نصف یا بیشتر» به‌جای «بیش از نصف»
- حساب کردن کمینه با نامزدهای حذف‌شده
- مقایسهٔ رشته‌ها با `==`

## چک‌لیست خودآزمایی

1. فقط شش تابع خواسته‌شده را تغییر داده‌ام.
2. رأی نامعتبر برنامه را با پیام خطا تمام می‌کند.
3. شمارش فقط به نامزدهای حذف‌نشده رأی می‌دهد.
4. برنده فقط با «بیش از نصف» اعلام می‌شود، نه «نصف».
5. کمینه فقط میان نامزدهای باقی‌مانده حساب می‌شود.
6. تساوی کامل باقی‌مانده‌ها کسی را حذف نمی‌کند.
7. check50 همه را سبز نشان می‌دهد.
8. style50 تغییری پیشنهاد نمی‌کند.
9. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/runoff
```

سبک با style50:

```bash
style50 runoff.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/runoff
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/embed/-Vc5aGywKxo): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/-Vc5aGywKxo)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/4rhSKgaZQsY93RLj0xgu7nwKB)

## پیوند رسمی

- [Runoff](https://cs50.harvard.edu/x/2026/psets/3/runoff/)
- [پرابلم‌ست ۳](https://cs50.harvard.edu/x/psets/3/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
