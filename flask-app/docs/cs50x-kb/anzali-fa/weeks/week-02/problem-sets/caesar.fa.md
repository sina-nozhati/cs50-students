---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-ps-caesar
type: problem-set-guide
title: راهنمای رمز سزار (Caesar)
title_fa: رمز سزار (Caesar)
title_en: Caesar
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/2/caesar/
source_refs:
- src-pset-2-caesar#specification
- src-anzali-authored-2
- src-pset-2#what-to-do
concept_ids:
- w02-c-argc-argv
- w02-c-argv-strings
- w02-c-exit-status
- w02-c-early-return
- w02-c-char-ascii
- w02-c-ascii-case
- w02-c-ctype
- w02-c-cipher-key
- w02-c-rotation-cipher
problem_set_ref: weeks/week-02/problem-sets/caesar.json
prev: w02-ps-readability
next: w02-ps-substitution
order: 30
submission: one-of-caesar-substitution
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای رمز سزار (Caesar)

> **منبع رسمی:** [Caesar](https://cs50.harvard.edu/x/2026/psets/2/caesar/) از پرابلم‌ست ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از Caesar یا Substitution را تحویل بده (طبق صفحهٔ رسمی، اگر هر دو را تحویل بدهی نمرهٔ بالاتر ثبت می‌شود). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

گفته می‌شود سزار پیام‌های محرمانه را با جابه‌جا کردن هر حرف به اندازهٔ چند جایگاه «رمز» می‌کرد؛ مثلاً با کلید ۱، `HELLO` به `IFMMP` تبدیل می‌شود. گیرنده با جابه‌جایی در جهت مخالف آن را رمزگشایی می‌کند.

برنامه‌ای در `caesar.c` (پوشهٔ `caesar`) بنویس که کلید را به‌صورت آرگومان خط فرمان بگیرد، متن ساده را بپرسد و متن رمز را چاپ کند. این همان رمز چرخشی یادداشت [رمزنگاری](/kb/d/w02-n18) است.

## خواسته‌های رسمی

1. فایل `caesar.c` در پوشهٔ `caesar`
2. دقیقاً یک آرگومان خط فرمان بپذیرد: یک عدد صحیح نامنفی (k).
3. بدون آرگومان یا با بیش از یکی، پیام خطا چاپ کند و فوراً 1 برگرداند.
4. اگر نویسه‌ای از آرگومان رقم نبود، `Usage: ./caesar key` چاپ کند و 1 برگرداند.
5. فرض نکن k حداکثر ۲۶ است.
6. `plaintext:` (با دو فاصله، بدون خط تازه) چاپ کند و متن ساده را با get_string بگیرد.
7. `ciphertext:` (با یک فاصله) و متن رمز را چاپ کند؛ نویسه‌های غیرحرفی تغییر نکنند.
8. بزرگی و کوچکی حرف حفظ شود.
9. در پایان خط تازه چاپ کند و با 0 از main خارج شود.

## شروع کار

پوشهٔ `caesar` را بساز، واردش شو و `code caesar.c` را اجرا کن. صفحهٔ رسمی پیشنهاد می‌کند گام‌به‌گام جلو بروی: اول شمارش آرگومان‌ها، بعد بررسی کلید، بعد استفاده از کلید.

## نمونه‌های رسمی ورودی و خروجی

بدون آرگومان:

```text
$ ./caesar
Usage: ./caesar key
```

با سه آرگومان:

```text
$ ./caesar 1 2 3
Usage: ./caesar key
```

با یک آرگومان (فعلاً بدون خروجی):

```text
$ ./caesar 1
```

کلید عددی:

```text
$ ./caesar 42
```

کلید غیرعددی:

```text
$ ./caesar banana
Usage: ./caesar key
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- argc و argv — [یادداشت](/kb/d/w02-n16) · درس کوتاه `w02-l08` (واحد `w02-l08-u01`)
- همهٔ عناصر argv رشته‌اند — [یادداشت](/kb/d/w02-sh-command-line-arguments) · درس کوتاه `w02-l08` (واحد `w02-l08-u02`)
- وضعیت خروج (exit status) — [یادداشت](/kb/d/w02-n17) · درس کوتاه `w02-l08` (واحد `w02-l08-u03`)
- طراحی: بازگشت زودهنگام و else زائد — [یادداشت](/kb/d/w02-sec) · درس کوتاه `w02-l08` (واحد `w02-l08-u04`)
- نویسه‌ها عددند: کدهای ASCII — [یادداشت](/kb/d/w02-n11) · درس کوتاه `w02-l06` (واحد `w02-l06-u01`)
- تبدیل حروف با حساب ASCII (تفاضل ۳۲) — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u03`)
- کتابخانهٔ ctype.h: islower و toupper — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u04`)
- متن ساده، متن رمز، کلید و الگوریتم رمز — [یادداشت](/kb/d/w02-n18) · درس کوتاه `w02-l09` (واحد `w02-l09-u01`)
- رمز چرخشی (سزار و ROT13) و آزمودن همهٔ کلیدها — [یادداشت](/kb/d/w02-n18) · درس کوتاه `w02-l09` (واحد `w02-l09-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. گام اول فقط شمردن آرگومان‌هاست؛ پیش از هر چیز دیگر آن را درست کن و با `echo $?` بسنج.
2. argv[1] یک رشته است، نه عدد. برای بررسی رقم‌ها یک‌به‌یک روی نویسه‌ها حرکت کن؛ صفحهٔ رسمی تابعی از ctype.h را پیشنهاد می‌کند.
3. برای تبدیل رشتهٔ عددی به int، صفحهٔ رسمی تابعی از stdlib.h را نام می‌برد. manual.cs50.io را ببین.
4. با دست حساب کن: Z با کلید ۱ باید چه شود؟ و A با کلید ۲۷؟ قاعده‌ای که این دو را درست کند، بقیه را هم درست می‌کند.
5. اگر خروجی چیزی نشان نمی‌دهد، صفحهٔ رسمی پیشنهاد می‌کند موقتاً نویسه‌ها را با `%i` چاپ کنی تا ببینی بیرون از بازهٔ ASCII هستند یا نه.

