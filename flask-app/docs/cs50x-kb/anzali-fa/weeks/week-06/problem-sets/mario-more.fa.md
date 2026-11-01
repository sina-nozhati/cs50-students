---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-ps-mario-more
type: problem-set-guide
title: راهنمای ماریو، نسخهٔ چالشی (Sentimental Mario)
title_fa: ماریو، نسخهٔ چالشی (Sentimental Mario)
title_en: Mario (more comfortable)
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/6/mario/more/
source_refs:
- src-pset-6-mario-more#problem-to-solve
- src-pset-6-mario-more#specification
- src-anzali-authored-6
- src-pset-6#what-to-do
- src-pset-6#academic-honesty
concept_ids:
- w06-c-port-c-to-python
- w06-c-cs50-library-py
- w06-c-while-true-break
- w06-c-for-range
- w06-c-string-repeat
- w06-c-print-end
- w06-c-nested-loops-py
problem_set_ref: weeks/week-06/problem-sets/mario-more.json
prev: w06-ps-mario-less
next: w06-ps-cash
order: 21
choice_group: mario
submission: choose-one
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای ماریو، نسخهٔ چالشی (Sentimental Mario)

> **منبع رسمی:** [Mario (more comfortable)](https://cs50.harvard.edu/x/2026/psets/6/mario/more/) از پرابلم‌ست ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از دو نسخه را تحویل بده؛ اگر هر دو را تحویل بدهی، نمرهٔ بالاتر ثبت می‌شود. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

همان دو نیم‌هرم کنار هم پرابلم‌ست ۱ (مثل مرحلهٔ پایانی بازی ماریو)، این بار به پایتون: برنامه‌ای در فایل `mario.py` و پوشهٔ `sentimental-mario-more`. هر دو نیم‌هرم یک ارتفاع دارند و میانشان شکافی به پهنای دو فاصله است.

ارتفاع را با `get_int` بگیر و اگر عدد صحیحی از `1` تا `8` نبود دوباره بپرس. پس از آخرین `#` هر سطر هیچ فاصلهٔ اضافه‌ای نباید باشد. صفحهٔ رسمی پرابلم‌ست ۶ می‌گوید نگاه کردن به پیاده‌سازی C خودت یا دیگران برای این مسئله معقول است، اما نگاه کردن به پیاده‌سازی پایتونِ دیگران معقول نیست. این راهنما هیچ کد پایتونی از برنامهٔ خواسته‌شده ندارد.

> **از سخنرانی:** سخنرانی چند شکل از Mario را در پایتون نشان می‌دهد (ستون، سطر، شبکه) و [یادداشت Mario](/kb/d/w06-n11) آن‌ها را توضیح می‌دهد، ولی هیچ‌کدام هرم پرابلم‌ست نیست.

> **از هفتهٔ ۱:** راهنمای فارسی نسخهٔ C این مسئله در [پرابلم‌ست ۱](/kb/d/w01-fa) هست. منطق همان است؛ فقط نحو عوض می‌شود.

## خواسته‌های رسمی

1. در فایل `mario.py` در پوشهٔ `sentimental-mario-more` برنامه‌ای بنویس که با `#` هرم بسازد، همان‌طور که در پرابلم‌ست ۱ ساختی، این بار به پایتون.
2. ابتدا با `get_int` ارتفاع را بپرس: عدد صحیح مثبتی از `1` تا `8` (شامل هر دو).
3. اگر کاربر عدد صحیح مثبتی که از `8` بزرگ‌تر نیست نداد، دوباره بپرس.
4. سپس با کمک `print` و یک یا چند حلقه نیم‌هرم‌ها را بساز.
5. گوشهٔ پایین‌چپ هرم را با لبهٔ چپ ترمینال هم‌تراز کن، میان دو نیم‌هرم دو فاصله بگذار و پس از آخرین `#` هر سطر فاصلهٔ اضافه نگذار.

> **ناهمخوانی (d110):** بخش Specification از «عدد صحیح مثبت بین ۱ و ۸» حرف می‌زند و بخش آزمون‌ها `foo` و ورودی خالی را هم امتحان می‌کند. `get_int` کتابخانهٔ CS50 ورودی غیرعددی را خودش دوباره می‌پرسد؛ بررسی بازهٔ ۱ تا ۸ کار توست.

## شروع کار

این مسئله کد آغازین ندارد. پوشهٔ `sentimental-mario-more` را بساز و فایل `mario.py` را در آن بنویس. صفحهٔ رسمی می‌خواهد این ورودی‌ها رد شوند و دوباره پرسیده شود: `-1`، `0`، `9`، `foo` و ورودی خالی.

## نمونه‌های رسمی ورودی و خروجی

ارتفاع `1`:

```text
#  #
```

ارتفاع `2`:

```text
 #  #
##  ##
```

ارتفاع `8`:

```text
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

ورودی `9` رد می‌شود و بعد ارتفاع `2`:

```text
 #  #
##  ##
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- بازنویسی برنامهٔ C در پایتون (Sentimental) — [یادداشت](/kb/d/w06-ps-hello)
- کتابخانهٔ CS50 در پایتون: get_string، get_int، get_float — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)
- while True با break به جای do-while — [یادداشت](/kb/d/w06-n11) · درس کوتاه `w06-l06` (واحد `w06-l06-u01`)
- for i in range(n) — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u01`)
- تکرار رشته با *: "?" * 4 — [یادداشت](/kb/d/w06-n11) · درس کوتاه `w06-l06` (واحد `w06-l06-u02`)
- print(..., end="") برای ماندن روی همان خط — [یادداشت](/kb/d/w06-n11) · درس کوتاه `w06-l06` (واحد `w06-l06-u02`)
- حلقهٔ تودرتو در پایتون — [یادداشت](/kb/d/w06-n11) · درس کوتاه `w06-l06` (واحد `w06-l06-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. برنامهٔ C خودت از پرابلم‌ست ۱ را مرور کن و بخش‌ها را جدا کن: گرفتن ارتفاع معتبر، و چاپ سطرها. هر بخش در پایتون چه شکلی دارد؟
2. پایتون `do-while` ندارد. الگوی جایگزین را در یادداشت Mario ببین و از خودت بپرس شرط خروج دقیقاً چیست: عددی از ۱ تا ۸.
3. `get_int` از کتابخانهٔ CS50 ورودی غیرعددی مثل `foo` یا ورودی خالی را خودش رد می‌کند و دوباره می‌پرسد؛ بررسی بازه بر عهدهٔ توست.
4. برای هر سطر بشمار: چند فاصله و چند `#`؟ رابطهٔ این دو عدد را با شمارهٔ سطر و ارتفاع روی کاغذ برای ارتفاع ۴ بنویس.
5. هر سطر سه بخش دارد: نیم‌هرم چپ (با فاصله‌های پیش از آن)، شکاف ثابت، و نیم‌هرم راست. نیم‌هرم راست پس از خود هیچ فاصله‌ای ندارد.
6. در پایتون می‌توانی یک رشته را با عدد ضرب کنی، و `print` پارامتری دارد که سطر تازه را کنترل می‌کند. هر دو را در یادداشت Mario دیده‌ای؛ کدام برای این مسئله ساده‌تر است، خودت تصمیم بگیر.
7. پس از نوشتن، خروجی را با نمونه‌های رسمی مقایسه کن و مطمئن شو در پایان هیچ سطری فاصلهٔ اضافه نیست.

