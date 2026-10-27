---
id: concept-functions
type: concept
title: Functions
week: 0
parent: concepts
children: []
prerequisites: []
related:
- practice-1-half
- practice-1-prime
- practice-3-max
- pset-1-cash
- pset-1-mario-less
- pset-2-readability
- pset-2-scrabble
- pset-3-plurality
- pset-5-speller
- pset-7-songs
- short-functions
- week-0-lecture
- week-1-lecture
- week-2-lecture
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
- functions
checksum: sha256:19cabb7558e628e3a2968377be2570125a4866712f959b0c0dad45909c39c712
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Functions

## 1. Source metadata
- **Title:** Functions
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that the input hello, world is passed to the function say, and the side effect of that function running is the cat saying hello, world.
>
> — Week 0 notes, section “Hello World” (<https://cs50.harvard.edu/x/notes/0/#hello-world>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#hello-world))

> Notice that when the green flag is clicked, the function ask is run. The program prompts you, the user, What's your name? It then stores that name in the variable called answer. The program then passes answer to a special function called join, which combines two strings of text hello, and whatever name was provided. The value of answer is passed as an argument to join. These collectively are passed to the say function. The cat says, Hello, and a name. Your program is now interactive.
>
> — Week 0 notes, section “Hello, You” (<https://cs50.harvard.edu/x/notes/0/#hello-you>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#hello-you))

> Notice that we are defining our own block called meow. The function plays the sound meow, and then waits one second. Below that, you can see that when the green flag is clicked, our meow function is repeated three times.
>
> — Week 0 notes, section “Meow, Loops, and Abstraction” (<https://cs50.harvard.edu/x/notes/0/#meow-loops-and-abstraction>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#meow-loops-and-abstraction))

> Notice that the printf function is called. The argument passed to printf is hello, world\n surrounded by double quotes. The statement of code is closed with a;.
>
> — Week 1 notes, section “From Scratch to C” (<https://cs50.harvard.edu/x/notes/1/#from-scratch-to-c>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#from-scratch-to-c))

> %s is a placeholder called a format code that tells the printf function to prepare to receive a string. answer is the string being passed to %s.
>
> — Week 1 notes, section “Hello, You” (<https://cs50.harvard.edu/x/notes/1/#hello-you>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-you))

### Other lecture sections that mention this concept

- Week 3: [Recursion](../weeks/week-03-algorithms/lecture.md#recursion), [Structs](../weeks/week-03-algorithms/lecture.md#structs)
- Week 4: [Copying and malloc](../weeks/week-04-memory/lecture.md#copying-and-malloc), [Overflow](../weeks/week-04-memory/lecture.md#overflow), [Swapping](../weeks/week-04-memory/lecture.md#swapping), [scanf](../weeks/week-04-memory/lecture.md#scanf)
- Week 5: [Arrays](../weeks/week-05-data-structures/lecture.md#arrays), [Hashing and Hash Tables](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables), [Linked Lists](../weeks/week-05-data-structures/lecture.md#linked-lists), [Trees](../weeks/week-05-data-structures/lecture.md#trees)
- Week 6: [Abstraction](../weeks/week-06-python/lecture.md#abstraction), [Calculator](../weeks/week-06-python/lecture.md#calculator), [Exit Status](../weeks/week-06-python/lecture.md#exit-status), [Functions](../weeks/week-06-python/lecture.md#functions), [Libraries, Modules, and Packages](../weeks/week-06-python/lecture.md#libraries-modules-and-packages), [Lists](../weeks/week-06-python/lecture.md#lists)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database), [Using SQL in Python](../weeks/week-07-sql/lecture.md#using-sql-in-python)
- Week 8: [JavaScript](../weeks/week-08-html-css-javascript/lecture.md#javascript)
- Week 9: [Flask](../weeks/week-09-flask/lecture.md#flask)
- Week 10: [Recap](../weeks/week-10/lecture.md#recap)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 0؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Half — Practice](../weeks/week-01-c/practice/half.md) (`practice-1-half`)
  - [Prime — Practice](../weeks/week-01-c/practice/prime.md) (`practice-1-prime`)
  - [Max — Practice](../weeks/week-03-algorithms/practice/max.md) (`practice-3-max`)
  - [Cash (less comfortable) — Problem Set 1](../weeks/week-01-c/psets/cash.md) (`pset-1-cash`)
  - [Mario (less comfortable) — Problem Set 1](../weeks/week-01-c/psets/mario-less.md) (`pset-1-mario-less`)
  - [Readability — Problem Set 2](../weeks/week-02-arrays/psets/readability.md) (`pset-2-readability`)
  - [Scrabble — Problem Set 2](../weeks/week-02-arrays/psets/scrabble.md) (`pset-2-scrabble`)
  - [Plurality — Problem Set 3](../weeks/week-03-algorithms/psets/plurality.md) (`pset-3-plurality`)
  - [Speller — Problem Set 5](../weeks/week-05-data-structures/psets/speller.md) (`pset-5-speller`)
  - [Songs — Problem Set 7](../weeks/week-07-sql/psets/songs.md) (`pset-7-songs`)
  - [Short: Functions](../weeks/week-02-arrays/shorts/functions.md) (`short-functions`)
  - [Week 0 — Lecture notes (Scratch)](../weeks/week-00-scratch/lecture.md) (`week-0-lecture`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
تابع یک قطعه‌کد نام‌دار است که ورودی (آرگومان) می‌گیرد، کاری انجام می‌دهد و ممکن است مقداری برگرداند یا اثر جانبی (مثل چاپ) داشته باشد.

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
- Passages were matched automatically with the regex `\bfunctions?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
