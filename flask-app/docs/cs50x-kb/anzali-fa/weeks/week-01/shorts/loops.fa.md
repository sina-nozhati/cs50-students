---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sh-loops
type: short-summary
title: 'ویدئوی کوتاه: حلقه‌ها (Loops)'
title_fa: حلقه‌ها
title_en: Loops
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/loops/
source_refs:
- src-short-loops
- src-anzali-inference-1
concept_ids:
- w01-c-while-loop
- w01-c-do-while
- w01-c-for-loop
- w01-c-infinite-loop
- w01-c-input-validation
prev: w01-sh-conditional-statements
next: w01-sh-command-line
order: 25
video:
  youtube_id: WgX8e_O7eG8
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: حلقهٔ بی‌پایان
    evidence_en: null
  - start: '1:25'
    start_seconds: 85
    title_fa: while با شرط
    evidence_en: something a little more useful
  - start: '2:40'
    start_seconds: 160
    title_fa: do while
    evidence_en: Meanwhile
  - start: '3:23'
    start_seconds: 203
    title_fa: for
    evidence_en: for loop
  - start: '4:01'
    start_seconds: 241
    title_fa: گام‌های اجرای for
    evidence_en: step by step
  - start: '6:41'
    start_seconds: 401
    title_fa: کاربرد هر حلقه
    evidence_en: use cases
  - start: '8:39'
    start_seconds: 519
    title_fa: جایگزین‌پذیری حلقه‌ها
    evidence_en: interchange
  chapters_origin: inference
recorded: '2017'
---

# ویدئوی کوتاه: حلقه‌ها (Loops)

> **منبع رسمی:** [صفحهٔ Short «Loops» در CS50x](https://cs50.harvard.edu/x/shorts/loops/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو سه حلقهٔ C را با هم مقایسه می‌کند: `while`، `do while` و `for`. هر کدام را با معادلش در Scratch و کاربرد معمولش توضیح می‌دهد.

## نکته‌های کلیدی

- `while (true)` حلقهٔ بی‌پایان است، معادل `forever` در Scratch.
- `while` تا وقتی شرط درست است تکرار می‌کند. `repeat until` در Scratch برعکس است: تا وقتی شرط نادرست است تکرار می‌کند.
- `do while` بدنه را **دست‌کم یک بار** اجرا می‌کند، سپس شرط را بررسی می‌کند.
- `for` سه بخش دارد: شروع، شرط و به‌روزرسانی. اگر شرط از ابتدا نادرست باشد، بدنه هیچ‌وقت اجرا نمی‌شود.
- کاربردها: `while` برای تعداد نامعلوم که شاید صفر باشد؛ `do while` برای ورودی گرفتن از کاربر؛ `for` برای تعداد مشخص تکرار.
- این سه حلقه جایگزین‌پذیرند، اما انتخاب درست کد را خواناتر می‌کند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`loops.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — حلقهٔ بی‌پایان](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=0s)
- [۱:۲۵ — while با شرط](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=85s)
- [۲:۴۰ — do while](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=160s)
- [۳:۲۳ — for](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=203s)
- [۴:۰۱ — گام‌های اجرای for](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=241s)
- [۶:۴۱ — کاربرد هر حلقه](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=401s)
- [۸:۳۹ — جایگزین‌پذیری حلقه‌ها](https://www.youtube.com/watch?v=WgX8e_O7eG8&t=519s)

## مفاهیم مرتبط

- حلقهٔ while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u01`)
- حلقهٔ do while — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)
- حلقهٔ for — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u02`)
- حلقهٔ بی‌پایان و control-C — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u03`)
- اعتبارسنجی ورودی و درخواست دوباره — [یادداشت](/kb/d/w01-n15) · درس کوتاه `w01-l09` (واحد `w01-l09-u04`)

## منابع

- [ویدئو در YouTube](https://youtu.be/WgX8e_O7eG8) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/loops/loops.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/loops/lang/en/loops.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/loops/lang/en/loops.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
