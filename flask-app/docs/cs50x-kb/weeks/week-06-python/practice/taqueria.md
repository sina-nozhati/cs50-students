---
id: practice-6-taqueria
type: practice
title: Felipe’s Taqueria — Practice
week: 6
parent: week-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-dictionaries
- concept-loops
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/taqueria/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:07+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- dicts
- felipe-s-taqueria
- loops
- practice
- try-except
checksum: sha256:74be5d69c5929403a515d80da7bfb95cbf7e5e717d056b970883ace5a0bba4cb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Felipe’s Taqueria — Practice

## 1. Source metadata
- **Title:** Felipe’s Taqueria — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/taqueria/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:07+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/taqueria/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="felipes-taqueria"></a>

### Felipe’s Taqueria

![Felipe's Taqueria](https://cs50.harvard.edu/x/practice/taqueria/felipes-logo.png)

One of the most popular places to eat in [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Felipe’s Taqueria](https://www.felipesboston.com/), which offers a [menu](https://www.felipesboston.com/menu) of entrees, per the `dict` below, wherein the value of each key is a price in dollars:

```py
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

In a file called `taqueria.py`, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (`$`) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be [titlecased](https://docs.python.org/3/library/stdtypes.html#str.title).

> **Hints** *(collapsible block on the source page)*
>
> * Note that you can detect when the user has inputted control-d by catching an [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) with code like:
>
>   ```py
>   try:
>       item = input()
>   except EOFError:
>       ...
>   ```
>
>   You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.
> * Inputting control-d does not require inputting Enter as well, and so the user’s cursor (and subsequent prompt) might thus remain on the same line as your program’s own prompt. You can move the user’s cursor to a new line by printing `\n` yourself!
> * Note that a `dict` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), among them `get`, and supports operations like:
>
>   ```py
>   d[key]
>   ```
>
>   and
>
>   ```py
>   if key in d:
>       ...
>   ```
>
>   wherein `d` is a `dict` and `key` is a `str`.
> * Be sure to avoid or catch any [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/J20VZsCKXRPoavI0nFwCreRmr]

<a id="before-you-begin"></a>

#### Before You Begin

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/6/taqueria.zip` followed by Enter in order to download a zip called `taqueria.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip taqueria.zip` to create a folder called `taqueria`.
5. You no longer need the ZIP file, so you can execute `rm taqueria.zip` and respond with “y” followed by Enter at the prompt.

<a id="how-to-test"></a>

#### How to Test

Here’s how to test your code manually:

* Run your program with `python taqueria.py`. Type `Taco` and press Enter, then type `Taco` again and press Enter. Your program should output:

  ```
  Total: $6.00
  ```

  and continue prompting the user until they input control-d.
* Run your program with `python taqueria.py`. Type `Baja Taco` and press Enter, then type `Tortilla Salad` and press enter. Your program should output:

  ```
  Total: $12.25
  ```

  and continue prompting the user until they input control-d.
* Run your program with `python taqueria.py`. Type `Burger` and press Enter. Your program should reprompt the user.

Be sure to try other foods and vary the casing of your input. Your program should behave as expected, case-insensitively.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/taqueria
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/6/taqueria.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `taqueria/taqueria.py` | 0 | [yes](taqueria-distribution/files/taqueria/taqueria.py) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `taqueria`; files shown on the page: `taqueria.py`
- check50: `cs50/problems/2022/python/taqueria`
- style50: not stated
- submit50: not stated
- Page sections (order on source): Demo, Before You Begin, How to Test, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم dicts، try/except، loops.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** From CS50P: taqueria.py reads menu items one at a time, looks up each price in a provided dict and prints the running total, ignoring unknown items, until the user ends input.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 6 — Python](../week.md) (`week-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Dictionaries (dict)](../../../concepts/dictionaries.md) (`concept-dictionaries`)
  - [Loops](../../../concepts/loops.md) (`concept-loops`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین دیکشنری و حلقه تا EOF در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. منو را به‌صورت دیکشنری نگه دار و ورودی را تا پایان فایل بخوان.
2. حساسیت به بزرگی و کوچکی حروف را در نظر بگیر.

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2022/python/taqueria` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/taqueria/ — retrieved 2026-10-18T05:11:07+03:30, sha256 `74be5d69c5929403…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
