---
id: practice-7-favorites
type: practice
title: Favorites — Practice
week: 7
parent: week-7
children: []
prerequisites:
- week-7-lecture
related:
- concept-sql-basics
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/favorites/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:08+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- SQL
tags:
- data-cleaning
- favorites
- practice
- sql-select
- sql-update
checksum: sha256:9bc9ba248c802a3a81603dcc7c3be89ece447caa91f59d716e07fad04bdd08d5
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Favorites — Practice

## 1. Source metadata
- **Title:** Favorites — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/favorites/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:08+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/favorites/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="favorites"></a>

### Favorites

<a id="learning-goals"></a>

#### Learning Goals

* Become familiar with SQL
* Practice using `SELECT` and `UPDATE` operations

<a id="background"></a>

#### Background

In 2021’s Week 7 lecture, we created a SQL database, `favorites.db`, with a table of CS50 students’ favorite TV shows. As often happens when importing raw data, however, we have some inconsistencies and typos to take care of (lest our queries become clumsy and our results inaccurate!).

Your job is to use the SQL `UPDATE` keyword to clean up this database, so it can be more effectively used for analysis.

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/7/favorites.zip` followed by Enter in order to download a zip called `favorites.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip favorites.zip` to create a folder called `favorites`.
5. You no longer need the ZIP file, so you can execute `rm favorites.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

Let’s first take a look at the data. Recall that you’ll need to use [SQLite](https://www.sqlite.org/index.html), a lightweight “database engine”, to open `favorites.db`. We’ll use the third (and latest) version of SQLite. You can open `favorites.db`, then, by executing

```bash
sqlite3 favorites.db
```

so long as your terminal’s working directory is the same directory in which `favorites.db` is located.

In your `sqlite3` prompt, try executing

```sql
.schema
```

to see the commands used to create the two tables in this database, `shows` and `genres`.

Now try viewing the data inside of `shows` by executing

```sql
SELECT * FROM shows;
```

Scrolling up, notice that the very first title in `shows` already looks like it might pose a problem. We want “How i met your mother” to be title-cased! Let’s `UPDATE` this title by executing

```sql
UPDATE shows SET title = "How I Met Your Mother" WHERE title = "How i met your mother";
```

While you *could* retype each incorrectly entered show title, it’s much more efficient to select muliple variations of the same show and `UPDATE` these to the correct spelling. Maybe the `LIKE` keyword could come in handy! There are many titles to clean up, including all of the below:

* Adventure Time
* Arrow
* Avatar: The Last Airbender
* Brooklyn Nine-Nine
* Community
* Family Guy
* Friends
* Game of Thrones
* Gilmore Girls
* Grey’s Anatomy
* How I Met Your Mother
* It’s Always Sunny in Philadelphia
* Parks and Recreation
* Sherlock
* Squid Game
* The Bachelorette
* The Crown
* The Office
* The Queen’s Gambit
* The Untamed

If pressed for time, though, some of the more interesting clean-ups involve these shows:

* Brooklyn Nine-Nine
* Game of Thrones
* Grey’s Anatomy
* It’s Always Sunny in Philadelphia
* Parks and Recreation
* The Office

Be sure to save each of these SQL statements to store in a new file `favorites.sql`.

<a id="thought-question"></a>

#### Thought Question

* Why do you think it’s necessary to “clean” data when you can use the SQL `LIKE` statement?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Once you have completed all of your database `UPDATE`s, you may want to `SELECT` all titles and list these alphabetically to make sure that all are correct.

No `check50` for this one!

<a id="how-to-submit"></a>

#### How to Submit

No need to submit. This is a practice problem!

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/7/favorites.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `favorites/favorites.db` | 20480 | no — binary/media/data file (inventory only) |
| `favorites/favorites.sql` | 0 | [yes](favorites-distribution/files/favorites/favorites.sql) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): SQL
- Folder: `favorites`; files shown on the page: `favorites.db`, `favorites.sql`
- check50: No check50 (stated)
- style50: not stated
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم SQL UPDATE، SQL SELECT، data cleaning.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Clean up inconsistencies and typos in a favorites.db table of students' favourite TV shows using SQL UPDATE statements, recorded in favorites.sql.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 7 — SQL](../week.md) (`week-7`)
- **Prerequisites (generated):** [Week 7 — Lecture notes (SQL)](../lecture.md) (`week-7-lecture`)
- **Related:**
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین UPDATE و پاک‌سازی داده با SQL.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. قبل از UPDATE، با SELECT ببین کدام سطرها تغییر خواهند کرد.

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
- https://cs50.harvard.edu/x/practice/favorites/ — retrieved 2026-10-18T05:11:08+03:30, sha256 `9bc9ba248c802a3a…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
