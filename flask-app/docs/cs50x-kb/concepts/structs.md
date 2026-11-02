---
id: concept-structs
type: concept
title: Structs and Custom Types (typedef)
week: 3
parent: concepts
children: []
prerequisites: []
related:
- practice-3-snackbar
- practice-3-temps
- practice-4-bottomup
- practice-5-trie
- pset-3-plurality
- pset-3-runoff
- pset-4-filter-less
- pset-4-filter-more
- pset-5-inheritance
- short-defining-custom-types
- short-structures
- week-3-lecture
- week-4-lecture
- week-5-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/3/
- https://cs50.harvard.edu/x/notes/4/
- https://cs50.harvard.edu/x/notes/5/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:24+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- structs
checksum: sha256:77e0896c7834b2b0847a1bbc39055410297f8a31720e610ea5fbd19dce7a33ac
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Structs and Custom Types (typedef)

## 1. Source metadata
- **Title:** Structs and Custom Types (typedef)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/3/>, <https://cs50.harvard.edu/x/notes/4/>, <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/3/>, <https://cs50.harvard.edu/x/notes/4/>, <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> It turns out that C allows us to create our own data types via a struct.
>
> — Week 3 notes, section “Structs” (<https://cs50.harvard.edu/x/notes/3/#structs>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#structs))

> Notice that the code begins with typedef struct where a new datatype called person is defined. Inside a person is a string called name and a string called number. In the main function, we begin by creating an array called people that is of type person that is of size 3. Then, we update the names and phone numbers of the three people in our people array. Most importantly, notice how the dot notation, such as people[0].name, allows us to access the person at the 0th location and assign that individual a name.
>
> — Week 3 notes, section “Structs” (<https://cs50.harvard.edu/x/notes/3/#structs>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#structs))

> Last week, we learned how to create your own data type as a struct.
>
> — Week 4 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/4/#strings>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#strings))

> The cs50 library includes a type definition as follows: typedef char *string
>
> — Week 4 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/4/#strings>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#strings))

> In recent weeks, you have learned about three useful primitives. A struct is a data type that you can define yourself. A. in dot notation allows you to access variables inside that structure. The * operator is used to declare a pointer or dereference a variable.
>
> — Week 5 notes, section “Linked Lists” (<https://cs50.harvard.edu/x/notes/5/#linked-lists>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#linked-lists))

### Other lecture sections that mention this concept

- Week 6: [Object-Oriented Programming](../weeks/week-06-python/lecture.md#object-oriented-programming)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 3؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Snackbar — Practice](../weeks/week-03-algorithms/practice/snackbar.md) (`practice-3-snackbar`)
  - [Average High Temperatures — Practice](../weeks/week-03-algorithms/practice/temps.md) (`practice-3-temps`)
  - [Bottom Up — Practice](../weeks/week-04-memory/practice/bottomup.md) (`practice-4-bottomup`)
  - [Trie — Practice](../weeks/week-05-data-structures/practice/trie.md) (`practice-5-trie`)
  - [Plurality — Problem Set 3](../weeks/week-03-algorithms/psets/plurality.md) (`pset-3-plurality`)
  - [Runoff (more or less comfortable) — Problem Set 3](../weeks/week-03-algorithms/psets/runoff.md) (`pset-3-runoff`)
  - [Filter (less comfortable) — Problem Set 4](../weeks/week-04-memory/psets/filter-less.md) (`pset-4-filter-less`)
  - [Filter (more comfortable) — Problem Set 4](../weeks/week-04-memory/psets/filter-more.md) (`pset-4-filter-more`)
  - [Inheritance — Problem Set 5](../weeks/week-05-data-structures/psets/inheritance.md) (`pset-5-inheritance`)
  - [Short: Defining Custom Types](../weeks/week-04-memory/shorts/defining-custom-types.md) (`short-defining-custom-types`)
  - [Short: Structures](../weeks/week-05-data-structures/shorts/structures.md) (`short-structures`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)
  - [Week 4 — Lecture notes (Memory)](../weeks/week-04-memory/lecture.md) (`week-4-lecture`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
struct چند مقدار مرتبط را در یک نوع داده‌ی جدید کنار هم قرار می‌دهد و typedef به آن نامی ساده‌تر می‌دهد.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/3/ — retrieved 2026-10-18T05:10:24+03:30, sha256 `77e0896c7834b2b0…`
- https://cs50.harvard.edu/x/notes/4/ — retrieved 2026-10-18T05:10:28+03:30, sha256 `9776ed69bbe1af97…`
- https://cs50.harvard.edu/x/notes/5/ — retrieved 2026-10-18T05:10:31+03:30, sha256 `3796458db78c64c5…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bstruct\b|\btypedef\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
