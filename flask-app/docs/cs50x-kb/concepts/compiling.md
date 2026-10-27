---
id: concept-compiling
type: concept
title: Compiling (preprocessing, compiling, assembling, linking)
week: 1
parent: concepts
children: []
prerequisites: []
related:
- practice-1-debug
- pset-1-world
- week-1-lecture
- week-2-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/1/
- https://cs50.harvard.edu/x/notes/2/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:18+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- compiling
- concept
checksum: sha256:c782785752ff90a3516e9c720a63be3bd6b277cb1de0555c8a1637a0902c1481
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Compiling (preprocessing, compiling, assembling, linking)

## 1. Source metadata
- **Title:** Compiling (preprocessing, compiling, assembling, linking)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/1/>, <https://cs50.harvard.edu/x/notes/2/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:18+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/1/>, <https://cs50.harvard.edu/x/notes/2/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> It turns out that we can convert source code into machine code using a very special piece of software called a compiler. Today, we will be introducing you to a compiler that will allow you to convert source code in the programming language C into machine code.
>
> — Week 1 notes, section “Source Code” (<https://cs50.harvard.edu/x/notes/1/#source-code>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#source-code))

> The first command, code hello.c creates a file and allows us to type instructions for this program. The second command, make hello, compiles the file from our instructions in C and creates an executable file called hello. The last command,./hello, runs the program called hello.
>
> — Week 1 notes, section “Hello World” (<https://cs50.harvard.edu/x/notes/1/#hello-world>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-world))

> Clicking back in the terminal window, you can compile your code by executing make hello. Notice that we are omitting.c. make is a build tool that will compile our hello.c file and turn it into a program called hello. If executing this command results in no errors, you can proceed. If not, double-check your code to ensure it matches the above.
>
> — Week 1 notes, section “Hello World” (<https://cs50.harvard.edu/x/notes/1/#hello-world>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-world))

> Looking at the errors, string and get_string are not recognized by the compiler. We need to provide the compiler with these definitions by adding a library called cs50.h. Also, we notice that answer is not provided as we intended. Modify your code as follows:
>
> — Week 1 notes, section “Hello, You” (<https://cs50.harvard.edu/x/notes/1/#hello-you>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-you))

> int scores[3] is a way of telling the compiler to provide you three back-to-back places in memory of size int to store three scores. Considering our program, you can revise your code as follows:
>
> — Week 2 notes, section “Arrays” (<https://cs50.harvard.edu/x/notes/2/#arrays>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#arrays))

### Other lecture sections that mention this concept

- Week 0: [Hello, You](../weeks/week-00-scratch/lecture.md#hello-you), [Ivy’s Hardest Game](../weeks/week-00-scratch/lecture.md#ivys-hardest-game), [RGB](../weeks/week-00-scratch/lecture.md#rgb)
- Week 3: [search.c](../weeks/week-03-algorithms/lecture.md#searchc)
- Week 4: [Copying and malloc](../weeks/week-04-memory/lecture.md#copying-and-malloc), [Garbage Values](../weeks/week-04-memory/lecture.md#garbage-values), [Hexadecimal](../weeks/week-04-memory/lecture.md#hexadecimal), [Strings](../weeks/week-04-memory/lecture.md#strings), [Swapping](../weeks/week-04-memory/lecture.md#swapping), [Valgrind](../weeks/week-04-memory/lecture.md#valgrind)
- Week 5: [Data Structures](../weeks/week-05-data-structures/lecture.md#data-structures), [Hashing and Hash Tables](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables)
- Week 6: [Abstraction](../weeks/week-06-python/lecture.md#abstraction), [Filter](../weeks/week-06-python/lecture.md#filter), [Hello Python!](../weeks/week-06-python/lecture.md#hello-python), [Speller](../weeks/week-06-python/lecture.md#speller)
- Artificial Intelligence: [Decision Trees](../weeks/week-ai-artificial-intelligence/lecture.md#decision-trees), [Large Language Models](../weeks/week-ai-artificial-intelligence/lecture.md#large-language-models)
- Week 8: [HTML](../weeks/week-08-html-css-javascript/lecture.md#html), [Regular Expressions](../weeks/week-08-html-css-javascript/lecture.md#regular-expressions), [Routers](../weeks/week-08-html-css-javascript/lecture.md#routers)
- Week 9: [Cookies and Session](../weeks/week-09-flask/lecture.md#cookies-and-session), [Flask](../weeks/week-09-flask/lecture.md#flask)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 1؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Debug — Practice](../weeks/week-01-c/practice/debug.md) (`practice-1-debug`)
  - [Hello, World — Problem Set 1](../weeks/week-01-c/psets/world.md) (`pset-1-world`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
کامپایل فرایند تبدیل کد منبع قابل‌خواندن برای انسان به کد ماشین است و در C شامل پیش‌پردازش، کامپایل، اسمبل و لینک می‌شود.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/1/ — retrieved 2026-10-18T05:10:18+03:30, sha256 `c782785752ff90a3…`
- https://cs50.harvard.edu/x/notes/2/ — retrieved 2026-10-18T05:10:21+03:30, sha256 `fa3b156e1bfc2fbe…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bcompil(e|er|ing|ed)\b|\bclang\b|\bmake\b|\blinking\b|\bassembl`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
