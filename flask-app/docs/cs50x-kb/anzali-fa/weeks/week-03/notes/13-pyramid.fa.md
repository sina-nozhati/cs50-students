---
id: w03-n13
type: note
title: 'هرم ماریو: تکرار در برابر بازگشت (Recursion: iteration.c and recursion.c)'
title_fa: 'هرم ماریو: تکرار در برابر بازگشت'
title_en: 'Recursion: iteration.c and recursion.c'
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Recursion
official_anchor: recursion
source_url: https://cs50.harvard.edu/x/2026/notes/3/#recursion
source_refs:
- src-notes-3#recursion
- src-transcript-3
- src-short-call-stacks
- src-section-3
- src-section-3-transcript
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-iteration-vs-recursion
prev: w03-n12
next: w03-n14
order: 13
video:
  youtube_id: 6Svu_ae5ebk
  start: '1:36:05'
  start_seconds: 5765
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=5765s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'iteration.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# هرم ماریو: تکرار در برابر بازگشت

> **منبع رسمی:** بخش «Recursion» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#recursion). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۳۶:۰۵ تا حدود ۱:۴۶:۰۹](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=5765s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هرم ماریو را از هفتهٔ ۱ می‌شناسی. حالا همان هرم را دو جور می‌سازیم: یک بار با حلقه (**تکرار**، `iteration`) و یک بار با **بازگشت**. مقایسهٔ این دو بهترین راه برای «فهمیدنِ» بازگشت است.

## هرم به زبان بازگشت

به یاد بیاور که در هفتهٔ ۱ می‌خواستیم چنین ساختاری بسازیم:

```text
#
##
###
####
```

- **از سخنرانی:** هرمِ ارتفاع ۴ چیست؟ هرمِ ارتفاع ۳ به‌اضافهٔ یک ردیف دیگر. هرمِ ارتفاع ۳؟ هرمِ ارتفاع ۲ به‌اضافهٔ یک ردیف. و هرمِ ارتفاع ۱؟ فقط یک آجر. همین جملهٔ آخر **حالت پایه** است.

## iteration.c: با حلقه

در ترمینال `code iteration.c` را بزن و بنویس:

```c
// Draws a pyramid using iteration

#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    // Get height of pyramid
    int height = get_int("Height: ");

    // Draw pyramid
    draw(height);
}

void draw(int n)
{
    // Draw pyramid of height n
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

- این کد هرم را با **حلقه زدن** می‌سازد. حلقهٔ بیرونی ردیف‌ها را می‌شمارد و حلقهٔ درونی در ردیف `i` تعداد `i + 1` علامت `#` چاپ می‌کند.

## recursion.c: با بازگشت

برای پیاده‌سازی با بازگشت، `code recursion.c` را بزن و بنویس:

```c
// Draws a pyramid using recursion

#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    // Get height of pyramid
    int height = get_int("Height: ");

    // Draw pyramid
    draw(height);
}

void draw(int n)
{
    // If nothing to draw
    if (n <= 0)
    {
        return;
    }

    // Draw pyramid of height n - 1
    draw(n - 1);

    // Draw one more row of width n
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

- حالت پایه تضمین می‌کند کد تا ابد اجرا نشود. خط `if (n <= 0)` بازگشت را پایان می‌دهد، چون مسئله حل شده است.
- هر بار که `draw` خودش را صدا می‌زند، این کار را با `n-1` انجام می‌دهد. سرانجام `n-1` برابر `0` می‌شود، تابع `draw` برمی‌گردد و برنامه تمام می‌شود.

> [!IMPORTANT]
> **مهم**
> ترتیب مهم است: `draw(n - 1)` **قبل از** چاپ ردیف آمده است. اول کل هرمِ کوچک‌تر کشیده می‌شود و بعد ردیفِ پهن‌تر زیر آن. برای همین ردیف‌ها از کوتاه به بلند چاپ می‌شوند.

## ردگیری draw(3) (تألیفی)

- `draw(3)` صدا می‌زند `draw(2)` و منتظر می‌ماند.
- `draw(2)` صدا می‌زند `draw(1)` و منتظر می‌ماند.
- `draw(1)` صدا می‌زند `draw(0)`؛ چون `0 <= 0`، بلافاصله برمی‌گردد.
- حالا `draw(1)` یک `#` چاپ می‌کند، بعد `draw(2)` دو تا و در آخر `draw(3)` سه تا.

> [!TIP]
> **راهنما**
> **از ویدئوی کوتاه Call Stacks:** هر کدام از این فراخوانی‌ها قاب خودش را روی پشتهٔ فراخوانی دارد؛ `draw(0)` بالای پشته است و اولین قابی است که برداشته می‌شود.

## اشتباه‌های رایج

- جابه‌جا کردن `draw(n - 1)` با حلقهٔ چاپ؛ هرم وارونه می‌شود.
- نوشتن `if (n == 0)` و صدا زدن با عدد منفی؛ حالت پایه هرگز رخ نمی‌دهد. به همین دلیل درس‌نامه `n <= 0` نوشته است.
- فراموش کردن `return` در حالت پایه.

## جمع‌بندی

- هر کار تکراری را معمولاً می‌شود هم با حلقه نوشت هم با بازگشت. **از جلسهٔ حل تمرین:** Kelly هم همین را گفت.
- در بازگشت، مسئله را به «نسخهٔ کوچک‌تر به‌اضافهٔ یک گام» بشکن.

## پیوندها

- قبلی: [بازگشت: حالت پایه و حالت بازگشتی](/kb/d/w03-n12)
- بعدی: [مرتب‌سازی ادغامی](/kb/d/w03-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
