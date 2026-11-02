---
id: pset-1-mario-more
type: pset
title: Mario (more comfortable) — Problem Set 1
week: 1
parent: pset-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-forms-get-post
- concept-loops
- concept-strings
- pset-1-mario-less
- pset-6-mario-more
source_urls:
- https://cs50.harvard.edu/x/psets/1/mario/more/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:17+03:30'
review_status: verified-against-source
difficulty: more comfortable
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- input-validation
- mario
- nested-loops
- pset
- string-output-formatting
checksum: sha256:22283d9fadec26278dde987d8ebfa414ddef41afda541f3637265799bc8d6835
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Mario (more comfortable) — Problem Set 1

## 1. Source metadata
- **Title:** Mario (more comfortable) — Problem Set 1
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/1/mario/more/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:17+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/1/mario/more/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="mario"></a>

### Mario

[Embedded video: https://www.youtube.com/embed/cWOkHQXw0JQ](https://www.youtube.com/embed/cWOkHQXw0JQ)

<a id="problem-to-solve"></a>

#### Problem to Solve

Toward the beginning of World 1-1 in Nintendo’s Super Mario Brothers, Mario must hop over adjacent pyramids of blocks, per the below.

![screenshot of Mario jumping over adjacent pyramids](https://cs50.harvard.edu/x/psets/1/mario/more/pyramids.png)

In a file called `mario.c` in a folder called `mario-more`, implement a program in C that recreates that pyramid, using hashes (`#`) for bricks, as in the below:

```
   #  #
  ##  ##
 ###  ###
####  ####
```

And let’s allow the user to decide just how tall the pyramids should be by first prompting them for a positive `int` between, say, 1 and 8, inclusive.

> **Examples** *(collapsible block on the source page)*
>
> Here’s how the program might work if the user inputs `8` when prompted:
>
> ```
> $ ./mario
> Height: 8
>        #  #
>       ##  ##
>      ###  ###
>     ####  ####
>    #####  #####
>   ######  ######
>  #######  #######
> ########  ########
> ```
>
> Here’s how the program might work if the user inputs `4` when prompted:
>
> ```
> $ ./mario
> Height: 4
>    #  #
>   ##  ##
>  ###  ###
> ####  ####
> ```
>
> Here’s how the program might work if the user inputs `2` when prompted:
>
> ```
> $ ./mario
> Height: 2
>  #  #
> ##  ##
> ```
>
> And here’s how the program might work if the user inputs `1` when prompted:
>
> ```
> $ ./mario
> Height: 1
> #  #
> ```
>
> If the user doesn’t, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:
>
> ```
> $ ./mario
> Height: -1
> Height: 0
> Height: 42
> Height: 50
> Height: 4
>    #  #
>   ##  ##
>  ###  ###
> ####  ####
> ```

Notice that width of the “gap” between adjacent pyramids is equal to the width of two hashes, irrespective of the pyramids’ heights.

<a id="walkthrough"></a>

##### Walkthrough

[Embedded video: https://www.youtube.com/embed/FzN9RAjYG_Q](https://www.youtube.com/embed/FzN9RAjYG_Q)

<a id="how-to-test-your-code"></a>

##### How to Test Your Code

Does your code work as prescribed when you input

* `-1` (or other negative numbers)?
* `0`?
* `1` through `8`?
* `9` or other positive numbers?
* letters or words?
* no input at all, when you only hit Enter?

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

```
check50 cs50/problems/2026/x/mario/more
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 mario.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/mario/more
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): more comfortable
- Choice group: pset1-choice1 — “this version of Mario , if feeling more comfortable”
- Language (derived from files/commands on the page): C
- Folder: `mario-more`; files shown on the page: `mario.c`
- check50: `cs50/problems/2026/x/mario/more`
- style50: `mario.c`
- submit50: `cs50/problems/2026/x/mario/more`
- Page sections (order on source): Problem to Solve, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/cWOkHQXw0JQ, https://www.youtube.com/embed/FzN9RAjYG_Q
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: more comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم nested loops، input validation، string output formatting.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** The harder Mario variant: mario.c (folder mario-more) prints two adjacent right- and left-aligned pyramids separated by a gap two hashes wide, as at the start of World 1-1. The user is prompted for a height from 1 to 8 inclusive and re-prompted until they comply. Output should match the examples shown on the page.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 1](README.md) (`pset-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Forms, GET and POST](../../../concepts/forms-get-post.md) (`concept-forms-get-post`)
  - [Loops](../../../concepts/loops.md) (`concept-loops`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Mario (less comfortable) — Problem Set 1](mario-less.md) (`pset-1-mario-less`)
  - [Mario (more comfortable) — Problem Set 6](../../week-06-python/psets/mario-more.md) (`pset-6-mario-more`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
نسخه‌ی چالشی‌تر Mario برای دانشجویان راحت‌تر؛ تمرین تجزیه‌ی الگو به بخش‌های تکرارشونده.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. هر سطر را به چند قطعه تقسیم کن: فاصله‌ها، نیمه‌ی چپ، شکاف، نیمه‌ی راست.
2. برای ارتفاع کوچک الگو را روی کاغذ بکش و طول هر قطعه را بر حسب شماره‌ی سطر بنویس.
3. فکر کن آیا می‌توانی چاپ یک قطعه‌ی تکراری را در یک تابع جدا کنی.

### اشتباه‌های رایج (مفهومی)
- فاصله‌ی اضافه بعد از آخرین #
- اندازه‌ی نادرست شکاف وسط

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/mario/more` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/1/mario/more/ — retrieved 2026-10-18T05:11:17+03:30, sha256 `22283d9fadec2627…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
