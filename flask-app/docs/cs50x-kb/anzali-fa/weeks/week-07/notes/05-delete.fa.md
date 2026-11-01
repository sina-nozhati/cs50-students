---
id: w07-n05
type: note
title: حذف سطر با DELETE و NULL (DELETE)
title_fa: حذف سطر با DELETE و NULL
title_en: DELETE
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: DELETE
official_anchor: delete
source_url: https://cs50.harvard.edu/x/2026/notes/7/#delete
source_refs:
- src-notes-7#delete
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-delete
- w07-c-is-null
prev: w07-n04
next: w07-n06
order: 5
video:
  youtube_id: oqRU2So6Z2Y
  start: '47:22'
  start_seconds: 2842
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=2842s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'our old friend null'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# حذف سطر با DELETE و NULL

> **منبع رسمی:** بخش «DELETE» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#delete). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۷:۲۲ تا حدود ۵۰:۲۶](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=2842s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`DELETE` حرف D در CRUD است. حذف داده برگشت‌ناپذیر است، پس باید دقیقاً بدانی کدام سطرها را انتخاب کرده‌ای. این یادداشت همچنین نشان می‌دهد چرا برای پیدا کردن `NULL` باید `IS NULL` بنویسی، نه `= NULL`.

## DELETE

- `DELETE` اجازه می‌دهد بخش‌هایی از داده را حذف کنی. برای نمونه می‌توانی بنویسی:

```sql
DELETE FROM favorites WHERE Timestamp IS NULL;
```

- این فرمان هر رکوردی را که `Timestamp` آن `NULL` است حذف می‌کند.

> [!TIP]
> **تألیفی: چرا IS NULL و نه = NULL**
> `NULL` یعنی «مقدار نامعلوم»، و مقایسهٔ هر چیزی با `NULL` با `=` نتیجهٔ نامعلوم می‌دهد، نه درست. برای همین روی پایگاه دادهٔ نمونه (پس از `INSERT` یادداشت قبل) `WHERE "Timestamp" = NULL` عدد `0` می‌دهد، اما `WHERE "Timestamp" IS NULL` عدد `2` (اجراشده روی جعبهٔ ساخت). برای حالت برعکس `IS NOT NULL` بنویس.

> [!TIP]
> **تألیفی: پیش از DELETE، همان WHERE را با SELECT ببین**
> عادت خوب این است که اول `SELECT * FROM favorites WHERE Timestamp IS NULL;` را اجرا کنی، سطرهایی را که برمی‌گردد بررسی کنی و بعد همان `WHERE` را پس از `DELETE FROM favorites` بگذاری. `DELETE FROM favorites;` بدون `WHERE` همهٔ سطرهای جدول را حذف می‌کند.

## اشتباه‌های رایج

- نوشتن `WHERE Timestamp = NULL`؛ هیچ سطری حذف نمی‌شود و خطایی هم نمی‌گیری.
- فراموش کردن `WHERE`؛ همهٔ سطرها حذف می‌شوند.
- انتظار «واگرد» (undo) در `sqlite3`؛ بدون نسخهٔ پشتیبان یا تراکنش باز، حذف برگشت ندارد.

## جمع‌بندی

- `DELETE FROM table WHERE condition;` سطرهای منطبق را حذف می‌کند.
- برای `NULL` از `IS NULL` و `IS NOT NULL` استفاده کن.
- پیش از حذف، شرط را با `SELECT` امتحان کن.

## پیوندها

- قبلی: [افزودن سطر با INSERT](/kb/d/w07-n04)
- بعدی: [تغییر داده با UPDATE](/kb/d/w07-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
