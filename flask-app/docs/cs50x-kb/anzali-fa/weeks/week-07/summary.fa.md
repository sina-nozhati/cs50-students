---
week: 7
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
generated_at: '2026-10-29T06:00:00+03:30'
review_status: draft-needs-human-review
id: w07-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۷ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۷
title_en: Summing Up
parent: w07-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; quick-review table and outlook are authored. Designed to replace the English official summary on /kb/week/7 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/7/#summing-up
source_refs:
- src-notes-7#summing-up
- src-week-7#week-7-sql
- src-anzali-authored-7
prev: w07-n12
next: w07-sec
order: 16
replaces_official_summary_for: week-7
---

# خلاصهٔ هفتهٔ ۷: SQL

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۷](https://cs50.harvard.edu/x/notes/7/#summing-up) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس نحو بیشتری از پایتون یاد گرفتی. همچنین یاد گرفتی این دانش را با داده، به شکل پایگاه‌داده‌های تخت و رابطه‌ای، ترکیب کنی. در پایان با **SQL** آشنا شدی. به‌طور مشخص این‌ها را دیدی:

- پایگاه‌داده‌های تخت.
- پایگاه‌داده‌های رابطه‌ای.
- فرمان‌های SQL مثل `SELECT`، `CREATE`، `INSERT`، `DELETE` و `UPDATE`.
- کلیدهای اصلی و خارجی.
- `JOIN`ها.
- شاخص‌ها.
- استفاده از SQL در پایتون.
- شرایط رقابتی.
- حمله‌های تزریق SQL.

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| پایگاه دادهٔ تخت | یک جدول در یک فایل متنی مثل CSV؛ `csv.DictReader` سطرها را dict می‌کند. | [پایگاه دادهٔ تخت](/kb/d/w07-n01) |
| sqlite3 | `sqlite3 file.db`، `.mode csv`، `.import` و `.schema`. | [پایگاه دادهٔ رابطه‌ای](/kb/d/w07-n02) |
| SELECT | `SELECT columns FROM table WHERE ... GROUP BY ... ORDER BY ... LIMIT n;` | [SELECT](/kb/d/w07-n03) |
| INSERT | `INSERT INTO table (columns) VALUES (values);` ستون نام‌برده‌نشده `NULL` می‌شود. | [INSERT](/kb/d/w07-n04) |
| DELETE | `DELETE FROM table WHERE ...;` برای NULL از `IS NULL` استفاده کن. | [DELETE](/kb/d/w07-n05) |
| UPDATE | `UPDATE table SET col = value WHERE ...;` بدون `WHERE` همهٔ سطرها. | [UPDATE](/kb/d/w07-n06) |
| کلید اصلی و خارجی | کلید اصلی سطر را یکتا می‌کند؛ کلید خارجی به کلید اصلی جدول دیگر اشاره می‌کند. | [IMDb](/kb/d/w07-n07) |
| پرس‌وجوی تودرتو | `WHERE id IN (SELECT ...)` نتیجهٔ یک پرس‌وجو را در دیگری به کار می‌برد. | [IMDb](/kb/d/w07-n07) |
| JOIN | `JOIN b ON a.id = b.a_id` جدول‌ها را موقتاً کنار هم می‌گذارد. | [JOINها](/kb/d/w07-n08) |
| شاخص | `CREATE INDEX name ON table (column);` یک B-tree؛ خواندن سریع‌تر، فضای بیشتر. | [شاخص‌ها](/kb/d/w07-n09) |
| SQL در پایتون | `db = SQL("sqlite:///file.db")` و `db.execute(sql, args)`؛ `SELECT` فهرستی از dict برمی‌گرداند. | [SQL در پایتون](/kb/d/w07-n10) |
| شرایط رقابتی | کارهای هم‌زمان؛ `BEGIN TRANSACTION`، `COMMIT`، `ROLLBACK`. | [شرایط رقابتی](/kb/d/w07-n11) |
| تزریق SQL | ورودی کاربر نباید بخشی از کد SQL شود؛ همیشه `?`. | [تزریق SQL](/kb/d/w07-n12) |

## بعد از این هفته

> **تألیفی:** هفتهٔ ۸ دربارهٔ HTML، CSS و JavaScript است و هفتهٔ ۹ پایتون و SQL این هفته را با Flask در یک برنامهٔ وب ترکیب می‌کند. `db.execute` با جای‌نگهدار `?` در آنجا هم همان است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
