---
id: w01-n15
type: note
title: حلقه‌ها و meow.c (Loops and meow.c)
title_fa: حلقه‌ها و meow.c
title_en: Loops and meow.c
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Loops and meow.c
official_anchor: loops-and-meowc
source_url: https://cs50.harvard.edu/x/notes/1/#loops-and-meowc
source_refs:
- src-notes-1#loops-and-meowc
- src-short-loops
- src-srt-1
concept_ids:
- w01-c-while-loop
- w01-c-for-loop
- w01-c-zero-indexing
- w01-c-infinite-loop
- w01-c-do-while
- w01-c-input-validation
- w01-c-break-continue
prev: w01-n14
next: w01-n16
order: 15
video:
  youtube_id: SlqjA04_dpk
  start: '1:22:33'
  start_seconds: 4953
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=4953s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'meow'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# حلقه‌ها و meow.c

> **منبع رسمی:** بخش «Loops and meow.c» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#loops-and-meowc). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۲:۳۳ تا حدود ۱:۴۶:۰۹](https://www.youtube.com/watch?v=SlqjA04_dpk&t=4953s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حلقه‌ها همان `repeat` و `forever` در Scratch هستند. این بخش طولانی است، چون C چند نوع حلقه دارد و هر کدام کاربرد خودش را دارد.

## از تکرار به حلقه

```c
// Opportunity for better design

#include <stdio.h>

int main(void)
{
    printf("meow\n");
    printf("meow\n");
    printf("meow\n");
}
```

درس‌نامه می‌گوید این کد کار می‌کند، اما **طراحی** بهتری ممکن است: یک خط سه بار تکرار شده است.

## حلقهٔ while با شمارش معکوس

```c
// Better design

#include <stdio.h>

int main(void)
{
    int i = 3;
    while (i > 0)
    {
        printf("meow\n");
        i--;
    }
}
```

- متغیر `i` با `3` شروع می‌شود.
- حلقهٔ `while` تا وقتی `i > 0` درست است اجرا می‌شود و هر بار `i--` یکی از `i` کم می‌کند.

## شمارش رو به بالا

```c
// Print values of i

#include <stdio.h>

int main(void)
{
    int i = 1;
    while (i <= 3)
    {
        printf("meow\n");
        i++;
    }
}
```

- شمارنده از `1` شروع می‌شود و هر بار یکی زیاد می‌شود. وقتی از `3` بیشتر شد، حلقه متوقف می‌شود.

## شمارش از صفر

در علوم کامپیوتر معمولاً **از صفر می‌شماریم**. درس‌نامه نسخهٔ بهتر را این‌طور می‌نویسد:

```c
// Better design

#include <stdio.h>

int main(void)
{
    int i = 0;
    while (i < 3)
    {
        printf("meow\n");
        i++;
    }
}
```

## حلقهٔ for

```c
// Better design

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }
}
```

حلقهٔ `for` سه بخش دارد که با `;` جدا می‌شوند:

1. `int i = 0`: شمارنده از صفر شروع می‌شود.
2. `i < 3`: شرطی که پیش از هر دور بررسی می‌شود.
3. `i++`: بعد از هر دور، شمارنده یکی زیاد می‌شود.

## حلقهٔ بی‌پایان

```c
// Infinite loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    while (true)
    {
        printf("meow\n");
    }
}
```

- `true` همیشه درست است، پس حلقه هرگز تمام نمی‌شود و کنترل ترمینال از دستت می‌رود.
- با فشردن **control-C** برنامه متوقف می‌شود؛ این کلید یک سیگنال SIGINT برای پایان دادن به برنامه می‌فرستد.

## پرسیدن تعداد از کاربر

```c
// Prompts user for n.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("What's n? ");

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- کاربر `n` را تعیین می‌کند و برنامه `n` بار میو می‌کند.

## اگر کاربر عدد منفی بدهد؟

```c
// Prompts user again if need be. (Poor design.)

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("What's n? ");
    if (n < 0)
    {
        n = get_int("What's n? ");
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

درس‌نامه این را **طراحی ضعیف** می‌داند: فقط یک بار دوباره می‌پرسد. اگر کاربر چند بار پشت سر هم عدد منفی بدهد چه؟

## حلقه با continue و break

```c
// Uses a loop with continue/break.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    while (true)
    {
        n = get_int("What's n? ");
        if (n < 0)
        {
            continue;
        }
        else
        {
            break;
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- `continue` حلقه را به دور بعد می‌فرستد و `break` از حلقه بیرون می‌پرد.
- حلقه آن‌قدر تکرار می‌شود تا `n` بزرگ‌تر یا مساوی صفر شود.

## فقط با break

```c
// Uses a loop with just break.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    while (true)
    {
        n = get_int("What's n? ");
        if (n >= 0)
        {
            break;
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- همان منطق با خط‌های کمتر.

## حلقهٔ do while

```c
// Uses a do-while loop instead.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("What's n? ");
    }
    while (n < 0);

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- بخش `do` **دست‌کم یک بار** اجرا می‌شود، سپس تا وقتی `n < 0` است تکرار می‌شود.
- **از ویدئوی کوتاه Loops:** کاربرد رایج `do while` همین است: گرفتن ورودی از کاربر، چون دست‌کم یک بار باید پرسید.

درس‌نامه در پایان می‌گوید: با نگاه دقیق می‌شود بخش «میو کردن» را در یک تابع **انتزاع** (abstract away) کرد. این کار را در [توابع](/kb/d/w01-n16) می‌بینی.

## کدام حلقه، کی؟ (از ویدئوی کوتاه Loops)

| حلقه | کاربرد معمول |
| --- | --- |
| `while` | تعداد تکرار نامعلوم است و شاید اصلاً اجرا نشود |
| `do while` | تعداد نامعلوم، اما دست‌کم یک بار باید اجرا شود |
| `for` | تعداد تکرار مشخص است (حتی اگر هنگام کامپایل معلوم نباشد) |

این سه حلقه جایگزین‌پذیرند، اما هر کدام برای کاری خواناتر است.

## اشتباه‌های رایج

- فراموش کردن `i++` در `while`: حلقه بی‌پایان می‌شود.
- `<=` به‌جای `<` وقتی از صفر می‌شماری: یک دور اضافه.
- فراموش کردن `;` بعد از `while (...)` در `do while`.

## جمع‌بندی

- `while`، `for` و `do while` سه شکل حلقه‌اند.
- از صفر بشمار؛ برای ورودی تکراری از `do while` استفاده کن.

## پیوندها

- قبلی: [agree.c: نویسه‌ها و عملگرهای منطقی](/kb/d/w01-n14)
- بعدی: [توابع: انتزاع، پارامتر، حوزه و مقدار بازگشتی](/kb/d/w01-n16)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
