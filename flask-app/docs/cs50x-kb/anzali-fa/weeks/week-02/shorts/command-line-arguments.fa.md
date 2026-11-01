---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sh-command-line-arguments
type: short-summary
title: 'ویدئوی کوتاه: آرگومان‌های خط فرمان (Command-Line Arguments)'
title_fa: آرگومان‌های خط فرمان
title_en: Command-Line Arguments
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/command_line_arguments/
source_refs:
- src-short-command-line-arguments
- src-anzali-inference-2
concept_ids:
- w02-c-argc-argv
- w02-c-argv0
- w02-c-argv-strings
- w02-c-array-bounds
prev: w02-sh-arrays
next: w02-ps-scrabble
order: 27
video:
  youtube_id: AI6Ccfno6Pk
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'ورودی تا اینجا: int main(void)'
    evidence_en: null
  - start: 0:59
    start_seconds: 59
    title_fa: اعلان تازهٔ main
    evidence_en: int argc
  - start: '1:44'
    start_seconds: 104
    title_fa: 'argc: تعداد آرگومان‌ها'
    evidence_en: argument count
  - start: '1:54'
    start_seconds: 114
    title_fa: 'argv: آرایه‌ای از رشته‌ها'
    evidence_en: argument vector
  - start: '3:55'
    start_seconds: 235
    title_fa: اولین و آخرین عنصر argv
    evidence_en: argc minus one
  - start: '5:36'
    start_seconds: 336
    title_fa: همه چیز رشته است
    evidence_en: stored as a string
  - start: '7:33'
    start_seconds: 453
    title_fa: بیرون زدن از مرز argv
    evidence_en: segmentation fault
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: آرگومان‌های خط فرمان (Command-Line Arguments)

> **منبع رسمی:** [صفحهٔ Short «Command-Line Arguments» در CS50x](https://cs50.harvard.edu/x/shorts/command_line_arguments/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

تا اینجا `main` را با `int main(void)` نوشته‌ایم و ورودی را درون برنامه پرسیده‌ایم. اگر بخواهیم کاربر داده را هنگام اجرای برنامه، در خط فرمان بدهد، باید `main` را به شکل `int main(int argc, string argv[])` اعلان کنیم.

ویدئو معنای `argc` (تعداد آرگومان‌ها) و `argv` (آرایه‌ای از رشته‌ها) را با مثال `./greedy 1024 cs50` توضیح می‌دهد.

## نکته‌های کلیدی

- `argc` یعنی argument count و `argv` یعنی argument vector؛ این نام‌ها قراردادی‌اند و می‌شد نام دیگری داد.
- نام برنامه خودش یک آرگومان است: برای `./greedy` مقدار `argc` برابر 1 و برای `./greedy 1024 cs50` برابر 3 است. فاصله (یا هر فضای خالی) آرگومان‌ها را جدا می‌کند.
- `argv[0]` همیشه نام برنامه است و آخرین عنصر در `argv[argc - 1]` قرار دارد.
- هر عنصر `argv` یک رشته است: `"1024"` چهار نویسه است، نه عدد صحیح 1024. تابعی برای تبدیل رشته به عدد وجود دارد که ویدئو عمداً نامش را نمی‌برد.
- دسترسی به `argv[3]` وقتی فقط سه عنصر داری، بیرون از مرز آرایه است و احتمالاً به segmentation fault می‌انجامد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`command_line_arguments.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — ورودی تا اینجا: int main(void)](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=0s)
- [۰:۵۹ — اعلان تازهٔ main](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=59s)
- [۱:۴۴ — argc: تعداد آرگومان‌ها](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=104s)
- [۱:۵۴ — argv: آرایه‌ای از رشته‌ها](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=114s)
- [۳:۵۵ — اولین و آخرین عنصر argv](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=235s)
- [۵:۳۶ — همه چیز رشته است](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=336s)
- [۷:۳۳ — بیرون زدن از مرز argv](https://www.youtube.com/watch?v=AI6Ccfno6Pk&t=453s)

## مفاهیم مرتبط

- argc و argv — [یادداشت](/kb/d/w02-n16) · درس کوتاه `w02-l08` (واحد `w02-l08-u01`)
- argv[0] نام خود برنامه است — [یادداشت](/kb/d/w02-n16) · درس کوتاه `w02-l08` (واحد `w02-l08-u02`)
- همهٔ عناصر argv رشته‌اند — [یادداشت](/kb/d/w02-sh-command-line-arguments) · درس کوتاه `w02-l08` (واحد `w02-l08-u02`)
- بیرون زدن از مرز آرایه و segmentation fault — [یادداشت](/kb/d/w02-sh-arrays) · درس کوتاه `w02-l04` (واحد `w02-l04-u04`)

## منابع

- [ویدئو در YouTube](https://youtu.be/AI6Ccfno6Pk) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/command_line_arguments.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
