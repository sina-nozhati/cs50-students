---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-selection-sort
type: short-summary
title: 'ویدئوی کوتاه: مرتب‌سازی انتخابی (Selection Sort)'
title_fa: مرتب‌سازی انتخابی
title_en: Selection Sort
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/selection_sort/
source_refs:
- src-short-selection-sort
- src-anzali-inference-3
concept_ids:
- w03-c-selection-sort
- w03-c-swap
prev: w03-sh-bubble-sort
next: w03-sh-call-stacks
order: 25
video:
  youtube_id: 3hH8kTHFw2A
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: ایدهٔ اصلی
    evidence_en: null
  - start: 0:22
    start_seconds: 22
    title_fa: شبه‌کد
    evidence_en: Breaking it down to pseudocode
  - start: 0:29
    start_seconds: 29
    title_fa: یافتن کوچک‌ترین و جابه‌جایی
    evidence_en: Search through the unsorted data
  - start: '1:47'
    start_seconds: 107
    title_fa: تکرار فرایند
    evidence_en: Now we just repeat the process again
  - start: '2:47'
    start_seconds: 167
    title_fa: بدترین حالت
    evidence_en: worst case scenario here?
  - start: '3:09'
    start_seconds: 189
    title_fa: بهترین حالت
    evidence_en: What's the best case scenario?
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: مرتب‌سازی انتخابی (Selection Sort)

> **منبع رسمی:** [صفحهٔ Short «Selection Sort» در CS50x](https://cs50.harvard.edu/x/shorts/selection_sort/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ایدهٔ مرتب‌سازی انتخابی این است: کوچک‌ترین عنصر مرتب‌نشده را پیدا کن و به انتهای بخش مرتب اضافه کن. ویدئو بخش مرتب را آبی و بخش مرتب‌نشده را قرمز نشان می‌دهد.

در نمونهٔ ویدئو اول ۱ با ۵ جابه‌جا می‌شود؛ در گام بعد عدد ۲ با خودش جابه‌جا می‌شود که یعنی همان‌جا می‌ماند.

## نکته‌های کلیدی

- شبه‌کد: تا وقتی همه مرتب نشده‌اند، در دادهٔ مرتب‌نشده کوچک‌ترین مقدار را پیدا کن و با اولین عنصر مرتب‌نشده جابه‌جا کن.
- بدترین حالت: برای هر یک از n عنصر باید همهٔ عنصرهای مرتب‌نشده را بگردیم، پس O(n²).
- بهترین حالت: حتی اگر آرایه مرتب باشد، باز باید همه را بگردیم تا مطمئن شویم کوچک‌ترین را داریم، پس Ω(n²).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`selection_sort.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — ایدهٔ اصلی](https://www.youtube.com/watch?v=3hH8kTHFw2A&t=0s)
- [۰:۲۲ — شبه‌کد](https://www.youtube.com/watch?v=3hH8kTHFw2A&t=22s)
- [۰:۲۹ — یافتن کوچک‌ترین و جابه‌جایی](https://www.youtube.com/watch?v=3hH8kTHFw2A&t=29s)
- [۱:۴۷ — تکرار فرایند](https://www.youtube.com/watch?v=3hH8kTHFw2A&t=107s)
- [۲:۴۷ — بدترین حالت](https://www.youtube.com/watch?v=3hH8kTHFw2A&t=167s)
- [۳:۰۹ — بهترین حالت](https://www.youtube.com/watch?v=3hH8kTHFw2A&t=189s)

## مفاهیم مرتبط

- مرتب‌سازی انتخابی — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u01`)
- جابه‌جا کردن دو خانه با متغیر موقت — [یادداشت](/kb/d/w03-n10) · درس کوتاه `w03-l05` (واحد `w03-l05-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/3hH8kTHFw2A) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/selection_sort/selection_sort.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
