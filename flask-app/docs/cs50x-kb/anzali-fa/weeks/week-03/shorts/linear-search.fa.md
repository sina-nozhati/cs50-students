---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-linear-search
type: short-summary
title: 'ویدئوی کوتاه: جست‌وجوی خطی (Linear Search)'
title_fa: جست‌وجوی خطی
title_en: Linear Search
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/linear_search/
source_refs:
- src-short-linear-search
- src-anzali-inference-3
concept_ids:
- w03-c-linear-search
- w03-c-omega
prev: w03-sec
next: w03-sh-binary-search
order: 22
video:
  youtube_id: TwsgCHYmbbA
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: معرفی جست‌وجوی خطی
    evidence_en: null
  - start: 0:17
    start_seconds: 17
    title_fa: شبه‌کد
    evidence_en: In pseudocode
  - start: 0:36
    start_seconds: 36
    title_fa: 'نمونه: یافتن ۹'
    evidence_en: target value nine
  - start: '1:25'
    start_seconds: 85
    title_fa: 'نمونه: ۵۰ که در آرایه نیست'
    evidence_en: hoping that we find the number 50
  - start: '2:00'
    start_seconds: 120
    title_fa: بدترین حالت
    evidence_en: worst case scenario with linear search
  - start: '2:14'
    start_seconds: 134
    title_fa: بهترین حالت
    evidence_en: best case scenario?
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: جست‌وجوی خطی (Linear Search)

> **منبع رسمی:** [صفحهٔ Short «Linear Search» در CS50x](https://cs50.harvard.edu/x/shorts/linear_search/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو جست‌وجوی خطی را ساده‌ترین الگوریتم جست‌وجو معرفی می‌کند: از چپ به راست روی آرایه حرکت کن تا عنصر را پیدا کنی یا آرایه تمام شود.

دو نمونه دنبال می‌شود: یک بار مقدار هدف ۹ پیدا می‌شود و یک بار دنبال ۵۰ می‌گردیم که در آرایه نیست. در پایان بدترین و بهترین حالت تحلیل می‌شود.

## نکته‌های کلیدی

- شبه‌کد: تکرار از اول تا آخر آرایه؛ اگر عنصر اول همان هدف است، تمام؛ وگرنه به عنصر بعدی برو.
- برای ۵۰، فقط وقتی همهٔ عنصرها را دیده‌ایم می‌توانیم نتیجه بگیریم که ۵۰ در آرایه نیست.
- بدترین حالت: باید به همهٔ n عنصر نگاه کنیم (چه عنصر آخر باشد، چه اصلاً نباشد)، پس O(n).
- بهترین حالت: عنصر را بلافاصله در اولین خانه پیدا می‌کنیم، پس Ω(1).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`linear_search.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — معرفی جست‌وجوی خطی](https://www.youtube.com/watch?v=TwsgCHYmbbA&t=0s)
- [۰:۱۷ — شبه‌کد](https://www.youtube.com/watch?v=TwsgCHYmbbA&t=17s)
- [۰:۳۶ — نمونه: یافتن ۹](https://www.youtube.com/watch?v=TwsgCHYmbbA&t=36s)
- [۱:۲۵ — نمونه: ۵۰ که در آرایه نیست](https://www.youtube.com/watch?v=TwsgCHYmbbA&t=85s)
- [۲:۰۰ — بدترین حالت](https://www.youtube.com/watch?v=TwsgCHYmbbA&t=120s)
- [۲:۱۴ — بهترین حالت](https://www.youtube.com/watch?v=TwsgCHYmbbA&t=134s)

## مفاهیم مرتبط

- جست‌وجوی خطی — [یادداشت](/kb/d/w03-n02) · درس کوتاه `w03-l01` (واحد `w03-l01-u02`)
- نماد Ω: کران پایین یا بهترین حالت — [یادداشت](/kb/d/w03-n05) · درس کوتاه `w03-l02` (واحد `w03-l02-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/TwsgCHYmbbA) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/linear_search/linear_search.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
