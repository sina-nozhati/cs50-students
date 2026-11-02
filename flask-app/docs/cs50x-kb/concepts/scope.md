---
id: concept-scope
type: concept
title: Variable Scope
week: 2
parent: concepts
children: []
prerequisites: []
related:
- short-variables-and-scope
- week-1-lecture
- week-2-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/1/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:18+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- scope
checksum: sha256:c782785752ff90a3516e9c720a63be3bd6b277cb1de0555c8a1637a0902c1481
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Variable Scope

## 1. Source metadata
- **Title:** Variable Scope
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/1/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:18+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> When working with variables and functions, it’s important to understand the scope of a variable. Consider the following code:
>
> — Week 1 notes, section “Functions” (<https://cs50.harvard.edu/x/notes/1/#functions>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#functions))

> Notice how n is defined in the main function. Because of that, n is only in the scope of the main function. The only way that the meow function is able to use n is that a copy of n is passed to the meow function. meow is not using the original n from the main function. Instead, it is using its own copy of n.
>
> — Week 1 notes, section “Functions” (<https://cs50.harvard.edu/x/notes/1/#functions>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#functions))

### Other lecture sections that mention this concept

- Week 4: [Swapping](../weeks/week-04-memory/lecture.md#swapping)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 2؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Short: Variables and Scope](../weeks/week-02-arrays/shorts/variables-and-scope.md) (`short-variables-and-scope`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
حوزه‌ی دید (scope) مشخص می‌کند یک متغیر در کدام بخش کد قابل دسترسی است؛ متغیرهای محلی فقط درون آکولادهایی که تعریف شده‌اند معتبرند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/1/ — retrieved 2026-10-18T05:10:18+03:30, sha256 `c782785752ff90a3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bscope\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
