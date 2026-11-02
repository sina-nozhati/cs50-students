---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-fa
type: week-overview
title: هفتهٔ ۶ — پایتون (پایگاه دانش فارسی)
title_fa: هفتهٔ ۶ — پایتون
title_en: Week 6 — Python
parent: week-6
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/6/
source_refs:
- src-week-6#week-6-python
- src-notes-6#lecture-6
- src-pset-6#what-to-do
- src-pset-6#when-to-do-it
- src-pset-6#academic-honesty
- src-anzali-authored-6
- src-anzali-inference-6
children:
- w06-n01
- w06-n02
- w06-n03
- w06-n04
- w06-n05
- w06-n06
- w06-n07
- w06-n08
- w06-n09
- w06-n10
- w06-n11
- w06-n12
- w06-n13
- w06-n14
- w06-n15
- w06-summary
- w06-sec
- w06-sh-python
- w06-ps-hello
- w06-ps-mario-less
- w06-ps-mario-more
- w06-ps-cash
- w06-ps-credit
- w06-ps-readability
- w06-ps-dna
- w06-pr-bank
- w06-pr-figlet
- w06-pr-jar
- w06-pr-seven-day-average
- w06-pr-taqueria
objective_ids:
- w06-o01
- w06-o02
- w06-o03
- w06-o04
- w06-o05
- w06-o06
- w06-o07
- w06-o08
- w06-o09
- w06-o10
---

# هفتهٔ ۶ — پایتون