## اشتباه‌های رایج

- فرض اینکه کلید حداکثر ۲۶ است
- رمز کردن علامت‌ها یا فاصله‌ها
- از دست رفتن بزرگی و کوچکی حرف
- یک فاصله به‌جای دو فاصله بعد از `plaintext:`
- بررسی نکردن argc پیش از دسترسی به argv[1]

## چک‌لیست خودآزمایی

1. فایل در پوشهٔ درست است.
2. بدون آرگومان و با چند آرگومان، پیام خطا و وضعیت خروج 1 (با `echo $?` بررسی کرده‌ام).
3. کلید غیرعددی مثل banana پیام Usage می‌دهد.
4. کلید بزرگ‌تر از ۲۶ را امتحان کرده‌ام.
5. `plaintext:` دو فاصله و `ciphertext:` یک فاصله دارد.
6. علامت‌ها و فاصله‌ها تغییر نمی‌کنند.
7. حروف بزرگ بزرگ و حروف کوچک کوچک می‌مانند.
8. نمونه‌های رسمی همان خروجی را می‌دهند.
9. check50 همه را سبز نشان می‌دهد.
10. style50 تغییری پیشنهاد نمی‌کند.
11. با submit50 تحویل داده‌ام (یا Substitution را).

## اشکال‌زدایی با debug50

صفحهٔ رسمی این فرمان‌ها را پیشنهاد می‌کند (اول یک نقطهٔ توقف بگذار):

اجرای debug50 با کلید:

```bash
debug50 ./caesar KEY
```

اجرای debug50 بدون کلید:

```bash
debug50 ./caesar
```

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/caesar
```

سبک با style50:

```bash
style50 caesar.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/caesar
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [شبه‌کد رسمی main و فراخوانی‌های نمونهٔ rotate](https://cs50.harvard.edu/x/psets/2/caesar/#advice): صفحهٔ رسمی شبه‌کد کامل main و نمونه‌های رفتار rotate را در «Hint»ها آورده و خودش می‌گوید شبه‌کد را کپی نکن؛ این بسته فقط پیوند می‌دهد.
- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/watch?v=V2uusmv2wxI): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/V2uusmv2wxI)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY)

## پیوند رسمی

- [Caesar](https://cs50.harvard.edu/x/2026/psets/2/caesar/)
- [پرابلم‌ست ۲](https://cs50.harvard.edu/x/psets/2/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
