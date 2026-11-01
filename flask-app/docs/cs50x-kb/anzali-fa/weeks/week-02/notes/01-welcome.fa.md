---
id: w02-n01
type: note
title: 'خوش آمدید: نگاهی زیر کاپوت (Welcome!)'
title_fa: 'خوش آمدید: نگاهی زیر کاپوت'
title_en: Welcome!
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Welcome!
official_anchor: welcome
source_url: https://cs50.harvard.edu/x/2026/notes/2/#welcome
source_refs:
- src-notes-2#welcome
- src-transcript-2
- src-pset-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-bottom-up
prev: w02-fa
next: w02-n02
order: 1
video:
  youtube_id: h5Gc1n8ZuU8
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# خوش آمدید: نگاهی زیر کاپوت

> **منبع رسمی:** بخش «Welcome!» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#welcome). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۱:۵۶](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هفتهٔ ۱ با C شروع کردیم؛ یک زبان متنی. این هفته کاپوت را بالا می‌زنیم: می‌بینیم کامپایل واقعاً چه می‌کند، داده‌ها چطور در حافظه کنار هم می‌نشینند و چطور با یک ساختار تازه به نام **آرایه** (`array`) کلی مقدار را با یک نام نگه داریم.

## حرف اصلی درس‌نامه

- هفتهٔ پیش C را یاد گرفتیم، یک زبان برنامه‌نویسی متنی.
- این هفته سراغ **بلوک‌های سازندهٔ** بیشتری می‌رویم تا برنامه‌نویسی را **از پایین به بالا** (`bottom up`) بفهمیم.
- درس‌نامه تأکید می‌کند که این درس، جدا از اصول برنامه‌نویسی، دربارهٔ **حل مسئله** (`problem-solving`) است. پس روی شیوهٔ رویارویی با مسئله‌های علوم کامپیوتر هم تمرکز می‌کنیم.
- تا پایان درس یاد می‌گیری با همین بلوک‌ها انبوهی از مسئله‌ها را حل کنی؛ راه‌حل‌هایی که امروز بی‌آن‌که فکر کنیم از آن‌ها استفاده می‌کنیم.

## نقشهٔ این هفته

> **تألیفی:** این فهرست ترتیب یادداشت‌های همین بسته است، نه بخشی از درس‌نامه.

```text
debugging  ->  compiling  ->  arrays  ->  strings  ->  string length  ->  command-line arguments  ->  exit status  ->  cryptography
```

- **اشکال‌زدایی:** خطای کامپایل، `printf`، `debug50` و اردک.
- **کامپایل:** `clang` و چهار مرحلهٔ پشت `make`.
- **آرایه و رشته:** مقدارهای پشت‌سرهم در حافظه؛ رشته‌ای که در واقع آرایه‌ای از نویسه‌هاست.
- **آرگومان‌های خط فرمان و وضعیت خروج:** ورودی پیش از اجرای برنامه، و عددی که برنامه هنگام پایان برمی‌گرداند.

## سخنرانی چه می‌گوید

**از سخنرانی:** David J. Malan هفته را با دو مسئلهٔ واقعی شروع می‌کند: سنجیدن **سطح خوانایی** متن و **رمزنگاری**. هر دو بعداً در پرابلم‌ست ۲ برمی‌گردند (Readability، و Caesar یا Substitution).

## جمع‌بندی

- هدف هفتهٔ ۲: دیدن آنچه زیر کاپوت C می‌گذرد و ابزار تازهٔ آرایه.
- تمرکز درس فقط نحو زبان نیست؛ حل مسئله است.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w02-fa)
- بعدی: [سطح خوانایی متن و رمزنگاری: دو مسئلهٔ این هفته](/kb/d/w02-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
