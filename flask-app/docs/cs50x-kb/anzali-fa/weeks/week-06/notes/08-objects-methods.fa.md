---
id: w06-n08
type: note
title: 'شیء و متد: lower و capitalize (Object-Oriented Programming)'
title_fa: 'شیء و متد: lower و capitalize'
title_en: Object-Oriented Programming
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Object-Oriented Programming
official_anchor: object-oriented-programming
source_url: https://cs50.harvard.edu/x/2026/notes/6/#object-oriented-programming
source_refs:
- src-notes-6#object-oriented-programming
- src-transcript-6
- src-python-docs
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-object-method
- w06-c-string-methods
- w06-c-method-returns-new
prev: w06-n07
next: w06-n09
order: 8
video:
  youtube_id: Rl0ludWTLxs
  start: '1:04:07'
  start_seconds: 3847
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=3847s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'you are using what are called methods'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# شیء و متد: lower و capitalize

> **منبع رسمی:** بخش «Object-Oriented Programming» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#object-oriented-programming). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۴:۰۷ تا حدود ۱:۱۲:۰۲](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=3847s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در پایتون تقریباً هر مقداری یک **شیء** است و تابع‌هایی همراه خودش دارد. اگر بدانی متد چیست و چه چیزی برمی‌گرداند، کارهایی مثل یکسان‌سازی ورودی کاربر (`lower`) یا بزرگ کردن حرف اول (`capitalize`) را در یک سطر انجام می‌دهی.

## برنامه‌نویسی شیءگرا

- ممکن است نوعی از مقدارها نه‌تنها **ویژگی‌ها** (properties یا attributes) درون خود داشته باشند، بلکه تابع هم داشته باشند. در پایتون به این مقدارها **شیء** (object) می‌گویند.
- در C می‌توانستی یک `struct` بسازی و چند متغیر را در یک نوع داده که خودت ساخته بودی کنار هم بگذاری. در پایتون این کار ممکن است و می‌شود **تابع** را هم در نوع دادهٔ خودساخته گذاشت. وقتی تابعی متعلق به یک شیء مشخص باشد، به آن **متد** (method) می‌گویند.
- مثلاً `str` در پایتون متدهای داخلی دارد. پس می‌توانی کدت را این‌طور تغییر دهی:

```python
# Logical operators, using lists

# Prompt user to agree
s = input("Do you agree? ").lower()

# Check whether agreed
if s in ["y", "yes"]:
    print("Agreed.")
else:
    print("Not agreed.")
```

- `s.lower()` با متد داخلی `lower` رشته، ورودی را **یکسان‌سازی** (normalize) می‌کند؛ پس `Y`، `y`، `YES` و `Yes` همه پذیرفته می‌شوند.
- به یاد داری چگونه در C یک رشته را کپی می‌کردیم:

```c
// Capitalizes a copy of a string without memory errors

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    // Copy string into memory
    strcpy(t, s);

    // Capitalize copy
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Free memory
    free(t);
    return 0;
}
```

- همین را در پایتون این‌طور پیاده می‌کنیم:

```python
# Capitalizes a copy of a string

# Get a string
s = input("s: ")

# Capitalize copy of string
t = s.capitalize()

# Print strings
print(f"s: {s}")
print(f"t: {t}")
```

- این برنامه چقدر کوتاه‌تر از نسخهٔ C است. برای ورودی `sina` خروجی دو سطر است: `s: sina` و `t: Sina` (اجراشده روی جعبهٔ ساخت).

> [!IMPORTANT]
> **استنتاجی: متد رشته، رشتهٔ تازه برمی‌گرداند**
> رشته‌ها در پایتون **تغییرناپذیر**اند. `s.capitalize()` و `s.lower()` خودِ `s` را عوض نمی‌کنند؛ رشتهٔ تازه‌ای برمی‌گردانند. برای همین در `copy.py` مقدار `s` پس از ساختن `t` هنوز `sina` است. اگر فقط بنویسی `s.lower()` و نتیجه را در متغیری نگذاری، آن نتیجه از دست می‌رود (بر پایهٔ مستندات پایتون).

- در این درس فقط سطح پایتون را می‌خراشیم؛ برای همین [مستندات پایتون](https://docs.python.org) هنگام ادامهٔ کار اهمیت ویژه‌ای دارد. دربارهٔ متدهای رشته می‌توانی در [بخش string methods مستندات](https://docs.python.org/3/library/stdtypes.html#string-methods) بیشتر بخوانی.

> [!NOTE]
> **از سخنرانی: متد یعنی تابع درون شیء**
> David گفت متدها همان تابع‌هایی هستند که درون شیءها قرار دارند و با نقطه صدا زده می‌شوند، مثل `s.lower()`.

## اشتباه‌های رایج

- نوشتن `s.lower` بدون پرانتز؛ این متد را **صدا نمی‌زند** و خودِ شیء متد را برمی‌گرداند.
- انتظار اینکه `s.upper()` به‌تنهایی `s` را تغییر دهد.
- اشتباه گرفتن `capitalize` (فقط حرف اول بزرگ، بقیه کوچک) با `upper` (همهٔ حرف‌ها بزرگ).

## جمع‌بندی

- شیء = داده + تابع؛ تابعِ متعلق به شیء = متد.
- `str` متدهایی مثل `lower`، `upper` و `capitalize` دارد.
- متدهای رشته رشتهٔ تازه برمی‌گردانند؛ رشتهٔ اصلی تغییر نمی‌کند.

## پیوندها

- قبلی: [شرط‌ها، تورفتگی و or](/kb/d/w06-n07)
- بعدی: [حلقه‌ها و تابع‌سازی (main)](/kb/d/w06-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
