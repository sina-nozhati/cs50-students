---
id: practice-3-atoi
type: practice
title: Recursive atoi — Practice
week: 3
parent: week-3
children: []
prerequisites:
- week-3-lecture
related:
- concept-recursion
- concept-strings
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/atoi/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:55+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- practice
- recursion
- recursive-atoi
- strings
checksum: sha256:487bc5558f634d2da020b5f501288cfbea3ef1e8d7d6378e22169a692eef6b7b
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Recursive atoi — Practice

## 1. Source metadata
- **Title:** Recursive atoi — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/atoi/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:55+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/atoi/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="recursive-atoi"></a>

### Recursive `atoi`

<a id="learning-goals"></a>

#### Learning Goals

* Deepen an understanding of strings
* Practice creating recursive functions

<a id="background"></a>

#### Background

Imagine that you travel back in time to the 1970’s, when the `C` programming language was first created. You are hired as a programmer to come up with a way to convert `string`s to `int`s. (You may have used a function just like this in Week 2, called [`atoi`](https://manual.cs50.io/3/atoi)). You want to be thorough in your development process and plan to try several approaches before deciding on the most efficient.

In this problem, you will start with a simple implementation of `atoi` that handles positive `int`s using loops. You want to rework this into an implementation that uses recursion. Recusive functions can be memory intensive and are not always the best solution, but there are some problems in which using recursion can provide a simpler and more elegant solution.

(Scroll to the bottom of this page to see what an implementation of `atoi` might actually look like.)

* Hints
  * Start by getting the index of the last `char` in the string (the `char` before the `\0`).
  * Convert this `char` into its numeric value. Can you subtract some `char` to do this?
  * Remove the last `char` from the string by moving the null terminator one position to the left.
  * Return this value plus 10 times the integer value of the new shortened string.
  * Remember you need a base case when creating a recursive function.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/qH1q1cIz2kZEnbl1Mc4CCCcYK]

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/3/atoi.zip` followed by Enter in order to download a zip called `atoi.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip atoi.zip` to create a folder called `atoi`.
5. You no longer need the ZIP file, so you can execute `rm atoi.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

In the recursive version of `convert`, start with the last `char` and convert it into an integer value. Then shorten the `string`, removing the last `char`, and then recursively call `convert` using the shortened string as input, where the next `char` will be processed.

<a id="thought-question"></a>

#### Thought Question

Why do you need a base case whenever you create a recursive function?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
atoi/ $ ./atoi
Enter a positive integer: 3432
3432
```

```
atoi/ $ ./atoi
Enter a positive integer: 98765
98765
```

No `check50` for this one!

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 atoi.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem.

<a id="a-more-thorough-implementation"></a>

#### A More Thorough Implementation

The actual version of `atoi` must handle negative numbers, as well as leading spaces and non-numeric characters. It might look something like this:

```c
#include <stdio.h>
 
// Iterative function to implement `atoi()` function in C
long atoi(const char S[])
{
    long num = 0;
    int i = 0, sign = 1;
 
    // skip white space characters
    while (S[i] == ' ' || S[i] == '\n' || S[i] == '\t') {
        i++;
    }
 
    // note sign of the number
    if (S[i] == '+' || S[i] == '-')
    {
        if (S[i] == '-') {
            sign = -1;
        }
        i++;
    }
 
    // run till the end of the string is reached, or the
    // current character is non-numeric
    while (S[i] && (S[i] >= '0' && S[i] <= '9'))
    {
        num = num * 10 + (S[i] - '0');
        i++;
    }
 
    return sign * num;
}
 
// Implement `atoi()` function in C
int main(void)
{
    char S[] = " -1234567890";
 
    printf("%ld ", atoi(S));
 
    return 0;
}
```

From [techiedelight.com/implement-atoi-function-c-iterative-recursive](https://www.techiedelight.com/implement-atoi-function-c-iterative-recursive/).

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/3/atoi.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `atoi/atoi.c` | 489 | [yes](atoi-distribution/files/atoi/atoi.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `atoi`; files shown on the page: `atoi.c`
- check50: No check50 (stated)
- style50: `atoi.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit, A More Thorough Implementation
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم recursion، strings.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Rewrite a loop-based string-to-int converter (atoi for positive numbers) as a recursive function.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 3 — Algorithms](../week.md) (`week-3`)
- **Prerequisites (generated):** [Week 3 — Lecture notes (Algorithms)](../lecture.md) (`week-3-lecture`)
- **Related:**
  - [Recursion](../../../concepts/recursion.md) (`concept-recursion`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین بازگشت با تبدیل رشته به عدد.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. مسئله را بر حسب یک نسخه‌ی کوچک‌تر از خودش بیان کن.
2. حالت پایه‌ی بازگشت چیست؟

### اشتباه‌های رایج (مفهومی)
- نبود حالت پایه

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای (در صفحه ذکر نشده) و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/atoi/ — retrieved 2026-10-18T05:10:55+03:30, sha256 `487bc5558f634d2d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
