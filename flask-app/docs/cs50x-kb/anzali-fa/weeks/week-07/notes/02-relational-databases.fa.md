---
id: w07-n02
type: note
title: پایگاه دادهٔ رابطه‌ای و sqlite3 (Relational Databases)
title_fa: پایگاه دادهٔ رابطه‌ای و sqlite3
title_en: Relational Databases
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Relational Databases
official_anchor: relational-databases
source_url: https://cs50.harvard.edu/x/2026/notes/7/#relational-databases
source_refs:
- src-notes-7#relational-databases
- src-short-sql
- src-sqlite-docs
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-relational-db
- w07-c-sql-language
- w07-c-crud
- w07-c-sqlite3-cli
- w07-c-csv-import
- w07-c-schema
- w07-c-sql-functions
prev: w07-n01
next: w07-n03
order: 2
video:
  youtube_id: oqRU2So6Z2Y
  start: '24:12'
  start_seconds: 1452
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=1452s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'what the world calls a relational database'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# پایگاه دادهٔ رابطه‌ای و sqlite3

> **منبع رسمی:** بخش «Relational Databases» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#relational-databases). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۴:۱۲ تا حدود ۳۲:۴۹](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=1452s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برنامهٔ پایتونی یادداشت قبل برای هر پرسش تازه («کدام زبان محبوب‌تر است؟»، «چند نفر Hello, World را انتخاب کردند؟») به کد تازه نیاز داشت. پایگاه دادهٔ رابطه‌ای و SQL این پرسش‌ها را به چند کلمه تبدیل می‌کنند. در این یادداشت یاد می‌گیری پایگاه داده را بسازی، CSV را واردش کنی و ساختارش را ببینی.

## پایگاه دادهٔ رابطه‌ای

- Google، X و Meta همه برای ذخیرهٔ اطلاعاتشان در مقیاس بزرگ از پایگاه داده‌های رابطه‌ای استفاده می‌کنند.
- پایگاه دادهٔ رابطه‌ای داده را در سطرها و ستون‌ها، در ساختارهایی به نام **جدول** ذخیره می‌کند.
- SQL چهار نوع فرمان دارد:

```text
Create 
Read
Update
Delete
```

- به این چهار عمل با محبت **CRUD** می‌گویند.
- با نحو SQL یعنی `CREATE TABLE table (column type, ...);` می‌توانیم پایگاه داده بسازیم. اما این فرمان را کجا اجرا کنیم؟
- `sqlite3` نوعی پایگاه دادهٔ SQL است که ویژگی‌های اصلی لازم برای این درس را دارد.
- در ترمینال با نوشتن `sqlite3 favorites.db` یک پایگاه دادهٔ SQL می‌سازیم. وقتی پرسیده شد، با زدن `y` تأیید می‌کنیم که می‌خواهیم `favorites.db` ساخته شود.
- اعلان (prompt) ترمینال عوض می‌شود، چون حالا داخل برنامه‌ای به نام `sqlite` هستیم.
- با نوشتن `.mode csv` برنامهٔ `sqlite` را به حالت `csv` می‌بریم. بعد با `.import favorites.csv favorites` داده را از فایل `csv` وارد می‌کنیم. به نظر می‌رسد هیچ اتفاقی نیفتاده است!
- با نوشتن `.schema` ساختار پایگاه داده را می‌بینیم.
- با نحو `SELECT columns FROM table` می‌توانی داده را از یک جدول بخوانی.
- برای نمونه، `SELECT * FROM favorites;` هر سطر `favorites` را چاپ می‌کند.
- با `SELECT language FROM favorites;` زیرمجموعه‌ای از داده (فقط یک ستون) را می‌گیری.
- SQL فرمان‌های زیادی برای دسترسی به داده دارد، از جمله:

```text
AVG
COUNT
DISTINCT
LOWER
MAX
MIN
UPPER
```

