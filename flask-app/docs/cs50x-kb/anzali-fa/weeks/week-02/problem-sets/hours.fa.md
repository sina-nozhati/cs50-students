---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-pr-hours
type: practice-guide
title: راهنمای ساعت‌های مطالعه (Hours)
title_fa: ساعت‌های مطالعه (Hours)
title_en: Hours
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/hours/
source_refs:
- src-practice-hours#implementation-details
- src-anzali-authored-2
concept_ids:
- w02-c-array
- w02-c-array-loop
- w02-c-array-parameter
- w02-c-function-anatomy
problem_set_ref: weeks/week-02/problem-sets/hours.json
prev: w02-ps-substitution
next: w02-pr-no-vowels
order: 32
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای ساعت‌های مطالعه (Hours)

> **منبع رسمی:** [Hours](https://cs50.harvard.edu/x/2026/practice/hours/) از مسئله‌های تمرینی هفتهٔ ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

فرض کن هر هفته روی پرابلم‌ست‌های CS50 وقت می‌گذاری و می‌خواهی بدانی روی هم یا به‌طور میانگین چند ساعت کار کرده‌ای. در این تمرین تابعی را کامل می‌کنی که بر اساس ورودی کاربر، کل ساعت‌ها یا میانگین آن‌ها را حساب کند.

main تعداد هفته‌ها را می‌پرسد، آرایه‌ای با همان تعداد خانه می‌سازد و بعد T (کل) یا A (میانگین) را می‌پرسد. کار تو کامل کردن `calc_hours` است.

## خواسته‌های رسمی

1. ابتدا ساعت‌های ذخیره‌شده در آرایه را در یک متغیر تازه جمع بزن.
2. بسته به مقدار `output`، این جمع یا میانگین ساعت‌ها را برگردان.

## شروع کار

ابتدا `cd`، بعد `mkdir hours` و `cd hours`.

فایل آغازین رسمی را دانلود کن:

```bash
wget https://cdn.cs50.net/2022/fall/labs/2/hours.c
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی: میانگین:

```text
hours/ $ ./hours
Number of weeks taking CS50: 3
Week 0 HW Hours: 3
Week 1 HW Hours: 7
Week 2 HW Hours: 10
Enter T for total hours, A for average hours per week: A
6.7 hours
```

نمونهٔ رسمی: کل:

```text
hours/ $ ./hours
Number of weeks taking CS50: 2
Week 0 HW Hours: 2
Week 1 HW Hours: 8
Enter T for total hours, A for average hours per week: T
10.0 hours
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- آرایه — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u02`)
- پیمایش آرایه با حلقه — [یادداشت](/kb/d/w02-n09) · درس کوتاه `w02-l04` (واحد `w02-l04-u03`)
- آرایه به‌عنوان پارامتر تابع — [یادداشت](/kb/d/w02-n10) · درس کوتاه `w02-l05` (واحد `w02-l05-u02`)
- اجزای اعلان تابع: نوع بازگشتی، نام، فهرست آرگومان‌ها — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. صفحهٔ رسمی می‌گوید برای جمع زدن، متغیری را با صفر شروع کن و در حلقه هر خانه را به آن اضافه کن.
2. تقسیم دو int اعشار را دور می‌ریزد؛ یادداشت scores3 را ببین.

## اشتباه‌های رایج

- مقدار اولیه ندادن به متغیر جمع
- تقسیم int بر int
- برگرداندن جمع در هر دو حالت

## چک‌لیست خودآزمایی

1. جمع را با مقدار اولیهٔ صفر شروع کرده‌ام.
2. هر دو حالت T و A را امتحان کرده‌ام.
3. میانگین اعشار درست دارد (6.7 در نمونهٔ رسمی).
4. check50 همه را سبز نشان می‌دهد.
5. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/hours
```

سبک با style50:

```bash
style50 hours.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: استفاده از تابع برای محاسبهٔ ساعت‌ها چه مزیتی دارد؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد آغازین hours.c](https://cdn.cs50.net/2022/fall/labs/2/hours.c): با wget دانلود کن؛ این بسته کد آغازین را تکرار نمی‌کند.

## پیوند رسمی

- [Hours](https://cs50.harvard.edu/x/2026/practice/hours/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
