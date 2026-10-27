---
id: concept-sql-basics
type: concept
title: SQL and Relational Databases
week: 7
parent: concepts
children: []
prerequisites: []
related:
- practice-7-favorites
- practice-7-prophecy
- pset-7-fiftyville
- pset-7-movies
- pset-7-songs
- pset-8-homepage
- pset-9-birthdays
- pset-9-finance
- short-sql
- week-7-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/7/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:37+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- sql-basics
checksum: sha256:a8e4860d454734029be5ba3feb3c875257e82350407e2ee739be9b075a92e6d7
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# SQL and Relational Databases

## 1. Source metadata
- **Title:** SQL and Relational Databases
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/7/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/7/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Relational databases store data in rows and columns in structures called tables.
>
> — Week 7 notes, section “Relational Databases” (<https://cs50.harvard.edu/x/notes/7/#relational-databases>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#relational-databases))

> sqlite3 is a type of SQL database that has the core features required for this course.
>
> — Week 7 notes, section “Relational Databases” (<https://cs50.harvard.edu/x/notes/7/#relational-databases>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#relational-databases))

> We could separate our database into multiple sheets. We could have a shows sheet, a stars sheet, and a people sheet. On the people sheet, each person could have a unique id. On the shows sheet, each show could have a unique id too. On a third sheet called stars we could relate people to shows by having a show_id and person_id. While this is an improvement, this is not an ideal database.
>
> — Week 7 notes, section “IMDb” (<https://cs50.harvard.edu/x/notes/7/#imdb>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#imdb))

> Let’s zero in on the relationship between two tables within the database called shows and ratings. The relationship between these two tables can be illustrated as follows:
>
> — Week 7 notes, section “IMDb” (<https://cs50.harvard.edu/x/notes/7/#imdb>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#imdb))

> A reference to the show’s id exists in all tables. In the shows table, it is simply called id. This common field among all the tables is called a key. Primary keys are used to identify a unique record in a table. Foreign keys are used to build relationships between tables by pointing to the primary key in another table. You can see in the schema of ratings that show_id is a foreign key that references id in shows.
>
> — Week 7 notes, section “IMDb” (<https://cs50.harvard.edu/x/notes/7/#imdb>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#imdb))

### Other lecture sections that mention this concept

- Week 5: [Hashing and Hash Tables](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables)
- Week 8: [CSS](../weeks/week-08-html-css-javascript/lecture.md#css), [DNS](../weeks/week-08-html-css-javascript/lecture.md#dns), [HTML](../weeks/week-08-html-css-javascript/lecture.md#html)
- Week 9: [APIs](../weeks/week-09-flask/lecture.md#apis), [Cookies and Session](../weeks/week-09-flask/lecture.md#cookies-and-session), [Flask and SQL](../weeks/week-09-flask/lecture.md#flask-and-sql), [JSON](../weeks/week-09-flask/lecture.md#json), [Shopping Cart](../weeks/week-09-flask/lecture.md#shopping-cart), [Summing Up](../weeks/week-09-flask/lecture.md#summing-up)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 7؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Favorites — Practice](../weeks/week-07-sql/practice/favorites.md) (`practice-7-favorites`)
  - [Hall of Prophecy — Practice](../weeks/week-07-sql/practice/prophecy.md) (`practice-7-prophecy`)
  - [Fiftyville — Problem Set 7](../weeks/week-07-sql/psets/fiftyville.md) (`pset-7-fiftyville`)
  - [Movies — Problem Set 7](../weeks/week-07-sql/psets/movies.md) (`pset-7-movies`)
  - [Songs — Problem Set 7](../weeks/week-07-sql/psets/songs.md) (`pset-7-songs`)
  - [Homepage — Problem Set 8](../weeks/week-08-html-css-javascript/psets/homepage.md) (`pset-8-homepage`)
  - [Birthdays — Problem Set 9](../weeks/week-09-flask/psets/birthdays.md) (`pset-9-birthdays`)
  - [C$50 Finance — Problem Set 9](../weeks/week-09-flask/psets/finance.md) (`pset-9-finance`)
  - [Short: SQL](../weeks/week-07-sql/shorts/sql.md) (`short-sql`)
  - [Week 7 — Lecture notes (SQL)](../weeks/week-07-sql/lecture.md) (`week-7-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
SQL زبانی برای ایجاد، خواندن، به‌روزرسانی و حذف داده (CRUD) در پایگاه داده‌ی رابطه‌ای است که داده را در جدول‌هایی از سطر و ستون نگه می‌دارد.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/7/ — retrieved 2026-10-18T05:10:37+03:30, sha256 `a8e4860d45473402…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bSQL\b|\bSELECT\b|\bdatabases?\b|\btables?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
