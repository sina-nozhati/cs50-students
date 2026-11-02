---
id: pset-1-cash
type: pset
title: Cash (less comfortable) — Problem Set 1
week: 1
parent: pset-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-algorithms-and-pseudocode
- concept-functions
- concept-operators
- pset-1-credit
- pset-6-cash
source_urls:
- https://cs50.harvard.edu/x/psets/1/cash/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:18+03:30'
review_status: verified-against-source
difficulty: less comfortable
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- arithmetic-modulo
- cash
- functions
- greedy-algorithms
- input-validation
- pset
checksum: sha256:d54f1d95d309c06595a4123803e84831f4e16d3634b94f5fcd0b7754d5549950
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Cash (less comfortable) — Problem Set 1

## 1. Source metadata
- **Title:** Cash (less comfortable) — Problem Set 1
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/1/cash/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:18+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/1/cash/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="cash"></a>

### Cash

![US coins](https://cs50.harvard.edu/x/psets/1/cash/coins.jpg)

<a id="problem-to-solve"></a>

#### Problem to Solve

Suppose you work at a store and a customer gives you $1.00 (100 cents) for candy that costs $0.50 (50 cents). You’ll need to pay them their “change,” the amount leftover after paying for the cost of the candy. When making change, odds are you want to minimize the number of coins you’re dispensing for each customer, lest you run out (or annoy the customer!). In a file called `cash.c` in a folder called `cash`, implement a program in C that prints the minimum coins needed to make the given amount of change, in cents, as in the below:

```
Change owed: 25
1
```

But prompt the user for an `int` greater than 0, so that the program works for any amount of change:

```
Change owed: 70
4
```

Re-prompt the user, again and again as needed, if their input is not greater than or equal to 0 (or if their input isn’t an `int` at all!).

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/p6PlFqQgSWNWn4ggpIIaBOvIq]

<a id="greedy-algorithms"></a>

#### Greedy Algorithms

Fortunately, computer science has given cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one “that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems.”

What’s all that mean? Well, suppose that a cashier owes a customer some change and in that cashier’s drawer are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). The problem to be solved is to decide which coins and how many of each to hand to the customer. Think of a “greedy” cashier as one who wants to take the biggest bite out of this problem as possible with each coin they take out of the drawer. For instance, if some customer is owed 41¢, the biggest first (i.e., best immediate, or local) bite that can be taken is 25¢. (That bite is “best” inasmuch as it gets us closer to 0¢ faster than any other coin would.) Note that a bite of this size would whittle what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16. That is, the remainder is a similar but smaller problem. Needless to say, another 25¢ bite would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to a bite of size 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ bite followed by one 1¢ bite, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.

It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America’s currency (and also the European Union’s). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible. How few? Well, you tell us!

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
>
> Notice that you’ve now included `cs50.h` and `stdio.h`, two “header files” that will give you access to functions that might help you solve this problem.

