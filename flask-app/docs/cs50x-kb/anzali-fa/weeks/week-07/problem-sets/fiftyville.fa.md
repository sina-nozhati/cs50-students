---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-ps-fiftyville
type: problem-set-guide
title: راهنمای معمای Fiftyville
title_fa: معمای Fiftyville
title_en: Fiftyville
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/7/fiftyville/
source_refs:
- src-pset-7-fiftyville#problem-to-solve
- src-pset-7-fiftyville#specification
- src-anzali-authored-7
- src-pset-7#what-to-do
- src-pset-7#when-to-do-it
concept_ids:
- w07-c-sqlite3-cli
- w07-c-schema
- w07-c-select
- w07-c-where
- w07-c-and-or
- w07-c-like-wildcard
- w07-c-nested-query
- w07-c-join
- w07-c-multi-join
- w07-c-qualified-column
- w07-c-sql-comment
- w07-c-query-log
- w07-c-sql-style
- w07-c-no-id-assumption
problem_set_ref: weeks/week-07/problem-sets/fiftyville.json
prev: w07-ps-movies
next: w07-pr-favorites
order: 21
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای معمای Fiftyville

> **منبع رسمی:** [Fiftyville](https://cs50.harvard.edu/x/2026/psets/7/fiftyville/) از پرابلم‌ست ۷ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

اردک CS50 دزدیده شده است! شهر Fiftyville از تو کمک خواسته است. مقام‌ها فکر می‌کنند دزد اردک را دزدیده و کمی بعد با کمک یک همدست با هواپیما از شهر رفته است. باید سه چیز را پیدا کنی: دزد کیست، به کدام شهر فرار کرده و همدستش کیست.

تنها چیزی که می‌دانی این است که دزدی **در ۲۸ ژوئیهٔ ۲۰۲۵** و **در خیابان Humphrey** رخ داده است. مقام‌های شهر بخشی از سوابق شهر را در پایگاه دادهٔ SQLite به نام `fiftyville.db` گذاشته‌اند و تو فقط با پرس‌وجوهای `SELECT` و فقط با اطلاعات همین پایگاه داده معما را حل می‌کنی.

صفحهٔ رسمی می‌گوید **فرایند حل** به اندازهٔ خود پاسخ مهم است: هر پرس‌وجویی را که اجرا می‌کنی در `log.sql` با توضیح `--` ثبت می‌کنی. این راهنما هیچ پرس‌وجو، داده یا پاسخی از این معما ندارد و فقط شیوهٔ کار را نشان می‌دهد (D58).

> **از سخنرانی:** `.schema`، `SELECT`، `WHERE` و `LIKE` در [یادداشت SELECT](/kb/d/w07-n03)؛ پرس‌وجوی تودرتو در [یادداشت IMDb](/kb/d/w07-n07)؛ `JOIN` در [یادداشت JOINها](/kb/d/w07-n08)؛ توضیح با `--` در [یادداشت تزریق SQL](/kb/d/w07-n12).

## خواسته‌های رسمی

1. دزد، شهری که به آن فرار کرده و همدستی که کمکش کرده را پیدا کن.
2. فقط از اطلاعات پایگاه داده و پرس‌وجوهای `SELECT` استفاده کن.
3. در `log.sql` همهٔ پرس‌وجوهایی را که روی پایگاه داده اجرا می‌کنی ثبت کن.
4. بالای هر پرس‌وجو با توضیح `--` بنویس چرا آن را اجرا می‌کنی یا چه اطلاعاتی از آن می‌خواهی؛ یادداشت‌های فکری‌ات را هم می‌توانی بیفزایی.
5. برای خوانایی پرس‌وجوهای پیچیده، اصول سبک sqlstyle.guide (به‌ویژه تورفتگی) را رعایت کن.
6. پس از حل معما، هر سطر `answers.txt` را با نام دزد، شهر و نام همدست کامل کن، بدون تغییر متن موجود یا افزودن سطر.
7. هر دو فایل `log.sql` و `answers.txt` را تحویل بده.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. پس از `ls` سه فایل می‌بینی: `answers.txt`، `fiftyville.db` و `log.sql`.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/7/fiftyville.zip
unzip fiftyville.zip
rm fiftyville.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd fiftyville
```

## نمونه‌های رسمی ورودی و خروجی

فایل‌ها پس از `ls`:

```text
answers.txt  fiftyville.db  log.sql
```

## راهنمایی‌های رسمی

> **رسمی:** بازنویسی فارسی بخش Hints صفحهٔ رسمی.

- برای شروع، `sqlite3 fiftyville.db` را اجرا کن.
- در `sqlite3`، فرمان `.tables` همهٔ جدول‌های پایگاه داده را فهرست می‌کند.
- در `sqlite3`، فرمان `.schema TABLE_NAME` (به جای `TABLE_NAME` نام یک جدول) دستور `CREATE TABLE` آن جدول را نشان می‌دهد تا بدانی کدام ستون‌ها را پرس‌وجو کنی.
- شاید شروع از جدول `crime_scene_reports` کمک کند: دنبال گزارشی بگرد که با تاریخ و محل جرم بخواند.
- برای نحو SQL، [مرجع کلیدواژه‌های SQL در w3schools](https://www.w3schools.com/sql/sql_ref_keywords.asp) را ببین.

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- sqlite3: برنامهٔ خط فرمان SQLite — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- طرح‌واره (schema) و .schema / CREATE TABLE — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- SELECT ... FROM ...: خواندن ستون‌ها از جدول — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- WHERE: فیلتر سطرها با عبارت بولی — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- ترکیب شرط‌ها با AND و OR — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- LIKE و % برای الگو — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- پرس‌وجوی تودرتو با IN (SELECT ...) — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u03`)
- JOIN ... ON: ترکیب دو جدول با کلید مشترک — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u01`)
- JOIN سه جدول: shows، stars، people — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u02`)
- نام کامل ستون: table.column — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u01`)
- توضیح در SQL با -- — [یادداشت](/kb/d/w07-n12) · درس کوتاه `w07-l07` (واحد `w07-l07-u03`)
- لاگ پرس‌وجو با توضیح -- در log.sql — [یادداشت](/kb/d/w07-ps-fiftyville)
- سبک SQL: کلیدواژه‌های بزرگ، تورفتگی (sqlstyle.guide) — [یادداشت](/kb/d/w07-sec) · درس کوتاه `w07-l05` (واحد `w07-l05-u04`)
- فرض نکردن id ثابت؛ پیدا کردن id با پرس‌وجو — [یادداشت](/kb/d/w07-ps-songs)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. پیش از هر پرس‌وجو، طرح‌وارهٔ همهٔ جدول‌ها را بخوان و برای خودت بنویس هر جدول چه چیزی را ثبت می‌کند و کدام ستون‌ها به جدول‌های دیگر وصل می‌شوند.
2. لاگ را مثل دفترچهٔ کارآگاه بنویس: پیش از هر پرس‌وجو در یک خط `--` بنویس دنبال چه هستی، و بعد از آن نتیجهٔ مهم را هم در یک خط `--` خلاصه کن.
3. هر یافته (یک زمان، یک مکان، یک شناسه) سرنخی برای پرس‌وجوی بعدی است. به جای کپی کردن دستی مقدارها، از پرس‌وجوی تودرتو یا `JOIN` استفاده کن تا اشتباه تایپی نکنی.
4. وقتی چند نامزد داری، هر سرنخ تازه را مثل یک شرط اضافه ببین که فهرست را کوتاه‌تر می‌کند. نتیجه را فقط وقتی قطعی بدان که همهٔ سرنخ‌ها با آن بخوانند.
5. با `LIKE` و `%` می‌توانی متن‌های طولانی را برای یک واژه جست‌وجو کنی، ولی یادت باشد `=` برای متن دقیق است.

## اشتباه‌های رایج

- اجرای پرس‌وجو در اعلان و ثبت نکردن آن در `log.sql`
- نوشتن پرس‌وجو بدون توضیح `--`
- حدس زدن پاسخ پیش از آن‌که همهٔ سرنخ‌ها با آن بخوانند
- کپی دستی شناسه‌ها و تاریخ‌ها و خطای تایپی
- تغییر متن موجود در `answers.txt` یا افزودن سطر به آن

## چک‌لیست خودآزمایی

1. هر پرس‌وجویی که روی پایگاه داده اجرا کرده‌ام در `log.sql` هست.
2. بالای هر پرس‌وجو توضیح `--` دارد که چرا اجرایش کرده‌ام.
3. هر نتیجه‌گیری‌ام به نتیجهٔ یک پرس‌وجوی ثبت‌شده برمی‌گردد، نه به حدس.
4. پرس‌وجوهای طولانی را با تورفتگی خوانا نوشته‌ام.
5. در `answers.txt` فقط جای خالی سه سطر را پر کرده‌ام و متن موجود را تغییر نداده‌ام.
6. check50 همه را سبز نشان می‌دهد.
7. `log.sql` و `answers.txt` را با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/fiftyville
```

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/fiftyville
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/watch?v=YHhgEoJMDnU): ویدئوی رسمی؛ فقط پیوند.
- [sqlstyle.guide (بخش تورفتگی)](https://www.sqlstyle.guide/#indentation): راهنمای سبک پیشنهادی صفحهٔ رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/YHhgEoJMDnU)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/YgI5fyTP939jINCZm7l3o7WCY)

## پیوند رسمی

- [Fiftyville](https://cs50.harvard.edu/x/2026/psets/7/fiftyville/)
- [پرابلم‌ست ۷](https://cs50.harvard.edu/x/psets/7/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
