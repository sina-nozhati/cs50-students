---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-pr-favorites
type: practice-guide
title: راهنمای پاک‌سازی علاقه‌مندی‌ها (Favorites)
title_fa: پاک‌سازی علاقه‌مندی‌ها (Favorites)
title_en: Favorites
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/favorites/
source_refs:
- src-practice-favorites#background
- src-practice-favorites#implementation-details
- src-anzali-authored-7
concept_ids:
- w07-c-sqlite3-cli
- w07-c-schema
- w07-c-select-star
- w07-c-update
- w07-c-where
- w07-c-like-wildcard
- w07-c-missing-where-danger
- w07-c-backups-permissions
- w07-c-string-literal-quotes
- w07-c-data-cleaning
problem_set_ref: weeks/week-07/problem-sets/favorites.json
prev: w07-ps-fiftyville
next: w07-pr-prophecy
order: 22
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای پاک‌سازی علاقه‌مندی‌ها (Favorites)

> **منبع رسمی:** [Favorites](https://cs50.harvard.edu/x/2026/practice/favorites/) از مسئله‌های تمرینی هفتهٔ ۷ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

در سخنرانی هفتهٔ ۷ سال ۲۰۲۱ پایگاه داده‌ای به نام `favorites.db` از سریال‌های محبوب دانشجویان CS50 ساخته شد. مثل بیشتر داده‌های خام، عنوان‌ها ناهمسان و پر از غلط تایپی‌اند، و کار تو پاک‌سازی آن‌ها با `UPDATE` است تا پرس‌وجوها ساده و نتیجه‌ها درست شوند.

این `favorites.db` با فایل `favorites.db` سخنرانی ۲۰۲۶ (زبان و مسئلهٔ محبوب) فرق دارد: دو جدول `shows` و `genres` دارد (d124).

> **از سخنرانی:** `UPDATE` و خطر نبودن `WHERE` در [یادداشت UPDATE](/kb/d/w07-n06)؛ `LIKE` و نقل‌قول‌ها در [یادداشت SELECT](/kb/d/w07-n03).

## خواسته‌های رسمی

1. با کلیدواژهٔ `UPDATE` پایگاه داده را پاک‌سازی کن تا برای تحلیل مفیدتر شود.
2. به جای بازنویسی تک‌تک عنوان‌های نادرست، چند گونهٔ یک سریال را با هم انتخاب و به املای درست به‌روزرسانی کن؛ شاید `LIKE` کمک کند.
3. عنوان‌های زیادی باید پاک شوند، از جمله بیست عنوان فهرست رسمی؛ اگر وقت کم است، شش عنوان پیشنهادی صفحهٔ رسمی جالب‌ترند.
4. همهٔ دستورهای SQL را در فایل تازهٔ `favorites.sql` ذخیره کن.

> **توجه (d124):** این مسئلهٔ تمرینی از آزمایشگاه‌های CS50 پاییز ۲۰۲۲ آمده است؛ فایل آغازین نشانی ۲۰۲۲ دارد و همان‌طور که در صفحهٔ رسمی هست نقل شده است. صفحهٔ رسمی می‌گوید check50 ندارد و تحویل لازم نیست.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. پوشه `favorites.db` و فایل خالی `favorites.sql` را دارد. پیش از هر `UPDATE` یک نسخهٔ پشتیبان از `favorites.db` بگیر (مثلاً با `cp`) تا اگر اشتباه کردی بتوانی از نو شروع کنی.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/7/favorites.zip
unzip favorites.zip
rm favorites.zip
```

## فرمان‌های رسمی صفحه

> **رسمی:** این فرمان‌ها عیناً از صفحهٔ رسمی آمده‌اند.

باز کردن پایگاه داده:

```bash
sqlite3 favorites.db
```

دیدن دستورهای ساخت دو جدول:

```sql
.schema
```

دیدن داده‌های shows:

```sql
SELECT * FROM shows;
```

نمونهٔ رسمی صفحه برای اولین عنوان:

```sql
UPDATE shows SET title = "How I Met Your Mother" WHERE title = "How i met your mother";
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- sqlite3: برنامهٔ خط فرمان SQLite — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- طرح‌واره (schema) و .schema / CREATE TABLE — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- SELECT *: همهٔ ستون‌ها — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- UPDATE ... SET ... WHERE ... — [یادداشت](/kb/d/w07-n06) · درس کوتاه `w07-l03` (واحد `w07-l03-u03`)
- WHERE: فیلتر سطرها با عبارت بولی — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- LIKE و % برای الگو — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- UPDATE یا DELETE بدون WHERE همهٔ سطرها را تغییر می‌دهد — [یادداشت](/kb/d/w07-n06) · درس کوتاه `w07-l03` (واحد `w07-l03-u03`)
- مجوزها و نسخهٔ پشتیبان پیش از تغییر داده — [یادداشت](/kb/d/w07-n06) · درس کوتاه `w07-l03` (واحد `w07-l03-u04`)
- رشتهٔ SQL داخل نقل‌قول تکی؛ نقل‌قول دوتایی برای شناسه — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u04`)
- پاک‌سازی داده با UPDATE (اختیاری) — [یادداشت](/kb/d/w07-pr-favorites)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. پیش از هر `UPDATE`، همان شرط `WHERE` را در یک `SELECT` اجرا کن و ببین دقیقاً کدام سطرها را می‌گیرد.
2. `LIKE` بزرگی و کوچکی حروف لاتین را نادیده می‌گیرد و `%` هر تعداد نویسه را می‌پذیرد. ولی الگوی خیلی کلی ممکن است عنوان سریال دیگری را هم بگیرد.
3. صفحهٔ رسمی پیشنهاد می‌کند در پایان همهٔ عنوان‌ها را به ترتیب الفبا ببینی؛ گونه‌های باقی‌مانده کنار هم دیده می‌شوند.
4. نمونهٔ رسمی صفحه رشته‌ها را با نقل‌قول دوتایی نوشته است. SQLite این را می‌پذیرد چون ستونی با آن نام نیست، ولی در دستورهای خودت نقل‌قول تکی امن‌تر است (d121).

## اشتباه‌های رایج

- `UPDATE` بدون `WHERE` که همهٔ عنوان‌ها را یکی می‌کند
- الگوی `LIKE` خیلی کلی که سریال دیگری را هم تغییر می‌دهد
- نگه نداشتن نسخهٔ پشتیبان
- ذخیره نکردن دستورها در `favorites.sql`

## چک‌لیست خودآزمایی

1. پیش از تغییر، از `favorites.db` نسخهٔ پشتیبان گرفته‌ام.
2. هر `UPDATE` بند `WHERE` دارد و پیش از اجرا، همان شرط را با `SELECT` آزموده‌ام.
3. گونه‌های یک عنوان را با یک دستور و `LIKE` گرفته‌ام، ولی مراقب بوده‌ام عنوان سریال دیگری را نگیرم.
4. دست‌کم شش عنوان پیشنهادی را پاک کرده‌ام.
5. همهٔ دستورها در `favorites.sql` ذخیره شده‌اند.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چرا فکر می‌کنی «پاک‌سازی» داده لازم است وقتی می‌توانی از `LIKE` استفاده کنی؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [فایل آغازین favorites.zip](https://cdn.cs50.net/2022/fall/labs/7/favorites.zip): پایگاه دادهٔ رسمی؛ این بسته آن را باز نمی‌کند (D59).

## پیوند رسمی

- [Favorites](https://cs50.harvard.edu/x/2026/practice/favorites/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
