---
id: concept-arrays
type: concept
title: Arrays
week: 2
parent: concepts
children: []
prerequisites: []
related:
- practice-2-hours
- practice-3-max
- practice-4-license
- pset-2-scrabble
- pset-2-substitution
- pset-3-plurality
- pset-3-runoff
- pset-3-tideman
- pset-4-filter-less
- pset-4-filter-more
- short-arrays
- week-2-lecture
- week-3-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/2/
- https://cs50.harvard.edu/x/notes/3/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:21+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- arrays
- concept
checksum: sha256:fa3b156e1bfc2fbeb77c6a14dd873548979a427fb5a6da2784ef3be4dc6a6b3a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Arrays

## 1. Source metadata
- **Title:** Arrays
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/2/>, <https://cs50.harvard.edu/x/notes/3/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:21+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/2/>, <https://cs50.harvard.edu/x/notes/3/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Arrays are a sequence of values that are stored back-to-back in memory.
>
> — Week 2 notes, section “Arrays” (<https://cs50.harvard.edu/x/notes/2/#arrays>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#arrays))

> Considering the following image, you can see how a string is an array of characters that begins with the first character and ends with a special character called a NUL character (note: NUL with one L is the ‘\0’ character, different from NULL with two L’s):
>
> — Week 2 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/2/#strings>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#strings))

> Notice how the printf statement presents three values from our array called s.
>
> — Week 2 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/2/#strings>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#strings))

> Notice that an array of words is created. It is an array of strings. Each word is stored in words.
>
> — Week 2 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/2/#strings>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#strings))

> The far-left position is called location 0 or the beginning of the array. The far-right position is location 6 or the end of the array.
>
> — Week 3 notes, section “Linear Search” (<https://cs50.harvard.edu/x/notes/3/#linear-search>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#linear-search))

### Other lecture sections that mention this concept

- Week 4: [Garbage Values](../weeks/week-04-memory/lecture.md#garbage-values), [String Comparison](../weeks/week-04-memory/lecture.md#string-comparison), [Strings](../weeks/week-04-memory/lecture.md#strings), [Valgrind](../weeks/week-04-memory/lecture.md#valgrind), [scanf](../weeks/week-04-memory/lecture.md#scanf)
- Week 5: [Arrays](../weeks/week-05-data-structures/lecture.md#arrays), [Hashing and Hash Tables](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables), [Linked Lists](../weeks/week-05-data-structures/lecture.md#linked-lists), [Queues](../weeks/week-05-data-structures/lecture.md#queues), [Stacks](../weeks/week-05-data-structures/lecture.md#stacks), [Trees](../weeks/week-05-data-structures/lecture.md#trees)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 2؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Hours — Practice](../weeks/week-02-arrays/practice/hours.md) (`practice-2-hours`)
  - [Max — Practice](../weeks/week-03-algorithms/practice/max.md) (`practice-3-max`)
  - [License — Practice](../weeks/week-04-memory/practice/license.md) (`practice-4-license`)
  - [Scrabble — Problem Set 2](../weeks/week-02-arrays/psets/scrabble.md) (`pset-2-scrabble`)
  - [Substitution (more comfortable) — Problem Set 2](../weeks/week-02-arrays/psets/substitution.md) (`pset-2-substitution`)
  - [Plurality — Problem Set 3](../weeks/week-03-algorithms/psets/plurality.md) (`pset-3-plurality`)
  - [Runoff (more or less comfortable) — Problem Set 3](../weeks/week-03-algorithms/psets/runoff.md) (`pset-3-runoff`)
  - [Tideman (very, very, very comfortable) — Problem Set 3](../weeks/week-03-algorithms/psets/tideman.md) (`pset-3-tideman`)
  - [Filter (less comfortable) — Problem Set 4](../weeks/week-04-memory/psets/filter-less.md) (`pset-4-filter-less`)
  - [Filter (more comfortable) — Problem Set 4](../weeks/week-04-memory/psets/filter-more.md) (`pset-4-filter-more`)
  - [Short: Arrays](../weeks/week-02-arrays/shorts/arrays.md) (`short-arrays`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
آرایه دنباله‌ای از مقادیر هم‌نوع است که پشت سر هم در حافظه ذخیره شده‌اند و با اندیس (از صفر) به آن‌ها دسترسی داریم.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/2/ — retrieved 2026-10-18T05:10:21+03:30, sha256 `fa3b156e1bfc2fbe…`
- https://cs50.harvard.edu/x/notes/3/ — retrieved 2026-10-18T05:10:24+03:30, sha256 `77e0896c7834b2b0…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\barrays?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
