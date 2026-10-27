---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sh-data-types
type: short-summary
title: 'ویدئوی کوتاه: انواع داده (Data Types)'
title_fa: انواع داده
title_en: Data Types
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/data_types/
source_refs:
- src-short-data-types
- src-anzali-inference-1
concept_ids:
- w01-c-data-types
- w01-c-type-sizes
- w01-c-void
- w01-c-variable-declaration
- w01-c-char
prev: w01-sec
next: w01-sh-operators
order: 22
video:
  youtube_id: Fc9htmvVZ9U
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: مقدمه
    evidence_en: null
  - start: 0:26
    start_seconds: 26
    title_fa: int و بازهٔ آن
    evidence_en: int
  - start: '1:50'
    start_seconds: 110
    title_fa: unsigned و پیشوندها
    evidence_en: unsigned
  - start: '3:18'
    start_seconds: 198
    title_fa: char و ASCII
    evidence_en: char
  - start: '4:15'
    start_seconds: 255
    title_fa: float
    evidence_en: floating point
  - start: '5:31'
    start_seconds: 331
    title_fa: double
    evidence_en: double
  - start: '6:23'
    start_seconds: 383
    title_fa: void
    evidence_en: void
  - start: '8:18'
    start_seconds: 498
    title_fa: bool از کتابخانهٔ CS50
    evidence_en: bool
  - start: '9:11'
    start_seconds: 551
    title_fa: string
    evidence_en: string
  - start: '10:14'
    start_seconds: 614
    title_fa: اعلان متغیر
    evidence_en: create a variable
  - start: '13:21'
    start_seconds: 801
    title_fa: مقداردهی اولیه
    evidence_en: initialization
  chapters_origin: inference
recorded: '2017'
---

# ویدئوی کوتاه: انواع داده (Data Types)

> **منبع رسمی:** [صفحهٔ Short «Data Types» در CS50x](https://cs50.harvard.edu/x/shorts/data_types/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئوی کوتاه انواع دادهٔ پایهٔ C و اندازهٔ آن‌ها را مرور می‌کند. پیام اصلی: در C باید نوع هر متغیر را خودت اعلام کنی، چون نوع تعیین می‌کند چه مقدار حافظه کنار گذاشته شود و چه مقدارهایی مجازند.

در پایان، شیوهٔ اعلان، انتساب و مقداردهی اولیهٔ متغیرها را می‌بینی.

## نکته‌های کلیدی

- `int` عدد صحیح است و ۴ بایت (۳۲ بیت) جا می‌گیرد؛ بازهٔ آن تقریباً از منفی ۲ میلیارد تا مثبت ۲ میلیارد است.
- `unsigned` یک پیشوند (qualifier) است: مقدارهای منفی را حذف می‌کند و بازهٔ مثبت را دو برابر می‌کند. پیشوندهای دیگر: `short`، `long` و `const`.
- `char` یک نویسه را در ۱ بایت نگه می‌دارد. طبق ASCII، `'A'` برابر ۶۵، `'a'` برابر ۹۷ و `'0'` برابر ۴۸ است.
- `float` عدد اعشاری با ۴ بایت است و دقت محدود دارد. `double` همان کار را با ۸ بایت و دقت بیشتر می‌کند.
- `void` یک نوع است اما نوع داده نیست. تابعی با نوع بازگشتی `void` چیزی برنمی‌گرداند؛ `(void)` در فهرست پارامترها یعنی تابع ورودی نمی‌گیرد.
- `bool` و `string` در C پایه نیستند و با `cs50.h` در دسترس قرار می‌گیرند.
- اعلان چند متغیر هم‌نوع در یک خط ممکن است. اگر اعلان و انتساب در یک خط باشند، به آن مقداردهی اولیه (initialization) می‌گوییم.
- متغیری را که اعلان کرده‌ای دوباره اعلان نکن؛ فقط مقدار تازه را منتسب کن.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`data_types.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=0s)
- [۰:۲۶ — int و بازهٔ آن](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=26s)
- [۱:۵۰ — unsigned و پیشوندها](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=110s)
- [۳:۱۸ — char و ASCII](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=198s)
- [۴:۱۵ — float](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=255s)
- [۵:۳۱ — double](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=331s)
- [۶:۲۳ — void](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=383s)
- [۸:۱۸ — bool از کتابخانهٔ CS50](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=498s)
- [۹:۱۱ — string](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=551s)
- [۱۰:۱۴ — اعلان متغیر](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=614s)
- [۱۳:۲۱ — مقداردهی اولیه](https://www.youtube.com/watch?v=Fc9htmvVZ9U&t=801s)

## مفاهیم مرتبط

- انواع داده در C — [یادداشت](/kb/d/w01-n10) · درس کوتاه `w01-l05` (واحد `w01-l05-u01`)
- اندازهٔ انواع (بایت) و بازه — [یادداشت](/kb/d/w01-sh-data-types) · درس کوتاه `w01-l05` (واحد `w01-l05-u02`)
- void: نبودِ ورودی یا خروجی — [یادداشت](/kb/d/w01-sh-data-types) · درس کوتاه `w01-l05` (واحد `w01-l05-u01`)
- اعلان متغیر با نوع — [یادداشت](/kb/d/w01-n07) · درس کوتاه `w01-l03` (واحد `w01-l03-u03`)
- نوع char و نقل‌قول تکی — [یادداشت](/kb/d/w01-n14) · درس کوتاه `w01-l08` (واحد `w01-l08-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/Fc9htmvVZ9U) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/data_types/data_types.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/data_types/lang/en/data_types.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/data_types/lang/en/data_types.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
