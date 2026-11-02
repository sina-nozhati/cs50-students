---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-bubble-sort
type: short-summary
title: 'ویدئوی کوتاه: مرتب‌سازی حبابی (Bubble Sort)'
title_fa: مرتب‌سازی حبابی
title_en: Bubble Sort
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/bubble_sort/
source_refs:
- src-short-bubble-sort
- src-anzali-inference-3
concept_ids:
- w03-c-bubble-sort
- w03-c-early-exit-no-swaps
- w03-c-swap
prev: w03-sh-binary-search
next: w03-sh-selection-sort
order: 24
video:
  youtube_id: RT-hUXUWQ2I
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: ایدهٔ حبابی
    evidence_en: null
  - start: 0:26
    start_seconds: 26
    title_fa: شمارندهٔ جابه‌جایی
    evidence_en: set a swap counter to a non-zero value
  - start: '1:37'
    start_seconds: 97
    title_fa: شروع نمونه
    evidence_en: So let's begin this process
  - start: '2:26'
    start_seconds: 146
    title_fa: مقایسه با انتخابی
    evidence_en: So in selection sort, if you've seen
  - start: '3:06'
    start_seconds: 186
    title_fa: تکرار تا صفر شدن شمارنده
    evidence_en: repeat until the swap counter is 0
  - start: '4:38'
    start_seconds: 278
    title_fa: بدترین حالت
    evidence_en: worst case scenario with bubble sort
  - start: '5:01'
    start_seconds: 301
    title_fa: بهترین حالت
    evidence_en: In the best case scenario though
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: مرتب‌سازی حبابی (Bubble Sort)

> **منبع رسمی:** [صفحهٔ Short «Bubble Sort» در CS50x](https://cs50.harvard.edu/x/shorts/bubble_sort/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

در مرتب‌سازی حبابی عنصرهای بزرگ‌تر به سمت راست و کوچک‌ترها به سمت چپ «حباب‌وار» حرکت می‌کنند. ویدئو برای این کار یک **شمارندهٔ جابه‌جایی** (`swap counter`) نگه می‌دارد.

نمونه روی یک آرایهٔ کوچک اجرا می‌شود (اولین جفت ۵ و ۲ است که جابه‌جا می‌شوند) و بعد بدترین و بهترین حالت با مرتب‌سازی انتخابی مقایسه می‌شود.

## نکته‌های کلیدی

- شبه‌کد: شمارنده را مقداری غیرصفر بگذار؛ تا صفر نشده تکرار کن: شمارنده را صفر کن، هر جفت کنار هم را نگاه کن و اگر ترتیبشان غلط است جابه‌جا کن و یکی به شمارنده اضافه کن.
- بعد از هر گذر، بزرگ‌ترین عنصر بخش مرتب‌نشده به جای نهایی‌اش می‌رسد و دیگر لازم نیست بررسی شود.
- بدترین حالت: آرایه کاملاً برعکس است؛ هر عنصر باید تا آن سر آرایه برود، پس O(n²).
- بهترین حالت: آرایه از قبل مرتب است؛ در اولین گذر هیچ جابه‌جایی رخ نمی‌دهد و کار تمام است، پس Ω(n). این از انتخابی بهتر است.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`bubble_sort.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — ایدهٔ حبابی](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=0s)
- [۰:۲۶ — شمارندهٔ جابه‌جایی](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=26s)
- [۱:۳۷ — شروع نمونه](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=97s)
- [۲:۲۶ — مقایسه با انتخابی](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=146s)
- [۳:۰۶ — تکرار تا صفر شدن شمارنده](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=186s)
- [۴:۳۸ — بدترین حالت](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=278s)
- [۵:۰۱ — بهترین حالت](https://www.youtube.com/watch?v=RT-hUXUWQ2I&t=301s)

## مفاهیم مرتبط

- مرتب‌سازی حبابی — [یادداشت](/kb/d/w03-n11) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)
- توقف زودهنگام وقتی جابه‌جایی رخ نداد — [یادداشت](/kb/d/w03-n11) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)
- جابه‌جا کردن دو خانه با متغیر موقت — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/RT-hUXUWQ2I) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/bubble_sort/bubble_sort.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/bubble_sort/lang/en/bubble_sort.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/bubble_sort/lang/en/bubble_sort.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
