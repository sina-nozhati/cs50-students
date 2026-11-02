---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-hash-tables
type: short-summary
title: 'ویدئوی کوتاه: جدول‌های درهم‌سازی (Hash Tables)'
title_fa: جدول‌های درهم‌سازی
title_en: Hash Tables
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/hash_tables/
source_refs:
- src-short-hash-tables
- src-anzali-inference-5
concept_ids:
- w05-c-hash-table
- w05-c-hash-function
- w05-c-good-hash-properties
- w05-c-bucket
- w05-c-collision
- w05-c-linear-probing
- w05-c-chaining
prev: w05-sh-queues
next: w05-sh-tries
order: 20
video:
  youtube_id: nvzVHwrrub0
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: فراتر از آرایه و فهرست
    evidence_en: null
  - start: 0:37
    start_seconds: 37
    title_fa: ترکیب آرایه و فهرست پیوندی
    evidence_en: combine an array with a linked list
  - start: '1:42'
    start_seconds: 102
    title_fa: داده خودش جایش را می‌گوید
    evidence_en: rethink how we add data
  - start: '2:11'
    start_seconds: 131
    title_fa: 'ضعف: مرتب‌سازی'
    evidence_en: bad at ordering
  - start: '2:49'
    start_seconds: 169
    title_fa: تابع درهم‌ساز و آرایه
    evidence_en: hash function
  - start: '3:39'
    start_seconds: 219
    title_fa: 'نمونه: John و Paul'
    evidence_en: hash John
  - start: '5:03'
    start_seconds: 303
    title_fa: ویژگی‌های تابع درهم‌ساز خوب
    evidence_en: what makes up a good hash function
  - start: '6:12'
    start_seconds: 372
    title_fa: یک تابع درهم‌ساز نمونه
    evidence_en: Here's an example of a hash function
  - start: '7:56'
    start_seconds: 476
    title_fa: ذکر منبع
    evidence_en: cite your sources
  - start: '9:02'
    start_seconds: 542
    title_fa: برخورد
    evidence_en: We call this a collision
  - start: '9:38'
    start_seconds: 578
    title_fa: کاوش خطی
    evidence_en: linear probing
  - start: '11:44'
    start_seconds: 704
    title_fa: خوشه‌شدن
    evidence_en: clustering
  - start: '12:31'
    start_seconds: 751
    title_fa: زنجیره‌سازی
    evidence_en: chaining
  - start: '17:19'
    start_seconds: 1039
    title_fa: 'برخورد با زنجیره‌سازی: Phoebe'
    evidence_en: hash Phoebe
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: جدول‌های درهم‌سازی (Hash Tables)

