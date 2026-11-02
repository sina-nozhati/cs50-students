---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-pr-bottomup
type: practice-guide
title: راهنمای از پایین به بالا (Bottom Up)
title_fa: از پایین به بالا (Bottom Up)
title_en: Bottom Up
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/bottomup/
source_refs:
- src-practice-bottomup#background
- src-practice-bottomup#implementation-details
- src-anzali-authored-4
concept_ids:
- w04-c-file-header
- w04-c-bmp-rgbtriple
- w04-c-typedef-struct
- w04-c-fread-fwrite
- w04-c-stdint-types
problem_set_ref: weeks/week-04/problem-sets/bottomup.json
prev: w04-ps-recover
next: w04-pr-license
order: 27
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای از پایین به بالا (Bottom Up)

> **منبع رسمی:** [Bottom Up](https://cs50.harvard.edu/x/2026/practice/bottomup/) از مسئله‌های تمرینی هفتهٔ ۴ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

تصویری که باید در یک ارائهٔ مهم نشان بدهی خراب شده و وارونه دیده می‌شود. پیکسل‌ها سالم‌اند؛ مشکل در **فراداده** (metadata) است، یعنی سرآیندهای ابتدای فایل BMP که ارتفاع، عرض و چیزهای دیگر را توصیف می‌کنند.

کار تو: با کد، فراداده را طوری ویرایش کنی که سطر بالای تصویر اول و سطر پایین آخر بیاید. صفحهٔ رسمی تأکید می‌کند به خود پیکسل‌ها دست نزن تا فایل بیشتر خراب نشود.

## خواسته‌های رسمی

1. فراداده را با کد ویرایش کن تا سطر بالای تصویر اول و سطر پایین آخر باشد.
2. پیکسل‌ها را مستقیم ویرایش نکن.
3. در `bottomup.c` کمی کد بنویس تا تصویر از پایین‌به‌بالا به بالا‌به‌پایین تبدیل شود.

## شروع کار

در ترمینال cs50.dev اول `cd` را تنها اجرا کن، بعد فایل‌ها را با فرمان رسمی دانلود کن (نشانی دانلود قدیمی‌تر است؛ ناهمخوانی d63). در پوشه `bmp.h`، `bottomup.c` و تصویر وارونهٔ `harvard_bottomup.bmp` هست.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/4/bottomup.zip
unzip bottomup.zip
rm bottomup.zip
```

## نمونه‌های رسمی ورودی و خروجی

اجرای نمونه:

```text
bottomup/ $ ./bottomup harvard_bottomup.bmp harvard_topdown.bmp
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- سرآیند فایل: فرادادهٔ ابتدای فایل (WAV و BMP) — [یادداشت](/kb/d/w04-ps-volume) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)
- BMP، RGBTRIPLE و ترتیب BGR — [یادداشت](/kb/d/w04-ps-filter-less) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)
- typedef همراه struct برای ساختن نوع دلخواه — [یادداشت](/kb/d/w04-sh-defining-custom-types) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)
- fread و fwrite: خواندن و نوشتن بایت‌ها — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)
- نوع‌های اندازه‌دقیق stdint.h: uint8_t و int16_t — [یادداشت](/kb/d/w04-ps-volume) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. `bmp.h` را باز کن و فیلدهای struct `BITMAPINFOHEADER` را یکی‌یکی بخوان.
2. صفحهٔ رسمی پیشنهاد می‌کند مستند Microsoft هر فیلد را بخوانی. کدام فیلد دربارهٔ جهت ذخیرهٔ سطرها چیزی می‌گوید؟
3. در `bottomup.c` ببین سرآیندها کجا خوانده و کجا نوشته می‌شوند. تغییر تو باید بین این دو باشد.
4. صفحهٔ رسمی می‌گوید این کد لازم نیست پیچیده باشد.

## اشتباه‌های رایج

- دست زدن به پیکسل‌ها
- تغییر سرآیند پس از نوشته شدنش در فایل خروجی
- تغییر فیلد اشتباه از سرآیند

## چک‌لیست خودآزمایی

1. فقط فراداده را تغییر داده‌ام، نه پیکسل‌ها را.
2. تصویر خروجی `harvard_topdown.bmp` ساخته می‌شود و درست ایستاده است.
3. تغییرم در `bottomup.c` است.
4. check50 همه را سبز نشان می‌دهد.
5. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/bottomup
```

سبک با style50:

```bash
style50 bottomup.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: Why do image files need metadata?

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [مستند Microsoft برای BITMAPINFOHEADER](https://learn.microsoft.com/en-us/previous-versions//dd183376(v=vs.85)): مرجع بیرونی که صفحهٔ رسمی پیشنهاد می‌کند.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/PTWrnMK23dr9co7YhmLzGU1lM)

## پیوند رسمی

- [Bottom Up](https://cs50.harvard.edu/x/2026/practice/bottomup/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
