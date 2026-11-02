---
id: w06-n06
type: note
title: 'ماشین‌حساب: input همیشه str برمی‌گرداند (Calculator)'
title_fa: 'ماشین‌حساب: input همیشه str برمی‌گرداند'
title_en: Calculator
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Calculator
official_anchor: calculator
source_url: https://cs50.harvard.edu/x/2026/notes/6/#calculator
source_refs:
- src-notes-6#calculator
- src-anzali-authored-6
- src-srt-6
concept_ids:
- w06-c-input-returns-str
- w06-c-int-conversion
prev: w06-n05
next: w06-n07
order: 6
video:
  youtube_id: Rl0ludWTLxs
  start: '40:04'
  start_seconds: 2404
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=2404s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'bring back one of our old calculators'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ماشین‌حساب: input همیشه str برمی‌گرداند

> **منبع رسمی:** بخش «Calculator» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#calculator). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۰:۰۴ تا حدود ۴۹:۲۷](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=2404s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

یکی از رایج‌ترین خطاهای تازه‌کارها در پایتون این است که فراموش می‌کنند `input` همیشه **رشته** برمی‌گرداند. این یادداشت با ماشین‌حساب هفتهٔ ۱ نشان می‌دهد این خطا چه شکلی است و چطور درستش کنی.

## ماشین‌حساب

- `calculator.c` را از هفته‌های قبل به یاد داری:

```c
// Addition with int

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("x: ");

    // Prompt user for y
    int y = get_int("y: ");

    // Perform addition
    printf("%i\n", x + y);
}
```

- همین ماشین‌حساب ساده را در پایتون می‌نویسیم. `code calculator.py` را اجرا کن و بنویس:

```python
# Addition with int [using get_int]

from cs50 import get_int

# Prompt user for x
x = get_int("x: ")

# Prompt user for y
y = get_int("y: ")

# Perform addition
print(x + y)
```

- کتابخانهٔ CS50 وارد شده، `x` و `y` از کاربر گرفته می‌شوند و در پایان نتیجه چاپ می‌شود. تابع `main` که در C داشتیم کاملاً حذف شده است. می‌شود از `main` استفاده کرد، اما الزامی نیست.
- می‌شود «چرخ‌های کمکی» کتابخانهٔ CS50 را برداشت:

```python
# Addition with int [using input]

# Prompt user for x
x = input("x: ")

# Prompt user for y
y = input("y: ")

# Perform addition
print(x + y)
```

- اجرای این کد رفتار عجیبی دارد. چرا؟ مفسر `x` و `y` را **رشته** فهمیده است. برای ورودی‌های `1` و `2`، خروجی `12` است، چون `+` دو رشته را به هم الحاق می‌کند.
- با تابع `int` درستش می‌کنی:

```python
# Addition with int [using input]

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Perform addition
print(x + y)
```

- ورودی `x` و `y` به تابع `int` داده می‌شود که آن را به عدد صحیح تبدیل می‌کند. بدون این تبدیل، نویسه‌ها به هم الحاق می‌شوند.

> [!WARNING]
> **int(input()) با ورودی غیرعددی**
> `get_int` کتابخانهٔ CS50 اگر کاربر چیزی جز عدد صحیح بنویسد، دوباره می‌پرسد. اما `int(input("x: "))` با ورودی‌ای مثل `cat` خطای `ValueError` می‌دهد و برنامه متوقف می‌شود. راه گرفتن این خطا را در یادداشت ۱۰ (استثناها) می‌بینی (d112).

> [!TIP]
> **تألیفی: عدد اعشاری**
> اگر عدد اعشاری لازم داری، از `float(input(...))` یا `get_float` استفاده کن. `int("2.5")` هم `ValueError` می‌دهد، چون رشتهٔ `"2.5"` شکل یک عدد صحیح نیست.

## اشتباه‌های رایج

- جمع زدن مستقیم دو مقدار `input()` و گرفتن `12` به جای `3`.
- این فرض که `int(input())` مثل `get_int` دوباره می‌پرسد.

## جمع‌بندی

- `input` همیشه `str` برمی‌گرداند.
- برای عدد: `int(...)` یا `float(...)`، یا `get_int` و `get_float` از کتابخانهٔ CS50.
- در پایتون `main` الزامی نیست.

## پیوندها

- قبلی: [متغیرها و نوع‌ها](/kb/d/w06-n05)
- بعدی: [شرط‌ها، تورفتگی و or](/kb/d/w06-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