> **منبع رسمی:** [صفحهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/weeks/6/) و [درس‌نامهٔ هفتهٔ ۶](https://cs50.harvard.edu/x/notes/6/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

پنج هفته با C کار کردی: نوع‌ها، شرط‌ها، حلقه‌ها، آرایه‌ها، اشاره‌گرها و ساختمان‌های داده. این هفته همان بلوک‌های سازنده را در زبانی **سطح بالا** به نام **پایتون** می‌بینی. پایتون **تفسیری** است: برنامه را با `python file.py` اجرا می‌کنی و کامپایل جداگانه لازم نیست.

هفته با بازنویسی Speller و Filter در چند سطر شروع می‌شود تا ببینی زبان سطح بالا چه چیزی به تو می‌دهد و بهایش (سرعت و کنترل کمتر بر حافظه) چیست. بعد نحو پایتون را با برنامه‌های آشنا مقایسه می‌کنی: `print` و f-string، متغیر بدون اعلان نوع، `input` که همیشه رشته برمی‌گرداند، شرط با تورفتگی و `elif`، متدهای رشته، حلقهٔ `for` روی `range` یا روی یک رشته، و `main` به عنوان قرارداد. سپس می‌بینی که در پایتون ۳ تقسیم بریده نمی‌شود اما عدم دقت ممیز شناور هنوز هست، و خطاها به شکل **استثنا** می‌آیند که با `try` و `except` گرفته می‌شوند. هفته با فهرست، واژه‌نامه، `sys.argv`، `sys.exit`، کتابخانهٔ `csv` و کتابخانه‌های شخص ثالث تمام می‌شود. پیام اصلی: مهارت برنامه‌نویسی تو به یک زبان محدود نیست و حالا یاد می‌گیری چطور زبان تازه را **خودت** یاد بگیری.

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

پایتون: تابع‌ها، آرگومان‌ها، مقدار برگشتی؛ متغیرها؛ عبارت‌های بولی و شرط‌ها؛ حلقه‌ها (Python: Functions, Arguments, Return Values; Variables; Boolean Expressions, Conditionals; Loops). ماژول‌ها و بسته‌ها (Modules, Packages).

> **توجه:** صفحهٔ هفته یک ویدئوی کوتاه («Python»، Doug Lloyd) فهرست می‌کند که در سال ۲۰۱۷ ضبط شده است؛ برخی جزئیاتش با سخنرانی ۲۰۲۵ فرق دارد (d108 در `sources.json`).

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه، سخنرانی، جلسهٔ حل تمرین و پرابلم‌ست ۶ استخراج کرده است.

- **w06-o01** — فرق زبان کامپایلی و تفسیری را توضیح بدهی، برنامهٔ پایتون را با `python file.py` اجرا کنی و بهای زبان سطح بالا را بگویی.
- **w06-o02** — تابع را در پایتون صدا بزنی و کتابخانه را با `import` یا `from ... import` وارد کنی، از جمله کتابخانهٔ CS50.
- **w06-o03** — متن را با الحاق، چند آرگومان یا f-string بسازی و پارامترهای نام‌دار `sep` و `end` را درست به کار ببری.
- **w06-o04** — بدون اعلان نوع متغیر بسازی، نوع‌های پرکاربرد پایتون را بشناسی و خروجی `input` را با `int` یا `float` تبدیل کنی.
- **w06-o05** — شرط را با تورفتگی، دونقطه، `elif`، `or`، `and` و `in` بنویسی.
- **w06-o06** — شیء و متد را توضیح بدهی و بدانی متدهای رشته رشتهٔ تازه برمی‌گردانند.
- **w06-o07** — با `for`، `range`، `while`، `while True` و `break` حلقه بنویسی، روی رشته پیمایش کنی، `end` و ضرب رشته را به کار ببری و تابع و `main` تعریف کنی.
- **w06-o08** — تفاوت `/` و `//` در پایتون ۳ را بگویی، عدم دقت ممیز شناور را بشناسی و استثنای `ValueError` را با `try` و `except` بگیری.
- **w06-o09** — با فهرست، `len`، `sum`، `append`، نمایه و برش، جست‌وجوی خطی، `for ... else` و واژه‌نامه کار کنی.
- **w06-o10** — از `sys.argv` و `sys.exit` استفاده کنی، با `csv.writer` و `csv.DictWriter` در فایل بنویسی و کتابخانهٔ شخص ثالث را با `pip` نصب کنی.

## پیش‌نیازها

- هفتهٔ ۱: نوع‌ها، شرط‌ها، حلقه‌ها، `get_int`، Mario و Cash و Credit در C. ([نمای کلی هفتهٔ ۱](/kb/d/w01-fa))
- هفتهٔ ۲: آرایه، رشته، `argv` و Readability در C. ([نمای کلی هفتهٔ ۲](/kb/d/w02-fa))
- هفتهٔ ۴ و ۵: فایل، `struct`، جدول درهم‌سازی و واژه‌نامه. ([نمای کلی هفتهٔ ۵](/kb/d/w05-fa))

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: از C به پایتون
  زبان تفسیری -> python file.py -> بهای زبان سطح بالا -> import

مرحلهٔ ۲: رشته و نوع
  الحاق، ویرگول، f-string -> sep و end -> نوع بدون اعلان -> input و int

مرحلهٔ ۳: شرط، متد و حلقه
  تورفتگی و elif -> or و in -> متد رشته -> for و range -> def و main

مرحلهٔ ۴: عدد و استثنا
  / و // -> عدم دقت ممیز شناور -> ValueError -> try و except

مرحلهٔ ۵: Mario و فهرست
  while True و break -> end و ضرب رشته -> list و append -> نمایه و برش

مرحلهٔ ۶: واژه‌نامه، خط فرمان و فایل
  جست‌وجوی خطی و for-else -> dict -> sys.argv و sys.exit -> csv و pip
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۵ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران (۷ درس).
3. ویدئوی کوتاه [پایتون](/kb/d/w06-sh-python) را پس از یادداشت حلقه‌ها ببین.
4. [جلسهٔ حل تمرین (Section)](/kb/d/w06-sec) را پیش از پرابلم‌ست ببین.
5. چالش‌های کوتاه هفته را امتحان کن، آزمون تسلط را بده و بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۶

طبق صفحهٔ رسمی پرابلم‌ست ۶:

- [Hello](/kb/d/w06-ps-hello) را به پایتون **تحویل بده**.
- **یکی** از [Mario (less comfortable)](/kb/d/w06-ps-mario-less) یا [Mario (more comfortable)](/kb/d/w06-ps-mario-more) را تحویل بده.
- **یکی** از [Cash](/kb/d/w06-ps-cash) یا [Credit](/kb/d/w06-ps-credit) را تحویل بده.
- [Readability](/kb/d/w06-ps-readability) را **تحویل بده**.
- [DNA](/kb/d/w06-ps-dna) را **تحویل بده**.
- اگر هر دو نسخهٔ Mario یا هر دوی Cash و Credit را تحویل بدهی، نمرهٔ بالاتر ثبت می‌شود.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

مسئله‌های تمرینی اختیاری: [Bank](/kb/d/w06-pr-bank)، [Figlet](/kb/d/w06-pr-figlet)، [Jar](/kb/d/w06-pr-jar)، [Seven Day Average](/kb/d/w06-pr-seven-day-average)، [Taqueria](/kb/d/w06-pr-taqueria).

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود. صفحهٔ رسمی می‌گوید برای Hello، Mario، Cash، Credit و Readability نگاه کردن به پیاده‌سازی‌های C (خودت یا دیگران) معقول است، اما نگاه کردن به پیاده‌سازی پایتونِ دیگران معقول نیست. برای همین این بسته هیچ نسخهٔ پایتونی از این برنامه‌ها، و هیچ کدی برای شمردن STRها در DNA، ارائه نمی‌دهد.

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی مسئله‌هایی که انتخاب کرده‌ای کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۶](https://cs50.harvard.edu/x/weeks/6/) · [درس‌نامه](https://cs50.harvard.edu/x/notes/6/) · [ویدئوی سخنرانی](https://video.cs50.io/Rl0ludWTLxs)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/6/lecture6.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/6/src6.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/6/lang/en/lecture6.srt)
- [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/6/) · [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
