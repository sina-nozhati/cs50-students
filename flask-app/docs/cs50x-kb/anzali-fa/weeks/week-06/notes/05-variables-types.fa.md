---
id: w06-n05
type: note
title: متغیرها و نوع‌ها (Variables and Types)
title_fa: متغیرها و نوع‌ها
title_en: Variables and Types
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Types
official_anchor: types
source_url: https://cs50.harvard.edu/x/2026/notes/6/#types
source_refs:
- src-notes-6#types
- src-notes-6#variables
- src-short-python
- src-anzali-authored-6
- src-srt-6
concept_ids:
- w06-c-no-declaration
- w06-c-augmented-assignment
- w06-c-python-types
- w06-c-no-long-double
- w06-c-collection-types
prev: w06-n04
next: w06-n06
order: 5
video:
  youtube_id: Rl0ludWTLxs
  start: '38:16'
  start_seconds: 2296
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=2296s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'what about the various types that exist in Python'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# متغیرها و نوع‌ها

> **منبع رسمی:** بخش «Types» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#types). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۸:۱۶ تا حدود ۴۰:۰۴](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=2296s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در C پیش از استفاده از هر متغیر باید نوعش را اعلام می‌کردی و حواست به اندازهٔ نوع‌ها بود. پایتون این بار را از دوشت برمی‌دارد، اما نوع‌ها هنوز وجود دارند و رفتار برنامه را تعیین می‌کنند.

## متغیرها

- اعلان متغیر هم ساده‌تر شده است. در C ممکن بود بنویسی `int counter = 0;`. در پایتون همین سطر می‌شود `counter = 0`. لازم نیست نوع متغیر را اعلام کنی.
- پایتون برای افزودن یک واحد `counter += 1` را ترجیح می‌دهد؛ امکان نوشتن `counter++` که در C داشتی، در پایتون نیست.

## نوع‌ها

- نوع داده‌ها در پایتون لازم نیست صریحاً اعلام شوند. مثلاً دیدی که `answer` در یادداشت قبل یک رشته بود، اما لازم نبود این را به مفسر بگوییم؛ خودش می‌دانست.
- نوع‌های پرکاربرد در پایتون:

```text
bool
float
int
str
```

- `long` و `double` در فهرست نیستند. پایتون خودش تصمیم می‌گیرد برای عددهای بزرگ‌تر و کوچک‌تر از چه نوع داده‌ای استفاده کند.
- چند نوع دادهٔ دیگر در پایتون:

```text
range   sequence of numbers
list    sequence of mutable values
tuple   sequence of immutable values
dict    collection of key-value pairs
set     collection of unique values
```

- همهٔ این نوع‌ها را می‌شود در C هم پیاده کرد، اما در پایتون بسیار ساده‌تر به دست می‌آیند.

> [!TIP]
> **تألیفی: عدد صحیح بدون سرریز**
> در هفتهٔ ۱ دیدی که `int` در C چهار بایت است و با رسیدن به حدود دو میلیارد **سرریز** می‌کند. `int` در پایتون اندازهٔ ثابت ندارد و تا جایی که حافظه اجازه دهد بزرگ می‌شود؛ مثلاً `print(2 ** 100)` عدد ۳۱ رقمی درستی چاپ می‌کند (اجراشده روی جعبهٔ ساخت). اما `float` پایتون همان دقت محدود را دارد (یادداشت ۱۰).

> [!NOTE]
> **از ویدئوی کوتاه: True و False**
> در ویدئوی کوتاه «Python»، Doug Lloyd یادآوری می‌کند که مقدارهای بولی در پایتون `True` و `False` با حرف اول بزرگ‌اند، نه `true` و `false` مثل C.

## اشتباه‌های رایج

- نوشتن `counter++` در پایتون؛ این نحو در پایتون وجود ندارد و خطای نحوی می‌دهد.
- این برداشت که چون نوع را اعلام نمی‌کنی، پایتون «نوع ندارد»؛ هر مقدار نوع دارد و مثلاً `"3" + 1` خطا می‌دهد.
- نوشتن `true` با حرف کوچک.

## جمع‌بندی

- متغیر بدون اعلان نوع: `counter = 0`؛ افزایش با `+=`.
- نوع‌های پرکاربرد: `bool`، `float`، `int`، `str`؛ `long` و `double` نیست.
- نوع‌های دیگر: `range`، `list`، `tuple`، `dict`، `set`.

## پیوندها

- قبلی: [رشته‌ها، f-string و پارامترهای نام‌دار print](/kb/d/w06-n04)
- بعدی: [ماشین‌حساب: input همیشه str برمی‌گرداند](/kb/d/w06-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
