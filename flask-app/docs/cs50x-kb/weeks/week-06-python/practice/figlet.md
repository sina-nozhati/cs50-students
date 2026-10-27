---
id: practice-6-figlet
type: practice
title: Frank, Ian and Glen’s Letters — Practice
week: 6
parent: week-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-command-line-arguments
- concept-python-basics
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/figlet/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:04+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- command-line-arguments
- frank-ian-and-glen-s-letters
- practice
- python-libraries
- sysargv
checksum: sha256:498f64c1d3fbc8bcf659c3671d54c4d5bdfb186cf77a6ddc39082666988d4797
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Frank, Ian and Glen’s Letters — Practice

## 1. Source metadata
- **Title:** Frank, Ian and Glen’s Letters — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/figlet/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:04+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/figlet/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="frank-ian-and-glens-letters"></a>

### Frank, Ian and Glen’s Letters

[FIGlet](https://en.wikipedia.org/wiki/FIGlet), named after [Frank, Ian, and Glen’s letters](https://www.figlet.org/faq.html), is a program from the early 1990s for making large letters out of ordinary text, a form of [ASCII art](https://en.wikipedia.org/wiki/ASCII_art):

```
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```

Among the fonts supported by FIGlet are those at [figlet.org/examples.html](https://www.figlet.org/examples.html).

FIGlet has since been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).

In a file called `figlet.py`, implement a program that:

* Expects zero or two command-line arguments:
  * Zero if the user would like to output text in a random font.
  * Two if the user would like to output text in a specific font, in which case the first of the two should be `-f` or `--font`, and the second of the two should be the name of the font.
* Prompts the user for a `str` of text.
* Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via `sys.exit` with an error message.

> **Hints** *(collapsible block on the source page)*
>
> * You can install `pyfiglet` with:
>
>   ```
>   pip install pyfiglet
>   ```
> * The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
>
>   ```py
>   from pyfiglet import Figlet
>
>   figlet = Figlet()
>   ```
>
>   You can then get a `list` of available fonts with code like this:
>
>   ```py
>   figlet.getFonts()
>   ```
>
>   You can set the font with code like this, wherein `f` is the font’s name as a `str`:
>
>   ```py
>   figlet.setFont(font=f)
>   ```
>
>   And you can output text in that font with code like this, wherein `s` is that text as a `str`:
>
>   ```py
>   print(figlet.renderText(s))
>   ```
> * Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

<a id="demo"></a>

#### Demo

This demo’s first output used a random font. Your output may vary.

[Terminal demo recording (asciinema): https://asciinema.org/a/LIo5QcHpUiXepVFiL4fTBwmuE]

<a id="before-you-begin"></a>

#### Before You Begin

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/6/figlet.zip` followed by Enter in order to download a zip called `figlet.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip figlet.zip` to create a folder called `figlet`.
5. You no longer need the ZIP file, so you can execute `rm figlet.zip` and respond with “y” followed by Enter at the prompt.

<a id="how-to-test"></a>

#### How to Test

Here’s how to test your code manually:

* Run your program with `python figlet.py test`. Your program should exit via `sys.exit` and print an error message:

  ```
  Invalid usage
  ```
* Run your program with `python figlet.py -a slant`. Your program should exit via `sys.exit` and print an error message:

  ```
  Invalid usage
  ```
* Run your program with `python figlet.py -f invalid_font`. Your program should exit via `sys.exit` and print an error message:

  ```
  Invalid usage
  ```
* Run your program with `python figlet.py -f slant`. Type `CS50`. Your program should print the following:

  ```
     ___________ __________
    / ____/ ___// ____/ __ \
   / /    \__ \/___ \/ / / /
  / /___ ___/ /___/ / /_/ /
  \____//____/_____/\____/
  ```
* Run your program with `python figlet.py -f rectangles`. Type `Hello, world`. Your program should print the following:

  ```
   _____     _ _                        _   _
  |  |  |___| | |___      _ _ _ ___ ___| |_| |
  |     | -_| | | . |_   | | | | . |  _| | . |
  |__|__|___|_|_|___| |  |_____|___|_| |_|___|
                    |_|
  ```
* Run your program with `python figlet.py -f alphabet`. Type `Moo`. Your program should print the following:

  ```
  M   M         
  MM MM         
  M M M ooo ooo
  M   M o o o o
  M   M ooo ooo
  ```

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/figlet
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/6/figlet.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `figlet/figlet.py` | 0 | [yes](figlet-distribution/files/figlet/figlet.py) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `figlet`; files shown on the page: `figlet.py`
- check50: `cs50/problems/2022/python/figlet`
- style50: not stated
- submit50: not stated
- Page sections (order on source): Demo, Before You Begin, How to Test, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python libraries، command-line arguments، sys.argv.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** From CS50P: use the pyfiglet library to render user text in large ASCII-art fonts, with an optional font selected via command-line arguments.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 6 — Python](../week.md) (`week-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Command-Line Arguments (argc, argv)](../../../concepts/command-line-arguments.md) (`concept-command-line-arguments`)
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین استفاده از کتابخانه‌های شخص ثالث و sys.argv در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. مستندات کتابخانه را برای فهم توابع لازم بخوان.
2. آرگومان‌های خط فرمان را با دقت اعتبارسنجی کن.

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2022/python/figlet` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/figlet/ — retrieved 2026-10-18T05:11:04+03:30, sha256 `498f64c1d3fbc8bc…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
