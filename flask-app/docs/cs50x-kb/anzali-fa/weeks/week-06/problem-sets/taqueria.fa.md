---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-pr-taqueria
type: practice-guide
title: راهنمای تاکوفروشی Felipe
title_fa: تاکوفروشی Felipe
title_en: Felipe’s Taqueria
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/taqueria/
source_refs:
- src-practice-taqueria#felipes-taqueria
- src-anzali-authored-6
concept_ids:
- w06-c-dict
- w06-c-dict-lookup
- w06-c-try-except
- w06-c-exception
- w06-c-string-methods
- w06-c-f-string
- w06-c-while-true-break
problem_set_ref: weeks/week-06/problem-sets/taqueria.json
prev: w06-pr-seven-day-average
next: null
order: 30
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای تاکوفروشی Felipe

> **منبع رسمی:** [Felipe’s Taqueria](https://cs50.harvard.edu/x/2026/practice/taqueria/) از مسئله‌های تمرینی هفتهٔ ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

Felipe’s Taqueria یکی از رستوران‌های محبوب Harvard Square است و صفحهٔ رسمی منوی آن را به شکل یک `dict` داده است: نام هر غذا کلید و قیمتش به دلار مقدار است.

در فایل `taqueria.py` برنامه‌ای بنویس که سفارش بگیرد: غذاها را یکی‌یکی بپرسد تا کاربر control-d بزند، و پس از هر غذا جمع کل را با علامت `$` و دو رقم اعشار چاپ کند. بزرگی و کوچکی حروف مهم نیست و ورودی‌ای که در منو نیست نادیده گرفته می‌شود.

> **از سخنرانی:** واژه‌نامه و `in` در [یادداشت جست‌وجو و واژه‌نامه](/kb/d/w06-n13)، استثنا در [یادداشت تقسیم و استثنا](/kb/d/w06-n10) و f-string در [یادداشت رشته‌ها](/kb/d/w06-n04).

## خواسته‌های رسمی

1. در فایل `taqueria.py` برنامه‌ای بنویس که سفارش بگیرد و غذاها را یکی در هر سطر بپرسد تا کاربر control-d بزند.
2. پس از هر غذا، جمع کل غذاهای واردشده تا آن لحظه را با پیشوند `$` و دو رقم اعشار نشان بده.
3. به بزرگی و کوچکی حروف ورودی حساس نباش.
4. ورودی‌ای را که غذای منو نیست نادیده بگیر.
5. فرض کن نام همهٔ غذاهای منو با حروف آغازین بزرگ (titlecase) نوشته شده است.

> **توجه (d107):** این مسئلهٔ تمرینی از CS50P سال ۲۰۲۲ آمده است؛ فایل آغازین و دستور check50 آن نشانی ۲۰۲۲ دارند و همان‌طور که در صفحهٔ رسمی هست نقل شده‌اند.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل آغازین را دانلود کن. منوی رسمی را در برنامه‌ات به شکل یک `dict` بگذار.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/6/taqueria.zip
unzip taqueria.zip
rm taqueria.zip
```

## نمونه‌های رسمی ورودی و خروجی

منوی رسمی (واژه‌نامهٔ قیمت‌ها):

```text
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

## آزمون‌های رسمی ورودی و خروجی

صفحهٔ رسمی این ورودی‌ها و خروجی‌ها را می‌دهد (هر غذا را تایپ کن و Enter بزن):

- `Taco, Taco` ← `Total: $6.00`
- `Baja Taco, Tortilla Salad` ← `Total: $12.25`
- `Burger` ← دوباره می‌پرسد

## قطعه‌کدهای رسمی راهنما

> **رسمی:** این قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند و ابزار عمومی‌اند، نه بخشی از راه‌حل.

تشخیص control-d با گرفتن `EOFError` (از بخش Hints):

```python
try:
    item = input()
except EOFError:
    ...
```

دسترسی به مقدار با کلید:

```python
d[key]
```

بررسی وجود کلید:

```python
if key in d:
    ...
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- دیکشنری (dict): جفت‌های کلید و مقدار — [یادداشت](/kb/d/w06-n13) · درس کوتاه `w06-l07` (واحد `w06-l07-u02`)
- جست‌وجو با key in d و d[key] — [یادداشت](/kb/d/w06-n13) · درس کوتاه `w06-l07` (واحد `w06-l07-u02`)
- try و except برای گرفتن استثنا — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u03`)
- استثنا (exception) و ValueError — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u03`)
- متدهای رشته: lower، upper، capitalize — [یادداشت](/kb/d/w06-n08) · درس کوتاه `w06-l03` (واحد `w06-l03-u03`)
- رشتهٔ قالب‌بندی‌شده (f-string) و {} — [یادداشت](/kb/d/w06-n04) · درس کوتاه `w06-l02` (واحد `w06-l02-u01`)
- while True با break به جای do-while — [یادداشت](/kb/d/w06-n11) · درس کوتاه `w06-l06` (واحد `w06-l06-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. حلقه‌ای لازم داری که تا control-d ادامه بدهد. قطعهٔ رسمی `EOFError` را ببین و فکر کن `break` کجا می‌آید.
2. صفحهٔ رسمی می‌گوید نام همهٔ غذاهای منو titlecase است. در مستندات متدهای رشته، متدی را پیدا کن که ورودی کاربر را به همان شکل درآورد.
3. پیش از دسترسی به قیمت، بسنج که کلید در واژه‌نامه هست، یا `KeyError` را بگیر؛ صفحهٔ رسمی هر دو را می‌پذیرد.
4. برای دو رقم اعشار، قالب‌بندی f-string را در مستندات پایتون بخوان.
5. پس از control-d یک سطر تازه چاپ کن تا اعلان ترمینال روی همان خط نماند.

## اشتباه‌های رایج

- گرفتن `KeyError` برای غذایی که در منو نیست
- چاپ جمع کل بدون دو رقم اعشار (مثلاً `$6.0`)
- حساس بودن به بزرگی حروف
- گرفتن `except` خیلی کلی که control-d را هم با خطای دیگر یکی می‌کند

## چک‌لیست خودآزمایی

1. برنامه تا control-d غذا می‌پرسد.
2. پس از هر غذای معتبر جمع کل به شکل `Total: $6.00` چاپ می‌شود.
3. `taco` و `TACO` هم پذیرفته می‌شوند.
4. `Burger` نادیده گرفته می‌شود و برنامه خطا نمی‌دهد.
5. check50 همه را سبز نشان می‌دهد.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2022/python/taqueria
```

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/J20VZsCKXRPoavI0nFwCreRmr)

## پیوند رسمی

- [Felipe’s Taqueria](https://cs50.harvard.edu/x/2026/practice/taqueria/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
