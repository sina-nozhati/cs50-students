---
id: concept-loops
type: concept
title: Loops
week: 0
parent: concepts
children: []
prerequisites: []
related:
- practice-1-prime
- practice-6-taqueria
- pset-0-scratch
- pset-1-mario-less
- pset-1-mario-more
- pset-6-mario-less
- pset-6-mario-more
- short-loops
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
- loops
checksum: sha256:19cabb7558e628e3a2968377be2570125a4866712f959b0c0dad45909c39c712
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Loops

## 1. Source metadata
- **Title:** Loops
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> While AI provides huge advancements, sometimes eliminating the human bottlenecks that can slow down processes, being able to understand, create, and organize code allows you to be a driver, a pilot, an empowered creator through programming.
>
> — Week 0 notes, section “Welcome!” (<https://cs50.harvard.edu/x/notes/0/#welcome>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#welcome))

> While the pattern of zeros and ones is standardized within Unicode, each device manufacturer may display each emoji slightly differently than another manufacturer.
>
> — Week 0 notes, section “Unicode” (<https://cs50.harvard.edu/x/notes/0/#unicode>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#unicode))

> Notice that the loop does exactly as the previous program did. However, the problem is simplified by abstracting away the repetition to a block that repeats the code for us.
>
> — Week 0 notes, section “Meow, Loops, and Abstraction” (<https://cs50.harvard.edu/x/notes/0/#meow-loops-and-abstraction>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#meow-loops-and-abstraction))

> Another tool in our toolbox for looping is a for loop.
>
> — Week 1 notes, section “Loops and meow.c” (<https://cs50.harvard.edu/x/notes/1/#loops-and-meowc>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#loops-and-meowc))

> Notice that the for loop includes three arguments. The first argument int i = 0 starts our counter at zero. The second argument i < 3 is the condition that is being checked. Finally, the argument i++ tells the loop to increment by one each time the loop runs.
>
> — Week 1 notes, section “Loops and meow.c” (<https://cs50.harvard.edu/x/notes/1/#loops-and-meowc>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#loops-and-meowc))

### Other lecture sections that mention this concept

- Week 2: [Arrays](../weeks/week-02-arrays/lecture.md#arrays), [Compiling](../weeks/week-02-arrays/lecture.md#compiling), [Debugging](../weeks/week-02-arrays/lecture.md#debugging), [String Length](../weeks/week-02-arrays/lecture.md#string-length)
- Week 3: [Recursion](../weeks/week-03-algorithms/lecture.md#recursion), [phonebook.c](../weeks/week-03-algorithms/lecture.md#phonebookc), [search.c](../weeks/week-03-algorithms/lecture.md#searchc)
- Week 4: [Copying and malloc](../weeks/week-04-memory/lecture.md#copying-and-malloc), [File I/O](../weeks/week-04-memory/lecture.md#file-io), [Garbage Values](../weeks/week-04-memory/lecture.md#garbage-values), [Swapping](../weeks/week-04-memory/lecture.md#swapping), [Valgrind](../weeks/week-04-memory/lecture.md#valgrind)
- Week 5: [Arrays](../weeks/week-05-data-structures/lecture.md#arrays), [Hashing and Hash Tables](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables), [Linked Lists](../weeks/week-05-data-structures/lecture.md#linked-lists)
- Week 6: [Abstraction](../weeks/week-06-python/lecture.md#abstraction), [CSV Files](../weeks/week-06-python/lecture.md#csv-files), [Calculator](../weeks/week-06-python/lecture.md#calculator), [Loops](../weeks/week-06-python/lecture.md#loops), [Mario](../weeks/week-06-python/lecture.md#mario), [Speller](../weeks/week-06-python/lecture.md#speller)
- Week 7: [IMDb](../weeks/week-07-sql/lecture.md#imdb), [Indexes](../weeks/week-07-sql/lecture.md#indexes)
- Week 8: [CSS](../weeks/week-08-html-css-javascript/lecture.md#css), [Regular Expressions](../weeks/week-08-html-css-javascript/lecture.md#regular-expressions)
- Week 9: [Cookies and Session](../weeks/week-09-flask/lecture.md#cookies-and-session), [JSON](../weeks/week-09-flask/lecture.md#json)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 0؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Prime — Practice](../weeks/week-01-c/practice/prime.md) (`practice-1-prime`)
  - [Felipe’s Taqueria — Practice](../weeks/week-06-python/practice/taqueria.md) (`practice-6-taqueria`)
  - [Starting from Scratch — Problem Set 0](../weeks/week-00-scratch/psets/scratch.md) (`pset-0-scratch`)
  - [Mario (less comfortable) — Problem Set 1](../weeks/week-01-c/psets/mario-less.md) (`pset-1-mario-less`)
  - [Mario (more comfortable) — Problem Set 1](../weeks/week-01-c/psets/mario-more.md) (`pset-1-mario-more`)
  - [Mario (less comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-less.md) (`pset-6-mario-less`)
  - [Mario (more comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-more.md) (`pset-6-mario-more`)
  - [Short: Loops](../weeks/week-01-c/shorts/loops.md) (`short-loops`)
  - [Week 0 — Lecture notes (Scratch)](../weeks/week-00-scratch/lecture.md) (`week-0-lecture`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
حلقه یک بخش از کد را تکرار می‌کند؛ for برای تعداد تکرار معین، while برای تکرار تا وقتی شرطی برقرار است، و do-while برای حداقل یک بار اجرا مناسب‌اند.

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
- Passages were matched automatically with the regex `\bloops?\b|\bwhile\b|\bfor\b loop|do while`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
