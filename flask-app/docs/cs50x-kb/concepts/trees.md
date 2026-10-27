---
id: concept-trees
type: concept
title: Trees and Binary Search Trees
week: 5
parent: concepts
children: []
prerequisites: []
related:
- pset-5-inheritance
- week-5-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/5/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:31+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- trees
checksum: sha256:3796458db78c64c561a31e256f6370366d8348c6fbe855fd3c1bf49e7ff74457
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Trees and Binary Search Trees

## 1. Source metadata
- **Title:** Trees and Binary Search Trees
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:31+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Binary search trees are another data structure that can be used to store data more efficiently so that it can be searched and retrieved.
>
> — Week 5 notes, section “Trees” (<https://cs50.harvard.edu/x/notes/5/#trees>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#trees))

> Imagine then that the center value becomes the top of a tree. Those that are less than this value are placed to the left. Values greater than this are placed to the right.
>
> — Week 5 notes, section “Trees” (<https://cs50.harvard.edu/x/notes/5/#trees>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#trees))

> In code, searching such a tree could be implemented as follows:
>
> — Week 5 notes, section “Trees” (<https://cs50.harvard.edu/x/notes/5/#trees>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#trees))

> Notice how this search function recursively searches the tree. If the searched number is less than the current node’s number, it searches the left subtree. If greater, it searches the right subtree. This recursive approach allows for efficient searching with a time complexity of O(log n) when the tree is balanced.
>
> — Week 5 notes, section “Trees” (<https://cs50.harvard.edu/x/notes/5/#trees>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#trees))

> A tree offers dynamism that an array does not offer. It can grow and shrink as we wish.
>
> — Week 5 notes, section “Trees” (<https://cs50.harvard.edu/x/notes/5/#trees>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#trees))

### Other lecture sections that mention this concept

- Week 7: [Indexes](../weeks/week-07-sql/lecture.md#indexes)
- Artificial Intelligence: [Decision Trees](../weeks/week-ai-artificial-intelligence/lecture.md#decision-trees), [Minimax](../weeks/week-ai-artificial-intelligence/lecture.md#minimax)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 5؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Inheritance — Problem Set 5](../weeks/week-05-data-structures/psets/inheritance.md) (`pset-5-inheritance`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
درخت ساختاری سلسله‌مراتبی از گره‌هاست؛ در درخت جستجوی دودویی، مقادیر کوچک‌تر در زیردرخت چپ و بزرگ‌تر در راست قرار می‌گیرند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/5/ — retrieved 2026-10-18T05:10:31+03:30, sha256 `3796458db78c64c5…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\btrees?\b|\bbinary search tree\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
