---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-sh-defining-custom-types
type: short-summary
title: 'ویدئوی کوتاه: تعریف نوع‌های دلخواه (Defining Custom Types)'
title_fa: تعریف نوع‌های دلخواه
title_en: Defining Custom Types
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/defining_custom_types/
source_refs:
- src-short-defining-custom-types
- src-anzali-inference-4
concept_ids:
- w04-c-typedef
- w04-c-typedef-struct
- w04-c-byte-type
- w04-c-string-char-star
prev: w04-sh-pointers
next: w04-sh-dynamic-memory-allocation
order: 20
video:
  youtube_id: 96M4q0OnMfY
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: دردسر کلیدواژهٔ struct
    evidence_en: null
  - start: 0:43
    start_seconds: 43
    title_fa: typedef نام قدیم نام تازه
    evidence_en: typedef old name new name
  - start: '1:12'
    start_seconds: 72
    title_fa: typedef در cs50.h
    evidence_en: In CS50's library, we do this
  - start: '1:39'
    start_seconds: 99
    title_fa: typedef همراه struct
    evidence_en: typedef becomes great when combined with structures
  - start: '2:28'
    start_seconds: 148
    title_fa: تعریف struct درون typedef
    evidence_en: you can actually define the type in between
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: تعریف نوع‌های دلخواه (Defining Custom Types)

> **منبع رسمی:** [صفحهٔ Short «Defining Custom Types» در CS50x](https://cs50.harvard.edu/x/shorts/defining_custom_types/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

کوتاه‌ترین ویدئوی هفته typedef را معرفی می‌کند: راهی برای ساختن نام کوتاه یا تازه برای یک نوع داده، چه نوع موجود و چه نوعی که خودمان تعریف کرده‌ایم.

نمونه‌ها: نام BYTE برای unsigned char، خط `typedef char *string` در cs50.h، و کوتاه کردن `struct car` به `car_t`.

## نکته‌های کلیدی

- الگوی کلی: `typedef <نام قدیم> <نام تازه>`. این تعریف‌ها معمولاً بالای فایل .c یا در یک فایل .h می‌آیند.
- `typedef unsigned char byte` اجازه می‌دهد هر جا unsigned char لازم بود، نام کوتاه‌تر را بنویسیم.
- کتابخانهٔ CS50 با `typedef char *string` اشاره‌گر را پنهان کرده بود، چون فهم اینکه رشته اشاره‌گری به اولین کاراکتر است در ابتدا گیج‌کننده است.
- typedef با struct مفیدتر است، چون نام نوع struct دوکلمه‌ای است؛ می‌توان struct را جداگانه تعریف و بعد نام‌گذاری کرد، یا struct را درست وسط typedef تعریف کرد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`custom_types.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — دردسر کلیدواژهٔ struct](https://www.youtube.com/watch?v=96M4q0OnMfY&t=0s)
- [۰:۴۳ — typedef نام قدیم نام تازه](https://www.youtube.com/watch?v=96M4q0OnMfY&t=43s)
- [۱:۱۲ — typedef در cs50.h](https://www.youtube.com/watch?v=96M4q0OnMfY&t=72s)
- [۱:۳۹ — typedef همراه struct](https://www.youtube.com/watch?v=96M4q0OnMfY&t=99s)
- [۲:۲۸ — تعریف struct درون typedef](https://www.youtube.com/watch?v=96M4q0OnMfY&t=148s)

## مفاهیم مرتبط

- typedef: نام تازه برای یک نوع (مثل string در cs50.h) — [یادداشت](/kb/d/w04-n05) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)
- typedef همراه struct برای ساختن نوع دلخواه — [یادداشت](/kb/d/w04-sh-defining-custom-types) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)
- نوع BYTE با typedef unsigned char — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)
- رشته همان char * است: نشانی اولین نویسه — [یادداشت](/kb/d/w04-n05) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/96M4q0OnMfY) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/custom_types/custom_types.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
