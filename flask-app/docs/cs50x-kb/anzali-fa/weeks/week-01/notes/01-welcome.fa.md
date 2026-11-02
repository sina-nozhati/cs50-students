---
id: w01-n01
type: note
title: 'خوش آمدید: از Scratch به C (Welcome!)'
title_fa: 'خوش آمدید: از Scratch به C'
title_en: Welcome!
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Welcome!
official_anchor: welcome
source_url: https://cs50.harvard.edu/x/notes/1/#welcome
source_refs:
- src-notes-1#welcome
- src-anzali-authored-1
- src-srt-1
concept_ids:
- w01-c-scratch-to-c
prev: w01-fa
next: w01-n02
order: 1
video:
  youtube_id: SlqjA04_dpk
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# خوش آمدید: از Scratch به C

> **منبع رسمی:** بخش «Welcome!» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#welcome). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۳:۱۵](https://www.youtube.com/watch?v=SlqjA04_dpk&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هفتهٔ ۰ با Scratch گذشت. این هفته همان ایده‌ها را در زبان **C** می‌نویسیم. در C دستورها را به‌جای کشیدن بلوک، تایپ می‌کنی.

## آنچه درس‌نامه می‌گوید

- در جلسهٔ قبل با Scratch، یک زبان برنامه‌نویسی بصری، آشنا شدیم.
- یادگرفتن مفاهیم علوم کامپیوتر می‌تواند بسیار دشوار باشد؛ گاهی حس می‌کنی از **شیلنگ آتش‌نشانی** آب می‌نوشی.
- آنچه در نهایت اهمیت دارد، پیشرفتی است که در هفته‌ها و ماه‌های آینده با تلاش و مطالعه به دست می‌آوری.
- همهٔ مفاهیم اصلی Scratch در یادگیری هر زبان برنامه‌نویسی به کار می‌آیند. **تابع** (function)، **شرط** (conditional)، **حلقه** (loop) و **متغیر** (variable) بلوک‌های سازنده‌ای هستند که در هر زبانی پیدا می‌کنی.

## یک تصویر ذهنی

> **تألیفی:** جدول زیر را CS50x Anzali برای مرور ساخته است. معادل‌ها را در یادداشت‌های بعدی همراه کد رسمی می‌بینی.

| در Scratch | در C (همین هفته) |
| --- | --- |
| بلوک `say` | تابع `printf` |
| بلوک `ask` و `answer` | تابع `get_string` و یک متغیر |
| `if` و `if else` | `if` و `else` |
| `repeat` و `forever` | `while`، `for` و `do while` |
| بلوک سفارشی (`define`) | تابعی که خودت تعریف می‌کنی |

## جمع‌بندی

- مفاهیم C همان مفاهیم Scratch هستند. آنچه تازه است **نحو** (syntax) است، و نحو با تمرین راحت می‌شود.
- اگر این هفته سخت بود، طبیعی است. معیار، پیشرفت تو در طول دوره است.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w01-fa)
- بعدی: [کد منبع، کد ماشین و کامپایلر](/kb/d/w01-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
