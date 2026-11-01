---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sh-structures
type: short-summary
title: 'ویدئوی کوتاه: ساختارها (struct) (Structures)'
title_fa: ساختارها (struct)
title_en: Structures
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/structures/
source_refs:
- src-short-structures
- src-anzali-inference-5
concept_ids:
- w05-c-arrow-operator
- w05-c-multi-file-program
prev: w05-sec
next: w05-sh-singly-linked-lists
order: 15
video:
  youtube_id: E4lb2gkyXr8
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: نیاز به نوع دادهٔ تازه
    evidence_en: null
  - start: 0:22
    start_seconds: 22
    title_fa: ساختار چیست؟
    evidence_en: unify variables of different types
  - start: '2:00'
    start_seconds: 120
    title_fa: فیلدها و نمونهٔ struct car
    evidence_en: so-called fields
  - start: '2:26'
    start_seconds: 146
    title_fa: نقطه‌ویرگول پایانی
    evidence_en: semicolon at the end
  - start: '2:58'
    start_seconds: 178
    title_fa: کجا تعریف کنیم؟
    evidence_en: define our structures at the very top
  - start: '3:39'
    start_seconds: 219
    title_fa: عملگر نقطه
    evidence_en: dot operator
  - start: '4:53'
    start_seconds: 293
    title_fa: ساختار پویا با malloc
    evidence_en: do not need to be created on the stack
  - start: '6:51'
    start_seconds: 411
    title_fa: عملگر پیکان
    evidence_en: operator called arrow
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: ساختارها (struct) (Structures)

> **منبع رسمی:** [صفحهٔ Short «Structures» در CS50x](https://cs50.harvard.edu/x/shorts/structures/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو با این پرسش شروع می‌کند که چطور نوع دادهٔ تازه بسازیم. پاسخ `struct` است: راهی برای کنار هم گذاشتن متغیرهایی از نوع‌های مختلف در یک نوع تازه، چیزی شبیه یک «اَبَرمتغیر». نمونهٔ ویدئو `struct car` است با سال، مدل، پلاک، کیلومترشمار و حجم موتور.

سپس ویدئو جای تعریف ساختار (بالای برنامه یا در فایل `.h`)، دسترسی به فیلدها با عملگر نقطه، ساختن ساختار با `malloc` و در پایان عملگر پیکان `->` را توضیح می‌دهد که رفتن به نشانی و دسترسی به فیلد را یکجا انجام می‌دهد.

## نکته‌های کلیدی

- `struct` متغیرهایی از نوع‌های مختلف را در یک واحد منطقی جمع می‌کند؛ آرایه فقط مقدارهای هم‌نوع را.
- نام نوع در نمونهٔ ویدئو `struct car` است، نه فقط `car`؛ فیلدها (members) داخل آکولادها می‌آیند.
- بعد از آکولاد بستهٔ تعریف ساختار نقطه‌ویرگول لازم است؛ ویدئو این را خطای نحوی رایجی می‌داند.
- ساختارها را معمولاً بالای برنامه یا در یک فایل `.h` تعریف می‌کنند تا همهٔ تابع‌ها (و فایل‌ها) به آن دسترسی داشته باشند.
- با متغیر ساختاری، فیلد را با نقطه می‌خوانی و می‌نویسی، مثل `mycar.year = 2011`.
- اگر ساختار را با `malloc` ساخته باشی و فقط اشاره‌گر داشته باشی، اول باید به نشانی بروی و بعد فیلد را بخوانی: `(*mycar).year`.
- عملگر پیکان همین دو کار را یکجا انجام می‌دهد: `mycar->year`. نقطه برای خود متغیر، پیکان برای اشاره‌گر به آن.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`structures.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — نیاز به نوع دادهٔ تازه](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=0s)
- [۰:۲۲ — ساختار چیست؟](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=22s)
- [۲:۰۰ — فیلدها و نمونهٔ struct car](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=120s)
- [۲:۲۶ — نقطه‌ویرگول پایانی](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=146s)
- [۲:۵۸ — کجا تعریف کنیم؟](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=178s)
- [۳:۳۹ — عملگر نقطه](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=219s)
- [۴:۵۳ — ساختار پویا با malloc](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=293s)
- [۶:۵۱ — عملگر پیکان](https://www.youtube.com/watch?v=E4lb2gkyXr8&t=411s)

## مفاهیم مرتبط

- عملگر پیکان -> : رفتن به نشانی و نگاه به فیلد — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u02`)
- برنامهٔ چندفایلی: .h، .c و Makefile — [یادداشت](/kb/d/w05-ps-speller)

## منابع

- [ویدئو در YouTube](https://youtu.be/E4lb2gkyXr8) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/structures/structures.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
