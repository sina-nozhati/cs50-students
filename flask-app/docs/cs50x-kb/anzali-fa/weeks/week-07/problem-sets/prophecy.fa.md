---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-pr-prophecy
type: practice-guide
title: راهنمای تالار پیشگویی (Hall of Prophecy)
title_fa: تالار پیشگویی (Hall of Prophecy)
title_en: Hall of Prophecy
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/prophecy/
source_refs:
- src-practice-prophecy#implementation-details
- src-practice-prophecy#developing-a-schema
- src-practice-prophecy#inserting-data
- src-anzali-authored-7
concept_ids:
- w07-c-redundancy
- w07-c-schema
- w07-c-primary-key
- w07-c-foreign-key
- w07-c-sqlite-types
- w07-c-many-to-many
- w07-c-insert
- w07-c-cs50-sql
- w07-c-placeholder-qmark
- w07-c-dictreader-columns
- w07-c-schema-refactor
problem_set_ref: weeks/week-07/problem-sets/prophecy.json
prev: w07-pr-favorites
next: null
order: 23
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای تالار پیشگویی (Hall of Prophecy)

> **منبع رسمی:** [Hall of Prophecy](https://cs50.harvard.edu/x/2026/practice/prophecy/) از مسئله‌های تمرینی هفتهٔ ۷ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

نگهبان «تالار پیشگویی» پایگاه داده‌ای از دانش‌آموزان هاگوارتز ساخته، ولی طراحی آن ضعیف است: `roster.db` فقط یک جدول `students` دارد و نام و رئیس هر خانه برای هر دانش‌آموز بارها تکرار شده است.

طراحی بهتر سه جدول دارد: یکی **فقط** برای دانش‌آموزان، یکی **فقط** برای خانه‌ها و یکی برای رابطهٔ دانش‌آموز و خانه. به این تغییر طرح‌واره **بازسازی** (refactoring) می‌گویند. داده را با `SELECT`، `CREATE` و `INSERT` جابه‌جا می‌کنی و صفحهٔ رسمی پیشنهاد می‌کند برای پر کردن جدول‌ها برنامه‌ای پایتون بنویسی.

> **از سخنرانی:** تکرار داده و کلیدهای اصلی و خارجی در [یادداشت IMDb](/kb/d/w07-n07)؛ رابطهٔ چندبه‌چند و جدول واسط در [یادداشت JOINها](/kb/d/w07-n08)؛ اجرای SQL از پایتون در [یادداشت SQL در پایتون](/kb/d/w07-n10). [جلسهٔ حل تمرین](/kb/d/w07-sec) همین اصل «یک جدول، یک موجودیت» را با مثال کارمندان توضیح می‌دهد.

## خواسته‌های رسمی

1. با دادهٔ موجود در `roster.db` پایگاه دادهٔ تازه‌ای بساز با یک جدول برای دانش‌آموزان، یک جدول برای خانه‌ها و یک جدول برای انتساب به خانه‌ها.
2. در `schema.sql` سه دستور `CREATE TABLE` لازم برای سه جدول تازه را بنویس.
3. هر جدول فقط یک موجودیت را نشان بدهد و هر جدول کلید اصلی داشته باشد؛ بعضی جدول‌ها با کلید خارجی بهتر طراحی می‌شوند.
4. سه دستور `CREATE TABLE` را اجرا کن و نتیجه را با `.schema` ببین.
5. داده را در طرح‌وارهٔ تازه وارد کن؛ بهتر است برنامه‌ای پایتون بنویسی که از `students.csv` بخواند.

> **توجه (d124):** این مسئلهٔ تمرینی از آزمایشگاه‌های CS50 پاییز ۲۰۲۲ آمده است؛ فایل آغازین نشانی ۲۰۲۲ دارد و همان‌طور که در صفحهٔ رسمی هست نقل شده است. صفحهٔ رسمی می‌گوید check50 ندارد و تحویل لازم نیست.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. پوشه `roster.db`، فایل خالی `schema.sql` و `students.csv` (همان دادهٔ جدول `students` به شکل CSV) را دارد. صفحهٔ رسمی می‌گوید با `sqlite3 roster.db` و `.schema` جدول را ببین و با `SELECT` محتوایش را.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/7/prophecy.zip
unzip prophecy.zip
rm prophecy.zip
```

## قطعه‌کدهای رسمی راهنما

> **رسمی:** این قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند و ابزار عمومی‌اند، نه بخشی از راه‌حل.

دستور `CREATE TABLE` جدول فعلی `students` (از صفحهٔ رسمی):

```sql
CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- تکرار داده (redundancy) و دلیل جدا کردن جدول‌ها — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u01`)
- طرح‌واره (schema) و .schema / CREATE TABLE — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- کلید اصلی (PRIMARY KEY) — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u01`)
- کلید خارجی (FOREIGN KEY ... REFERENCES) — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u01`)
- نوع‌های SQLite: BLOB، INTEGER، NUMERIC، REAL، TEXT — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u02`)
- رابطهٔ چندبه‌چند و جدول واسط (stars) — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u02`)
- INSERT INTO ... (ستون‌ها) VALUES (...) — [یادداشت](/kb/d/w07-n04) · درس کوتاه `w07-l03` (واحد `w07-l03-u01`)
- from cs50 import SQL و db.execute — [یادداشت](/kb/d/w07-n10) · درس کوتاه `w07-l06` (واحد `w07-l06-u03`)
- جای‌نگهدار ? و آرگومان جدا در db.execute — [یادداشت](/kb/d/w07-n10) · درس کوتاه `w07-l06` (واحد `w07-l06-u04`)
- DictReader: دسترسی به ستون با نام، مقاوم در برابر جابه‌جایی ستون‌ها — [یادداشت](/kb/d/w07-n01) · درس کوتاه `w07-l01` (واحد `w07-l01-u01`)
- بازطراحی طرح‌واره برای حذف تکرار (اختیاری) — [یادداشت](/kb/d/w07-pr-prophecy)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول فهرست کن چه اطلاعاتی داری (نام دانش‌آموز، نام خانه، رئیس خانه) و هر کدام به کدام موجودیت تعلق دارد. صفحهٔ رسمی می‌گوید پیش از نوع‌ها به همین فکر کن.
2. برای جدول رابطه از خودت بپرس هر سطر آن چه چیزی را ثبت می‌کند و به کدام کلیدهای اصلی نیاز دارد. جدول `stars` در یادداشت JOINها الگوی خوبی است.
3. در برنامهٔ پایتون، یک خانه را فقط یک بار وارد کن. پیش از وارد کردن، فکر کن از کجا می‌فهمی آن خانه را قبلاً افزوده‌ای و کلید اصلی‌اش چیست.
4. `db.execute` برای `INSERT` کلید اصلی سطر تازه را برمی‌گرداند (یادداشت SQL در پایتون). این عدد برای پر کردن جدول رابطه به کار می‌آید.
5. همیشه با جای‌نگهدار `?` مقدار بده، نه با f-string؛ نام‌ها ممکن است آپاستروف داشته باشند.

## اشتباه‌های رایج

- نگه داشتن نام یا رئیس خانه در جدول دانش‌آموزان
- جدول بدون کلید اصلی
- وارد کردن یک خانه به ازای هر دانش‌آموز
- ساختن رشتهٔ SQL با f-string به جای `?`

## چک‌لیست خودآزمایی

1. `schema.sql` سه دستور `CREATE TABLE` دارد.
2. هر جدول فقط یک موجودیت را نگه می‌دارد و نام و رئیس یک خانه فقط یک بار ذخیره می‌شود.
3. هر جدول کلید اصلی دارد و جدول رابطه با کلید خارجی به دو جدول دیگر اشاره می‌کند.
4. `.schema` سه جدول تازه را نشان می‌دهد.
5. برنامهٔ پایتون داده را از `students.csv` می‌خواند و با جای‌نگهدار `?` وارد می‌کند.
6. با `SELECT * FROM table;` محتوای هر سه جدول را بررسی کرده‌ام.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چرا فکر می‌کنی تکرار نکردن اطلاعاتی مثل خانه‌ها و رئیس‌ها برای هر دانش‌آموز طراحی بهتری است؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [فایل آغازین prophecy.zip](https://cdn.cs50.net/2022/fall/labs/7/prophecy.zip): پایگاه داده و CSV رسمی؛ این بسته آن‌ها را بازتولید نمی‌کند.
- [مقالهٔ بازسازی پایگاه داده](https://en.wikipedia.org/wiki/Database_refactoring): پیوند صفحهٔ رسمی؛ فقط پیوند.

## پیوند رسمی

- [Hall of Prophecy](https://cs50.harvard.edu/x/2026/practice/prophecy/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
