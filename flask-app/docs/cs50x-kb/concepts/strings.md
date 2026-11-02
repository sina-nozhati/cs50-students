---
id: concept-strings
type: concept
title: Strings
week: 2
parent: concepts
children: []
prerequisites: []
related:
- practice-2-no-vowels
- practice-2-password
- practice-3-atoi
- practice-4-license
- practice-6-bank
- pset-1-mario-more
- pset-1-me
- pset-2-readability
- pset-2-scrabble
- pset-6-credit
- pset-6-dna
- pset-6-hello
- pset-6-mario-less
- pset-6-mario-more
- pset-6-readability
- week-2-lecture
- week-4-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/2/
- https://cs50.harvard.edu/x/notes/4/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:21+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- strings
checksum: sha256:fa3b156e1bfc2fbeb77c6a14dd873548979a427fb5a6da2784ef3be4dc6a6b3a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Strings

## 1. Source metadata
- **Title:** Strings
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/2/>, <https://cs50.harvard.edu/x/notes/4/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:21+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/2/>, <https://cs50.harvard.edu/x/notes/4/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Considering the following image, you can see how a string is an array of characters that begins with the first character and ends with a special character called a NUL character (note: NUL with one L is the ‘\0’ character, different from NULL with two L’s):
>
> — Week 2 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/2/#strings>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#strings))

> Notice that an array of words is created. It is an array of strings. Each word is stored in words.
>
> — Week 2 notes, section “Strings” (<https://cs50.harvard.edu/x/notes/2/#strings>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#strings))

> Notice that a new function called string_length counts characters until NUL is located.
>
> — Week 2 notes, section “String Length” (<https://cs50.harvard.edu/x/notes/2/#string-length>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#string-length))

> Notice that this code uses the string.h library, declared at the top of the file. Further, it uses a function from that library called strlen, which calculates the length of the string passed to it.
>
> — Week 2 notes, section “String Length” (<https://cs50.harvard.edu/x/notes/2/#string-length>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#string-length))

> Notice that strcmp can return 0 if the strings are the same. You can download this code here.
>
> — Week 4 notes, section “String Comparison” (<https://cs50.harvard.edu/x/notes/4/#string-comparison>; KB: [week-4-lecture](../weeks/week-04-memory/lecture.md#string-comparison))

### Other lecture sections that mention this concept

- Week 0: [Hello, You](../weeks/week-00-scratch/lecture.md#hello-you)
- Week 1: [Format Codes](../weeks/week-01-c/lecture.md#format-codes), [Hello, You](../weeks/week-01-c/lecture.md#hello-you), [Operators](../weeks/week-01-c/lecture.md#operators), [agree.c](../weeks/week-01-c/lecture.md#agreec)
- Week 3: [Linear Search](../weeks/week-03-algorithms/lecture.md#linear-search), [Structs](../weeks/week-03-algorithms/lecture.md#structs), [phonebook.c](../weeks/week-03-algorithms/lecture.md#phonebookc), [search.c](../weeks/week-03-algorithms/lecture.md#searchc)
- Week 6: [Calculator](../weeks/week-06-python/lecture.md#calculator), [Command-Line Arguments](../weeks/week-06-python/lecture.md#command-line-arguments), [Loops](../weeks/week-06-python/lecture.md#loops), [Object-Oriented Programming](../weeks/week-06-python/lecture.md#object-oriented-programming), [Types](../weeks/week-06-python/lecture.md#types)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 2؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [N0 V0w3ls — Practice](../weeks/week-02-arrays/practice/no-vowels.md) (`practice-2-no-vowels`)
  - [Password — Practice](../weeks/week-02-arrays/practice/password.md) (`practice-2-password`)
  - [Recursive atoi — Practice](../weeks/week-03-algorithms/practice/atoi.md) (`practice-3-atoi`)
  - [License — Practice](../weeks/week-04-memory/practice/license.md) (`practice-4-license`)
  - [Home Federal Savings Bank — Practice](../weeks/week-06-python/practice/bank.md) (`practice-6-bank`)
  - [Mario (more comfortable) — Problem Set 1](../weeks/week-01-c/psets/mario-more.md) (`pset-1-mario-more`)
  - [Hello, It’s Me — Problem Set 1](../weeks/week-01-c/psets/me.md) (`pset-1-me`)
  - [Readability — Problem Set 2](../weeks/week-02-arrays/psets/readability.md) (`pset-2-readability`)
  - [Scrabble — Problem Set 2](../weeks/week-02-arrays/psets/scrabble.md) (`pset-2-scrabble`)
  - [Credit (more comfortable) — Problem Set 6](../weeks/week-06-python/psets/credit.md) (`pset-6-credit`)
  - [DNA — Problem Set 6](../weeks/week-06-python/psets/dna.md) (`pset-6-dna`)
  - [Hello, Again — Problem Set 6](../weeks/week-06-python/psets/hello.md) (`pset-6-hello`)
  - [Mario (less comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-less.md) (`pset-6-mario-less`)
  - [Mario (more comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-more.md) (`pset-6-mario-more`)
  - [Readability — Problem Set 6](../weeks/week-06-python/psets/readability.md) (`pset-6-readability`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)
  - [Week 4 — Lecture notes (Memory)](../weeks/week-04-memory/lecture.md) (`week-4-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
در C رشته آرایه‌ای از کاراکترهاست که با کاراکتر NUL (\0) پایان می‌یابد؛ این دید در هفته ۴ به «آدرس اولین کاراکتر» تبدیل می‌شود.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/2/ — retrieved 2026-10-18T05:10:21+03:30, sha256 `fa3b156e1bfc2fbe…`
- https://cs50.harvard.edu/x/notes/4/ — retrieved 2026-10-18T05:10:28+03:30, sha256 `9776ed69bbe1af97…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bstrings?\b|\bNUL\b|\\0`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
