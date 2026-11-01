---
id: w07-n04
type: note
title: افزودن سطر با INSERT (INSERT)
title_fa: افزودن سطر با INSERT
title_en: INSERT
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: INSERT
official_anchor: insert
source_url: https://cs50.harvard.edu/x/2026/notes/7/#insert
source_refs:
- src-notes-7#insert
- src-transcript-7
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-insert
- w07-c-null
prev: w07-n03
next: w07-n05
order: 4
video:
  youtube_id: oqRU2So6Z2Y
  start: '46:07'
  start_seconds: 2767
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=2767s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'You literally say insert into'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# افزودن سطر با INSERT

> **منبع رسمی:** بخش «INSERT» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#insert). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۶:۰۷ تا حدود ۴۷:۲۲](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=2767s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا فقط داده را **خواندیم** (حرف R در CRUD). `INSERT` حرف C است: افزودن سطر تازه. هر فرم ثبت‌نام و هر «پست جدید» در یک برنامهٔ وب در نهایت یک `INSERT` است و هفتهٔ ۹ دقیقاً همین را با Flask انجام می‌دهی.

## INSERT

- با این شکل کلی می‌توانیم در پایگاه دادهٔ SQL سطر تازه **درج** کنیم:

```sql
INSERT INTO table (column...) VALUES(value, ...);
```

- برای نمونه می‌توانیم این را اجرا کنیم:

```sql
INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');
```

- با اجرای `SELECT * FROM favorites;` می‌توانی بررسی کنی که این علاقه‌مندی اضافه شده است.

> [!TIP]
> **تألیفی: ستونی که نام نبری NULL می‌شود**
> در `INSERT` بالا ستون `Timestamp` نام برده نشده است، پس مقدار آن در سطر تازه `NULL` (نبود مقدار) می‌شود. روی پایگاه دادهٔ نمونه، پس از این `INSERT`، پرس‌وجوی `SELECT COUNT(*) FROM favorites WHERE "Timestamp" IS NULL;` عدد `2` می‌دهد: یک سطر از قبل بی‌زمان بود و سطر تازه هم بی‌زمان است (اجراشده روی جعبهٔ ساخت). سخنرانی همین را «دوست قدیمی‌مان null» می‌نامد و در یادداشت بعدی با `DELETE` از آن استفاده می‌کند.

> [!TIP]
> **تألیفی: ترتیب ستون‌ها و مقدارها**
> مقدارها به ترتیب ستون‌هایی که در پرانتز اول آمده‌اند نسبت داده می‌شوند. `VALUES ('Fiftyville', 'SQL')` بدون خطا اجرا می‌شود، اما زبان را `Fiftyville` و مسئله را `SQL` ذخیره می‌کند. SQL نوع داده را در این حالت بررسی نمی‌کند، پس این اشتباه فقط با خواندن دوبارهٔ داده دیده می‌شود.

## اشتباه‌های رایج

- برابر نبودن تعداد ستون‌ها و مقدارها؛ SQLite خطا می‌دهد (`2 values for 1 columns` و مانند آن).
- جابه‌جا نوشتن مقدارها نسبت به ستون‌ها.
- نوشتن رشته با نقل‌قول دوتایی؛ در این بسته رشته‌ها همیشه نقل‌قول تکی دارند.

## جمع‌بندی

- `INSERT INTO table (columns) VALUES (values);` یک سطر تازه می‌سازد.
- ستونی که نام برده نشود `NULL` می‌شود (مگر مقدار پیش‌فرض داشته باشد).
- بعد از درج، با `SELECT` نتیجه را بررسی کن.

## پیوندها

- قبلی: [خواندن داده با SELECT](/kb/d/w07-n03)
- بعدی: [حذف سطر با DELETE و NULL](/kb/d/w07-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
