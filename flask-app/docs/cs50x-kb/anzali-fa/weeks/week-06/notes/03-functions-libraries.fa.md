---
id: w06-n03
type: note
title: تابع، کتابخانه، ماژول و بسته (Functions; Libraries, Modules, and Packages)
title_fa: تابع، کتابخانه، ماژول و بسته
title_en: Functions; Libraries, Modules, and Packages
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Libraries, Modules, and Packages
official_anchor: libraries-modules-and-packages
source_url: https://cs50.harvard.edu/x/2026/notes/6/#libraries-modules-and-packages
source_refs:
- src-notes-6#libraries-modules-and-packages
- src-notes-6#functions
- src-transcript-6
- src-python-docs
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-function-call-py
- w06-c-cs50-library-py
- w06-c-import
prev: w06-n02
next: w06-n04
order: 3
video:
  youtube_id: Rl0ludWTLxs
  start: '17:51'
  start_seconds: 1071
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=1071s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'a module is just a library'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# تابع، کتابخانه، ماژول و بسته

> **منبع رسمی:** بخش «Libraries, Modules, and Packages» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#libraries-modules-and-packages). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۷:۵۱ تا حدود ۱۸:۴۱](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=1071s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

بیشتر کار در پایتون **فراخوانی تابع** است: تابع‌های خود زبان، تابع‌های کتابخانه‌ها و تابع‌هایی که خودت می‌نویسی. این یادداشت نشان می‌دهد تابع را چطور صدا می‌زنی و کتابخانه را چطور وارد برنامه می‌کنی.

## تابع‌ها

- در C تابع را این‌طور دیده بودی:

```c
printf("hello, world\n");
```

- در پایتون:

```python
print("hello, world")
```

> [!TIP]
> **تألیفی: چه چیزی عوض شد؟**
> نام تابع `print` است نه `printf`، نقطه‌ویرگول نیست و `\n` هم لازم نیست. ساختار کلی (نام تابع، پرانتز، آرگومان) همان است که در C می‌شناختی.

## کتابخانه، ماژول و بسته

- مثل C، کتابخانهٔ CS50 در پایتون هم در دسترس است. این تابع‌ها به‌ویژه به کارت می‌آیند:

```text
get_float
get_int
get_string
```

- می‌توانی کل کتابخانهٔ cs50 را این‌طور وارد کنی:

```python
import cs50
```

- یا فقط تابع‌های مشخصی را از آن وارد کنی:

```python
from cs50 import get_float, get_int, get_string
```

> [!NOTE]
> **از سخنرانی: ماژول و بسته**
> David گفت «ماژول» در اصطلاح پایتون همان کتابخانه است؛ کتابخانه ممکن است همراه خود زبان بیاید یا کتابخانهٔ **شخص ثالث** باشد که جداگانه نصب می‌کنی. «بسته» (package) راه توزیع چنین کتابخانه‌هایی است.

> [!IMPORTANT]
> **تفاوت دو شکل import**
> با `import cs50` تابع را با نام کامل صدا می‌زنی: `cs50.get_int("x: ")`. با `from cs50 import get_int` می‌توانی مستقیم بنویسی `get_int("x: ")`. اگر شکل اول را بنویسی و `get_int` را بدون پیشوند صدا بزنی، پایتون خطای `NameError` می‌دهد (استنتاجی، بر پایهٔ مستندات پایتون).

## اشتباه‌های رایج

- نوشتن `#include` در پایتون؛ در پایتون `import` به کار می‌رود.
- `import cs50` و بعد صدا زدن `get_string(...)` بدون `cs50.`.

## جمع‌بندی

- فراخوانی تابع مثل C است، با نام‌ها و نحو ساده‌تر.
- کتابخانهٔ CS50 در پایتون `get_float`، `get_int` و `get_string` دارد.
- `import cs50` یا `from cs50 import ...`.

## پیوندها

- قبلی: [Speller و Filter در پایتون: چرا زبان سطح بالا](/kb/d/w06-n02)
- بعدی: [رشته‌ها، f-string و پارامترهای نام‌دار print](/kb/d/w06-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
