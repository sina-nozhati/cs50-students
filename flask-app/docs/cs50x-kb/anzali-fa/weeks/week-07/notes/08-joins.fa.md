---
id: w07-n08
type: note
title: پیوند جدول‌ها با JOIN (JOINs)
title_fa: پیوند جدول‌ها با JOIN
title_en: JOINs
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: JOINs
official_anchor: joins
source_url: https://cs50.harvard.edu/x/2026/notes/7/#joins
source_refs:
- src-notes-7#joins
- src-section-7
- src-section-7-transcript
- src-sqlite-docs
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-join
- w07-c-one-to-many
- w07-c-many-to-many
- w07-c-multi-join
- w07-c-implicit-join
- w07-c-qualified-column
prev: w07-n07
next: w07-n09
order: 8
video:
  youtube_id: oqRU2So6Z2Y
  start: '1:10:09'
  start_seconds: 4209
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=4209s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'an ability to join two tables'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# پیوند جدول‌ها با JOIN

> **منبع رسمی:** بخش «JOINs» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#joins). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۰:۰۹ تا حدود ۱:۴۱:۴۹](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=4209s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پرس‌وجوی تودرتو یک راه رسیدن از جدولی به جدول دیگر بود. `JOIN` راه دوم است: جدول‌ها را موقتاً کنار هم می‌گذارد تا ستون‌های هر دو را در یک نتیجه ببینی. در Movies و Fiftyville تقریباً هر پرسش جالب به داده‌ای از دو یا چند جدول نیاز دارد، پس باید هر دو راه را بشناسی.

## JOINها

- داده را از `shows` و `ratings` می‌گیریم. دقت کن که `shows` و `ratings` هر دو یک `id` مشترک دارند.
- چطور جدول‌ها را موقتاً ترکیب کنیم؟ با فرمان `JOIN` می‌شود جدول‌ها را به هم **پیوند** داد.
- این فرمان را اجرا کن:

```sql
SELECT * FROM shows
  JOIN ratings ON shows.id = ratings.show_id
  WHERE rating >= 6.0
  LIMIT 10;
```

- دقت کن که نتیجه جدولی پهن‌تر از جدول‌هایی است که تا اینجا دیده‌ایم.
- پرس‌وجوهای قبلی رابطهٔ **یک‌به‌یک** میان این کلیدها را نشان دادند. حالا چند رابطهٔ **یک‌به‌چند** را بررسی کنیم. روی جدول `genres` تمرکز کن و این را اجرا کن:

```sql
SELECT * FROM genres
LIMIT 10;
```

- دقت کن که این دید خوبی از دادهٔ خام می‌دهد. شاید ببینی یک سریال سه مقدار دارد. این یک رابطهٔ یک‌به‌چند است.
- با نوشتن `.schema genres` می‌توانیم دربارهٔ جدول `genres` بیشتر بدانیم.
- برای دانستن بیشتر دربارهٔ کمدی‌های پایگاه داده، این فرمان را اجرا کن:

```sql
SELECT title FROM shows
WHERE id IN (
  SELECT show_id FROM genres
  WHERE genre = 'Comedy'
  LIMIT 10
);
```

- دقت کن که نتیجه فهرستی از کمدی‌هاست، از جمله *Catweazle*.
- با پیوند دادن جدول‌ها می‌توانیم دربارهٔ Catweazle بیشتر بدانیم:

```sql
SELECT * FROM shows
JOIN genres
ON shows.id = genres.show_id
WHERE id = 63881;
```

- دقت کن که نتیجه یک جدول موقت است. اشکالی ندارد که جدول تکرار داشته باشد. همچنین دقت کن که به Catweazle (یک عنوان) **چند** ژانر نسبت داده شده است، از جمله ماجراجویی، کمدی و خانوادگی.
- در برابر رابطه‌های یک‌به‌یک و یک‌به‌چند، رابطه‌های **چندبه‌چند** هم داریم. برای نمونه، افراد زیادی می‌توانند در سریال‌های زیادی ظاهر شوند!
- با این فرمان می‌توانیم دربارهٔ سریال *The Office* و بازیگرانش بیشتر بدانیم:

```sql
SELECT name FROM people WHERE id IN 
    (SELECT person_id FROM stars WHERE show_id = 
        (SELECT id FROM shows WHERE title = 'The Office' AND year = 2005));
```

