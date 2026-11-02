---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-sh-dynamic-memory-allocation
type: short-summary
title: 'ویدئوی کوتاه: تخصیص پویای حافظه (Dynamic Memory Allocation)'
title_fa: تخصیص پویای حافظه
title_en: Dynamic Memory Allocation
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/dynamic_memory_allocation/
source_refs:
- src-short-dynamic-memory-allocation
- src-anzali-inference-4
concept_ids:
- w04-c-malloc
- w04-c-free
- w04-c-malloc-null-check
- w04-c-heap-vs-stack-alloc
- w04-c-free-rules
- w04-c-memory-leak
- w04-c-sizeof
prev: w04-sh-defining-custom-types
next: w04-sh-file-pointers
order: 21
video:
  youtube_id: xa4ugmMDhiE
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'پیش‌نیاز: اشاره‌گرها'
    evidence_en: null
  - start: '1:21'
    start_seconds: 81
    title_fa: حافظهٔ ایستا در برابر پویا
    evidence_en: need to use dynamic memory allocation
  - start: '1:32'
    start_seconds: 92
    title_fa: heap و stack
    evidence_en: The heap is a giant pool of memory
  - start: '2:26'
    start_seconds: 146
    title_fa: malloc
    evidence_en: a new function called malloc
  - start: '3:25'
    start_seconds: 205
    title_fa: بررسی NULL
    evidence_en: always check for null after malloc
  - start: '5:09'
    start_seconds: 309
    title_fa: آرایه روی stack و روی heap
    evidence_en: declare an array of that many floats
  - start: '7:05'
    start_seconds: 425
    title_fa: نشت حافظه
    evidence_en: what you get is something called a memory leak
  - start: '8:32'
    start_seconds: 512
    title_fa: free و سه قانون
    evidence_en: three basic rules for malloc and free
  - start: '9:48'
    start_seconds: 588
    title_fa: نمونهٔ جعبه‌ای
    evidence_en: close this video by taking a look at a couple of lines
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: تخصیص پویای حافظه (Dynamic Memory Allocation)

> **منبع رسمی:** [صفحهٔ Short «Dynamic Memory Allocation» در CS50x](https://cs50.harvard.edu/x/shorts/dynamic_memory_allocation/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

تا اینجا اشاره‌گرها فقط به متغیرهایی اشاره می‌کردند که از قبل وجود داشتند. اما اگر ندانیم برنامه چقدر حافظه لازم دارد، باید هنگام اجرا حافظهٔ تازه بگیریم؛ این حافظهٔ پویا از heap می‌آید.

ویدئو malloc، بررسی NULL، sizeof، آرایه روی stack در برابر آرایه روی heap، نشت حافظه، free و سه قانون اصلی را توضیح می‌دهد و با یک نمودار جعبه‌ای قدم‌به‌قدم تمام می‌شود.

## نکته‌های کلیدی

- حافظهٔ ایستا (هر چیزی که نام دارد، مثل متغیرها) روی stack ساخته می‌شود و حافظهٔ پویا از heap می‌آید؛ هر دو بخشی از یک حافظهٔ بزرگ‌اند: stack رو به بالا و heap رو به پایین رشد می‌کند.
- malloc در stdlib.h است و فقط تعداد بایت‌ها را می‌گیرد؛ اشاره‌گری به آن حافظه برمی‌گرداند، یا اگر نتواند، NULL.
- قانون اول پس از malloc: همیشه NULL را بررسی کن؛ اگر NULL بود، برنامه باید متوقف شود.
- به‌جای عدد ۴ می‌شود از `sizeof(int)` استفاده کرد؛ `malloc(x * sizeof(float))` بلوکی برای x عدد اعشاری می‌دهد که مثل آرایه با آن کار می‌کنیم.
- حافظهٔ پویا خودکار به سیستم برنمی‌گردد؛ اگر آزادش نکنی، نشت حافظه پیش می‌آید و سیستم کند می‌شود (ویدئو مثال مرورگرهایی را می‌زند که روزها باز می‌مانند).
- سه قانون: هر چه malloc کردی free کن؛ فقط چیزی را free کن که malloc کرده‌ای؛ هیچ بلوکی را دو بار free نکن.
- پس از free، اشاره‌گرها هنوز به همان جا اشاره می‌کنند ولی دیگر حق استفاده نداری؛ نوشتن در آن رفتار پیش‌بینی‌ناپذیر دارد و ممکن است segmentation fault بدهد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`dynamic_memory_allocation.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — پیش‌نیاز: اشاره‌گرها](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=0s)
- [۱:۲۱ — حافظهٔ ایستا در برابر پویا](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=81s)
- [۱:۳۲ — heap و stack](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=92s)
- [۲:۲۶ — malloc](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=146s)
- [۳:۲۵ — بررسی NULL](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=205s)
- [۵:۰۹ — آرایه روی stack و روی heap](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=309s)
- [۷:۰۵ — نشت حافظه](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=425s)
- [۸:۳۲ — free و سه قانون](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=512s)
- [۹:۴۸ — نمونهٔ جعبه‌ای](https://www.youtube.com/watch?v=xa4ugmMDhiE&t=588s)

## مفاهیم مرتبط

- malloc: گرفتن چند بایت حافظه از سیستم عامل — [یادداشت](/kb/d/w04-n09) · درس کوتاه `w04-l04` (واحد `w04-l04-u02`)
- free: پس دادن حافظه‌ای که malloc داده است — [یادداشت](/kb/d/w04-n09) · درس کوتاه `w04-l04` (واحد `w04-l04-u02`)
- بررسی NULL پس از malloc (و هر تابعی که اشاره‌گر برمی‌گرداند) — [یادداشت](/kb/d/w04-n09) · درس کوتاه `w04-l04` (واحد `w04-l04-u02`)
- حافظهٔ ایستا (پشته) در برابر پویا (هیپ) — [یادداشت](/kb/d/w04-sh-dynamic-memory-allocation) · درس کوتاه `w04-l04` (واحد `w04-l04-u03`)
- سه قانون free: همه را آزاد کن، فقط malloc شده‌ها، یک بار — [یادداشت](/kb/d/w04-sh-dynamic-memory-allocation) · درس کوتاه `w04-l04` (واحد `w04-l04-u03`)
- نشت حافظه: malloc بدون free — [یادداشت](/kb/d/w04-n10) · درس کوتاه `w04-l05` (واحد `w04-l05-u01`)
- sizeof برای اندازهٔ یک نوع به بایت — [یادداشت](/kb/d/w04-n10) · درس کوتاه `w04-l05` (واحد `w04-l05-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/xa4ugmMDhiE) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/dynamic_memory_allocation/dynamic_memory_allocation.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/dynamic_memory_allocation/lang/en/dynamic_memory_allocation.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/dynamic_memory_allocation/lang/en/dynamic_memory_allocation.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
