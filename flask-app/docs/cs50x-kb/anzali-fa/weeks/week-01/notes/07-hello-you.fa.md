---
id: w01-n07
type: note
title: 'سلام به تو: get_string، متغیر و جای‌نگهدار (Hello, You)'
title_fa: 'سلام به تو: get_string، متغیر و جای‌نگهدار'
title_en: Hello, You
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Hello, You
official_anchor: hello-you
source_url: https://cs50.harvard.edu/x/notes/1/#hello-you
source_refs:
- src-notes-1#hello-you
- src-transcript-1
- src-srt-1
concept_ids:
- w01-c-get-string
- w01-c-variable-declaration
- w01-c-assignment-operator
- w01-c-placeholder
prev: w01-n06
next: w01-n08
order: 7
video:
  youtube_id: SlqjA04_dpk
  start: '32:00'
  start_seconds: 1920
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=1920s
  origin: inference
  basis: first lecture1.srt cue containing the phrase "what's your name"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# سلام به تو: get_string، متغیر و جای‌نگهدار

> **منبع رسمی:** بخش «Hello, You» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#hello-you). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۲:۰۰ تا حدود ۴۴:۳۸](https://www.youtube.com/watch?v=SlqjA04_dpk&t=1920s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در Scratch با `ask` نام کاربر را می‌پرسیدی و با `join` آن را کنار «hello» می‌گذاشتی. در C همین کار به سه مفهوم تازه نیاز دارد: **متغیر**، **نوع داده** و **جای‌نگهدار**.

## تلاش اول: جای‌نگهدار نادرست

درس‌نامه ابتدا این نسخه را نشان می‌دهد:

```c
// get_string and printf with incorrect placeholder

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, answer\n");
}
```

- تابع `get_string` یک **رشته** (string) از کاربر می‌گیرد.
- مقدار برگشتی در متغیر `answer` ریخته می‌شود.
- با `make hello`، خطاهای زیادی ظاهر می‌شود. در نسخهٔ رسمی کامپایلر `string` و `get_string` را نمی‌شناسد؛ باید کتابخانهٔ `cs50.h` اضافه شود.
- مشکل دوم: `printf("hello, answer\n")` کلمهٔ «answer» را عیناً چاپ می‌کند، نه مقدار متغیر را.

## نسخهٔ درست با %s

```c
// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

- `%s` یک **جای‌نگهدار** (placeholder) است. به `printf` می‌گوید آماده باشد یک `string` دریافت کند.
- `answer` بعد از ویرگول به `printf` داده می‌شود و جای `%s` می‌نشیند.
- حالا برنامه نامت را می‌پرسد و به تو سلام می‌کند.

## متغیر و نوع داده

- `answer` جایی برای نگهداری داده است که به آن **متغیر** می‌گوییم.
- نوع `answer` از جنس `string` است و می‌تواند هر رشته‌ای را نگه دارد.
- **انواع داده** (data types) دیگری هم هست، مثل `int`، `bool` و `char`.
- `%s` را **کد قالب** (format code) هم می‌نامیم. فهرست کدهای قالب را در [کدهای قالب](/kb/d/w01-n11) می‌بینی.

## سخنرانی چه می‌گوید

**از سخنرانی:** علامت `=` در C به معنای «برابری» نیست؛ **انتساب** (assignment) است: مقدار سمت راست را در متغیر سمت چپ می‌ریزد. خط را از راست به چپ بخوان: «get_string را صدا بزن و نتیجه را در answer بگذار».

## اشتباه‌های رایج

- نوشتن نام متغیر داخل نقل‌قول به‌جای جای‌نگهدار.
- فراموش کردن ویرگول میان رشتهٔ قالب و متغیر.
- فراموش کردن `#include <cs50.h>`.

## جمع‌بندی

- `string answer = get_string("...");` مقدار ورودی را در متغیر نگه می‌دارد.
- `%s` جای مقدار رشته را در `printf` نگه می‌دارد.

## پیوندها

- قبلی: [فایل‌های سرآیند، کتابخانه‌ها و راهنمای CS50](/kb/d/w01-n06)
- بعدی: [لینوکس و فرمان‌های ترمینال](/kb/d/w01-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
