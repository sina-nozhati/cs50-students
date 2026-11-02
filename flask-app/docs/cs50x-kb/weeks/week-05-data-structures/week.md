---
id: week-5
type: week
title: Week 5 — Data Structures
week: 5
parent: course
children:
- week-5-lecture
- week-5-section
- short-structures
- short-singly-linked-lists
- short-doubly-linked-lists
- short-stacks
- short-queues
- short-hash-tables
- short-tries
- short-data-structures
- week-5-source-code
- pset-5
- practice-5-trie
prerequisites:
- week-4
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/5/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:00+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- abstract-data-types
- hash-tables
- linked-lists
- queues-stacks
- trees-binary-search-trees
- tries
- week
checksum: sha256:30e9d85bdb48a759ca9e5031033b41ff4de0db2dc9334263c33b8c79f36f0b90
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 5 — Data Structures

## 1. Source metadata
- **Title:** Week 5 — Data Structures
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/5/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:00+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/5/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-5-data-structures"></a>

### Week 5 *Data Structures*

Abstract Data Types. Queues, Stacks. Linked Lists. Trees, Binary Search Trees. Hash Tables. Tries.

[Embedded video: https://video.cs50.io/PmAI76OGE_E](https://video.cs50.io/PmAI76OGE_E)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/5/lecture5.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/5/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1sIyEI5b48DNa8GT5okXyFu9mdimxGDSHgQdVJM-zRVQ/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/5/lecture5.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/5/src5/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/5/src5.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/5/src5.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/5/lang/en/lecture5.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/5/lang/pt/aula5.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/5/lang/es/clase5.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/5/lang/en/lecture5.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/5/lang/pt/aula5.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/5/lang/es/clase5.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/PmAI76OGE_E)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/5/lecture5-4k.mp4)
      * [YouTube](https://youtu.be/PmAI76OGE_E)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/pttqNxchp9k)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/5/pt/aula5-4k.mp4)
      * [YouTube](https://youtu.be/pttqNxchp9k)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/Q0xvQT87ekA)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/5/es/clase5-4k.mp4)
      * [YouTube](https://youtu.be/Q0xvQT87ekA)
* Shorts
  1. [Structures](https://cs50.harvard.edu/x/shorts/structures/)
  2. [Singly-Linked Lists](https://cs50.harvard.edu/x/shorts/singly_linked_lists/)
  3. [Doubly-Linked Lists](https://cs50.harvard.edu/x/shorts/doubly_linked_lists/)
  4. [Stacks](https://cs50.harvard.edu/x/shorts/stacks/)
  5. [Queues](https://cs50.harvard.edu/x/shorts/queues/)
  6. [Hash Tables](https://cs50.harvard.edu/x/shorts/hash_tables/)
  7. [Tries](https://cs50.harvard.edu/x/shorts/tries/)
  8. [Data Structures](https://cs50.harvard.edu/x/shorts/data_structures/)
* [Section](https://cs50.harvard.edu/x/sections/5/)
* [Problem Set 5](https://cs50.harvard.edu/x/psets/5/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Abstract Data Types
- Queues, Stacks
- Linked Lists
- Trees, Binary Search Trees
- Hash Tables
- Tries

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Abstract Data Types، Queues, Stacks، Linked Lists، Trees, Binary Search Trees، Hash Tables، Tries.

**پیش‌نیاز (تولیدشده):** Week 4.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 5 — Lecture notes (Data Structures)](lecture.md) (`week-5-lecture`)
  - [Week 5 — Section](sections.md) (`week-5-section`)
  - [Short: Structures](shorts/structures.md) (`short-structures`)
  - [Short: Singly-Linked Lists](shorts/singly-linked-lists.md) (`short-singly-linked-lists`)
  - [Short: Doubly-Linked Lists](shorts/doubly-linked-lists.md) (`short-doubly-linked-lists`)
  - [Short: Stacks](shorts/stacks.md) (`short-stacks`)
  - [Short: Queues](shorts/queues.md) (`short-queues`)
  - [Short: Hash Tables](shorts/hash-tables.md) (`short-hash-tables`)
  - [Short: Tries](shorts/tries.md) (`short-tries`)
  - [Short: Data Structures](shorts/data-structures.md) (`short-data-structures`)
  - [Week 5 — Lecture source code](source-code/README.md) (`week-5-source-code`)
  - [Problem Set 5](psets/README.md) (`pset-5`)
  - [Trie — Practice](practice/trie.md) (`practice-5-trie`)
- **Prerequisites (generated):** [Week 4 — Memory](../week-04-memory/week.md) (`week-4`)
- **Backlinks (auto-generated):**
  - [Week 6 — Python](../week-06-python/week.md) (`week-6`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
ساختمان‌داده‌ها: لیست پیوندی، درخت، جدول درهم‌سازی و trie؛ مقایسه‌ی بده‌بستان‌های زمان و حافظه.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.

### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.harvard.edu/x/weeks/5/ — retrieved 2026-10-18T05:10:00+03:30, sha256 `30e9d85bdb48a759…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