> **Write some pseudocode before writing more code** *(collapsible block on the source page)*
>
> If unsure how to solve the problem itself, break it down into smaller problems that you can probably solve first. For instance, this problem is really only a handful of problems:
>
> 1. Prompt the user for change owed, in cents.
> 2. Calculate how many *quarters* you should give customer. Subtract the value of those quarters from cents.
> 3. Calculate how many *dimes* you should give customer. Subtract the value of those dimes from remaining cents.
> 4. Calculate how many *nickels* you should give customer. Subtract the value of those nickels from remaining cents.
> 5. Calculate how many *pennies* you should give customer. Subtract the value of those pennies from remaining cents.
> 6. Sum the number of quarters, dimes, nickels, and pennies used.
> 7. Print that sum.
>
> This is the greedy algorithm you can use to solve this problem, so let’s write some pseudcode as comments to remind you to do just that:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int main(void)
> {
>     // Prompt the user for change owed, in cents
>
>     // Calculate how many quarters you should give customer
>     // Subtract the value of those quarters from cents
>
>     // Calculate how many dimes you should give customer
>     // Subtract the value of those dimes from remaining cents
>
>     // Calculate how many nickels you should give customer
>     // Subtract the value of those nickels from remaining cents
>
>     // Calculate how many pennies you should give customer
>     // Subtract the value of those pennies from remaining cents
>
>     // Sum the number of quarters, dimes, nickels, and pennies used
>     // Print that sum
> }
> ```

> **Convert the pseudocode to code** *(collapsible block on the source page)*
>
> First, consider how you might prompt the user for the cents they are owed. Recall that a `do while` loop is helpful when you want to do something at least once, and possibly again and again, as in the below:
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int main(void)
> {
>     // Prompt the user for change owed, in cents
>     int cents;
>     do
>     {
>         cents = get_int("Change owed: ");
>     }
>     while (cents < 0);
> }
> ```
>
> It’s wise to stop here and `make` your program. Test to be sure your program compiles, and that it reprompts you if you enter less than 0 cents (or if you enter an input like “cat”).
>
> Next, consider how to calculate how many quarters you should give the customer. Since we’re using a greedy algorithm, this question becomes “what’s the *greatest* number of quarters could you give them?”. You *could* write a solution to this problem in your `main` function. But, it might clear up your thinking to write a new function: one called `calculate_quarters`. That way you can better focus on the logic to calculate quarters. Later, you can integrate this function into your larger solution.
>
> ```c
> int calculate_quarters(int cents)
> {
>     // Calculate how many quarters you should give customer
> }
> ```
>
> Notice that this function is indeed named `calculate_quarters`. Per `int cents` in parentheses, it takes an `int` called `cents` as input. And, per the `int` in front of its name, it should also “return” an `int`. That is, the output of this function is an integer: the number of quarters that fit into cents.
>
> Now consider this way of implementing `calculate_quarters` by adding to the number of quarters until we’ve run out of cents to convert to quarters:
>
> ```c
> int calculate_quarters(int cents)
> {
>     // Calculate how many quarters you should give customer
>     int quarters = 0;
>     while (cents >= 25)
>     {
>         quarters++;
>         cents = cents - 25;
>     }
>     return quarters;
> }
> ```
>
> Granted, there is at least one simpler way to solve this `calculate_quarters` problem. But we’ll leave that up to you to figure out!
>
> With `calculate_quarters` functioning as intended, you can integrate this function into your program. Take care to “declare” the function’s “signature” (i.e., `int calculate_quarters(int cents)`) above your `main` function, so you can indeed use `calculate_quarters` there while defining it later, below `main`.
>
> ```c
> #include <cs50.h>
> #include <stdio.h>
>
> int calculate_quarters(int cents);
>
> int main(void)
> {
>     // Prompt the user for change owed, in cents
>     int cents;
>     do
>     {
>         cents = get_int("Change owed: ");
>     }
>     while (cents < 0);
>
>     // Calculate how many quarters you should give customer
>     int quarters = calculate_quarters(cents);
>
>     // Subtract the value of those quarters from cents
>     cents = cents - (quarters * 25);
> }
>
> int calculate_quarters(int cents)
> {
>     // Calculate how many quarters you should give customer
>     int quarters = 0;
>     while (cents >= 25)
>     {
>         quarters++;
>         cents = cents - 25;
>     }
>     return quarters;
> }
> ```
>
> A few problems down, and a few more to go! Notice a pattern you could re-use here?

<a id="how-to-test"></a>

#### How to Test

For this program, try testing your code manually. It’s good practice:

* If you input `-1`, does your program prompt you again?
* If you input `0`, does your program output `0`?
* If you input `1`, does your program output `1` (i.e., one penny)?
* If you input `4`, does your program output `4` (i.e., four pennies)?
* If you input `5`, does your program output `1` (i.e., one nickel)?
* If you input `24`, does your program output `6` (i.e., two dimes and four pennies)?
* If you input `25`, does your program output `1` (i.e., one quarter)?
* If you input `26`, does your program output `2` (i.e., one quarter and one penny)?
* If you input `99`, does your program output `9` (i.e., three quarters, two dimes, and four pennies)?

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/cash
```

<a id="style"></a>

##### Style

```
style50 cash.c
```

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/cash
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): less comfortable
- Choice group: pset1-choice2 — “Cash , if feeling less comfortable”
- Language (derived from files/commands on the page): C
- Folder: `cash`; files shown on the page: `cash.c`
- check50: `cs50/problems/2026/x/cash`
- style50: `cash.c`
- submit50: `cs50/problems/2026/x/cash`
- Page sections (order on source): Problem to Solve, Demo, Greedy Algorithms, Advice, How to Test
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: less comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم greedy algorithms، arithmetic / modulo، functions، input validation.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write cash.c that prints the minimum number of coins (quarters, dimes, nickels, pennies) needed for a given amount of change in cents. The user is re-prompted until they enter a non-negative int. It illustrates a greedy algorithm, which always takes the largest coin that still fits.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 1](README.md) (`pset-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Algorithms and Pseudocode](../../../concepts/algorithms-and-pseudocode.md) (`concept-algorithms-and-pseudocode`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Operators](../../../concepts/operators.md) (`concept-operators`)
  - [Credit (more comfortable) — Problem Set 1](credit.md) (`pset-1-credit`)
  - [Cash (less comfortable) — Problem Set 6](../../week-06-python/psets/cash.md) (`pset-6-cash`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
آشنایی با الگوریتم حریصانه (greedy) و تقسیم یک مسئله به توابع کوچک.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. خودت به‌عنوان صندوق‌دار فکر کن: برای کمترین تعداد سکه، اول کدام سکه را می‌دهی؟
2. بعد از دادن هر سکه، چه مقداری باقی می‌ماند و چه چیزی را باید شمرد؟
3. عملگرهای تقسیم صحیح و باقیمانده را در جزوه‌ی هفته ۱ مرور کن.

### اشتباه‌های رایج (مفهومی)
- اعتبارسنجی نکردن ورودی منفی
- تغییر ندادن مقدار باقی‌مانده بعد از هر نوع سکه

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/cash` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/1/cash/ — retrieved 2026-10-18T05:11:18+03:30, sha256 `d54f1d95d309c065…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
