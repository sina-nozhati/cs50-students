---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-queues
type: short-summary
title: 'ویدئوی کوتاه: صف‌ها (Queues)'
title_fa: صف‌ها
title_en: Queues
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/queues/
source_refs:
- src-short-queues
- src-anzali-inference-5
concept_ids:
- w05-c-queue
- w05-c-fifo
- w05-c-enqueue-dequeue
- w05-c-capacity-vs-size
- w05-c-queue-wraparound
- w05-c-doubly-linked-list
prev: w05-sh-stacks
next: w05-sh-hash-tables
order: 19
video:
  youtube_id: 3TmUv1uS92s
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: صف در برابر پشته
    evidence_en: null
  - start: 0:45
    start_seconds: 45
    title_fa: صف بانک و عدالت
    evidence_en: amusement park
  - start: '1:36'
    start_seconds: 96
    title_fa: enqueue و dequeue
    evidence_en: enqueue, which is to add
  - start: '2:10'
    start_seconds: 130
    title_fa: 'پیاده‌سازی آرایه‌ای: front و size'
    evidence_en: array-based implementations
  - start: '4:07'
    start_seconds: 247
    title_fa: enqueue در آرایه
    evidence_en: first operation we can perform is to enqueue
  - start: '8:01'
    start_seconds: 481
    title_fa: dequeue در آرایه
    evidence_en: dequeue something
  - start: '10:33'
    start_seconds: 633
    title_fa: چرخش با باقی‌ماندهٔ تقسیم
    evidence_en: mod by the size of capacity
  - start: '11:31'
    start_seconds: 691
    title_fa: صف با فهرست پیوندی
    evidence_en: implement a queue as a linked list
  - start: '14:08'
    start_seconds: 848
    title_fa: dequeue در فهرست
    evidence_en: Dequeuing is actually very similar
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: صف‌ها (Queues)

> **منبع رسمی:** [صفحهٔ Short «Queues» در CS50x](https://cs50.harvard.edu/x/shorts/queues/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

صف شبیه پشته است با یک تفاوت: اول وارد، اول خارج (FIFO). ویدئو صف بانک یا شهربازی را مثال می‌زند و صف را «ساختار عدالت‌محور» می‌نامد. دو عمل دارد: enqueue (افزودن به انتها) و dequeue (برداشتن قدیمی‌ترین عنصر از ابتدا).

در پیاده‌سازی آرایه‌ای، صف به‌جای نگه داشتن انتها، دو فیلد `front` و `size` دارد؛ جای عنصر بعدی از جمع آن‌ها به دست می‌آید و با باقی‌ماندهٔ تقسیم بر ظرفیت دور آرایه می‌چرخد. پیاده‌سازی دوم با فهرست پیوندی (در ویدئو دوطرفه) و اشاره‌گرهایی به سر و ته است.

## نکته‌های کلیدی

- FIFO یعنی قدیمی‌ترین عنصر همیشه اولین عنصری است که بیرون می‌آید.
- صف آرایه‌ای در ویدئو سه فیلد دارد: آرایه‌ای به ظرفیت `CAPACITY`، `front` (قدیمی‌ترین عنصر) و `size` (تعداد عنصرها).
- عنصر تازه در خانهٔ `front + size` می‌نشیند؛ وقتی به انتهای آرایه رسیدی، با باقی‌ماندهٔ تقسیم بر ظرفیت به ابتدای آرایه برمی‌گردی.
- صف وقتی پر است که `size` با ظرفیت برابر شود.
- dequeue مقدار را پاک نمی‌کند؛ `front` را جلو می‌برد، `size` را کم می‌کند و مقدار را برمی‌گرداند.
- در پیاده‌سازی با فهرست پیوندی، اشاره‌گرهای سر و ته را نگه می‌داری: enqueue پشت ته اضافه می‌کند و dequeue گرهٔ سر را آزاد می‌کند. ویدئو می‌گوید با فهرست یک‌طرفه هم شدنی است.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`queues.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — صف در برابر پشته](https://www.youtube.com/watch?v=3TmUv1uS92s&t=0s)
- [۰:۴۵ — صف بانک و عدالت](https://www.youtube.com/watch?v=3TmUv1uS92s&t=45s)
- [۱:۳۶ — enqueue و dequeue](https://www.youtube.com/watch?v=3TmUv1uS92s&t=96s)
- [۲:۱۰ — پیاده‌سازی آرایه‌ای: front و size](https://www.youtube.com/watch?v=3TmUv1uS92s&t=130s)
- [۴:۰۷ — enqueue در آرایه](https://www.youtube.com/watch?v=3TmUv1uS92s&t=247s)
- [۸:۰۱ — dequeue در آرایه](https://www.youtube.com/watch?v=3TmUv1uS92s&t=481s)
- [۱۰:۳۳ — چرخش با باقی‌ماندهٔ تقسیم](https://www.youtube.com/watch?v=3TmUv1uS92s&t=633s)
- [۱۱:۳۱ — صف با فهرست پیوندی](https://www.youtube.com/watch?v=3TmUv1uS92s&t=691s)
- [۱۴:۰۸ — dequeue در فهرست](https://www.youtube.com/watch?v=3TmUv1uS92s&t=848s)

## مفاهیم مرتبط

- صف (queue) — [یادداشت](/kb/d/w05-n03) · درس کوتاه `w05-l01` (واحد `w05-l01-u02`)
- FIFO: اول وارد، اول خارج — [یادداشت](/kb/d/w05-n03) · درس کوتاه `w05-l01` (واحد `w05-l01-u02`)
- enqueue و dequeue — [یادداشت](/kb/d/w05-n03) · درس کوتاه `w05-l01` (واحد `w05-l01-u02`)
- ظرفیت (CAPACITY) در برابر اندازهٔ فعلی (size) — [یادداشت](/kb/d/w05-n03) · درس کوتاه `w05-l01` (واحد `w05-l01-u02`)
- صف آرایه‌ای با front و چرخش (mod CAPACITY) — [یادداشت](/kb/d/w05-sh-queues) · درس کوتاه `w05-l01` (واحد `w05-l01-u02`)
- فهرست پیوندی دوطرفه (prev و next) — [یادداشت](/kb/d/w05-sh-doubly-linked-lists) · درس کوتاه `w05-l05` (واحد `w05-l05-u04`)

## منابع

- [ویدئو در YouTube](https://youtu.be/3TmUv1uS92s) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/queues/queues.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/queues/lang/en/queues.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/queues/lang/en/queues.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
