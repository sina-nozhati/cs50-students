---
id: concept-python-basics
type: concept
title: Python Basics
week: 6
parent: concepts
children: []
prerequisites: []
related:
- practice-6-bank
- practice-6-figlet
- practice-7-prophecy
- pset-6-cash
- pset-6-credit
- pset-6-dna
- pset-6-hello
- pset-6-mario-less
- pset-6-mario-more
- pset-6-readability
- short-python
- week-6-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/6/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:34+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- python-basics
checksum: sha256:7878c7965cd69abedcf90c75ace1c4d81577271d80474c307228d7ff96288f84
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Python Basics

## 1. Source metadata
- **Title:** Python Basics
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/6/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:34+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/6/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Python is a programming language that builds upon what you have already learned in C.
>
> — Week 6 notes, section “Hello Python!” (<https://cs50.harvard.edu/x/notes/6/#hello-python>; KB: [week-6-lecture](../weeks/week-06-python/lecture.md#hello-python))

> Unlike in C, which is a compiled language, Python is an interpreted language, where you need not separately compile your program. Instead, you run your program in the Python Interpreter.
>
> — Week 6 notes, section “Hello Python!” (<https://cs50.harvard.edu/x/notes/6/#hello-python>; KB: [week-6-lecture](../weeks/week-06-python/lecture.md#hello-python))

> One of the trade-offs of using Python is an interpreted language, instead of being compiled (as we strictly defined earlier in the course). Accordingly, there is some (usually very small) slow-down that may not be expected in a compiled program.
>
> — Week 6 notes, section “Filter” (<https://cs50.harvard.edu/x/notes/6/#filter>; KB: [week-6-lecture](../weeks/week-06-python/lecture.md#filter))

> Data types in Python do not need to be explicitly declared. For example, you saw how answer above is a string, but we did not have to tell the interpreter this was the case: It knew on its own.
>
> — Week 6 notes, section “Types” (<https://cs50.harvard.edu/x/notes/6/#types>; KB: [week-6-lecture](../weeks/week-06-python/lecture.md#types))

> To further our understanding of loops and iteration in Python, let’s create a new file called uppercase.py as follows:
>
> — Week 6 notes, section “Loops” (<https://cs50.harvard.edu/x/notes/6/#loops>; KB: [week-6-lecture](../weeks/week-06-python/lecture.md#loops))

### Other lecture sections that mention this concept

- Week 0: [What’s Ahead](../weeks/week-00-scratch/lecture.md#whats-ahead)
- Week 5: [Welcome!](../weeks/week-05-data-structures/lecture.md#welcome)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database), [Summing Up](../weeks/week-07-sql/lecture.md#summing-up), [Using SQL in Python](../weeks/week-07-sql/lecture.md#using-sql-in-python), [Welcome!](../weeks/week-07-sql/lecture.md#welcome)
- Artificial Intelligence: [Prompt Engineering and Copilot](../weeks/week-ai-artificial-intelligence/lecture.md#prompt-engineering-and-copilot)
- Week 8: [Frameworks](../weeks/week-08-html-css-javascript/lecture.md#frameworks), [Welcome!](../weeks/week-08-html-css-javascript/lecture.md#welcome)
- Week 9: [Flask](../weeks/week-09-flask/lecture.md#flask), [Flask and SQL](../weeks/week-09-flask/lecture.md#flask-and-sql), [JSON](../weeks/week-09-flask/lecture.md#json), [Summing Up](../weeks/week-09-flask/lecture.md#summing-up), [Welcome!](../weeks/week-09-flask/lecture.md#welcome), [http-server](../weeks/week-09-flask/lecture.md#http-server)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 6؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Home Federal Savings Bank — Practice](../weeks/week-06-python/practice/bank.md) (`practice-6-bank`)
  - [Frank, Ian and Glen’s Letters — Practice](../weeks/week-06-python/practice/figlet.md) (`practice-6-figlet`)
  - [Hall of Prophecy — Practice](../weeks/week-07-sql/practice/prophecy.md) (`practice-7-prophecy`)
  - [Cash (less comfortable) — Problem Set 6](../weeks/week-06-python/psets/cash.md) (`pset-6-cash`)
  - [Credit (more comfortable) — Problem Set 6](../weeks/week-06-python/psets/credit.md) (`pset-6-credit`)
  - [DNA — Problem Set 6](../weeks/week-06-python/psets/dna.md) (`pset-6-dna`)
  - [Hello, Again — Problem Set 6](../weeks/week-06-python/psets/hello.md) (`pset-6-hello`)
  - [Mario (less comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-less.md) (`pset-6-mario-less`)
  - [Mario (more comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-more.md) (`pset-6-mario-more`)
  - [Readability — Problem Set 6](../weeks/week-06-python/psets/readability.md) (`pset-6-readability`)
  - [Short: Python](../weeks/week-06-python/shorts/python.md) (`short-python`)
  - [Week 6 — Lecture notes (Python)](../weeks/week-06-python/lecture.md) (`week-6-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
Python زبانی سطح بالا و تفسیری است که بسیاری از جزئیات C (مدیریت حافظه، اعلام نوع) را پنهان می‌کند و کتابخانه‌های غنی دارد.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/6/ — retrieved 2026-10-18T05:10:34+03:30, sha256 `7878c7965cd69abe…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bpython\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