## اشتباه‌های رایج

- پذیرفتن `0` یا `9` به عنوان ارتفاع
- فاصلهٔ اضافه در پایان سطرها، که check50 آن را خطا می‌داند
- هرم چپ‌چین به جای راست‌چین (یا برعکس)
- یک سطر کم یا زیاد به‌خاطر شروع `range` از ۰ یا ۱
- فراموش کردن `from cs50 import get_int` یا اجرای برنامه با `make`
- فاصله گذاشتن پس از نیم‌هرم راست برای «قرینه» کردن شکل

## چک‌لیست خودآزمایی

1. فایل `mario.py` در پوشهٔ `sentimental-mario-more` است و به پایتون نوشته شده.
2. ارتفاع را با `get_int` می‌گیرم.
3. `-1`، `0`، `9`، `foo` و ورودی خالی رد می‌شوند و دوباره پرسیده می‌شود.
4. خروجی ارتفاع‌های ۱، ۲ و ۸ دقیقاً با نمونه‌های رسمی یکی است.
5. میان دو نیم‌هرم دقیقاً دو فاصله است و پس از آخرین `#` هر سطر فاصله‌ای نیست.
6. check50 همه را سبز نشان می‌دهد.
7. style50 تغییری پیشنهاد نمی‌کند.
8. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/sentimental/mario/more
```

سبک با style50:

```bash
style50 mario.py
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/sentimental/mario/more
```

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/B0CE4bjPGR19PoRKUe5ZF9VoM)

## پیوند رسمی

- [Mario (more comfortable)](https://cs50.harvard.edu/x/2026/psets/6/mario/more/)
- [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