- برای نمونه، می‌توانی `SELECT COUNT(*) FROM favorites;` را بنویسی. همچنین `SELECT DISTINCT language FROM favorites;` فهرست زبان‌های یکتای پایگاه داده را می‌دهد و حتی `SELECT COUNT(DISTINCT language) FROM favorites;` تعداد آن‌ها را می‌شمارد.
- SQL فرمان‌های دیگری هم برای پرس‌وجوها دارد:

```text
WHERE       -- adding a Boolean expression to filter our data
LIKE        -- filtering responses more loosely
ORDER BY    -- ordering responses
LIMIT       -- limiting the number of responses
GROUP BY    -- grouping responses together
```

- دقت کن که در SQL برای نوشتن توضیح از `--` استفاده می‌کنیم.

> [!NOTE]
> **یادداشت**
> درخواست تأیید با `y` هنگام اجرای `sqlite3 favorites.db` رفتار محیط cs50.dev است؛ برنامهٔ استاندارد `sqlite3` بدون پرسش، فایل را در اولین نوشتن می‌سازد (d130). فرمان‌هایی که با نقطه شروع می‌شوند (`.mode`، `.import`، `.schema`) فرمان‌های خود برنامهٔ `sqlite3` هستند، نه بخشی از زبان SQL، و نقطه‌ویرگول نمی‌خواهند.

> [!TIP]
> **تألیفی: خروجی در این بسته**
> در cs50.dev خروجی `sqlite3` ممکن است به شکل جدول با حاشیه نمایش داده شود. در پرسش‌ها و تمرین‌های این بسته خروجی را به «حالت فهرست» (list mode) خود `sqlite3` می‌نویسیم: هر سطر نتیجه در یک خط، ستون‌ها با `|` جدا، بدون سطر سرستون، و `NULL` به شکل خالی. فقط **مقدارها** مقایسه می‌شوند، نه حاشیه‌ها. پایگاه‌داده‌های نمونهٔ این بسته در پوشهٔ `weeks/week-07/fixtures/` هستند و داده‌هایشان ساختگی است.

> [!NOTE]
> **از ویدئوی کوتاه: SQLite و MySQL**
> Doug Lloyd در ویدئوی کوتاه SQL می‌گوید آن ویدئو بخشی از مجموعهٔ ویدئوهای «توسعهٔ وب» است و نمونه‌هایش را با MySQL و ابزار گرافیکی phpMyAdmin نشان می‌دهد. در CS50x 2026 با `sqlite3` در ترمینال کار می‌کنی؛ ایده‌ها یکی‌اند اما نام نوع‌ها و ابزارها فرق دارند (d126).

## اشتباه‌های رایج

- فراموش کردن `;` در پایان فرمان SQL؛ `sqlite3` منتظر ادامهٔ فرمان می‌ماند و اعلان `...>` نشان می‌دهد.
- گذاشتن `;` بعد از فرمان‌های نقطه‌دار یا اجرای آن‌ها در پایتون؛ این فرمان‌ها فقط در خود `sqlite3` معنا دارند.
- اجرای `.import` بدون `.mode csv`؛ فایل به‌درستی به ستون‌ها شکسته نمی‌شود.

## جمع‌بندی

- پایگاه دادهٔ رابطه‌ای داده را در جدول‌ها نگه می‌دارد؛ SQL زبان کار با آن است و چهار عمل CRUD دارد.
- `sqlite3 file.db` پایگاه داده را باز می‌کند؛ `.mode csv` و `.import` فایل CSV را وارد می‌کنند و `.schema` ساختار را نشان می‌دهد.
- `SELECT`، تابع‌هایی مثل `COUNT` و `DISTINCT`، و بندهایی مثل `WHERE`، `LIKE`، `ORDER BY`، `LIMIT` و `GROUP BY` ابزارهای اصلی خواندن داده‌اند.

## پیوندها

- قبلی: [پایگاه دادهٔ تخت: CSV و شمارش با پایتون](/kb/d/w07-n01)
- بعدی: [خواندن داده با SELECT](/kb/d/w07-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
