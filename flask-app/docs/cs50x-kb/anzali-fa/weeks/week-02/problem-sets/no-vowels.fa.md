---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-pr-no-vowels
type: practice-guide
title: راهنمای بی‌واکه (No Vowels)
title_fa: بی‌واکه (No Vowels)
title_en: No Vowels
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/no-vowels/
source_refs:
- src-practice-no-vowels#implementation-details
- src-anzali-authored-2
concept_ids:
- w02-c-argc-argv
- w02-c-argv-strings
- w02-c-exit-status
- w02-c-early-return
- w02-c-string-char-array
- w02-c-function-anatomy
problem_set_ref: weeks/week-02/problem-sets/no-vowels.json
prev: w02-pr-hours
next: w02-pr-password
order: 33
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای بی‌واکه (No Vowels)

> **منبع رسمی:** [No Vowels](https://cs50.harvard.edu/x/2026/practice/no-vowels/) از مسئله‌های تمرینی هفتهٔ ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

«leetspeak» یعنی جایگزین کردن حرف‌ها با نمادهایی که شبیه آن‌ها هستند. در این تمرین برنامه‌ای می‌نویسی که برخی واکه‌های یک واژه را با رقم جایگزین کند؛ واژه از خط فرمان می‌آید.

کد آغازین فقط چند کتابخانه و یک main خالی دارد؛ یعنی برنامه را تقریباً از صفر می‌نویسی.

## خواسته‌های رسمی

1. فایل `no-vowels.c` در پوشهٔ `no-vowels`
2. دقیقاً یک آرگومان خط فرمان، یعنی واژه، بپذیرد.
3. بدون آرگومان یا با بیش از یکی، پیام خطا و return 1.
4. تابعی به نام `replace` داشته باشد که string بگیرد و string برگرداند.
5. a به 6، e به 3، i به 1 و o به 0 تبدیل شود و u تغییر نکند.
6. main واژهٔ تبدیل‌شده و سپس `\n` را چاپ کند.

## شروع کار

ابتدا `cd`، بعد `mkdir no-vowels` و `cd no-vowels`.

فایل آغازین رسمی را دانلود کن:

```bash
wget https://cdn.cs50.net/2022/fall/labs/2/no-vowels.c
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: بدون آرگومان:

```text
no-vowels/ $ ./no-vowels
Usage: ./no-vowels word
```

نمونهٔ رسمی: hello:

```text
no-vowels/ $ ./no-vowels hello
h3ll0
```

نمونهٔ رسمی: pseudocode:

```text
no-vowels/ $ ./no-vowels pseudocode
ps3ud0c0d3
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- argc و argv — [یادداشت](/kb/d/w02-n16) · درس کوتاه `w02-l08` (واحد `w02-l08-u01`)
- همهٔ عناصر argv رشته‌اند — [یادداشت](/kb/d/w02-sh-command-line-arguments) · درس کوتاه `w02-l08` (واحد `w02-l08-u02`)
- وضعیت خروج (exit status) — [یادداشت](/kb/d/w02-n17) · درس کوتاه `w02-l08` (واحد `w02-l08-u03`)
- طراحی: بازگشت زودهنگام و else زائد — [یادداشت](/kb/d/w02-sec) · درس کوتاه `w02-l08` (واحد `w02-l08-u04`)
- رشته، آرایه‌ای از char — [یادداشت](/kb/d/w02-n12) · درس کوتاه `w02-l06` (واحد `w02-l06-u02`)
- اجزای اعلان تابع: نوع بازگشتی، نام، فهرست آرگومان‌ها — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی تأکید می‌کند main در کد آغازین argc و argv دارد؛ از آن‌ها استفاده کن.
2. رشته آرایه‌ای از char است؛ می‌توانی نویسه‌به‌نویسه روی argv[1] حرکت کنی.
3. صفحهٔ رسمی پیشنهاد می‌کند دستور switch را امتحان کنی؛ راهنمای سبک CS50 را ببین.

## اشتباه‌های رایج

- دسترسی به argv[1] پیش از بررسی argc
- فراموش کردن `\n` در پایان
- تبدیل u

## چک‌لیست خودآزمایی

1. تعداد آرگومان‌ها را پیش از هر کار دیگری بررسی کرده‌ام.
2. تابع replace با امضای خواسته‌شده دارم.
3. هر چهار واکه درست تبدیل می‌شوند و u دست نمی‌خورد.
4. نمونه‌های رسمی همان خروجی را می‌دهند.
5. check50 همه را سبز نشان می‌دهد.
6. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/no-vowels
```

سبک با style50:

```bash
style50 no-vowels.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چرا ممکن است آرگومان خط فرمان را به get_string یا get_int ترجیح بدهی؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد آغازین no-vowels.c](https://cdn.cs50.net/2022/fall/labs/2/no-vowels.c): با wget دانلود کن.
- [راهنمای سبک: switch](https://cs50.readthedocs.io/style/c/#switches): پیوند رسمی صفحه.

## پیوند رسمی

- [No Vowels](https://cs50.harvard.edu/x/2026/practice/no-vowels/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
