---
id: pset-3-sort
type: pset
title: Sort — Problem Set 3
week: 3
parent: pset-3
children: []
prerequisites:
- week-3-lecture
related:
- concept-algorithms-and-pseudocode
- concept-running-time-big-o
- concept-selection-and-bubble-sort
source_urls:
- https://cs50.harvard.edu/x/psets/3/sort/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:24+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C (analyse compiled programs; answers in a text file)
tags:
- best-vs-worst-case
- empirical-timing
- pset
- running-time-big-o
- sort
- sorting-algorithms
checksum: sha256:b0deb5c1555fc26c119993bd638290c82fe51f881554bf841d77ade63383c5ca
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Sort — Problem Set 3

## 1. Source metadata
- **Title:** Sort — Problem Set 3
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/3/sort/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/3/sort/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="sort"></a>

### Sort

<a id="problem-to-solve"></a>

#### Problem to Solve

Recall from lecture that we saw a few algorithms for sorting a sequence of numbers: selection sort, bubble sort, and merge sort.

* Selection sort iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location.
* Bubble sort compares pairs of adjacent values one at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
* Merge sort recursively divides the list into two repeatedly and then merges the smaller lists back into a larger one in the correct order.

In this problem, you’ll analyze three (compiled!) sorting programs to determine which algorithms they use. In a file called `answers.txt` in a folder called `sort`, record your answers, along with an explanation for each program, by filling in the blanks marked `TODO`.

<a id="distribution-code"></a>

#### Distribution Code

For this problem, you’ll need some “distribution code”—that is, code written by CS50’s staff. Provided to you are three already-compiled C programs, `sort1`, `sort2`, and `sort3`, as well as several `.txt` files for input and another file, `answers.txt`, in which to write your answers. Each of `sort1`, `sort2`, and `sort3` implements a different sorting algorithm: selection sort, bubble sort, or merge sort (though not necessarily in that order!). Your task is to determine which sorting algorithm is used by each file. Start by downloading these files.

> **Download distribution files** *(collapsible block on the source page)*
>
> Open [cs50.dev](https://cs50.dev/).
>
> Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.
>
> ```
> $
> ```
>
> Click inside of that terminal window and then execute
>
> ```
> wget https://cdn.cs50.net/2026/x/psets/3/sort.zip
> ```
>
> followed by Enter in order to download a ZIP called `sort.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
>
> Now execute
>
> ```
> unzip sort.zip
> ```
>
> to create a folder called `sort`. You no longer need the ZIP file, so you can execute
>
> ```
> rm sort.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

<a id="hints"></a>

#### Hints

> **Explore the .txt files** *(collapsible block on the source page)*
>
> * Multiple `.txt` files are provided to you. These files contain `n` lines of values, either reversed, shuffled, or sorted.
>   * For example, `reversed10000.txt` contains 10,000 lines of numbers that are reversed from `10000`, while `random50000.txt` contains 50,000 lines of numbers that are in random order.
> * The different types of `.txt` files may help you determine which sort is which. Consider how each algorithm performs with an already sorted list. How about a reversed list? Or shuffled list? It may help to work through a smaller list of each type and walk through each sorting process.

> **Time each sort with different inputs** *(collapsible block on the source page)*
>
> * To run the sorts on the text files, in the terminal, run `./[program_name] [text_file.txt]`. Make sure you have made use of `cd` to move into the `sort` directory!
>   * For example, to sort `reversed10000.txt` with `sort1`, run `./sort1 reversed10000.txt`.
> * You may find it helpful to time your sorts. To do so, run `time ./[sort_file] [text_file.txt]`.
>   * For example, you could run `time ./sort1 reversed10000.txt` to run `sort1` on 10,000 reversed numbers. At the end of your terminal’s output, you can look at the `real` time to see how much time actually elapsed while running the program.

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://video.cs50.io/-Bhxxw6JKKY](https://video.cs50.io/-Bhxxw6JKKY)

> **Not sure how to solve?** *(collapsible block on the source page)*
>

<a id="how-to-test"></a>

#### How to Test

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/sort
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/sort
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/3/sort.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `sort/sorted10000.txt` | 48894 | [yes](sort-distribution/files/sort/sorted10000.txt) |
| `sort/random10000.txt` | 48894 | [yes](sort-distribution/files/sort/random10000.txt) |
| `sort/reversed5000.txt` | 23893 | [yes](sort-distribution/files/sort/reversed5000.txt) |
| `sort/sorted5000.txt` | 23893 | [yes](sort-distribution/files/sort/sorted5000.txt) |
| `sort/reversed50000.txt` | 288894 | no — text file larger than 100 KB (inventory only) |
| `sort/random5000.txt` | 23893 | [yes](sort-distribution/files/sort/random5000.txt) |
| `sort/sort3` | 8368 | no — binary/media/data file (inventory only) |
| `sort/sort2` | 8448 | no — binary/media/data file (inventory only) |
| `sort/reversed10000.txt` | 48894 | [yes](sort-distribution/files/sort/reversed10000.txt) |
| `sort/answers.txt` | 125 | [yes](sort-distribution/files/sort/answers.txt) |
| `sort/random50000.txt` | 288894 | no — text file larger than 100 KB (inventory only) |
| `sort/sorted50000.txt` | 288894 | no — text file larger than 100 KB (inventory only) |
| `sort/sort1` | 8368 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C (analyse compiled programs; answers in a text file)
- Folder: `sort`; files shown on the page: `answers.txt`, `random50000.txt`, `reversed10000.txt`
- check50: `cs50/problems/2026/x/sort`
- style50: not stated
- submit50: `cs50/problems/2026/x/sort`
- Page sections (order on source): Problem to Solve, Distribution Code, Hints, Walkthrough, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم sorting algorithms، running time / Big O، best vs worst case، empirical timing.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Analyse three compiled sorting programs (sort1, sort2, sort3) and work out which uses selection sort, bubble sort or merge sort. Run them on the provided sorted, reversed and random number files and compare their running times. Record each answer, with an explanation, in answers.txt.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 3](README.md) (`pset-3`)
- **Prerequisites (generated):** [Week 3 — Lecture notes (Algorithms)](../lecture.md) (`week-3-lecture`)
- **Related:**
  - [Algorithms and Pseudocode](../../../concepts/algorithms-and-pseudocode.md) (`concept-algorithms-and-pseudocode`)
  - [Running Time, Big O, Omega, Theta](../../../concepts/running-time-big-o.md) (`concept-running-time-big-o`)
  - [Selection Sort and Bubble Sort](../../../concepts/selection-and-bubble-sort.md) (`concept-selection-and-bubble-sort`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
مقایسه‌ی تجربی الگوریتم‌های مرتب‌سازی و ارتباط زمان اجرا با Big O.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. زمان اجرای هر برنامه را روی فایل‌های مرتب، معکوس و تصادفی با اندازه‌های مختلف ثبت کن.
2. کدام الگوریتم روی ورودی از قبل مرتب‌شده سریع‌تر عمل می‌کند و چرا؟
3. نتیجه‌ها را با Big O و Omega هر الگوریتم در جزوه مقایسه کن.

### اشتباه‌های رایج (مفهومی)
- اکتفا به یک فایل ورودی
- توضیح نادادن استدلال در answers.txt

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/sort` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/3/sort/ — retrieved 2026-10-18T05:11:24+03:30, sha256 `b0deb5c1555fc26c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
