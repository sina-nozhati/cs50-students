---
id: practice-3-max
type: practice
title: Max — Practice
week: 3
parent: week-3
children: []
prerequisites:
- week-3-lecture
related:
- concept-arrays
- concept-functions
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/max/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:57+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- arrays
- functions
- linear-scan
- max
- practice
checksum: sha256:93831c36eef62d5312c1a10eb23600bc2d284c565ce7ffa953f50eff99375c58
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Max — Practice

## 1. Source metadata
- **Title:** Max — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/max/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:57+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/max/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="max"></a>

### Max

<a id="learning-goals"></a>

#### Learning Goals

* Pass an array into a function
* Create a helper function that finds a maximum value

<a id="background"></a>

#### Background

There are many situations where you’ll find it helpful to have a function that finds the maximum (and minimum) value in an array. Since there is no built-in `max` function in `C`, you’ll create one in this practice problem. You can then use it in upcoming problem sets where it may be helpful!

* Hints
  * Start out with a variable that keeps track of your max value. There are two ways to initialize this. You can start out using the lowest possible value (be careful you don’t start with zero, as the max value could be a negative number!) or you can start with the first element in the array.
  * Loop through the array and reset this max value every time you find a value that’s larger.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/TSe2Z5ZlnpuN3Od14jNKerLqM]

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/3/max.zip` followed by Enter in order to download a zip called `max.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip max.zip` to create a folder called `max`.
5. You no longer need the ZIP file, so you can execute `rm max.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

The `main` function initializes the array, asks the user to enter values, and then passes the array and the number of items to the `max` function. Complete the `max` function by iterating through every element in the array, and return the maximum value.

<a id="thought-question"></a>

#### Thought Question

* What types of programs can you think of that might benefit from a `max` helper function?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
max/ $ ./max
Number of elements: 3
Element 0: 2
Element 1: 10
Element 2: -1
The max value is 10.
```

```
max/ $ ./max
Number of elements: 4
Element 0: -100
Element 1: -200
Element 2: -3
Element 3: -5000
The max value is -3.
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/max
```

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 max.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/3/max.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `max/max.c` | 470 | [yes](max-distribution/files/max/max.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `max`; files shown on the page: `max.c`
- check50: `cs50/labs/2023/x/max`
- style50: `max.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم arrays، functions، linear scan.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write a max function that returns the largest value in an array of ints, since C has no built-in max.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 3 — Algorithms](../week.md) (`week-3`)
- **Prerequisites (generated):** [Week 3 — Lecture notes (Algorithms)](../lecture.md) (`week-3-lecture`)
- **Related:**
  - [Arrays](../../../concepts/arrays.md) (`concept-arrays`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین پیمایش آرایه و پیدا کردن بیشینه.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. مقدار اولیه‌ی «بیشینه تا این لحظه» را چه بگذاریم؟

### اشتباه‌های رایج (مفهومی)
- مقداردهی اولیه‌ی صفر برای آرایه‌های منفی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/max` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/max/ — retrieved 2026-10-18T05:10:57+03:30, sha256 `93831c36eef62d53…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
