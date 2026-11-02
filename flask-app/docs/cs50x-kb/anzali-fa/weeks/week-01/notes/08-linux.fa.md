---
id: w01-n08
type: note
title: لینوکس و فرمان‌های ترمینال (Linux)
title_fa: لینوکس و فرمان‌های ترمینال
title_en: Linux
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Linux
official_anchor: linux
source_url: https://cs50.harvard.edu/x/notes/1/#linux
source_refs:
- src-notes-1#linux
- src-transcript-1
- src-short-command-line
- src-srt-1
concept_ids:
- w01-c-linux-commands
prev: w01-n07
next: w01-n09
order: 8
video:
  youtube_id: SlqjA04_dpk
  start: '44:38'
  start_seconds: 2678
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=2678s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'Linux'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# لینوکس و فرمان‌های ترمینال

> **منبع رسمی:** بخش «Linux» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#linux). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۴:۳۸ تا حدود ۵۶:۰۱](https://www.youtube.com/watch?v=SlqjA04_dpk&t=2678s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا با ترمینال فقط `make` و `./` را اجرا کردی. ترمینال کارهای بیشتری می‌کند: می‌توانی با آن فایل بسازی، جابه‌جا کنی و پاک کنی.

## CLI یا GUI؟

- تا اینجا از CLI برای `make` و اجرای برنامه استفاده کرده‌ایم.
- طبق درس‌نامه، CLI برای اجرای فرمان‌ها و کار با فایل‌ها اغلب از GUI مفیدتر است.

## فرمان‌های رایج

| فرمان | کار |
| --- | --- |
| `cd` | تغییر پوشهٔ جاری (change directory) |
| `cp` | کپی کردن فایل یا پوشه |
| `ls` | فهرست فایل‌های یک پوشه |
| `mkdir` | ساختن پوشه |
| `mv` | جابه‌جا کردن یا تغییر نام فایل و پوشه |
| `rm` | حذف فایل |
| `rmdir` | حذف پوشه |

- پرکاربردترین آن‌ها `ls` است. آن را در ترمینال تایپ کن و Enter بزن تا همهٔ فایل‌های پوشهٔ جاری را ببینی.

## از ویدئوی کوتاه Command Line

ویدئوی کوتاه [Command Line](/kb/d/w01-sh-command-line) چند نکتهٔ دیگر می‌گوید:

- `pwd` مسیر پوشهٔ جاری را نشان می‌دهد.
- `.` یعنی پوشهٔ جاری و `..` یعنی پوشهٔ والد؛ پس `cd ..` یک پله بالا می‌رود.
- `cd` بدون آرگومان تو را به پوشهٔ خانه (`~`) می‌برد.
- `cp -r` یک پوشه را با همهٔ محتوایش کپی می‌کند.
- `rm -r` پوشه را حذف می‌کند و `rm -f` بدون پرسیدن حذف می‌کند. حذف در ترمینال **برگشت ندارد**.

> **نکته:** آن ویدئو سال ۲۰۱۷ ضبط شده و از CS50 IDE قدیمی و پوشهٔ `~/workspace` استفاده می‌کند. مفاهیم همان‌اند، اما محیط امروز cs50.dev است.

## سخنرانی چه می‌گوید

**از سخنرانی:** `mv` همان «تغییر نام» است؛ فرمان جداگانه‌ای برای تغییر نام لازم نیست.

## اشتباه‌های رایج

- حذف `hello.c` به‌جای `hello`؛ کد منبع از دست می‌رود.
- استفادهٔ عجولانه از `rm -rf`.

## جمع‌بندی

- `ls`، `cd`، `mkdir`، `cp`، `mv`، `rm` و `rmdir` بیشتر کارهای روزمره را پوشش می‌دهند.

## پیوندها

- قبلی: [سلام به تو: get_string، متغیر و جای‌نگهدار](/kb/d/w01-n07)
- بعدی: [شرط‌ها در C](/kb/d/w01-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
