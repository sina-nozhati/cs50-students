---
id: concept-binary
type: concept
title: Binary and Representation
week: 0
parent: concepts
children: []
prerequisites: []
related:
- pset-4-volume
- week-0-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/0/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:16+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- binary
- concept
checksum: sha256:19cabb7558e628e3a2968377be2570125a4866712f959b0c0dad45909c39c712
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Binary and Representation

## 1. Source metadata
- **Title:** Binary and Representation
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/0/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/0/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Computers today count using a system called binary (also called base-2 ). It’s from the term binary digit that we get a familiar term called bit. A bit is a zero or one: on or off.
>
> — Week 0 notes, section “Computer Science and Problem Solving” (<https://cs50.harvard.edu/x/notes/0/#computer-science-and-problem-solving>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#computer-science-and-problem-solving))

> Therefore, you could say that it would require three bits (the four’s place, the two’s place, and the one’s place) to represent a number as high as seven.
>
> — Week 0 notes, section “Computer Science and Problem Solving” (<https://cs50.harvard.edu/x/notes/0/#computer-science-and-problem-solving>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#computer-science-and-problem-solving))

> Computers generally use eight bits (also known as a byte ) to represent a number. For example, 00000101 is the number 5 in binary. 11111111 represents the number 255. You can imagine zero as follows:
>
> — Week 0 notes, section “Computer Science and Problem Solving” (<https://cs50.harvard.edu/x/notes/0/#computer-science-and-problem-solving>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#computer-science-and-problem-solving))

> Just as numbers are binary patterns of ones and zeros, letters are represented using ones and zeros, too!
>
> — Week 0 notes, section “ASCII” (<https://cs50.harvard.edu/x/notes/0/#ascii>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#ascii))

> If you received a text message, the binary under that message might represent the numbers 72, 73, and 33. Mapping these out to ASCII, your message would look as follows:
>
> — Week 0 notes, section “ASCII” (<https://cs50.harvard.edu/x/notes/0/#ascii>; KB: [week-0-lecture](../weeks/week-00-scratch/lecture.md#ascii))

### Other lecture sections that mention this concept

- Week 1: [Operators](../weeks/week-01-c/lecture.md#operators), [Source Code](../weeks/week-01-c/lecture.md#source-code)
- Week 2: [Arrays](../weeks/week-02-arrays/lecture.md#arrays)
- Week 3: [Binary Search](../weeks/week-03-algorithms/lecture.md#binary-search), [Running Time](../weeks/week-03-algorithms/lecture.md#running-time), [Sorting and Selection Sort](../weeks/week-03-algorithms/lecture.md#sorting-and-selection-sort), [Summing Up](../weeks/week-03-algorithms/lecture.md#summing-up)
- Week 4: [File I/O](../weeks/week-04-memory/lecture.md#file-io), [Pixel Art](../weeks/week-04-memory/lecture.md#pixel-art), [Pointers](../weeks/week-04-memory/lecture.md#pointers), [String Comparison](../weeks/week-04-memory/lecture.md#string-comparison), [Strings](../weeks/week-04-memory/lecture.md#strings), [scanf](../weeks/week-04-memory/lecture.md#scanf)
- Week 5: [Linked Lists](../weeks/week-05-data-structures/lecture.md#linked-lists), [Trees](../weeks/week-05-data-structures/lecture.md#trees)
- Week 7: [Indexes](../weeks/week-07-sql/lecture.md#indexes)
- Week 8: [HTTPS](../weeks/week-08-html-css-javascript/lecture.md#https), [Routers](../weeks/week-08-html-css-javascript/lecture.md#routers)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 0؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Volume — Problem Set 4](../weeks/week-04-memory/psets/volume.md) (`pset-4-volume`)
  - [Week 0 — Lecture notes (Scratch)](../weeks/week-00-scratch/lecture.md) (`week-0-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
رایانه‌ها همه‌چیز را با دو حالت (۰ و ۱) نمایش می‌دهند. اعداد، متن (ASCII/Unicode)، رنگ‌ها و تصاویر همگی الگوهایی از بیت‌ها هستند و معنای آن‌ها به نحوه‌ی تفسیرشان بستگی دارد.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/0/ — retrieved 2026-10-18T05:10:16+03:30, sha256 `19cabb7558e628e3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bbinary\b|\bbits?\b|\bbytes?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
