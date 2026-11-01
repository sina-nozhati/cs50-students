---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-singly-linked-lists
type: short-summary
title: 'ویدئوی کوتاه: فهرست پیوندی یک‌طرفه (Singly-Linked Lists)'
title_fa: فهرست پیوندی یک‌طرفه
title_en: Singly-Linked Lists
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/singly_linked_lists/
source_refs:
- src-short-singly-linked-lists
- src-anzali-inference-5
concept_ids:
- w05-c-linked-list
- w05-c-node
- w05-c-self-referential-struct
- w05-c-list-null-end
- w05-c-head-pointer
- w05-c-list-traversal
- w05-c-prepend
- w05-c-link-before-move
- w05-c-append
- w05-c-free-list
- w05-c-list-complexity
prev: w05-sh-structures
next: w05-sh-doubly-linked-lists
order: 16
video:
  youtube_id: zQI3FyWm144
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: ساختن داده‌ساختارهای خودمان
    evidence_en: null
  - start: '1:37'
    start_seconds: 97
    title_fa: مشکل انعطاف‌ناپذیری آرایه
    evidence_en: inflexibility
  - start: '3:08'
    start_seconds: 188
    title_fa: 'گره: داده و اشاره‌گر'
    evidence_en: this node has two members
  - start: '4:26'
    start_seconds: 266
    title_fa: ساختار خودارجاع
    evidence_en: self referential structure
  - start: '6:06'
    start_seconds: 366
    title_fa: ساختن فهرست از هیچ
    evidence_en: create a linked list out of thin air
  - start: '9:15'
    start_seconds: 555
    title_fa: جست‌وجو در فهرست
    evidence_en: bool find
  - start: '13:07'
    start_seconds: 787
    title_fa: درج در ابتدا
    evidence_en: insert a new node into the linked list
  - start: '16:30'
    start_seconds: 990
    title_fa: ترتیب اشتباه و یتیم شدن فهرست
    evidence_en: orphaning the rest of the list
  - start: '18:04'
    start_seconds: 1084
    title_fa: حذف کل فهرست به‌صورت بازگشتی
    evidence_en: get rid of an entire linked list
  - start: '22:00'
    start_seconds: 1320
    title_fa: چرا حذف یک گره سخت است
    evidence_en: deleting a single element
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: فهرست پیوندی یک‌طرفه (Singly-Linked Lists)

> **منبع رسمی:** [صفحهٔ Short «Singly-Linked Lists» در CS50x](https://cs50.harvard.edu/x/shorts/singly_linked_lists/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو از محدودیت‌های آرایه شروع می‌کند: درج در میانه گران است و اندازه فقط یک بار تعیین می‌شود. با ترکیب اشاره‌گر، ساختار و `malloc` به **فهرست پیوندی یک‌طرفه** می‌رسد: زنجیره‌ای از گره‌ها که هر کدام یک مقدار و اشاره‌گری به گرهٔ بعدی دارند.

سپس عملیات اصلی را با شبه‌کد و تصویر مرور می‌کند: ساختن فهرست از هیچ، جست‌وجو با اشاره‌گر پیمایش، درج در ابتدا (و چرا ترتیب جابه‌جایی اشاره‌گرها مهم است) و حذف کل فهرست به‌صورت بازگشتی. حذف یک گرهٔ تنها را عمداً به ویدئوی فهرست دوطرفه می‌سپارد.

## نکته‌های کلیدی

- هر گره دو فیلد دارد: داده و اشاره‌گری به گره‌ای از همان نوع. NULL پایان فهرست است.
- در `struct` خودارجاع باید نام موقتی برای ساختار بگذاری (مثل `struct sllist`)، چون نام نهایی `typedef` تا پایان تعریف هنوز وجود ندارد.
- همیشه اشاره‌گری به گرهٔ اول نگه دار؛ بقیهٔ فهرست از راه زنجیره در دسترس است.
- بعد از هر `malloc` بلافاصله `NULL` را بسنج؛ رفتن به نشانی NULL به segfault می‌رسد.
- جست‌وجو یعنی حرکت با یک اشاره‌گر کمکی (`trav`) از ابتدا تا یافتن مقدار یا رسیدن به NULL؛ این کار O(n) است.
- درج در ابتدا همیشه فوری است؛ درج در انتها بدون اشاره‌گری به انتها O(n) می‌شود.
- ترتیب درست درج: اول گرهٔ تازه را به سر قدیمی وصل کن، بعد سر فهرست را جابه‌جا کن؛ وگرنه بقیهٔ فهرست یتیم می‌شود.
- ویدئو حذف کل فهرست را بازگشتی توضیح می‌دهد: اگر به NULL رسیدی بایست، وگرنه بقیهٔ فهرست را حذف کن و بعد گرهٔ فعلی را آزاد کن. آزاد کردن فقط سر فهرست بقیه را نشت می‌دهد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`singly_linked_lists.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — ساختن داده‌ساختارهای خودمان](https://www.youtube.com/watch?v=zQI3FyWm144&t=0s)
- [۱:۳۷ — مشکل انعطاف‌ناپذیری آرایه](https://www.youtube.com/watch?v=zQI3FyWm144&t=97s)
- [۳:۰۸ — گره: داده و اشاره‌گر](https://www.youtube.com/watch?v=zQI3FyWm144&t=188s)
- [۴:۲۶ — ساختار خودارجاع](https://www.youtube.com/watch?v=zQI3FyWm144&t=266s)
- [۶:۰۶ — ساختن فهرست از هیچ](https://www.youtube.com/watch?v=zQI3FyWm144&t=366s)
- [۹:۱۵ — جست‌وجو در فهرست](https://www.youtube.com/watch?v=zQI3FyWm144&t=555s)
- [۱۳:۰۷ — درج در ابتدا](https://www.youtube.com/watch?v=zQI3FyWm144&t=787s)
- [۱۶:۳۰ — ترتیب اشتباه و یتیم شدن فهرست](https://www.youtube.com/watch?v=zQI3FyWm144&t=990s)
- [۱۸:۰۴ — حذف کل فهرست به‌صورت بازگشتی](https://www.youtube.com/watch?v=zQI3FyWm144&t=1084s)
- [۲۲:۰۰ — چرا حذف یک گره سخت است](https://www.youtube.com/watch?v=zQI3FyWm144&t=1320s)

## مفاهیم مرتبط

- فهرست پیوندی (linked list) — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- گره: یک مقدار و اشاره‌گر next — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- struct خودارجاع: struct node *next — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- NULL پایان فهرست را نشان می‌دهد — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- اشاره‌گر سر فهرست (head) — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- پیمایش فهرست با اشاره‌گر ptr — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u02`)
- افزودن به ابتدای فهرست (prepend) — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u01`)
- اول n->next = list، بعد list = n؛ وگرنه فهرست یتیم می‌شود — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u01`)
- افزودن به انتها (append) با پیمایش؛ O(n) — [یادداشت](/kb/d/w05-n09) · درس کوتاه `w05-l05` (واحد `w05-l05-u01`)
- آزاد کردن کل فهرست با next موقت — [یادداشت](/kb/d/w05-n09) · درس کوتاه `w05-l05` (واحد `w05-l05-u03`)
- هزینهٔ فهرست: درج در ابتدا O(1)، جست‌وجو O(n) — [یادداشت](/kb/d/w05-n08) · درس کوتاه `w05-l04` (واحد `w05-l04-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/zQI3FyWm144) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/singly_linked_lists/singly_linked_lists.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/singly_linked_lists/lang/en/singly_linked_lists.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/singly_linked_lists/lang/en/singly_linked_lists.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
