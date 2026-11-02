---
id: concept-recursion
type: concept
title: Recursion
week: 3
parent: concepts
children: []
prerequisites: []
related:
- practice-3-atoi
- pset-3-tideman
- pset-5-inheritance
- short-call-stacks
- short-recursion
- week-3-lecture
- week-5-lecture
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
- recursion
checksum: sha256:77e0896c7834b2b0847a1bbc39055410297f8a31720e610ea5fbd19dce7a33ac
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Recursion

## 1. Source metadata
- **Title:** Recursion
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/3/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/3/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Recursion is a concept within programming where a function calls itself. We saw this earlier when we saw…
>
> — Week 3 notes, section “Recursion” (<https://cs50.harvard.edu/x/notes/3/#recursion>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#recursion))

> Similarly, in our pseudocode for Week 0, you can see where recursion was implemented:
>
> — Week 3 notes, section “Recursion” (<https://cs50.harvard.edu/x/notes/3/#recursion>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#recursion))

> This code could have been simplified to highlight its recursive properties as follows:
>
> — Week 3 notes, section “Recursion” (<https://cs50.harvard.edu/x/notes/3/#recursion>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#recursion))

> A base case is defined as the condition that stops the recursion from continuing indefinitely, preventing infinite loops.
>
> — Week 3 notes, section “Recursion” (<https://cs50.harvard.edu/x/notes/3/#recursion>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#recursion))

> We can now leverage recursion in our quest for a more efficient sort algorithm and implement what is called merge sort, a very efficient sort algorithm.
>
> — Week 3 notes, section “Merge Sort” (<https://cs50.harvard.edu/x/notes/3/#merge-sort>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#merge-sort))

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 3؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Recursive atoi — Practice](../weeks/week-03-algorithms/practice/atoi.md) (`practice-3-atoi`)
  - [Tideman (very, very, very comfortable) — Problem Set 3](../weeks/week-03-algorithms/psets/tideman.md) (`pset-3-tideman`)
  - [Inheritance — Problem Set 5](../weeks/week-05-data-structures/psets/inheritance.md) (`pset-5-inheritance`)
  - [Short: Call Stacks](../weeks/week-03-algorithms/shorts/call-stacks.md) (`short-call-stacks`)
  - [Short: Recursion](../weeks/week-03-algorithms/shorts/recursion.md) (`short-recursion`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
بازگشت یعنی تابعی که خودش را با ورودی کوچک‌تر صدا می‌زند؛ هر تابع بازگشتی به یک حالت پایه برای توقف نیاز دارد.

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
- Passages were matched automatically with the regex `\brecursi(on|ve|vely)\b|\bbase case\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
