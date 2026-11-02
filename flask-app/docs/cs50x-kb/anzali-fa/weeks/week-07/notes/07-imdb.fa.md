---
id: w07-n07
type: note
title: 'IMDb: طراحی جدول‌ها، کلیدها، نوع‌ها و پرس‌وجوی تودرتو (IMDb)'
title_fa: 'IMDb: طراحی جدول‌ها، کلیدها، نوع‌ها و پرس‌وجوی تودرتو'
title_en: IMDb
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: IMDb
official_anchor: imdb
source_url: https://cs50.harvard.edu/x/2026/notes/7/#imdb
source_refs:
- src-notes-7#imdb
- src-short-sql
- src-pset-7
- src-sqlite-docs
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-redundancy
- w07-c-one-to-one
- w07-c-primary-key
- w07-c-foreign-key
- w07-c-sqlite-types
- w07-c-constraints
- w07-c-nested-query
prev: w07-n06
next: w07-n08
order: 7
video:
  youtube_id: oqRU2So6Z2Y
  start: '53:25'
  start_seconds: 3205
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=3205s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'familiar with IMDB'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# IMDb: طراحی جدول‌ها، کلیدها، نوع‌ها و پرس‌وجوی تودرتو

> **منبع رسمی:** بخش «IMDb» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#imdb). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۳:۲۵ تا حدود ۱:۱۰:۰۹](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=3205s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

داده‌های واقعی در یک جدول جا نمی‌شوند. اینجا می‌بینی چرا داده را در چند جدول می‌شکنیم، کلید اصلی و کلید خارجی چه نقشی دارند و چطور با پرس‌وجوی تودرتو از یک جدول به جدول دیگر می‌رسیم. ساختار پایگاه دادهٔ پرابلم‌ست Movies هم بسیار شبیه همین پایگاه دادهٔ IMDb است.

## IMDb

- پایگاه داده‌ای را تصور کن برای فهرست کردن سریال‌های تلویزیونی. می‌شود صفحه‌گسترده‌ای ساخت با ستون‌هایی مثل `title`، `star`، `star`، `star`، `star` و ستاره‌های بیشتر. مشکل این روش این است که فضای زیادی هدر می‌رود: بعضی سریال‌ها یک ستاره دارند و بعضی ده‌ها ستاره.
- می‌توانیم پایگاه داده را به چند برگه تقسیم کنیم: برگهٔ `shows`، برگهٔ `stars` و برگهٔ `people`. در برگهٔ `people` هر فرد یک `id` یکتا دارد و در برگهٔ `shows` هر سریال هم یک `id` یکتا. در برگهٔ سوم به نام `stars` با یک `show_id` و یک `person_id` افراد را به سریال‌ها ربط می‌دهیم. این بهتر است، اما هنوز پایگاه دادهٔ ایدئالی نیست.
- IMDb پایگاه داده‌ای از افراد، سریال‌ها، نویسندگان، ستاره‌ها، ژانرها و امتیازها ارائه می‌دهد. درس‌نامه رابطهٔ این جدول‌ها را با نموداری از شش جعبه نشان می‌دهد که پیکان‌ها آن‌ها را به هم وصل می‌کنند: `people`، `shows`، `stars`، `writers`، `genres` و `ratings` (پیوند تصویر در `media.json`، فقط پیوند).

- پس از دانلود `shows.db` (پیوند در درس‌نامهٔ رسمی) می‌توانی در ترمینال `sqlite3 shows.db` را اجرا کنی.
- روی رابطهٔ دو جدول `shows` و `ratings` تمرکز کنیم. درس‌نامه این رابطه را با دو جعبه نشان می‌دهد، یکی `shows` و دیگری `ratings` (پیوند تصویر در `media.json`).

- برای دیدن این رابطه می‌توانیم `SELECT * FROM ratings LIMIT 10;` را اجرا کنیم و پس از بررسی خروجی، `SELECT * FROM shows LIMIT 10;` را.
- با بررسی `shows` و `ratings` می‌بینیم که رابطه‌شان **یک‌به‌یک** است: هر سریال یک امتیاز دارد.
- برای فهم پایگاه داده، با اجرای `.schema` نه فقط هر جدول، بلکه ستون‌های درون هر جدول را هم می‌بینی.
- دقیق‌تر، `.schema shows` ستون‌های `shows` را نشان می‌دهد و `.schema ratings` ستون‌های `ratings` را.
- ارجاعی به `id` سریال در همهٔ جدول‌ها هست. در جدول `shows` این ستون فقط `id` نام دارد. به این ستون مشترک **کلید** می‌گویند. **کلید اصلی** (primary key) برای شناسایی یکتای یک رکورد در جدول به کار می‌رود. **کلید خارجی** (foreign key) با اشاره به کلید اصلی جدول دیگر، میان جدول‌ها رابطه می‌سازد. در طرح‌وارهٔ `ratings` می‌بینی که `show_id` کلید خارجی است که به `id` در `shows` ارجاع می‌دهد.
- با ذخیرهٔ داده در پایگاه دادهٔ رابطه‌ای به این شکل، داده بهینه‌تر ذخیره می‌شود.
- در SQLite پنج نوع داده داریم:

