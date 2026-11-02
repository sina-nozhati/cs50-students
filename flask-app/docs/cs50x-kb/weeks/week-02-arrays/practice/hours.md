---
id: practice-2-hours
type: practice
title: Hours — Practice
week: 2
parent: week-2
children: []
prerequisites:
- week-2-lecture
related:
- concept-arrays
- concept-data-types
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/hours/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:52+03:30'
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
- arrays-as-parameters
- hours
- integer-division
- practice
- type-casting
checksum: sha256:c5d13dec2b0612427dd4a8cc8b301b2af11e28cdde539ac00f2700ab8c92dd9f
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hours — Practice

## 1. Source metadata
- **Title:** Hours — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/hours/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:52+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/hours/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="hours"></a>

### Hours

<a id="learning-goals"></a>

#### Learning Goals

* Practice using arrays
* Using an array as a parameter to a function
* Adding values in a loop
* Integer division and type casting

![OfficeHours](https://cs50.harvard.edu/x/practice/hours/officehours.jpeg)

<a id="background"></a>

#### Background

Suppose you’re taking CS50 (if you’re reading this you probably are!) and spending time every week on each problem set. You may be wondering how many hours you’ve spent learning computer science, on average or in total! In this program, you’ll complete a function that calculates, based on a user’s input, a total number of hours *or* an average number of hours across a given number of days.

* Hints
  * To add up numbers in an array, you might first want to initialize a variable to zero. After, you’ll want to use a loop that adds each value in the array to that variable.
  * Be sure to pay attention to what happens if you divide two `int`s when calculating the average!

<a id="demo"></a>

#### Demo

![HoursGif](https://cs50.harvard.edu/x/practice/hours/hoursDemo.gif)

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir hours`
4. Now execute `cd hours`
5. Then copy and paste `wget https://cdn.cs50.net/2022/fall/labs/2/hours.c` into your terminal to download this lab’s distribution code.

<a id="implementation-details"></a>

#### Implementation Details

The `main` function prompts the user for the number of weeks a user has been taking CS50, then creates an array with as many elements. Notice that, after retrieving some data, the program prompts the user to type in either “T” or “A”—”T” should (but doesn’t yet!) print the total number of hours the user entered, while “A” should (but doesn’t yet!) print the average hours the user entered. Notice that the `do while` loop uses `toupper` to capitalize the letter that’s input before it is saved in the variable `output`. Then, the `printf` function calls `calc_hours`. Note the syntax involved when passing an array to a function.

To complete `calc_hours`, first total up the hours saved in the array into a new variable. Then, depending on the value of `output`, return either this sum, or the average number of hours.

<a id="thought-question"></a>

#### Thought Question

* What is the advantage of using a function to calculate hours?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
hours/ $ ./hours
Number of weeks taking CS50: 3
Week 0 HW Hours: 3
Week 1 HW Hours: 7
Week 2 HW Hours: 10
Enter T for total hours, A for average hours per week: A
6.7 hours
```

```
hours/ $ ./hours
Number of weeks taking CS50: 2
Week 0 HW Hours: 2
Week 1 HW Hours: 8
Enter T for total hours, A for average hours per week: T
10.0 hours
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/hours
```

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 hours.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem completed with your lab.

### Distribution code inventory (downloaded files)

#### Distribution files downloaded individually (linked on the page)

| File | Bytes | Stored in KB |
|---|---:|---|
| `https://cdn.cs50.net/2022/fall/labs/2/hours.c` | 654 | [yes](hours-distribution/files/hours.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `None`; files shown on the page: `hours.c`
- check50: `cs50/labs/2023/x/hours`
- style50: `hours.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم arrays، arrays as parameters، integer division، type casting.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete a function that computes the total or average hours spent per week from user-entered values stored in an array.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 2 — Arrays](../week.md) (`week-2`)
- **Prerequisites (generated):** [Week 2 — Lecture notes (Arrays)](../lecture.md) (`week-2-lecture`)
- **Related:**
  - [Arrays](../../../concepts/arrays.md) (`concept-arrays`)
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین آرایه‌ها و میانگین/مجموع.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. داده‌ها را در آرایه جمع کن و سپس بر اساس انتخاب کاربر محاسبه را انجام بده.
2. نوع داده‌ی میانگین چیست؟

### اشتباه‌های رایج (مفهومی)
- تقسیم صحیح

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/hours` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/hours/ — retrieved 2026-10-18T05:10:52+03:30, sha256 `c5d13dec2b061242…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
