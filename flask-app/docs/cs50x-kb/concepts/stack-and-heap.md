---
id: concept-stack-and-heap
type: concept
title: Stack, Heap and Call Stacks
week: 4
parent: concepts
children: []
prerequisites: []
related:
- short-call-stacks
- week-3-lecture
- week-4-lecture
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
- stack-and-heap
checksum: sha256:9776ed69bbe1af974ceb9a7b2b8098473b924513dda13b40456f8ba708a20bdd
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Stack, Heap and Call Stacks

## 1. Source metadata
- **Title:** Stack, Heap and Call Stacks
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/4/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/4/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that global variables, which we have not used in this course, live in one place in memory. Various functions are stored in the stack in another area of memory.
>
> — Week 4 notes, section “Swapping” (<https://cs50.harvard.edu/x/notes/4/#swapping>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#swapping))

> A heap overflow is when you overflow the heap, touching areas of memory you are not supposed to.
>
> — Week 4 notes, section “Overflow” (<https://cs50.harvard.edu/x/notes/4/#overflow>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#overflow))

> A stack overflow is when too many functions are called, overflowing the amount of memory available.
>
> — Week 4 notes, section “Overflow” (<https://cs50.harvard.edu/x/notes/4/#overflow>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#overflow))

### Other lecture sections that mention this concept

- Week 5: [Stacks](../weeks/week-05-data-structures/lecture.md#stacks)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 4؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Short: Call Stacks](../weeks/week-03-algorithms/shorts/call-stacks.md) (`short-call-stacks`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)
  - [Week 4 — Lecture notes (Memory)](../weeks/week-04-memory/lecture.md) (`week-4-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
حافظه‌ی برنامه بخش‌هایی دارد؛ stack برای فراخوانی توابع و متغیرهای محلی و heap برای حافظه‌ی پویا استفاده می‌شود.

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
- Passages were matched automatically with the regex `\bstack\b|\bheap\b|\bstack overflow\b|\bbuffer overflow\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
