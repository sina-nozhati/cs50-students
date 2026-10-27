---
id: practice-1-prime
type: practice
title: Prime — Practice
week: 1
parent: week-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-conditionals
- concept-functions
- concept-loops
- concept-operators
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/prime/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:51+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- boolean-functions
- for-loops
- modulo
- practice
- prime
checksum: sha256:2452736d8793a98a98de79964ca5bd1e39d67ea05fdf6ad37e67567cb0d402fc
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Prime — Practice

## 1. Source metadata
- **Title:** Prime — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/prime/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:51+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/prime/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="prime"></a>

### Prime

<a id="learning-goals"></a>

#### Learning Goals

* Practice using `for` loops
* Using modulo
* Creating a Boolean function

![prime-numbers](https://cs50.harvard.edu/x/practice/prime/prime-numbers.jpg)

<a id="background"></a>

#### Background

[Prime numbers](https://en.wikipedia.org/wiki/Prime_number) are defined as whole numbers greater than 1, whose only factors are 1 and itself. So 3 is prime because its only factors are 1 and 3, while 4 is composite and not prime, because it is the product of 2 × 2. In this lab you will write an algorithm to generate all prime numbers in a range specified by the user.

* Hints
  * Modulo may come in handy, as it produces the remainder when dividing two integers.
  * By definition, 1 is not a prime number.
  * There is only one even prime number, 2.

<a id="demo"></a>

#### Demo

![PrimeGif](https://cs50.harvard.edu/x/practice/prime/primeDemo.gif)

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir prime`
4. Now execute `cd prime`
5. Then copy and paste `wget https://cdn.cs50.net/2022/fall/labs/1/prime.c` into your terminal to download this lab’s distribution code.
6. You are to complete the Boolean function, `prime`, which tests if a number is prime, and returns true if it is, and false if it is not.

<a id="implementation-details"></a>

#### Implementation Details

The easiest way to check if a number is prime, is to try dividing it by every number from 2 up to, but not including, the number itself. If any number divides into it with no remainder, that number is not prime.

The `main` function in the distribution code contains a `for` loop that iterates through the range specified by the user, with both ends inclusive. For example, if the user types in `1` for `min` and `100` for `max`, the `for` loop will test each number, 1 to 100. Each of these numbers is passed to a function, `prime`, that you will implement to return either `true` or `false` depending on whether the number is prime.

<a id="thought-question"></a>

#### Thought Question

* Can you make the prime-finding algorithm more efficient than checking if a number is divisible by every number between 2 and 1 less than itself? Can you think of another way to generate prime numbers?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
prime/ $ ./prime
Minimum: 1
Maximum: 100
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/prime
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the `$` prompt.

```
style50 prime.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem.

### Distribution code inventory (downloaded files)

#### Distribution files downloaded individually (linked on the page)

| File | Bytes | Stored in KB |
|---|---:|---|
| `https://cdn.cs50.net/2022/fall/labs/1/prime.c` | 485 | [yes](prime-distribution/files/prime.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `None`; files shown on the page: `prime.c`
- check50: `cs50/labs/2023/x/prime`
- style50: `prime.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم for loops، modulo، Boolean functions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete a Boolean function so the program prints all prime numbers in a user-given range.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 1 — C](../week.md) (`week-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Conditionals and Boolean Expressions](../../../concepts/conditionals.md) (`concept-conditionals`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Loops](../../../concepts/loops.md) (`concept-loops`)
  - [Operators](../../../concepts/operators.md) (`concept-operators`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین حلقه‌ها و عملگر باقیمانده برای تشخیص اعداد اول.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. تعریف عدد اول را به یک شرط قابل‌بررسی تبدیل کن.
2. برای هر عدد، چه مقسوم‌علیه‌هایی را باید بررسی کرد؟

### اشتباه‌های رایج (مفهومی)
- در نظر گرفتن ۱ به‌عنوان عدد اول

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/prime` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/prime/ — retrieved 2026-10-18T05:10:51+03:30, sha256 `2452736d8793a98a…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
