---
id: concept-conditionals
type: concept
title: Conditionals and Boolean Expressions
week: 0
parent: concepts
children: []
prerequisites: []
related:
- practice-1-prime
- practice-2-no-vowels
- practice-2-password
- practice-6-bank
- pset-0-scratch
- pset-1-credit
- short-conditional-statements
- week-0-lecture
- week-1-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/0/
- https://cs50.harvard.edu/x/notes/1/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:16+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- conditionals
checksum: sha256:19cabb7558e628e3a2968377be2570125a4866712f959b0c0dad45909c39c712
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Conditionals and Boolean Expressions

## 1. Source metadata
- **Title:** Conditionals and Boolean Expressions
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/0/>, <https://cs50.harvard.edu/x/notes/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Second, notice that some lines include statements like if or else if. These are called conditionals.
>
> — Week 0 notes, section “Pseudocode” (<https://cs50.harvard.edu/x/notes/0/#pseudocode>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#pseudocode))

> Conditionals are an essential building block of programming, where the program looks to see if a specific condition has been met. If a condition is met, the program does something.
>
> — Week 0 notes, section “Conditionals” (<https://cs50.harvard.edu/x/notes/0/#conditionals>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#conditionals))

> To illustrate a conditional, write code as follows:
>
> — Week 0 notes, section “Conditionals” (<https://cs50.harvard.edu/x/notes/0/#conditionals>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#conditionals))

> The basic building blocks of programming including functions, conditionals, loops, and variables.
>
> — Week 0 notes, section “Summing Up” (<https://cs50.harvard.edu/x/notes/0/#summing-up>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#summing-up))

> Another building block you utilized within Scratch was conditionals. For example, you might want to do one thing if x is greater than y. Further, you might want to do something else if that condition is not met.
>
> — Week 1 notes, section “Conditionals” (<https://cs50.harvard.edu/x/notes/1/#conditionals>; KB: [week-1-lecture](../weeks/week-01-c/lecture.md#conditionals))

### Other lecture sections that mention this concept

- Week 6: [Conditionals](../weeks/week-06-python/lecture.md#conditionals)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 0؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Prime — Practice](../weeks/week-01-c/practice/prime.md) (`practice-1-prime`)
  - [N0 V0w3ls — Practice](../weeks/week-02-arrays/practice/no-vowels.md) (`practice-2-no-vowels`)
  - [Password — Practice](../weeks/week-02-arrays/practice/password.md) (`practice-2-password`)
  - [Home Federal Savings Bank — Practice](../weeks/week-06-python/practice/bank.md) (`practice-6-bank`)
  - [Starting from Scratch — Problem Set 0](../weeks/week-00-scratch/psets/scratch.md) (`pset-0-scratch`)
  - [Credit (more comfortable) — Problem Set 1](../weeks/week-01-c/psets/credit.md) (`pset-1-credit`)
  - [Short: Conditional Statements](../weeks/week-01-c/shorts/conditional-statements.md) (`short-conditional-statements`)
  - [Week 0 — Lecture notes (Scratch)](../weeks/week-00-scratch/lecture.md) (`week-0-lecture`)
  - [Week 1 — Lecture notes (C)](../weeks/week-01-c/lecture.md) (`week-1-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
شرط‌ها به برنامه اجازه می‌دهند بر اساس درستی یا نادرستی یک عبارت بولی مسیرهای متفاوتی را اجرا کند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/0/ — retrieved 2026-10-18T05:10:16+03:30, sha256 `19cabb7558e628e3…`
- https://cs50.harvard.edu/x/notes/1/ — retrieved 2026-10-18T05:10:18+03:30, sha256 `c782785752ff90a3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bconditionals?\b|\bboolean\b|\bif\b statement`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
