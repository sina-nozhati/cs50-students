---
id: concept-command-line-arguments
type: concept
title: Command-Line Arguments (argc, argv)
week: 2
parent: concepts
children: []
prerequisites: []
related:
- practice-2-no-vowels
- practice-6-figlet
- pset-2-caesar
- pset-2-substitution
- pset-6-dna
- short-command-line-arguments
- week-2-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/2/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:21+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- command-line-arguments
- concept
checksum: sha256:fa3b156e1bfc2fbeb77c6a14dd873548979a427fb5a6da2784ef3be4dc6a6b3a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Command-Line Arguments (argc, argv)

## 1. Source metadata
- **Title:** Command-Line Arguments (argc, argv)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/2/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:21+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/2/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Command-line arguments are provided at the command line to clang as -o hello hello.c.
>
> — Week 2 notes, section “Compiling” (<https://cs50.harvard.edu/x/notes/2/#compiling>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#compiling))

> Command-line arguments are those arguments that are passed to your program at the command line. For example, all those statements you typed after clang are considered command line arguments. You can use these arguments in your own programs!
>
> — Week 2 notes, section “Command-Line Arguments” (<https://cs50.harvard.edu/x/notes/2/#command-line-arguments>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#command-line-arguments))

> Notice that this program knows both argc, the number of command line arguments, and argv, which is an array of strings passed as arguments at the command line.
>
> — Week 2 notes, section “Command-Line Arguments” (<https://cs50.harvard.edu/x/notes/2/#command-line-arguments>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#command-line-arguments))

> You can print each of the command-line arguments with the following:
>
> — Week 2 notes, section “Command-Line Arguments” (<https://cs50.harvard.edu/x/notes/2/#command-line-arguments>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#command-line-arguments))

> Notice how this code prints out each command-line argument on its own line. The first argument (argv[0]) is always the name of the program itself, followed by any arguments you provide when running the program.
>
> — Week 2 notes, section “Command-Line Arguments” (<https://cs50.harvard.edu/x/notes/2/#command-line-arguments>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#command-line-arguments))

### Other lecture sections that mention this concept

- Week 6: [Command-Line Arguments](../weeks/week-06-python/lecture.md#command-line-arguments)

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
  - [Frank, Ian and Glen’s Letters — Practice](../weeks/week-06-python/practice/figlet.md) (`practice-6-figlet`)
  - [Caesar (less comfortable) — Problem Set 2](../weeks/week-02-arrays/psets/caesar.md) (`pset-2-caesar`)
  - [Substitution (more comfortable) — Problem Set 2](../weeks/week-02-arrays/psets/substitution.md) (`pset-2-substitution`)
  - [DNA — Problem Set 6](../weeks/week-06-python/psets/dna.md) (`pset-6-dna`)
  - [Short: Command Line Arguments](../weeks/week-02-arrays/shorts/command-line-arguments.md) (`short-command-line-arguments`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
برنامه می‌تواند هنگام اجرا ورودی‌هایی را از خط فرمان بگیرد؛ در C این ورودی‌ها از طریق argc (تعداد) و argv (آرایه‌ای از رشته‌ها) در دسترس‌اند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/2/ — retrieved 2026-10-18T05:10:21+03:30, sha256 `fa3b156e1bfc2fbe…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bargc\b|\bargv\b|command-line argument`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
