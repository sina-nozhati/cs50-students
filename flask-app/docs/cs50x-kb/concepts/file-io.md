---
id: concept-file-io
type: concept
title: File I/O (fopen, fread, fwrite, fclose)
week: 4
parent: concepts
children: []
prerequisites: []
related:
- practice-4-bottomup
- practice-4-license
- pset-4-recover
- pset-4-volume
- pset-6-dna
- short-file-pointers
- week-4-lecture
- week-6-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/4/
- https://cs50.harvard.edu/x/notes/6/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:28+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- file-io
checksum: sha256:9776ed69bbe1af974ceb9a7b2b8098473b924513dda13b40456f8ba708a20bdd
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# File I/O (fopen, fread, fwrite, fclose)

## 1. Source metadata
- **Title:** File I/O (fopen, fread, fwrite, fclose)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/4/>, <https://cs50.harvard.edu/x/notes/6/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/4/>, <https://cs50.harvard.edu/x/notes/6/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> You can read from and manipulate files. While this topic will be discussed further in a future week, consider the following code for phonebook.c:
>
> — Week 4 notes, section “File I/O” (<https://cs50.harvard.edu/x/notes/4/#file-io>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#file-io))

> Notice that this code uses pointers to access the file. You can download this code here.
>
> — Week 4 notes, section “File I/O” (<https://cs50.harvard.edu/x/notes/4/#file-io>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#file-io))

> You can create a file called phonebook.csv in advance of running the above code or download phonebook.csv. After running the above program and inputting a name and phone number, you will notice that this data persists in your CSV file.
>
> — Week 4 notes, section “File I/O” (<https://cs50.harvard.edu/x/notes/4/#file-io>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#file-io))

> Notice that this file creates our own data type called a BYTE, which is equivalent to the size of a uint8_t. Then, the file reads a BYTE and writes it to a file. You can download this code here.
>
> — Week 4 notes, section “File I/O” (<https://cs50.harvard.edu/x/notes/4/#file-io>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#file-io))

> Further, you can create a new file called edges.py as follows:
>
> — Week 6 notes, section “Filter” (<https://cs50.harvard.edu/x/notes/6/#filter>; KB: [week-6-lecture](../weeks/week-06-python/lecture.md#filter))

### Other lecture sections that mention this concept

- Week 1: [Header Files and CS50 Manual Pages](../weeks/week-01-c/lecture.md#header-files-and-cs50-manual-pages), [Hello World](../weeks/week-01-c/lecture.md#hello-world), [Linux](../weeks/week-01-c/lecture.md#linux), [Visual Studio Code for CS50](../weeks/week-01-c/lecture.md#visual-studio-code-for-cs50)
- Week 2: [Compiling](../weeks/week-02-arrays/lecture.md#compiling), [Debugging](../weeks/week-02-arrays/lecture.md#debugging), [String Length](../weeks/week-02-arrays/lecture.md#string-length)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database), [Indexes](../weeks/week-07-sql/lecture.md#indexes), [Relational Databases](../weeks/week-07-sql/lecture.md#relational-databases), [Summing Up](../weeks/week-07-sql/lecture.md#summing-up), [Using SQL in Python](../weeks/week-07-sql/lecture.md#using-sql-in-python)
- Week 8: [CSS](../weeks/week-08-html-css-javascript/lecture.md#css), [Frameworks](../weeks/week-08-html-css-javascript/lecture.md#frameworks), [HTML](../weeks/week-08-html-css-javascript/lecture.md#html), [HTTPS](../weeks/week-08-html-css-javascript/lecture.md#https), [JavaScript](../weeks/week-08-html-css-javascript/lecture.md#javascript), [Routers](../weeks/week-08-html-css-javascript/lecture.md#routers)
- Week 9: [Cookies and Session](../weeks/week-09-flask/lecture.md#cookies-and-session), [Flask](../weeks/week-09-flask/lecture.md#flask), [Flask and SQL](../weeks/week-09-flask/lecture.md#flask-and-sql), [Frosh IMs](../weeks/week-09-flask/lecture.md#frosh-ims), [JSON](../weeks/week-09-flask/lecture.md#json), [Request Methods](../weeks/week-09-flask/lecture.md#request-methods)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 4؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Bottom Up — Practice](../weeks/week-04-memory/practice/bottomup.md) (`practice-4-bottomup`)
  - [License — Practice](../weeks/week-04-memory/practice/license.md) (`practice-4-license`)
  - [Recover — Problem Set 4](../weeks/week-04-memory/psets/recover.md) (`pset-4-recover`)
  - [Volume — Problem Set 4](../weeks/week-04-memory/psets/volume.md) (`pset-4-volume`)
  - [DNA — Problem Set 6](../weeks/week-06-python/psets/dna.md) (`pset-6-dna`)
  - [Short: File Pointers](../weeks/week-04-memory/shorts/file-pointers.md) (`short-file-pointers`)
  - [Week 4 — Lecture notes (Memory)](../weeks/week-04-memory/lecture.md) (`week-4-lecture`)
  - [Week 6 — Lecture notes (Python)](../weeks/week-06-python/lecture.md) (`week-6-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
برنامه‌ها با باز کردن فایل، خواندن/نوشتن بایت‌ها یا متن و بستن آن با داده‌ی ماندگار کار می‌کنند؛ در C این کار با اشاره‌گر FILE انجام می‌شود.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/4/ — retrieved 2026-10-18T05:10:28+03:30, sha256 `9776ed69bbe1af97…`
- https://cs50.harvard.edu/x/notes/6/ — retrieved 2026-10-18T05:10:34+03:30, sha256 `7878c7965cd69abe…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bfopen\b|\bfclose\b|\bfread\b|\bfwrite\b|\bfprintf\b|\bFILE\b|\bfiles?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
