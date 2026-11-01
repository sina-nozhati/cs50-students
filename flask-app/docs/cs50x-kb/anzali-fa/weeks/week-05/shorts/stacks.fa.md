---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-stacks
type: short-summary
title: 'ویدئوی کوتاه: پشته‌ها (Stacks)'
title_fa: پشته‌ها
title_en: Stacks
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/stacks/
source_refs:
- src-short-stacks
- src-anzali-inference-5
concept_ids:
- w05-c-stack
- w05-c-lifo
- w05-c-push-pop
- w05-c-capacity-vs-size
- w05-c-fixed-capacity-limit
- w05-c-prepend
prev: w05-sh-doubly-linked-lists
next: w05-sh-queues
order: 18
video:
  youtube_id: hVsNqhEthOk
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: پشته به‌عنوان ساختمان داده
    evidence_en: null
  - start: '1:28'
    start_seconds: 88
    title_fa: 'LIFO: آخر وارد، اول خارج'
    evidence_en: LIFO
  - start: '2:04'
    start_seconds: 124
    title_fa: پیاده‌سازی آرایه‌ای
    evidence_en: array based
  - start: '5:49'
    start_seconds: 349
    title_fa: push روی پشتهٔ آرایه‌ای
    evidence_en: push the number 28
  - start: '6:56'
    start_seconds: 416
    title_fa: pop
    evidence_en: popping is the sort of counterpart
  - start: '9:50'
    start_seconds: 590
    title_fa: پیاده‌سازی با فهرست پیوندی
    evidence_en: Now linked lists are another way
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: پشته‌ها (Stacks)

> **منبع رسمی:** [صفحهٔ Short «Stacks» در CS50x](https://cs50.harvard.edu/x/shorts/stacks/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو ابتدا تأکید می‌کند که این «پشته» ساختمان داده است، نه بخش پشتهٔ حافظه. پشته ساختاری است که فقط تازه‌ترین عنصر افزوده‌شده را می‌توان از آن برداشت: آخر وارد، اول خارج (LIFO). دو عمل دارد: push و pop.

سپس دو پیاده‌سازی را نشان می‌دهد: با آرایه‌ای به اندازهٔ ثابت `CAPACITY` و فیلد `top`، و با فهرست پیوندی که در آن فقط از ابتدای فهرست درج و حذف می‌کنی.

## نکته‌های کلیدی

- LIFO یعنی آخرین عنصری که گذاشتی اولین عنصری است که برمی‌داری؛ مثل برداشتن از بالای یک توده.
- push یعنی گذاشتن عنصر تازه روی پشته؛ pop یعنی برداشتن تازه‌ترین عنصر و برگرداندن مقدارش.
- در پیاده‌سازی آرایه‌ای، ظرفیت ثابت (`CAPACITY`) محدودیت ذاتی است و فیلد `top` جای عنصر بعدی را نشان می‌دهد.
- push و pop باید اشاره‌گری به پشته بگیرند، وگرنه روی یک کپی کار می‌کنند؛ مگر پشته سراسری باشد.
- pop در آرایه مقدار را واقعاً پاک نمی‌کند؛ فقط `top` را کم می‌کند و push بعدی روی آن می‌نویسد.
- در پیاده‌سازی با فهرست پیوندی، push همان درج در ابتدا و pop همان حذف گرهٔ اول است؛ همیشه اشاره‌گری به سر فهرست نگه دار.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`stacks.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — پشته به‌عنوان ساختمان داده](https://www.youtube.com/watch?v=hVsNqhEthOk&t=0s)
- [۱:۲۸ — LIFO: آخر وارد، اول خارج](https://www.youtube.com/watch?v=hVsNqhEthOk&t=88s)
- [۲:۰۴ — پیاده‌سازی آرایه‌ای](https://www.youtube.com/watch?v=hVsNqhEthOk&t=124s)
- [۵:۴۹ — push روی پشتهٔ آرایه‌ای](https://www.youtube.com/watch?v=hVsNqhEthOk&t=349s)
- [۶:۵۶ — pop](https://www.youtube.com/watch?v=hVsNqhEthOk&t=416s)
- [۹:۵۰ — پیاده‌سازی با فهرست پیوندی](https://www.youtube.com/watch?v=hVsNqhEthOk&t=590s)

## مفاهیم مرتبط

- پشته (stack) — [یادداشت](/kb/d/w05-n04) · درس کوتاه `w05-l01` (واحد `w05-l01-u03`)
- LIFO: آخر وارد، اول خارج — [یادداشت](/kb/d/w05-n04) · درس کوتاه `w05-l01` (واحد `w05-l01-u03`)
- push و pop — [یادداشت](/kb/d/w05-n04) · درس کوتاه `w05-l01` (واحد `w05-l01-u03`)
- ظرفیت (CAPACITY) در برابر اندازهٔ فعلی (size) — [یادداشت](/kb/d/w05-n03) · درس کوتاه `w05-l01` (واحد `w05-l01-u02`)
- محدودیت ظرفیت ثابت: یا کم می‌آید یا هدر می‌رود — [یادداشت](/kb/d/w05-n04) · درس کوتاه `w05-l01` (واحد `w05-l01-u03`)
- افزودن به ابتدای فهرست (prepend) — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/hVsNqhEthOk) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/stacks/stacks.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/stacks/lang/en/stacks.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/stacks/lang/en/stacks.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
