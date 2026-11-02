---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۷ (Section 7)
title_fa: جلسهٔ حل تمرین هفتهٔ ۷
title_en: Section 7
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly, read in full); chapter times from section7.srt (inference for boundaries); Songs answer queries written live in the section are NOT reproduced (D57); source-code link is a 404 (d119); note on renumbering ids is authored
source_url: https://cs50.harvard.edu/x/sections/7/
source_refs:
- src-section-7#week-7-sql
- src-section-7-transcript
- src-section-7-video
- src-section-7-slides
- src-section-7-code
- src-sqlite-docs
- src-anzali-inference-7
- src-anzali-authored-7
concept_ids:
- w07-c-relational-db
- w07-c-redundancy
- w07-c-primary-key
- w07-c-foreign-key
- w07-c-sqlite3-cli
- w07-c-schema
- w07-c-constraints
- w07-c-insert
- w07-c-update
- w07-c-delete
- w07-c-missing-where-danger
- w07-c-backups-permissions
- w07-c-select
- w07-c-where
- w07-c-and-or
- w07-c-order-by
- w07-c-limit
- w07-c-sql-functions
- w07-c-like-wildcard
- w07-c-nested-query
- w07-c-join
- w07-c-qualified-column
- w07-c-no-id-assumption
- w07-c-string-literal-quotes
- w07-c-sql-style
prev: w07-summary
next: w07-sh-sql
order: 17
video:
  youtube_id: g1gKEPqikOE
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'خوش‌آمد: پایگاه داده دربارهٔ آدم‌هاست'
    evidence_en: null
  - start: '3:31'
    start_seconds: 211
    title_fa: 'اصول طراحی: یک موجودیت، یک جا، کلید اصلی'
    evidence_en: quick design principles
  - start: '6:23'
    start_seconds: 383
    title_fa: ساختن friends.db با sqlite3
    evidence_en: database called Friends
  - start: '7:36'
    start_seconds: 456
    title_fa: CREATE TABLE با نوع، NOT NULL و PRIMARY KEY
    evidence_en: syntax for creating a new table
  - start: '10:52'
    start_seconds: 652
    title_fa: INSERT INTO
    evidence_en: we can use insert into
  - start: '13:53'
    start_seconds: 833
    title_fa: UPDATE ... SET ... WHERE
    evidence_en: now I want to update it
  - start: '16:11'
    start_seconds: 971
    title_fa: DELETE و هشدار نسخهٔ پشتیبان
    evidence_en: also want to delete things sometimes
  - start: '18:17'
    start_seconds: 1097
    title_fa: تغییر id پس از حذف
    evidence_en: when I deleted Bob
  - start: '19:00'
    start_seconds: 1140
    title_fa: SELECT و WHERE
    evidence_en: move to select queries
  - start: '20:14'
    start_seconds: 1214
    title_fa: 'شروع Songs: ساختار songs.db'
    evidence_en: first part of the problem set
  - start: '23:35'
    start_seconds: 1415
    title_fa: LIKE و %
    evidence_en: ways you can do this by using this percent
  - start: '39:49'
    start_seconds: 2389
    title_fa: تابع‌های تجمیعی
    evidence_en: So we have aggregating
  - start: '45:33'
    start_seconds: 2733
    title_fa: پرس‌وجوی تودرتو
    evidence_en: nested selects to be specific
  - start: '51:49'
    start_seconds: 3109
    title_fa: JOIN ... ON
    evidence_en: So let's talk about joints
  - start: '54:15'
    start_seconds: 3255
    title_fa: 'JOIN یا تودرتو: کدام سریع‌تر؟'
    evidence_en: joins are typically going to be
  - start: '56:07'
    start_seconds: 3367
    title_fa: تمرین تودرتو و JOIN روی Songs
    evidence_en: practice here with nested selects and joints
  - start: '1:03:40'
    start_seconds: 3820
    title_fa: نقل‌قول تکی یا دوتایی
    evidence_en: the single quote versus the double quotes
  chapters_origin: inference
code_files:
- file: songs (section source link)
  policy: unavailable
  reason: official link https://cs50.harvard.edu/x/sections/psets/7/songs returned HTTP 404 (d119)
- file: section7.pdf
  policy: link-only
  reason: slides; contain Songs walkthrough (D57)
---

# جلسهٔ حل تمرین هفتهٔ ۷ (Section)

