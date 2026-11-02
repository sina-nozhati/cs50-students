---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-pr-snackbar
type: practice-guide
title: راهنمای اسنک‌بار (Snackbar)
title_fa: اسنک‌بار (Snackbar)
title_en: Snackbar
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/snackbar/
source_refs:
- src-practice-snackbar#implementation-details
- src-anzali-authored-3
concept_ids:
- w03-c-struct
- w03-c-array-of-structs
- w03-c-linear-search
- w03-c-search-strings
- w03-c-strcmp-return
- w03-c-encapsulation
problem_set_ref: weeks/week-03/problem-sets/snackbar.json
prev: w03-pr-max
next: null
order: 35
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای اسنک‌بار (Snackbar)

> **منبع رسمی:** [Snackbar](https://cs50.harvard.edu/x/2026/practice/snackbar/) از مسئله‌های تمرینی هفتهٔ ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

در ساحل هستی و می‌خواهی از اسنک‌بار چند چیز سفارش بدهی، ولی پول نقدت محدود است. در `snackbar.c` دو تابع را کامل می‌کنی: `add_items` که دست‌کم چهار قلم اول منوی Beach Burger Shack را اضافه می‌کند و `get_cost` که با **جست‌وجوی خطی** قیمت هر قلم را پیدا می‌کند.

هدف‌های یادگیری رسمی: تمرین کار با `struct` و نوشتن یک الگوریتم جست‌وجوی خطی. `main` از قبل کامل است.

## خواسته‌های رسمی

1. `add_items` دست‌کم چهار قلم اول منو را به آرایهٔ `menu` اضافه کند.
2. `get_cost` با جست‌وجوی خطی قیمت هر قلم را برگرداند.
3. جست‌وجو به بزرگی و کوچکی حرف حساس نباشد.

## شروع کار

فایل آغازین را با فرمان رسمی دانلود و از حالت فشرده خارج کن. این تمرین check50 و تحویل ندارد.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/3/snackbar.zip
unzip snackbar.zip
rm snackbar.zip
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی ۱:

```text
snackbar/ $ ./snackbar

Welcome to Beach Burger Shack!
Choose from the following menu to order. Press enter when done.

Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: burger
Enter a food item: fries
Enter a food item: soda
Enter a food item: 

Your total cost is: $16.50
```

نمونهٔ رسمی ۲:

```text
snackbar/ $ ./snackbar

Welcome to Beach Burger Shack!
Choose from the following menu to order. Press enter when done.

Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: cold brew
Enter a food item: hot dog
Enter a food item: 

Your total cost is: $8.00
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- ساختار داده با typedef struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- آرایه‌ای از struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- جست‌وجوی خطی — [یادداشت](/kb/d/w03-n02) · درس کوتاه `w03-l01` (واحد `w03-l01-u02`)
- جست‌وجو در آرایهٔ رشته‌ها با strcmp — [یادداشت](/kb/d/w03-n07) · درس کوتاه `w03-l03` (واحد `w03-l03-u02`)
- مقدار بازگشتی strcmp: صفر یعنی برابر — [یادداشت](/kb/d/w03-n07) · درس کوتاه `w03-l03` (واحد `w03-l03-u02`)
- کپسوله‌سازی داده‌های مرتبط — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. این همان الگوی phonebook سخنرانی است: آرایه‌ای از struct که در آن با نام می‌گردی. یادداشت ۹ را مرور کن.
2. صفحهٔ رسمی می‌گوید تابعی در `strings.h` به کار می‌آید. در manual.cs50.io ببین کدام تابع رشته‌ها را بدون توجه به بزرگی و کوچکی حرف مقایسه می‌کند.
3. اگر قلمی پیدا نشد، `get_cost` چه باید برگرداند؟ کد آغازین را بخوان.

## اشتباه‌های رایج

- مقایسهٔ رشته‌ها با `==`
- حساس بودن جست‌وجو به بزرگی و کوچکی حرف
- پیمایش بیشتر از تعداد قلم‌های اضافه‌شده

## چک‌لیست خودآزمایی

1. دست‌کم چهار قلم اول منو اضافه شده‌اند.
2. قیمت‌ها با جست‌وجوی خطی پیدا می‌شوند.
3. `burger` و `Burger` هر دو کار می‌کنند.
4. هر دو نمونهٔ رسمی جمع درست می‌دهند.
5. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

سبک با style50:

```bash
style50 snackbar.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: Why is an array of `struct`s a better solution here than multiple arrays?

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/sNDasPt6uPRp8mWF12ZePqNn1)

## پیوند رسمی

- [Snackbar](https://cs50.harvard.edu/x/2026/practice/snackbar/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
