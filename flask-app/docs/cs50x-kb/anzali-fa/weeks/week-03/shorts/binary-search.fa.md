---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-binary-search
type: short-summary
title: 'ویدئوی کوتاه: جست‌وجوی دودویی (Binary Search)'
title_fa: جست‌وجوی دودویی
title_en: Binary Search
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/binary_search/
source_refs:
- src-short-binary-search
- src-anzali-inference-3
concept_ids:
- w03-c-binary-search
- w03-c-sorted-precondition
prev: w03-sh-linear-search
next: w03-sh-bubble-sort
order: 23
video:
  youtube_id: T98PIp4omUA
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: تقسیم و غلبه
    evidence_en: null
  - start: 0:29
    start_seconds: 29
    title_fa: پیش‌شرط مرتب بودن
    evidence_en: if the array is sorted
  - start: 0:52
    start_seconds: 52
    title_fa: شبه‌کد
    evidence_en: pseudocode steps for binary search
  - start: '3:17'
    start_seconds: 197
    title_fa: 'نمونه: یافتن ۱۹'
    evidence_en: trying to find the number 19
  - start: '5:19'
    start_seconds: 319
    title_fa: 'نمونه: ۱۶ که در آرایه نیست'
    evidence_en: look for the element 16
  - start: '8:17'
    start_seconds: 497
    title_fa: بدترین حالت
    evidence_en: In the worst case scenario, we had to split
  - start: '8:42'
    start_seconds: 522
    title_fa: بهترین حالت
    evidence_en: What's the best case scenario?
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: جست‌وجوی دودویی (Binary Search)

> **منبع رسمی:** [صفحهٔ Short «Binary Search» در CS50x](https://cs50.harvard.edu/x/shorts/binary_search/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

جست‌وجوی دودویی «تقسیم و غلبه» است: هر بار ناحیهٔ جست‌وجو را نصف می‌کنیم. شرطش این است که آرایه مرتب باشد؛ روی آرایهٔ نامرتب نمی‌شود این کار را کرد.

ویدئو با یک آرایهٔ ۱۵ عضوی (اندیس ۰ تا ۱۴) و متغیرهای نقطهٔ شروع، پایان و وسط کار می‌کند: یک بار ۱۹ را پیدا می‌کند و یک بار نشان می‌دهد ۱۶ در آرایه نیست.

## نکته‌های کلیدی

- شبه‌کد: تکرار تا وقتی زیرآرایه به اندازهٔ صفر برسد؛ وسط زیرآرایه را حساب کن؛ اگر هدف همان است، تمام؛ اگر کوچک‌تر است، پایان را به چپ وسط ببر؛ اگر بزرگ‌تر است، شروع را به راست وسط ببر.
- برای ۱۹، وسط اول اندیس ۷ (مقدار ۱۵) و وسط دوم اندیس ۱۱ است؛ بعد ناحیه به اندیس‌های ۸ تا ۱۰ محدود می‌شود و ۱۹ پیدا می‌شود.
- برای ۱۶، سرانجام نقطهٔ شروع از نقطهٔ پایان جلو می‌زند؛ این یعنی هدف در آرایه نیست.
- بدترین حالت: آرایه را تا یک عنصر نصف می‌کنیم، پس O(log n). بهترین حالت: هدف همان وسط اول است، پس Ω(1).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`binary_search.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — تقسیم و غلبه](https://www.youtube.com/watch?v=T98PIp4omUA&t=0s)
- [۰:۲۹ — پیش‌شرط مرتب بودن](https://www.youtube.com/watch?v=T98PIp4omUA&t=29s)
- [۰:۵۲ — شبه‌کد](https://www.youtube.com/watch?v=T98PIp4omUA&t=52s)
- [۳:۱۷ — نمونه: یافتن ۱۹](https://www.youtube.com/watch?v=T98PIp4omUA&t=197s)
- [۵:۱۹ — نمونه: ۱۶ که در آرایه نیست](https://www.youtube.com/watch?v=T98PIp4omUA&t=319s)
- [۸:۱۷ — بدترین حالت](https://www.youtube.com/watch?v=T98PIp4omUA&t=497s)
- [۸:۴۲ — بهترین حالت](https://www.youtube.com/watch?v=T98PIp4omUA&t=522s)

## مفاهیم مرتبط

- جست‌وجوی دودویی روی آرایهٔ مرتب — [یادداشت](/kb/d/w03-n03) · درس کوتاه `w03-l01` (واحد `w03-l01-u03`)
- پیش‌شرط مرتب بودن برای جست‌وجوی دودویی — [یادداشت](/kb/d/w03-n03) · درس کوتاه `w03-l01` (واحد `w03-l01-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/T98PIp4omUA) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/binary_search/binary_search.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/binary_search/lang/en/binary_search.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/binary_search/lang/en/binary_search.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
