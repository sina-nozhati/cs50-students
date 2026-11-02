---
id: w02-n08
type: note
title: 'حافظه و اندازهٔ انواع داده (Arrays: memory and type sizes)'
title_fa: حافظه و اندازهٔ انواع داده
title_en: 'Arrays: memory and type sizes'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Arrays
official_anchor: arrays
source_url: https://cs50.harvard.edu/x/2026/notes/2/#arrays
source_refs:
- src-notes-2#arrays
- src-transcript-2
- src-srt-2
concept_ids:
- w02-c-memory-bytes
prev: w02-n07
next: w02-n09
order: 8
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:02:30'
  start_seconds: 3750
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=3750s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'bytes'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# حافظه و اندازهٔ انواع داده

> **منبع رسمی:** بخش «Arrays» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#arrays). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۲:۳۰ تا حدود ۱:۱۲:۴۶](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=3750s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پیش از آرایه باید بدانی داده‌ها **کجا** و **چقدر** جا می‌گیرند. هر نوع داده مقدار مشخصی از حافظه را می‌خواهد و حافظهٔ کامپیوتر **محدود** است.

## اندازهٔ انواع داده

- درس‌نامه یادآوری می‌کند که پیش‌تر از انواع داده‌ای مثل `bool`، `int`، `char` و `string` حرف زدیم.

> **توجه:** متن رسمی می‌گوید «در هفتهٔ ۰ از انواع داده حرف زدیم»، اما انواع داده در [هفتهٔ ۱](/kb/d/w01-n10) معرفی شدند (ناهمخوانی d20).

- هر نوع داده مقداری از منابع سیستم را می‌خواهد. این‌ها اندازه‌های **معمول در محیط CS50** است:

| نوع | اندازه |
| --- | --- |
| `bool` | ۱ بایت |
| `int` | ۴ بایت |
| `long` | ۸ بایت |
| `float` | ۴ بایت |
| `double` | ۸ بایت |
| `char` | ۱ بایت |
| `string` | ؟ بایت |

- علامت سؤال جلوی `string` عمدی است: اندازهٔ رشته به طولش بستگی دارد. پاسخ کامل را در یادداشت [رشته و NUL](/kb/d/w02-n12) می‌بینی.

## حافظه مثل شبکه‌ای از بایت‌ها

- درون کامپیوتر مقدار **محدودی** حافظه هست. درس‌نامه تصویر یک تراشهٔ حافظه را نشان می‌دهد (تصویر memory، فقط پیوند).
- می‌توانی تصور کنی یک `char` که فقط ۱ بایت می‌خواهد، یک خانه از این شبکه را پر می‌کند (تصویر «1 byte»).
- یک `int` که ۴ بایت می‌خواهد، چهار خانهٔ پشت‌سرهم را می‌گیرد (تصویر «4 bytes»).

> **منبع رسمی:** تصویرها: [memory](https://cs50.harvard.edu/x/notes/2/cs50Week2Slide084.png)، [1 byte](https://cs50.harvard.edu/x/notes/2/cs50Week2Slide087.png)، [4 bytes](https://cs50.harvard.edu/x/notes/2/cs50Week2Slide088.png). هر سه حدود ۰٫۹ مگابایت‌اند و فقط پیوند داده شده‌اند.

## سخنرانی چه می‌گوید

**از سخنرانی:** David حافظه را مثل شبکه‌ای از خانه‌ها روی تراشه نشان می‌دهد که هر خانه یک بایت است و می‌شود به هر کدام نشانی داد؛ اولی، دومی، سومی و همین‌طور تا آخر.

## اشتباه‌های رایج

- تصور این‌که اندازهٔ هر نوع در همهٔ کامپیوترها یکی است؛ درس‌نامه صریحاً می‌گوید این اندازه‌ها «معمول در محیط CS50» است.
- فکر کردن به `string` به‌عنوان یک نوع با اندازهٔ ثابت.

## جمع‌بندی

- `char` و `bool` ۱ بایت، `int` و `float` ۴ بایت، `long` و `double` ۸ بایت.
- حافظه محدود است و داده‌ها در خانه‌های یک‌بایتی آن می‌نشینند.

## پیوندها

- قبلی: [چهار مرحلهٔ کامپایل: پیش‌پردازش، کامپایل، اسمبل، پیوند](/kb/d/w02-n07)
- بعدی: [آرایه‌ها و حلقه‌ها](/kb/d/w02-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
