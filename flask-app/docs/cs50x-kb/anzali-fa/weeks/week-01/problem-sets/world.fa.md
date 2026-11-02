---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-ps-world
type: problem-set-guide
title: راهنمای سلام، دنیا
title_fa: سلام، دنیا
title_en: Hello, World
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/psets/1/world/
source_refs:
- src-pset-1-world#problem-to-solve
- src-anzali-authored-1
- src-pset-1#what-to-do
concept_ids:
- w01-c-code-make-run
- w01-c-printf
- w01-c-escape-sequence
- w01-c-header-file
- w01-c-main
- w01-c-linux-commands
problem_set_ref: weeks/week-01/problem-sets/world.json
prev: w01-sh-magic-numbers
next: w01-ps-me
order: 28
submission: do-not-submit
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای سلام، دنیا

> **منبع رسمی:** [Hello, World](https://cs50.harvard.edu/x/psets/1/world/) از پرابلم‌ست ۱ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** انجامش لازم است، اما تحویل ندارد. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

اولین برنامهٔ C تو: فایلی به نام `hello.c` در پوشه‌ای به نام `world` که `hello, world\n` را چاپ کند و تمام. صفحهٔ رسمی یادآوری می‌کند «hello, world» به لطف Brian Kernighan در صدها زبان پیاده شده است.

این مسئله تحویل ندارد، اما باید انجامش بدهی. هدفش آشنایی با چرخهٔ نوشتن، کامپایل و اجرا در cs50.dev است.

## خواسته‌های رسمی

1. فایل `hello.c` در پوشهٔ `world`
2. برنامه دقیقاً `hello, world\n` چاپ کند.

## شروع کار

ابتدا `cd` را تنها اجرا کن تا اعلان ترمینال به `$` برسد.

فرمان‌های رسمی:

```bash
mkdir world
cd world
code hello.c
make hello
ls
./hello
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- چرخهٔ code، make و اجرا با ./ — [یادداشت](/kb/d/w01-n04) · درس کوتاه `w01-l01` (واحد `w01-l01-u04`)
- تابع printf — [یادداشت](/kb/d/w01-n05) · درس کوتاه `w01-l02` (واحد `w01-l02-u01`)
- دنبالهٔ گریز — [یادداشت](/kb/d/w01-n05) · درس کوتاه `w01-l02` (واحد `w01-l02-u02`)
- فایل سرآیند و #include — [یادداشت](/kb/d/w01-n06) · درس کوتاه `w01-l03` (واحد `w01-l03-u01`)
- تابع main — [یادداشت](/kb/d/w01-n04) · درس کوتاه `w01-l01` (واحد `w01-l01-u04`)
- فرمان‌های پایهٔ لینوکس — [یادداشت](/kb/d/w01-n08) · درس کوتاه `w01-l04` (واحد `w01-l04-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اگر make خطا داد، اولین خطا را بخوان و در help50 یا CS50 Duck بپرس.
2. اگر اعلان ترمینال کنار خروجی آمد، به یادداشت دنبالهٔ گریز برگرد.

## اشتباه‌های رایج

- اجرای make در پوشهٔ اشتباه
- نوشتن `make hello.c` به‌جای `make hello`
- فراموش‌کردن `\n`
- فراموش‌کردن `;`
- بزرگ نوشتن H در hello

## چک‌لیست خودآزمایی

1. پوشهٔ `world` و فایل `hello.c` را ساخته‌ام.
2. کد را خودم تایپ کرده‌ام، نه کپی.
3. `make hello` بدون خطا اجرا شد.
4. `./hello` دقیقاً hello, world را در یک خط چاپ می‌کند و اعلان در خط بعد می‌آید.
5. check50 همه را سبز نشان می‌دهد.
6. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/world
```

سبک با style50:

```bash
style50 hello.c
```

این مسئله تحویل ندارد.

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد کامل در «Hint» صفحهٔ رسمی](https://cs50.harvard.edu/x/psets/1/world/#problem-to-solve): صفحهٔ رسمی خودش کد را می‌دهد و می‌گوید تایپش کن. این راهنما آن را تکرار نمی‌کند؛ کد همان hello.c درس‌نامه است: [یادداشت سلام دنیا](/kb/d/w01-n04).

## ویدئو و نمایش

- [ویدئوی معرفی مسئله](https://youtu.be/ufB53UE2Cvo)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/C5rag3703OZpKxGJ6dSwHnUEF)

## پیوند رسمی

- [Hello, World](https://cs50.harvard.edu/x/psets/1/world/)
- [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
