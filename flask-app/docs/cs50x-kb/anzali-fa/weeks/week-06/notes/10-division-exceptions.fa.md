---
id: w06-n10
type: note
title: تقسیم، ناپایداری اعشاری و استثناها (Truncation, Floating-Point Imprecision and Exceptions)
title_fa: تقسیم، ناپایداری اعشاری و استثناها
title_en: Truncation, Floating-Point Imprecision and Exceptions
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Truncation and Floating Point Imprecision
official_anchor: truncation-and-floating-point-imprecision
source_url: https://cs50.harvard.edu/x/2026/notes/6/#truncation-and-floating-point-imprecision
source_refs:
- src-notes-6#truncation-and-floating-point-imprecision
- src-notes-6#exceptions
- src-short-python
- src-python-docs
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-true-division
- w06-c-floor-division
- w06-c-float-imprecision-py
- w06-c-exception
- w06-c-try-except
prev: w06-n09
next: w06-n11
order: 10
video:
  youtube_id: Rl0ludWTLxs
  start: '1:27:25'
  start_seconds: 5245
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=5245s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'integer overflow and truncation'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# تقسیم، ناپایداری اعشاری و استثناها

> **منبع رسمی:** بخش «Truncation and Floating Point Imprecision» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#truncation-and-floating-point-imprecision). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۷:۲۵ تا حدود ۱:۴۱:۵۲](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=5245s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

دو دردسر C در پایتون شکل دیگری پیدا می‌کنند: **بریدن** (truncation) در تقسیم عدد صحیح از میان می‌رود، اما **عدم دقت ممیز شناور** همچنان هست. و به جای برگرداندن مقدارهای ویژه مثل `NULL`، پایتون **استثنا** (exception) پرتاب می‌کند که می‌شود آن را گرفت.

## بریدن و عدم دقت ممیز شناور

- به یاد داری که در C با **بریدن** روبه‌رو شدیم: تقسیم یک عدد صحیح بر دیگری ممکن بود نتیجهٔ نادقیق بدهد.
- با تغییر `calculator.py` می‌بینی پایتون با چنین تقسیمی چه می‌کند:

```python
# Division with integers, demonstration lack of truncation

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
print(z)
```

- اجرای این کد یک مقدار می‌دهد (برای `1` و `3`: `0.3333333333333333`)؛ اما اگر رقم‌های بیشتری پس از `.333333` می‌دیدی، با **عدم دقت ممیز شناور** روبه‌رو می‌شدی. بریدن رخ نمی‌دهد.
- با تغییری کوچک می‌شود این عدم دقت را آشکار کرد:

```python
# Floating-point imprecision

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
print(f"{z:.50f}")
```

- این کد عدم دقت را نشان می‌دهد. پایتون هم درست مثل C با این مشکل روبه‌روست.

> [!IMPORTANT]
> **استنتاجی: / و // در پایتون ۳**
> در پایتون ۳ عملگر `/` همیشه نتیجهٔ `float` می‌دهد، حتی برای `4 / 2` که `2.0` است. اگر تقسیم صحیح می‌خواهی، از `//` (تقسیم کف) استفاده کن: `7 // 2` برابر `3` است. دقت کن که `//` به سمت **منفی بی‌نهایت** گرد می‌کند، نه به سمت صفر مثل C: `-7 // 2` در پایتون `-4` است، اما `-7 / 2` در C با عددهای صحیح `-3` می‌شود (بر پایهٔ مستندات پایتون؛ هر دو روی جعبهٔ ساخت اجرا شدند).

> [!NOTE]
> **از ویدئوی کوتاه: پایتون ۲ و ۳**
> Doug Lloyd در ویدئوی کوتاه (ضبط‌شده در ۲۰۱۷) یادآوری می‌کند که CS50 پایتون ۳ را درس می‌دهد و هنگام جست‌وجوی مستندات باید «Python 3» را در جست‌وجو بیاوری، چون نتیجه‌های پایتون ۲ لزوماً کار نمی‌کنند (d108). رفتار `/` که بالا آمد، رفتار پایتون ۳ است.

## استثناها

- بیایید استثناهایی را که هنگام اجرای کد پایتون ممکن است رخ دهند بیشتر بررسی کنیم.
- `integer.py` را این‌طور تغییر بده:

```python
# Doesn't handle exception

# Prompt user for an integer
n = int(input("Input: "))
print("Integer")
```

- واردکردن دادهٔ نادرست (مثلاً `cat`) به خطا می‌انجامد: `int` استثنای `ValueError` پرتاب می‌کند و برنامه با پیام traceback متوقف می‌شود.
- می‌توانیم با `try` استثناهای احتمالی را **بگیریم** (catch) و رسیدگی کنیم:

```python
# Handles exception

# Prompt user for an integer
try:
    n = int(input("Input: "))
    print("Integer.")
except ValueError:
    print("Not integer.")
```

- برای ورودی `cat` خروجی `Input: Not integer.` است و برنامه بدون traceback تمام می‌شود.

> [!NOTE]
> **یادداشت**
> درس‌نامه می‌گوید این کد «بارها تلاش می‌کند داده‌ای با نوع درست بگیرد و در صورت نیاز دوباره می‌پرسد»، اما `integer2.py` حلقه ندارد و فقط **یک بار** می‌پرسد (d101). برای پرسیدن دوباره باید `try` را درون یک حلقهٔ `while True` بگذاری. همچنین `integer1.py` عبارت `Integer` را بدون نقطه و `integer2.py` عبارت `Integer.` را با نقطه چاپ می‌کند (d104).

> [!TIP]
> **تألیفی: فقط استثنای مشخص را بگیر**
> `except ValueError:` فقط خطای تبدیل را می‌گیرد. `except:` بدون نام همه‌چیز را می‌گیرد، حتی خطاهایی که نشانهٔ اشکال در کد خودت هستند، و پیدا کردنشان را سخت می‌کند.

## اشتباه‌های رایج

- انتظار `0` از `1 / 3` (رفتار C)؛ در پایتون ۳ نتیجه `0.3333333333333333` است.
- فرض اینکه `//` در عددهای منفی مثل تقسیم صحیح C رفتار می‌کند.
- فرض اینکه `integer2.py` تا گرفتن عدد صحیح دوباره می‌پرسد.

## جمع‌بندی

- در پایتون ۳، `/` بریدن ندارد و `float` می‌دهد؛ `//` تقسیم کف است.
- عدم دقت ممیز شناور همچنان هست: `f"{z:.50f}"` آن را نشان می‌دهد.
- `try`/`except ValueError` استثنای تبدیل را می‌گیرد.

## پیوندها

- قبلی: [حلقه‌ها و تابع‌سازی (main)](/kb/d/w06-n09)
- بعدی: [ماریو در پایتون: while True و end](/kb/d/w06-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
