---
id: w06-n07
type: note
title: شرط‌ها، تورفتگی و or (Conditionals)
title_fa: شرط‌ها، تورفتگی و or
title_en: Conditionals
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Conditionals
official_anchor: conditionals
source_url: https://cs50.harvard.edu/x/2026/notes/6/#conditionals
source_refs:
- src-notes-6#conditionals
- src-python-docs
- src-section-6
- src-section-6-transcript
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-indentation-blocks
- w06-c-elif
- w06-c-logical-words
- w06-c-in-list
- w06-c-no-char
prev: w06-n06
next: w06-n08
order: 7
video:
  youtube_id: Rl0ludWTLxs
  start: '49:27'
  start_seconds: 2967
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=2967s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'single line of code inside of a conditional'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# شرط‌ها، تورفتگی و or

> **منبع رسمی:** بخش «Conditionals» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#conditionals). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۹:۲۷ تا حدود ۱:۰۴:۰۷](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=2967s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در پایتون **تورفتگی** بخشی از نحو زبان است: آکولادی وجود ندارد و تنها چیزی که مشخص می‌کند کدام سطرها درون `if` هستند، فاصلهٔ ابتدای سطرهاست. این یادداشت شرط‌ها و عملگرهای منطقی را با برنامه‌های آشنای هفتهٔ ۱ مقایسه می‌کند.

## شرط‌ها

- در C احتمالاً برنامه‌ای مثل این را به یاد داری:

```c
// Conditionals, Boolean expressions, relational operators

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

- در پایتون:

```python
# Conditionals, Boolean expressions, relational operators

from cs50 import get_int

# Prompt user for integers
x = get_int("What's x? ")
y = get_int("What's y? ")

# Compare integers
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

- آکولادها دیگر نیستند و به جایشان از **تورفتگی** استفاده می‌شود. پس از شرط `if` یک **دونقطه** (`:`) می‌آید. `elif` جای `else if` را می‌گیرد. پرانتز دور شرط‌های `if` و `elif` هم دیگر لازم نیست.

> [!IMPORTANT]
> **تورفتگی یعنی معنا**
> در C تورفتگی فقط برای خوانایی بود. در پایتون اگر سطری را که باید درون `if` باشد هم‌تراز `if` بنویسی، آن سطر بیرون از شرط اجرا می‌شود؛ و اگر تورفتگی‌ها ناهماهنگ باشند، مفسر خطای `IndentationError` می‌دهد. قرارداد رایج پایتون چهار فاصله برای هر سطح است (استنتاجی، بر پایهٔ مستندات پایتون).

## عملگرهای منطقی

- این کد C را در نظر بگیر:

```c
// Logical operators

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'Y' || c == 'y')
    {
        printf("Agreed.\n");
    }
    else
    {
        printf("Not agreed.\n");
    }
}
```

- در پایتون می‌شود این‌طور نوشت:

```python
# Logical operators

from cs50 import get_string

# Prompt user to agree
s = get_string("Do you agree? ")

# Check whether agreed
if s == "Y" or s == "y":
    print("Agreed.")
else:
    print("Not agreed.")
```

- دو خط عمودی `||` در C به `or` تبدیل شده است (و `&&` به `and`). بسیاری پایتون را به همین دلیل دوست دارند: خواندنش برای انسان آسان‌تر است. `char` هم در پایتون وجود ندارد؛ به جایش از `str` استفاده می‌شود.
- راه دیگر برای همین کار، استفاده از **فهرست** (list) است:

```python
# Logical operators, using lists

from cs50 import get_string

# Prompt user to agree
s = get_string("Do you agree? ")

# Check whether agreed
if s in ["y", "yes"]:
    print("Agreed.")
else:
    print("Not agreed.")
```

- چند واژهٔ کلیدی مثل `y` و `yes` را در یک `list` آورده‌ایم و `in` می‌پرسد آیا `s` یکی از آن‌هاست یا نه.

> [!NOTE]
> **یادداشت**
> درس‌نامه دو برنامهٔ متفاوت را هر دو با نام `agree2.py` پیوند داده است: یکی نسخهٔ `or` در همین بخش و دیگری نسخهٔ `lower()` در بخش شیءگرایی (d103). این صفحه هر دو را با نام‌های جدا نگه می‌دارد.

> [!TIP]
> **تألیفی: مقایسهٔ رشته‌ها**
> در هفتهٔ ۴ دیدی که در C نمی‌شود دو رشته را با `==` مقایسه کرد، چون `==` دو **نشانی** را مقایسه می‌کند و باید از `strcmp` استفاده کنی. در پایتون `s == "Y"` محتوای دو رشته را مقایسه می‌کند. این موضوع در جلسهٔ حل تمرین هم بررسی شد.

## اشتباه‌های رایج

- فراموش کردن دونقطه پس از `if`، `elif` یا `else` (خطای نحوی).
- نوشتن `else if` به جای `elif`.
- نوشتن `if s == "y" or "yes":`؛ این شرط همیشه درست است، چون `"yes"` به‌تنهایی یک رشتهٔ غیرخالی و درنتیجه درست (truthy) حساب می‌شود. شکل درست `s == "y" or s == "yes"` یا `s in ["y", "yes"]` است (استنتاجی، اجراشده روی جعبهٔ ساخت).

## جمع‌بندی

- بلوک با تورفتگی و دونقطه مشخص می‌شود؛ آکولاد و پرانتز لازم نیست.
- `elif` به جای `else if`؛ `or` و `and` به جای `||` و `&&`.
- `in` روی فهرست، عضویت را می‌پرسد.

## پیوندها

- قبلی: [ماشین‌حساب: input همیشه str برمی‌گرداند](/kb/d/w06-n06)
- بعدی: [شیء و متد: lower و capitalize](/kb/d/w06-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
