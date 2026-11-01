---
id: w06-n01
type: note
title: 'سلام پایتون: زبان تفسیری (Welcome! and Hello Python!)'
title_fa: 'سلام پایتون: زبان تفسیری'
title_en: Welcome! and Hello Python!
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Hello Python!
official_anchor: hello-python
source_url: https://cs50.harvard.edu/x/2026/notes/6/#hello-python
source_refs:
- src-notes-6#hello-python
- src-notes-6#welcome
- src-anzali-authored-6
- src-srt-6
concept_ids:
- w06-c-python-language
- w06-c-interpreted
- w06-c-run-python
- w06-c-python-syntax-basics
prev: w06-fa
next: w06-n02
order: 1
video:
  youtube_id: Rl0ludWTLxs
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# سلام پایتون: زبان تفسیری

> **منبع رسمی:** بخش «Hello Python!» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#hello-python). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۷:۰۲](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا همهٔ ایده‌های برنامه‌نویسی را با C یاد گرفتی: تابع، متغیر، شرط، حلقه، آرایه و حافظه. این هفته همان ایده‌ها را در زبان دیگری به نام **پایتون** (Python) می‌بینی. هدف اصلی این است که یاد بگیری **زبان تازه را خودت یاد بگیری**.

## خوش آمدید

- در هفته‌های قبل با بلوک‌های سازندهٔ برنامه‌نویسی در زبانی **سطح پایین** به نام C آشنا شدی.
- امروز با زبانی **سطح بالا** به نام پایتون کار می‌کنیم.
- هرچه زبان تازه‌ای یاد بگیری، توانایی‌ات برای آموختن زبان‌های بعدی بیشتر می‌شود.

## سلام پایتون

- انسان‌ها در طول دهه‌ها دیده‌اند که تصمیم‌های طراحی زبان‌های قبلی را می‌شود بهتر کرد. پایتون روی همان چیزهایی ساخته شده که در C یاد گرفتی و به تعداد بسیار زیادی کتابخانهٔ ساخت کاربران دسترسی دارد.
- C زبانی **کامپایلی** است؛ پایتون زبانی **تفسیری** (interpreted) است: لازم نیست برنامه را جداگانه کامپایل کنی، بلکه آن را در **مفسر پایتون** اجرا می‌کنی.
- برنامهٔ آشنای C:

```c
// A program that says hello to the world

#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

- همین برنامه در پایتون:

```python
# A program that says hello to the world

print("hello, world")
```

- نقطه‌ویرگول حذف شده و هیچ کتابخانه‌ای لازم نیست. برنامه را در ترمینال با `python hello.py` اجرا می‌کنی. توضیح‌ها در پایتون با `#` شروع می‌شوند، نه با `//`.
- یکی از هدف‌های این هفته این است که با **ناآشنایی کنار بیایی**: وقتی دقیقاً نمی‌دانی مسئله را چطور حل کنی یا نحوِ درست چیست، خودت در منابع بگردی (در چارچوب سیاست صداقت علمی درس).

> [!NOTE]
> **یادداشت**
> `print` در پایتون خودش در پایان یک سطر تازه چاپ می‌کند؛ برای همین در نسخهٔ پایتون `\n` نیامده است. چگونگی تغییر این رفتار را در یادداشت «رشته‌ها و پارامترهای نام‌دار» می‌بینی.

> [!TIP]
> **تألیفی: کامپایلی در برابر تفسیری**
> در C دو گام داشتی: `make hello` و بعد `./hello`. در پایتون یک گام داری: `python hello.py`. مفسر هر بار که برنامه را اجرا می‌کنی، کد را می‌خواند و اجرا می‌کند؛ پس فایل اجرایی جدایی ساخته نمی‌شود و پس از هر تغییر کافی است دوباره اجرا کنی.

## اشتباه‌های رایج

- اجرای `make hello` یا `./hello.py` برای برنامهٔ پایتون؛ راه درست در این درس `python hello.py` است.
- گذاشتن نقطه‌ویرگول یا `\n` از روی عادت C؛ نقطه‌ویرگول در پایان سطر خطا نمی‌دهد اما سبک پایتون نیست، و `\n` اضافه یک سطر خالی اضافه چاپ می‌کند.

## جمع‌بندی

- پایتون زبانی سطح بالا و تفسیری است که روی ایده‌های C ساخته شده.
- برنامه را با `python file.py` اجرا می‌کنی؛ کامپایل جداگانه لازم نیست.
- توضیح با `#`؛ `print` خودش سطر را تمام می‌کند.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w06-fa)
- بعدی: [Speller و Filter در پایتون: چرا زبان سطح بالا](/kb/d/w06-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
