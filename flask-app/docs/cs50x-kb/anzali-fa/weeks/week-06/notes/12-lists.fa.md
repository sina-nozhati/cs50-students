---
id: w06-n12
type: note
title: فهرست‌ها (list)، sum و len (Lists)
title_fa: فهرست‌ها (list)، sum و len
title_en: Lists
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Lists
official_anchor: lists
source_url: https://cs50.harvard.edu/x/2026/notes/6/#lists
source_refs:
- src-notes-6#lists
- src-transcript-6
- src-python-docs
- src-section-6
- src-section-6-transcript
- src-anzali-authored-6
- src-srt-6
concept_ids:
- w06-c-list
- w06-c-sum-len
- w06-c-append
prev: w06-n11
next: w06-n13
order: 12
video:
  youtube_id: Rl0ludWTLxs
  start: '1:50:50'
  start_seconds: 6650
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=6650s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'called scores of three scores'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# فهرست‌ها (list)، sum و len

> **منبع رسمی:** بخش «Lists» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#lists). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۰:۵۰ تا حدود ۱:۵۴:۴۵](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=6650s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

آرایهٔ C اندازهٔ ثابت داشت و برای بزرگ کردنش باید `realloc` یا فهرست پیوندی هفتهٔ ۵ را به کار می‌بردی. `list` پایتون خودش بزرگ و کوچک می‌شود و تابع‌ها و متدهای آماده‌ای مثل `len`، `sum` و `append` دارد.

## فهرست‌ها

- `list` یکی از ساختمان داده‌های پایتون است.
- فهرست‌ها متدها یا تابع‌های داخلی دارند.
- برای نمونه این کد را در نظر بگیر:

```python
# Averages three numbers using a list

# Scores
scores = [72, 73, 33]

# Print average
average = sum(scores) / len(scores)
print(f"Average: {average}")
```

- برای محاسبهٔ میانگین از `sum` داخلی استفاده شده است. خروجی این برنامه `Average: 59.333333333333336` است (اجراشده روی جعبهٔ ساخت با پایتون ۳)؛ رقم پایانی `6` همان عدم دقت ممیز شناور یادداشت ۱۰ است.

> [!NOTE]
> **یادداشت**
> درس‌نامه `sum` را «متد» داخلی می‌نامد، اما `sum` و `len` **تابع**‌های داخلی پایتون‌اند که فهرست را به عنوان آرگومان می‌گیرند (`sum(scores)`)، نه متدی که با نقطه روی فهرست صدا زده شود. `append` واقعاً متدِ فهرست است (`scores.append(score)`) (d102).

- حتی می‌شود از نحو زیر برای گرفتن مقدار از کاربر استفاده کرد:

```python
# Averages three numbers using a list and a loop

from cs50 import get_int

# Get scores
scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

# Print average
average = sum(scores) / len(scores)
print(f"Average: {average}")
```

- این کد از متد داخلی `append` فهرست‌ها استفاده می‌کند: فهرست خالی `[]` شروع می‌شود و هر نمره به انتهایش اضافه می‌شود.
- دربارهٔ فهرست‌ها در [مستندات پایتون](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) و دربارهٔ `len` در [همان مستندات](https://docs.python.org/3/library/functions.html#len) بیشتر بخوان.

> [!TIP]
> **از سخنرانی: فهرست به جای فهرست پیوندی**
> David یادآوری کرد که فهرست پیوندی می‌توانست به‌صورت پویا بزرگ و کوچک شود؛ فهرست پایتون همین توانایی را آماده در اختیارت می‌گذارد و می‌شود از همان ابتدا با مقدارهای مشخص ساختش.

> [!IMPORTANT]
> **تألیفی: نمایه و برش**
> `scores[0]` نخستین عضو و `scores[-1]` آخرین عضو است. `scores[1:]` فهرست تازه‌ای از عضو دوم تا آخر می‌سازد. نمایهٔ خارج از محدوده (مثلاً `scores[3]` برای فهرست سه‌عضوی) خطای `IndexError` می‌دهد، نه رفتار تعریف‌نشده مثل C. همین ایده‌ها برای رشته‌ها هم برقرارند و در جلسهٔ حل تمرین با `str_prediction.py` تمرین شدند.

## اشتباه‌های رایج

- نوشتن `scores.sum()` یا `scores.len()`؛ درستش `sum(scores)` و `len(scores)` است.
- فراموش کردن `scores = []` پیش از حلقه؛ `append` روی متغیر تعریف‌نشده `NameError` می‌دهد.
- انتظار اینکه `sum(scores) / len(scores)` عدد صحیح بدهد؛ `/` همیشه `float` می‌دهد.

## جمع‌بندی

- `list` پویا است: `[]`، `append`، نمایه و برش.
- `len` و `sum` تابع‌اند؛ `append` متد است.
- نمایهٔ نادرست `IndexError` می‌دهد.

## پیوندها

- قبلی: [ماریو در پایتون: while True و end](/kb/d/w06-n11)
- بعدی: [جست‌وجو، in و دیکشنری](/kb/d/w06-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