```text
BLOB       -- binary large objects that are groups of ones and zeros
INTEGER    -- an integer
NUMERIC    -- for numbers that are formatted specially like dates
REAL       -- like a float
TEXT       -- for strings and the like
```

- همچنین می‌شود برای ستون‌ها **قید**های ویژه گذاشت:

```text
NOT NULL
UNIQUE
```

- با این داده‌ها بیشتر بازی کنیم تا رابطه‌ها را بهتر بفهمیم. `SELECT * FROM ratings;` را اجرا کن. امتیازها خیلی زیادند!
- با `SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10;` داده را محدودتر می‌کنیم. این پرس‌وجو ده سریال نشان می‌دهد، اما نمی‌دانیم هر `show_id` کدام سریال است.
- با `SELECT * FROM shows WHERE id = 626124;` می‌توانی بفهمی این سریال‌ها کدام‌اند.
- می‌توانیم پرس‌وجو را کارآمدتر کنیم و این را اجرا کنیم:

```sql
SELECT title
FROM shows
WHERE id IN (
    SELECT show_id
    FROM ratings
    WHERE rating >= 6.0
    LIMIT 10
);
```

- دقت کن که این پرس‌وجو دو پرس‌وجو را **تودرتو** می‌کند: پرس‌وجوی درونی را پرس‌وجوی بیرونی به کار می‌برد.

> [!NOTE]
> **یادداشت**
> درس‌نامه از «پنج نوع داده» می‌گوید و `NUMERIC` را «برای عددهایی با قالب ویژه مثل تاریخ» معرفی می‌کند. مستندات SQLite دقیق‌تر است: SQLite پنج **کلاس ذخیره‌سازی** دارد (`NULL`، `INTEGER`، `REAL`، `TEXT`، `BLOB`) و `NUMERIC` یک «وابستگی نوع» (type affinity) ستون است، نه کلاس ذخیره‌سازی. SQLite تاریخ را معمولاً به شکل `TEXT`، `REAL` یا `INTEGER` نگه می‌دارد (d129).

> [!NOTE]
> **از ویدئوی کوتاه: نوع CHAR**
> Doug Lloyd در ویدئوی کوتاه (با MySQL) می‌گوید ستون `CHAR` با طول ثابت، جای خالی را با «معادل بایت‌های null» پر می‌کند. مستندات MySQL می‌گوید مقدار `CHAR` با **فاصله** پر می‌شود و SQLite اصلاً طول اعلام‌شده را رعایت نمی‌کند (d127).

> [!TIP]
> **تألیفی: پرس‌وجوی تودرتو روی پایگاه دادهٔ نمونه**
> پایگاه دادهٔ نمونهٔ `fixtures/shows.sql` شش سریال دارد و یکی از آن‌ها (`Brooklyn Nine-Nine`) در `ratings` سطری ندارد. پرس‌وجوی تودرتوی بالا روی آن پنج عنوان برمی‌گرداند، از جمله دو بار `The Office`، چون دو سریال جدا با این نام هست (۲۰۰۱ و ۲۰۰۵) با دو `id` متفاوت (اجراشده روی جعبهٔ ساخت). همین است که عنوان را برای شناسایی کافی نمی‌کند و به `id` نیاز داریم.

> [!TIP]
> **تألیفی: LIMIT درون پرس‌وجوی درونی**
> در پرس‌وجوی رسمی، `LIMIT 10` بدون `ORDER BY` آمده است؛ پس «ده سریال دلخواه با امتیاز دست‌کم ۶» انتخاب می‌شود، نه ده سریال برتر. برای «برترین‌ها» باید `ORDER BY rating DESC` پیش از `LIMIT` بیاید.

## اشتباه‌های رایج

- ذخیرهٔ چند ستاره در ستون‌های `star1`، `star2`، ... به جای جدول جدا.
- استفاده از عنوان یا نام به‌عنوان شناسه؛ عنوان‌ها و نام‌ها تکراری می‌شوند.
- استفاده از `=` به جای `IN` وقتی پرس‌وجوی درونی بیش از یک سطر برمی‌گرداند؛ SQLite خطا نمی‌دهد و فقط با سطر اول مقایسه می‌کند.

## جمع‌بندی

- تکرار و ستون‌های خالی را با شکستن داده به چند جدول از بین می‌بریم.
- کلید اصلی هر سطر را یکتا مشخص می‌کند و کلید خارجی به کلید اصلی جدول دیگر اشاره می‌کند.
- `WHERE id IN (SELECT ...)` پرس‌وجوها را تودرتو می‌کند.

## پیوندها

- قبلی: [تغییر داده با UPDATE](/kb/d/w07-n06)
- بعدی: [پیوند جدول‌ها با JOIN](/kb/d/w07-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
