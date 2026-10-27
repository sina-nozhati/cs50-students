---
id: practice-6-bank
type: practice
title: Home Federal Savings Bank — Practice
week: 6
parent: week-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-conditionals
- concept-python-basics
- concept-strings
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/bank/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:03+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- conditionals
- home-federal-savings-bank
- practice
- python-strings
checksum: sha256:0106f7d44918f4d65db10be304da8eda0babc0ccb87bcc2cfe4dad3b5c2ae7cb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Home Federal Savings Bank — Practice

## 1. Source metadata
- **Title:** Home Federal Savings Bank — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/bank/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:03+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/bank/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="home-federal-savings-bank"></a>

### Home Federal Savings Bank

[Embedded video: https://www.youtube.com/embed/IN6cJ_wGmsk](https://www.youtube.com/embed/IN6cJ_wGmsk)

In [season 7, episode 24](https://en.wikipedia.org/wiki/The_Invitations) of [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld), [Kramer](https://en.wikipedia.org/wiki/Cosmo_Kramer) visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

> **Hints** *(collapsible block on the source page)*
>
> * Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
> * Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/Pes7djS4b1GmwpwqNu2vj6LgY]

<a id="before-you-begin"></a>

#### Before You Begin

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/6/bank.zip` followed by Enter in order to download a zip called `bank.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip bank.zip` to create a folder called `bank`.
5. You no longer need the ZIP file, so you can execute `rm bank.zip` and respond with “y” followed by Enter at the prompt.

<a id="how-to-test"></a>

#### How to Test

Here’s how to test your code manually:

* Run your program with `python bank.py`. Type `Hello` and press Enter. Your program should output:

  ```
  $0
  ```
* Run your program with `python bank.py`. Type `Hello, Newman` and press Enter. Your program should output:

  ```
  $0
  ```
* Run your program with `python bank.py`. Type `How you doing?` and press Enter. Your program should output

  ```
  $20
  ```
* Run your program with `python bank.py`. Type `What's happening?` and press Enter. Your program should output

  ```
  $100
  ```

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/bank
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/6/bank.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `bank/bank.py` | 0 | [yes](bank-distribution/files/bank/bank.py) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `bank`; files shown on the page: `bank.py`
- check50: `cs50/problems/2022/python/bank`
- style50: not stated
- submit50: not stated
- Page sections (order on source): Demo, Before You Begin, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/IN6cJ_wGmsk
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python strings، conditionals.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** From CS50P: bank.py prompts for a greeting and outputs $0 if it starts with "hello", $20 if it starts with some other "h" word, and $100 otherwise (a Seinfeld reference).

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 6 — Python](../week.md) (`week-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Conditionals and Boolean Expressions](../../../concepts/conditionals.md) (`concept-conditionals`)
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین رشته‌ها و شرط‌ها در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. متدهای رشته در Python برای حذف فاصله و تغییر حروف را مرور کن.

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2022/python/bank` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/bank/ — retrieved 2026-10-18T05:11:03+03:30, sha256 `0106f7d44918f4d6…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
