---
id: w01-n09
type: note
title: شرط‌ها در C (Conditionals)
title_fa: شرط‌ها در C
title_en: Conditionals
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Conditionals
official_anchor: conditionals
source_url: https://cs50.harvard.edu/x/notes/1/#conditionals
source_refs:
- src-notes-1#conditionals
- src-transcript-1
- src-short-conditional-statements
- src-srt-1
concept_ids:
- w01-c-if-else
- w01-c-else-if-chain
prev: w01-n08
next: w01-n10
order: 9
video:
  youtube_id: SlqjA04_dpk
  start: '56:01'
  start_seconds: 3361
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=3361s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'conditionals'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# شرط‌ها در C

> **منبع رسمی:** بخش «Conditionals» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#conditionals). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۶:۰۱ تا حدود ۱:۰۳:۲۱](https://www.youtube.com/watch?v=SlqjA04_dpk&t=3361s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

**شرط‌ها** (conditionals) دوراهی‌های برنامه‌اند: اگر چیزی درست بود این کار را بکن، وگرنه کار دیگری. در Scratch بلوک `if` و `if else` را دیدی؛ اینجا همان را در C می‌نویسیم.

## دو شاخه

```c
// Conditionals that are mutually exclusive

if (x < y)
{
    printf("x is less than y\n");
}
else
{
    printf("x is not less than y\n");
}
```

- اگر `x < y` درست باشد، خط اول چاپ می‌شود؛ وگرنه خط دوم.
- عبارت داخل پرانتز یک **عبارت بولی** (Boolean expression) است: یا درست است یا نادرست.
- بدنهٔ هر شاخه داخل آکولاد `{ }` می‌آید و با ۴ فاصله تورفتگی دارد.

## سه شاخه، با یک پرسش اضافی

```c
// Conditional that isn't necessary

if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf("x is greater than y\n");
}
else if (x == y)
{
    printf("x is equal to y\n");
}
```

درس‌نامه می‌پرسد: آیا همهٔ این خط‌ها لازم‌اند؟ اگر `x` نه کمتر از `y` باشد و نه بیشتر، **حتماً** برابر است. پس پرسیدن `x == y` یک محاسبهٔ اضافی است.

## نسخهٔ بهتر

```c
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
```

- پرسش آخر با `else` جایگزین شده است.
- این شاخه‌ها **ناسازگار** (mutually exclusive) هستند: در هر اجرا فقط یکی اجرا می‌شود.

## نکته‌های ویدئوی کوتاه Conditional Statements

- در زنجیرهٔ `if`، `else if`، `else` فقط یک شاخه اجرا می‌شود.
- اگر چند `if` پشت سر هم بنویسی (بدون `else`)، چند شاخه ممکن است با هم اجرا شوند.
- C دو ساختار شرطی دیگر هم دارد: `switch` و عملگر سه‌تایی `?:`. آن‌ها را در [یادداشت ویدئوی کوتاه](/kb/d/w01-sh-conditional-statements) می‌بینی.

## سخنرانی چه می‌گوید

**از سخنرانی:** در C علامت `==` یعنی «برابری» و `=` یعنی «انتساب». درس‌نامه این نکته را در [agree.c](/kb/d/w01-n14) هم می‌گوید.

## اشتباه‌های رایج

- نوشتن `if (x = y)` به‌جای `if (x == y)`.
- گذاشتن `;` بعد از پرانتز `if`.
- پرسیدن شرطی که پاسخش از قبل معلوم است.

## جمع‌بندی

- `if`، `else if` و `else` شاخه‌های ناسازگار می‌سازند.
- وقتی همهٔ حالت‌های دیگر رد شده‌اند، `else` کافی است.

## پیوندها

- قبلی: [لینوکس و فرمان‌های ترمینال](/kb/d/w01-n08)
- بعدی: [انواع داده در C](/kb/d/w01-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
