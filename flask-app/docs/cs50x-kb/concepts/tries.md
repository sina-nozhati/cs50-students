---
id: concept-tries
type: concept
title: Tries
week: 5
parent: concepts
children: []
prerequisites: []
related:
- practice-5-trie
- short-tries
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
- tries
checksum: sha256:3796458db78c64c561a31e256f6370366d8348c6fbe855fd3c1bf49e7ff74457
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Tries

## 1. Source metadata
- **Title:** Tries
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/5/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:31+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Tries are another form of data structure. Tries are trees of arrays.
>
> — Week 5 notes, section “Tries” (<https://cs50.harvard.edu/x/notes/5/#tries>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#tries))

> Tries are always searchable in constant time.
>
> — Week 5 notes, section “Tries” (<https://cs50.harvard.edu/x/notes/5/#tries>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#tries))

> One downside to Tries is that they tend to take up a large amount of memory. Notice that we need \(26 \times 4 = 104\) nodes just to store Toad!
>
> — Week 5 notes, section “Tries” (<https://cs50.harvard.edu/x/notes/5/#tries>; KB: [week-5-lecture](../weeks/week-05-data-structures/lecture.md#tries))

### Other lecture sections that mention this concept

- Week 0: [Algorithms](../weeks/week-00-scratch/lecture.md#algorithms)
- Week 6: [Exceptions](../weeks/week-06-python/lecture.md#exceptions)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 5؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Trie — Practice](../weeks/week-05-data-structures/practice/trie.md) (`practice-5-trie`)
  - [Short: Tries](../weeks/week-05-data-structures/shorts/tries.md) (`short-tries`)
  - [Week 5 — Lecture notes (Data Structures)](../weeks/week-05-data-structures/lecture.md) (`week-5-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
trie درختی است که هر سطح آن متناظر با یک حرف کلید است؛ جستجو به طول کلید بستگی دارد نه تعداد کلیدها، ولی حافظه‌ی زیادی مصرف می‌کند.

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
- Passages were matched automatically with the regex `\btries\b|\btrie\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
