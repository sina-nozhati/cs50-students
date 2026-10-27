---
id: concept-linked-lists
type: concept
title: Linked Lists
week: 5
parent: concepts
children: []
prerequisites: []
related:
- pset-5-speller
- short-doubly-linked-lists
- short-singly-linked-lists
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
- linked-lists
checksum: sha256:3796458db78c64c561a31e256f6370366d8348c6fbe855fd3c1bf49e7ff74457
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Linked Lists

## 1. Source metadata
- **Title:** Linked Lists
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:31+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> These boxes are called nodes. A node contains both an item and a pointer called next. In code, you can imagine a node as follows:
>
> — Week 5 notes, section “Linked Lists” (<https://cs50.harvard.edu/x/notes/5/#linked-lists>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#linked-lists))

> Notice that the item contained within this node is an integer called number. Second, a pointer to a node called next is included, which will point to another node somewhere in memory.
>
> — Week 5 notes, section “Linked Lists” (<https://cs50.harvard.edu/x/notes/5/#linked-lists>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#linked-lists))

> Next, a node called n is allocated in memory.
>
> — Week 5 notes, section “Linked Lists” (<https://cs50.harvard.edu/x/notes/5/#linked-lists>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#linked-lists))

> Looking at our diagram of the list, we can see that the last number added is the first number that appears in the list. Accordingly, if we print the list in order, starting with the first node, the list will appear out of order.
>
> — Week 5 notes, section “Linked Lists” (<https://cs50.harvard.edu/x/notes/5/#linked-lists>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#linked-lists))

> A hash table is a fantastic combination of both arrays and linked lists. When implemented in code, a hash table is an array of pointers to node s.
>
> — Week 5 notes, section “Hashing and Hash Tables” (<https://cs50.harvard.edu/x/notes/5/#hashing-and-hash-tables>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables))

### Other lecture sections that mention this concept

- Week 7: [Indexes](../weeks/week-07-sql/lecture.md#indexes)
- Artificial Intelligence: [Deep Learning](../weeks/week-ai-artificial-intelligence/lecture.md#deep-learning)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 5؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Speller — Problem Set 5](../weeks/week-05-data-structures/psets/speller.md) (`pset-5-speller`)
  - [Short: Doubly-Linked Lists](../weeks/week-05-data-structures/shorts/doubly-linked-lists.md) (`short-doubly-linked-lists`)
  - [Short: Singly-Linked Lists](../weeks/week-05-data-structures/shorts/singly-linked-lists.md) (`short-singly-linked-lists`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
لیست پیوندی مجموعه‌ای از گره‌هاست که هرکدام داده و اشاره‌گری به گره بعدی دارند؛ درج آسان است ولی دسترسی تصادفی ندارد.

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
- Passages were matched automatically with the regex `\blinked lists?\b|\bnodes?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
