---
id: w07-n09
type: note
title: نمایه (index) و B-tree (Indexes)
title_fa: نمایه (index) و B-tree
title_en: Indexes
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Indexes
official_anchor: indexes
source_url: https://cs50.harvard.edu/x/2026/notes/7/#indexes
source_refs:
- src-notes-7#indexes
- src-transcript-7
- src-sqlite-docs
- src-sql-box-7
- src-anzali-authored-7
- src-anzali-inference-7
- src-srt-7
concept_ids:
- w07-c-timer
- w07-c-index
- w07-c-btree
- w07-c-index-tradeoff
prev: w07-n08
next: w07-n10
order: 9
video:
  youtube_id: oqRU2So6Z2Y
  start: '1:41:49'
  start_seconds: 6109
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=6109s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'command called Timer'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# نمایه (index) و B-tree

> **منبع رسمی:** بخش «Indexes» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#indexes). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۱:۴۹ تا حدود ۱:۴۶:۳۰](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=6109s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پرس‌وجوی درست کافی نیست؛ وقتی میلیون‌ها سطر و هزاران کاربر داری، سرعت هم مهم است. شاخص (index) همان ایدهٔ درخت متوازن هفتهٔ ۵ است که پایگاه داده برایت می‌سازد، و این یادداشت هزینهٔ آن را هم نشان می‌دهد.

## شاخص‌ها

- پایگاه‌های دادهٔ رابطه‌ای می‌توانند سریع‌تر و مقاوم‌تر از فایل `CSV` باشند، و با **شاخص**ها می‌شود داده را درون جدول بهینه‌تر کرد.
- شاخص‌ها پرس‌وجوها را سریع‌تر می‌کنند.
- با اجرای `.timer on` در `sqlite3` می‌توانیم سرعت پرس‌وجوها را بسنجیم.
- برای دیدن اثر شاخص، اول این را اجرا کن و زمانی را که پس از اجرا نمایش داده می‌شود ببین:

```sql
SELECT * FROM shows WHERE title = 'The Office';
```

- بعد با این نحو یک شاخص می‌سازیم:

```sql
CREATE INDEX title_index ON shows (title);
```

- این فرمان به `sqlite3` می‌گوید شاخصی بسازد و برای ستون `title` بهینه‌سازی ویژه‌ای پشت صحنه انجام دهد.
- نتیجه ساختمان داده‌ای به نام **B-tree** است؛ ساختمان داده‌ای شبیه درخت دودویی، با این تفاوت که هر گره می‌تواند بیش از دو فرزند داشته باشد (درس‌نامه آن را با تصویری از درختی با گره‌های چندفرزندی نشان می‌دهد؛ پیوند در `media.json`).
- همچنین می‌توانیم این شاخص‌ها را بسازیم:

```sql
CREATE INDEX name_index ON people (name);
CREATE INDEX person_index ON stars (person_id);
```

- حالا این پرس‌وجو را اجرا کن؛ می‌بینی که خیلی سریع‌تر اجرا می‌شود:

```sql
SELECT title FROM shows WHERE id IN 
    (SELECT show_id FROM stars WHERE person_id = 
        (SELECT id FROM people WHERE name = 'Steve Carell'));
```

- متأسفانه شاخص‌گذاری همهٔ ستون‌ها فضای ذخیره‌سازی بیشتری مصرف می‌کند. پس برای سرعت بیشتر یک **بده‌بستان** وجود دارد.

> [!NOTE]
> **از سخنرانی**
> در سخنرانی، پرس‌وجوی `The Office` پیش از ساخت شاخص حدود 0.042 ثانیه طول می‌کشد. دیوید توضیح می‌دهد که حتی پرس‌وجوهای سریع هم ارزش بهینه‌سازی دارند وقتی بسیار پرتکرارند (مثل جست‌وجوی سریال در IMDb): کاربران خشنودتر می‌شوند و همان سخت‌افزار می‌تواند به کاربران بیشتری پاسخ دهد.

> [!TIP]
> **تألیفی: چرا این دو شاخص به پرس‌وجوی Steve Carell کمک می‌کنند**
> پرس‌وجوی درونی `WHERE name = 'Steve Carell'` روی `people.name` جست‌وجو می‌کند و پرس‌وجوی میانی `WHERE person_id = ...` روی `stars.person_id`. بدون شاخص، هر دو جست‌وجوی خطی‌اند (O(n))؛ با شاخص B-tree، پیدا کردن هر مقدار به‌طور تقریبی O(log n) می‌شود. `shows.id` کلید اصلی است و SQLite برای آن از قبل ساختار مرتب دارد. هزینه: فضای بیشتر، و کندتر شدن `INSERT` و `UPDATE`، چون هر شاخص هم باید به‌روز شود (استنتاجی، بر پایهٔ مستندات SQLite).

> [!TIP]
> **تألیفی: شاخص نتیجه را عوض نمی‌کند**
> ساخت شاخص فقط **سرعت** را تغییر می‌دهد، نه مجموعهٔ سطرهای نتیجه را. روی پایگاه دادهٔ نمونه، پرس‌وجوی Steve Carell پیش و پس از `CREATE INDEX` همان `The Office` را برمی‌گرداند (اجراشده روی جعبهٔ ساخت). اما ترتیب سطرها در پرس‌وجوی بدون `ORDER BY` ممکن است پس از ساخت شاخص عوض شود.

## اشتباه‌های رایج

- شاخص‌گذاری همهٔ ستون‌ها «برای احتیاط»؛ فضای بیشتر و درج کندتر.
- ساختن دوبارهٔ شاخص با همان نام؛ خطای `index title_index already exists` می‌گیری.
- انتظار اینکه شاخص پرس‌وجوی نادرست را درست کند.

## جمع‌بندی

- `.timer on` زمان هر پرس‌وجو را نشان می‌دهد.
- `CREATE INDEX name ON table (column);` یک B-tree روی ستون می‌سازد و جست‌وجو روی آن ستون را سریع‌تر می‌کند.
- بده‌بستان: سرعت خواندن در برابر فضای ذخیره‌سازی و هزینهٔ به‌روزرسانی.

## پیوندها

- قبلی: [پیوند جدول‌ها با JOIN](/kb/d/w07-n08)
- بعدی: [SQL در پایتون با کتابخانهٔ CS50](/kb/d/w07-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
