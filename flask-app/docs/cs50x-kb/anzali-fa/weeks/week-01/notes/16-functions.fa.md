---
id: w01-n16
type: note
title: 'توابع: انتزاع، پارامتر، حوزه و مقدار بازگشتی (Functions)'
title_fa: 'توابع: انتزاع، پارامتر، حوزه و مقدار بازگشتی'
title_en: Functions
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Functions
official_anchor: functions
source_url: https://cs50.harvard.edu/x/notes/1/#functions
source_refs:
- src-notes-1#functions
- src-transcript-1
- src-anzali-authored-1
- src-srt-1
concept_ids:
- w01-c-function-definition
- w01-c-prototype
- w01-c-parameter
- w01-c-scope
- w01-c-return-value
prev: w01-n15
next: w01-n17
order: 16
video:
  youtube_id: SlqjA04_dpk
  start: '1:46:09'
  start_seconds: 6369
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=6369s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'invent'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# توابع: انتزاع، پارامتر، حوزه و مقدار بازگشتی

> **منبع رسمی:** بخش «Functions» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#functions). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۶:۰۹ تا حدود ۱:۵۸:۳۴](https://www.youtube.com/watch?v=SlqjA04_dpk&t=6369s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در Scratch با «Make a Block» بلوک خودت را می‌ساختی. در C همین کار را با **تعریف تابع** (function definition) می‌کنی. توابع کد را کوتاه‌تر، خواناتر و قابل‌استفادهٔ دوباره می‌کنند.

## اولین تابع خودت

درس‌نامه می‌گوید راهنمایی بیشتر بعداً می‌آید، اما شکل یک تابع ساده این است:

```c
void meow(void)
{
    printf("meow\n");
}
```

- `void` اول یعنی تابع **هیچ مقداری برنمی‌گرداند**.
- `(void)` یعنی **هیچ ورودی‌ای** به تابع داده نمی‌شود.

## استفاده در main: انتزاع

```c
// Abstraction

#include <stdio.h>

void meow(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        meow();
    }
}

// Meow once
void meow(void)
{
    printf("meow\n");
}
```

- تابع با `meow()` صدا زده می‌شود.
- تعریف کامل `meow` پایین فایل است. پس بالای فایل یک **پیش‌نمونه** (prototype) آمده: `void meow(void);`.
- **از سخنرانی:** کامپایلر کد را از بالا به پایین می‌خواند. بدون پیش‌نمونه، وقتی به `meow()` در `main` می‌رسد هنوز آن را نمی‌شناسد.

## پارامتر

```c
// Abstraction with parameterization

#include <stdio.h>

void meow(int n);

int main(void)
{
    meow(3);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- پیش‌نمونه حالا `void meow(int n)` است؛ یعنی `meow` یک `int` به‌عنوان ورودی می‌گیرد.
- `meow(3)` سه بار میو می‌کند. این همان «meow n times» هفتهٔ ۰ است.

## حوزهٔ متغیر

```c
// Demonstrates scope

#include <stdio.h>

void meow(int n);

int main(void)
{
    int n = 3;
    meow(n);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- `n` داخل `main` تعریف شده، پس فقط در **حوزهٔ** (scope) `main` وجود دارد.
- `meow` به `n` اصلی دسترسی ندارد. یک **کپی** از `n` به `meow` داده می‌شود و `meow` با کپی خودش کار می‌کند.

## ورودی کاربر

```c
// User input

#include <cs50.h>
#include <stdio.h>

void meow(int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number: ");
    }
    while (n < 1);
    meow(n);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- `get_int` عدد را از کاربر می‌گیرد و `n` به `meow` داده می‌شود.
- حلقهٔ `do while` تا وقتی `n < 1` است دوباره می‌پرسد.

## مقدار بازگشتی

```c
// Return value

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);
void meow(int n);

int main(void)
{
    int n = get_positive_int();
    meow(n);
}

// Get number of meows
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Number: ");
    }
    while (n < 1);
    return n;
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- تابع تازهٔ `get_positive_int` تا وقتی `n < 1` است عدد می‌خواهد.
- پس از گرفتن عدد مثبت، با `return n` آن را به `main` **برمی‌گرداند**.
- `int` اول نام تابع یعنی این تابع یک `int` برمی‌گرداند.

## مقایسه با هفتهٔ ۰

| مفهوم | Scratch | C |
| --- | --- | --- |
| تعریف بلوک یا تابع | `define meow` | `void meow(void) { ... }` |
| ورودی | `meow (n) times` | `void meow(int n)` |
| مقدار بازگشتی | بلوک گرد `answer` | `return n;` |

> **تألیفی:** این جدول برای پیوند دادن دو هفته ساخته شده است.

## اشتباه‌های رایج

- فراموش کردن پیش‌نمونه، وقتی تابع پایین `main` تعریف شده است.
- نبودن `;` در پایان پیش‌نمونه، یا گذاشتن `;` بعد از سطر اول تعریف تابع.
- انتظار این‌که تغییر `n` در یک تابع، `n` تابع دیگر را هم عوض کند.

## جمع‌بندی

- `void` در جای نوع بازگشتی یعنی «چیزی برنمی‌گرداند»؛ در پرانتز یعنی «ورودی ندارد».
- پیش‌نمونه، پارامتر، حوزه و `return` چهار مفهوم کلیدی توابع‌اند.

## پیوندها

- قبلی: [حلقه‌ها و meow.c](/kb/d/w01-n15)
- بعدی: [درستی، طراحی و سبک](/kb/d/w01-n17)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
