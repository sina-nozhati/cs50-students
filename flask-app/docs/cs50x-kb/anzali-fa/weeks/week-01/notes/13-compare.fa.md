---
id: w01-n13
type: note
title: 'compare.c: مقایسهٔ دو عدد صحیح (compare.c)'
title_fa: 'compare.c: مقایسهٔ دو عدد صحیح'
title_en: compare.c
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: compare.c
official_anchor: comparec
source_url: https://cs50.harvard.edu/x/notes/1/#comparec
source_refs:
- src-notes-1#comparec
- src-transcript-1
- src-short-operators
- src-srt-1
concept_ids:
- w01-c-relational-operators
- w01-c-get-int
- w01-c-comments
prev: w01-n12
next: w01-n14
order: 13
video:
  youtube_id: SlqjA04_dpk
  start: '1:09:08'
  start_seconds: 4148
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=4148s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'compare'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# compare.c: مقایسهٔ دو عدد صحیح

> **منبع رسمی:** بخش «compare.c» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#comparec). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۹:۰۸ تا حدود ۱:۱۷:۲۱](https://www.youtube.com/watch?v=SlqjA04_dpk&t=4148s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اولین برنامهٔ کامل با شرط: دو عدد از کاربر می‌گیری و آن‌ها را مقایسه می‌کنی. این برنامه `get_int`، متغیرهای `int`، **عملگرهای مقایسه‌ای** (relational operators) و **توضیح** (comment) را کنار هم می‌گذارد.

## نسخهٔ اول

در ترمینال `code compare.c` را بزن و این کد را بنویس:

```c
// Conditional, Boolean expression, relational operator

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for integers
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    // Compare integers
    if (x < y)
    {
        printf("x is less than y\n");
    }
}
```

- دو متغیر `int` به نام‌های `x` و `y` ساخته می‌شود.
- مقدار آن‌ها با `get_int` از کاربر گرفته می‌شود.
- خط‌هایی که با `//` شروع می‌شوند **توضیح** (comment) هستند؛ کامپایلر آن‌ها را نادیده می‌گیرد و برای خواننده‌اند.
- برای اجرا: `make compare` و سپس `./compare`.

## نسخهٔ کامل

```c
// Conditionals

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for integers
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    // Compare integers
    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }
}
```

- حالا همهٔ حالت‌های ممکن پوشش داده شده‌اند: کمتر، بیشتر، برابر.
- برنامه را دوباره بساز و اجرا کن و با عددهای مختلف آزمایش کن.

## نمودار جریان

درس‌نامه یادآوری می‌کند که تقریباً هر قطعه کد را می‌توان به شکل **نمودار جریان** (flowchart) کشید. با مقایسهٔ نمودارها، کارایی تصمیم‌های طراحی دیده می‌شود.

**از سخنرانی:** در نمودار نسخهٔ بهتر، اگر `x < y` درست باشد کار با یک پرسش تمام می‌شود؛ پرسش اضافی `x == y` حذف شده است.

## عملگرهای مقایسه‌ای

| عملگر | معنا |
| --- | --- |
| `<` | کمتر از |
| `>` | بیشتر از |
| `<=` | کمتر یا مساوی |
| `>=` | بیشتر یا مساوی |
| `==` | مساوی |
| `!=` | نامساوی |

> **منبع جدول:** ویدئوی کوتاه [Operators](/kb/d/w01-sh-operators). درس‌نامه در این بخش `<` و `>` و `==` را به کار می‌برد.

## اشتباه‌های رایج

- آزمایش برنامه فقط با یک جفت عدد. هر سه حالت را امتحان کن.
- فراموش کردن `#include <cs50.h>` برای `get_int`.

## جمع‌بندی

- `get_int` یک عدد صحیح از کاربر می‌گیرد.
- زنجیرهٔ `if`، `else if` و `else` همهٔ حالت‌ها را پوشش می‌دهد.

## پیوندها

- قبلی: [متغیرها، انتساب و افزایش](/kb/d/w01-n12)
- بعدی: [agree.c: نویسه‌ها و عملگرهای منطقی](/kb/d/w01-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
