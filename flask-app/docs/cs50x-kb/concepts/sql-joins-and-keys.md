---
id: concept-sql-joins-and-keys
type: concept
title: Primary Keys, Foreign Keys and JOINs
week: 7
parent: concepts
children: []
prerequisites: []
related:
- pset-7-fiftyville
- pset-7-movies
- pset-7-songs
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
- sql-joins-and-keys
checksum: sha256:a8e4860d454734029be5ba3feb3c875257e82350407e2ee739be9b075a92e6d7
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Primary Keys, Foreign Keys and JOINs

## 1. Source metadata
- **Title:** Primary Keys, Foreign Keys and JOINs
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/7/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/7/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> A reference to the show’s id exists in all tables. In the shows table, it is simply called id. This common field among all the tables is called a key. Primary keys are used to identify a unique record in a table. Foreign keys are used to build relationships between tables by pointing to the primary key in another table. You can see in the schema of ratings that show_id is a foreign key that references id in shows.
>
> — Week 7 notes, section “IMDb” (<https://cs50.harvard.edu/x/notes/7/#imdb>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#imdb))

> How could we combine tables temporarily? Tables could be joined together using the JOIN command.
>
> — Week 7 notes, section “JOIN s” (<https://cs50.harvard.edu/x/notes/7/#joins>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#joins))

> This could be expressed as a JOIN as:
>
> — Week 7 notes, section “JOIN s” (<https://cs50.harvard.edu/x/notes/7/#joins>; KB: [week-7-lecture](../weeks/week-07-sql/lecture.md#joins))

### Other lecture sections that mention this concept

- Week 0: [Hello, You](../weeks/week-00-scratch/lecture.md#hello-you)
- Week 5: [Queues](../weeks/week-05-data-structures/lecture.md#queues)
- Week 10: [Final Project](../weeks/week-10/lecture.md#final-project), [Looking Ahead](../weeks/week-10/lecture.md#looking-ahead)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 7؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Fiftyville — Problem Set 7](../weeks/week-07-sql/psets/fiftyville.md) (`pset-7-fiftyville`)
  - [Movies — Problem Set 7](../weeks/week-07-sql/psets/movies.md) (`pset-7-movies`)
  - [Songs — Problem Set 7](../weeks/week-07-sql/psets/songs.md) (`pset-7-songs`)
  - [Week 7 — Lecture notes (SQL)](../weeks/week-07-sql/lecture.md) (`week-7-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
کلید اصلی هر سطر را یکتا مشخص می‌کند و کلید خارجی به سطری در جدول دیگر اشاره می‌کند؛ JOIN جدول‌ها را بر اساس این رابطه‌ها ترکیب می‌کند.

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
- Passages were matched automatically with the regex `\bJOIN\b|\bprimary key\b|\bforeign key\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
