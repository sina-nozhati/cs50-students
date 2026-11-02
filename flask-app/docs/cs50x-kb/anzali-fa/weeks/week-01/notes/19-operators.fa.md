---
id: w01-n19
type: note
title: عملگرها، سرریز، بریدن و عدم دقت اعشار (Operators)
title_fa: عملگرها، سرریز، بریدن و عدم دقت اعشار
title_en: Operators
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Operators
official_anchor: operators
source_url: https://cs50.harvard.edu/x/notes/1/#operators
source_refs:
- src-notes-1#operators
- src-transcript-1
- src-short-operators
- src-anzali-authored-1
- src-srt-1
concept_ids:
- w01-c-arithmetic-operators
- w01-c-integer-overflow
- w01-c-truncation
- w01-c-type-casting
- w01-c-floating-point-imprecision
prev: w01-n18
next: w01-summary
order: 19
video:
  youtube_id: SlqjA04_dpk
  start: '2:13:07'
  start_seconds: 7987
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=7987s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'calculator'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# عملگرها، سرریز، بریدن و عدم دقت اعشار

> **منبع رسمی:** بخش «Operators» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#operators). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۱۳:۰۷](https://www.youtube.com/watch?v=SlqjA04_dpk&t=7987s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

کامپیوتر حساب می‌کند، اما با حافظهٔ محدود. این بخش نشان می‌دهد این محدودیت چطور به **سرریز** (overflow)، **بریدن** (truncation) و **عدم دقت اعشار** (floating-point imprecision) می‌رسد.

## عملگرهای حسابی

| عملگر | کار |
| --- | --- |
| `+` | جمع |
| `-` | تفریق |
| `*` | ضرب |
| `/` | تقسیم |
| `%` | باقی‌مانده |

درس‌نامه می‌گوید در این دوره از همهٔ این عملگرها استفاده می‌کنیم.

## ماشین‌حساب

با `code calculator.c` شروع کن:

```c
// Addition with int

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Add numbers
    int z = x + y;

    // Perform addition
    printf("%i\n", z);
}
```

- متغیر سوم `z` حاصل جمع را نگه می‌دارد و با `%i` چاپ می‌شود.

```c
// Addition with int, without third variable

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Perform addition
    printf("%i\n", x + y);
}
```

- این نسخه بدون متغیر سوم است؛ جمع مستقیماً داخل `printf` انجام می‌شود.

```c
// Doubles a number

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Double it
    printf("%i\n", x * 2);
}
```

- عملگر `*` ورودی را دو برابر می‌کند.

## سرریز عدد صحیح

```c
// Overflow 

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int dollars = 1;
    while (true)
    {
        char c = get_char("Here's $%i. Double it and give to next person? ", dollars);
        if (c == 'y')
        {
            dollars *= 2;
        }
        else
        {
            break;
        }
    }
    printf("Here's $%i.\n", dollars);
}
```

- برنامه مقدار `dollars` را پشت سر هم دو برابر می‌کند.
- سرانجام عدد از بیشینهٔ `int` بیشتر می‌شود و **سرریز** می‌کند: مقدار به یک عدد منفی یا صفر می‌چرخد.
- طبق درس‌نامه، بیشینهٔ یک `int` علامت‌دار معمولاً `2147483647` است و یک `int` بی‌علامت (unsigned) تا `4294967295` می‌رسد.
- تعداد بیت‌ها بازهٔ مقدارها را تعیین می‌کند.
- C کنترل زیادی بر حافظه می‌دهد، اما برنامه‌نویس باید مراقب دام‌های آن باشد. این خطاها می‌توانند پیامدهای فاجعه‌بار در دنیای واقعی داشته باشند.

**از سخنرانی:** دو مثال واقعی آمد: یک هشدار ایمنی برای هواپیماهای Boeing که پس از ۲۴۸ روز روشن ماندن پیوسته ممکن بود برقشان قطع شود، و مشکل Y2K که سال را با دو رقم ذخیره می‌کرد.

## راه‌حل جزئی: long

```c
// long

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long dollars = 1;
    while (true)
    {
        char c = get_char("Here's $%li. Double it and give to next person? ", dollars);
        if (c == 'y')
        {
            dollars *= 2;
        }
        else
        {
            break;
        }
    }
    printf("Here's $%li.\n", dollars);
}
```

- نوع به `long` و کد قالب به `%li` تغییر کرده است.
- `long` مقدارهای بسیار بزرگ‌تری نگه می‌دارد. سرریز را **به تأخیر می‌اندازد**، اما از بین نمی‌برد.

## بریدن در تقسیم صحیح

```c
// Division with ints, demonstrating truncation

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Divide x by y
    printf("%i\n", x / y);
}
```

- تقسیم دو `int` نتیجهٔ صحیح می‌دهد و بخش اعشاری **دور ریخته می‌شود**. مثال درس‌نامه: `7 / 2` می‌شود `3`، نه `3.5`.

## تبدیل نوع

```c
// Casting

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Divide x by y
    printf("%f\n", (float) x / y);
}
```

- `(float) x` پیش از تقسیم، `x` را به `float` **تبدیل** (cast) می‌کند. حالا نتیجه اعشاری است و بریده نمی‌شود.

## عدم دقت اعشار

```c
// Floats

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    float x = get_float("What's x? ");

    // Prompt user for y
    float y = get_float("What's y? ");

    // Divide x by y
    printf("%.50f\n", x / y);
}
```

- `get_float` ورودی اعشاری می‌گیرد و `%.50f` تا ۵۰ رقم بعد از ممیز چاپ می‌کند.
- رقم‌های غیرمنتظره نشان می‌دهند که کامپیوتر هر عدد اعشاری را دقیق نمی‌تواند نمایش دهد؛ دلیلش محدودیت نمایش دودویی است.
- هنگام کدنویسی به نوع متغیرها دقت کن تا دچار این مشکل‌ها نشوی.

## نکته‌های ویدئوی کوتاه Operators

- `%` باقی‌ماندهٔ تقسیم است: `13 % 4` برابر `1` است.

## اشتباه‌های رایج

- انتظار `3.5` از `7 / 2` با متغیرهای `int`.
- تغییر نوع به `long` اما فراموش کردن `%li` در `printf`.
- مقایسهٔ مستقیم دو عدد اعشاری با `==` و انتظار برابری دقیق (**تألیفی**).

## جمع‌بندی

- هر نوع بازهٔ محدودی دارد؛ عبور از آن سرریز است.
- تقسیم صحیح بخش اعشاری را می‌بُرد؛ با تبدیل نوع از آن جلوگیری کن.
- اعداد اعشاری دقت محدود دارند.

## پیوندها

- قبلی: [Mario: حلقه‌های تودرتو، ثابت و تابع کمکی](/kb/d/w01-n18)
- بعدی: [خلاصهٔ هفته](/kb/d/w01-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
