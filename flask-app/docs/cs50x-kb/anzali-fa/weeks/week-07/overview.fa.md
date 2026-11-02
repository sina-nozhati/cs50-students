---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-fa
type: week-overview
title: هفتهٔ ۷ — SQL (پایگاه دانش فارسی)
title_fa: هفتهٔ ۷ — SQL
title_en: Week 7 — SQL
parent: week-7
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/7/
source_refs:
- src-week-7#week-7-sql
- src-notes-7#lecture-7
- src-pset-7#what-to-do
- src-pset-7#when-to-do-it
- src-pset-7#advice
- src-short-sql
- src-anzali-authored-7
- src-anzali-inference-7
children:
- w07-n01
- w07-n02
- w07-n03
- w07-n04
- w07-n05
- w07-n06
- w07-n07
- w07-n08
- w07-n09
- w07-n10
- w07-n11
- w07-n12
- w07-summary
- w07-sec
- w07-sh-sql
- w07-ps-songs
- w07-ps-movies
- w07-ps-fiftyville
- w07-pr-favorites
- w07-pr-prophecy
objective_ids:
- w07-o01
- w07-o02
- w07-o03
- w07-o04
- w07-o05
- w07-o06
- w07-o07
- w07-o08
- w07-o09
- w07-o10
---

# هفتهٔ ۷ — SQL