> **منبع رسمی:** [صفحهٔ Section 7 CS50x](https://cs50.harvard.edu/x/sections/7/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/7/lang/en/section7.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، مدرس (preceptor) CS50 در هاروارد، اداره می‌کند و سه بخش دارد: اصول طراحی پایگاه داده، ساختن یک پایگاه دادهٔ کوچک با چهار فرمان CRUD، و کار روی پرابلم‌ست Songs.

بخش اول دربارهٔ این است که **پایگاه داده دربارهٔ آدم‌هاست**. Kelly چرخهٔ داده را مرور می‌کند (از چه کسی و چطور داده جمع می‌کنیم، چطور ذخیره‌اش می‌کنیم و دیگران چطور از آن استفاده می‌کنند) و می‌پرسد انتخاب‌های طراحی چطور می‌توانند روی آدم‌های پشت داده اثر بگذارند، مثلاً با کنار گذاشتن ناخواستهٔ بعضی گروه‌ها در شیوهٔ نمایش داده. بعد دو اصل طراحی می‌آید: هر جدول باید مجموعه‌ای از **یک نوع موجودیت** باشد (مثلاً جدول کارمندان جدا از جدول رابطه‌های میان کارمندان)، و هر تکه داده باید **فقط در یک جا** ذخیره شود و بعد با **شناسه** (کلید اصلی) به آن ارجاع داده شود؛ چون ممکن است دو کارمند هر دو Alice باشند.

بخش دوم پایگاه دادهٔ `friends.db` است. Kelly با `sqlite3` آن را می‌سازد و پرسش ساخت فایل را تأیید می‌کند. `.schema` اول چیزی نشان نمی‌دهد، چون پایگاه داده خالی است. بعد با `CREATE TABLE` جدولی به نام `friend` با ستون‌های `id`، `name` و `age` می‌سازد، همراه با نوع هر ستون، قید `NOT NULL` و `PRIMARY KEY` روی `id`. با `INSERT INTO` سه دوست (Alice، Bob و Charlie) را اضافه می‌کند و نشان می‌دهد که لازم نیست `id` را بدهی؛ کلید اصلی خودش شمرده می‌شود. با `UPDATE ... SET ... WHERE` سن Alice را عوض می‌کند و یادآوری می‌کند که بدون `WHERE` همهٔ سطرها تغییر می‌کنند. با `DELETE FROM ... WHERE` سطر Bob را حذف می‌کند و هشدار می‌دهد که حذف ویرانگر است و نسخهٔ پشتیبان مهم است. در پاسخ به پرسش‌ها می‌گوید کلید اصلی یک جدول می‌تواند در جدول دیگر کلید خارجی باشد.

بخش سوم **پرابلم‌ست Songs** است. Kelly ساختار `songs.db` (جدول‌های `songs` و `artists`) را توضیح می‌دهد و ابزارهای `SELECT` را یکی‌یکی معرفی می‌کند: انتخاب ستون، `WHERE` با `AND` و `OR`، `ORDER BY` (صعودی پیش‌فرض است)، `LIMIT`، تابع‌های تجمیعی مثل `AVG` و `COUNT`، `LIKE` با `%` در ابتدا، انتها یا دو طرف الگو، پرس‌وجوی تودرتو برای پیدا کردن `id` بدون حدس زدن آن، و `JOIN ... ON` با نام کامل ستون (`table.column`). او این ابزارها را مستقیم روی فایل‌های شماره‌دار Songs به کار می‌برد.

> **سیاست این بسته (D57):** نیمهٔ دوم جلسه پرس‌وجوهای پاسخ چند فایل Songs را زنده می‌نویسد. این خلاصه آن پرس‌وجوها را بازنویسی نمی‌کند؛ اگر می‌خواهی خودت Songs را حل کنی، پیش از دیدن این بخش از ویدئو، پرس‌وجوهایت را بنویس و بعد مقایسه کن. همهٔ ابزارهای این بخش در یادداشت‌ها و درس‌های کوتاه این بسته با پایگاه‌داده‌های ساختگی تمرین شده‌اند.

در پایان، در پاسخ به پرسش‌ها، Kelly می‌گوید JOINها معمولاً کمی کندتر از SELECTهای تودرتو هستند ولی بستگی دارد، و تفاوت نقل‌قول تکی و دوتایی را مسئلهٔ سبک می‌داند، به شرط یکدست بودن.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section7.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — خوش‌آمد: پایگاه داده دربارهٔ آدم‌هاست](https://www.youtube.com/watch?v=g1gKEPqikOE&t=0s)
- [۳:۳۱ — اصول طراحی: یک موجودیت، یک جا، کلید اصلی](https://www.youtube.com/watch?v=g1gKEPqikOE&t=211s)
- [۶:۲۳ — ساختن friends.db با sqlite3](https://www.youtube.com/watch?v=g1gKEPqikOE&t=383s)
- [۷:۳۶ — CREATE TABLE با نوع، NOT NULL و PRIMARY KEY](https://www.youtube.com/watch?v=g1gKEPqikOE&t=456s)
- [۱۰:۵۲ — INSERT INTO](https://www.youtube.com/watch?v=g1gKEPqikOE&t=652s)
- [۱۳:۵۳ — UPDATE ... SET ... WHERE](https://www.youtube.com/watch?v=g1gKEPqikOE&t=833s)
- [۱۶:۱۱ — DELETE و هشدار نسخهٔ پشتیبان](https://www.youtube.com/watch?v=g1gKEPqikOE&t=971s)
- [۱۸:۱۷ — تغییر id پس از حذف](https://www.youtube.com/watch?v=g1gKEPqikOE&t=1097s)
- [۱۹:۰۰ — SELECT و WHERE](https://www.youtube.com/watch?v=g1gKEPqikOE&t=1140s)
- [۲۰:۱۴ — شروع Songs: ساختار songs.db](https://www.youtube.com/watch?v=g1gKEPqikOE&t=1214s)
- [۲۳:۳۵ — LIKE و %](https://www.youtube.com/watch?v=g1gKEPqikOE&t=1415s)
- [۳۹:۴۹ — تابع‌های تجمیعی](https://www.youtube.com/watch?v=g1gKEPqikOE&t=2389s)
- [۴۵:۳۳ — پرس‌وجوی تودرتو](https://www.youtube.com/watch?v=g1gKEPqikOE&t=2733s)
- [۵۱:۴۹ — JOIN ... ON](https://www.youtube.com/watch?v=g1gKEPqikOE&t=3109s)
- [۵۴:۱۵ — JOIN یا تودرتو: کدام سریع‌تر؟](https://www.youtube.com/watch?v=g1gKEPqikOE&t=3255s)
- [۵۶:۰۷ — تمرین تودرتو و JOIN روی Songs](https://www.youtube.com/watch?v=g1gKEPqikOE&t=3367s)
- [۱:۰۳:۴۰ — نقل‌قول تکی یا دوتایی](https://www.youtube.com/watch?v=g1gKEPqikOE&t=3820s)

## کد رسمی جلسه

صفحهٔ جلسه برای «Source Code» فقط پیوند `Songs` به `https://cs50.harvard.edu/x/sections/psets/7/songs` را دارد که هنگام بررسی (۲۰۲۶-۱۰-۲۹) خطای HTTP 404 داد (d119). اسلایدهای جلسه به شکل [PDF](https://cdn.cs50.net/2025/fall/sections/7/section7.pdf) در دسترس‌اند (فقط پیوند).

> [!NOTE]
> **یادداشت**
> سه گفتهٔ جلسه با مستندات SQLite دقیق‌تر می‌شوند: SQLite علاوه بر `JOIN` پیوندهای `LEFT JOIN` و `CROSS JOIN` هم دارد (d120)؛ سرعت JOIN و پرس‌وجوی تودرتو بیشتر به طرح پرس‌وجو و شاخص‌ها بستگی دارد (d122)؛ و نقل‌قول دوتایی در SQLite برای نام ستون است و فقط وقتی چنین ستونی نباشد رشته حساب می‌شود (d121).

> **تألیفی: دربارهٔ تغییر id پس از حذف**
> در جلسه پس از حذف Bob، `id` سطر Charlie با `UPDATE` به `2` تغییر داده می‌شود تا شماره‌ها پشت سر هم بمانند. در جدول تنها این کار بی‌خطر است، اما وقتی جدول دیگری با کلید خارجی به این `id` اشاره می‌کند (مثل `stars.person_id` در IMDb)، تغییر کلید اصلی آن ارجاع‌ها را می‌شکند. شکاف در شماره‌ها مشکلی نیست؛ کلید اصلی فقط باید یکتا و پایدار باشد.

## نکته‌های کلیدی

- هر جدول یک نوع موجودیت؛ هر تکه داده در یک جا، با ارجاع از راه کلید اصلی.
- `CREATE TABLE` با نوع، `NOT NULL` و `PRIMARY KEY`؛ `.schema` برای دیدن نتیجه.
- `INSERT`، `UPDATE` و `DELETE` بدون `WHERE` (برای دو تای آخر) روی همهٔ سطرها اثر دارند.
- `ORDER BY` صعودی پیش‌فرض است؛ `DESC` برای نزولی.
- `LIKE 'x%'` با x شروع می‌شود، `'%x'` با x تمام می‌شود و `'%x%'` x را جایی در خود دارد.
- `id` را حدس نزن؛ آن را با پرس‌وجوی تودرتو یا `JOIN` از روی نام پیدا کن.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