> **منبع رسمی:** [صفحهٔ Short «Hash Tables» در CS50x](https://cs50.harvard.edu/x/shorts/hash_tables/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

جدول درهم‌سازی آرایه و فهرست پیوندی را ترکیب می‌کند تا هم دسترسی تصادفی آرایه را داشته باشی و هم رشد و کوچک شدن فهرست را. ایدهٔ اصلی این است که خود داده بگوید کجا باید ذخیره شود: داده از تابع درهم‌ساز می‌گذرد، عددی (hashcode) بیرون می‌آید و داده در همان خانهٔ آرایه می‌نشیند.

ویدئو ویژگی‌های تابع درهم‌ساز خوب را می‌گوید، با نام‌هایی مثل John، Paul و Ringo مسئلهٔ **برخورد** را نشان می‌دهد و دو راه حل را مقایسه می‌کند: **کاوش خطی** که به خوشه‌شدن می‌رسد و **زنجیره‌سازی** که هر خانهٔ آرایه را سر یک فهرست پیوندی می‌کند. ویدئو زنجیره‌سازی را مؤثرترین روش می‌داند.

## نکته‌های کلیدی

- درج، حذف و جست‌وجو در جدول درهم‌سازی به‌طور میانگین می‌تواند به زمان ثابت نزدیک شود؛ ولی جدول درهم‌سازی برای مرتب نگه داشتن داده مناسب نیست.
- تابع درهم‌ساز خوب فقط از دادهٔ ورودی و از همهٔ آن استفاده می‌کند، قطعی است (ورودی یکسان، خروجی یکسان؛ پس عدد تصادفی ممنوع) و داده را یکنواخت پخش می‌کند.
- خروجی تابع باید در محدودهٔ اندازهٔ آرایه بماند؛ ویدئو برای این کار باقی‌ماندهٔ تقسیم بر اندازهٔ جدول را نشان می‌دهد. خروج از محدوده یعنی دسترسی غیرمجاز به حافظه.
- ویدئو نمونه‌ای از یک تابع درهم‌ساز ساده نشان می‌دهد و خودش می‌گوید تابع خوبی نیست. این بسته کد آن را بازتولید نمی‌کند (تصمیم D40).
- برخورد یعنی دو داده با یک hashcode. کاوش خطی دادهٔ دوم را در خانهٔ بعدی خالی می‌گذارد، ولی خوشه‌ها احتمال برخورد بعدی را بیشتر می‌کنند و جدول هم پر می‌شود.
- زنجیره‌سازی: هر خانهٔ آرایه اشاره‌گری به سر یک فهرست پیوندی است؛ دادهٔ تازه به ابتدای همان فهرست اضافه می‌شود. با k فهرست، جست‌وجو هنوز خطی است ولی هر فهرست به‌طور میانگین k برابر کوتاه‌تر است.
- ویدئو توصیه می‌کند تابع درهم‌ساز را از اینترنت بگیری و منبع را ذکر کنی؛ ولی صفحهٔ رسمی Speller می‌گوید تابع درهم‌ساز تو باید «در نهایت از خودت» باشد. برای Speller از قاعدهٔ صفحهٔ پرابلم‌ست پیروی کن (ناهمخوانی ثبت‌شده در `sources.json`).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`hash_tables.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — فراتر از آرایه و فهرست](https://www.youtube.com/watch?v=nvzVHwrrub0&t=0s)
- [۰:۳۷ — ترکیب آرایه و فهرست پیوندی](https://www.youtube.com/watch?v=nvzVHwrrub0&t=37s)
- [۱:۴۲ — داده خودش جایش را می‌گوید](https://www.youtube.com/watch?v=nvzVHwrrub0&t=102s)
- [۲:۱۱ — ضعف: مرتب‌سازی](https://www.youtube.com/watch?v=nvzVHwrrub0&t=131s)
- [۲:۴۹ — تابع درهم‌ساز و آرایه](https://www.youtube.com/watch?v=nvzVHwrrub0&t=169s)
- [۳:۳۹ — نمونه: John و Paul](https://www.youtube.com/watch?v=nvzVHwrrub0&t=219s)
- [۵:۰۳ — ویژگی‌های تابع درهم‌ساز خوب](https://www.youtube.com/watch?v=nvzVHwrrub0&t=303s)
- [۶:۱۲ — یک تابع درهم‌ساز نمونه](https://www.youtube.com/watch?v=nvzVHwrrub0&t=372s)
- [۷:۵۶ — ذکر منبع](https://www.youtube.com/watch?v=nvzVHwrrub0&t=476s)
- [۹:۰۲ — برخورد](https://www.youtube.com/watch?v=nvzVHwrrub0&t=542s)
- [۹:۳۸ — کاوش خطی](https://www.youtube.com/watch?v=nvzVHwrrub0&t=578s)
- [۱۱:۴۴ — خوشه‌شدن](https://www.youtube.com/watch?v=nvzVHwrrub0&t=704s)
- [۱۲:۳۱ — زنجیره‌سازی](https://www.youtube.com/watch?v=nvzVHwrrub0&t=751s)
- [۱۷:۱۹ — برخورد با زنجیره‌سازی: Phoebe](https://www.youtube.com/watch?v=nvzVHwrrub0&t=1039s)

## مفاهیم مرتبط

- جدول درهم‌سازی: آرایه‌ای از اشاره‌گر به گره — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)
- تابع درهم‌سازی: ورودی ← اندیس آرایه — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u01`)
- تابع درهم‌سازی خوب: قطعی، با توزیع یکنواخت، فقط از داده — [یادداشت](/kb/d/w05-sh-hash-tables) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)
- سطل (bucket) و سطل‌بندی — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u01`)
- برخورد (collision) — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)
- کاوش خطی (linear probing) و خوشه‌شدن — [یادداشت](/kb/d/w05-sh-hash-tables) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)
- زنجیره‌سازی: فهرست پیوندی در هر سطل — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/nvzVHwrrub0) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/hash_tables/hash_tables.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/hash_tables/lang/en/hash_tables.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/hash_tables/lang/en/hash_tables.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
