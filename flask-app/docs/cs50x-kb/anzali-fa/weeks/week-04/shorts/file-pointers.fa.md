---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-sh-file-pointers
type: short-summary
title: 'ویدئوی کوتاه: اشاره‌گرهای فایل (File Pointers)'
title_fa: اشاره‌گرهای فایل
title_en: File Pointers
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/file_pointers/
source_refs:
- src-short-file-pointers
- src-anzali-inference-4
concept_ids:
- w04-c-file-pointer
- w04-c-fopen-null-check
- w04-c-fprintf-fclose
- w04-c-fgetc-eof
- w04-c-fread-fwrite
prev: w04-sh-dynamic-memory-allocation
next: w04-ps-volume
order: 22
video:
  youtube_id: bOF-SpEAYgk
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: دادهٔ ماندگار
    evidence_en: null
  - start: '2:23'
    start_seconds: 143
    title_fa: stdio.h و اشاره‌گر فایل
    evidence_en: every single file I/O, input output function
  - start: '2:46'
    start_seconds: 166
    title_fa: شش تابع پایه
    evidence_en: six pretty common basic ones
  - start: '3:43'
    start_seconds: 223
    title_fa: fopen و حالت‌ها
    evidence_en: how do we make a call to fopen
  - start: '5:16'
    start_seconds: 316
    title_fa: fclose
    evidence_en: What about fclose
  - start: '6:05'
    start_seconds: 365
    title_fa: fgetc و بازسازی cat
    evidence_en: the first function that we'll see that will do that is fgetc
  - start: '9:34'
    start_seconds: 574
    title_fa: fputc و بازسازی cp
    evidence_en: fputc was the companion function
  - start: '11:47'
    start_seconds: 707
    title_fa: fread
    evidence_en: It can be a bit inefficient if we're getting characters
  - start: '15:20'
    start_seconds: 920
    title_fa: fwrite
    evidence_en: is pretty much the exact equivalent of fread
  - start: '16:35'
    start_seconds: 995
    title_fa: تابع‌های دیگر
    evidence_en: lots of other great file I/O functions
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: اشاره‌گرهای فایل (File Pointers)

> **منبع رسمی:** [صفحهٔ Short «File Pointers» در CS50x](https://cs50.harvard.edu/x/shorts/file_pointers/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

برنامه‌های تا اینجا «زودگذر» بودند و پس از پایان، اثری از خود نمی‌گذاشتند. با فایل‌ها می‌توانیم دادهٔ ماندگار بسازیم؛ در C معمولاً با اشاره‌گر به فایل (`FILE *`) کار می‌کنیم.

ویدئو شش تابع پایه را دوتا‌دوتا معرفی می‌کند: fopen و fclose، fgetc و fputc، fread و fwrite. با این تابع‌ها دستورهای cat و cp لینوکس را بازسازی می‌کند و در پایان چند تابع دیگر را نام می‌برد.

## نکته‌های کلیدی

- همهٔ این تابع‌ها در stdio.h هستند؛ همه یک اشاره‌گر فایل می‌گیرند، به جز fopen که خودش آن را می‌سازد.
- پس از fopen همیشه بررسی کن که اشاره‌گر برگشتی NULL نباشد.
- حالت‌ها: "r" برای خواندن، "w" برای نوشتن (فایل موجود را از اول بازنویسی می‌کند) و "a" برای افزودن به انتها.
- fclose فایل را می‌بندد؛ پس از آن دیگر نمی‌شود با آن اشاره‌گر خواند یا نوشت.
- fgetc کاراکتر بعدی را می‌خواند و فایل باید برای خواندن باز شده باشد. حلقه‌ای که تا EOF می‌خواند و چاپ می‌کند، همان کار cat را می‌کند؛ با fputc به‌جای printf، همان cp می‌شود.
- fread چهار آرگومان دارد: نشانی محل ذخیره، اندازهٔ هر واحد، تعداد واحدها و فایل. برای یک متغیر تکی باید نشانی آن (&c) را داد؛ نام آرایه خودش اشاره‌گر است.
- fwrite همان fread است در جهت برعکس: از بافر به فایل.
- تابع‌های مفید دیگر: fgets و fputs، fprintf، fseek، ftell، feof و ferror.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`file_pointers.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — دادهٔ ماندگار](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=0s)
- [۲:۲۳ — stdio.h و اشاره‌گر فایل](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=143s)
- [۲:۴۶ — شش تابع پایه](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=166s)
- [۳:۴۳ — fopen و حالت‌ها](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=223s)
- [۵:۱۶ — fclose](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=316s)
- [۶:۰۵ — fgetc و بازسازی cat](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=365s)
- [۹:۳۴ — fputc و بازسازی cp](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=574s)
- [۱۱:۴۷ — fread](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=707s)
- [۱۵:۲۰ — fwrite](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=920s)
- [۱۶:۳۵ — تابع‌های دیگر](https://www.youtube.com/watch?v=bOF-SpEAYgk&t=995s)

## مفاهیم مرتبط

- FILE * و fopen با حالت r، w، a — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- بررسی NULL پس از fopen — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- fprintf برای نوشتن در فایل و fclose برای بستن — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- fgetc، fputc و EOF — [یادداشت](/kb/d/w04-sh-file-pointers) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)
- fread و fwrite: خواندن و نوشتن بایت‌ها — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/bOF-SpEAYgk) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/file_pointers/file_pointers.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/file_pointers/lang/en/file_pointers.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/file_pointers/lang/en/file_pointers.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
