---
id: w01-n10
type: note
title: انواع داده در C (Types)
title_fa: انواع داده در C
title_en: Types
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Types
official_anchor: types
source_url: https://cs50.harvard.edu/x/notes/1/#types
source_refs:
- src-notes-1#types
- src-transcript-1
- src-short-data-types
- src-srt-1
concept_ids:
- w01-c-data-types
prev: w01-n09
next: w01-n11
order: 10
video:
  youtube_id: SlqjA04_dpk
  start: '1:03:21'
  start_seconds: 3801
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=3801s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'float'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# انواع داده در C

> **منبع رسمی:** بخش «Types» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#types). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۳:۲۱ تا حدود ۱:۰۵:۴۱](https://www.youtube.com/watch?v=SlqjA04_dpk&t=3801s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در C هر متغیر باید **نوع** (type) داشته باشد. نوع تعیین می‌کند متغیر چه چیزی را نگه می‌دارد و کامپیوتر چه مقدار حافظه برایش کنار بگذارد.

## فهرست درس‌نامه

درس‌نامه این انواع را نام می‌برد (سه نقطه یعنی فهرست ادامه دارد):

```text
bool
char
float
int
long
string
...
```

| نوع | چه چیزی نگه می‌دارد |
| --- | --- |
| `bool` | درست یا نادرست (`true` / `false`) |
| `char` | یک نویسه، مثل `'y'` |
| `float` | عدد اعشاری (ممیز شناور) |
| `int` | عدد صحیح |
| `long` | عدد صحیح بزرگ‌تر |
| `string` | رشته‌ای از نویسه‌ها |

## اندازه‌ها، از ویدئوی کوتاه Data Types

ویدئوی کوتاه [Data Types](/kb/d/w01-sh-data-types) این جزئیات را اضافه می‌کند:

| نوع | اندازه | نکته |
| --- | --- | --- |
| `int` | ۴ بایت (۳۲ بیت) | بازه تقریباً از منفی ۲ میلیارد تا مثبت ۲ میلیارد |
| `char` | ۱ بایت | در ASCII، `'A'` برابر ۶۵ است |
| `float` | ۴ بایت | دقت محدود دارد |
| `double` | ۸ بایت | دقت بیشتری از `float` دارد |
| `long` | ۸ بایت | طبق سخنرانی، ۶۴ بیت |

- `bool` و `string` جزو C پایه نیستند. با `#include <cs50.h>` در دسترس قرار می‌گیرند.
- `unsigned` یک «پیشوند» (qualifier) است: عدد را فقط مثبت می‌کند و بازهٔ مثبت را دو برابر می‌کند.
- `void` یک نوع است، اما نوع داده نیست. یعنی «هیچ». در `int main(void)` یعنی `main` ورودی نمی‌گیرد.

## سخنرانی چه می‌گوید

**از سخنرانی:** اگر به دقت بیشتر نیاز داری، می‌توانی متغیر را از `float` به `double` «ارتقا» بدهی. همین‌طور برای عددهای صحیح خیلی بزرگ، `long` به‌جای `int`.

## اشتباه‌های رایج

- استفاده از `int` برای عددی که بخش اعشاری دارد.
- فراموش کردن `cs50.h` هنگام استفاده از `string` یا `bool`.

## جمع‌بندی

- هر متغیر در C نوع دارد.
- نوع، اندازهٔ حافظه و بازهٔ مقدارها را تعیین می‌کند.

## پیوندها

- قبلی: [شرط‌ها در C](/kb/d/w01-n09)
- بعدی: [کدهای قالب در printf](/kb/d/w01-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
