---
id: w06-n11
type: note
title: 'ماریو در پایتون: while True و end (Mario)'
title_fa: 'ماریو در پایتون: while True و end'
title_en: Mario
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Mario
official_anchor: mario
source_url: https://cs50.harvard.edu/x/2026/notes/6/#mario
source_refs:
- src-notes-6#mario
- src-transcript-6
- src-python-docs
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-while-true-break
- w06-c-print-end
- w06-c-string-repeat
- w06-c-nested-loops-py
prev: w06-n10
next: w06-n12
order: 11
video:
  youtube_id: Rl0ludWTLxs
  start: '1:41:52'
  start_seconds: 6112
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=6112s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'around with Mario in a few different forms'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ماریو در پایتون: while True و end

> **منبع رسمی:** بخش «Mario» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#mario). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۱:۵۲ تا حدود ۱:۵۰:۵۰](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=6112s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

دیوارها و هرم‌های Mario در هفتهٔ ۱ با حلقه‌های تودرتو ساخته شدند. در پایتون همان ایده‌ها را با `while True`، پارامتر `end` در `print` و ضرب رشته در عدد می‌بینی. این یادداشت فقط نمونه‌های **خود سخنرانی** را توضیح می‌دهد؛ حل Sentimental Mario با خودت است.

## Mario

- چند هفته پیش چالش ساختن سه بلوک روی هم، مثل Mario، را به یاد داری.
- در پایتون می‌شود چیزی شبیه آن را این‌طور پیاده کرد:

```python
# Prints a column of 3 bricks with a loop

for i in range(3):
    print("#")
```

- این برنامه ستونی از سه آجر چاپ می‌کند.
- در C حلقهٔ `do-while` را داشتیم. اما پایتون حلقهٔ `do-while` ندارد و قرارداد این است که از حلقهٔ `while` استفاده کنی. در فایلی به نام `mario.py` می‌توانی بنویسی:

```python
# Prints a column of n bricks with a loop

from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0:
        break

for i in range(n):
    print("#")
```

- حلقهٔ `while` برای گرفتن ارتفاع به کار رفته است. به محض واردشدن ارتفاعی بزرگ‌تر از صفر، حلقه با `break` شکسته می‌شود.

> [!TIP]
> **تألیفی: الگوی while True و break**
> این الگو همان کار `do-while` را می‌کند: بدنهٔ حلقه **دست‌کم یک بار** اجرا می‌شود و شرطِ ماندن یا رفتن در پایان بدنه بررسی می‌شود. توجه کن که `n` پس از حلقه هم در دسترس است، چون در پایتون حلقه دامنهٔ (scope) جدایی برای متغیرها نمی‌سازد (استنتاجی، بر پایهٔ مستندات پایتون).

> [!NOTE]
> **یادداشت**
> `get_int` کتابخانهٔ CS50 اگر ورودی عدد صحیح نباشد (مثلاً `foo`) خودش دوباره می‌پرسد؛ حلقهٔ `while` فقط شرط «بزرگ‌تر از صفر» را بررسی می‌کند. با ورودی‌های `0`، `foo` و `3` برنامه دو بار دوباره می‌پرسد و سپس سه `#` چاپ می‌کند (اجراشده روی جعبهٔ ساخت با یک نسخهٔ جایگزین ساده از کتابخانهٔ CS50؛ d110).

- حالا چهار بلوک علامت سؤال افقی را در نظر بگیر. در پایتون می‌شود کد را این‌طور تغییر داد:

```python
# Prints a row of 4 question marks with a loop

for i in range(4):
    print("?", end="")
print()
```

- می‌توانی رفتار `print` را تغییر دهی تا روی همان سطرِ چاپ قبلی بماند.
- با همان روحیهٔ نسخه‌های قبلی، می‌شود این برنامه را ساده‌تر کرد:

```python
# Prints a row of 4 question marks without a loop

print("?" * 4)
```

- با `*` رشته را **ضرب** می‌کنیم تا `4` بار تکرار شود.
- یک بلوک بزرگ از آجرها چطور؟ برای پیاده‌سازی آن:

```python
# Prints a 3-by-3 grid of bricks with loops

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```

- یک حلقهٔ `for` درون دیگری قرار دارد. دستور `print()` در پایان هر ردیف آجر یک سطر تازه اضافه می‌کند.
- دربارهٔ تابع `print` می‌توانی در [مستندات پایتون](https://docs.python.org/3/library/functions.html#print) بیشتر بخوانی.

> [!WARNING]
> **صداقت علمی**
> Sentimental Mario از تو می‌خواهد برنامهٔ Mario هفتهٔ ۱ را به پایتون **ترجمه** کنی. این صفحه کد آن برنامه را نمی‌دهد. از این نمونه‌ها برای فهم `while True`، `end=""`، ضرب رشته و حلقهٔ تودرتو استفاده کن و راه‌حل خودت را بنویس.

## اشتباه‌های رایج

- جست‌وجوی `do while` در پایتون؛ وجود ندارد.
- فراموش کردن `print()` پس از حلقهٔ درونی در `mario4.py`؛ همهٔ ۹ آجر در یک سطر چاپ می‌شوند.
- نوشتن `4 * "?"` و تعجب از اینکه کار می‌کند؛ ضرب رشته در عدد از هر دو طرف کار می‌کند، اما `"?" * "4"` خطای `TypeError` می‌دهد.

## جمع‌بندی

- `while True:` همراه با `break` جای `do-while` را می‌گیرد.
- `print(..., end="")` سطر را ادامه می‌دهد؛ `print()` خالی سطر را تمام می‌کند.
- `"?" * 4` رشته را تکرار می‌کند.

## پیوندها

- قبلی: [تقسیم، ناپایداری اعشاری و استثناها](/kb/d/w06-n10)
- بعدی: [فهرست‌ها (list)، sum و len](/kb/d/w06-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
