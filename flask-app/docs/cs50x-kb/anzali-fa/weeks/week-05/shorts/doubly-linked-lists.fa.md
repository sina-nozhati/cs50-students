---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-doubly-linked-lists
type: short-summary
title: 'ویدئوی کوتاه: فهرست پیوندی دوطرفه (Doubly-Linked Lists)'
title_fa: فهرست پیوندی دوطرفه
title_en: Doubly-Linked Lists
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/doubly_linked_lists/
source_refs:
- src-short-doubly-linked-lists
- src-anzali-inference-5
concept_ids:
- w05-c-doubly-linked-list
- w05-c-link-before-move
- w05-c-list-complexity
- w05-c-list-tradeoffs
prev: w05-sh-singly-linked-lists
next: w05-sh-stacks
order: 17
video:
  youtube_id: FHMPswJDCvU
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: ادامهٔ داستان فهرست‌ها
    evidence_en: null
  - start: 0:26
    start_seconds: 26
    title_fa: محدودیت فهرست یک‌طرفه
    evidence_en: one critical limitation
  - start: '1:46'
    start_seconds: 106
    title_fa: اشاره‌گر prev
    evidence_en: Previous pointer
  - start: '2:37'
    start_seconds: 157
    title_fa: درج در ابتدای فهرست دوطرفه
    evidence_en: insert a new node into a doubly-linked list
  - start: '5:06'
    start_seconds: 306
    title_fa: حذف یک گرهٔ میانی
    evidence_en: delete a node from a linked list
  - start: '7:47'
    start_seconds: 467
    title_fa: 'جمع‌بندی: زمان ثابت در برابر دسترسی تصادفی'
    evidence_en: Final note here on linked lists
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: فهرست پیوندی دوطرفه (Doubly-Linked Lists)

> **منبع رسمی:** [صفحهٔ Short «Doubly-Linked Lists» در CS50x](https://cs50.harvard.edu/x/shorts/doubly_linked_lists/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو ادامهٔ فهرست یک‌طرفه است. محدودیت اصلی فهرست یک‌طرفه این است که فقط در یک جهت حرکت می‌کنی و حذف یک گرهٔ تنها دردسر دارد. با افزودن یک فیلد `prev` به گره، **فهرست پیوندی دوطرفه** ساخته می‌شود که در هر دو جهت پیمایش‌پذیر است.

ویدئو درج در ابتدای فهرست دوطرفه و حذف یک گرهٔ میانی را با تصویر نشان می‌دهد و با جمع‌بندی بده‌بستان فهرست‌ها تمام می‌شود: درج و حذف در زمان ثابت، ولی بدون دسترسی تصادفی.

## نکته‌های کلیدی

- گرهٔ دوطرفه سه فیلد دارد: داده، `next` و `prev`؛ پس از گرهٔ یک‌طرفه بزرگ‌تر است. اگر حذف تک‌گره لازم نیست، شاید ارزش حافظهٔ اضافه را نداشته باشد.
- ساختن، جست‌وجو و حذف کل فهرست تقریباً مثل فهرست یک‌طرفه است؛ تفاوت در درج و حذف یک گره است.
- در درج در ابتدا اول اشاره‌گرهای گرهٔ تازه را پر کن (`next` به سر قدیمی، `prev` به NULL)، بعد `prev` سر قدیمی را به گرهٔ تازه برگردان و در پایان سر فهرست را جابه‌جا کن.
- برای حذف گرهٔ میانی، `next` گرهٔ قبلی و `prev` گرهٔ بعدی را طوری تنظیم کن که از روی آن بپرند، بعد گره را آزاد کن.
- حذف ابتدای فهرست و انتهای آن حالت‌های خاص دارند که ویدئو به عهدهٔ بیننده می‌گذارد.
- درج در ابتدا و حذف گره‌ای که اشاره‌گرش را داری تعداد گام ثابتی دارد؛ ولی یافتن یک عنصر هنوز جست‌وجوی خطی است.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`doubly_linked_lists.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — ادامهٔ داستان فهرست‌ها](https://www.youtube.com/watch?v=FHMPswJDCvU&t=0s)
- [۰:۲۶ — محدودیت فهرست یک‌طرفه](https://www.youtube.com/watch?v=FHMPswJDCvU&t=26s)
- [۱:۴۶ — اشاره‌گر prev](https://www.youtube.com/watch?v=FHMPswJDCvU&t=106s)
- [۲:۳۷ — درج در ابتدای فهرست دوطرفه](https://www.youtube.com/watch?v=FHMPswJDCvU&t=157s)
- [۵:۰۶ — حذف یک گرهٔ میانی](https://www.youtube.com/watch?v=FHMPswJDCvU&t=306s)
- [۷:۴۷ — جمع‌بندی: زمان ثابت در برابر دسترسی تصادفی](https://www.youtube.com/watch?v=FHMPswJDCvU&t=467s)

## مفاهیم مرتبط

- فهرست پیوندی دوطرفه (prev و next) — [یادداشت](/kb/d/w05-sh-doubly-linked-lists) · درس کوتاه `w05-l05` (واحد `w05-l05-u04`)
- اول n->next = list، بعد list = n؛ وگرنه فهرست یتیم می‌شود — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u01`)
- هزینهٔ فهرست: درج در ابتدا O(1)، جست‌وجو O(n) — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u03`)
- بده‌بستان فهرست: پویایی در برابر حافظهٔ اضافه و نبود دسترسی تصادفی — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/FHMPswJDCvU) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/doubly_linked_lists/doubly_linked_lists.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/doubly_linked_lists/lang/en/doubly_linked_lists.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/doubly_linked_lists/lang/en/doubly_linked_lists.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
