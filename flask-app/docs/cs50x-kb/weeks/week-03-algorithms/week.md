---
id: week-3
type: week
title: Week 3 — Algorithms
week: 3
parent: course
children:
- week-3-lecture
- week-3-section
- short-linear-search
- short-binary-search
- short-bubble-sort
- short-selection-sort
- short-call-stacks
- short-recursion
- short-merge-sort
- week-3-source-code
- pset-3
- practice-3-atoi
- practice-3-temps
- practice-3-max
- practice-3-snackbar
prerequisites:
- week-2
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/3/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:09:58+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- asymptotic-notation-o-omega-theta
- recursion
- searching-linear-search-binary-search
- sorting-bubble-sort-selection-sort-merge-sort
- week
checksum: sha256:0491a46d2169747624694c8ece5d2355615882d3293baf0821bbf43452baf62f
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 3 — Algorithms

## 1. Source metadata
- **Title:** Week 3 — Algorithms
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/3/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:09:58+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/3/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-3-algorithms"></a>

### Week 3 *Algorithms*

Searching: Linear Search, Binary Search. Sorting: Bubble Sort, Selection Sort, Merge Sort. Asymptotic Notation: \(O\), \(\Omega\), \(\Theta\). Recursion.

[Embedded video: https://video.cs50.io/6Svu_ae5ebk](https://video.cs50.io/6Svu_ae5ebk)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/3/lecture3.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/3/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/18hLMy4Qw8fKjwnz4oQtcoTdUnMFxFxx6PBjm4b7ekgo/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/3/lecture3.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/3/src3/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/3/src3.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/3/src3.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/3/lang/en/lecture3.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/3/lang/pt/aula3.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/3/lang/es/clase3.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/3/lang/en/lecture3.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/3/lang/pt/aula3.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/3/lang/es/clase3.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/6Svu_ae5ebk)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/3/lecture3-4k.mp4)
      * [YouTube](https://youtu.be/6Svu_ae5ebk)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/1dV61IMUwIc)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/3/pt/aula3-4k.mp4)
      * [YouTube](https://youtu.be/1dV61IMUwIc)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/zU0DbilHvYM)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/3/es/clase3-4k.mp4)
      * [YouTube](https://youtu.be/zU0DbilHvYM)
* Shorts
  1. [Linear Search](https://cs50.harvard.edu/x/shorts/linear_search/)
  2. [Binary Search](https://cs50.harvard.edu/x/shorts/binary_search/)
  3. [Bubble Sort](https://cs50.harvard.edu/x/shorts/bubble_sort/)
  4. [Selection Sort](https://cs50.harvard.edu/x/shorts/selection_sort/)
  5. [Call Stacks](https://cs50.harvard.edu/x/shorts/call_stacks/)
  6. [Recursion](https://cs50.harvard.edu/x/shorts/recursion/)
  7. [Merge Sort](https://cs50.harvard.edu/x/shorts/merge_sort/)
* [Section](https://cs50.harvard.edu/x/sections/3/)
* [Problem Set 3](https://cs50.harvard.edu/x/psets/3/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Searching: Linear Search, Binary Search
- Sorting: Bubble Sort, Selection Sort, Merge Sort
- Asymptotic Notation: \(O\), \(\Omega\), \(\Theta\)
- Recursion

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Searching: Linear Search, Binary Search، Sorting: Bubble Sort, Selection Sort, Merge Sort، Asymptotic Notation: \(O\), \(\Omega\), \(\Theta\)، Recursion.

**پیش‌نیاز (تولیدشده):** Week 2.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 3 — Lecture notes (Algorithms)](lecture.md) (`week-3-lecture`)
  - [Week 3 — Section](sections.md) (`week-3-section`)
  - [Short: Linear Search](shorts/linear-search.md) (`short-linear-search`)
  - [Short: Binary Search](shorts/binary-search.md) (`short-binary-search`)
  - [Short: Bubble Sort](shorts/bubble-sort.md) (`short-bubble-sort`)
  - [Short: Selection Sort](shorts/selection-sort.md) (`short-selection-sort`)
  - [Short: Call Stacks](shorts/call-stacks.md) (`short-call-stacks`)
  - [Short: Recursion](shorts/recursion.md) (`short-recursion`)
  - [Short: Merge Sort](shorts/merge-sort.md) (`short-merge-sort`)
  - [Week 3 — Lecture source code](source-code/README.md) (`week-3-source-code`)
  - [Problem Set 3](psets/README.md) (`pset-3`)
  - [Recursive atoi — Practice](practice/atoi.md) (`practice-3-atoi`)
  - [Average High Temperatures — Practice](practice/temps.md) (`practice-3-temps`)
  - [Max — Practice](practice/max.md) (`practice-3-max`)
  - [Snackbar — Practice](practice/snackbar.md) (`practice-3-snackbar`)
- **Prerequisites (generated):** [Week 2 — Arrays](../week-02-arrays/week.md) (`week-2`)
- **Backlinks (auto-generated):**
  - [Week 4 — Memory](../week-04-memory/week.md) (`week-4`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
الگوریتم‌ها، جستجو و مرتب‌سازی، Big O و بازگشت. مناسب برای فعالیت‌های فیزیکی (مرتب کردن کارت‌ها) پیش از کدنویسی.

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
- https://cs50.harvard.edu/x/weeks/3/ — retrieved 2026-10-18T05:09:58+03:30, sha256 `0491a46d21697476…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
