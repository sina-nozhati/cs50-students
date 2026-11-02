---
id: concept-variables
type: concept
title: Variables
week: 0
parent: concepts
children: []
prerequisites: []
related:
- pset-0-scratch
- pset-1-me
- short-data-types
- short-variables-and-scope
- week-0-lecture
- week-1-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/0/
- https://cs50.harvard.edu/x/notes/1/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:16+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- variables
checksum: sha256:19cabb7558e628e3a2968377be2570125a4866712f959b0c0dad45909c39c712
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Variables

## 1. Source metadata
- **Title:** Variables
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that when the green flag is clicked, the function ask is run. The program prompts you, the user, What's your name? It then stores that name in the variable called answer. The program then passes answer to a special function called join, which combines two strings of text hello, and whatever name was provided. The value of answer is passed as an argument to join. These collectively are passed to the say function. The cat says, Hello, and a name. Your program is now interactive.
>
> — Week 0 notes, section “Hello, You” (<https://cs50.harvard.edu/x/notes/0/#hello-you>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#hello-you))

> answer is a special holding place we call a variable. answer is of type string and can hold any string within it. There are many data types, such as int, bool, char, and many others.
>
> — Week 1 notes, section “Hello, You” (<https://cs50.harvard.edu/x/notes/1/#hello-you>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-you))

> Notice how a variable called counter of type int is assigned the value 0.
>
> — Week 1 notes, section “Variables” (<https://cs50.harvard.edu/x/notes/1/#variables>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#variables))

> Notice that we create two variables, an int or integer called x and another called y. The values of these are populated using the get_int function.
>
> — Week 1 notes, section “compare.c” (<https://cs50.harvard.edu/x/notes/1/#comparec>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#comparec))

> Types refer to the possible data that can be stored in a variable. For example, a char is designed to accommodate a single character like a or 2.
>
> — Week 1 notes, section “Operators” (<https://cs50.harvard.edu/x/notes/1/#operators>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#operators))

### Other lecture sections that mention this concept

- Week 2: [Arrays](../weeks/week-02-arrays/lecture.md#arrays), [Debugging](../weeks/week-02-arrays/lecture.md#debugging)
- Week 4: [Pointers](../weeks/week-04-memory/lecture.md#pointers), [Swapping](../weeks/week-04-memory/lecture.md#swapping)
- Week 5: [Arrays](../weeks/week-05-data-structures/lecture.md#arrays), [Linked Lists](../weeks/week-05-data-structures/lecture.md#linked-lists)
- Week 6: [Abstraction](../weeks/week-06-python/lecture.md#abstraction), [Object-Oriented Programming](../weeks/week-06-python/lecture.md#object-oriented-programming), [Variables](../weeks/week-06-python/lecture.md#variables)
- Week 7: [SELECT](../weeks/week-07-sql/lecture.md#select)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 0؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Starting from Scratch — Problem Set 0](../weeks/week-00-scratch/psets/scratch.md) (`pset-0-scratch`)
  - [Hello, It’s Me — Problem Set 1](../weeks/week-01-c/psets/me.md) (`pset-1-me`)
  - [Short: Data Types](../weeks/week-01-c/shorts/data-types.md) (`short-data-types`)
  - [Short: Variables and Scope](../weeks/week-02-arrays/shorts/variables-and-scope.md) (`short-variables-and-scope`)
  - [Week 0 — Lecture notes (Scratch)](../weeks/week-00-scratch/lecture.md) (`week-0-lecture`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
متغیر نامی برای یک مقدار ذخیره‌شده در حافظه است. در C هر متغیر نوع مشخصی دارد که تعیین می‌کند چه داده‌ای و چند بایت در آن جا می‌گیرد.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/0/ — retrieved 2026-10-18T05:10:16+03:30, sha256 `19cabb7558e628e3…`
- https://cs50.harvard.edu/x/notes/1/ — retrieved 2026-10-18T05:10:18+03:30, sha256 `c782785752ff90a3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bvariables?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
