---
id: concept-pointers
type: concept
title: Pointers
week: 4
parent: concepts
children: []
prerequisites: []
related:
- practice-4-license
- practice-5-trie
- pset-4-filter-less
- pset-4-volume
- pset-5-inheritance
- short-pointers
- week-4-lecture
- week-5-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/4/
- https://cs50.harvard.edu/x/notes/5/
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
- pointers
checksum: sha256:9776ed69bbe1af974ceb9a7b2b8098473b924513dda13b40456f8ba708a20bdd
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Pointers

## 1. Source metadata
- **Title:** Pointers
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/4/>, <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/4/>, <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> A pointer is a variable that stores the address of something. Most succinctly, a pointer is an address in your computer’s memory.
>
> — Week 4 notes, section “Pointers” (<https://cs50.harvard.edu/x/notes/4/#pointers>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#pointers))

> Notice that p is a pointer that contains the address of an integer n.
>
> — Week 4 notes, section “Pointers” (<https://cs50.harvard.edu/x/notes/4/#pointers>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#pointers))

> Notice how a pointer called s tells the compiler where the first byte of the string exists in memory.
>
> — Week 4 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/4/#strings>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#strings))

> Pointer arithmetic is the ability to do math on locations of memory.
>
> — Week 4 notes, section “Pointer Arithmetic” (<https://cs50.harvard.edu/x/notes/4/#pointer-arithmetic>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#pointer-arithmetic))

> By convention, we would keep one more element in memory, a pointer, that keeps track of the first item in the list, called the head of the list.
>
> — Week 5 notes, section “Linked Lists” (<https://cs50.harvard.edu/x/notes/5/#linked-lists>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#linked-lists))

### Other lecture sections that mention this concept

- Week 0: [Conditionals](../weeks/week-00-scratch/lecture.md#conditionals)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 4؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [License — Practice](../weeks/week-04-memory/practice/license.md) (`practice-4-license`)
  - [Trie — Practice](../weeks/week-05-data-structures/practice/trie.md) (`practice-5-trie`)
  - [Filter (less comfortable) — Problem Set 4](../weeks/week-04-memory/psets/filter-less.md) (`pset-4-filter-less`)
  - [Volume — Problem Set 4](../weeks/week-04-memory/psets/volume.md) (`pset-4-volume`)
  - [Inheritance — Problem Set 5](../weeks/week-05-data-structures/psets/inheritance.md) (`pset-5-inheritance`)
  - [Short: Pointers](../weeks/week-04-memory/shorts/pointers.md) (`short-pointers`)
  - [Week 4 — Lecture notes (Memory)](../weeks/week-04-memory/lecture.md) (`week-4-lecture`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
اشاره‌گر متغیری است که آدرس یک مقدار دیگر را نگه می‌دارد؛ عملگر & آدرس را می‌دهد و عملگر * به مقدارِ آن آدرس می‌رود.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/4/ — retrieved 2026-10-18T05:10:28+03:30, sha256 `9776ed69bbe1af97…`
- https://cs50.harvard.edu/x/notes/5/ — retrieved 2026-10-18T05:10:31+03:30, sha256 `3796458db78c64c5…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bpointers?\b|\bdereferenc`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
