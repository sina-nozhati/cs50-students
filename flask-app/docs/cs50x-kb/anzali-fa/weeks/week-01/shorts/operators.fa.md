---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sh-operators
type: short-summary
title: 'ویدئوی کوتاه: عملگرها (Operators)'
title_fa: عملگرها
title_en: Operators
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/operators/
source_refs:
- src-short-operators
- src-anzali-inference-1
concept_ids:
- w01-c-arithmetic-operators
- w01-c-increment
- w01-c-logical-operators
- w01-c-relational-operators
- w01-c-equality-vs-assignment
prev: w01-sh-data-types
next: w01-sh-conditional-statements
order: 23
video:
  youtube_id: f1xZf4iJDWE
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: مقدمه و انتساب
    evidence_en: null
  - start: 0:23
    start_seconds: 23
    title_fa: عملگرهای حسابی
    evidence_en: arithmetic operators
  - start: '2:06'
    start_seconds: 126
    title_fa: باقی‌مانده
    evidence_en: modulus
  - start: '3:45'
    start_seconds: 225
    title_fa: کوتاه‌نویسی انتساب
    evidence_en: x times equals 5
  - start: '4:30'
    start_seconds: 270
    title_fa: افزایش و کاهش
    evidence_en: plus plus
  - start: '4:54'
    start_seconds: 294
    title_fa: عبارت‌های بولی
    evidence_en: Boolean expressions
  - start: '6:00'
    start_seconds: 360
    title_fa: صفر و غیرصفر
    evidence_en: every non-0
  - start: '7:04'
    start_seconds: 424
    title_fa: AND منطقی
    evidence_en: Logical AND
  - start: '8:02'
    start_seconds: 482
    title_fa: OR منطقی
    evidence_en: Logical OR
  - start: '10:04'
    start_seconds: 604
    title_fa: عملگرهای مقایسه‌ای
    evidence_en: relational operators
  - start: '11:06'
    start_seconds: 666
    title_fa: == در برابر =
    evidence_en: equals equals
  chapters_origin: inference
recorded: '2017'
---

# ویدئوی کوتاه: عملگرها (Operators)

> **منبع رسمی:** [صفحهٔ Short «Operators» در CS50x](https://cs50.harvard.edu/x/shorts/operators/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو عملگرهای C را معرفی می‌کند: انتساب، عملگرهای حسابی، عملگرهای کوتاه‌نویسی، عبارت‌های بولی، عملگرهای منطقی و مقایسه‌ای.

هشدار اصلی آن این است که `=` (انتساب) و `==` (مقایسه) را با هم اشتباه نگیری.

## نکته‌های کلیدی

- `=` انتساب است: مقدار سمت راست را در متغیر سمت چپ می‌گذارد.
- `+`، `-`، `*` و `/` عملگرهای حسابی‌اند. `%` باقی‌مانده است: `13 % 4` برابر `1` است. باقی‌مانده مثلاً برای محدود کردن عدد تصادفی به یک بازه کاربرد دارد.
- کوتاه‌نویسی: `x *= 5` یعنی `x = x * 5`؛ همین برای `+=`، `-=`، `/=` و `%=` برقرار است. `x++` و `x--` یکی اضافه یا کم می‌کنند.
- عبارت بولی درست یا نادرست است. در C هر مقدار غیرصفر درست و صفر نادرست شمرده می‌شود.
- عملگرهای منطقی: `&&` (و)، `||` (یا) و `!` (نقیض، که در انگلیسی «bang» هم خوانده می‌شود).
- عملگرهای مقایسه‌ای: `<`، `<=`، `>`، `>=`، `==` و `!=`.
- اشتباه رایج: نوشتن `=` به‌جای `==` در شرط.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`operators.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه و انتساب](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=0s)
- [۰:۲۳ — عملگرهای حسابی](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=23s)
- [۲:۰۶ — باقی‌مانده](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=126s)
- [۳:۴۵ — کوتاه‌نویسی انتساب](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=225s)
- [۴:۳۰ — افزایش و کاهش](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=270s)
- [۴:۵۴ — عبارت‌های بولی](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=294s)
- [۶:۰۰ — صفر و غیرصفر](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=360s)
- [۷:۰۴ — AND منطقی](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=424s)
- [۸:۰۲ — OR منطقی](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=482s)
- [۱۰:۰۴ — عملگرهای مقایسه‌ای](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=604s)
- [۱۱:۰۶ — == در برابر =](https://www.youtube.com/watch?v=f1xZf4iJDWE&t=666s)

## مفاهیم مرتبط

- عملگرهای حسابی و باقی‌مانده % — [یادداشت](/kb/d/w01-n19) · درس کوتاه `w01-l12` (واحد `w01-l12-u01`)
- افزایش و کاهش (+= ++ --) — [یادداشت](/kb/d/w01-n12) · درس کوتاه `w01-l06` (واحد `w01-l06-u01`)
- عملگرهای منطقی && || ! — [یادداشت](/kb/d/w01-n14) · درس کوتاه `w01-l08` (واحد `w01-l08-u02`)
- عملگرهای مقایسه‌ای — [یادداشت](/kb/d/w01-n13) · درس کوتاه `w01-l07` (واحد `w01-l07-u02`)
- == در برابر = — [یادداشت](/kb/d/w01-n14) · درس کوتاه `w01-l08` (واحد `w01-l08-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/f1xZf4iJDWE) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/operators/operators.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/operators/lang/en/operators.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/operators/lang/en/operators.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
