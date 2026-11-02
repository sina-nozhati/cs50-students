---
id: week-7
type: week
title: Week 7 — SQL
week: 7
parent: course
children:
- week-7-lecture
- week-7-section
- short-sql
- week-7-source-code
- pset-7
- practice-7-favorites
- practice-7-prophecy
prerequisites:
- week-6
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/7/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:02+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- race-conditions
- sql-injection-attacks
- sql-tables-types-statements-constraints-indexes-keywords-functions-transactions
- week
checksum: sha256:aea0b1dff42dbb65cc515768c66a424789dddb15570cf4912b025acf214b7f46
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 7 — SQL

## 1. Source metadata
- **Title:** Week 7 — SQL
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/7/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:02+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/7/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-7-sql"></a>

### Week 7 *SQL*

SQL: Tables; Types; Statements; Constraints; Indexes; Keywords, Functions; Transactions. Race Conditions. SQL Injection Attacks.

[Embedded video: https://video.cs50.io/oqRU2So6Z2Y](https://video.cs50.io/oqRU2So6Z2Y)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/7/lecture7.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/7/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1LIwdwxj6Byq9RMe2Pwz9RiurtWDBX1YDrCgju_uirEI/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/7/lecture7.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/7/src7/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/7/src7.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/7/src7.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/7/lang/pt/aula7.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/7/lang/es/clase7.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/7/lang/pt/aula7.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/7/lang/es/clase7.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/oqRU2So6Z2Y)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/7/lecture7-4k.mp4)
      * [YouTube](https://youtu.be/oqRU2So6Z2Y)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/Samqz7iHwPM)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/7/pt/aula7-4k.mp4)
      * [YouTube](https://youtu.be/Samqz7iHwPM)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/VnfMRaZUSrc)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/7/es/clase7-4k.mp4)
      * [YouTube](https://youtu.be/VnfMRaZUSrc)
* Shorts
  * [SQL](https://cs50.harvard.edu/x/shorts/sql/)
* [Section](https://cs50.harvard.edu/x/sections/7/)
* [Problem Set 7](https://cs50.harvard.edu/x/psets/7/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- SQL: Tables; Types; Statements; Constraints; Indexes; Keywords, Functions; Transactions
- Race Conditions
- SQL Injection Attacks

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: SQL: Tables; Types; Statements; Constraints; Indexes; Keywords, Functions; Transactions، Race Conditions، SQL Injection Attacks.

**پیش‌نیاز (تولیدشده):** Week 6.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 7 — Lecture notes (SQL)](lecture.md) (`week-7-lecture`)
  - [Week 7 — Section](sections.md) (`week-7-section`)
  - [Short: SQL](shorts/sql.md) (`short-sql`)
  - [Week 7 — Lecture source code](source-code/README.md) (`week-7-source-code`)
  - [Problem Set 7](psets/README.md) (`pset-7`)
  - [Favorites — Practice](practice/favorites.md) (`practice-7-favorites`)
  - [Hall of Prophecy — Practice](practice/prophecy.md) (`practice-7-prophecy`)
- **Prerequisites (generated):** [Week 6 — Python](../week-06-python/week.md) (`week-6`)
- **Backlinks (auto-generated):**
  - [Artificial Intelligence — Artificial Intelligence](../week-ai-artificial-intelligence/week.md) (`week-ai`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
SQL و پایگاه داده‌ی رابطه‌ای؛ طراحی جدول، JOIN و خطرات SQL injection.

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
- https://cs50.harvard.edu/x/weeks/7/ — retrieved 2026-10-18T05:10:02+03:30, sha256 `aea0b1dff42dbb65…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
