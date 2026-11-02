---
id: w01-n12
type: note
title: متغیرها، انتساب و افزایش (Variables)
title_fa: متغیرها، انتساب و افزایش
title_en: Variables
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Variables
official_anchor: variables
source_url: https://cs50.harvard.edu/x/notes/1/#variables
source_refs:
- src-notes-1#variables
- src-short-data-types
- src-short-operators
- src-srt-1
concept_ids:
- w01-c-increment
prev: w01-n11
next: w01-n13
order: 12
video:
  youtube_id: SlqjA04_dpk
  start: '1:06:24'
  start_seconds: 3984
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=3984s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'counter'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# متغیرها، انتساب و افزایش

> **منبع رسمی:** بخش «Variables» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#variables). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۶:۲۴ تا حدود ۱:۰۹:۰۸](https://www.youtube.com/watch?v=SlqjA04_dpk&t=3984s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

متغیرها حافظهٔ برنامه‌اند. در این بخش می‌بینی چطور یک متغیر عدد صحیح بسازی و مقدارش را یکی‌یکی زیاد یا کم کنی؛ همان کاری که شمارنده‌های حلقه می‌کنند.

## ساختن و مقداردهی

```c
int counter = 0;
```

- متغیری به نام `counter` از نوع `int` ساخته می‌شود و مقدار `0` می‌گیرد.
- **از ویدئوی کوتاه Data Types:** ساختن متغیر را **اعلان** (declaration) و دادن اولین مقدار را **مقداردهی اولیه** (initialization) می‌گویند. این خط هر دو کار را با هم می‌کند.

## سه راه برای «یکی اضافه کن»

```c
counter = counter + 1;
```

```c
counter += 1;
```

```c
counter++;
```

- هر سه خط کار یکسانی می‌کنند: یک واحد به `counter` اضافه می‌کنند.
- خط اول را از راست بخوان: «`counter + 1` را حساب کن و نتیجه را در `counter` بگذار».
- `+=` شکل کوتاه‌تر است و `++` کوتاه‌ترین.

## یکی کم کن

```c
counter--;
```

- `--` یک واحد از `counter` کم می‌کند.

## نکته‌های ویدئوهای کوتاه

- **Operators:** همین الگو برای عملگرهای دیگر هم کار می‌کند: `x *= 5` یعنی `x = x * 5`.
- **Data Types:** پس از اعلان یک متغیر، دیگر نوعش را تکرار نکن. `int counter = 0;` و بعد `int counter = 1;` خطاست؛ فقط بنویس `counter = 1;`.

## اشتباه‌های رایج

- `counter + 1;` به‌تنهایی مقدار را عوض نمی‌کند؛ نتیجه جایی ذخیره نمی‌شود.
- اعلان دوبارهٔ یک متغیر با همان نام در همان بخش کد.

## جمع‌بندی

- `int counter = 0;` اعلان و مقداردهی است.
- `counter = counter + 1`، `counter += 1` و `counter++` معادل‌اند؛ `counter--` یکی کم می‌کند.

## پیوندها

- قبلی: [کدهای قالب در printf](/kb/d/w01-n11)
- بعدی: [compare.c: مقایسهٔ دو عدد صحیح](/kb/d/w01-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
