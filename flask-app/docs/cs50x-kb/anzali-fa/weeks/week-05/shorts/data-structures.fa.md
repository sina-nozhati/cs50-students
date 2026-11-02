---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-data-structures
type: short-summary
title: 'ویدئوی کوتاه: مقایسهٔ ساختمان‌های داده (Data Structures)'
title_fa: مقایسهٔ ساختمان‌های داده
title_en: Data Structures
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/data_structures/
source_refs:
- src-short-data-structures
- src-anzali-inference-5
concept_ids:
- w05-c-structure-choice
- w05-c-array-contiguous
- w05-c-list-tradeoffs
- w05-c-hash-table
- w05-c-trie-memory
- w05-c-time-space-tradeoff
prev: w05-sh-tries
next: w05-ps-inheritance
order: 22
video:
  youtube_id: 3uGchQbk7g8
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: ساختمان‌های داده در CS50
    evidence_en: null
  - start: 0:17
    start_seconds: 17
    title_fa: چهار ایدهٔ پایه
    evidence_en: four basic ideas
  - start: '1:21'
    start_seconds: 81
    title_fa: آرایه
    evidence_en: start with arrays
  - start: '2:52'
    start_seconds: 172
    title_fa: فهرست پیوندی
    evidence_en: With a linked list
  - start: '4:22'
    start_seconds: 262
    title_fa: جدول درهم‌سازی
    evidence_en: Hash tables. Insertion
  - start: '6:27'
    start_seconds: 387
    title_fa: ترای
    evidence_en: tries are the fourth
  - start: '7:51'
    start_seconds: 471
    title_fa: هزینهٔ حافظهٔ ترای
    evidence_en: rapidly becomes huge
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: مقایسهٔ ساختمان‌های داده (Data Structures)

> **منبع رسمی:** [صفحهٔ Short «Data Structures» در CS50x](https://cs50.harvard.edu/x/shorts/data_structures/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو جمع‌بندی ساختمان‌های دادهٔ CS50 است. به گفتهٔ ویدئو همه چیز به چهار ایدهٔ پایه برمی‌گردد: آرایه، فهرست پیوندی، جدول درهم‌سازی و ترای. برای هر کدام درج، حذف، جست‌وجو، مرتب‌سازی و اندازه سنجیده می‌شود.

پیام ویدئو این است که ساختمان دادهٔ «بهترین» وجود ندارد: اگر فقط دسترسی تصادفی سریع می‌خواهی شاید آرایه بهتر باشد، و اگر حافظه کمیاب است شاید ترای انتخاب درستی نباشد.

## نکته‌های کلیدی

- آرایه: درج و حذف (جز در انتها) بد، جست‌وجو با دسترسی تصادفی عالی، مرتب‌سازی نسبتاً آسان، کم‌حجم، ولی اندازهٔ ثابت.
- فهرست پیوندی: درج در ابتدا آسان، حذف پس از یافتن آسان، جست‌وجو خطی و بد، مرتب‌سازی دشوار (فقط هنگام ساختن)، کمی بزرگ‌تر از آرایه.
- جدول درهم‌سازی: درج دو گام (درهم‌سازی و درج)، حذف پس از یافتن آسان، جست‌وجو به‌طور میانگین بهتر از فهرست، برای مرتب‌سازی نامناسب، اندازه وابسته به طراحی.
- ترای: درج پیچیده ولی در عمل ثابت، حذف و جست‌وجو سریع و فقط وابسته به طول کلید، به‌خودی‌خود مرتب، ولی بسیار حجیم.
- ویدئو می‌گوید گره‌ای با ۱۰ اشاره‌گر در CS50 IDE دست‌کم ۸۰ بایت است و با ۲۶ اشاره‌گر «احتمالاً حدود ۲۰۰ بایت»؛ حساب دقیق ۲۶ × ۸ = ۲۰۸ بایت است (ناهمخوانی ثبت‌شده در `sources.json`).
- انتخاب ساختمان داده به عملیات غالب و محدودیت حافظه بستگی دارد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`data_structures.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — ساختمان‌های داده در CS50](https://www.youtube.com/watch?v=3uGchQbk7g8&t=0s)
- [۰:۱۷ — چهار ایدهٔ پایه](https://www.youtube.com/watch?v=3uGchQbk7g8&t=17s)
- [۱:۲۱ — آرایه](https://www.youtube.com/watch?v=3uGchQbk7g8&t=81s)
- [۲:۵۲ — فهرست پیوندی](https://www.youtube.com/watch?v=3uGchQbk7g8&t=172s)
- [۴:۲۲ — جدول درهم‌سازی](https://www.youtube.com/watch?v=3uGchQbk7g8&t=262s)
- [۶:۲۷ — ترای](https://www.youtube.com/watch?v=3uGchQbk7g8&t=387s)
- [۷:۵۱ — هزینهٔ حافظهٔ ترای](https://www.youtube.com/watch?v=3uGchQbk7g8&t=471s)

## مفاهیم مرتبط

- انتخاب ساختمان داده بر اساس عملیات غالب — [یادداشت](/kb/d/w05-sec) · درس کوتاه `w05-l07` (واحد `w05-l07-u04`)
- آرایه بلوکی پیوسته از حافظه است — [یادداشت](/kb/d/w05-n05) · درس کوتاه `w05-l02` (واحد `w05-l02-u01`)
- بده‌بستان فهرست: پویایی در برابر حافظهٔ اضافه و نبود دسترسی تصادفی — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u03`)
- جدول درهم‌سازی: آرایه‌ای از اشاره‌گر به گره — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)
- هزینهٔ حافظهٔ ترای — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- بده‌بستان زمان و حافظه — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/3uGchQbk7g8) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/data_structures/data_structures.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
