---
id: practice-1-debug
type: practice
title: Debug — Practice
week: 1
parent: week-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-compiling
- concept-debugging
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/debug/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:49+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- c-syntax
- compiler-errors
- debug
- debugging
- practice
checksum: sha256:0ee1de5ad7da5722024abe6be14baee67c868543119c38b8d3a5b86bf9753679
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Debug — Practice

## 1. Source metadata
- **Title:** Debug — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/debug/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:49+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/debug/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="debug"></a>

### Debug

<a id="learning-goals"></a>

#### Learning Goals

* Become familiar with C syntax
* Learn what C compiler error messages mean
* Get practice debugging

![debugging](https://cs50.harvard.edu/x/practice/debug/first_bug.jpg)

<a id="background"></a>

#### Background

There are two kinds of errors that can occur when writing a program. The first errors you are likely to encounter are **syntactical** errors. In addition to syntactical errors, there can also be logical errors, which we’ll take a look at soon.

In computer science, syntax is important for a computer to understand what you are telling it to do. Each programming language has its own syntactical rules, which include the combination of both words and punctuation.

This lab starts with distribution code which has several syntactical errors. The idea is for you to try to compile (`make`) the program, learn to interpret the rather cryptic error messages output by the compiler, and **debug** the program.

* Hints
  * You’ll probably see the first error after trying to compile `debug.c` will be `debug.c:9:5: error: use of undeclared identifier 'name'`. The `9` after `debug.c:` means there is a problem on line 9. Why do you think is says `undeclared identifier`?
  * You may want to look for errors such as missing symbols, missing libraries, missing variable declarations.
  * If you are still stuck, look just below the error: `help50` will offer a hint in yellow if it recognizes it, or a **help50** button atop your terminal window that you can click to ask the duck about it.

<a id="demo"></a>

#### Demo

![DebugGif](https://cs50.harvard.edu/x/practice/debug/debugDemo.gif)

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir debug`
4. Now execute `cd debug`
5. Then copy and paste `wget https://cdn.cs50.net/2022/fall/labs/1/debug.c` into your terminal to download this lab’s distribution code.
6. Now try compiling this program, by typing `make debug` and see what happens!
7. You most likely see an error that says: `debug.c:9:5: error: use of undeclared identifier 'name'`
8. This means there is an error that has something to do with an “undeclared identifier”, on line 9. Fix this bug, and then try to compile again. Keep in mind that debugging is an iterative process. You may need to fix an error, compile, then fix another error, compile again, multiple times!

<a id="thought-question"></a>

#### Thought Question

* Why do you think C (as well as other programming languages) have such specific rules regarding syntax?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
debug/ $ ./debug
What is your name? Carter
Where do you live? Cambridge
Hello, Carter, from Cambridge!
```

```
debug/ $ ./debug
What is your name? Margaret
Where do you live? New York
Hello, Margaret, from New York!
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the $ prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/debug
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the `$` prompt.

```
style50 debug.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem.

### Distribution code inventory (downloaded files)

#### Distribution files downloaded individually (linked on the page)

| File | Bytes | Stored in KB |
|---|---:|---|
| `https://cdn.cs50.net/2022/fall/labs/1/debug.c` | 315 | [yes](debug-distribution/files/debug.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `None`; files shown on the page: `debug.c`
- check50: `cs50/labs/2023/x/debug`
- style50: `debug.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم debugging، compiler errors، C syntax.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Fix the syntax errors in provided C code (debug.c) by compiling it and interpreting compiler error messages.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 1 — C](../week.md) (`week-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Compiling (preprocessing, compiling, assembling, linking)](../../../concepts/compiling.md) (`concept-compiling`)
  - [Debugging (printf, debug50, rubber duck)](../../../concepts/debugging.md) (`concept-debugging`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین خواندن پیام‌های خطای کامپایلر و رفع اشکال.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. پیام خطا را از اولین خطا شروع به خواندن کن؛ شماره‌ی خط را ببین.
2. help50 یا ابزار اشکال‌زدایی را برای فهم پیام‌ها امتحان کن.

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/debug` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/debug/ — retrieved 2026-10-18T05:10:49+03:30, sha256 `0ee1de5ad7da5722…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
