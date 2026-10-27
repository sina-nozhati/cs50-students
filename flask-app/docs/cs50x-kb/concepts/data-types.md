---
id: concept-data-types
type: concept
title: Data Types
week: 1
parent: concepts
children: []
prerequisites: []
related:
- practice-1-half
- practice-2-hours
- practice-2-password
- pset-2-caesar
- pset-2-readability
- pset-2-scrabble
- pset-2-substitution
- pset-4-volume
- short-data-types
- week-1-lecture
- week-2-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/1/
- https://cs50.harvard.edu/x/notes/2/
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
- data-types
checksum: sha256:c782785752ff90a3516e9c720a63be3bd6b277cb1de0555c8a1637a0902c1481
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Data Types

## 1. Source metadata
- **Title:** Data Types
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/1/>, <https://cs50.harvard.edu/x/notes/2/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:18+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/1/>, <https://cs50.harvard.edu/x/notes/2/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> answer is a special holding place we call a variable. answer is of type string and can hold any string within it. There are many data types, such as int, bool, char, and many others.
>
> — Week 1 notes, section “Hello, You” (<https://cs50.harvard.edu/x/notes/1/#hello-you>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#hello-you))

> Notice how a variable called counter of type int is assigned the value 0.
>
> — Week 1 notes, section “Variables” (<https://cs50.harvard.edu/x/notes/1/#variables>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#variables))

> Considering another data type called a char, we can start a new program by typing code agree.c into the terminal window.
>
> — Week 1 notes, section “agree.c” (<https://cs50.harvard.edu/x/notes/1/#agreec>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#agreec))

> Types refer to the possible data that can be stored in a variable. For example, a char is designed to accommodate a single character like a or 2.
>
> — Week 1 notes, section “Operators” (<https://cs50.harvard.edu/x/notes/1/#operators>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#operators))

> In Week 0, we talked about data types such as bool, int, char, string, etc.
>
> — Week 2 notes, section “Arrays” (<https://cs50.harvard.edu/x/notes/2/#arrays>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#arrays))

### Other lecture sections that mention this concept

- Week 4: [Strings](../weeks/week-04-memory/lecture.md#strings), [scanf](../weeks/week-04-memory/lecture.md#scanf)
- Week 6: [Types](../weeks/week-06-python/lecture.md#types)
- Week 8: [Regular Expressions](../weeks/week-08-html-css-javascript/lecture.md#regular-expressions)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 1؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Half — Practice](../weeks/week-01-c/practice/half.md) (`practice-1-half`)
  - [Hours — Practice](../weeks/week-02-arrays/practice/hours.md) (`practice-2-hours`)
  - [Password — Practice](../weeks/week-02-arrays/practice/password.md) (`practice-2-password`)
  - [Caesar (less comfortable) — Problem Set 2](../weeks/week-02-arrays/psets/caesar.md) (`pset-2-caesar`)
  - [Readability — Problem Set 2](../weeks/week-02-arrays/psets/readability.md) (`pset-2-readability`)
  - [Scrabble — Problem Set 2](../weeks/week-02-arrays/psets/scrabble.md) (`pset-2-scrabble`)
  - [Substitution (more comfortable) — Problem Set 2](../weeks/week-02-arrays/psets/substitution.md) (`pset-2-substitution`)
  - [Volume — Problem Set 4](../weeks/week-04-memory/psets/volume.md) (`pset-4-volume`)
  - [Short: Data Types](../weeks/week-01-c/shorts/data-types.md) (`short-data-types`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
نوع داده مشخص می‌کند یک مقدار چگونه در حافظه ذخیره و تفسیر شود و چه عملیاتی روی آن معنادار است (مثلاً int، float، char، bool، string).

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/1/ — retrieved 2026-10-18T05:10:18+03:30, sha256 `c782785752ff90a3…`
- https://cs50.harvard.edu/x/notes/2/ — retrieved 2026-10-18T05:10:21+03:30, sha256 `fa3b156e1bfc2fbe…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\btypes?\b.*\b(int|float|char|long|double|bool|string)\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
