---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-sh-sql
type: short-summary
title: 'ویدئوی کوتاه: SQL (SQL)'
title_fa: SQL
title_en: SQL
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/sql/
source_refs:
- src-short-sql
- src-sqlite-docs
- src-anzali-inference-7
concept_ids:
- w07-c-relational-db
- w07-c-sql-language
- w07-c-mysql-vs-sqlite
- w07-c-sqlite-types
- w07-c-primary-key
- w07-c-autoincrement
- w07-c-crud
- w07-c-insert
- w07-c-select
- w07-c-select-star
- w07-c-where
- w07-c-order-by
- w07-c-join
- w07-c-qualified-column
- w07-c-update
- w07-c-delete
prev: w07-sec
next: w07-ps-songs
order: 18
video:
  youtube_id: AywtnUjQ6X4
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: پایگاه داده در وب'
    evidence_en: null
  - start: 0:47
    start_seconds: 47
    title_fa: تشبیه صفحه‌گسترده
    evidence_en: Microsoft Excel
  - start: '2:24'
    start_seconds: 144
    title_fa: SQL، MySQL و SQLite
    evidence_en: Structured Query Language
  - start: '3:15'
    start_seconds: 195
    title_fa: phpMyAdmin
    evidence_en: phpMyAdmin
  - start: '4:37'
    start_seconds: 277
    title_fa: نوع‌های داده
    evidence_en: data types
  - start: '6:29'
    start_seconds: 389
    title_fa: CHAR و VARCHAR
    evidence_en: char and varchar
  - start: '8:19'
    start_seconds: 499
    title_fa: وابستگی نوع در SQLite
    evidence_en: type affinity
  - start: '8:58'
    start_seconds: 538
    title_fa: کلید اصلی
    evidence_en: primary key
  - start: '9:30'
    start_seconds: 570
    title_fa: کلید اصلی ترکیبی
    evidence_en: joint primary key
  - start: '10:44'
    start_seconds: 644
    title_fa: جدول‌های نمونهٔ users و moms
    evidence_en: users and moms
  - start: '11:29'
    start_seconds: 689
    title_fa: INSERT
    evidence_en: INSERT INTO table
  - start: '12:49'
    start_seconds: 769
    title_fa: autoincrement
    evidence_en: autoincrement
  - start: '14:13'
    start_seconds: 853
    title_fa: SELECT
    evidence_en: second operation, which is select
  - start: '16:05'
    start_seconds: 965
    title_fa: SELECT *
    evidence_en: SELECT *
  - start: '17:49'
    start_seconds: 1069
    title_fa: JOIN
    evidence_en: select join query
  - start: '19:54'
    start_seconds: 1194
    title_fa: تشبیه نمودار ون
    evidence_en: Venn diagram
  - start: '21:06'
    start_seconds: 1266
    title_fa: UPDATE
    evidence_en: UPDATE table SET
  - start: '21:42'
    start_seconds: 1302
    title_fa: DELETE
    evidence_en: DELETE from
  - start: '22:16'
    start_seconds: 1336
    title_fa: خودکارسازی با زبان برنامه‌نویسی
    evidence_en: manual intervention
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: SQL (SQL)

