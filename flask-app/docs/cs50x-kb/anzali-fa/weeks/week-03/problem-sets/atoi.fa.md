---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-pr-atoi
type: practice-guide
title: راهنمای atoi بازگشتی (Recursive atoi)
title_fa: atoi بازگشتی (Recursive atoi)
title_en: Recursive atoi
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/atoi/
source_refs:
- src-practice-atoi#implementation-details
- src-practice-atoi#how-to-test-your-code
- src-anzali-authored-3
concept_ids:
- w03-c-recursion
- w03-c-base-case
- w03-c-recursive-case
- w03-c-iteration-vs-recursion
problem_set_ref: weeks/week-03/problem-sets/atoi.json
prev: w03-ps-tideman
next: w03-pr-temps
order: 32
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای atoi بازگشتی (Recursive atoi)

> **منبع رسمی:** [Recursive atoi](https://cs50.harvard.edu/x/2026/practice/atoi/) از مسئله‌های تمرینی هفتهٔ ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

تصور کن به دههٔ ۱۹۷۰ برگشته‌ای و باید راهی برای تبدیل `string` به `int` بسازی، همان کاری که `atoi` می‌کند. صفحهٔ رسمی یک پیاده‌سازی با حلقه برای عددهای مثبت می‌دهد و تو آن را به نسخهٔ **بازگشتی** تبدیل می‌کنی.

هدف‌های یادگیری رسمی: عمیق‌تر فهمیدن رشته‌ها و تمرین نوشتن تابع بازگشتی. صفحهٔ رسمی یادآوری می‌کند که بازگشت می‌تواند حافظه‌بر باشد و همیشه بهترین راه نیست.

## خواسته‌های رسمی

1. تابع `convert` را بازگشتی بنویس.
2. برنامه برای عدد صحیح مثبت باید مثل نمونه‌های رسمی رفتار کند.

## شروع کار

فایل آغازین را با فرمان رسمی دانلود و از حالت فشرده خارج کن. این تمرین check50 و تحویل ندارد.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/3/atoi.zip
unzip atoi.zip
rm atoi.zip
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی ۱:

```text
atoi/ $ ./atoi
Enter a positive integer: 3432
3432
```

نمونهٔ رسمی ۲:

```text
atoi/ $ ./atoi
Enter a positive integer: 98765
98765
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- بازگشت: تابعی که خودش را صدا می‌زند — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- حالت پایه — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- حالت بازگشتی — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- تکرار در برابر بازگشت: هرم با حلقه و با بازگشت — [یادداشت](/kb/d/w03-n13) · درس کوتاه `w03-l06` (واحد `w03-l06-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول بپرس: کوچک‌ترین رشته‌ای که جوابش را بدون فکر می‌دانی چیست؟ آن حالت پایه است.
2. یادداشت ۱۲ را مرور کن: هر فراخوانی بازگشتی باید مسئله را کوچک‌تر کند. اینجا «کوچک‌تر» یعنی چه؟
3. یادت هست رشته در C با `\0` تمام می‌شود (هفتهٔ ۲)؟ این در کوتاه کردن رشته به کار می‌آید.
4. یک عدد دورقمی را با دست دنبال کن: رقم آخر و بقیهٔ رشته چه رابطه‌ای با عدد کامل دارند؟

## اشتباه‌های رایج

- فراموش کردن حالت پایه
- فراخوانی بازگشتی با همان رشته بدون کوتاه کردن
- جمع کردن کد ASCII رقم به‌جای مقدار عددی آن

## چک‌لیست خودآزمایی

1. تابع `convert` بازگشتی است و حلقه ندارد.
2. هر دو نمونهٔ رسمی خروجی درست دارند.
3. حالت پایه را مشخص کرده‌ام.
4. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

سبک با style50:

```bash
style50 atoi.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: Why do you need a base case whenever you create a recursive function?

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های گام‌به‌گام «Hints» صفحهٔ رسمی](https://cs50.harvard.edu/x/practice/atoi/#background): این راهنمایی‌ها الگوریتم را تقریباً کامل توصیف می‌کنند؛ اول خودت امتحان کن.
- [«A More Thorough Implementation»](https://cs50.harvard.edu/x/practice/atoi/#a-more-thorough-implementation): پیاده‌سازی کامل رسمی atoi؛ در این بسته بازتولید نشده است.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/qH1q1cIz2kZEnbl1Mc4CCCcYK)

## پیوند رسمی

- [Recursive atoi](https://cs50.harvard.edu/x/2026/practice/atoi/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
