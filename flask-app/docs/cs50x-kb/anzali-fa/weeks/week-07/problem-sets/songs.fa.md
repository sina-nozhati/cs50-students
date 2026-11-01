---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-ps-songs
type: problem-set-guide
title: راهنمای آهنگ‌ها (Songs)
title_fa: آهنگ‌ها (Songs)
title_en: Songs
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/7/songs/
source_refs:
- src-pset-7-songs#implementation-details
- src-pset-7-songs#spotify-wrapped
- src-anzali-authored-7
- src-pset-7#what-to-do
- src-pset-7#when-to-do-it
concept_ids:
- w07-c-sqlite3-cli
- w07-c-schema
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
- w07-c-sql-file-pipe
problem_set_ref: weeks/week-07/problem-sets/songs.json
prev: w07-sh-sql
next: w07-ps-movies
order: 19
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای آهنگ‌ها (Songs)

> **منبع رسمی:** [Songs](https://cs50.harvard.edu/x/2026/psets/7/songs/) از پرابلم‌ست ۷ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

پایگاه دادهٔ `songs.db` داده‌های Spotify دربارهٔ ۱۰۰ آهنگ پرپخش سال ۲۰۱۸ و خوانندگانشان را دارد. کار تو نوشتن هشت پرس‌وجوی SQL در فایل‌های `1.sql` تا `8.sql` است که هر کدام به یک پرسش دربارهٔ این داده پاسخ می‌دهد.

پیش از نوشتن، `sqlite3 songs.db` را اجرا کن و با `.schema` دستورهای `CREATE TABLE` را ببین. صفحهٔ رسمی می‌گوید هر خواننده (`artist`) یک `id` و یک `name` دارد و هر آهنگ یک `name`، یک `artist_id` (همان `id` خواننده) و مقدارهایی برای danceability، energy، key، loudness، speechiness، valence، tempo و مدت (به میلی‌ثانیه) دارد.

در پایان، در `answers.txt` دربارهٔ «Audio Aura» در Spotify Wrapped فکر می‌کنی: این داده چه چیزی دربارهٔ یک شنونده می‌گوید و چه چیزی نمی‌گوید. این راهنما هیچ پرس‌وجوی پاسخی برای فایل‌های شماره‌دار ندارد. همهٔ ابزارهای لازم در یادداشت‌ها و درس‌های کوتاه این هفته روی پایگاه‌داده‌های ساختگی تمرین شده‌اند.

> **از سخنرانی و جلسه:** `SELECT`، `WHERE`، `ORDER BY`، `LIMIT`، `LIKE` و تابع‌ها در [یادداشت SELECT](/kb/d/w07-n03)؛ پرس‌وجوی تودرتو در [یادداشت IMDb](/kb/d/w07-n07)؛ `JOIN` در [یادداشت JOINها](/kb/d/w07-n08). [جلسهٔ حل تمرین](/kb/d/w07-sec) پرسش‌های Songs را زنده حل می‌کند؛ اگر می‌خواهی خودت حل کنی، اول پرس‌وجوهایت را بنویس (D57).

## خواسته‌های رسمی

1. برای هر مسئله یک پرس‌وجوی SQL بنویس که نتیجهٔ خواسته‌شده را بدهد؛ پاسخ باید **یک** پرس‌وجو باشد، هرچند می‌توانی پرس‌وجوهای دیگر را درون آن تودرتو کنی.
2. دربارهٔ `id` هیچ آهنگ یا خواننده‌ای فرض نکن؛ پرس‌وجو باید حتی اگر `id`ها فرق کنند درست باشد.
3. هر پرس‌وجو فقط دادهٔ لازم را برگرداند؛ اگر فقط نام آهنگ خواسته شده، ستون دیگری نیاور.
4. `1.sql`: نام همهٔ آهنگ‌های پایگاه داده (یک ستون).
5. `2.sql`: نام همهٔ آهنگ‌ها به ترتیب صعودی tempo (یک ستون).
6. `3.sql`: نام ۵ آهنگ طولانی‌تر، به ترتیب نزولی طول (یک ستون).
7. `4.sql`: نام آهنگ‌هایی که danceability، energy و valence هر سه بیشتر از 0.75 دارند (یک ستون).
8. `5.sql`: میانگین energy همهٔ آهنگ‌ها (یک ستون و یک سطر).
9. `6.sql`: نام آهنگ‌های Post Malone (یک ستون)، بدون فرض دربارهٔ `artist_id` او.
10. `7.sql`: میانگین energy آهنگ‌های Drake (یک ستون و یک سطر)، بدون فرض دربارهٔ `artist_id` او.
11. `8.sql`: نام آهنگ‌هایی که خوانندهٔ دیگری را همراه دارند؛ نام این آهنگ‌ها «feat.» دارد (یک ستون).
12. در `answers.txt` به دو پرسش Audio Aura پاسخ بده: اگر `songs.db` صد آهنگ برتر یک شنونده در ۲۰۱۸ باشد، aura او را چطور توصیف می‌کنی؟ و چرا این روش محاسبه ممکن است نمایندهٔ خوبی نباشد و چه روش بهتری پیشنهاد می‌کنی؟
13. `answers.txt` را همراه همهٔ فایل‌های `.sql` تحویل بده.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. صفحهٔ رسمی می‌گوید پس از `ls` باید ۸ فایل `.sql`، `songs.db` و `answers.txt` را ببینی. هر فایل `.sql` خالی است و قرار است یک پرس‌وجو در آن بنویسی.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/7/songs.zip
unzip songs.zip
rm songs.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd songs
ls
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- sqlite3: برنامهٔ خط فرمان SQLite — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- طرح‌واره (schema) و .schema / CREATE TABLE — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l01` (واحد `w07-l01-u03`)
- SELECT ... FROM ...: خواندن ستون‌ها از جدول — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- WHERE: فیلتر سطرها با عبارت بولی — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- ترکیب شرط‌ها با AND و OR — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- ORDER BY با ASC و DESC — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u03`)
- LIMIT: محدود کردن تعداد سطرها — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- تابع‌های SQL: COUNT، AVG، MIN، MAX، LOWER، UPPER، DISTINCT — [یادداشت](/kb/d/w07-n02) · درس کوتاه `w07-l02` (واحد `w07-l02-u01`)
- LIKE و % برای الگو — [یادداشت](/kb/d/w07-n03) · درس کوتاه `w07-l02` (واحد `w07-l02-u02`)
- پرس‌وجوی تودرتو با IN (SELECT ...) — [یادداشت](/kb/d/w07-n07) · درس کوتاه `w07-l04` (واحد `w07-l04-u03`)
- JOIN ... ON: ترکیب دو جدول با کلید مشترک — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u01`)
- نام کامل ستون: table.column — [یادداشت](/kb/d/w07-n08) · درس کوتاه `w07-l05` (واحد `w07-l05-u01`)
- فرض نکردن id ثابت؛ پیدا کردن id با پرس‌وجو — [یادداشت](/kb/d/w07-ps-songs)
- اجرای فایل پرس‌وجو: cat N.sql | sqlite3 db — [یادداشت](/kb/d/w07-ps-movies)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. `.schema` را اجرا کن و برای هر پرسش اول بنویس به کدام جدول و کدام ستون‌ها نیاز داری. اگر همهٔ داده در یک جدول است، `JOIN` لازم نیست.
2. برای هر پرسش، کلیدواژه‌ها را از متن آن پیدا کن: «به ترتیب» یعنی کدام بند؟ «۵ تا» یعنی کدام بند؟ «میانگین» کدام تابع است؟ یادداشت SELECT همه را دارد.
3. وقتی پرسش با نام یک خواننده است ولی جدول آهنگ‌ها فقط `artist_id` دارد، دو راه داری: پرس‌وجوی تودرتو یا `JOIN`. هر دو را روی پایگاه دادهٔ ساختگی درس‌های کوتاه تمرین کرده‌ای.
4. پرس‌وجوی درونی را اول جدا اجرا کن و ببین دقیقاً یک مقدار برمی‌گرداند یا چند تا. اگر ممکن است چند مقدار باشد، `IN` امن‌تر از `=` است.
5. برای تطبیق بخشی از یک رشته، `LIKE` و `%` را در یادداشت SELECT مرور کن. به جای `%` در ابتدا، انتها یا دو طرف فکر کن.
6. هر پرس‌وجو را در یک فایل ذخیره کن و با `cat N.sql | sqlite3 songs.db` اجرا کن تا مطمئن شوی فایل همان چیزی است که در اعلان آزموده‌ای.

## اشتباه‌های رایج

- نوشتن عدد `id` یک خواننده در پرس‌وجو (خواستهٔ رسمی صریحاً منع می‌کند)
- برگرداندن ستون‌های اضافه مثل tempo کنار نام
- فراموش کردن `DESC` وقتی ترتیب نزولی خواسته شده
- استفاده از `OR` به جای `AND` وقتی هر سه شرط باید برقرار باشند
- نوشتن دو پرس‌وجو در یک فایل
- خالی گذاشتن `answers.txt`

## چک‌لیست خودآزمایی

1. هر فایل `.sql` فقط یک پرس‌وجو دارد (تودرتو مجاز است).
2. در هیچ پرس‌وجویی عدد `id` را دستی ننوشته‌ام؛ `id` را از روی نام پیدا می‌کنم.
3. هر پرس‌وجو فقط ستون‌های خواسته‌شده را برمی‌گرداند.
4. جهت مرتب‌سازی (`2.sql` صعودی، `3.sql` نزولی) با خواستهٔ رسمی می‌خواند.
5. `5.sql` و `7.sql` یک ستون و یک سطر برمی‌گردانند.
6. هر پرس‌وجو را در `sqlite3 songs.db` اجرا کرده و نتیجه را با پرسش سنجیده‌ام.
7. به هر دو پرسش `answers.txt` پاسخ داده‌ام.
8. check50 همه را سبز نشان می‌دهد.
9. همهٔ فایل‌ها را با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/songs
```

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/songs
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [بخش Hints صفحهٔ رسمی Songs](https://cs50.harvard.edu/x/psets/7/songs/#hints): هر بلوک این بخش پرس‌وجوی کامل یکی از فایل‌های شماره‌دار را نشان می‌دهد (d123، D56)؛ در این بسته بازنویسی نشده است.
- [ویدئوی راهنمای گام‌به‌گام](https://video.cs50.io/wgKPUd_95AA): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/wgKPUd_95AA)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/DsiNSGFrMq2J6t9aDYhIQUQHy)

## پیوند رسمی

- [Songs](https://cs50.harvard.edu/x/2026/psets/7/songs/)
- [پرابلم‌ست ۷](https://cs50.harvard.edu/x/psets/7/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
