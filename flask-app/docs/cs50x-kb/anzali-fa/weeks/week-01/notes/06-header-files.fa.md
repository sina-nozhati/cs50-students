---
id: w01-n06
type: note
title: فایل‌های سرآیند، کتابخانه‌ها و راهنمای CS50 (Header Files and CS50 Manual Pages)
title_fa: فایل‌های سرآیند، کتابخانه‌ها و راهنمای CS50
title_en: Header Files and CS50 Manual Pages
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Header Files and CS50 Manual Pages
official_anchor: header-files-and-cs50-manual-pages
source_url: https://cs50.harvard.edu/x/notes/1/#header-files-and-cs50-manual-pages
source_refs:
- src-notes-1#header-files-and-cs50-manual-pages
- src-transcript-1
- src-manual
- src-srt-1
concept_ids:
- w01-c-header-file
- w01-c-library
- w01-c-manual-pages
- w01-c-cs50-library
prev: w01-n05
next: w01-n07
order: 6
video:
  youtube_id: SlqjA04_dpk
  start: '25:11'
  start_seconds: 1511
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=1511s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'header file'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# فایل‌های سرآیند، کتابخانه‌ها و راهنمای CS50

> **منبع رسمی:** بخش «Header Files and CS50 Manual Pages» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#header-files-and-cs50-manual-pages). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۵:۱۱ تا حدود ۳۲:۰۰](https://www.youtube.com/watch?v=SlqjA04_dpk&t=1511s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

خط اول برنامه، `#include <stdio.h>`، بی‌دلیل آنجا نیست. این بخش توضیح می‌دهد چرا باید کتابخانه‌ها را «وارد» کنی و از کجا دربارهٔ توابع یاد بگیری.

## فایل سرآیند

- `#include <stdio.h>` دستور ویژه‌ای است که به کامپایلر می‌گوید می‌خواهی از توانایی‌های یک **کتابخانه** (library) به نام `stdio.h` استفاده کنی.
- `stdio.h` یک **فایل سرآیند** (header file) است. همین فایل امکان استفاده از `printf` را می‌دهد.
- درس‌نامه تأکید می‌کند نام آن *studio* نیست؛ `stdio.h` است (کوتاه‌شدهٔ standard input/output).

## کتابخانه چیست؟

- کتابخانه مجموعه‌ای از کد است که کس دیگری از پیش نوشته است.
- با استفاده از کتابخانه‌ها، از توابعی بهره می‌بری که دیگران قبلاً ساخته‌اند و لازم نیست همه‌چیز را از صفر بنویسی.

## صفحه‌های راهنما

- همهٔ توانایی‌های این کتابخانه را می‌توانی در [Manual Pages](https://manual.cs50.io) بخوانی.
- صفحه‌های راهنما (manual pages) کمک می‌کنند بفهمی هر فرمان یا تابع چه می‌کند و چطور کار می‌کند.

## کتابخانهٔ CS50

CS50 کتابخانهٔ خودش را دارد: `cs50.h`. درس‌نامه آن را «چرخ‌های کمکی» (training wheels) برای شروع کار با C می‌نامد. توابع آن:

```text
get_char
get_double
get_float
get_int
get_long
get_string
```

- هر تابع `get_` یک نوع داده از کاربر می‌گیرد؛ مثلاً `get_int` یک عدد صحیح و `get_string` یک رشته.
- این کتابخانه‌ها در [cs50.dev](https://cs50.dev) از پیش نصب شده‌اند. روی کامپیوتر خودت احتمالاً باید نصبشان کنی؛ به همین دلیل درس‌نامه توصیه می‌کند در این دوره از cs50.dev استفاده کنی.

## سخنرانی چه می‌گوید

**از سخنرانی:** برخی توابع جزو خود زبان C هستند و برخی را CS50 ساخته است. توابع CS50 فقط برای چند هفتهٔ اول‌اند و بعداً کنار گذاشته می‌شوند.

## اشتباه‌های رایج

- نوشتن `#include <studio.h>`.
- استفاده از `get_string` بدون `#include <cs50.h>`؛ کامپایلر آن را نمی‌شناسد.

## جمع‌بندی

- `#include` یک کتابخانه را در دسترس برنامه می‌گذارد.
- `stdio.h` برای `printf`، `cs50.h` برای توابع `get_*`.
- پیش از استفاده از یک تابع ناآشنا، صفحهٔ راهنمای آن را ببین.

## پیوندها

- قبلی: [از Scratch به C: printf و دنبالهٔ گریز](/kb/d/w01-n05)
- بعدی: [سلام به تو: get_string، متغیر و جای‌نگهدار](/kb/d/w01-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
