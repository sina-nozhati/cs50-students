---
id: practice-6-seven-day-average
type: practice
title: Seven Day Averages — Practice
week: 6
parent: week-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-dictionaries
- concept-exceptions
- concept-internet-and-http
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/seven-day-average/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:06+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- csvdictreader
- dicts-and-lists
- exceptions
- http-requests
- practice
- seven-day-averages
checksum: sha256:f92e7c2c34012d9913929ede1ee6735716e7e5ea9302b58132cc28c3cc6c5571
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Seven Day Averages — Practice

## 1. Source metadata
- **Title:** Seven Day Averages — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/seven-day-average/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:06+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/seven-day-average/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="seven-day-averages"></a>

### Seven Day Averages

<a id="learning-goals"></a>

#### Learning Goals

* Work with live data
* Get practice with CSV files and `csv.DictReader`
* Practice using dictionaries, lists and exceptions

![sevendaysavg](https://cs50.harvard.edu/x/practice/seven-day-average/seven-day-averages.png)

<a id="background"></a>

#### Background

A popular way to track COVID cases is using a 7-day average. Some states only record cases once a week, so using a 7-day average is much more accurate than daily numbers. In this program, you will be using a [New York Times repository](https://github.com/nytimes/covid-19-data) of live, cumulative COVID data to calculate new daily cases, create a 7-day average, and compare this week’s average to the previous week.

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/6/seven-day-average.zip` followed by Enter in order to download a zip called `seven-day-average.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip seven-day-average.zip` to create a folder called `seven-day-average`.
5. You no longer need the ZIP file, so you can execute `rm seven-day-average.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

The distribution code for this problem uses the python `requests` library to access the New York Times data stored in an accessible GitHub repository. This is stored as a CSV file. The program then uses `DictReader` to read the CSV file. It then creates a `states` list to use selected states for calculations.

You will be completing two functions, `calculate` and `comparative_averages`.

<a id="calculate"></a>

##### `calculate`

In `calculate`, you’ll be creating a dictionary, `new_cases`, which will keep track of 14 days of new COVID cases for each state. Keys in this `dict` will be the names of states, and the values for each of those keys will be the most recent 14 days of new cases. Since the data from the New York Times is cumulative, each day’s new cases must be calculated by subtracting the previous day’s cases. To do this, you may want to create a second dictionary, `previous_cases`, that keeps track of each day’s new cases as it’s calculated.

* Hint
  * You can store 14 values in the list for each state by appending each new day’s data to end of the list and when the length of the list is greater than 14, removing the first element from the list.

Your `calculate` function should ultimately return the `new_cases` dictionary.

<a id="comparative_averages"></a>

##### `comparative_averages`

Since your `new_cases` dictionary is passed to this function, you can calculate this week’s 7-day average by summing up the *last* 7 elements in the list for a selected state, then dividing this by 7. You can create a 7-day average for the previous week by doing the same with the *first* 7 elements in that same list.

* Hint
  * Check out python list slicing to easily access a range of elements in a list. For example, `values[3:5]` will return the 3rd through 4th indexed elements in the list `values`. Note that the second index is *not* inclusive.

You can then calculate the percent increase or decrease, by taking the difference of the two 7-day averages and dividing by last week’s average.

* Hint
  * Note that you can detect division by zero by handling a `ZeroDivisionError` with a `try` and `except` block. For example:

  ```python
  try:
      numerator / denominator
  except ZeroDivisionError:
      ...
  ```

  Take a look at Week 3 in [CS50P](https://cs50.harvard.edu/python/2022/weeks/3/) for more on exceptions in Python.

<a id="thought-question"></a>

#### Thought Question

Why do you think some websites, such as [The Washington Post](https://www.washingtonpost.com/graphics/2020/national/coronavirus-us-cases-deaths/?state=US) post different values than your program generates for “Average daily new cases” and “Change in avg. daily cases in last 7 days” for some states, and the same values for others?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
seven-day-average/ $ python seven-day-average.py
Choose one or more states to view average COVID cases.
Press enter when done.

State: Massachusetts
State: New York
State: 

Seven-Day Averages
Massachusetts had a 7-day average of 1646 and an increase of 46%.
New York had a 7-day average of 7502 and a decrease of 1%.
```

```
seven-day-average/ $ python seven-day-average.py
Choose one or more states to view average COVID cases.
Press enter when done.

State: Maine
State: California
State: 

Seven-Day Averages
California had a 7-day average of 20461 and a decrease of 8%.
Maine had a 7-day average of 196 and a decrease of 10%.
```

Do note that the numbers will vary each day, since the data you are using is updated daily.

No `check50` for this one!

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 seven-day-average.py
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/6/seven-day-average.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `seven-day-average/seven-day-average.py` | 1128 | [yes](seven-day-average-distribution/files/seven-day-average/seven-day-average.py) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `seven-day-average`; files shown on the page: `seven-day-average.py`
- check50: No check50 (stated)
- style50: `seven-day-average.py`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم csv.DictReader، dicts and lists، HTTP requests، exceptions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Use live New York Times COVID data (CSV) to compute new daily cases, 7-day averages and week-over-week change for chosen states.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Week 6 — Python](../week.md) (`week-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Dictionaries (dict)](../../../concepts/dictionaries.md) (`concept-dictionaries`)
  - [Exceptions](../../../concepts/exceptions.md) (`concept-exceptions`)
  - [Internet, TCP/IP, DNS and HTTP](../../../concepts/internet-and-http.md) (`concept-internet-and-http`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین CSV از وب، دیکشنری و محاسبه‌ی میانگین متحرک در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. داده‌ها را بر اساس ایالت گروه‌بندی کن.
2. فقط به داده‌های اخیر نیاز داری؛ کدام ساختار داده برای این کار مناسب است؟

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
- https://cs50.harvard.edu/x/practice/seven-day-average/ — retrieved 2026-10-18T05:11:06+03:30, sha256 `f92e7c2c34012d99…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
