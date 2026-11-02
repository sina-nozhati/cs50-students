---
id: w06-n09
type: note
title: حلقه‌ها و تابع‌سازی (main) (Loops and Abstraction)
title_fa: حلقه‌ها و تابع‌سازی (main)
title_en: Loops and Abstraction
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Loops
official_anchor: loops
source_url: https://cs50.harvard.edu/x/2026/notes/6/#loops
source_refs:
- src-notes-6#loops
- src-notes-6#abstraction
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-for-range
- w06-c-while-py
- w06-c-iterate-string
- w06-c-def-function
- w06-c-main-convention
prev: w06-n08
next: w06-n10
order: 9
video:
  youtube_id: Rl0ludWTLxs
  start: '1:12:02'
  start_seconds: 4322
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=4322s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'If I wanted to me meow 3 times'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# حلقه‌ها و تابع‌سازی (main)

> **منبع رسمی:** بخش «Loops» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#loops). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۲:۰۲ تا حدود ۱:۲۷:۲۵](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=4322s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حلقه‌ها در پایتون همان ایدهٔ C هستند، اما شکل `for` عوض شده است: به جای سه بخشِ مقداردهی، شرط و افزایش، روی یک **دنباله** (مثل `range(3)` یا نویسه‌های یک رشته) پیمایش می‌کنی. سپس با تابع‌ها کد تکراری را پشت یک نام پنهان می‌کنی.

## حلقه‌ها

- حلقه‌ها در پایتون بسیار شبیه C هستند. این کد C را به یاد داری:

```c
// Demonstrates for loop

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }
}
```

- حلقهٔ `for` در پایتون:

```python
# Better design

for i in range(3):
    print("meow")
```

- از `i` هیچ‌جا صریحاً استفاده نشده است، اما پایتون مقدار `i` را خودش افزایش می‌دهد. `range(3)` مقدارهای `0`، `1` و `2` را می‌دهد.
- حلقهٔ `while` هم این‌طور نوشته می‌شود:

```python
# Demonstrates while loop

i = 0
while i < 3:
    print("meow")
    i += 1
```

- برای فهم بیشتر حلقه و پیمایش در پایتون، فایل تازه‌ای به نام `uppercase.py` بساز:

```python
# Uppercases string one character at a time

before = input("Before: ")
print("After:  ", end="")
for c in before:
    print(c.upper(), end="")
print()
```

- `end=` پارامتری به `print` می‌دهد که سطر را بدون پایان سطر ادامه می‌دهد. این کد هر بار **یک نویسه** را پردازش می‌کند؛ `for c in before` روی نویسه‌های رشته پیمایش می‌کند و `print()` در پایان، سطر را تمام می‌کند.
- با خواندن مستندات می‌فهمیم پایتون متدهایی دارد که روی کل رشته اعمال می‌شوند:

```python
# Uppercases string all at once

before = input("Before: ")
after = before.upper()
print(f"After:  {after}")
```

- اینجا `.upper` روی **کل رشته** اعمال شده است.

> [!TIP]
> **تألیفی: range را دقیق بخوان**
> `range(n)` از `0` شروع می‌شود و **پیش از** `n` می‌ایستد. `range(1, 4)` مقدارهای `1، 2، 3` را می‌دهد و `range(3, 0, -1)` مقدارهای `3، 2، 1` را. پارامتر سوم گام است (اجراشده روی جعبهٔ ساخت با پایتون ۳).

## انتزاع

- همان‌طور که پیش‌تر اشاره شد، می‌توانی کد را با تابع‌ها و **انتزاع** بخش‌هایی از آن در تابع، بهتر کنی. کد `meow.py` را این‌طور تغییر بده:

```python
# Abstraction

def main():
    for i in range(3):
        meow()

# Meow once
def meow():
    print("meow")

main()
```

- تابع `meow` دستور `print` را پنهان (انتزاع) می‌کند. تابع `main` در بالای فایل آمده و در پایین فایل صدا زده می‌شود. طبق قرارداد، انتظار می‌رود در پایتون تابع `main` بسازی.
- می‌توانی مقدار را میان تابع‌ها رد و بدل کنی:

```python
# Abstraction with parameterization

def main():
    meow(3)

# Meow some number of times
def meow(n):
    for i in range(n):
        print("meow")

main()
```

- حالا `meow` متغیری به نام `n` می‌گیرد. در `main` تابع `meow` را صدا می‌زنی و مقداری مثل `3` به آن می‌دهی؛ سپس `meow` از `n` در حلقهٔ `for` استفاده می‌کند.
- به عنوان برنامه‌نویس C به‌راحتی این کد را می‌فهمی. با اینکه برخی قراردادها فرق کرده‌اند، بلوک‌های سازنده‌ای که پیش‌تر آموختی در این زبان تازه کاملاً پیدا هستند.

> [!IMPORTANT]
> **چرا main() در پایان فایل صدا زده می‌شود؟**
> مفسر فایل را از بالا به پایین اجرا می‌کند. `def` فقط تابع را **تعریف** می‌کند و اجرایش نمی‌کند. اگر سطر آخر `main()` نباشد، برنامه هیچ خروجی‌ای نمی‌دهد؛ و اگر `main()` را **پیش از** `def meow` صدا بزنی، `meow` هنوز تعریف نشده و خطای `NameError` می‌گیری. به همین دلیل در C نمونهٔ اولیه (prototype) لازم بود اما در پایتون نیست، به شرطی که صدا زدن پس از همهٔ تعریف‌ها باشد (استنتاجی، اجراشده روی جعبهٔ ساخت).

## اشتباه‌های رایج

- انتظار اینکه `range(3)` عدد `3` را هم بدهد.
- فراموش کردن `print()` پایانی در `uppercase0.py`؛ اعلان بعدی ترمینال به همان سطر می‌چسبد.
- جا انداختن سطر `main()` در پایان فایل.

## جمع‌بندی

- `for i in range(n)` و `while شرط:`؛ `i++` نداریم، `i += 1` داریم.
- `for c in s` روی نویسه‌های رشته پیمایش می‌کند.
- طبق قرارداد `main` می‌سازیم و در پایان فایل صدایش می‌زنیم.

## پیوندها

- قبلی: [شیء و متد: lower و capitalize](/kb/d/w06-n08)
- بعدی: [تقسیم، ناپایداری اعشاری و استثناها](/kb/d/w06-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
