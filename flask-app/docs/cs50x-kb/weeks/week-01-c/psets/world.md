---
id: pset-1-world
type: pset
title: Hello, World — Problem Set 1
week: 1
parent: pset-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-compiling
source_urls:
- https://cs50.harvard.edu/x/psets/1/world/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:14+03:30'
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
- codespace-setup
- compiling-with-make
- hello-world
- printf
- pset
checksum: sha256:618f284019528288334c8f3d6afca72170db2729cd90c720ecc8a1f36f5766a3
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hello, World — Problem Set 1

## 1. Source metadata
- **Title:** Hello, World — Problem Set 1
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/1/world/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:14+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/1/world/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="hello-world"></a>

### Hello, World

[Embedded video: https://www.youtube.com/embed/ufB53UE2Cvo](https://www.youtube.com/embed/ufB53UE2Cvo)

<a id="problem-to-solve"></a>

#### Problem to Solve

Thanks to Professor [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) (who taught CS50 when David took it!), “hello, world” has been implemented in hundreds of languages. Let’s add your implementation to the list!

In a file called `hello.c`, in a folder called `world`, implement a program in C that prints `hello, world\n`, and that’s it!

> **Hint** *(collapsible block on the source page)*
>
> Here’s the actual code you should write! (Quite the hint, huh?) Best to type it yourself, though, rather than copy/paste, so that you start to develop some “muscle memory” for writing code.
>
> ```c
> #include <stdio.h>
>
> int main(void)
> {
>     printf("hello, world\n");
> }
> ```

<a id="demo"></a>

#### Demo

Here’s a demo of what should happen when you compile and execute your program.

[Terminal demo recording (asciinema): https://asciinema.org/a/C5rag3703OZpKxGJ6dSwHnUEF]

<a id="how-to-begin"></a>

#### How to Begin

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir world
```

to make a folder called `world` in your codespace.

Then execute

```
cd world
```

to change directories into that folder. You should now see your terminal prompt as `world/ $`. You can now execute

```
code hello.c
```

to create a file called `hello.c` in which you can write your code.

<a id="how-to-test"></a>

#### How to Test

Recall that you can compile `hello.c` with:

```
make hello
```

If you don’t see an error message, it compiled successfully! You can confirm as much with

```
ls
```

which should list not only `hello.c` (which is source code) but also `hello` (which is machine code).

If you do see an error message, try to fix your code and try to compile it again. If you don’t understand the error message, though, look just below it: `help50` will offer a hint in yellow if it recognizes the error, or a **help50** button atop your terminal window that you can click to ask the duck about it.

Once your code compiles successfully, you can execute your program with:

```
./hello
```

<a id="correctness"></a>

##### Correctness

Execute the below to evaluate the correctness of your code using `check50`, a command-line program that will output happy faces whenever your code passes CS50’s automated tests and sad faces whenever it doesn’t!

```
check50 cs50/problems/2026/x/world
```

<a id="style"></a>

##### Style

Execute the below to evaluate the style of your code using `style50`, a command-line program that will output additions (in green) and deletions (in red) that you should make to your program in order to improve its style. If you have trouble seeing those colors, `style50` supports other [modes](https://cs50.readthedocs.io/style50/) too!

```
style50 hello.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit this one! Just a practice exercise!

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `world`; files shown on the page: `hello.c`
- check50: `cs50/problems/2026/x/world`
- style50: `hello.c`
- submit50: not stated
- Page sections (order on source): Problem to Solve, Demo, How to Begin, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/ufB53UE2Cvo
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم C syntax، printf، compiling with make، codespace setup.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write the classic first C program, hello.c in a folder called world, that prints "hello, world" followed by a newline. The page gives the exact code and suggests typing it by hand to build muscle memory. It is mainly a check that the codespace, make and check50 work. The pset page says to 'Complete' it, and its page says it need not be submitted.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Problem Set 1](README.md) (`pset-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Compiling (preprocessing, compiling, assembling, linking)](../../../concepts/compiling.md) (`concept-compiling`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
آشنایی با محیط VS Code، ترمینال، کامپایل و اجرای اولین برنامه‌ی C.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. ترتیب کار را دنبال کن: ساختن فایل، نوشتن، کامپایل با make، اجرا.
2. اگر کامپایلر خطا داد، اولین خطا را از بالا بخوان؛ معمولاً بقیه از آن ناشی می‌شوند.
3. به نام فایل و پوشه دقت کن؛ check50 به آن‌ها حساس است.

### اشتباه‌های رایج (مفهومی)
- اجرای make در پوشه‌ی اشتباه
- فراموش کردن \n در انتهای خروجی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/world` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/1/world/ — retrieved 2026-10-18T05:11:14+03:30, sha256 `618f284019528288…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
