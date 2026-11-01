---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-ps-hello
type: problem-set-guide
title: راهنمای سلام دوباره (Sentimental Hello)
title_fa: سلام دوباره (Sentimental Hello)
title_en: Hello, Again
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/6/hello/
source_refs:
- src-pset-6-hello#problem-to-solve
- src-anzali-authored-6
- src-pset-6#what-to-do
- src-pset-6#academic-honesty
concept_ids:
- w06-c-port-c-to-python
- w06-c-run-python
- w06-c-cs50-library-py
- w06-c-import
- w06-c-input-returns-str
- w06-c-f-string
problem_set_ref: weeks/week-06/problem-sets/hello.json
prev: w06-sh-python
next: w06-ps-mario-less
order: 19
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای سلام دوباره (Sentimental Hello)

> **منبع رسمی:** [Hello, Again](https://cs50.harvard.edu/x/2026/psets/6/hello/) از پرابلم‌ست ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

این همان مسئلهٔ «سلام» پرابلم‌ست ۱ است، این بار به پایتون: برنامه‌ای در فایل `hello.py` و پوشهٔ `sentimental-hello` که نام کاربر را می‌پرسد و `hello,` و بعد همان نام را چاپ می‌کند.

صفحهٔ رسمی سه یادآوری دارد: `get_string` از کتابخانهٔ `cs50` رشته می‌گیرد، `print` چاپ می‌کند، و با گذاشتن `f` پیش از رشته می‌توانی مقدار یک متغیر را درون رشته جای‌گذاری کنی. صفحهٔ رسمی پرابلم‌ست ۶ می‌گوید نگاه کردن به پیاده‌سازی C خودت یا دیگران برای این مسئله معقول است، اما نگاه کردن به پیاده‌سازی پایتونِ دیگران معقول نیست. این راهنما هیچ کد پایتونی از برنامهٔ خواسته‌شده ندارد.

> **از سخنرانی:** `print`، `input` و f-string در [یادداشت رشته‌ها](/kb/d/w06-n04)؛ `import` و کتابخانهٔ CS50 در [یادداشت تابع‌ها و کتابخانه‌ها](/kb/d/w06-n03).

> **از هفتهٔ ۱:** راهنمای فارسی نسخهٔ C این مسئله در [پرابلم‌ست ۱](/kb/d/w01-fa) هست. منطق همان است؛ فقط نحو عوض می‌شود.

## خواسته‌های رسمی

1. در فایل `hello.py` در پوشهٔ `sentimental-hello` برنامه‌ای بنویس که نام کاربر را بپرسد و `hello, so-and-so` را چاپ کند، که `so-and-so` همان نامی است که کاربر داده است.
2. این بار برنامه باید به پایتون نوشته شود.

## شروع کار

این مسئله کد آغازین ندارد. در ترمینال cs50.dev پوشهٔ `sentimental-hello` را بساز، واردش شو و فایل `hello.py` را بساز. برنامه را با `python hello.py` اجرا کن؛ کامپایل لازم نیست.

## آزمون‌های رسمی ورودی و خروجی

صفحهٔ رسمی پیشنهاد می‌کند پیش از check50 این ورودی‌ها را خودت بیازمایی (برنامه را با `python hello.py` اجرا کن):

- `David` ← `hello, David`
- `Inno` ← `hello, Inno`
- `Kamryn` ← `hello, Kamryn`

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- بازنویسی برنامهٔ C در پایتون (Sentimental) — [یادداشت](/kb/d/w06-ps-hello)
- اجرای برنامه با python hello.py — [یادداشت](/kb/d/w06-n01) · درس کوتاه `w06-l01` (واحد `w06-l01-u01`)
- کتابخانهٔ CS50 در پایتون: get_string، get_int، get_float — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)
- import و from ... import — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)
- input همیشه str برمی‌گرداند — [یادداشت](/kb/d/w06-n06) · درس کوتاه `w06-l02` (واحد `w06-l02-u04`)
- رشتهٔ قالب‌بندی‌شده (f-string) و {} — [یادداشت](/kb/d/w06-n04) · درس کوتاه `w06-l02` (واحد `w06-l02-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. برنامهٔ C خودت از پرابلم‌ست ۱ را باز کن و خط‌به‌خط از خودت بپرس معادل پایتونی هر بخش چیست. کدام خط‌ها اصلاً لازم نیستند؟
2. برای استفاده از `get_string` باید آن را از کتابخانهٔ `cs50` وارد کنی. دو شیوهٔ `import` را در یادداشت تابع‌ها و کتابخانه‌ها مقایسه کن.
3. برای چاپ، به جای `%s` از f-string استفاده کن. یادت باشد `print` خودش سطر تازه می‌گذارد.
4. خروجی را دقیقاً با نمونه‌های رسمی مقایسه کن: ویرگول، فاصله و حروف کوچک `hello` مهم‌اند.

## اشتباه‌های رایج

- نوشتن `printf` یا گذاشتن نقطه‌ویرگول و آکولاد به عادت C
- فراموش کردن `f` پیش از رشته و چاپ شدن خود `{name}`
- چاپ `Hello` با حرف بزرگ یا جا انداختن فاصلهٔ پس از ویرگول
- اجرای برنامه با `make hello` یا `./hello` به جای `python hello.py`

## چک‌لیست خودآزمایی

1. فایل `hello.py` در پوشهٔ `sentimental-hello` است.
2. برنامه نام را می‌پرسد و دقیقاً `hello, ` و بعد نام را چاپ می‌کند.
3. برنامه به پایتون است و با `python hello.py` اجرا می‌شود.
4. سه آزمون رسمی (David، Inno، Kamryn) را خودم اجرا کرده‌ام.
5. check50 همه را سبز نشان می‌دهد.
6. style50 تغییری پیشنهاد نمی‌کند.
7. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/sentimental/hello
```

سبک با style50:

```bash
style50 hello.py
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/sentimental/hello
```

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/gqi2voQFzbKlna6WkQR0G2W93)

## پیوند رسمی

- [Hello, Again](https://cs50.harvard.edu/x/2026/psets/6/hello/)
- [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
