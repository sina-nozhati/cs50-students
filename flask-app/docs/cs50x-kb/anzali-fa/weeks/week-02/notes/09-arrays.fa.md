---
id: w02-n09
type: note
title: 'آرایه‌ها و حلقه‌ها (Arrays: declaring and looping)'
title_fa: آرایه‌ها و حلقه‌ها
title_en: 'Arrays: declaring and looping'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Arrays
official_anchor: arrays
source_url: https://cs50.harvard.edu/x/2026/notes/2/#arrays
source_refs:
- src-notes-2#arrays
- src-transcript-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-array
- w02-c-array-index
- w02-c-array-loop
prev: w02-n08
next: w02-n10
order: 9
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:12:46'
  start_seconds: 4366
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=4366s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'array'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# آرایه‌ها و حلقه‌ها

> **منبع رسمی:** بخش «Arrays» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#arrays). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۲:۴۶ تا حدود ۱:۱۹:۴۱](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=4366s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اگر به‌جای سه نمره، صد نمره داشتی چه؟ صد متغیر جدا با نام‌های `score1` تا `score100`؟ **آرایه** (`array`) راه‌حل است: دنباله‌ای از مقدارها که **پشت‌سرهم** در حافظه ذخیره می‌شوند.

## شروع: سه متغیر جدا

درس‌نامه می‌خواهد با `code scores.c` این برنامه را بنویسی:

```c
// Averages three (hardcoded) numbers

#include <stdio.h>

int main(void)
{
    // Scores
    int score1 = 72;
    int score2 = 73;
    int score3 = 33;

    // Print average
    printf("Average: %f\n", (score1 + score2 + score3) / 3.0);
}
```

- عدد سمت راست تقسیم `3.0` است، یک مقدار اعشاری؛ پس حاصل نهایی هم اعشاری محاسبه می‌شود.
- `make scores` کامپایل می‌کند و `./scores` اجرا.
- این سه متغیر در حافظه کنار هم می‌نشینند (تصویر رسمی «scores in memory»، فقط پیوند).
- **از سخنرانی:** David اول تقسیم را بر `3` نوشت و خروجی `59` شد؛ همان **بریدن** (`truncation`) هفتهٔ ۱. با `3.0` حاصل `59.333333` شد.

## آرایه

- **آرایه** دنباله‌ای از مقدارهاست که پشت‌سرهم در حافظه ذخیره می‌شوند.
- `int scores[3]` به کامپایلر می‌گوید سه جای پشت‌سرهم به اندازهٔ `int` برای سه نمره بدهد.

```c
// Averages three (hardcoded) numbers using an array

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Scores
    int scores[3];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    // Print average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}
```

- `scores[0]` با **اندیس‌گذاری** (`indexing`) در آرایهٔ `scores` در جایگاه `0` مقدار ذخیره‌شده در آن را می‌خواند.
- اندیس از **۰** شروع می‌شود؛ پس سه خانه `scores[0]`، `scores[1]` و `scores[2]` هستند.

## آرایه و حلقه

درس‌نامه می‌گوید کد بالا کار می‌کند، اما هنوز جای بهتر شدن دارد:

```c
// Averages three numbers using an array and a loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get scores
    int scores[3];
    for (int i = 0; i < 3; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Print average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}
```

- با `scores[i]` در آرایه اندیس می‌گذاریم و `i` را حلقهٔ `for` فراهم می‌کند.
- حالا نمره‌ها از کاربر گرفته می‌شوند و کد گرفتن ورودی سه بار تکرار نشده است.

> **تألیفی:** هنوز یک بوی بد مانده: عدد `3` در سه جا تکرار شده است. یادداشت بعد آن را با یک ثابت درست می‌کند.

## اشتباه‌های رایج

- دسترسی به `scores[3]` در آرایه‌ای سه‌خانه‌ای. آخرین اندیس `2` است.
- نوشتن `i <= 3` در شرط حلقه؛ یک دور اضافه و بیرون زدن از آرایه.
- تقسیم بر `3` به‌جای `3.0` و از دست رفتن بخش اعشاری.

## جمع‌بندی

- `type name[size]` آرایه‌ای با `size` خانهٔ هم‌نوع و پشت‌سرهم می‌سازد.
- اندیس‌ها از ۰ تا `size - 1` هستند و حلقهٔ `for` بهترین دوست آرایه است.

## پیوندها

- قبلی: [حافظه و اندازهٔ انواع داده](/kb/d/w02-n08)
- بعدی: [ثابت سراسری و آرایه به‌عنوان آرگومان تابع](/kb/d/w02-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
