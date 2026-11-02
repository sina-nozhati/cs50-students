---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sh-arrays
type: short-summary
title: 'ویدئوی کوتاه: آرایه‌ها (Arrays)'
title_fa: آرایه‌ها
title_en: Arrays
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/arrays/
source_refs:
- src-short-arrays
- src-anzali-inference-2
concept_ids:
- w02-c-array
- w02-c-array-index
- w02-c-array-init
- w02-c-array-bounds
- w02-c-array-parameter
prev: w02-sh-debugging-step-into
next: w02-sh-command-line-arguments
order: 26
video:
  youtube_id: K1yC1xshF40
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: آرایه چیست
    evidence_en: null
  - start: 0:44
    start_seconds: 44
    title_fa: تشبیه ادارهٔ پست
    evidence_en: post office
  - start: '2:05'
    start_seconds: 125
    title_fa: اندیس از صفر
    evidence_en: indexed starting from 0
  - start: '2:53'
    start_seconds: 173
    title_fa: بیرون زدن از مرز
    evidence_en: out of bounds
  - start: '3:19'
    start_seconds: 199
    title_fa: اعلان آرایه
    evidence_en: array declaration
  - start: '4:56'
    start_seconds: 296
    title_fa: کار با عنصرها
    evidence_en: Truthtable
  - start: '6:53'
    start_seconds: 413
    title_fa: مقداردهی اولیه با آکولاد
    evidence_en: instantiation syntax
  - start: '8:04'
    start_seconds: 484
    title_fa: آرایهٔ چندبعدی
    evidence_en: single dimension
  - start: '9:44'
    start_seconds: 584
    title_fa: کپی آرایه با حلقه
    evidence_en: copy one array
  - start: '11:20'
    start_seconds: 680
    title_fa: فرستادن آرایه به تابع
    evidence_en: passing by reference
  - start: '12:20'
    start_seconds: 740
    title_fa: تمرین پایانی
    evidence_en: one more exercise
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: آرایه‌ها (Arrays)

> **منبع رسمی:** [صفحهٔ Short «Arrays» در CS50x](https://cs50.harvard.edu/x/shorts/arrays/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

آرایه مقدارهای هم‌نوع را در خانه‌های پشت سر هم حافظه نگه می‌دارد تا لازم نباشد به هر کدام نام جدا بدهی. Doug آرایه را به دیوار صندوق‌های پستی یک ادارهٔ پست تشبیه می‌کند: خانه‌های هم‌اندازه، هر کدام با یک شماره.

ویدئو اعلان آرایه، اندیس‌گذاری از صفر، خطر بیرون زدن از مرز آرایه، مقداردهی اولیه با آکولاد، آرایهٔ چندبعدی، کپی کردن آرایه با حلقه و فرستادن آرایه به تابع را پوشش می‌دهد.

## نکته‌های کلیدی

- اندیس‌ها از 0 شروع می‌شوند: در آرایهٔ n عنصری، اولین عنصر در اندیس 0 و آخرین در اندیس n منهای 1 است.
- C جلوی دسترسی بیرون از مرز آرایه را نمی‌گیرد؛ برنامه کامپایل می‌شود اما ممکن است هنگام اجرا با segmentation fault روبه‌رو شوی.
- اعلان آرایه سه بخش دارد: نوع، نام و اندازه در کروشه؛ مثلاً `int student_grades[40];`.
- با فهرست مقداردهی در آکولاد می‌توان آرایه را هنگام اعلان پر کرد؛ در این حالت می‌توان اندازه را ننوشت و کامپایلر خودش می‌شمارد.
- آرایهٔ چندبعدی مثل `bool battleship[10][10]` در حافظه در واقع یک آرایهٔ یک‌بعدی ۱۰۰ خانه‌ای است؛ شبکه فقط یک انتزاع برای ذهن ماست.
- یک آرایه را نمی‌شود با `=` در آرایهٔ دیگر ریخت؛ باید با حلقه عنصر‌به‌عنصر کپی کرد.
- به گفتهٔ ویدئو، آرایه برخلاف متغیرهای معمولی «by reference» به تابع فرستاده می‌شود و تابع خود آرایه را می‌گیرد، نه کپی آن. چرایی‌اش به هفته‌های بعد موکول می‌شود (ناهمخوانی d30).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`arrays.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — آرایه چیست](https://www.youtube.com/watch?v=K1yC1xshF40&t=0s)
- [۰:۴۴ — تشبیه ادارهٔ پست](https://www.youtube.com/watch?v=K1yC1xshF40&t=44s)
- [۲:۰۵ — اندیس از صفر](https://www.youtube.com/watch?v=K1yC1xshF40&t=125s)
- [۲:۵۳ — بیرون زدن از مرز](https://www.youtube.com/watch?v=K1yC1xshF40&t=173s)
- [۳:۱۹ — اعلان آرایه](https://www.youtube.com/watch?v=K1yC1xshF40&t=199s)
- [۴:۵۶ — کار با عنصرها](https://www.youtube.com/watch?v=K1yC1xshF40&t=296s)
- [۶:۵۳ — مقداردهی اولیه با آکولاد](https://www.youtube.com/watch?v=K1yC1xshF40&t=413s)
- [۸:۰۴ — آرایهٔ چندبعدی](https://www.youtube.com/watch?v=K1yC1xshF40&t=484s)
- [۹:۴۴ — کپی آرایه با حلقه](https://www.youtube.com/watch?v=K1yC1xshF40&t=584s)
- [۱۱:۲۰ — فرستادن آرایه به تابع](https://www.youtube.com/watch?v=K1yC1xshF40&t=680s)
- [۱۲:۲۰ — تمرین پایانی](https://www.youtube.com/watch?v=K1yC1xshF40&t=740s)

## مفاهیم مرتبط

- آرایه — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u02`)
- اندیس آرایه از صفر — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u02`)
- مقداردهی اولیهٔ آرایه با آکولاد و آرایهٔ چندبعدی — [یادداشت](/kb/d/w02-sh-arrays) · درس کوتاه `w02-l04` (واحد `w02-l04-u04`)
- بیرون زدن از مرز آرایه و segmentation fault — [یادداشت](/kb/d/w02-sh-arrays) · درس کوتاه `w02-l04` (واحد `w02-l04-u04`)
- آرایه به‌عنوان پارامتر تابع — [یادداشت](/kb/d/w02-n10) · درس کوتاه `w02-l05` (واحد `w02-l05-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/K1yC1xshF40) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/arrays/arrays.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/arrays/lang/en/arrays.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/arrays/lang/en/arrays.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
