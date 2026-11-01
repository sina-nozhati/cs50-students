---
id: w07-n06
type: note
title: تغییر داده با UPDATE (UPDATE)
title_fa: تغییر داده با UPDATE
title_en: UPDATE
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: UPDATE
official_anchor: update
source_url: https://cs50.harvard.edu/x/2026/notes/7/#update
source_refs:
- src-notes-7#update
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-update
- w07-c-missing-where-danger
- w07-c-backups-permissions
prev: w07-n05
next: w07-n07
order: 6
video:
  youtube_id: oqRU2So6Z2Y
  start: '50:26'
  start_seconds: 3026
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=3026s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'update favorites,'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# تغییر داده با UPDATE

> **منبع رسمی:** بخش «UPDATE» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#update). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۰:۲۶ تا حدود ۵۳:۲۵](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=3026s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`UPDATE` حرف U در CRUD است و قدرتمندترین (و خطرناک‌ترین) فرمان این هفته. یک `WHERE` جاافتاده می‌تواند همهٔ داده را بازنویسی کند. تمرین اختیاری Favorites هم دربارهٔ پاک‌سازی داده با همین فرمان است.

## UPDATE

- با فرمان `UPDATE` هم می‌توانیم داده را به‌روز کنیم.
- برای نمونه، می‌توانی این را اجرا کنی:

```sql
UPDATE favorites SET language = 'SQL', problem = 'Fiftyville';
```

- نتیجه این است که **همهٔ سطرها** به‌روز می‌شوند.
- دقت کن که این پرس‌وجوها قدرت زیادی دارند. برای همین در دنیای واقعی باید در نظر بگیری چه کسی اجازهٔ اجرای چه فرمان‌هایی را دارد و آیا نسخهٔ پشتیبان در دسترس است!

> [!TIP]
> **تألیفی: نتیجهٔ UPDATE بدون WHERE روی پایگاه دادهٔ نمونه**
> پس از اجرای این فرمان روی پایگاه دادهٔ نمونه، `SELECT DISTINCT language, problem FROM favorites;` فقط یک سطر برمی‌گرداند: `SQL|Fiftyville` (اجراشده روی جعبهٔ ساخت). برای تغییر فقط بعضی سطرها، `WHERE` لازم است؛ مثلاً روی پایگاه دادهٔ کتابخانه: `UPDATE books SET pages = 200 WHERE id = 5;` فقط یک سطر را تغییر می‌دهد.

> [!TIP]
> **تألیفی: مقدار تازه می‌تواند از مقدار قبلی ساخته شود**
> سمت راست `SET` می‌تواند عبارت باشد، نه فقط مقدار ثابت. `UPDATE posts SET likes = likes + 1 WHERE id = 1;` روی پایگاه دادهٔ نمونهٔ `posts` شمار پسندها را از `10` به `11` می‌رساند. یادداشت «شرایط رقابتی» نشان می‌دهد چرا این شکل یک‌دستوری از «خواندن، افزودن در پایتون، نوشتن» امن‌تر است.

## اشتباه‌های رایج

- فراموش کردن `WHERE`؛ همهٔ سطرها بازنویسی می‌شوند.
- جدا کردن چند ستون در `SET` با `AND` به جای ویرگول؛ `SET language = 'SQL' AND problem = 'Fiftyville'` خطا نمی‌دهد اما معنای دیگری دارد و ستون `language` را با نتیجهٔ یک مقایسه پر می‌کند.
- کار مستقیم روی تنها نسخهٔ داده بدون پشتیبان.

## جمع‌بندی

- `UPDATE table SET column = value, ... WHERE condition;` سطرهای منطبق را تغییر می‌دهد.
- بدون `WHERE` همهٔ سطرها تغییر می‌کنند.
- مجوزها و نسخهٔ پشتیبان در دنیای واقعی مهم‌اند.

## پیوندها

- قبلی: [حذف سطر با DELETE و NULL](/kb/d/w07-n05)
- بعدی: [IMDb: طراحی جدول‌ها، کلیدها، نوع‌ها و پرس‌وجوی تودرتو](/kb/d/w07-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
