---
id: concept-stacks-and-queues
type: concept
title: Stacks and Queues (abstract data types)
week: 5
parent: concepts
children: []
prerequisites: []
related:
- short-queues
- short-stacks
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
- stacks-and-queues
checksum: sha256:3796458db78c64c561a31e256f6370366d8348c6fbe855fd3c1bf49e7ff74457
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Stacks and Queues (abstract data types)

## 1. Source metadata
- **Title:** Stacks and Queues (abstract data types)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:31+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Queues are one form of abstract data structure.
>
> — Week 5 notes, section “Queues” (<https://cs50.harvard.edu/x/notes/5/#queues>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#queues))

> Queues have specific properties. Namely, they are FIFO or “first in first out.” You can imagine yourself in a line for a ride at an amusement park. The first person in the line gets to go on the ride first. The last person gets to go on the ride last.
>
> — Week 5 notes, section “Queues” (<https://cs50.harvard.edu/x/notes/5/#queues>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#queues))

> Notice that an array called people is of type person. The CAPACITY is how high the queue could be. The integer size is how full the queue actually is, regardless of how much it can hold.
>
> — Week 5 notes, section “Queues” (<https://cs50.harvard.edu/x/notes/5/#queues>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#queues))

> Queues contrast with a stack. Fundamentally, the properties of a stack are different from those of a queue. Specifically, it is LIFO or “last in first out.” Just like stacking trays in a dining hall, a tray that is placed in a stack last is the first that may be picked up.
>
> — Week 5 notes, section “Stacks” (<https://cs50.harvard.edu/x/notes/5/#stacks>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#stacks))

> Notice that an array called people is of type person. The CAPACITY is how high the stack could be. The integer size is how full the stack actually is, regardless of how much it could hold. Notice that this code is the same as the code from the queue.
>
> — Week 5 notes, section “Stacks” (<https://cs50.harvard.edu/x/notes/5/#stacks>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#stacks))

### Other lecture sections that mention this concept

- Week 4: [Overflow](../weeks/week-04-memory/lecture.md#overflow), [Swapping](../weeks/week-04-memory/lecture.md#swapping)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 5؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Short: Queues](../weeks/week-05-data-structures/shorts/queues.md) (`short-queues`)
  - [Short: Stacks](../weeks/week-05-data-structures/shorts/stacks.md) (`short-stacks`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
صف (FIFO) و پشته (LIFO) انواع داده‌ی انتزاعی‌اند که ترتیب ورود و خروج عناصر را تعریف می‌کنند و می‌توانند با آرایه یا لیست پیوندی پیاده شوند.

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
- Passages were matched automatically with the regex `\bqueues?\b|\bstacks?\b|\bLIFO\b|\bFIFO\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
