---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sh-magic-numbers
type: short-summary
title: 'ویدئوی کوتاه: عددهای جادویی (Magic Numbers)'
title_fa: عددهای جادویی
title_en: Magic Numbers
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/magic_numbers/
source_refs:
- src-short-magic-numbers
- src-anzali-inference-1
concept_ids:
- w01-c-magic-numbers
- w01-c-constant
- w01-c-header-file
prev: w01-sh-command-line
next: w01-ps-world
order: 27
video:
  youtube_id: vK_naJkrtjc
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: عدد جادویی چیست
    evidence_en: null
  - start: '1:08'
    start_seconds: 68
    title_fa: مثال دستهٔ کارت
    evidence_en: deck
  - start: '2:40'
    start_seconds: 160
    title_fa: مشکل متغیر
    evidence_en: declared globally
  - start: '3:16'
    start_seconds: 196
    title_fa: '#define و پیش‌پردازنده'
    evidence_en: preprocessor directive
  - start: '4:39'
    start_seconds: 279
    title_fa: جایگزینی هنگام کامپایل
    evidence_en: at compile time
  - start: '5:21'
    start_seconds: 321
    title_fa: قرارداد حروف بزرگ
    evidence_en: all caps
  - start: '6:38'
    start_seconds: 398
    title_fa: مزیت ثابت‌ها
    evidence_en: Germany
  chapters_origin: inference
recorded: '2017'
---

# ویدئوی کوتاه: عددهای جادویی (Magic Numbers)

> **منبع رسمی:** [صفحهٔ Short «Magic Numbers» در CS50x](https://cs50.harvard.edu/x/shorts/magic_numbers/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو توضیح می‌دهد چرا نوشتن عددهای ثابت بی‌نام در کد («عدد جادویی») طراحی بدی است و C چطور با `#define` ثابت نمادین می‌سازد.

## نکته‌های کلیدی

- عدد جادویی عددی است که بی‌توضیح در کد آمده و معنایش برای خواننده روشن نیست؛ مثال ویدئو حلقه‌ای است که تا `52` (تعداد کارت‌های یک دسته) می‌شمارد.
- گذاشتن عدد در یک متغیر کمک می‌کند، اما متغیر ممکن است به‌اشتباه تغییر کند.
- `#define NAME REPLACEMENT` یک **دستور پیش‌پردازنده** (preprocessor directive) است و ثابت نمادین می‌سازد. پیش از کامپایل، هر `NAME` با `REPLACEMENT` جایگزین می‌شود، مثل «پیدا کن و جایگزین کن».
- پایان خط `#define` نقطه‌ویرگول ندارد.
- طبق قرارداد، نام ثابت‌های `#define` با حروف بزرگ نوشته می‌شود.
- مزیت: برای تغییر مقدار (مثلاً دستهٔ ۳۲ کارتی در آلمان) فقط یک خط را عوض می‌کنی.
- در درس‌نامهٔ ۲۰۲۶ همین ایده با `const int n = 3;` آمده است ([Mario](/kb/d/w01-n18)).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`magic_numbers.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — عدد جادویی چیست](https://www.youtube.com/watch?v=vK_naJkrtjc&t=0s)
- [۱:۰۸ — مثال دستهٔ کارت](https://www.youtube.com/watch?v=vK_naJkrtjc&t=68s)
- [۲:۴۰ — مشکل متغیر](https://www.youtube.com/watch?v=vK_naJkrtjc&t=160s)
- [۳:۱۶ — #define و پیش‌پردازنده](https://www.youtube.com/watch?v=vK_naJkrtjc&t=196s)
- [۴:۳۹ — جایگزینی هنگام کامپایل](https://www.youtube.com/watch?v=vK_naJkrtjc&t=279s)
- [۵:۲۱ — قرارداد حروف بزرگ](https://www.youtube.com/watch?v=vK_naJkrtjc&t=321s)
- [۶:۳۸ — مزیت ثابت‌ها](https://www.youtube.com/watch?v=vK_naJkrtjc&t=398s)

## مفاهیم مرتبط

- عدد جادویی و #define — [یادداشت](/kb/d/w01-sh-magic-numbers) · درس کوتاه `w01-l11` (واحد `w01-l11-u03`)
- ثابت با const — [یادداشت](/kb/d/w01-n18) · درس کوتاه `w01-l11` (واحد `w01-l11-u03`)
- فایل سرآیند و #include — [یادداشت](/kb/d/w01-n06) · درس کوتاه `w01-l03` (واحد `w01-l03-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/vK_naJkrtjc) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/magic_numbers/magic_numbers.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
