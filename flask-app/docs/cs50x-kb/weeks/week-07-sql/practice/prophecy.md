---
id: practice-7-prophecy
type: practice
title: Hall of Prophecy — Practice
week: 7
parent: week-7
children: []
prerequisites:
- week-7-lecture
related:
- concept-python-basics
- concept-sql-basics
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/prophecy/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:09+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- SQL
tags:
- create-insert
- database-normalization
- hall-of-prophecy
- practice
- python-sql
checksum: sha256:89a8ffd9696cd7fa34686b300ba23af40642bc707b38f5e4f5fde83f6f33b389
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hall of Prophecy — Practice

## 1. Source metadata
- **Title:** Hall of Prophecy — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/prophecy/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:09+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/prophecy/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="hall-of-prophecy"></a>

### Hall of Prophecy

<a id="learning-goals"></a>

#### Learning Goals

* “Refactor” a `SQL` database to eliminate redundancies
* Use `SELECT`, `CREATE`, and `INSERT` statements to reorganize data
* Write Python to load new `SQL` tables

![Hall of Prophecy](https://cs50.harvard.edu/x/practice/prophecy/prophecy.jpg)

<a id="background"></a>

#### Background

The keeper of the Hall of Prophecy, whose job entailed labelling records and keeping them up to date, decided to create a SQL database of Hogwarts students. Unfortunately the database was poorly designed! The database, `roster.db`, contains only one table, `students`, with the name and head of each of the four Hogwarts Houses.

Stumbling upon this database, you decide it could be better designed. Take a look at `roster.db` and notice how the name and head of each house repeats over and over. A better design would contain a students table (for *only* students), a houses table (for *only* houses), and a table that codifies the relationship between students and houses. This process of changing the “schema” of a database is known as [refactoring](https://en.wikipedia.org/wiki/Database_refactoring).

* Hint
  * You can view the data in the Hall of Prophecy’s table by executing `sqlite3 roster.db`, followed by `.schema` in your `sqlite3` prompt. This will output the `CREATE TABLE` statement that was used to generate the `students` table.
  * You can then use `SELECT` statements to view the contents of this table.

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/7/prophecy.zip` followed by Enter in order to download a zip called `prophecy.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip prophecy.zip` to create a folder called `prophecy`.
5. You no longer need the ZIP file, so you can execute `rm prophecy.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

You will use the existing data in `roster.db` to create a new database, one with a table for students, a table for houses, and a table for house assignments. You can do this with individual `SQL` queries, though we recommend ultimately writing your own Python program to automate the process! Notice we’ve given you the data from the `students` table of `roster.db` in CSV format, `students.csv`, for your convenience.

<a id="developing-a-schema"></a>

##### Developing a Schema

First, let’s develop a new schema for the database. In `schema.sql`, document the three `CREATE TABLE` commands you’ll need to create your three new tables.

Keep in mind you’ll want each table to represent a single entity: that is, your students table should represent *only* students, your houses table should represent only *houses*, and your house assignments table should represent *only* house assignments. You might find it helpful to first consider the pieces of information you’ll need in each table, and then about which SQLite data type best represents that information. For example, this was the `CREATE TABLE` command for `students`:

```sql
CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);
```

Keep in mind that every table should have a primary key: a column that uniquely identifies every row in the table. Some tables may be best designed with foreign keys: columns that reference the primary keys of another table.

When you’re ready to configure your database with your new schema, run your three new `CREATE TABLE` queries. Type `.schema` to see your results.

<a id="inserting-data"></a>

##### Inserting Data

After you’ve configured your database with your new schema, you can begin inserting data into your new database (using your new schema!). It’s best to write a Python program here, which can save you the trouble of writing many `INSERT` queries. Keep in mind that you have `students.csv`, which contains the data from the previous database’s `students` table.

<a id="thought-question"></a>

#### Thought Question

* Why do you think it’s considered better design not to repeat information like houses and heads for each student?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

You’ll likely find the following commands helpful for testing your code:

* `.schema` to check the schema of your database
* `SELECT * FROM table;` where `table` is the name of the table you’d like to see data from

No `check50` for this one!

<a id="how-to-submit"></a>

#### How to Submit

No need to submit. This is a practice problem!

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/7/prophecy.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `prophecy/schema.sql` | 0 | [yes](prophecy-distribution/files/prophecy/schema.sql) |
| `prophecy/roster.db` | 8192 | no — binary/media/data file (inventory only) |
| `prophecy/students.csv` | 1869 | [yes](prophecy-distribution/files/prophecy/students.csv) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): SQL
- Folder: `prophecy`; files shown on the page: `roster.db`, `schema.sql`, `students.csv`
- check50: No check50 (stated)
- style50: not stated
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم database normalization، CREATE/INSERT، Python + SQL.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Refactor a poorly designed roster.db of Hogwarts students into separate students, houses and relationship tables, loading the data with Python.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Week 7 — SQL](../week.md) (`week-7`)
- **Prerequisites (generated):** [Week 7 — Lecture notes (SQL)](../lecture.md) (`week-7-lecture`)
- **Related:**
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین طراحی و نرمال‌سازی پایگاه داده.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. داده‌ی تکراری را در جدول‌های جدا بگذار و با کلید به هم وصل کن.
2. رابطه‌ی چند‌به‌چند به چه جدولی نیاز دارد؟

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
- https://cs50.harvard.edu/x/practice/prophecy/ — retrieved 2026-10-18T05:11:09+03:30, sha256 `89a8ffd9696cd7fa…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
