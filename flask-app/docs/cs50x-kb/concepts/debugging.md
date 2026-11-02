---
id: concept-debugging
type: concept
title: Debugging (printf, debug50, rubber duck)
week: 2
parent: concepts
children: []
prerequisites: []
related:
- practice-1-debug
- practice-4-license
- short-debugging-step-into
- short-debugging-step-through
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
- concept
- debugging
checksum: sha256:fa3b156e1bfc2fbeb77c6a14dd873548979a427fb5a6da2784ef3be4dc6a6b3a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Debugging (printf, debug50, rubber duck)

## 1. Source metadata
- **Title:** Debugging (printf, debug50, rubber duck)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/2/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:21+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/2/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Debugging is the process of locating and removing bugs from your code.
>
> — Week 2 notes, section “Debugging” (<https://cs50.harvard.edu/x/notes/2/#debugging>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#debugging))

> One of the debugging techniques you will use during this course to debug your code is called rubber duck debugging, where you can talk to an inanimate object (or yourself) to help think through your code and why it is not working as intended. When you are having challenges with your code, consider how speaking out loud to, quite literally, a rubber duck about the code problem. If you’d rather not talk to a small plastic duck, you are welcome to speak to a human near you!
>
> — Week 2 notes, section “Debugging” (<https://cs50.harvard.edu/x/notes/2/#debugging>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#debugging))

> printf is a very useful way of debugging your code. You could modify your code as follows:
>
> — Week 2 notes, section “Debugging” (<https://cs50.harvard.edu/x/notes/2/#debugging>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#debugging))

> A second tool in debugging is called a debugger, a software tool created by programmers to help track down bugs in code.
>
> — Week 2 notes, section “Debugging” (<https://cs50.harvard.edu/x/notes/2/#debugging>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#debugging))

> In VS Code, a pre-configured debugger has been provided to you called debug50.
>
> — Week 2 notes, section “Debugging” (<https://cs50.harvard.edu/x/notes/2/#debugging>; KB: [week-2-lecture](../weeks/week-02-arrays/lecture.md#debugging))

### Other lecture sections that mention this concept

- Week 0: [Visual Studio Code and chat.py](../weeks/week-00-scratch/lecture.md#visual-studio-code-and-chatpy)
- Artificial Intelligence: [Welcome!](../weeks/week-ai-artificial-intelligence/lecture.md#welcome)
- Week 9: [Request Methods](../weeks/week-09-flask/lecture.md#request-methods)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 2؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Debug — Practice](../weeks/week-01-c/practice/debug.md) (`practice-1-debug`)
  - [License — Practice](../weeks/week-04-memory/practice/license.md) (`practice-4-license`)
  - [Short: Debugging (“Step into”)](../weeks/week-02-arrays/shorts/debugging-step-into.md) (`short-debugging-step-into`)
  - [Short: Debugging (“Step through”)](../weeks/week-02-arrays/shorts/debugging-step-through.md) (`short-debugging-step-through`)
  - [Week 2 — Lecture notes (Arrays)](../weeks/week-02-arrays/lecture.md) (`week-2-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
اشکال‌زدایی یعنی پیدا کردن و رفع خطا؛ CS50 روش‌هایی مثل چاپ مقادیر با printf، ابزار debug50 و توضیح مسئله برای «اردک» را معرفی می‌کند.

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
- Passages were matched automatically with the regex `\bdebug|\bbugs?\b|\brubber duck\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
