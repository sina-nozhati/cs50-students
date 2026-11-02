---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-ps-tideman
type: problem-set-guide
title: راهنمای روش تایدمن (Tideman)
title_fa: روش تایدمن (Tideman)
title_en: Tideman
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/3/tideman/
source_refs:
- src-pset-3-tideman#specification
- src-anzali-authored-3
- src-pset-3#what-to-do
concept_ids:
- w03-c-struct
- w03-c-array-of-structs
- w03-c-sorting
- w03-c-selection-sort
- w03-c-bubble-sort
- w03-c-merge-sort
- w03-c-recursion
- w03-c-base-case
problem_set_ref: weeks/week-03/problem-sets/tideman.json
prev: w03-ps-runoff
next: w03-pr-atoi
order: 31
submission: one-of-runoff-tideman
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای روش تایدمن (Tideman)

> **منبع رسمی:** [Tideman](https://cs50.harvard.edu/x/2026/psets/3/tideman/) از پرابلم‌ست ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از Runoff یا Tideman را تحویل بده (طبق صفحهٔ رسمی، اگر هر دو را تحویل بدهی نمرهٔ بالاتر ثبت می‌شود؛ Tideman اختیاری ولی چالش‌برانگیز است). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

روش **تایدمن** (Tideman، یا «ranked pairs») روشی ترجیحی است که اگر «برندهٔ کندورسه» وجود داشته باشد، تضمین می‌کند همان برنده شود؛ یعنی کسی که در هر رقابت تن‌به‌تن از همه می‌برد.

این روش از نامزدها یک **گراف** می‌سازد: یال از A به B یعنی A در رقابت تن‌به‌تن از B می‌برد. سه مرحله دارد: **شمارش** (Tally)، **مرتب‌سازی** جفت‌ها بر اساس قدرت پیروزی (Sort) و **قفل کردن** یال‌ها به ترتیب، به شرطی که دور (cycle) نسازند (Lock). برنده «منبع» گراف است. برنامه‌ات را در `tideman.c` (پوشهٔ `tideman`) کامل می‌کنی.

## خواسته‌های رسمی

1. فقط `vote`، `record_preferences`، `add_pairs`، `sort_pairs`، `lock_pairs` و `print_winner` را کامل کن؛ افزودن سرآیند و تابع کمکی مجاز است، تغییر اعلان‌ها نه.
2. `vote` اگر نام معتبر بود، `ranks` را به‌روز کند و `true` برگرداند؛ وگرنه `false`.
3. `record_preferences` آرایهٔ سراسری `preferences` را با ترجیح‌های هر رأی‌دهنده به‌روز کند.
4. `add_pairs` همهٔ جفت‌هایی را که یکی بر دیگری ترجیح دارد اضافه کند (جفت‌های مساوی نه) و `pair_count` را به‌روز کند.
5. `sort_pairs` جفت‌ها را به ترتیب نزولی قدرت پیروزی مرتب کند.
6. `lock_pairs` یال‌ها را به ترتیب نزولی قفل کند، به شرطی که دور نسازند.
7. `print_winner` نام منبع گراف را چاپ کند.

## شروع کار

فایل آغازین را با فرمان‌های رسمی دانلود کن و وارد پوشه شو. بخش «Understanding» صفحهٔ رسمی را با کد کنار هم بخوان: `preferences`، `locked` و struct `pair` هر کدام چه معنایی دارند؟

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/3/tideman.zip
unzip tideman.zip
rm tideman.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd tideman
ls
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- ساختار داده با typedef struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- آرایه‌ای از struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- مرتب‌سازی و چرا مرتب کردن ارزشمند است — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u01`)
- مرتب‌سازی انتخابی — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u01`)
- مرتب‌سازی حبابی — [یادداشت](/kb/d/w03-n11) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)
- مرتب‌سازی ادغامی — [یادداشت](/kb/d/w03-n14) · درس کوتاه `w03-l07` (واحد `w03-l07-u01`)
- بازگشت: تابعی که خودش را صدا می‌زند — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- حالت پایه — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. نمونه‌های بخش «Background» را روی کاغذ دوباره بساز: گراف اول منبع دارد، گراف دوم دور دارد. تا این دو را با دست نفهمیده‌ای، سراغ کد نرو.
2. برای `sort_pairs` هر الگوریتم مرتب‌سازی این هفته کار می‌کند؛ فقط کلید مقایسه «قدرت پیروزی» است. قدرت پیروزی را از کدام آرایه می‌خوانی؟
3. `lock_pairs` سخت‌ترین بخش است. سؤال کلیدی: «اگر این یال را اضافه کنم، آیا از سر دیگرش می‌شود با یال‌های قفل‌شده به همین‌جا برگشت؟» فکر کن چطور همین سؤال را برای مسیرهای چندیالی هم می‌پرسی، و کی می‌توانی با اطمینان بگویی «نه».
4. `locked[i][j]` یک ماتریس مجاورت است. منبع گراف یعنی نامزدی که هیچ یالی به سمتش نیست؛ این را چطور در ماتریس می‌خوانی؟
5. هر تابع را جدا بنویس و با check50 بسنج؛ check50 توابع را جداگانه آزمایش می‌کند.

## اشتباه‌های رایج

- اضافه کردن جفت‌های مساوی
- مرتب‌سازی صعودی به‌جای نزولی
- بررسی دور فقط برای یک گام به‌جای کل مسیر
- اشتباه گرفتن `preferences[i][j]` با `preferences[j][i]`
- تغییر دادن اعلان توابع

## چک‌لیست خودآزمایی

1. فقط شش تابع خواسته‌شده را تغییر داده‌ام و اعلان‌ها دست‌نخورده‌اند.
2. `vote` نام نامعتبر را رد می‌کند.
3. `preferences[i][j]` تعداد رأی‌دهندگانی است که i را بر j ترجیح می‌دهند.
4. جفت‌های مساوی اضافه نمی‌شوند و `pair_count` درست است.
5. جفت‌ها نزولی مرتب‌اند.
6. نمونهٔ دوری صفحهٔ رسمی (سنگ‌کاغذقیچی) را با دست دنبال کرده‌ام.
7. منبع گراف درست چاپ می‌شود.
8. check50 همه را سبز نشان می‌دهد.
9. style50 تغییری پیشنهاد نمی‌کند.
10. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/tideman
```

سبک با style50:

```bash
style50 tideman.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/tideman
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/embed/kb83NwyYI68): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/kb83NwyYI68)

## پیوند رسمی

- [Tideman](https://cs50.harvard.edu/x/2026/psets/3/tideman/)
- [پرابلم‌ست ۳](https://cs50.harvard.edu/x/psets/3/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
