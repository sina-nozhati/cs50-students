---
id: concept-binary-search
type: concept
title: Binary Search
week: 3
parent: concepts
children: []
prerequisites: []
related:
- short-binary-search
- week-0-lecture
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
- binary-search
- concept
checksum: sha256:77e0896c7834b2b0847a1bbc39055410297f8a31720e610ea5fbd19dce7a33ac
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Binary Search

## 1. Source metadata
- **Title:** Binary Search
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/3/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/3/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Binary search is another search algorithm that could be employed in our task of finding the 50.
>
> — Week 3 notes, section “Binary Search” (<https://cs50.harvard.edu/x/notes/3/#binary-search>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#binary-search))

> Assuming that the values within the lockers have been arranged from smallest to largest, the pseudocode for binary search would appear as follows:
>
> — Week 3 notes, section “Binary Search” (<https://cs50.harvard.edu/x/notes/3/#binary-search>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#binary-search))

> Binary search was of order \(O(\log n)\) because it would take fewer and fewer steps to run, even in the worst case.
>
> — Week 3 notes, section “Running Time” (<https://cs50.harvard.edu/x/notes/3/#running-time>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#running-time))

> When a list is sorted, searching that list is far less taxing on the computer. Recall that we can use binary search on a sorted list but not on an unsorted one.
>
> — Week 3 notes, section “Sorting and Selection Sort” (<https://cs50.harvard.edu/x/notes/3/#sorting-and-selection-sort>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#sorting-and-selection-sort))

> Binary search and linear search.
>
> — Week 3 notes, section “Summing Up” (<https://cs50.harvard.edu/x/notes/3/#summing-up>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#summing-up))

### Other lecture sections that mention this concept

- Week 5: [Linked Lists](../weeks/week-05-data-structures/lecture.md#linked-lists), [Trees](../weeks/week-05-data-structures/lecture.md#trees)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 3؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Short: Binary Search](../weeks/week-03-algorithms/shorts/binary-search.md) (`short-binary-search`)
  - [Week 0 — Lecture notes (Scratch)](../weeks/week-00-scratch/lecture.md) (`week-0-lecture`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
جستجوی دودویی روی داده‌ی مرتب، در هر گام نیمی از فضای جستجو را حذف می‌کند و بنابراین با حدود log n گام کار می‌کند.

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
- Passages were matched automatically with the regex `\bbinary search\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
