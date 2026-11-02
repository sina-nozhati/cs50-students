---
id: practice-1-half
type: practice
title: Half — Practice
week: 1
parent: week-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-data-types
- concept-functions
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/half/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:50+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- data-types
- functions-with-parameters-return
- half
- practice
- type-casting
checksum: sha256:095c5ab4b6e264af1d2217a5da6d4ba58be5d483eee800490879d9d7e69ea6f4
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Half — Practice

## 1. Source metadata
- **Title:** Half — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/half/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:50+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/half/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="half"></a>

### Half

<a id="learning-goals"></a>

#### Learning Goals

* Work with different data types
* Practice type casting
* Use math operations
* Create a function with input parameters and return value

[Embedded video: https://www.youtube.com/embed/EYb9jnt2cv4](https://www.youtube.com/embed/EYb9jnt2cv4)

<a id="background"></a>

#### Background

Suppose you are eating out at a restaurant with a friend and want to split the bill evenly. You may want to anticipate the amount you’ll owe before the bill arrives with tax added. In this problem, you’ll complete a function to calculate the amount each of you owes based on the bill amount, the tax, and the tip.

* Hints
  * Note that the tax and tip are input as percents. You may want to change these to decimal values before calculating the total.
  * Since the tip is input as an `int`, keep in mind that if you divide an `int` by an `int` you’ll get back an `int`!
  * Order of operations here is exactly the same as in algebra, where multiplcation and division are performed before addition and subtraction.

<a id="demo"></a>

#### Demo

![DebugGif](https://cs50.harvard.edu/x/practice/half/halfDemo.gif)

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir half`
4. Now execute `cd half`
5. Then copy and paste `wget https://cdn.cs50.net/2022/fall/labs/1/half.c` into your terminal to download this lab’s distribution code.
6. You are to complete the function, `half`, which calculates exactly half of the bill after tax and tip are added, and returns that value.

<a id="implementation-details"></a>

#### Implementation Details

Your function should use the input parameters, `bill`, `tax`, and `tip`, to calculate the final amount. However, since these values are percentages, you’ll have to do some work to convert these to more appropriate formats to use for your calculation.

The tax should be added to the bill amount *before* calculating the tip. Finally, you will return exactly half of the full amount, including the bill amount, the tax and the tip.

<a id="thought-question"></a>

#### Thought Question

* Why do you think there are different data types in C?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
half/ $ ./half
Bill before tax and tip: 12.50
Sale Tax Percent: 8.875
Tip percent: 20
You will owe $8.17 each!
```

```
half/ $ ./half
Bill before tax and tip: 23.50
Sale Tax Percent: 7  
Tip percent: 15
You will owe $14.46 each!
```

```
half/ $ ./half
Bill before tax and tip: 100
Sale Tax Percent: 6.25
Tip percent: 18
You will owe $62.69 each!
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/half
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the `$` prompt.

```
style50 half.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem.

### Distribution code inventory (downloaded files)

#### Distribution files downloaded individually (linked on the page)

| File | Bytes | Stored in KB |
|---|---:|---|
| `https://cdn.cs50.net/2022/fall/labs/1/half.c` | 575 | [yes](half-distribution/files/half.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `None`; files shown on the page: `half.c`
- check50: `cs50/labs/2023/x/half`
- style50: `half.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/EYb9jnt2cv4
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم data types، type casting، functions with parameters/return.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete a function that computes each person's share of a restaurant bill after tax and tip, splitting it in half.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 1 — C](../week.md) (`week-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین توابع، پارامترها و انواع اعشاری.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. ترتیب محاسبه‌ی مالیات و انعام را از صورت مسئله دقیق بخوان.
2. مراقب تبدیل درصد به عدد اعشاری و تقسیم صحیح باش.

### اشتباه‌های رایج (مفهومی)
- تقسیم صحیح ناخواسته

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/half` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/half/ — retrieved 2026-10-18T05:10:50+03:30, sha256 `095c5ab4b6e264af…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
