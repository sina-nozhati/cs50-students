---
id: concept-command-line
type: concept
title: Command-Line Interface and Linux Commands
week: 1
parent: concepts
children: []
prerequisites: []
related:
- short-command-line
- week-1-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/1/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:18+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- command-line
- concept
checksum: sha256:c782785752ff90a3516e9c720a63be3bd6b277cb1de0555c8a1637a0902c1481
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Command-Line Interface and Linux Commands

## 1. Source metadata
- **Title:** Command-Line Interface and Linux Commands
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/1/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:18+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that there is a file explorer on the left side where you can find your files. Further, notice that there is a region in the middle called a text editor where you can edit your program. Finally, there is a command line interface, known as a CLI, command line, or terminal window, where we can send commands to the computer in the cloud.
>
> — Week 1 notes, section “Visual Studio Code for CS50” (<https://cs50.harvard.edu/x/notes/1/#visual-studio-code-for-cs50>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#visual-studio-code-for-cs50))

> We can build your first program in C by typing code hello.c into the terminal window. Notice that we deliberately lowercased the entire filename and included the.c extension. Then, in the text editor that appears, write code as follows:
>
> — Week 1 notes, section “Hello World” (<https://cs50.harvard.edu/x/notes/1/#hello-world>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-world))

> Clicking back in the terminal window, you can compile your code by executing make hello. Notice that we are omitting.c. make is a build tool that will compile our hello.c file and turn it into a program called hello. If executing this command results in no errors, you can proceed. If not, double-check your code to ensure it matches the above.
>
> — Week 1 notes, section “Hello World” (<https://cs50.harvard.edu/x/notes/1/#hello-world>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-world))

> Typing./hello in the terminal window, how did your program change? This \ character is called an escape character that tells the compiler that \n is a special instruction to create a line break.
>
> — Week 1 notes, section “From Scratch to C” (<https://cs50.harvard.edu/x/notes/1/#from-scratch-to-c>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#from-scratch-to-c))

> Considering another data type called a char, we can start a new program by typing code agree.c into the terminal window.
>
> — Week 1 notes, section “agree.c” (<https://cs50.harvard.edu/x/notes/1/#agreec>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#agreec))

### Other lecture sections that mention this concept

- Week 2: [Arrays](../weeks/week-02-arrays/lecture.md#arrays), [Command-Line Arguments](../weeks/week-02-arrays/lecture.md#command-line-arguments), [Compiling](../weeks/week-02-arrays/lecture.md#compiling), [Debugging](../weeks/week-02-arrays/lecture.md#debugging), [Exit Status](../weeks/week-02-arrays/lecture.md#exit-status), [String Length](../weeks/week-02-arrays/lecture.md#string-length)
- Week 3: [Recursion](../weeks/week-03-algorithms/lecture.md#recursion), [phonebook.c](../weeks/week-03-algorithms/lecture.md#phonebookc), [search.c](../weeks/week-03-algorithms/lecture.md#searchc)
- Week 4: [Copying and malloc](../weeks/week-04-memory/lecture.md#copying-and-malloc), [Memory](../weeks/week-04-memory/lecture.md#memory), [String Comparison](../weeks/week-04-memory/lecture.md#string-comparison)
- Week 5: [Arrays](../weeks/week-05-data-structures/lecture.md#arrays)
- Week 6: [Calculator](../weeks/week-06-python/lecture.md#calculator), [Command-Line Arguments](../weeks/week-06-python/lecture.md#command-line-arguments), [Filter](../weeks/week-06-python/lecture.md#filter), [Hello Python!](../weeks/week-06-python/lecture.md#hello-python), [Speller](../weeks/week-06-python/lecture.md#speller), [Strings](../weeks/week-06-python/lecture.md#strings)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database), [IMDb](../weeks/week-07-sql/lecture.md#imdb), [Relational Databases](../weeks/week-07-sql/lecture.md#relational-databases)
- Week 8: [CSS](../weeks/week-08-html-css-javascript/lecture.md#css), [HTML](../weeks/week-08-html-css-javascript/lecture.md#html), [HTTPS](../weeks/week-08-html-css-javascript/lecture.md#https)
- Week 9: [Flask](../weeks/week-09-flask/lecture.md#flask), [Flask and SQL](../weeks/week-09-flask/lecture.md#flask-and-sql), [Frosh IMs](../weeks/week-09-flask/lecture.md#frosh-ims)
- Week 10: [Looking Ahead](../weeks/week-10/lecture.md#looking-ahead)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 1؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Short: Command Line](../weeks/week-01-c/shorts/command-line.md) (`short-command-line`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
رابط خط فرمان (CLI) روش کار با رایانه از طریق تایپ دستورها در ترمینال است؛ دستورهایی مثل cd، ls، mkdir و rm پایه‌ی کار در codespace هستند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/1/ — retrieved 2026-10-18T05:10:18+03:30, sha256 `c782785752ff90a3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bcommand[- ]line\b|\bterminal\b|\bcd\b|\bls\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
