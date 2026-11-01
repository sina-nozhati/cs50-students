---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-pr-jar
type: practice-guide
title: راهنمای ظرف کلوچه (Cookie Jar)
title_fa: ظرف کلوچه (Cookie Jar)
title_en: Cookie Jar
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/jar/
source_refs:
- src-practice-jar#cookie-jar
- src-anzali-authored-6
concept_ids:
- w06-c-class-init
- w06-c-object-method
- w06-c-exception
- w06-c-try-except
problem_set_ref: weeks/week-06/problem-sets/jar.json
prev: w06-pr-figlet
next: w06-pr-seven-day-average
order: 28
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای ظرف کلوچه (Cookie Jar)

> **منبع رسمی:** [Cookie Jar](https://cs50.harvard.edu/x/2026/practice/jar/) از مسئله‌های تمرینی هفتهٔ ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

در فایل `jar.py` یک کلاس `Jar` می‌سازی که ظرف کلوچه را مدل می‌کند: ظرفیتی دارد، می‌شود در آن کلوچه گذاشت (`deposit`) یا از آن برداشت (`withdraw`)، و ظرفیت و تعداد فعلی را برمی‌گرداند.

هر جا عمل ناممکن است (ظرفیت منفی یا غیرصحیح، گذاشتن بیش از ظرفیت، برداشتن بیش از موجودی) باید استثنای `ValueError` برانگیخته شود. ساختار کلاس را صفحهٔ رسمی داده است و نباید پارامترهای متدها را تغییر بدهی. این مسئله check50 ندارد.

> **از ویدئوی کوتاه:** `class`، `__init__` و `self` در [ویدئوی کوتاه پایتون](/kb/d/w06-sh-python)؛ استثنا در [یادداشت تقسیم و استثنا](/kb/d/w06-n10).

## خواسته‌های رسمی

1. در فایل `jar.py` یک `class` به نام `Jar` با این متدها پیاده کن.
2. `__init__` ظرف را با ظرفیت `capacity` (بیشترین تعداد کلوچه) می‌سازد.
3. اگر `capacity` عدد صحیح نامنفی نبود، `__init__` باید `ValueError` برانگیزد.
4. `__str__` رشته‌ای با n نویسهٔ کلوچه برمی‌گرداند (n تعداد کلوچه‌های ظرف). صفحهٔ رسمی نویسهٔ کلوچه (U+1F36A) را به کار می‌برد.
5. `deposit` به تعداد `n` کلوچه به ظرف می‌افزاید.
6. اگر این کار از ظرفیت بیشتر شود، `deposit` باید `ValueError` برانگیزد.
7. `withdraw` به تعداد `n` کلوچه از ظرف برمی‌دارد.
8. اگر به این تعداد کلوچه در ظرف نبود، `withdraw` باید `ValueError` برانگیزد.
9. `capacity` ظرفیت ظرف را برمی‌گرداند.
10. `size` تعداد واقعی کلوچه‌های درون ظرف را برمی‌گرداند.
11. پارامترهای این متدها را تغییر نده، ولی می‌توانی متدهای خودت را بیفزایی.

> **توجه (d107):** این مسئلهٔ تمرینی از CS50P سال ۲۰۲۲ آمده است؛ فایل آغازین و دستور check50 آن نشانی ۲۰۲۲ دارند و همان‌طور که در صفحهٔ رسمی هست نقل شده‌اند.

> **توجه (d109):** متن رسمی نویسهٔ کلوچه را مستقیم نشان می‌دهد. این بسته شکلک چاپ نمی‌کند و آن را با کد یونیکدش (U+1F36A) نام می‌برد (تصمیم D50).

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل آغازین را دانلود کن. صفحهٔ رسمی پیشنهاد می‌کند یک تابع `main` بنویسی که با `jar = Jar()` ظرفی بسازد، با `print(str(jar.capacity))` ظرفیت و با `print(str(jar))` محتوا را چاپ کند، و `main()` را در پایان فایل صدا بزنی.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/6/jar.zip
unzip jar.zip
rm jar.zip
```

## قطعه‌کدهای رسمی راهنما

> **رسمی:** این قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند و ابزار عمومی‌اند، نه بخشی از راه‌حل.

ساختار رسمی کلاس (نباید پارامترها را تغییر بدهی):

```python
class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- class، __init__ و self — [یادداشت](/kb/d/w06-sh-python) · درس کوتاه `w06-l04` (واحد `w06-l04-u04`)
- شیء و متد: تابعی که به یک مقدار تعلق دارد — [یادداشت](/kb/d/w06-n08) · درس کوتاه `w06-l03` (واحد `w06-l03-u03`)
- استثنا (exception) و ValueError — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u03`)
- try و except برای گرفتن استثنا — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول ویدئوی کوتاه پایتون را دربارهٔ `class` و `__init__` و `self` ببین. هر متد پارامتر اول `self` دارد.
2. تصمیم بگیر شیء چه داده‌هایی را باید به خاطر بسپارد. دو عدد کافی است.
3. `@property` اجازه می‌دهد `jar.capacity` را بدون پرانتز بخوانی. اگر نام ویژگی داخلی با نام property یکی باشد چه مشکلی پیش می‌آید؟ مستندات `property` را ببین.
4. برای برانگیختن استثنا، صفحهٔ رسمی خودش `raise ValueError` را نام می‌برد. برای آزمودن آن در `main` می‌توانی از `try` و `except` استفاده کنی.
5. در `main` حالت‌های مرزی را امتحان کن: ظرفیت ۰، گذاشتن دقیقاً تا ظرفیت، برداشتن همهٔ کلوچه‌ها.

## اشتباه‌های رایج

- فراموش کردن `self` در تعریف متد یا هنگام دسترسی به ویژگی
- هم‌نام کردن ویژگی داخلی با property و گرفتن بازگشت بی‌پایان
- برانگیختن استثنا پس از تغییر تعداد کلوچه‌ها به جای پیش از آن
- پذیرفتن ظرفیت منفی

## چک‌لیست خودآزمایی

1. `Jar()` بدون آرگومان ظرفیت پیش‌فرض ۱۲ دارد.
2. ظرفیت منفی یا غیرصحیح `ValueError` برمی‌انگیزد.
3. `str(jar)` به تعداد کلوچه‌ها نویسهٔ کلوچه برمی‌گرداند.
4. گذاشتن بیش از ظرفیت و برداشتن بیش از موجودی هر دو `ValueError` برمی‌انگیزند.
5. `capacity` و `size` بدون پرانتز (به شکل property) کار می‌کنند.
6. پارامترهای متدها را تغییر نداده‌ام.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## پیوند رسمی

- [Cookie Jar](https://cs50.harvard.edu/x/2026/practice/jar/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
