---
id: pset-1-mario-less
type: pset
title: Mario (less comfortable) — Problem Set 1
week: 1
parent: pset-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-algorithms-and-pseudocode
- concept-functions
- concept-loops
- pset-1-mario-more
- pset-6-mario-less
source_urls:
- https://cs50.harvard.edu/x/psets/1/mario/less/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:16+03:30'
review_status: verified-against-source
difficulty: less comfortable
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- do-while-loops
- functions
- input-validation
- mario
- nested-for-loops
- pset
- pseudocode
checksum: sha256:de49c5021ee63ae4af23e711e1898871f0e926bacaebf475725c92afedf16cb2
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Mario (less comfortable) — Problem Set 1

## 1. Source metadata
- **Title:** Mario (less comfortable) — Problem Set 1
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/1/mario/less/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/1/mario/less/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="mario"></a>

### Mario

[Embedded video: https://www.youtube.com/embed/cWOkHQXw0JQ](https://www.youtube.com/embed/cWOkHQXw0JQ)

<a id="problem-to-solve"></a>

#### Problem to Solve

Toward the end of World 1-1 in Nintendo’s [Super Mario Bros.](https://en.wikipedia.org/wiki/Super_Mario_Bros.), Mario must ascend right-aligned pyramid of bricks, as in the below.

![screenshot of Mario jumping up a right-aligned pyramid](https://cs50.harvard.edu/x/psets/1/mario/less/pyramid.png)

In a file called `mario.c` in a folder called `mario-less`, implement a program in C that recreates that pyramid, using hashes (`#`) for bricks, as in the below:

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

But prompt the user for an `int` for the pyramid’s actual height, so that the program can also output shorter pyramids like the below:

```
  #
 ##
###
```

Re-prompt the user, again and again as needed, if their input is not greater than 0 or not an `int` altogether.

> **Hints** *(collapsible block on the source page)*
>
> * Recall that you can get an `int` from a user with `get_int`, which is declared in `cs50.h`.
> * Recall that you can print a `string` with `printf`, which is declared in `stdio.h`.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/WPrv7PFVLaLkJ2BU96uTEQKuA]

<a id="advice"></a>

#### Advice

> **Write some code that you know will compile** *(collapsible block on the source page)*
>
> Even though this program won’t do anything, it should at least compile with `make`!
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int main(void)
> {
>
> }
> ```

> **Write some pseudocode before writing more code** *(collapsible block on the source page)*
>
> If unsure how to solve the problem itself, break it down into smaller problems that you can probably solve first. For instance, this problem is really two problems:
>
> 1. Prompt the user for the pyramid’s height
> 2. Print a pyramid of that height
>
> So write some pseudocode as comments that remind you to do just that:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>
>     // Print a pyramid of that height
> }
> ```

> **Convert the pseudocode to code** *(collapsible block on the source page)*
>
> First, consider how you might prompt the user for the pyramid’s height. Recall that a `do while` loop is helpful when you want to do something at least once, and possibly again and again, as in the below:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>     int n;
>     do
>     {
>         n = get_int("Height: ");
>     }
>     while (n < 1);
>
>     // Print a pyramid of that height
> }
> ```
>
> Second, consider how you might print a pyramid of that height, from top to bottom. Notice how the first row should have one brick, the second row should have two bricks, and so on. Odds are you’ll want a loop, as in the below, even if not (yet!) sure what to put in that loop. So add some more pseudocode as a comment for now:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>     int n;
>     do
>     {
>         n = get_int("Height: ");
>     }
>     while (n < 1);
>
>     // Print a pyramid of that height
>     for (int i = 0; i < n; i++)
>     {
>         // Print row of bricks
>     }
> }
> ```
>
> How to print that row of bricks? Well, wouldn’t it be nice if there were a function called `print_row` that could do just that? Let’s suppose that there is:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> void print_row(int bricks);
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>     int n;
>     do
>     {
>         n = get_int("Height: ");
>     }
>     while (n < 1);
>
>     // Print a pyramid of that height
>     for (int i = 0; i < n; i++)
>     {
>         // Print row of bricks
>     }
> }
>
> void print_row(int bricks)
> {
>     // Print row of bricks
> }
> ```
>
> We could then call that function from `main`, as in the below:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> void print_row(int bricks);
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>     int n;
>     do
>     {
>         n = get_int("Height: ");
>     }
>     while (n < 1);
>
>     // Print a pyramid of that height
>     for (int i = 0; i < n; i++)
>     {
>         // Print row of bricks
>         print_row(i + 1);
>     }
> }
>
> void print_row(int bricks)
> {
>     // Print row of bricks
> }
> ```
>
> Why `i + 1`, though?
>
> Let’s now implement `print_row`:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> void print_row(int bricks);
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>     int n;
>     do
>     {
>         n = get_int("Height: ");
>     }
>     while (n < 1);
>
>     // Print a pyramid of that height
>     for (int i = 0; i < n; i++)
>     {
>         // Print row of bricks
>         print_row(i + 1);
>     }
> }
>
> void print_row(int bricks)
> {
>     for (int i = 0; i < bricks; i++)
>     {
>         printf("#");
>     }
>     printf("\n");
> }
> ```
>
> Why the `\n` at the end, though?
>
> Unfortunately, this code prints a left-aligned pyramid, but you need a right-aligned one! Perhaps we should print some blank spaces before some of the bricks, to move them to the right? Let’s change `print_row` as follows so that it can print both:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> void print_row(int spaces, int bricks);
>
> int main(void)
> {
>     // Prompt the user for the pyramid's height
>     int n;
>     do
>     {
>         n = get_int("Height: ");
>     }
>     while (n < 1);
>
>     // Print a pyramid of that height
>     for (int i = 0; i < n; i++)
>     {
>         // Print row of bricks
>     }
> }
>
> void print_row(int spaces, int bricks)
> {
>     // Print spaces
>
>     // Print bricks
> }
> ```
>
> Some pseudocode now remains in both `main` and `print_row`, so that we leave to you!
>
> And consider whether you could factor out some of the code in `main` to a `get_height` function, too, that returns the `int` you need!

