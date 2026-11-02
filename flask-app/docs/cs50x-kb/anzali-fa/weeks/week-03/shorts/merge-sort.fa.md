---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-merge-sort
type: short-summary
title: 'ویدئوی کوتاه: مرتب‌سازی ادغامی (Merge Sort)'
title_fa: مرتب‌سازی ادغامی
title_en: Merge Sort
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/merge_sort/
source_refs:
- src-short-merge-sort
- src-anzali-inference-3
concept_ids:
- w03-c-merge-sort
- w03-c-merging
- w03-c-n-log-n
- w03-c-memory-tradeoff
prev: w03-sh-recursion
next: w03-ps-sort
order: 28
video:
  youtube_id: Ns7tGNbtvV4
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: الگوریتم‌های n²
    evidence_en: null
  - start: 0:23
    start_seconds: 23
    title_fa: ایدهٔ ادغامی
    evidence_en: using an algorithm called merge sort
  - start: '1:42'
    start_seconds: 102
    title_fa: نیمهٔ چپ را مرتب کن
    evidence_en: sort the left half of this brick red
  - start: '5:06'
    start_seconds: 306
    title_fa: ادغام نیمه‌ها
    evidence_en: Well, two is lower
  - start: '6:28'
    start_seconds: 388
    title_fa: نیمهٔ راست
    evidence_en: Now I'm going to sort the right half
  - start: '8:47'
    start_seconds: 527
    title_fa: بدترین حالت
    evidence_en: In the worst case scenario, we have to split
  - start: '9:06'
    start_seconds: 546
    title_fa: بهترین حالت و حافظه
    evidence_en: In the best case scenario, sort of like
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: مرتب‌سازی ادغامی (Merge Sort)

> **منبع رسمی:** [صفحهٔ Short «Merge Sort» در CS50x](https://cs50.harvard.edu/x/shorts/merge_sort/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

مرتب‌سازی ادغامی آرایه‌های کوچک‌تر را مرتب می‌کند و بعد آن‌ها را به ترتیب **ادغام** می‌کند. ویدئو یادآوری می‌کند که حبابی، درجی (insertion sort) و انتخابی همه در بدترین حالت n² هستند و ادغامی بهتر است.

نمونه روی یک آرایهٔ شش‌عضوی اجرا می‌شود؛ وقتی تعداد عضوها فرد است، نیمهٔ چپ را کوچک‌تر می‌گیرد.

## نکته‌های کلیدی

- ایده: نیمهٔ چپ را مرتب کن، نیمهٔ راست را مرتب کن، دو نیمه را ادغام کن. آرایهٔ تک‌عضوی خودبه‌خود مرتب است.
- ویدئو بازگشت را قدم‌به‌قدم دنبال می‌کند: «نمی‌دانم چطور نیمهٔ چپ را مرتب کنم؟ پس نیمهٔ چپِ نیمهٔ چپ را مرتب می‌کنم» تا به تک‌عضوی‌ها برسد.
- بدترین حالت: n عنصر را log n بار نصف می‌کنیم و n عنصر را دوباره ترکیب می‌کنیم، پس O(n log n).
- بهترین حالت: مثل انتخابی، حتی آرایهٔ مرتب هم کامل نصف و ادغام می‌شود، پس Ω(n log n). روی آرایهٔ مرتب حتی ممکن است از حبابی کندتر باشد.
- ادغامی احتمالاً **حافظهٔ بیشتری** می‌گیرد، چون برای زیرآرایه‌ها بخش‌های تازه‌ای در حافظه ساخته می‌شود.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`merge_sort.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — الگوریتم‌های n²](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=0s)
- [۰:۲۳ — ایدهٔ ادغامی](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=23s)
- [۱:۴۲ — نیمهٔ چپ را مرتب کن](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=102s)
- [۵:۰۶ — ادغام نیمه‌ها](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=306s)
- [۶:۲۸ — نیمهٔ راست](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=388s)
- [۸:۴۷ — بدترین حالت](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=527s)
- [۹:۰۶ — بهترین حالت و حافظه](https://www.youtube.com/watch?v=Ns7tGNbtvV4&t=546s)

## مفاهیم مرتبط

- مرتب‌سازی ادغامی — [یادداشت](/kb/d/w03-n14) · درس کوتاه `w03-l07` (واحد `w03-l07-u01`)
- ادغام دو نیمهٔ مرتب — [یادداشت](/kb/d/w03-n14) · درس کوتاه `w03-l07` (واحد `w03-l07-u01`)
- چرا ادغامی n log n است: log n سطح × n کار — [یادداشت](/kb/d/w03-n14) · درس کوتاه `w03-l07` (واحد `w03-l07-u02`)
- بده‌بستان زمان و حافظه در ادغامی — [یادداشت](/kb/d/w03-sh-merge-sort) · درس کوتاه `w03-l07` (واحد `w03-l07-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/Ns7tGNbtvV4) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/merge_sort/merge_sort.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/merge_sort/lang/en/merge_sort.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/merge_sort/lang/en/merge_sort.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
