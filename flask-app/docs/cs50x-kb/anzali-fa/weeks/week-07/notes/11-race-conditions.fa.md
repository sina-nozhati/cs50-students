---
id: w07-n11
type: note
title: شرایط مسابقه و تراکنش (Race Conditions)
title_fa: شرایط مسابقه و تراکنش
title_en: Race Conditions
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Race Conditions
official_anchor: race-conditions
source_url: https://cs50.harvard.edu/x/2026/notes/7/#race-conditions
source_refs:
- src-notes-7#race-conditions
- src-transcript-7
- src-sqlite-docs
- src-sql-box-7
- src-anzali-authored-7
- src-anzali-inference-7
- src-srt-7
concept_ids:
- w07-c-race-condition
- w07-c-transaction
- w07-c-atomic-update
prev: w07-n10
next: w07-n12
order: 11
video:
  youtube_id: oqRU2So6Z2Y
  start: '2:06:57'
  start_seconds: 7617
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=7617s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'So what is a race condition?'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# شرایط مسابقه و تراکنش

> **منبع رسمی:** بخش «Race Conditions» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#race-conditions). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۶:۵۷](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=7617s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

وقتی فقط تو با پایگاه داده کار می‌کنی، ترتیب فرمان‌ها روشن است. در یک وب‌سایت، هزاران کاربر هم‌زمان می‌خوانند و می‌نویسند و دو برنامهٔ درست می‌توانند با هم نتیجهٔ نادرست بسازند. این یادداشت نام این مشکل و ابزارهای SQL برای مهار آن را معرفی می‌کند.

## شرایط رقابتی

- استفاده از SQL گاهی به مشکل‌هایی می‌انجامد.
- حالتی را تصور کن که چند کاربر هم‌زمان به یک پایگاه داده دسترسی دارند و فرمان اجرا می‌کنند.
- این ممکن است به خطاهایی منجر شود که در آن‌ها کدی با کارهای دیگران قطع می‌شود؛ نتیجه می‌تواند از دست رفتن داده باشد.
- امکانات داخلی SQL مثل `BEGIN TRANSACTION`، `COMMIT` و `ROLLBACK` به جلوگیری از بعضی از این مشکل‌های **شرایط رقابتی** (race condition) کمک می‌کنند.

> [!NOTE]
> **از سخنرانی: شیر و یخچال**
> دیوید مثال قدیمی یخچال خوابگاه را می‌گوید: تو به اتاق می‌رسی، می‌بینی شیر تمام شده و برای خرید می‌روی؛ در همین فاصله هم‌اتاقی‌ات هم می‌رسد، یخچال را خالی می‌بیند و او هم شیر می‌خرد. هر دو بر پایهٔ وضعیتی تصمیم گرفتید که در لحظهٔ عمل دیگر درست نبود.

> [!NOTE]
> **از سخنرانی: شمار پسندهای یک پست**
> بعد مثالی از پسندهای اینستاگرام می‌آید. کد روی هر سرور سه گام دارد: شمار فعلی پسندها را با `SELECT` بخوان، آن را در متغیری نگه دار، و با `UPDATE` مقدار یکی بیشتر را بنویس (با جای‌نگهدار `?`، پس تزریق SQL ممکن نیست). اگر دو سرور تقریباً هم‌زمان گام اول را اجرا کنند، هر دو مثلاً `100` را می‌خوانند و هر دو `101` را می‌نویسند؛ یکی از پسندها گم می‌شود. دیوید می‌گوید با **تراکنش** می‌شود فقط سطر مورد نظر را قفل کرد: `BEGIN TRANSACTION`، اجرای فرمان‌ها، و `COMMIT` برای ذخیره؛ اگر چیزی خراب شود یا کار قطع شود، می‌شود همه را برگرداند (`ROLLBACK`).

> [!TIP]
> **تألیفی: تراکنش روی پایگاه دادهٔ نمونه**
> روی `fixtures/posts.sql` (پست ۱ با ۱۰ پسند) این دنباله اجرا شد:
> `BEGIN TRANSACTION;` سپس `UPDATE posts SET likes = likes + 1 WHERE id = 1;` سپس `ROLLBACK;` سپس `SELECT likes FROM posts WHERE id = 1;`. نتیجه `10` بود، چون `ROLLBACK` تغییر را لغو کرد. با `COMMIT` به جای `ROLLBACK` نتیجه `11` می‌شود (اجراشده روی جعبهٔ ساخت).

> [!TIP]
> **استنتاجی: یک فرمان به جای خواندن و نوشتن جدا**
> برای این مثال خاص، `UPDATE posts SET likes = likes + 1 WHERE id = ?` افزایش را در **یک** فرمان SQL انجام می‌دهد و پایگاه داده آن را یکجا (اتمی) اجرا می‌کند؛ پس فاصله‌ای میان خواندن و نوشتن نمی‌ماند که سرور دیگری وسطش بیاید. وقتی منطق پیچیده‌تر است و چند فرمان لازم است، تراکنش ابزار درست است (بر پایهٔ مستندات SQLite دربارهٔ تراکنش‌ها).

## اشتباه‌های رایج

- فرض اینکه کدی که برای یک کاربر درست است، برای هزار کاربر هم‌زمان هم درست است.
- خواندن مقدار در پایتون، تغییرش و نوشتن دوباره، بدون تراکنش.
- فراموش کردن `COMMIT` پس از `BEGIN TRANSACTION`؛ تغییرها ذخیره نمی‌شوند و قفل باز می‌ماند.

## جمع‌بندی

- شرایط رقابتی: نتیجه به ترتیب تصادفی کارهای هم‌زمان بستگی دارد.
- `BEGIN TRANSACTION` ... `COMMIT` چند فرمان را یکجا اعمال می‌کند و `ROLLBACK` همه را لغو.
- افزایش در یک فرمان (`likes = likes + 1`) فاصلهٔ خواندن و نوشتن را حذف می‌کند.

## پیوندها

- قبلی: [SQL در پایتون با کتابخانهٔ CS50](/kb/d/w07-n10)
- بعدی: [حملهٔ تزریق SQL و جای‌نگهدار ?](/kb/d/w07-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
