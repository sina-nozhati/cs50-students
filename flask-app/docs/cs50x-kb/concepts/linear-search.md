---
id: concept-linear-search
type: concept
title: Linear Search
week: 3
parent: concepts
children: []
prerequisites: []
related:
- practice-3-snackbar
- pset-3-plurality
- short-linear-search
- week-3-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/3/
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
- linear-search
checksum: sha256:77e0896c7834b2b0847a1bbc39055410297f8a31720e610ea5fbd19dce7a33ac
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Linear Search

## 1. Source metadata
- **Title:** Linear Search
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/3/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/3/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Linear search was of order \(O(n)\) because it could take n steps in the worst case to run.
>
> — Week 3 notes, section “Running Time” (<https://cs50.harvard.edu/x/notes/3/#running-time>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#running-time))

> You can implement linear search by typing code search.c in your terminal window and writing code as follows:
>
> — Week 3 notes, section “search.c” (<https://cs50.harvard.edu/x/notes/3/#searchc>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#searchc))

> Notice that the line beginning with int numbers[] allows us to define the values of each element of the array as we create it. Then, in the for loop, we have an implementation of linear search. return 0 is used to indicate success and exit the program. return 1 is used to exit the program with an error (failure).
>
> — Week 3 notes, section “search.c” (<https://cs50.harvard.edu/x/notes/3/#searchc>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#searchc))

> We have now implemented linear search ourselves in C!
>
> — Week 3 notes, section “search.c” (<https://cs50.harvard.edu/x/notes/3/#searchc>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#searchc))

> Binary search and linear search.
>
> — Week 3 notes, section “Summing Up” (<https://cs50.harvard.edu/x/notes/3/#summing-up>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#summing-up))

### Other lecture sections that mention this concept

- Week 6: [Searching and Dictionaries](../weeks/week-06-python/lecture.md#searching-and-dictionaries)

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
  - [Plurality — Problem Set 3](../weeks/week-03-algorithms/psets/plurality.md) (`pset-3-plurality`)
  - [Short: Linear Search](../weeks/week-03-algorithms/shorts/linear-search.md) (`short-linear-search`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
جستجوی خطی عناصر را یکی‌یکی از ابتدا بررسی می‌کند؛ ساده است و روی داده‌ی نامرتب هم کار می‌کند اما در بدترین حالت n گام لازم دارد.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/3/ — retrieved 2026-10-18T05:10:24+03:30, sha256 `77e0896c7834b2b0…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\blinear search\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
