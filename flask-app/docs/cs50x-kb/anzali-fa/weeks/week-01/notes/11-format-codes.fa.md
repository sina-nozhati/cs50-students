---
id: w01-n11
type: note
title: کدهای قالب در printf (Format Codes)
title_fa: کدهای قالب در printf
title_en: Format Codes
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Format Codes
official_anchor: format-codes
source_url: https://cs50.harvard.edu/x/notes/1/#format-codes
source_refs:
- src-notes-1#format-codes
- src-manual
- src-anzali-authored-1
- src-srt-1
concept_ids:
- w01-c-format-codes
prev: w01-n10
next: w01-n12
order: 11
video:
  youtube_id: SlqjA04_dpk
  start: '1:05:41'
  start_seconds: 3941
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=3941s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'percent I'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# کدهای قالب در printf

> **منبع رسمی:** بخش «Format Codes» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#format-codes). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۵:۴۱ تا حدود ۱:۰۶:۲۴](https://www.youtube.com/watch?v=SlqjA04_dpk&t=3941s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`printf` باید بداند مقداری که به آن می‌دهی از چه نوعی است. این را با **کد قالب** (format code) می‌گویی. کد قالب نادرست یعنی خروجی نادرست یا خطای کامپایل.

## فهرست درس‌نامه

پیش‌تر `%s` را برای رشته دیدی. درس‌نامه این فهرست ناقص (اما کافی برای این دوره) را می‌آورد:

```text
%c
%f
%i
%li
%s
```

| کد قالب | نوع | مثال کاربرد |
| --- | --- | --- |
| `%c` | `char` | یک نویسه |
| `%f` | `float` | عدد اعشاری |
| `%i` | `int` | عدد صحیح |
| `%li` | `long` | عدد صحیح بزرگ |
| `%s` | `string` | رشته |

- جزئیات بیشتر در [Manual Pages](https://manual.cs50.io) آمده است.
- در طول دوره از بسیاری از انواع داده‌ای C استفاده می‌کنی.

## نمونه‌های بیشتر در همین هفته

- در [Operators](/kb/d/w01-n19) خواهی دید که `%.50f` عدد اعشاری را با ۵۰ رقم بعد از ممیز چاپ می‌کند.
- همان‌جا می‌بینی که برای چاپ `long` باید `%li` را به کار ببری، نه `%i`.

## اشتباه‌های رایج

- چاپ `int` با `%s` یا رشته با `%i`؛ کامپایلر معمولاً به آن ایراد می‌گیرد (**تألیفی**).
- تعداد جای‌نگهدارها با تعداد مقدارها برابر نیست.

## جمع‌بندی

- هر نوع، کد قالب خودش را دارد: `%c`، `%f`، `%i`، `%li`، `%s`.

## پیوندها

- قبلی: [انواع داده در C](/kb/d/w01-n10)
- بعدی: [متغیرها، انتساب و افزایش](/kb/d/w01-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
