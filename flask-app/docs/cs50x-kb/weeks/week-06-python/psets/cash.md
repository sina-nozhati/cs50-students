---
id: pset-6-cash
type: pset
title: Cash (less comfortable) — Problem Set 6
week: 6
parent: pset-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-algorithms-and-pseudocode
- concept-python-basics
- pset-1-cash
- pset-6-credit
source_urls:
- https://cs50.harvard.edu/x/psets/6/cash/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:38+03:30'
review_status: verified-against-source
difficulty: less comfortable
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- cash
- floats-vs-integers
- greedy-algorithm
- pset
- python
checksum: sha256:782a98123ad423d00f458634822715a9d05803532652ae3270d052aa40849a4e
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Cash (less comfortable) — Problem Set 6

## 1. Source metadata
- **Title:** Cash (less comfortable) — Problem Set 6
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/6/cash/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:38+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/6/cash/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="cash"></a>

### Cash

<a id="problem-to-solve"></a>

#### Problem to Solve

In a file called `cash.py` in a folder called `sentimental-cash`, write a program that asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made. You can do this exactly as you did in [Problem Set 1](https://cs50.harvard.edu/x/psets/1/), except that your program this time should be written in Python, and you should assume that the user will input their change in dollars (e.g., 0.50 dollars instead of 50 cents).

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/eoFGGVR2gwl2jvyj7sHchxUmW]

<a id="specification"></a>

#### Specification

* Use `get_float` from the CS50 Library to get the user’s input and `print` to output your answer. Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
  * We ask that you use `get_float` so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill), assume that your program’s input will be `9.75` and not `$9.75` or `975`. However, if some customer is owed $9 exactly, assume that your program’s input will be `9.00` or just `9` but, again, not `$9` or `900`. Of course, by nature of floating-point values, your program will likely work with inputs like `9.0` and `9.000` as well; you need not worry about checking whether the user’s input is “formatted” like money should be.
* If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
* Incidentally, so that we can automate some tests of your code, we ask that your program’s last line of output be only the minimum number of coins possible: an integer followed by a newline.

<a id="how-to-test"></a>

#### How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

* Run your program as `python cash.py`, and wait for a prompt for input. Type in `0.41` and press enter. Your program should output `4`.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `0.01` and press enter. Your program should output `1`.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `0.15` and press enter. Your program should output `2`.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `1.60` and press enter. Your program should output `7`.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `23` and press enter. Your program should output `92`.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `4.2` and press enter. Your program should output `18`.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `-1` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
* Run your program as `python cash.py`, and wait for a prompt for input. Type in `foo` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
* Run your program as `python cash.py`, and wait for a prompt for input. Do not type anything, and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/sentimental/cash
```

<a id="style"></a>

##### Style

```
style50 cash.py
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/sentimental/cash
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): less comfortable
- Choice group: pset6-choice2 — “Cash in Python, if feeling less comfortable”
- Language (derived from files/commands on the page): Python
- Folder: `sentimental-cash`; files shown on the page: `cash.py`
- check50: `cs50/problems/2026/x/sentimental/cash`
- style50: `cash.py`
- submit50: `cs50/problems/2026/x/sentimental/cash`
- Page sections (order on source): Problem to Solve, Demo, Specification, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: less comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python، floats vs integers، greedy algorithm.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Re-implement Cash in Python (cash.py in folder sentimental-cash). This time the user enters change in dollars (e.g. 0.50), and the program prints the minimum number of coins, re-prompting on invalid input.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 6](README.md) (`pset-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Algorithms and Pseudocode](../../../concepts/algorithms-and-pseudocode.md) (`concept-algorithms-and-pseudocode`)
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Cash (less comfortable) — Problem Set 1](../../week-01-c/psets/cash.md) (`pset-1-cash`)
  - [Credit (more comfortable) — Problem Set 6](credit.md) (`pset-6-credit`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
بازنویسی Cash در Python و توجه به اعداد اعشاری.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. ورودی این بار به دلار است؛ چطور آن را به واحدی تبدیل می‌کنی که خطای اعشاری ایجاد نکند؟
2. منطق حریصانه همان است؛ عملگرهای Python را برای تقسیم صحیح و باقیمانده مرور کن.

### اشتباه‌های رایج (مفهومی)
- خطای ممیز شناور در تبدیل به سنت

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/sentimental/cash` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/6/cash/ — retrieved 2026-10-18T05:11:38+03:30, sha256 `782a98123ad423d0…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
