---
id: pset-1-me
type: pset
title: Hello, It’s Me — Problem Set 1
week: 1
parent: pset-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-forms-get-post
- concept-strings
- concept-variables
- pset-6-hello
source_urls:
- https://cs50.harvard.edu/x/psets/1/me/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:15+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- cs50h
- get-string
- hello-it-s-me
- printf-format-codes
- pset
- variables
checksum: sha256:45c5d3daadddc45eaef581d2ee45970f7eec88ad6b2120dc4ac0f6b1f3701bca
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hello, It’s Me — Problem Set 1

## 1. Source metadata
- **Title:** Hello, It’s Me — Problem Set 1
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/1/me/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:15+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/1/me/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="hello-its-me"></a>

### Hello, It’s Me

[Embedded video: https://www.youtube.com/embed/YQHsXMglC9A](https://www.youtube.com/embed/YQHsXMglC9A)

<a id="problem-to-solve"></a>

#### Problem to Solve

In a file called `hello.c`, in a folder called `me`, implement a program in C that prompts the user for their name and then says hello to that user. For instance, if the user’s name is Adele, your program should print `hello, Adele\n`!

> **Hints** *(collapsible block on the source page)*
>
> * Recall that you can get a `string` from a user with `get_string`, which is declared in `cs50.h`.
> * Recall that you can print a `string` with `printf`, which is declared in `stdio.h`.
> * Recall that you can format a `string` with `printf` with `%s`.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/Jn4egWrG0Rvuzo9d2Rs0qpkcL]

<a id="how-to-begin"></a>

#### How to Begin

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir me
```

to make a folder called `me` in your codespace.

Then execute

```
cd me
```

to change directories into that folder. You should now see your terminal prompt as `me/ $`. You can now execute

```
code hello.c
```

to create a file called `hello.c` in which you can write your code.

<a id="walkthrough"></a>

#### Walkthrough

Here’s a “walkthrough” (i.e., tour) of this problem, if you’d like a verbal overview of what to do too!

[Embedded video: https://www.youtube.com/embed/wSk1KSDUEYA](https://www.youtube.com/embed/wSk1KSDUEYA)

<a id="how-to-test"></a>

#### How to Test

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/me
```

<a id="style"></a>

##### Style

```
style50 hello.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/me
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `me`; files shown on the page: `hello.c`
- check50: `cs50/problems/2026/x/me`
- style50: `hello.c`
- submit50: `cs50/problems/2026/x/me`
- Page sections (order on source): Problem to Solve, Demo, How to Begin, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/YQHsXMglC9A, https://www.youtube.com/embed/wSk1KSDUEYA
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم get_string، printf format codes، variables، cs50.h.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write hello.c in a folder called me that asks the user for their name and greets them, e.g. printing "hello, Adele". It introduces getting a string from the user with the CS50 library and formatting it into output with printf.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Problem Set 1](README.md) (`pset-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Forms, GET and POST](../../../concepts/forms-get-post.md) (`concept-forms-get-post`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Variables](../../../concepts/variables.md) (`concept-variables`)
  - [Hello, Again — Problem Set 6](../../week-06-python/psets/hello.md) (`pset-6-hello`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
اولین برنامه‌ی تعاملی: گرفتن ورودی رشته‌ای و استفاده از آن در خروجی با format code.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. از خودت بپرس: ورودی کاربر کجا ذخیره می‌شود و چه نوعی دارد؟
2. printf چطور می‌فهمد مقدار یک متغیر را کجای متن بگذارد؟ به format codeها در جزوه نگاه کن.
3. کتابخانه‌ای که get_string را تعریف می‌کند باید include شود.

### اشتباه‌های رایج (مفهومی)
- فراموش کردن #include <cs50.h>
- اختلاف جزئی متن خروجی با نمونه

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/me` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/1/me/ — retrieved 2026-10-18T05:11:15+03:30, sha256 `45c5d3daadddc45e…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
