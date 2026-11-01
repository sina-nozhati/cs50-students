---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-tries
type: short-summary
title: 'ویدئوی کوتاه: ترای‌ها (Tries)'
title_fa: ترای‌ها
title_en: Tries
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/tries/
source_refs:
- src-short-tries
- src-anzali-inference-5
concept_ids:
- w05-c-trie
- w05-c-trie-lookup
- w05-c-trie-memory
- w05-c-time-space-tradeoff
- w05-c-constant-time
prev: w05-sh-hash-tables
next: w05-sh-data-structures
order: 21
video:
  youtube_id: MC-iQHFdEDI
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: در جست‌وجوی جام مقدس
    evidence_en: null
  - start: 0:23
    start_seconds: 23
    title_fa: جفت‌های کلید و مقدار
    evidence_en: key-value pairs
  - start: '1:14'
    start_seconds: 74
    title_fa: کلید یکتا، بدون برخورد
    evidence_en: guaranteed to be unique
  - start: '3:03'
    start_seconds: 183
    title_fa: 'نمونه: دانشگاه‌ها و سال تأسیس'
    evidence_en: name of a university
  - start: '3:25'
    start_seconds: 205
    title_fa: ریشه و شاخه‌ها
    evidence_en: central route
  - start: '6:36'
    start_seconds: 396
    title_fa: درج Harvard
    evidence_en: insert the string Harvard
  - start: '9:50'
    start_seconds: 590
    title_fa: درج Yale
    evidence_en: insert Yale
  - start: '11:32'
    start_seconds: 692
    title_fa: درج Dartmouth
    evidence_en: Dartmouth
  - start: '12:49'
    start_seconds: 769
    title_fa: جست‌وجوی Harvard
    evidence_en: search for Harvard
  - start: '14:11'
    start_seconds: 851
    title_fa: جست‌وجوی Princeton
    evidence_en: Princeton
  - start: '15:07'
    start_seconds: 907
    title_fa: 'جمع‌بندی: زمان ثابت در برابر حافظه'
    evidence_en: only had to make 4 moves
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: ترای‌ها (Tries)

> **منبع رسمی:** [صفحهٔ Short «Tries» در CS50x](https://cs50.harvard.edu/x/shorts/tries/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو می‌پرسد آیا به «جام مقدس» ساختمان‌های داده، یعنی درج، حذف و جست‌وجو در زمان ثابت، رسیده‌ایم. ترای آرایه، ساختار و اشاره‌گر را ترکیب می‌کند و از خود داده (کلید) مثل نقشهٔ راه برای حرکت در ساختار استفاده می‌کند. چون کلیدها یکتا هستند، برخوردی پیش نمی‌آید.

نمونهٔ ویدئو نام دانشگاه‌ها با سال تأسیس چهاررقمی به‌عنوان کلید است: هر گره نام دانشگاه و آرایه‌ای از ۱۰ اشاره‌گر (برای رقم‌های 0 تا 9) دارد. ویدئو درج Harvard (1636)، Yale (1701) و Dartmouth (1769) و جست‌وجوی Harvard و Princeton (1746) را گام به گام نشان می‌دهد.

## نکته‌های کلیدی

- در ترای کلید یکتاست و مسیر از ریشه تا گره را تعیین می‌کند؛ مقدار می‌تواند به سادگی یک بولی (آیا هست؟) یا یک رشته باشد.
- ترای مثل درختی وارونه است: ریشه بالا و برگ‌ها پایین؛ شاخه‌ها با رقم‌ها (یا حرف‌ها) برچسب خورده‌اند.
- اشاره‌گری سراسری به ریشه نگه دار و برای حرکت از اشاره‌گر کمکی (`trav`) استفاده کن.
- برای درج، از ریشه رقم به رقم پایین برو؛ هرجا اشاره‌گر NULL بود گرهٔ تازه بساز (با `malloc`). در پایان کلید، داده را در گره بنویس.
- برای جست‌وجو همان مسیر را برو؛ اگر به NULL رسیدی داده نیست. اگر به پایان رسیدی هم باید داده را در گره بسنجی، چون کلیدی مثل bat می‌تواند پیشوند batch باشد.
- با کلید چهاررقمی همیشه ۴ حرکت لازم است و ۴ ثابت است؛ ولی ترای بسیار بزرگ می‌شود. بده‌بستان: سرعت در برابر حافظه.
- برای واژه‌ها به‌جای ۱۰ اشاره‌گر، ۲۶ اشاره‌گر در هر گره لازم است.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`tries.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — در جست‌وجوی جام مقدس](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=0s)
- [۰:۲۳ — جفت‌های کلید و مقدار](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=23s)
- [۱:۱۴ — کلید یکتا، بدون برخورد](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=74s)
- [۳:۰۳ — نمونه: دانشگاه‌ها و سال تأسیس](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=183s)
- [۳:۲۵ — ریشه و شاخه‌ها](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=205s)
- [۶:۳۶ — درج Harvard](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=396s)
- [۹:۵۰ — درج Yale](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=590s)
- [۱۱:۳۲ — درج Dartmouth](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=692s)
- [۱۲:۴۹ — جست‌وجوی Harvard](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=769s)
- [۱۴:۱۱ — جست‌وجوی Princeton](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=851s)
- [۱۵:۰۷ — جمع‌بندی: زمان ثابت در برابر حافظه](https://www.youtube.com/watch?v=MC-iQHFdEDI&t=907s)

## مفاهیم مرتبط

- ترای: درختی از آرایه‌ها — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- جست‌وجو در ترای: حرف به حرف، مستقل از تعداد کلمه‌ها — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- هزینهٔ حافظهٔ ترای — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- بده‌بستان زمان و حافظه — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u02`)
- O(1)، «جام مقدس» زمان اجرا — [یادداشت](/kb/d/w05-n11) · درس کوتاه `w05-l07` (واحد `w05-l07-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/MC-iQHFdEDI) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/tries/tries.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/tries/lang/en/tries.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/tries/lang/en/tries.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
