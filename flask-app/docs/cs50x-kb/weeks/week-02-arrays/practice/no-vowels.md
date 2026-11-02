---
id: practice-2-no-vowels
type: practice
title: N0 V0w3ls — Practice
week: 2
parent: week-2
children: []
prerequisites:
- week-2-lecture
related:
- concept-command-line-arguments
- concept-conditionals
- concept-strings
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/no-vowels/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:53+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- command-line-arguments
- n0-v0w3ls
- practice
- strings
- switch-conditionals
checksum: sha256:ffd6fa9d5c7b0dee7d20e64c941781243de6910f33f33ae675b1a3af634ba519
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# N0 V0w3ls — Practice

## 1. Source metadata
- **Title:** N0 V0w3ls — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/no-vowels/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:53+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/no-vowels/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="n0-v0w3ls"></a>

### N0 V0w3ls

<a id="learning-goals"></a>

#### Learning Goals

* Practice using strings
* Practice using command-line arguments
* Write a program entirely from scratch

![leetspeak](https://cs50.harvard.edu/x/practice/no-vowels/leetspeak-t.jpeg)

<a id="background"></a>

#### Background

If you’ve been on the internet, you might have seen [“leetspeak”](https://en.wikipedia.org/wiki/Leet) (or “l33tsp36k” for our purposes!), which involves the substitution of symbols for alphabetical characters, where those symbols somewhat resemble their alphabetical counterparts. In this lab, you’ll write a program to replace certain vowels with digits!

Up until now, you’ve frequently written programs for which you’ve been provided distribution code. You’ll notice when downloading the “distro” for this problem, you start with nothing more than a couple of commonly used libraries and an empty `main` function. In this problem, you will convert a word, which you will input at the command line, to a corresponding word with numbers replacing vowels.

* Hints
  * Do note that the `main` function in the distribution code uses `argc` and `argv`. Be sure to use these!
  * Be sure to check for the correct number of command-line arguments before doing anything else in your `main` function.

<a id="demo"></a>

#### Demo

![no-vowelsGif](https://cs50.harvard.edu/x/practice/no-vowels/no-vowelsDemo.gif)

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir no-vowels`
4. Now execute `cd no-vowels`
5. Then copy and paste `wget https://cdn.cs50.net/2022/fall/labs/2/no-vowels.c` into your terminal to download this lab’s distribution code.

<a id="implementation-details"></a>

#### Implementation Details

* Implement your program in a file called `no-vowels.c` in a directory called `no-vowels`.
* Your program must accept a single command-line argument, which will be the word that you want to convert.
* If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with `printf`) and `return` from `main` a value of 1 (which tends to signify an error) immediately.
* Your program must contain a function called `replace` which takes a `string` input and returns a `string` output.
* This function will change the following vowels to numbers: `a` becomes `6`, `e` becomes `3`, `i` becomes `1`, `o` becomes `0` and `u` does not change.
* The input parameter for the `replace` function will be `argv[1]` and the return value is the converted word.
* The main function will then print the converted word, followed by `\n`.
* You may want to try using the [`switch` statement](https://cs50.readthedocs.io/style/c/#switches) in your `replace` function.

<a id="thought-question"></a>

#### Thought Question

Why might you want to use command-line arguments rather than `get_string`, `get_int`, etc?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
no-vowels/ $ ./no-vowels
Usage: ./no-vowels word
```

```
no-vowels/ $ ./no-vowels hello
h3ll0
```

```
no-vowels/ $ ./no-vowels pseudocode
ps3ud0c0d3
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/no-vowels
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the `$` prompt.

```
style50 no-vowels.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem completed with your lab.

### Distribution code inventory (downloaded files)

#### Distribution files downloaded individually (linked on the page)

| File | Bytes | Stored in KB |
|---|---:|---|
| `https://cdn.cs50.net/2022/fall/labs/2/no-vowels.c` | 224 | [yes](no-vowels-distribution/files/no-vowels.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `no-vowels`; files shown on the page: `no-vowels.c`
- check50: `cs50/labs/2023/x/no-vowels`
- style50: `no-vowels.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم strings، command-line arguments، switch/conditionals.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write from scratch a program that converts a word given on the command line into 'leetspeak' by replacing certain vowels with digits.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 2 — Arrays](../week.md) (`week-2`)
- **Prerequisites (generated):** [Week 2 — Lecture notes (Arrays)](../lecture.md) (`week-2-lecture`)
- **Related:**
  - [Command-Line Arguments (argc, argv)](../../../concepts/command-line-arguments.md) (`concept-command-line-arguments`)
  - [Conditionals and Boolean Expressions](../../../concepts/conditionals.md) (`concept-conditionals`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین آرگومان خط فرمان و پیمایش رشته.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. هر کاراکتر رشته را بررسی کن و تصمیم بگیر با آن چه کنی.
2. اگر تعداد آرگومان‌ها درست نبود چه باید کرد؟

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/no-vowels` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/no-vowels/ — retrieved 2026-10-18T05:10:53+03:30, sha256 `ffd6fa9d5c7b0dee…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
