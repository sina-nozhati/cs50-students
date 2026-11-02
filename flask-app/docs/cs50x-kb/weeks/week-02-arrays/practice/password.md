---
id: practice-2-password
type: practice
title: Password — Practice
week: 2
parent: week-2
children: []
prerequisites:
- week-2-lecture
related:
- concept-conditionals
- concept-data-types
- concept-strings
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/password/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:54+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- booleans
- ctypeh
- password
- practice
- string-iteration
checksum: sha256:94e27d5e8d5d1907d18ffc8a06e44d8af3296c9a66a813f93fc4d89e60c2f54c
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Password — Practice

## 1. Source metadata
- **Title:** Password — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/password/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:54+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/password/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="password"></a>

### Password

<a id="learning-goals"></a>

#### Learning Goals

* Practice iterating through a string
* Practice using the `ctype` library
* Practice using Boolean variables

<a id="background"></a>

#### Background

[Embedded video: https://www.youtube.com/embed/B-NhD15ocwA](https://www.youtube.com/embed/B-NhD15ocwA)

If this video is blocked in your country, don’t worry, as it is not required to solve the problem. It’s a humorous clip about passwords from the movie Spaceballs.

As we all know by now, it’s important to use passwords that are not easy to guess! Many web apps now require passwords that require not only alphabetical characters, but also number and symbols.

In this lab, the user is prompted for a password, which will then be validated using a function `check` that you will complete. If the password contains at least one upper case letter, one lower case letter, a number, and a symbol (meaning a printable character that’s not a letter or number, such as ‘!’, ‘$’ and ‘#’), the function should return `true`. If not it should return `false`.

> **Hints** *(collapsible block on the source page)*
>
> 1. The `ctype` library has many useful functions that can come in handy here.
> 2. Boolean variables can keep track of whether each criteria in an algorithm is valid.

<a id="demo"></a>

#### Demo

![PasswordGif](https://cs50.harvard.edu/x/practice/password/passwordDemo.gif)

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir password`
4. Now execute `cd password`
5. Then copy and paste `wget https://cdn.cs50.net/2022/fall/labs/2/password.c` into your terminal to download this lab’s distribution code.
6. You are to complete the function, `valid`, which returns `true` if the password passes all criteria, and `false` if it does not.

<a id="implementation-details"></a>

#### Implementation Details

Your function will iterate through the password that’s supplied to it as an argument. Since you have to find at least one lower case letter, one upper case letter, one number and one symbol, you may want to create a boolean variable for each and set each to `false` before you iterate through the string. If you then find a number, for instance you can set that boolean to `true`. If all booleans are `true` at the end of the function, it means all criteria are met, and you would return `true`.

<a id="thought-question"></a>

#### Thought Question

* How many different passwords do you think can be made that are 8 letters long, can use any of 95 printable ASCII characters?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
password/ $ ./password
Enter your password: hello
Your password needs at least one uppercase letter, lowercase letter, number and symbol!
```

```
password/ $ ./password
Enter your password: h3ll(
Your password needs at least one uppercase letter, lowercase letter, number and symbol!
```

```
password/ $ ./password
Enter your password: h3LL0!
Your password is valid!
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the $ prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/password
```

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 password.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem completed with your lab.

### Distribution code inventory (downloaded files)

#### Distribution files downloaded individually (linked on the page)

| File | Bytes | Stored in KB |
|---|---:|---|
| `https://cdn.cs50.net/2022/fall/labs/2/password.c` | 625 | [yes](password-distribution/files/password.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `None`; files shown on the page: `password.c`
- check50: `cs50/labs/2023/x/password`
- style50: `password.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/B-NhD15ocwA
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم string iteration، ctype.h، Booleans.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete a check function that returns true only if a password contains an uppercase letter, a lowercase letter, a digit and a symbol.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 2 — Arrays](../week.md) (`week-2`)
- **Prerequisites (generated):** [Week 2 — Lecture notes (Arrays)](../lecture.md) (`week-2-lecture`)
- **Related:**
  - [Conditionals and Boolean Expressions](../../../concepts/conditionals.md) (`concept-conditionals`)
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین توابع ctype.h و پرچم‌های بولی.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. برای هر نوع کاراکتر لازم، یک متغیر بولی در نظر بگیر.
2. توابع کتابخانه‌ی ctype.h را در manual.cs50.io مرور کن.

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/password` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/password/ — retrieved 2026-10-18T05:10:54+03:30, sha256 `94e27d5e8d5d1907…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
