---
id: pset-1-credit
type: pset
title: Credit (more comfortable) — Problem Set 1
week: 1
parent: pset-1
children: []
prerequisites:
- week-1-lecture
related:
- concept-algorithms-and-pseudocode
- concept-conditionals
- pset-1-cash
- pset-6-credit
source_urls:
- https://cs50.harvard.edu/x/psets/1/credit/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:19+03:30'
review_status: verified-against-source
difficulty: more comfortable
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- conditionals
- credit
- digit-extraction-with-and
- long-integers
- luhns-algorithm
- pset
checksum: sha256:01fb53750c238eb53c382c13b8a70031a5c0d807f2265e68f3a0e5e40ecfa4fc
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Credit (more comfortable) — Problem Set 1

## 1. Source metadata
- **Title:** Credit (more comfortable) — Problem Set 1
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/1/credit/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:19+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/1/credit/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="credit"></a>

### Credit

![Person holding credit cards](https://cs50.harvard.edu/x/psets/1/credit/credit_cards.jpeg)

<a id="problem-to-solve"></a>

#### Problem to Solve

A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that’s also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a quadrillion.)

Actually, that’s a bit of an exaggeration, because credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous checks.

In a file called `credit.c` in a folder called `credit`, implement a program in C that checks the validity of a given credit card number.

<a id="luhns-algorithm"></a>

#### Luhn’s Algorithm

So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!

That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.

1. For the sake of discussion, let’s first underline every other digit, starting with the number’s second-to-last digit:

   4003600000000014

   Okay, let’s multiply each of the underlined digits by 2:

   1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

   That gives us:

   2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

   Now let’s add those products’ digits (i.e., not the products themselves) together:

   2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
2. Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

   13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
3. Yup, the last digit in that sum (20) is a 0, so David’s card is legit!

So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s write a program.

<a id="implementation-details"></a>

#### Implementation Details

In the file called `credit.c` in the `credit` directory, write a program that prompts the user for a credit card number and then reports (via `printf`) whether it is a valid American Express, MasterCard, or Visa card number, per the definitions of each’s format herein. So that we can automate some tests of your code, we ask that your program’s last line of output be `AMEX\n` or `MASTERCARD\n` or `VISA\n` or `INVALID\n`, nothing more, nothing less. For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card) and that it won’t have leading zeroes. But do not assume that the user’s input will fit in an `int`! Best to use `get_long` from CS50’s library to get users’ input. (Why?)

Consider the below representative of how your own program should behave when passed a valid credit card number (sans hyphens).

```
$ ./credit
Number: 4003600000000014
VISA
```

Now, `get_long` itself will reject hyphens (and more) anyway:

```
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

But it’s up to you to catch inputs that are not credit card numbers (e.g., a phone number), even if numeric:

```
$ ./credit
Number: 6176292929
INVALID
```

Test out your program with a whole bunch of inputs, both valid and invalid. (We certainly will!) Here are a [few card numbers](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) that PayPal recommends for testing.

If your program behaves incorrectly on some inputs (or doesn’t compile at all), time to debug!

<a id="walkthrough"></a>

##### Walkthrough

[Embedded video: https://www.youtube.com/embed/dF7wNjsRBjI](https://www.youtube.com/embed/dF7wNjsRBjI)

<a id="how-to-test-your-code"></a>

##### How to Test Your Code

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

```
check50 cs50/problems/2026/x/credit
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 credit.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2026/x/credit
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): more comfortable
- Choice group: pset1-choice2 — “Credit , if feeling more comfortable”
- Language (derived from files/commands on the page): C
- Folder: `credit`; files shown on the page: `credit.c`
- check50: `cs50/problems/2026/x/credit`
- style50: `credit.c`
- submit50: `cs50/problems/2026/x/credit`
- Page sections (order on source): Problem to Solve, Luhn’s Algorithm, Implementation Details, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/dF7wNjsRBjI
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: more comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Luhn's algorithm، long integers، digit extraction with % and /، conditionals.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write credit.c that reads a card number and reports whether it is a valid American Express, MasterCard or Visa number, or invalid. Validity is checked with Luhn's checksum algorithm, plus each company's length and starting-digit rules. Numbers are read as a long, so the program must extract digits arithmetically.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Problem Set 1](README.md) (`pset-1`)
- **Prerequisites (generated):** [Week 1 — Lecture notes (C)](../lecture.md) (`week-1-lecture`)
- **Related:**
  - [Algorithms and Pseudocode](../../../concepts/algorithms-and-pseudocode.md) (`concept-algorithms-and-pseudocode`)
  - [Conditionals and Boolean Expressions](../../../concepts/conditionals.md) (`concept-conditionals`)
  - [Cash (less comfortable) — Problem Set 1](cash.md) (`pset-1-cash`)
  - [Credit (more comfortable) — Problem Set 6](../../week-06-python/psets/credit.md) (`pset-6-credit`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین کار با ارقام یک عدد بزرگ (long) و پیاده‌سازی یک الگوریتم checksum از روی توضیح.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. چطور می‌شود رقم آخر یک عدد را جدا کرد و بعد آن رقم را از عدد حذف کرد؟
2. الگوریتم را برای یک شماره‌ی نمونه‌ی صفحه با دست انجام بده تا ترتیب مراحل را بفهمی.
3. تشخیص نوع کارت به تعداد ارقام و ارقام ابتدایی بستگی دارد؛ این دو را جدا از checksum محاسبه کن.
4. حالت‌های نامعتبر را هم با شماره‌های آزمایشی امتحان کن.

### اشتباه‌های رایج (مفهومی)
- استفاده از int به جای long
- فراموش کردن جمع ارقامِ حاصل‌ضرب‌های دو رقمی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/credit` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/1/credit/ — retrieved 2026-10-18T05:11:19+03:30, sha256 `01fb53750c238eb5…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
