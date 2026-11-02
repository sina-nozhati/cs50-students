---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-ps-substitution
type: problem-set-guide
title: راهنمای رمز جانشینی (Substitution)
title_fa: رمز جانشینی (Substitution)
title_en: Substitution
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/2/substitution/
source_refs:
- src-pset-2-substitution#specification
- src-anzali-authored-2
- src-pset-2#what-to-do
concept_ids:
- w02-c-argc-argv
- w02-c-exit-status
- w02-c-early-return
- w02-c-cryptography
- w02-c-cipher-key
- w02-c-string-length
- w02-c-array-index
- w02-c-ascii-case
- w02-c-ctype
problem_set_ref: weeks/week-02/problem-sets/substitution.json
prev: w02-ps-caesar
next: w02-pr-hours
order: 31
submission: one-of-caesar-substitution
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای رمز جانشینی (Substitution)

> **منبع رسمی:** [Substitution](https://cs50.harvard.edu/x/2026/psets/2/substitution/) از پرابلم‌ست ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از Caesar یا Substitution را تحویل بده (طبق صفحهٔ رسمی، اگر هر دو را تحویل بدهی نمرهٔ بالاتر ثبت می‌شود). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

در رمز جانشینی هر حرف با حرف دیگری جایگزین می‌شود. کلید یک نگاشت ۲۶حرفی است؛ مثلاً با کلید `NQXPOMAFTRHLZGECYJIUWSKDVB`، A به N و B به Q تبدیل می‌شود و `HELLO` به `FOLLE`.

برنامه‌ای در `substitution.c` (پوشهٔ `substitution`) بنویس که کلید را به‌صورت آرگومان خط فرمان بگیرد و پیام را رمز کند. این نسخه برای کسانی است که «بیشتر احساس راحتی» می‌کنند؛ یکی از Caesar یا Substitution کافی است.

## خواسته‌های رسمی

1. فایل `substitution.c` در پوشهٔ `substitution`
2. دقیقاً یک آرگومان (کلید) بپذیرد؛ کلید به بزرگی و کوچکی حساس نیست.
3. بدون آرگومان یا با بیش از یکی، پیام خطا و return 1.
4. کلید نامعتبر (نه ۲۶ نویسه، نویسهٔ غیرحرفی، یا حرف تکراری) پیام خطا و return 1.
5. `plaintext:` چاپ کند و متن ساده را با get_string بگیرد.
6. `ciphertext:` و متن رمز را چاپ کند؛ نویسه‌های غیرحرفی تغییر نکنند.
7. بزرگی و کوچکی حرف حفظ شود.
8. در پایان خط تازه و return 0.

## شروع کار

پوشهٔ `substitution` را بساز، واردش شو و `code substitution.c` را اجرا کن. صفحهٔ رسمی نمونهٔ اجرای کامل ندارد؛ نمایش asciinema را ببین.

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- argc و argv — [یادداشت](/kb/d/w02-n16) · درس کوتاه `w02-l08` (واحد `w02-l08-u01`)
- وضعیت خروج (exit status) — [یادداشت](/kb/d/w02-n17) · درس کوتاه `w02-l08` (واحد `w02-l08-u03`)
- طراحی: بازگشت زودهنگام و else زائد — [یادداشت](/kb/d/w02-sec) · درس کوتاه `w02-l08` (واحد `w02-l08-u04`)
- رمزنگاری — [یادداشت](/kb/d/w02-n18) · درس کوتاه `w02-l09` (واحد `w02-l09-u01`)
- متن ساده، متن رمز، کلید و الگوریتم رمز — [یادداشت](/kb/d/w02-n18) · درس کوتاه `w02-l09` (واحد `w02-l09-u01`)
- شمردن طول رشته تا NUL — [یادداشت](/kb/d/w02-n14) · درس کوتاه `w02-l07` (واحد `w02-l07-u01`)
- اندیس آرایه از صفر — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u02`)
- تبدیل حروف با حساب ASCII (تفاضل ۳۲) — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u03`)
- کتابخانهٔ ctype.h: islower و toupper — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u04`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. سه شرط کلید نامعتبر را جدا جدا بنویس و هر کدام را جدا امتحان کن.
2. برای «هر حرف دقیقاً یک بار»، فکر کن چطور می‌توانی دیده‌شدن هر حرف را ثبت کنی.
3. کلید یک رشتهٔ ۲۶تایی است و رشته آرایه است. جایگاه هر حرف متن ساده در الفبا، کدام خانهٔ کلید را نشان می‌دهد؟
4. کلید به بزرگی و کوچکی حساس نیست، اما خروجی باید بزرگی و کوچکی متن ساده را حفظ کند. ctype.h را ببین.

## اشتباه‌های رایج

- نپذیرفتن کلید با حروف کوچک
- پذیرفتن کلید با حرف تکراری
- از دست رفتن بزرگی و کوچکی حرف
- رمز کردن علامت‌ها

## چک‌لیست خودآزمایی

1. فایل در پوشهٔ درست است.
2. کلید با حروف کوچک هم همان نتیجه را می‌دهد.
3. بدون آرگومان یا با چند آرگومان، return 1.
4. کلید کوتاه، کلید با رقم و کلید با حرف تکراری را رد می‌کند.
5. علامت‌ها تغییر نمی‌کنند.
6. بزرگی و کوچکی حرف حفظ می‌شود.
7. مثال HELLO با کلید صفحهٔ رسمی FOLLE می‌دهد.
8. check50 همه را سبز نشان می‌دهد.
9. style50 تغییری پیشنهاد نمی‌کند.
10. با submit50 تحویل داده‌ام (یا Caesar را).

## اشکال‌زدایی با debug50

صفحهٔ رسمی این فرمان‌ها را پیشنهاد می‌کند (اول یک نقطهٔ توقف بگذار):

اجرای debug50 با کلید:

```bash
debug50 ./substitution KEY
```

اجرای debug50 بدون کلید:

```bash
debug50 ./substitution
```

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/substitution
```

سبک با style50:

```bash
style50 substitution.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/substitution
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/watch?v=cXAoZAsgxJ4): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/cXAoZAsgxJ4)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY)

## پیوند رسمی

- [Substitution](https://cs50.harvard.edu/x/2026/psets/2/substitution/)
- [پرابلم‌ست ۲](https://cs50.harvard.edu/x/psets/2/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
