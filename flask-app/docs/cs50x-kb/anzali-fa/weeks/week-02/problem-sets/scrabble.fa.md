---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-ps-scrabble
type: problem-set-guide
title: راهنمای اسکرابل (Scrabble)
title_fa: اسکرابل (Scrabble)
title_en: Scrabble
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/2/scrabble/
source_refs:
- src-pset-2-scrabble#problem-to-solve
- src-pset-2-scrabble#advice-and-hints
- src-anzali-authored-2
- src-pset-2#what-to-do
concept_ids:
- w02-c-array
- w02-c-array-index
- w02-c-char-ascii
- w02-c-ascii-case
- w02-c-ctype
- w02-c-string-char-array
- w02-c-strlen
- w02-c-function-anatomy
problem_set_ref: weeks/week-02/problem-sets/scrabble.json
prev: w02-sh-command-line-arguments
next: w02-ps-readability
order: 28
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای اسکرابل (Scrabble)

> **منبع رسمی:** [Scrabble](https://cs50.harvard.edu/x/2026/psets/2/scrabble/) از پرابلم‌ست ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

در بازی Scrabble بازیکن‌ها واژه می‌سازند و امتیاز هر واژه جمع امتیاز حرف‌های آن است. جدول امتیاز حرف‌ها در صفحهٔ رسمی آمده است؛ مثلاً «CODE» هفت امتیاز دارد.

برنامه‌ای در `scrabble.c` (پوشهٔ `scrabble`) بنویس که دو بار ورودی بگیرد، یک واژه از «Player 1» و یکی از «Player 2»، و بسته به امتیاز، `Player 1 wins!`، `Player 2 wins!` یا `Tie!` چاپ کند.

## خواسته‌های رسمی

1. فایل `scrabble.c` در پوشهٔ `scrabble`
2. دو بار ورودی بگیرد: یک بار برای Player 1 و یک بار برای Player 2.
3. بسته به امتیاز بیشتر، یکی از سه پیام برنده یا مساوی را چاپ کند.
4. نویسه‌هایی که حرف نیستند امتیاز صفر دارند.

## شروع کار

پوشهٔ `scrabble` را بساز، واردش شو و `code scrabble.c` را اجرا کن (همان الگوی هفتهٔ ۱). این مسئله کد آغازین برای دانلود ندارد.

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: مساوی:

```text
$ ./scrabble
Player 1: Question?
Player 2: Question!
Tie!
```

نمونهٔ رسمی: برد Player 2:

```text
$ ./scrabble
Player 1: red
Player 2: wheelbarrow
Player 2 wins!
```

نمونهٔ رسمی: برد Player 1:

```text
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

نمونهٔ رسمی: حروف بزرگ و کوچک:

```text
$ ./scrabble
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- آرایه — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u02`)
- اندیس آرایه از صفر — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u02`)
- نویسه‌ها عددند: کدهای ASCII — [یادداشت](/kb/d/w02-n11) · درس کوتاه `w02-l06` (واحد `w02-l06-u01`)
- تبدیل حروف با حساب ASCII (تفاضل ۳۲) — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u03`)
- کتابخانهٔ ctype.h: islower و toupper — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u04`)
- رشته، آرایه‌ای از char — [یادداشت](/kb/d/w02-n12) · درس کوتاه `w02-l06` (واحد `w02-l06-u02`)
- strlen و string.h — [یادداشت](/kb/d/w02-n14) · درس کوتاه `w02-l07` (واحد `w02-l07-u02`)
- اجزای اعلان تابع: نوع بازگشتی، نام، فهرست آرگومان‌ها — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول شبه‌کد بنویس: گرفتن دو واژه، حساب امتیاز هر کدام، چاپ برنده. صفحهٔ رسمی هم همین سه گام را پیشنهاد می‌کند.
2. امتیاز هر دو واژه با یک قاعده حساب می‌شود. آیا جای یک تابع کمکی است؟ (یادداشت ثابت و تابع کمکی را ببین.)
3. ۲۶ امتیاز پشت سر هم داری. کدام ساختار دادهٔ این هفته برای نگه‌داشتن مقدارهای هم‌نوع پشت سر هم مناسب است؟
4. یادت باشد هر char در واقع یک عدد ASCII است. چطور می‌توان از این برای رسیدن از یک حرف به جایگاهش در الفبا استفاده کرد؟
5. حروف بزرگ و کوچک باید یکسان امتیاز بگیرند. کدام توابع ctype.h کمک می‌کنند؟

## اشتباه‌های رایج

- امتیاز دادن به علامت‌ها و رقم‌ها
- حساس بودن به بزرگی و کوچکی حرف
- دسترسی بیرون از مرز آرایه برای نویسه‌ای که حرف نیست
- پیام خروجی با فاصله یا علامت متفاوت

## چک‌لیست خودآزمایی

1. فایل `scrabble.c` در پوشهٔ `scrabble` است.
2. هر دو بازیکن واژه وارد می‌کنند.
3. پیام‌های خروجی دقیقاً با متن رسمی یکی‌اند.
4. واژه‌های با حروف بزرگ و کوچک و با علامت را امتحان کرده‌ام.
5. هر چهار نمونهٔ رسمی خروجی درست دارند.
6. check50 همه را سبز نشان می‌دهد.
7. style50 تغییری پیشنهاد نمی‌کند.
8. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/scrabble
```

سبک با style50:

```bash
style50 scrabble.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/scrabble
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد کامل گام‌به‌گام در «Advice and Hints» صفحهٔ رسمی](https://cs50.harvard.edu/x/psets/2/scrabble/#advice-and-hints): صفحهٔ رسمی خودش می‌گوید این بخش «full spoiler» است و کل راه‌حل را نشان می‌دهد (ناهمخوانی d33). این بسته آن را بازتولید نمی‌کند؛ پیشنهاد CS50 هم این است که اول خودت امتحان کنی.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/74B4kq3ftleKe6AdN0NxFV8CN)

## پیوند رسمی

- [Scrabble](https://cs50.harvard.edu/x/2026/psets/2/scrabble/)
- [پرابلم‌ست ۲](https://cs50.harvard.edu/x/psets/2/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
