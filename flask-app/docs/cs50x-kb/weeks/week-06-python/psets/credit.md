---
id: pset-6-credit
type: pset
title: Credit (more comfortable) — Problem Set 6
week: 6
parent: pset-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-algorithms-and-pseudocode
- concept-python-basics
- concept-strings
- pset-1-credit
- pset-6-cash
source_urls:
- https://cs50.harvard.edu/x/psets/6/credit/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:39+03:30'
review_status: verified-against-source
difficulty: more comfortable
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- credit
- luhns-algorithm
- pset
- python-strings
checksum: sha256:c2fe2aed0e45b55d2d2a66ab81272cd0ff867d7210a1773b4ffa83d7310cf6a6
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Credit (more comfortable) — Problem Set 6

## 1. Source metadata
- **Title:** Credit (more comfortable) — Problem Set 6
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/6/credit/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:39+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/6/credit/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="credit"></a>

### Credit

<a id="problem-to-solve"></a>

#### Problem to Solve

In a filed called `credit.py` in a folder called `sentimental-credit`, write a program that prompts the user for a credit card number and then reports (via `print`) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in [Problem Set 1](https://cs50.harvard.edu/x/psets/1/). Your program this time should be written in Python!

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/QYLr1R1RDLO9QkPF2XFODLkq4]

<a id="specification"></a>

#### Specification

* So that we can automate some tests of your code, we ask that your program’s last line of output be `AMEX\n` or `MASTERCARD\n` or `VISA\n` or `INVALID\n`, nothing more, nothing less.
* For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
* Best to use `get_int` or `get_string` from CS50’s library to get users’ input, depending on how you to decide to implement this one.

<a id="hints"></a>

#### Hints

* It’s possible to use regular expressions to validate user input. You might use Python’s [`re`](https://docs.python.org/3/library/re.html) module, for example, to check whether the user’s input is indeed a sequence of digits of the correct length.

<a id="how-to-test"></a>

#### How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

* Run your program as `python credit.py`, and wait for a prompt for input. Type in `378282246310005` and press enter. Your program should output `AMEX`.
* Run your program as `python credit.py`, and wait for a prompt for input. Type in `371449635398431` and press enter. Your program should output `AMEX`.
* Run your program as `python credit.py`, and wait for a prompt for input. Type in `5555555555554444` and press enter. Your program should output `MASTERCARD`.
* Run your program as `python credit.py`, and wait for a prompt for input. Type in `5105105105105100` and press enter. Your program should output `MASTERCARD`.
* Run your program as `python credit.py`, and wait for a prompt for input. Type in `4111111111111111` and press enter. Your program should output `VISA`.
* Run your program as `python credit.py`, and wait for a prompt for input. Type in `4012888888881881` and press enter. Your program should output `VISA`.
* Run your program as `python credit.py`, and wait for a prompt for input. Type in `1234567890` and press enter. Your program should output `INVALID`.

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/sentimental/credit
```

<a id="style"></a>

##### Style

```
style50 credit.py
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/sentimental/credit
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): more comfortable
- Choice group: pset6-choice2 — “Credit in Python, if feeling more comfortable”
- Language (derived from files/commands on the page): Python
- Folder: `sentimental-credit`; files shown on the page: `credit.py`
- check50: `cs50/problems/2026/x/sentimental/credit`
- style50: `credit.py`
- submit50: `cs50/problems/2026/x/sentimental/credit`
- Page sections (order on source): Problem to Solve, Demo, Specification, Hints, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: more comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python strings، Luhn's algorithm.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Re-implement Credit in Python (credit.py in folder sentimental-credit). It validates a card number with Luhn's algorithm and prints whether it is AMEX, MASTERCARD, VISA or INVALID.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Problem Set 6](README.md) (`pset-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Algorithms and Pseudocode](../../../concepts/algorithms-and-pseudocode.md) (`concept-algorithms-and-pseudocode`)
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Credit (more comfortable) — Problem Set 1](../../week-01-c/psets/credit.md) (`pset-1-credit`)
  - [Cash (less comfortable) — Problem Set 6](cash.md) (`pset-6-cash`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
بازنویسی Credit در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. در Python می‌توانی با عدد یا رشته‌ی ارقام کار کنی؛ کدام برایت ساده‌تر است؟
2. الگوریتم Luhn را یک بار با دست روی یک شماره‌ی نمونه انجام بده.

### اشتباه‌های رایج (مفهومی)
- اشتباه در ترتیب ارقامی که دو برابر می‌شوند

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/sentimental/credit` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/6/credit/ — retrieved 2026-10-18T05:11:39+03:30, sha256 `c2fe2aed0e45b55d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
