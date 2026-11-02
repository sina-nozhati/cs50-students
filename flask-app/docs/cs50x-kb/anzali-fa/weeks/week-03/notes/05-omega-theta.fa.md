---
id: w03-n05
type: note
title: 'امگا و تتا: کران پایین و کران دقیق (Running Time: Omega and Theta)'
title_fa: 'امگا و تتا: کران پایین و کران دقیق'
title_en: 'Running Time: Omega and Theta'
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Running Time
official_anchor: running-time
source_url: https://cs50.harvard.edu/x/2026/notes/3/#running-time
source_refs:
- src-notes-3#running-time
- src-transcript-3
- src-short-linear-search
- src-short-binary-search
- src-section-3
- src-section-3-transcript
- src-anzali-authored-3
- src-anzali-inference-3
- src-srt-3
concept_ids:
- w03-c-omega
- w03-c-theta
- w03-c-asymptotic-notation
prev: w03-n04
next: w03-n06
order: 5
video:
  youtube_id: 6Svu_ae5ebk
  start: '35:53'
  start_seconds: 2153
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=2153s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'Omega,'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# امگا و تتا: کران پایین و کران دقیق

> **منبع رسمی:** بخش «Running Time» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#running-time). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۵:۵۳ تا حدود ۳۸:۵۴](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=2153s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

O بزرگ می‌گوید اوضاع **چقدر بد** می‌تواند بشود. اما گاهی می‌خواهی بدانی در **بهترین** حالت چه می‌شود: اگر داده از قبل مرتب باشد، آیا الگوریتم زود می‌فهمد؟ این‌جا دو نماد یونانی به کمک می‌آیند.

## کران بالا و کران پایین

- برنامه‌نویس‌ها هم به **بدترین حالت** یا **کران بالا** (`upper bound`) علاقه دارند و هم به **بهترین حالت** یا **کران پایین** (`lower bound`).
- نماد **Ω** (امگای بزرگ، `Omega`) برای بهترین حالت یک الگوریتم به کار می‌رود؛ درس‌نامه نمونهٔ `Ω(log n)` را می‌آورد.
- نماد **Θ** (تتای بزرگ، `Theta`) وقتی به کار می‌رود که کران بالا و کران پایین **یکی** باشند: یعنی بهترین و بدترین حالت زمان اجرای یکسانی دارند.

## نمادگذاری مجانبی

- **نمادگذاری مجانبی** (`asymptotic notation`) معیار این است که الگوریتم‌ها وقتی ورودی بزرگ و بزرگ‌تر می‌شود، چقدر خوب کار می‌کنند.
- درس‌نامه می‌گوید در ادامهٔ مسیر علوم کامپیوتر، این موضوع‌ها را در درس‌های بعدی با جزئیات بیشتری خواهی دید.

## جدول خلاصهٔ هفته (تألیفی، با عددهای رسمی)

| الگوریتم | O (بدترین) | Ω (بهترین) | Θ؟ |
| --- | --- | --- | --- |
| جست‌وجوی خطی | `O(n)` | `Ω(1)` | ندارد |
| جست‌وجوی دودویی | `O(log n)` | `Ω(1)` | ندارد |
| مرتب‌سازی انتخابی | `O(n²)` | `Ω(n²)` | `Θ(n²)` |
| مرتب‌سازی حبابی | `O(n²)` | `Ω(n)` | ندارد |
| مرتب‌سازی ادغامی | `O(n log n)` | `Ω(n log n)` | `Θ(n log n)` |

- Ω جست‌وجوها از سخنرانی و ویدئوهای کوتاه Linear Search و Binary Search آمده‌اند: شاید عدد مورد نظر را **در همان اولین نگاه** پیدا کنی.
- عددهای مرتب‌سازی‌ها را درس‌نامه در بخش‌های خودشان می‌دهد. Θ مرتب‌سازی ادغامی صریحاً در درس‌نامه آمده و Θ انتخابی نتیجهٔ مستقیم برابری O و Ω آن است (استنتاج).

> [!NOTE]
> **نکته**
> **از سخنرانی:** David گفت تا آن لحظه هیچ‌کدام از الگوریتم‌ها با Θ توصیف‌پذیر نبودند، چون O و Ω آن‌ها با هم فرق داشت. گفتن Θ به یک دانشمند کامپیوتر دیگر مثل این است که با یک کلمه دو برابر اطلاعات بدهی.

> [!WARNING]
> **هشدار**
> O بزرگ را «میانگین» نخوان. O کران بالاست، Ω کران پایین، و Θ فقط وقتی معنا دارد که این دو برابر باشند. **از جلسهٔ حل تمرین:** در پاسخ به سؤالی دربارهٔ «زمان اجرای میانگین»، Kelly توضیح داد که Θ برای وقتی است که کران بالا و پایین یکی‌اند و معمولاً O و Ω را برای توصیف کران بالا و پایین به کار می‌بریم.

## اشتباه‌های رایج

- نوشتن `Θ(n)` برای جست‌وجوی خطی؛ بهترین و بدترین حالتش یکی نیست.
- فکر کردن به اینکه Ω همیشه عدد کوچکی است؛ مرتب‌سازی انتخابی حتی در بهترین حالت `Ω(n²)` است.

## جمع‌بندی

- O: بدترین حالت، کران بالا. Ω: بهترین حالت، کران پایین. Θ: وقتی این دو یکی‌اند.
- نمادگذاری مجانبی دربارهٔ رفتار الگوریتم برای ورودی‌های **بزرگ** است.

## پیوندها

- قبلی: [زمان اجرا و نماد O بزرگ](/kb/d/w03-n04)
- بعدی: [search.c: جست‌وجوی خطی اعداد در C](/kb/d/w03-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
