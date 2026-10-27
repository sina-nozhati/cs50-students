---
id: practice-6-jar
type: practice
title: Cookie Jar — Practice
week: 6
parent: week-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-exceptions
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/jar/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:05+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- classes-oop
- cookie-jar
- exceptions
- practice
- properties
checksum: sha256:dee945776baca3a5dc16580469b3e76c289c650bd07b4aae31cd1da1f2c398b2
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Cookie Jar — Practice

## 1. Source metadata
- **Title:** Cookie Jar — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/jar/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:05+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/jar/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="cookie-jar"></a>

### Cookie Jar

![Cookie Monster](https://cs50.harvard.edu/x/practice/jar/giphy1.gif)

Source: Sesame Street

Suppose that you’d like to implement a [cookie jar](https://en.wikipedia.org/wiki/Cookie_jar) in which to store cookies. In a file called `jar.py`, implement a `class` called `Jar` with these methods:

* `__init__` should initialize a cookie jar with the given `capacity`, which represents the maximum number of cookies that can fit in the cookie jar. If `capacity` is not a non-negative `int`, though, `__init__` should instead raise a `ValueError` (via `raise ValueError`).
* `__str__` should return a `str` with \(n\) `🍪`, where \(n\) is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then `str` should return `"🍪🍪🍪"`
* `deposit` should add `n` cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, `deposit` should instead raise a `ValueError`.
* `withdraw` should remove `n` cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, `withdraw` should instead raise a `ValueError`.
* `capacity` should return the cookie jar’s capacity.
* `size` should return the number of cookies actually in the cookie jar.

Structure your `class` per the below. You may not alter these methods’ parameters, but you may add your own methods.

```py
class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
```

<a id="demo"></a>

#### Demo

You’re welcome, but not required, to implement a `main` function in which to test your class, so this is all we can demo!

![Cookie Monster](https://cs50.harvard.edu/x/practice/jar/giphy2.gif)

Source: Sesame Street

<a id="before-you-begin"></a>

#### Before You Begin

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/6/jar.zip` followed by Enter in order to download a zip called `jar.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip jar.zip` to create a folder called `jar`.
5. You no longer need the ZIP file, so you can execute `rm jar.zip` and respond with “y” followed by Enter at the prompt.

<a id="how-to-test"></a>

#### How to Test

Here’s how to test your code manually:

* Define a `main` function in your `jar.py` file, wherein you create a new instance of `Jar` with `jar = Jar()`. Test this `jar` has the capacity it should by calling `print(str(jar.capacity))`. Be sure your program calls `main` at the bottom of the file, as via `main()`.
* Test that your `__str__` function works as intended by calling `print(str(jar))`.
* Try calling `jar.deposit(2)` to deposit two cookies. Calling `print(str(jar))` should now show you the same number of cookies you’ve deposited.
* Try calling `jar.withdraw(1)` to withdraw one cookie. Calling `print(str(jar))` should now show you one fewer cookie than you had before.
* Try experimenting with depositing and withdrawing various amounts of cookies. Are you unable to withdraw past the jar’s size? Are you unable to deposit past the jar’s capacity?

No `check50` for this one!

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/6/jar.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `jar/jar.py` | 272 | [yes](jar-distribution/files/jar/jar.py) |
| `jar/giphy2.gif` | 2182618 | no — binary/media/data file (inventory only) |
| `jar/giphy1.gif` | 861490 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `jar`; files shown on the page: `jar.py`
- check50: No check50 (stated)
- style50: not stated
- submit50: not stated
- Page sections (order on source): Demo, Before You Begin, How to Test, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم classes / OOP، properties، exceptions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** From CS50P: implement a Jar class (cookie jar) with capacity, deposit and withdraw methods and validation, as an introduction to classes.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 6 — Python](../week.md) (`week-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Exceptions](../../../concepts/exceptions.md) (`concept-exceptions`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین کلاس‌ها، property و استثناها در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. هر متد کلاس چه پیش‌شرطی دارد و در صورت نقض چه استثنایی باید رخ دهد؟

### اشتباه‌های رایج (مفهومی)
- (none)

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
- https://cs50.harvard.edu/x/practice/jar/ — retrieved 2026-10-18T05:11:05+03:30, sha256 `dee945776baca3a5…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