- دقت کن که نتیجه جدولی است شامل نام ستاره‌های مختلف، به کمک پرس‌وجوهای تودرتو.
- می‌توانیم همهٔ سریال‌هایی را که Steve Carell در آن‌ها بازی کرده پیدا کنیم:

```sql
SELECT title FROM shows WHERE id IN 
    (SELECT show_id FROM stars WHERE person_id = 
        (SELECT id FROM people WHERE name = 'Steve Carell'));
```

- همین را می‌شود به شکل `JOIN` نوشت:

```sql
SELECT title FROM shows
JOIN stars ON shows.id = stars.show_id
JOIN people ON stars.person_id = people.id
WHERE name = 'Steve Carell';
```

- و همچنین به این شکل:

```sql
SELECT title FROM shows, stars, people 
WHERE shows.id = stars.show_id
AND people.id = stars.person_id
AND name = 'Steve Carell';
```

- با عملگر عام `%` می‌توانیم همهٔ افرادی را که نامشان با `Steve C` شروع می‌شود پیدا کنیم:

```sql
SELECT * FROM people WHERE name LIKE 'Steve C%';
```

> [!TIP]
> **تألیفی: سه شکل یک پاسخ روی پایگاه دادهٔ نمونه**
> روی `fixtures/shows.sql` هر سه پرس‌وجوی Steve Carell فقط `The Office` را برمی‌گردانند، و پرس‌وجوی `LIKE 'Steve C%'` دو نفر را: `Steve Carell` و `Steve Coogan`، اما نه `Steve Buscemi` (اجراشده روی جعبهٔ ساخت). سطرهای جدول موقت `JOIN` فقط وقتی ساخته می‌شوند که شرط `ON` برقرار باشد؛ برای همین `Brooklyn Nine-Nine` که در `ratings` سطری ندارد، در نتیجهٔ `JOIN` با `ratings` دیده نمی‌شود.

> [!TIP]
> **تألیفی: نام کامل ستون وقتی نام تکراری است**
> در `ON shows.id = ratings.show_id` نام جدول پیش از ستون آمده است. وقتی دو جدول ستونی هم‌نام دارند (مثلاً `id` در `shows` و `people`)، نوشتن `id` به‌تنهایی خطای `ambiguous column name: id` می‌دهد و باید `shows.id` یا `people.id` بنویسی. در پرس‌وجوی Catweazle، `WHERE id = 63881` کار می‌کند چون فقط `shows` ستونی به نام `id` دارد.

> [!NOTE]
> **از جلسهٔ حل تمرین: JOIN یا پرس‌وجوی تودرتو؟**
> در جلسهٔ حل تمرین گفته می‌شود JOINها «معمولاً کمی کندتر از SELECTهای تودرتو هستند، اما بستگی دارد»، و اینکه JOIN «تنها شکل پیوند است و نوع‌های مختلفی ندارد». در واقع SQLite علاوه بر `JOIN` (پیوند درونی) پیوندهای `LEFT JOIN` و `CROSS JOIN` هم دارد، و سرعت به طرح پرس‌وجو و شاخص‌ها بستگی دارد، نه به شکل نوشتن (d120، d122).

## اشتباه‌های رایج

- فراموش کردن `ON` در `JOIN`؛ هر سطر یک جدول با همهٔ سطرهای جدول دیگر جفت می‌شود و نتیجه بسیار بزرگ و نادرست می‌شود.
- نوشتن شرط پیوند اشتباه (مثلاً `shows.id = stars.person_id`).
- نوشتن نام ستون هم‌نام بدون نام جدول.
- فراموش کردن اینکه `JOIN` در رابطهٔ یک‌به‌چند سطر تکراری می‌سازد؛ گاهی `DISTINCT` لازم است.

## جمع‌بندی

- رابطه‌ها: یک‌به‌یک (`shows` و `ratings`)، یک‌به‌چند (`shows` و `genres`)، چندبه‌چند (`shows` و `people` از راه `stars`).
- `JOIN table ON a.col = b.col` جدول‌ها را موقتاً ترکیب می‌کند؛ `FROM a, b WHERE ...` همان کار را به شکل ضمنی انجام می‌دهد.
- یک پرسش را هم با پرس‌وجوی تودرتو و هم با `JOIN` می‌شود پاسخ داد.

## پیوندها

- قبلی: [IMDb: طراحی جدول‌ها، کلیدها، نوع‌ها و پرس‌وجوی تودرتو](/kb/d/w07-n07)
- بعدی: [نمایه (index) و B-tree](/kb/d/w07-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
