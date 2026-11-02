---
id: concept-dynamic-memory-allocation
type: concept
title: Dynamic Memory Allocation (malloc, free)
week: 4
parent: concepts
children: []
prerequisites: []
related:
- pset-4-recover
- pset-5-inheritance
- pset-5-speller
- short-dynamic-memory-allocation
- week-4-lecture
- week-5-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/4/
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
- dynamic-memory-allocation
checksum: sha256:9776ed69bbe1af974ceb9a7b2b8098473b924513dda13b40456f8ba708a20bdd
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Dynamic Memory Allocation (malloc, free)

## 1. Source metadata
- **Title:** Dynamic Memory Allocation (malloc, free)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/4/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/4/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that malloc(strlen(s) + 1) creates a block of memory that is the length of the string s plus one. This allows for the inclusion of the null \0 character in our final copied string. Then, the for loop walks through the string s and assigns each value to that same location on the string t. You can download this code here.
>
> — Week 4 notes, section “Copying and malloc” (<https://cs50.harvard.edu/x/notes/4/#copying-and-malloc>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#copying-and-malloc))

> Both get_string and malloc return NULL, a special value in memory, in the event that something goes wrong. You can write code that can check for this NULL condition as follows:
>
> — Week 4 notes, section “Copying and malloc” (<https://cs50.harvard.edu/x/notes/4/#copying-and-malloc>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#copying-and-malloc))

> Notice that if the string obtained is of length 0 or malloc fails, NULL is returned. Further, notice that free lets the computer know you are done with this block of memory you created via malloc. You can download this code here.
>
> — Week 4 notes, section “Copying and malloc” (<https://cs50.harvard.edu/x/notes/4/#copying-and-malloc>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#copying-and-malloc))

> Valgrind is a tool that can check to see if there are memory-related issues with your programs wherein you utilized malloc. Specifically, it checks to see if you free all the memory you allocated.
>
> — Week 4 notes, section “Valgrind” (<https://cs50.harvard.edu/x/notes/4/#valgrind>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#valgrind))

> Notice that running this program does not cause any errors. While malloc is used to allocate enough memory for an array, the code fails to free that allocated memory. You can download this code here.
>
> — Week 4 notes, section “Valgrind” (<https://cs50.harvard.edu/x/notes/4/#valgrind>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#valgrind))

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 4؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Recover — Problem Set 4](../weeks/week-04-memory/psets/recover.md) (`pset-4-recover`)
  - [Inheritance — Problem Set 5](../weeks/week-05-data-structures/psets/inheritance.md) (`pset-5-inheritance`)
  - [Speller — Problem Set 5](../weeks/week-05-data-structures/psets/speller.md) (`pset-5-speller`)
  - [Short: Dynamic Memory Allocation](../weeks/week-04-memory/shorts/dynamic-memory-allocation.md) (`short-dynamic-memory-allocation`)
  - [Week 4 — Lecture notes (Memory)](../weeks/week-04-memory/lecture.md) (`week-4-lecture`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
malloc حافظه را در زمان اجرا از heap می‌گیرد و free آن را برمی‌گرداند؛ هر حافظه‌ی گرفته‌شده باید دقیقاً یک بار آزاد شود.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/4/ — retrieved 2026-10-18T05:10:28+03:30, sha256 `9776ed69bbe1af97…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bmalloc\b|\bfree\b|\brealloc\b|\bheap\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