<a id="walkthrough"></a>

#### Walkthrough

Note this walkthrough specifies your program should prompt the user for a pyramid’s height and *re*-prompt if the user inputs a value less than 1 or greater than 8. The specification only requires you to re-prompt the user if they input a value less than 1.

[Embedded video: https://www.youtube.com/embed/NAs4FIWkJ4s](https://www.youtube.com/embed/NAs4FIWkJ4s)

<a id="how-to-test"></a>

#### How to Test

Does your code work as prescribed when you input:

* `-1` or other negative numbers?
* `0`?
* `1` or other positive numbers?
* letters or words?
* no input at all, when you only hit Enter?

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/mario/less
```

<a id="style"></a>

##### Style

```
style50 mario.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/mario/less
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): less comfortable
- Choice group: pset1-choice1 — “this version of Mario , if feeling less comfortable”
- Language (derived from files/commands on the page): C
- Folder: `mario-less`; files shown on the page: `mario.c`
- check50: `cs50/problems/2026/x/mario/less`
- style50: `mario.c`
- submit50: `cs50/problems/2026/x/mario/less`
- Page sections (order on source): Problem to Solve, Demo, Advice, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/cWOkHQXw0JQ, https://www.youtube.com/embed/NAs4FIWkJ4s
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: less comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم do-while loops، nested for loops، input validation، pseudocode، functions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write mario.c (folder mario-less) that prints a right-aligned half-pyramid of # bricks, like the staircase at the end of Super Mario Bros. World 1-1. The program asks for the height as an int and keeps re-prompting until it gets a positive integer. The page walks through pseudocode, a do-while loop for input and nested loops for printing rows.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 1](README.md) (`pset-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Algorithms and Pseudocode](../../../concepts/algorithms-and-pseudocode.md) (`concept-algorithms-and-pseudocode`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Loops](../../../concepts/loops.md) (`concept-loops`)
  - [Mario (more comfortable) — Problem Set 1](mario-more.md) (`pset-1-mario-more`)
  - [Mario (less comfortable) — Problem Set 6](../../week-06-python/psets/mario-less.md) (`pset-6-mario-less`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین حلقه‌های تودرتو و اعتبارسنجی ورودی با do-while؛ مناسب برای آموزش pseudocode.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. اول با کاغذ و قلم برای ارتفاع ۳ یا ۴ هر سطر را بکش و تعداد فاصله‌ها و #ها را در هر سطر بشمار.
2. رابطه‌ی بین شماره‌ی سطر و تعداد فاصله‌ها/آجرها را به زبان ساده بنویس.
3. مسئله را به دو بخش جدا تقسیم کن: گرفتن ورودی معتبر، و چاپ هرم.
4. چه زمانی باید دوباره از کاربر ورودی خواست؟ کدام نوع حلقه حداقل یک بار اجرا می‌شود؟

### اشتباه‌های رایج (مفهومی)
- فاصله‌ی اضافه در انتهای سطرها
- قبول کردن ارتفاع صفر یا منفی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/mario/less` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/1/mario/less/ — retrieved 2026-10-18T05:11:16+03:30, sha256 `de49c5021ee63ae4…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
