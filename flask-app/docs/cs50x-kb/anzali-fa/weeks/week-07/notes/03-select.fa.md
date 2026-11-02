---
id: w07-n03
type: note
title: خواندن داده با SELECT (SELECT)
title_fa: خواندن داده با SELECT
title_en: SELECT
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: SELECT
official_anchor: select
source_url: https://cs50.harvard.edu/x/2026/notes/7/#select
source_refs:
- src-notes-7#select
- src-transcript-7
- src-pset-7
- src-section-7
- src-section-7-transcript
- src-sqlite-docs
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-select
- w07-c-select-star
- w07-c-limit
- w07-c-count
- w07-c-distinct
- w07-c-where
- w07-c-and-or
- w07-c-like-wildcard
- w07-c-group-by
- w07-c-order-by
- w07-c-as-alias
- w07-c-string-literal-quotes
prev: w07-n02
next: w07-n04
order: 3
video:
  youtube_id: oqRU2So6Z2Y
  start: '32:49'
  start_seconds: 1969
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=1969s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'Select star from favorites'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# خواندن داده با SELECT

> **منبع رسمی:** بخش «SELECT» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#select). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۲:۴۹ تا حدود ۴۶:۰۷](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=1969s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`SELECT` پرکاربردترین فرمان SQL است و هر سه پرابلم‌ست این هفته (Songs، Movies و Fiftyville) فقط با `SELECT` حل می‌شوند. اینجا یاد می‌گیری سطرها را فیلتر، گروه‌بندی، مرتب و محدود کنی؛ همان کارهایی که در پایتون ده‌ها خط کد می‌خواست.

## SELECT

- برای نمونه، می‌توانیم این را اجرا کنیم و یک عدد (شمارش) نمایش داده می‌شود:

```sql
SELECT COUNT(*) FROM favorites WHERE language = 'C';
```

- همچنین می‌توانیم بنویسیم:

```sql
SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Hello, World';
```

- دقت کن چطور `AND` نتیجه را محدودتر می‌کند.
- به همین ترتیب می‌توانیم این را اجرا کنیم که یک جدول موقت با زبان و تعداد نشان می‌دهد:

```sql
SELECT language, COUNT(*) FROM favorites GROUP BY language;
```

- می‌توانیم آن را بهتر کنیم تا جدول نتیجه بر اساس تعداد مرتب شود:

```sql
SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);
```

- همین‌طور می‌توانیم این را اجرا کنیم:

```sql
SELECT COUNT(*) FROM favorites WHERE language = 'C' AND (problem = 'Hello, World' OR problem = 'Hello, It''s Me');
```

- دقت کن که دو علامت `''` پشت سر هم آمده‌اند تا بشود نقل‌قول تکی را طوری به کار برد که SQL را گیج نکند.
- همچنین می‌توانیم این را اجرا کنیم تا همهٔ مسئله‌هایی که با `Hello,` (همراه با یک فاصله) شروع می‌شوند پیدا شوند:

```sql
SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem LIKE 'Hello, %';
```

- خروجی را می‌توانیم این‌طور مرتب کنیم:

```sql
SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC;
```

- حتی می‌توانیم نام مستعار بسازیم، شبیه متغیر در پرس‌وجو:

```sql
SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC;
```

- و در پایان می‌توانیم خروجی را به یک یا چند مقدار محدود کنیم:

```sql
SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC LIMIT 1;
```

- دقت کن که طبق قرارداد، کلیدواژه‌های SQL اغلب با حروف بزرگ نوشته می‌شوند.

> [!TIP]
> **تألیفی: همین پرس‌وجوها روی پایگاه دادهٔ نمونه**
> پایگاه دادهٔ نمونهٔ `fixtures/favorites.sql` دوازده پاسخ ساختگی دارد. روی آن، پرس‌وجوی اول `4` را برمی‌گرداند، پرس‌وجوی `AND` عدد `1`، پرس‌وجوی `LIKE 'Hello, %'` عدد `2` و پرس‌وجوی `GROUP BY ... ORDER BY COUNT(*)` این سه سطر را به همین ترتیب: `Scratch|2`، `C|4`، `Python|6` (اجراشده روی جعبهٔ ساخت با SQLite 3.46). عددهای پایگاه دادهٔ واقعی سخنرانی فرق دارند.

> [!TIP]
> **تألیفی: ترتیب فقط با ORDER BY تضمین می‌شود**
> بدون `ORDER BY`، SQL هیچ ترتیبی برای سطرهای نتیجه قول نمی‌دهد؛ ممکن است امروز به یک ترتیب و بعد از ساخت شاخص به ترتیب دیگری بیایند. `LIMIT` بدون `ORDER BY` هم فقط «چند سطر دلخواه» را برمی‌گرداند. در پرسش‌های این بسته، نتیجهٔ پرس‌وجوی بدون `ORDER BY` به شکل مجموعه (بی‌ترتیب) مقایسه می‌شود.

> [!NOTE]
> **یادداشت**
> سخنرانی و جلسهٔ حل تمرین نقل‌قول تکی و دوتایی را بیشتر مسئلهٔ «سبک» می‌دانند. در SQLite نقل‌قول دوتایی برای **نام ستون یا جدول** است و فقط اگر چنین نامی نباشد، به رشته تبدیل می‌شود. روی پایگاه دادهٔ نمونه، `WHERE problem = "Mario"` عدد `2` می‌دهد، اما `WHERE problem = "problem"` عدد `12` می‌دهد، چون `"problem"` نام خود ستون است و هر سطر با خودش برابر است (اجراشده روی جعبهٔ ساخت). در این بسته رشته‌ها همیشه با نقل‌قول تکی نوشته می‌شوند (d121).

> [!TIP]
> **تألیفی: = حساس به بزرگی حروف است، LIKE نه**
> در SQLite، `language = 'c'` روی پایگاه دادهٔ نمونه `0` می‌دهد، اما `language LIKE 'c'` عدد `4`، چون `LIKE` برای حروف لاتین بزرگی و کوچکی را یکی می‌گیرد. `%` در `LIKE` یعنی «هر دنباله‌ای از نویسه‌ها، حتی خالی».

## اشتباه‌های رایج

- نوشتن رشته بدون نقل‌قول (`WHERE language = C`)؛ SQL آن را نام ستون می‌فهمد و خطای `no such column` می‌دهد.
- نوشتن `'Hello, It's Me'` با یک نقل‌قول تکی وسط رشته؛ رشته زودتر تمام می‌شود و خطای نحوی می‌گیری. باید `''` بنویسی.
- فراموش کردن پرانتز در ترکیب `AND` و `OR`؛ `AND` زودتر از `OR` ارزیابی می‌شود و نتیجه عوض می‌شود.
- انتظار ترتیب خاص بدون `ORDER BY`.

## جمع‌بندی

- `WHERE` با `=`، `AND`، `OR` و `LIKE` سطرها را فیلتر می‌کند.
- `GROUP BY` سطرها را گروه می‌کند و `COUNT(*)` هر گروه را می‌شمارد.
- `ORDER BY ... DESC`، `AS` و `LIMIT` نتیجه را مرتب، نام‌گذاری و محدود می‌کنند.

## پیوندها

- قبلی: [پایگاه دادهٔ رابطه‌ای و sqlite3](/kb/d/w07-n02)
- بعدی: [افزودن سطر با INSERT](/kb/d/w07-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
