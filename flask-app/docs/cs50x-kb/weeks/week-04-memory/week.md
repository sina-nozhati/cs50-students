---
id: week-4
type: week
title: Week 4 — Memory
week: 4
parent: course
children:
- week-4-lecture
- week-4-section
- short-hexadecimal
- short-pointers
- short-defining-custom-types
- short-dynamic-memory-allocation
- short-file-pointers
- week-4-source-code
- pset-4
- practice-4-bottomup
- practice-4-license
prerequisites:
- week-3
related:
- short-call-stacks
source_urls:
- https://cs50.harvard.edu/x/weeks/4/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:09:59+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- buffer-overflow
- dynamic-memory-allocation
- file-i-o
- heap
- images
- pointers
- segmentation-faults
- stack
- week
checksum: sha256:8b8e5885382b1281bc6c676d6c44f136914a7ec677312103718ce6efc1cbd3ec
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 4 — Memory

## 1. Source metadata
- **Title:** Week 4 — Memory
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/4/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:09:59+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/4/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-4-memory"></a>

### Week 4 *Memory*

Pointers. Segmentation Faults. Dynamic Memory Allocation. Stack. Heap. Buffer Overflow. File I/O. Images.

[Embedded video: https://video.cs50.io/db0H0U13YsA](https://video.cs50.io/db0H0U13YsA)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/4/lecture4.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/4/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1WyWZ1PoTrCBjD_oh4UxzRD3SVCF5942O2dOfzdZ1rKE/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/4/lecture4.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/4/src4/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/4/src4.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/4/src4.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/4/lang/en/lecture4.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/4/lang/pt/aula4.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/4/lang/es/clase4.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/4/lang/en/lecture4.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/4/lang/pt/aula4.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/4/lang/es/clase4.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/db0H0U13YsA)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/4/lecture4-4k.mp4)
      * [YouTube](https://youtu.be/db0H0U13YsA)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/DweS4KseeDE)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/4/pt/aula4-4k.mp4)
      * [YouTube](https://youtu.be/DweS4KseeDE)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/xRW70LgrEho)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/4/es/clase4-4k.mp4)
      * [YouTube](https://youtu.be/xRW70LgrEho)
* Shorts
  1. [Hexadecimal](https://cs50.harvard.edu/x/shorts/hexadecimal/)
  2. [Pointers](https://cs50.harvard.edu/x/shorts/pointers/)
  3. [Defining Custom Types](https://cs50.harvard.edu/x/shorts/defining_custom_types/)
  4. [Dynamic Memory Allocation](https://cs50.harvard.edu/x/shorts/dynamic_memory_allocation/)
  5. [Call Stacks](https://cs50.harvard.edu/x/shorts/call_stacks/)
  6. [File Pointers](https://cs50.harvard.edu/x/shorts/file_pointers/)
* [Section](https://cs50.harvard.edu/x/sections/4/)
* [Problem Set 4](https://cs50.harvard.edu/x/psets/4/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Pointers
- Segmentation Faults
- Dynamic Memory Allocation
- Stack
- Heap
- Buffer Overflow
- File I/O
- Images

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Pointers، Segmentation Faults، Dynamic Memory Allocation، Stack، Heap، Buffer Overflow، File I/O، Images.

**پیش‌نیاز (تولیدشده):** Week 3.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 4 — Lecture notes (Memory)](lecture.md) (`week-4-lecture`)
  - [Week 4 — Section](sections.md) (`week-4-section`)
  - [Short: Hexadecimal](shorts/hexadecimal.md) (`short-hexadecimal`)
  - [Short: Pointers](shorts/pointers.md) (`short-pointers`)
  - [Short: Defining Custom Types](shorts/defining-custom-types.md) (`short-defining-custom-types`)
  - [Short: Dynamic Memory Allocation](shorts/dynamic-memory-allocation.md) (`short-dynamic-memory-allocation`)
  - [Short: File Pointers](shorts/file-pointers.md) (`short-file-pointers`)
  - [Week 4 — Lecture source code](source-code/README.md) (`week-4-source-code`)
  - [Problem Set 4](psets/README.md) (`pset-4`)
  - [Bottom Up — Practice](practice/bottomup.md) (`practice-4-bottomup`)
  - [License — Practice](practice/license.md) (`practice-4-license`)
- **Prerequisites (generated):** [Week 3 — Algorithms](../week-03-algorithms/week.md) (`week-3`)
- **Related:**
  - [Short: Call Stacks](../week-03-algorithms/shorts/call-stacks.md) (`short-call-stacks`)
- **Backlinks (auto-generated):**
  - [Week 5 — Data Structures](../week-05-data-structures/week.md) (`week-5`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
حافظه، اشاره‌گرها، تخصیص پویا و فایل‌ها. یکی از دشوارترین هفته‌ها؛ رسم نمودار حافظه روی کاغذ بسیار کمک می‌کند.

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
- https://cs50.harvard.edu/x/weeks/4/ — retrieved 2026-10-18T05:09:59+03:30, sha256 `8b8e5885382b1281…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