> **منبع رسمی:** [صفحهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/weeks/7/) و [درس‌نامهٔ هفتهٔ ۷](https://cs50.harvard.edu/x/notes/7/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

هفتهٔ گذشته پایتون را یاد گرفتی. این هفته سراغ **داده** می‌روی. هفته با یک فایل CSV از پاسخ‌های دانشجویان شروع می‌شود: آن را با پایتون می‌خوانی، با واژه‌نامه می‌شماری و با `sorted` مرتب می‌کنی. بعد همان داده را در یک **پایگاه دادهٔ رابطه‌ای** می‌گذاری و با **SQL** همین پرسش‌ها را در یک خط پاسخ می‌دهی: `SELECT`، `WHERE`، `LIKE`، `GROUP BY`، `ORDER BY` و `LIMIT`؛ و داده را با `INSERT`، `DELETE` و `UPDATE` تغییر می‌دهی.

سپس پایگاه دادهٔ سریال‌های IMDb نشان می‌دهد چرا داده را در چند جدول می‌شکنیم: **کلید اصلی**، **کلید خارجی**، رابطه‌های یک‌به‌یک، یک‌به‌چند و چندبه‌چند، و دو راه رسیدن از جدولی به جدول دیگر: **پرس‌وجوی تودرتو** و **`JOIN`**. با **شاخص** (B-tree) پرس‌وجوها سریع‌تر می‌شوند، به بهای فضای بیشتر. در پایان SQL را درون پایتون با کتابخانهٔ CS50 اجرا می‌کنی و با دو خطر واقعی آشنا می‌شوی: **شرایط رقابتی** (و تراکنش‌ها) و **تزریق SQL** (و جای‌نگهدار `?`).

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

SQL: جدول‌ها؛ نوع‌ها؛ دستورها؛ قیدها؛ شاخص‌ها؛ کلیدواژه‌ها، تابع‌ها؛ تراکنش‌ها. شرایط رقابتی. حمله‌های تزریق SQL (SQL: Tables; Types; Statements; Constraints; Indexes; Keywords, Functions; Transactions. Race Conditions. SQL Injection Attacks.)

> **توجه:** صفحهٔ هفته یک ویدئوی کوتاه («SQL»، Doug Lloyd) فهرست می‌کند که در سال ۲۰۱۷ و برای مجموعهٔ «توسعهٔ وب» ضبط شده و نمونه‌هایش با MySQL و phpMyAdmin است (d126 در `sources.json`).

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه، سخنرانی، جلسهٔ حل تمرین و پرابلم‌ست ۷ استخراج کرده است.

- **w07-o01** — فایل CSV را با `csv.reader` و `csv.DictReader` بخوانی، با واژه‌نامه بشماری و با `sorted(..., key=..., reverse=True)` مرتب کنی.
- **w07-o02** — پایگاه دادهٔ رابطه‌ای، CRUD و نقش `sqlite3` را توضیح بدهی و با `.mode csv`، `.import` و `.schema` کار کنی.
- **w07-o03** — با `SELECT`، `WHERE`، `AND`، `OR`، `LIKE`، `COUNT`، `DISTINCT`، `GROUP BY`، `ORDER BY`، `AS` و `LIMIT` پرس‌وجو بنویسی و نتیجه‌اش را پیش‌بینی کنی.
- **w07-o04** — با `INSERT`، `DELETE` و `UPDATE` داده را تغییر بدهی، `IS NULL` را درست به کار ببری و خطر نبودن `WHERE` را بشناسی.
- **w07-o05** — طراحی چندجدولی، کلید اصلی و خارجی، نوع‌ها و قیدهای SQLite را توضیح بدهی.
- **w07-o06** — با پرس‌وجوی تودرتو (`IN`) و `JOIN ... ON` داده را از دو یا چند جدول بخوانی و رابطه‌های یک‌به‌یک، یک‌به‌چند و چندبه‌چند را تشخیص بدهی.
- **w07-o07** — کار شاخص و B-tree و بده‌بستان آن را توضیح بدهی.
- **w07-o08** — SQL را با `from cs50 import SQL` و `db.execute` در پایتون اجرا کنی و خروجی آن را (فهرستی از واژه‌نامه‌ها) به کار ببری.
- **w07-o09** — شرایط رقابتی را توضیح بدهی و نقش `BEGIN TRANSACTION`، `COMMIT` و `ROLLBACK` را بگویی.
- **w07-o10** — حملهٔ تزریق SQL را تشخیص بدهی و آن را با جای‌نگهدار `?` جلوگیری کنی.

## پیش‌نیازها

- هفتهٔ ۳: جست‌وجوی خطی و دودویی و نماد O بزرگ. ([نمای کلی هفتهٔ ۳](/kb/d/w03-fa))
- هفتهٔ ۵: درخت، درخت متوازن و جدول درهم‌سازی. ([نمای کلی هفتهٔ ۵](/kb/d/w05-fa))
- هفتهٔ ۶: پایتون، واژه‌نامه، فهرستی از واژه‌نامه‌ها، `try`/`except` و ماژول `csv`. ([نمای کلی هفتهٔ ۶](/kb/d/w06-fa))

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: از CSV به پایگاه داده
  csv.reader -> DictReader -> شمارش با dict -> sorted -> sqlite3 و .import -> .schema

مرحلهٔ ۲: خواندن با SELECT
  SELECT و * -> WHERE، AND، OR -> LIKE و % -> COUNT و DISTINCT -> GROUP BY -> ORDER BY، AS، LIMIT

مرحلهٔ ۳: تغییر داده
  INSERT -> NULL و IS NULL -> DELETE -> UPDATE -> خطر نبودن WHERE

مرحلهٔ ۴: طراحی چندجدولی
  تکرار داده -> کلید اصلی -> کلید خارجی -> نوع‌ها و قیدها -> پرس‌وجوی تودرتو

مرحلهٔ ۵: پیوند جدول‌ها
  JOIN ... ON -> یک‌به‌چند -> چندبه‌چند -> JOIN سه‌جدولی و ضمنی

مرحلهٔ ۶: سرعت و پایتون
  .timer -> CREATE INDEX -> B-tree و بده‌بستان -> cs50.SQL و db.execute

مرحلهٔ ۷: ایمنی
  شرایط رقابتی -> تراکنش -> تزریق SQL -> جای‌نگهدار ?
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۲ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران (۷ درس).
3. ویدئوی کوتاه [SQL](/kb/d/w07-sh-sql) را پس از یادداشت IMDb ببین.
4. [جلسهٔ حل تمرین (Section)](/kb/d/w07-sec) را پیش از پرابلم‌ست ببین؛ اما بدان که نیمهٔ دوم آن پرسش‌های Songs را زنده حل می‌کند (پایین‌تر را ببین).
5. چالش‌های کوتاه هفته را امتحان کن، آزمون تسلط را بده و بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۷

طبق صفحهٔ رسمی پرابلم‌ست ۷:

- [Songs](/kb/d/w07-ps-songs) را **تحویل بده**.
- [Movies](/kb/d/w07-ps-movies) را **تحویل بده**.
- [Fiftyville](/kb/d/w07-ps-fiftyville) را **تحویل بده**.
- پیش از شروع، `update50` را در codespace اجرا کن و وقتی پرسیده شد، **Rebuild now** را بزن.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

مسئله‌های تمرینی اختیاری: [Favorites](/kb/d/w07-pr-favorites) و [Hall of Prophecy](/kb/d/w07-pr-prophecy). هر دو در صفحهٔ خودشان می‌گویند check50 ندارند و تحویل لازم نیست.

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود: نه پرس‌وجوی پاسخ هیچ‌کدام از فایل‌های شماره‌دار Songs و Movies، نه لاگ یا پاسخ Fiftyville (دزد، شهر، همدست)، و نه دنباله‌ای از پرس‌وجوها که معما را حل کند. بخش «Hints» صفحه‌های رسمی Songs و Movies و نیمهٔ دوم جلسهٔ حل تمرین، پاسخ چند پرسش را مستقیم نشان می‌دهند؛ این بسته آن‌ها را بازنویسی نمی‌کند و فقط پیوند می‌دهد (D56، D57). همهٔ تمرین‌های SQL این بسته روی پایگاه‌داده‌های ساختگی خودش (`weeks/week-07/fixtures/`) اجرا می‌شوند، نه روی `songs.db`، `movies.db` یا `fiftyville.db` (D59).

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی هر سه پرابلم‌ست کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۷](https://cs50.harvard.edu/x/weeks/7/) · [درس‌نامه](https://cs50.harvard.edu/x/notes/7/) · [ویدئوی سخنرانی](https://video.cs50.io/oqRU2So6Z2Y)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/7/lecture7.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/7/src7.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.srt)
- [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/7/) · [پرابلم‌ست ۷](https://cs50.harvard.edu/x/psets/7/) · [مرجع SQL در w3schools](https://www.w3schools.com/sql/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
