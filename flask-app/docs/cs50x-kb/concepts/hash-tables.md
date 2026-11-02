---
id: concept-hash-tables
type: concept
title: Hash Tables and Hash Functions
week: 5
parent: concepts
children: []
prerequisites: []
related:
- pset-5-speller
- pset-9-finance
- short-hash-tables
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
- hash-tables
checksum: sha256:3796458db78c64c561a31e256f6370366d8348c6fbe855fd3c1bf49e7ff74457
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hash Tables and Hash Functions

## 1. Source metadata
- **Title:** Hash Tables and Hash Functions
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:31+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Hashing is the idea of taking a value and being able to output a value that becomes a shortcut to it later.
>
> — Week 5 notes, section “Hashing and Hash Tables” (<https://cs50.harvard.edu/x/notes/5/#hashing-and-hash-tables>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables))

> For example, hashing apple may hash as a value of 1, and berry may be hashed as 2. Therefore, finding apple is as easy as asking the hash algorithm where apple is stored. While not ideal in terms of design, ultimately, putting all a ’s in one bucket and b ’s in another, this concept of bucketizing hashed values illustrates how you can use this concept: a hashed value can be used to shortcut finding such a value.
>
> — Week 5 notes, section “Hashing and Hash Tables” (<https://cs50.harvard.edu/x/notes/5/#hashing-and-hash-tables>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables))

> A hash function is an algorithm that reduces a larger value to something small and predictable. Generally, this function takes in an item you wish to add to your hash table, and returns an integer representing the array index in which the item should be placed.
>
> — Week 5 notes, section “Hashing and Hash Tables” (<https://cs50.harvard.edu/x/notes/5/#hashing-and-hash-tables>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables))

> A hash table is a fantastic combination of both arrays and linked lists. When implemented in code, a hash table is an array of pointers to node s.
>
> — Week 5 notes, section “Hashing and Hash Tables” (<https://cs50.harvard.edu/x/notes/5/#hashing-and-hash-tables>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables))

> A hash table could be imagined as follows:
>
> — Week 5 notes, section “Hashing and Hash Tables” (<https://cs50.harvard.edu/x/notes/5/#hashing-and-hash-tables>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#hashing-and-hash-tables))

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
  - [C$50 Finance — Problem Set 9](../weeks/week-09-flask/psets/finance.md) (`pset-9-finance`)
  - [Short: Hash Tables](../weeks/week-05-data-structures/shorts/hash-tables.md) (`short-hash-tables`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
جدول درهم‌سازی با یک تابع hash هر کلید را به یک سطل نگاشت می‌کند تا دسترسی به‌طور میانگین تقریباً ثابت باشد؛ برخوردها معمولاً با لیست پیوندی مدیریت می‌شوند.

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
- Passages were matched automatically with the regex `\bhash(ing)? tables?\b|\bhash functions?\b|\bhashing\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
