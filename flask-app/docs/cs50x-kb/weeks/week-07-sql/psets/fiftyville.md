---
id: pset-7-fiftyville
type: pset
title: Fiftyville — Problem Set 7
week: 7
parent: pset-7
children: []
prerequisites:
- week-7-lecture
related:
- concept-sql-basics
- concept-sql-joins-and-keys
source_urls:
- https://cs50.harvard.edu/x/psets/7/fiftyville/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:44+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- SQL
tags:
- fiftyville
- investigative-reasoning
- joins
- pset
- sql-comments
- sql-querying
checksum: sha256:20acd7880925d30ce67181b834923b11ffde262ea297f07e43fd792ba55320f3
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Fiftyville — Problem Set 7

## 1. Source metadata
- **Title:** Fiftyville — Problem Set 7
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/7/fiftyville/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:44+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/7/fiftyville/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="fiftyville"></a>

### Fiftyville

<a id="problem-to-solve"></a>

#### Problem to Solve

The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify:

* Who the thief is,
* What city the thief escaped to, and
* Who the thief’s accomplice is who helped them escape

All you know is that the theft **took place on July 28, 2025** and that it **took place on Humphrey Street**.

How will you go about solving this mystery? The Fiftyville authorities have taken some of the town’s records from around the time of the theft and prepared a SQLite database for you, `fiftyville.db`, which contains tables of data from around the town. You can query that table using SQL `SELECT` queries to access the data of interest to you. Using just the information in the database, your task is to solve the mystery.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/YgI5fyTP939jINCZm7l3o7WCY]

<a id="getting-started"></a>

#### Getting Started

For this problem, you’ll use a database provided to you by CS50’s staff.

> **Download the distribution code** *(collapsible block on the source page)*
>
> Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:
>
> ```
> $
> ```
>
> Next execute
>
> ```
> wget https://cdn.cs50.net/2026/x/psets/7/fiftyville.zip
> ```
>
> in order to download a ZIP called `fiftyville.zip` into your codespace.
>
> Then execute
>
> ```
> unzip fiftyville.zip
> ```
>
> to create a folder called `fiftyville`. You no longer need the ZIP file, so you can execute
>
> ```
> rm fiftyville.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd fiftyville
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> fiftyville/ $
> ```
>
> Execute `ls` by itself, and you should see a few files:
>
> ```
> answers.txt  fiftyville.db  log.sql
> ```
>
> If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

<a id="specification"></a>

#### Specification

For this problem, equally as important as solving the mystery itself is the process that you use to solve the mystery. In `log.sql`, keep a log of all SQL queries that you run on the database. Above each query, label each with a comment (in SQL, comments are any lines that begin with `--`) describing why you’re running the query and/or what information you’re hoping to get out of that particular query. You can use comments in the log file to add additional notes about your thought process as you solve the mystery: ultimately, this file should serve as evidence of the process you used to identify the thief!

As you write your queries, you may notice that some of them can become quite complex. To help keep your queries readable, see principles of good style at [sqlstyle.guide](https://www.sqlstyle.guide). The [indentation](https://www.sqlstyle.guide/#indentation) section may be particularly helpful!

Once you solve the mystery, complete each of the lines in `answers.txt` by filling in the name of the thief, the city that the thief escaped to, and the name of the thief’s accomplice who helped them escape town. (Be sure not to change any of the existing text in the file or to add any other lines to the file!)

Ultimately, you should submit both your `log.sql` and `answers.txt` files.

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/YHhgEoJMDnU](https://www.youtube.com/embed/YHhgEoJMDnU)

<a id="hints"></a>

#### Hints

* Execute `sqlite3 fiftyville.db` to begin running queries on the database.
  * While running `sqlite3`, executing `.tables` will list all of the tables in the database.
  * While running `sqlite3`, executing `.schema TABLE_NAME`, where `TABLE_NAME` is the name of a table in the database, will show you the `CREATE TABLE` command used to create the table. This can be helpful for knowing which columns to query!
* You may find it helpful to start with the `crime_scene_reports` table. Start by looking for a crime scene report that matches the date and the location of the crime.
* See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!

<a id="how-to-test"></a>

#### How to Test

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/fiftyville
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/fiftyville
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/7/fiftyville.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `fiftyville/log.sql` | 72 | [yes](fiftyville-distribution/files/fiftyville/log.sql) |
| `fiftyville/answers.txt` | 64 | [yes](fiftyville-distribution/files/fiftyville/answers.txt) |
| `fiftyville/fiftyville.db` | 278528 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): SQL
- Folder: `fiftyville`; files shown on the page: `answers.txt`, `fiftyville.db`, `log.sql`
- check50: `cs50/problems/2026/x/fiftyville`
- style50: not stated
- submit50: `cs50/problems/2026/x/fiftyville`
- Page sections (order on source): Problem to Solve, Demo, Getting Started, Specification, Walkthrough, Hints, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/YHhgEoJMDnU
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم SQL querying، JOINs، investigative reasoning، SQL comments.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Solve a mystery with SQL: the CS50 Duck was stolen in Fiftyville on July 28, 2025 on Humphrey Street. Query fiftyville.db to identify the thief, the city they escaped to and their accomplice. Log every query with explanatory comments in log.sql, and record the answers in answers.txt.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Problem Set 7](README.md) (`pset-7`)
- **Prerequisites (generated):** [Week 7 — Lecture notes (SQL)](../lecture.md) (`week-7-lecture`)
- **Related:**
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)
  - [Primary Keys, Foreign Keys and JOINs](../../../concepts/sql-joins-and-keys.md) (`concept-sql-joins-and-keys`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
حل یک معمای کارآگاهی با SQL؛ تمرین کاوش داده و مستندسازی استدلال.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. از گزارش جرم شروع کن و هر سرنخ را به یک پرس‌وجوی جدید تبدیل کن.
2. در log.sql هر پرس‌وجو را همراه با توضیح اینکه چه چیزی فهمیدی ثبت کن.
3. فهرست مظنونان را با تقاطع سرنخ‌ها کوچک کن.

### اشتباه‌های رایج (مفهومی)
- نوشتن پاسخ بدون پرس‌وجوهای پشتیبان در log

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/fiftyville` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/7/fiftyville/ — retrieved 2026-10-18T05:11:44+03:30, sha256 `20acd7880925d30c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
