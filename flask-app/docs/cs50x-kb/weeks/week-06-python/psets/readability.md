---
id: pset-6-readability
type: pset
title: Readability — Problem Set 6
week: 6
parent: pset-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-python-basics
- concept-strings
- pset-2-readability
source_urls:
- https://cs50.harvard.edu/x/psets/6/readability/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:40+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- counting
- pset
- python-string-methods
- readability
- rounding
checksum: sha256:6bf586418cee597dc8b875709b8d136412a855323faa9a2afd07b3740635b4f4
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Readability — Problem Set 6

## 1. Source metadata
- **Title:** Readability — Problem Set 6
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/6/readability/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:40+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/6/readability/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="readability"></a>

### Readability

<a id="problem-to-solve"></a>

#### Problem to Solve

Write, in a file called `readability.py` in a folder called `sentimental-readability`, a program that first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula, exactly as you did in [Problem Set 2](https://cs50.harvard.edu/x/psets/2/), except that your program this time should be written in Python.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/WnE6pZNnDkDm8NtuxrTqY1Nu4]

<a id="specification"></a>

#### Specification

* Recall that the Coleman-Liau index is computed as `0.0588 * L - 0.296 * S - 15.8`, where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.
* Use `get_string` from the CS50 Library to get the user’s input, and `print` to output your answer.
* Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase character from `a` to `z` or any uppercase character from `A` to `Z`, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
* Your program should print as output `"Grade X"` where `X` is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
* If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output `"Grade 16+"` instead of giving the exact index number. If the index number is less than 1, your program should output `"Before Grade 1"`.

<a id="how-to-test"></a>

#### How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

* Run your program as `python readability.py`, and wait for a prompt for input. Type in `One fish. Two fish. Red fish. Blue fish.` and press enter. Your program should output `Before Grade 1`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` and press enter. Your program should output `Grade 2`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `Congratulations! Today is your day. You're off to Great Places! You're off and away!` and press enter. Your program should output `Grade 3`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` and press enter. Your program should output `Grade 5`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` and press enter. Your program should output `Grade 7`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` and press enter. Your program should output `Grade 8`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` and press enter. Your program should output `Grade 8`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` and press enter. Your program should output `Grade 9`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` and press enter. Your program should output `Grade 10`.
* Run your program as `python readability.py`, and wait for a prompt for input. Type in `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` and press enter. Your program should output `Grade 16+`.

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/sentimental/readability
```

<a id="style"></a>

##### Style

```
style50 readability.py
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/sentimental/readability
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `sentimental-readability`; files shown on the page: `readability.py`
- check50: `cs50/problems/2026/x/sentimental/readability`
- style50: `readability.py`
- submit50: `cs50/problems/2026/x/sentimental/readability`
- Page sections (order on source): Problem to Solve, Demo, Specification, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python string methods، counting، rounding.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Re-implement Readability in Python (readability.py in folder sentimental-readability). It computes the Coleman-Liau grade level of user-entered text, with the same output rules as the C version.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 6](README.md) (`pset-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Readability — Problem Set 2](../../week-02-arrays/psets/readability.md) (`pset-2-readability`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
بازنویسی Readability در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. همان تعریف‌های حرف، کلمه و جمله را حفظ کن.
2. متدهای رشته در Python چطور کار شمارش را ساده‌تر می‌کنند؟

### اشتباه‌های رایج (مفهومی)
- تفاوت گرد کردن با نسخه‌ی C

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/sentimental/readability` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/6/readability/ — retrieved 2026-10-18T05:11:40+03:30, sha256 `6bf586418cee597d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