> **منبع رسمی:** [صفحهٔ Short «SQL» در CS50x](https://cs50.harvard.edu/x/shorts/sql/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو با کاربرد پایگاه داده در وب‌سایت‌ها شروع می‌شود: نگه داشتن نام کاربری و گذرواژه برای ورود، یا تاریخچهٔ خرید. بعد تشبیه آشنایی می‌آورد: یک فایل Excel یا Google Sheets (کتاب کار) همان **پایگاه داده** است، هر برگه یک **جدول** است و هر جدول **سطر** و **ستون** دارد.

SQL (Structured Query Language) زبانی است که تنها کارش پرسیدن از پایگاه داده و گرفتن داده از آن است. ویدئو دو پیاده‌سازی را نام می‌برد: MySQL که متن‌باز و رایج است، و **SQLite** که امکاناتی شبیه دارد ولی سبک‌تر است و CS50 از ۲۰۱۶ آن را به کار می‌برد. ابزار گرافیکی phpMyAdmin هم برای ساختن جدول‌ها معرفی می‌شود (d126).

جدول را باید از پیش طراحی کرد: ستون‌ها و نوع هر کدام. ویدئو فهرستی از نوع‌های MySQL را نشان می‌دهد (`INT` و گونه‌هایش، `DECIMAL`، `FLOAT`، تاریخ و زمان، `TEXT`، `ENUM`، `CHAR` و `VARCHAR`) و می‌گوید در SQLite همهٔ این‌ها به یکی از پنج **وابستگی نوع** (type affinity) می‌رسند: NULL، INTEGER، REAL، TEXT و BLOB. هر جدول یک **کلید اصلی** لازم دارد تا هر سطر یکتا و سریع شناخته شود؛ کلید اصلی می‌تواند ترکیبی از چند ستون هم باشد.

بیشتر ویدئو چهار عمل اصلی را روی دو جدول نمونهٔ `users` و `moms` نشان می‌دهد: `INSERT INTO ... VALUES`، `SELECT ... FROM ... WHERE ... ORDER BY` (و `SELECT *`)، `JOIN ... ON` با نام کامل ستون (`users.username`) و تشبیه نمودار ون، `UPDATE ... SET ... WHERE` و `DELETE FROM ... WHERE`. در پایان می‌گوید کار دستی در phpMyAdmin برای وب‌سایت مناسب نیست و زبان‌هایی مثل پایتون می‌توانند همین پرس‌وجوها را خودکار اجرا کنند.

## نکته‌های کلیدی

- پایگاه داده مثل کتاب کار صفحه‌گسترده است: جدول‌ها مثل برگه‌ها، هر کدام با سطر و ستون.
- SQLite سبک‌تر از MySQL است و CS50 همان را به کار می‌برد.
- نوع‌های فراوان MySQL در SQLite به پنج وابستگی نوع می‌رسند: NULL، INTEGER، REAL، TEXT، BLOB.
- کلید اصلی هر سطر را یکتا می‌کند؛ معمولاً عدد صحیحی است که خودکار افزایش می‌یابد (autoincrement).
- چهار عمل اصلی: `INSERT`، `SELECT`، `UPDATE` و `DELETE`؛ `WHERE` تعیین می‌کند کدام سطرها.
- `JOIN ... ON` دو جدول را موقتاً کنار هم می‌گذارد و جدول‌ها از هم جدا می‌مانند.
- وقتی دو جدول ستون هم‌نام دارند، نام کامل `table.column` ابهام را برطرف می‌کند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`sql.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: پایگاه داده در وب](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=0s)
- [۰:۴۷ — تشبیه صفحه‌گسترده](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=47s)
- [۲:۲۴ — SQL، MySQL و SQLite](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=144s)
- [۳:۱۵ — phpMyAdmin](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=195s)
- [۴:۳۷ — نوع‌های داده](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=277s)
- [۶:۲۹ — CHAR و VARCHAR](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=389s)
- [۸:۱۹ — وابستگی نوع در SQLite](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=499s)
- [۸:۵۸ — کلید اصلی](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=538s)
- [۹:۳۰ — کلید اصلی ترکیبی](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=570s)
- [۱۰:۴۴ — جدول‌های نمونهٔ users و moms](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=644s)
- [۱۱:۲۹ — INSERT](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=689s)
- [۱۲:۴۹ — autoincrement](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=769s)
- [۱۴:۱۳ — SELECT](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=853s)
- [۱۶:۰۵ — SELECT *](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=965s)
- [۱۷:۴۹ — JOIN](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=1069s)
- [۱۹:۵۴ — تشبیه نمودار ون](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=1194s)
- [۲۱:۰۶ — UPDATE](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=1266s)
- [۲۱:۴۲ — DELETE](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=1302s)
- [۲۲:۱۶ — خودکارسازی با زبان برنامه‌نویسی](https://www.youtube.com/watch?v=AywtnUjQ6X4&t=1336s)

> [!NOTE]
> **یادداشت (d126، d127)**
> این ویدئو در ۲۰۱۷ برای بخش توسعهٔ وب CS50 قدیمی ضبط شده است. نوع‌های `CHAR(n)`، `VARCHAR(n)` و `ENUM` مال MySQL‌اند؛ SQLite طول `n` را نادیده می‌گیرد و چیزی با «بایت‌های null» پر نمی‌کند، و `ENUM` ندارد. در این هفته SQLite و `sqlite3` را به کار می‌بری، نه phpMyAdmin. جملهٔ «احتمالاً JOIN زیادی نمی‌نویسی» هم برای هفتهٔ ۷ امروز صادق نیست: Movies و Fiftyville به JOIN یا پرس‌وجوی تودرتو نیاز دارند.

> **تألیفی: دربارهٔ گذرواژه‌ها**
> جدول نمونهٔ `users` در ویدئو گذرواژه را به شکل متن ساده نگه می‌دارد. این فقط برای نمایش است؛ برنامه‌های واقعی گذرواژه را درهم‌سازی (hash) می‌کنند و هرگز متن ساده‌اش را ذخیره نمی‌کنند. هفتهٔ ۹ این را نشان می‌دهد.

## مفاهیم مرتبط

- پایگاه دادهٔ رابطه‌ای: جدول‌ها، سطرها و ستون‌ها — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- SQL: زبانی برای کار با پایگاه داده — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- SQLite در برابر MySQL و phpMyAdmin در ویدئوی کوتاه — [یادداشت](/kb/d/w07-sh-sql)
- نوع‌های SQLite: BLOB، INTEGER، NUMERIC، REAL، TEXT — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u02`)
- کلید اصلی (PRIMARY KEY) — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u01`)
- AUTOINCREMENT و کلید اصلی خودکار — [یادداشت](/kb/d/w07-sh-sql) · درس کوتاه `w07-l04` (واحد `w07-l04-u02`)
- CRUD: ایجاد، خواندن، به‌روزرسانی، حذف — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- INSERT INTO ... (ستون‌ها) VALUES (...) — [یادداشت](/kb/d/w07-n04) · درس کوتاه `w07-l03` (واحد `w07-l03-u01`)
- SELECT ... FROM ...: خواندن ستون‌ها از جدول — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- SELECT *: همهٔ ستون‌ها — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- WHERE: فیلتر سطرها با عبارت بولی — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- ORDER BY با ASC و DESC — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u03`)
- JOIN ... ON: ترکیب دو جدول با کلید مشترک — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u01`)
- نام کامل ستون: table.column — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u01`)
- UPDATE ... SET ... WHERE ... — [یادداشت](/kb/d/w07-n06) · درس کوتاه `w07-l03` (واحد `w07-l03-u03`)
- DELETE FROM ... WHERE ... — [یادداشت](/kb/d/w07-n05) · درس کوتاه `w07-l03` (واحد `w07-l03-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/AywtnUjQ6X4) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/sql/sql.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/sql/lang/en/sql.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/sql/lang/en/sql.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
