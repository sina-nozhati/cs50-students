---
id: w01-n18
type: note
title: 'Mario: حلقه‌های تودرتو، ثابت و تابع کمکی (Mario)'
title_fa: 'Mario: حلقه‌های تودرتو، ثابت و تابع کمکی'
title_en: Mario
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Mario
official_anchor: mario
source_url: https://cs50.harvard.edu/x/notes/1/#mario
source_refs:
- src-notes-1#mario
- src-transcript-1
- src-short-magic-numbers
- src-pset-1
- src-anzali-authored-1
- src-srt-1
concept_ids:
- w01-c-nested-loops
- w01-c-constant
- w01-c-helper-function
prev: w01-n17
next: w01-n19
order: 18
video:
  youtube_id: SlqjA04_dpk
  start: '2:02:49'
  start_seconds: 7369
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=7369s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'Mario'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# Mario: حلقه‌های تودرتو، ثابت و تابع کمکی

> **منبع رسمی:** بخش «Mario» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#mario). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۲:۴۹ تا حدود ۲:۱۳:۰۷](https://www.youtube.com/watch?v=SlqjA04_dpk&t=7369s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

درس‌نامه می‌پرسد: «چطور با یک مسئلهٔ علوم کامپیوتر روبه‌رو شویم؟» پاسخ آن با یک مثال از بازی Super Mario Bros. است: از ساده شروع کن و گام‌به‌گام پیچیده‌اش کن. این همان روشی است که برای پرابلم‌ست‌ها به کار می‌آید.

## یک ردیف علامت سؤال

![Mario Question Marks](https://cs50.harvard.edu/x/notes/1/cs50Week1Slide123.png "Mario Question Marks")

*تصویر رسمی: چهار بلوک علامت سؤال در یک ردیف افقی.*

```c
// Prints a row of 4 question marks

#include <stdio.h>

int main(void)
{
    printf("????\n");
}
```

## همان ردیف، با حلقه

```c
// Prints a row of 4 question marks with a loop

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 4; i++)
    {
        printf("?");
    }
    printf("\n");
}
```

- حلقه چهار `?` کنار هم چاپ می‌کند و بعد از حلقه یک `\n` می‌آید.

## یک ستون آجر

![Mario Blocks](https://cs50.harvard.edu/x/notes/1/cs50Week1Slide125.png "Mario Blocks")

*تصویر رسمی: سه بلوک آجری روی هم.*

```c
// Prints a column of 3 bricks with a loop

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("#\n");
    }
}
```

- این بار `\n` داخل حلقه است، پس هر `#` در خط جدا می‌آید.

## شبکهٔ ۳ در ۳

![Mario Grid](https://cs50.harvard.edu/x/notes/1/cs50Week1Slide127.png "Mario Grid")

*تصویر رسمی: شبکه‌ای سه در سه از آجر.*

```c
// Prints a 3-by-3 grid of bricks with nested loops

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

- این **حلقه‌های تودرتو** (nested loops) هستند: یک حلقه داخل دیگری.
- حلقهٔ بیرونی ردیف را تعیین می‌کند. برای هر ردیف، حلقهٔ درونی سه ستون چاپ می‌کند. بعد از هر ردیف یک خط تازه می‌آید.

## ثابت

```c
// Prints a 3-by-3 grid of bricks with nested loops using a constant

#include <stdio.h>

int main(void)
{
    const int n = 3;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

- `const int n = 3;` یک **ثابت** (constant) می‌سازد که هرگز تغییر نمی‌کند.
- **از سخنرانی:** با `const` جلوی این را می‌گیری که خودت یا همکارت به‌اشتباه مقدار را عوض کنید.
- **از ویدئوی کوتاه Magic Numbers:** نوشتن مستقیم عددی مثل `3` در چند جای کد «عدد جادویی» است. یک نام معنادار، مثل `n` یا `#define`، کد را خواناتر و تغییرش را ساده‌تر می‌کند. جزئیات در [Magic Numbers](/kb/d/w01-sh-magic-numbers).

## تابع کمکی

```c
// Helper function

#include <stdio.h>

void print_row(int width);

int main(void)
{
    const int n = 3;
    for (int i = 0; i < n; i++)
    {
        print_row(n);
    }
}

void print_row(int width)
{
    for (int i = 0; i < width; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

- چاپ یک ردیف به تابعی به نام `print_row` سپرده شده است. این همان **انتزاع** است که در [توابع](/kb/d/w01-n16) دیدی.
- `main` حالا فقط می‌گوید «n بار یک ردیف به پهنای n چاپ کن».

## از این بخش برای پرابلم‌ست چه برمی‌داری؟

> **تألیفی:** این بخش درس‌نامه **راه‌حل** پرابلم‌ست Mario نیست. شکل هرم آنجا فرق دارد. آنچه برمی‌داری **روش** است: یک حالت ساده بنویس، اجرا کن، سپس یک گام پیچیده‌ترش کن. راهنمای مسئله را در [Mario (نسخهٔ آسان‌تر)](/kb/d/w01-ps-mario-less) ببین.

## اشتباه‌های رایج

- گذاشتن `printf("\n")` داخل حلقهٔ درونی: هر `#` در خط جدا چاپ می‌شود.
- استفاده از یک نام شمارنده (`i`) برای هر دو حلقهٔ تودرتو.

## جمع‌بندی

- مسئلهٔ بزرگ را از ساده‌ترین نسخه شروع کن.
- حلقهٔ تودرتو برای ردیف و ستون؛ `const` برای مقدار ثابت؛ تابع کمکی برای زیرمسئله.

## پیوندها

- قبلی: [درستی، طراحی و سبک](/kb/d/w01-n17)
- بعدی: [عملگرها، سرریز، بریدن و عدم دقت اعشار](/kb/d/w01-n19)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
