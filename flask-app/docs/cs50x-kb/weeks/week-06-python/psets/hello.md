---
id: pset-6-hello
type: pset
title: Hello, Again — Problem Set 6
week: 6
parent: pset-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-python-basics
- concept-strings
- pset-1-me
source_urls:
- https://cs50.harvard.edu/x/psets/6/hello/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:35+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- f-strings
- hello-again
- input-print
- pset
- python-basics
checksum: sha256:d25fbb85e051dbb9103d69390357dcc588d40c94ba20ab8b906378b766d64f05
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hello, Again — Problem Set 6

## 1. Source metadata
- **Title:** Hello, Again — Problem Set 6
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/6/hello/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:35+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/6/hello/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="hello-again"></a>

### Hello, Again

<a id="problem-to-solve"></a>

#### Problem to Solve

In a file called `hello.py` in a folder called `sentimental-hello`, implement a program that prompts a user for their name, and then prints `hello, so-and-so`, where `so-and-so` is their provided name, exactly as you did in [Problem Set 1](https://cs50.harvard.edu/x/psets/1/). Except that your program this time should be written in Python!

> **Hints** *(collapsible block on the source page)*
>
> * Recall that you can get a `str` from a user with `get_string`, which is declared in the `cs50` library.
> * Recall that you can print a `str` with `print`.
> * Recall that you can create formatted strings in Python by prepending `f` to a string itself. For example, `f"{name}"` will substitute (“interpolate”) the value of the variable `name` where you’ve written `{name}`.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/gqi2voQFzbKlna6WkQR0G2W93]

<a id="how-to-test"></a>

#### How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

* Run your program as `python hello.py`, and wait for a prompt for input. Type in `David` and press enter. Your program should output `hello, David`.
* Run your program as `python hello.py`, and wait for a prompt for input. Type in `Inno` and press enter. Your program should output `hello, Inno`.
* Run your program as `python hello.py`, and wait for a prompt for input. Type in `Kamryn` and press enter. Your program should output `hello, Kamryn`.

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/sentimental/hello
```

<a id="style"></a>

##### Style

```
style50 hello.py
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/sentimental/hello
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `sentimental-hello`; files shown on the page: `hello.py`
- check50: `cs50/problems/2026/x/sentimental/hello`
- style50: `hello.py`
- submit50: `cs50/problems/2026/x/sentimental/hello`
- Page sections (order on source): Problem to Solve, Demo, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python basics، input/print، f-strings.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Re-implement Problem Set 1's Hello, It's Me in Python: hello.py (folder sentimental-hello) asks for a name and prints a greeting. It introduces Python syntax and input/print after C.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Problem Set 6](README.md) (`pset-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Hello, It’s Me — Problem Set 1](../../week-01-c/psets/me.md) (`pset-1-me`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
شروع Python و مقایسه‌ی آن با C.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. نسخه‌ی C این برنامه را به یاد بیاور و ببین کدام بخش‌ها در Python لازم نیستند.
2. در Python ورودی گرفتن و قالب‌بندی رشته چه روش‌هایی دارد؟

### اشتباه‌های رایج (مفهومی)
- اختلاف جزئی متن خروجی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/sentimental/hello` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/6/hello/ — retrieved 2026-10-18T05:11:35+03:30, sha256 `d25fbb85e051dbb9…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
