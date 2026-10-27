---
id: concept-merge-sort
type: concept
title: Merge Sort
week: 3
parent: concepts
children: []
prerequisites: []
related:
- short-merge-sort
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
- merge-sort
checksum: sha256:77e0896c7834b2b0847a1bbc39055410297f8a31720e610ea5fbd19dce7a33ac
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Merge Sort

## 1. Source metadata
- **Title:** Merge Sort
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/3/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/3/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> We can now leverage recursion in our quest for a more efficient sort algorithm and implement what is called merge sort, a very efficient sort algorithm.
>
> — Week 3 notes, section “Merge Sort” (<https://cs50.harvard.edu/x/notes/3/#merge-sort>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#merge-sort))

> The pseudocode for merge sort is quite short:
>
> — Week 3 notes, section “Merge Sort” (<https://cs50.harvard.edu/x/notes/3/#merge-sort>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#merge-sort))

> First, merge sort asks, “Is this one number?” The answer is “no,” so the algorithm continues.
>
> — Week 3 notes, section “Merge Sort” (<https://cs50.harvard.edu/x/notes/3/#merge-sort>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#merge-sort))

> Second, merge sort will now split the numbers down the middle (or as close as it can get) and sort the left half of numbers.
>
> — Week 3 notes, section “Merge Sort” (<https://cs50.harvard.edu/x/notes/3/#merge-sort>; KB: [week-3-lecture](../weeks/week-03-algorithms/lecture.md#merge-sort))

> Merge sort is a very efficient sort algorithm with a worst case of \(O(n \log n)\). The best case is still \(\Omega(n \log n)\) because the algorithm still must visit each place in the list. Therefore, merge sort is also \(\Theta(n \log n)\) since the best case and worst case are the same.
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
  - [Short: Merge Sort](../weeks/week-03-algorithms/shorts/merge-sort.md) (`short-merge-sort`)
  - [Week 3 — Lecture notes (Algorithms)](../weeks/week-03-algorithms/lecture.md) (`week-3-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
مرتب‌سازی ادغامی آرایه را نصف می‌کند، هر نیمه را به‌صورت بازگشتی مرتب و سپس دو نیمه را ادغام می‌کند؛ از مرتبه‌ی n log n است ولی حافظه‌ی اضافه لازم دارد.

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
- Passages were matched automatically with the regex `\bmerge sort\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
