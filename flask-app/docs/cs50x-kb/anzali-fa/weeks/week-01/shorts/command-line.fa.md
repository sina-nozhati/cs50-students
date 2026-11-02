---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sh-command-line
type: short-summary
title: 'ویدئوی کوتاه: خط فرمان لینوکس (Command Line)'
title_fa: خط فرمان لینوکس
title_en: Command Line
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/command_line/
source_refs:
- src-short-command-line
- src-anzali-inference-1
concept_ids:
- w01-c-linux-commands
- w01-c-paths-navigation
- w01-c-gui-cli
prev: w01-sh-loops
next: w01-sh-magic-numbers
order: 26
video:
  youtube_id: BnJ013X02b8
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: چرا خط فرمان'
    evidence_en: null
  - start: '1:20'
    start_seconds: 80
    title_fa: ls
    evidence_en: The first one that you'll probably use
  - start: '3:17'
    start_seconds: 197
    title_fa: cd
    evidence_en: change directory
  - start: '3:44'
    start_seconds: 224
    title_fa: نام‌های . و ..
    evidence_en: dot, dot
  - start: '3:56'
    start_seconds: 236
    title_fa: pwd
    evidence_en: present working directory
  - start: '6:04'
    start_seconds: 364
    title_fa: 'نمایش زنده: cd و ..'
    evidence_en: cd, space, dot, dot
  - start: '7:21'
    start_seconds: 441
    title_fa: بازگشت به خانه با cd
    evidence_en: cd with nothing after it
  - start: '7:42'
    start_seconds: 462
    title_fa: mkdir
    evidence_en: mkdir
  - start: '9:20'
    start_seconds: 560
    title_fa: cp و cp -r
    evidence_en: make a copy
  - start: '11:58'
    start_seconds: 718
    title_fa: rm و گزینه‌هایش
    evidence_en: rm, for remove
  - start: '14:52'
    start_seconds: 892
    title_fa: rm -rf
    evidence_en: rm -rf
  - start: '16:02'
    start_seconds: 962
    title_fa: mv برای تغییر نام
    evidence_en: greddy
  chapters_origin: inference
recorded: '2017'
---

# ویدئوی کوتاه: خط فرمان لینوکس (Command Line)

> **منبع رسمی:** [صفحهٔ Short «Command Line» در CS50x](https://cs50.harvard.edu/x/shorts/command_line/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو فرمان‌های پایهٔ خط فرمان لینوکس را با نمایش زنده آموزش می‌دهد: دیدن، جابه‌جا شدن، ساختن، کپی، حذف و تغییر نام.

ویدئو در سال ۲۰۱۷ و در CS50 IDE ضبط شده است. محیط امروز cs50.dev است، اما فرمان‌ها همان‌اند.

## نکته‌های کلیدی

- `ls` محتوای پوشهٔ جاری را فهرست می‌کند.
- `cd <dir>` وارد یک پوشه می‌شود. `.` پوشهٔ جاری و `..` پوشهٔ والد است؛ `cd` بدون آرگومان به پوشهٔ خانه (`~`) برمی‌گردد.
- `pwd` مسیر کامل پوشهٔ جاری را چاپ می‌کند.
- `mkdir <dir>` پوشه می‌سازد.
- `cp <source> <destination>` فایل را کپی می‌کند. برای کپی یک پوشه با محتوایش `cp -r` لازم است.
- `rm <file>` حذف می‌کند و پیش از آن تأیید می‌خواهد. `rm -f` بدون پرسش حذف می‌کند و `rm -r` پوشه را حذف می‌کند. `rm -rf` بسیار خطرناک است، چون حذف در ترمینال برگشت ندارد.
- `mv <source> <destination>` جابه‌جا می‌کند یا نام را تغییر می‌دهد. مثال ویدئو: تصحیح نام فایلی که اشتباه تایپ شده بود.
- Ctrl-L صفحهٔ ترمینال را پاک می‌کند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`command_line.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: چرا خط فرمان](https://www.youtube.com/watch?v=BnJ013X02b8&t=0s)
- [۱:۲۰ — ls](https://www.youtube.com/watch?v=BnJ013X02b8&t=80s)
- [۳:۱۷ — cd](https://www.youtube.com/watch?v=BnJ013X02b8&t=197s)
- [۳:۴۴ — نام‌های . و ..](https://www.youtube.com/watch?v=BnJ013X02b8&t=224s)
- [۳:۵۶ — pwd](https://www.youtube.com/watch?v=BnJ013X02b8&t=236s)
- [۶:۰۴ — نمایش زنده: cd و ..](https://www.youtube.com/watch?v=BnJ013X02b8&t=364s)
- [۷:۲۱ — بازگشت به خانه با cd](https://www.youtube.com/watch?v=BnJ013X02b8&t=441s)
- [۷:۴۲ — mkdir](https://www.youtube.com/watch?v=BnJ013X02b8&t=462s)
- [۹:۲۰ — cp و cp -r](https://www.youtube.com/watch?v=BnJ013X02b8&t=560s)
- [۱۱:۵۸ — rm و گزینه‌هایش](https://www.youtube.com/watch?v=BnJ013X02b8&t=718s)
- [۱۴:۵۲ — rm -rf](https://www.youtube.com/watch?v=BnJ013X02b8&t=892s)
- [۱۶:۰۲ — mv برای تغییر نام](https://www.youtube.com/watch?v=BnJ013X02b8&t=962s)

## مفاهیم مرتبط

- فرمان‌های پایهٔ لینوکس — [یادداشت](/kb/d/w01-n08) · درس کوتاه `w01-l04` (واحد `w01-l04-u01`)
- پوشهٔ جاری، پوشهٔ والد و خانه (. .. ~ pwd) — [یادداشت](/kb/d/w01-sh-command-line) · درس کوتاه `w01-l04` (واحد `w01-l04-u02`)
- رابط گرافیکی و رابط خط فرمان — [یادداشت](/kb/d/w01-n03) · درس کوتاه `w01-l01` (واحد `w01-l01-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/BnJ013X02b8) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/command_line/command_line.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/command_line/lang/en/command_line.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/command_line/lang/en/command_line.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
