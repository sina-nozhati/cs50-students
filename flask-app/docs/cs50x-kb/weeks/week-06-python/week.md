---
id: week-6
type: week
title: Week 6 — Python
week: 6
parent: course
children:
- week-6-lecture
- week-6-section
- short-python
- week-6-source-code
- pset-6
- practice-6-bank
- practice-6-figlet
- practice-6-jar
- practice-6-seven-day-average
- practice-6-taqueria
prerequisites:
- week-5
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/6/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:01+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- modules-packages
- python-functions-arguments-return-values-variables-boolean-expressions-conditionals-loops
- week
checksum: sha256:3f0eba353d8ce96b26d277a61b551584f553a7ce3b13e717d77340ffc63f240a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 6 — Python

## 1. Source metadata
- **Title:** Week 6 — Python
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/6/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:01+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/6/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-6-python"></a>

### Week 6 *Python*

Python: Functions, Arguments, Return Values; Variables; Boolean Expressions, Conditionals; Loops. Modules, Packages.

[Embedded video: https://video.cs50.io/Rl0ludWTLxs](https://video.cs50.io/Rl0ludWTLxs)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/6/lecture6.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/6/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1dawZYqjfCOZ3byPyqbQ6lUFiw80g2YUJhvT7x9JyKIU/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/6/lecture6.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/6/src6/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/6/src6.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/6/src6.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/6/lang/en/lecture6.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/6/lang/pt/aula6.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/6/lang/es/clase6.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/6/lang/en/lecture6.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/6/lang/pt/aula6.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/6/lang/es/clase6.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/Rl0ludWTLxs)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/6/lecture6-4k.mp4)
      * [YouTube](https://youtu.be/Rl0ludWTLxs)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/iIG8j9kWlIY)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/6/pt/aula6-4k.mp4)
      * [YouTube](https://youtu.be/iIG8j9kWlIY)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/N3zVFYQu3bU)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/6/es/clase6-4k.mp4)
      * [YouTube](https://youtu.be/N3zVFYQu3bU)
* Shorts
  * [Python](https://cs50.harvard.edu/x/shorts/python/)
* [Section](https://cs50.harvard.edu/x/sections/6/)
* [Problem Set 6](https://cs50.harvard.edu/x/psets/6/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Python: Functions, Arguments, Return Values; Variables; Boolean Expressions, Conditionals; Loops
- Modules, Packages

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Python: Functions, Arguments, Return Values; Variables; Boolean Expressions, Conditionals; Loops، Modules, Packages.

**پیش‌نیاز (تولیدشده):** Week 5.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 6 — Lecture notes (Python)](lecture.md) (`week-6-lecture`)
  - [Week 6 — Section](sections.md) (`week-6-section`)
  - [Short: Python](shorts/python.md) (`short-python`)
  - [Week 6 — Lecture source code](source-code/README.md) (`week-6-source-code`)
  - [Problem Set 6](psets/README.md) (`pset-6`)
  - [Home Federal Savings Bank — Practice](practice/bank.md) (`practice-6-bank`)
  - [Frank, Ian and Glen’s Letters — Practice](practice/figlet.md) (`practice-6-figlet`)
  - [Cookie Jar — Practice](practice/jar.md) (`practice-6-jar`)
  - [Seven Day Averages — Practice](practice/seven-day-average.md) (`practice-6-seven-day-average`)
  - [Felipe’s Taqueria — Practice](practice/taqueria.md) (`practice-6-taqueria`)
- **Prerequisites (generated):** [Week 5 — Data Structures](../week-05-data-structures/week.md) (`week-5`)
- **Backlinks (auto-generated):**
  - [Week 7 — SQL](../week-07-sql/week.md) (`week-7`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
Python: بازنویسی ایده‌های C در یک زبان سطح بالا؛ فرصت مقایسه‌ی دو زبان و بهره‌وری.

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
- https://cs50.harvard.edu/x/weeks/6/ — retrieved 2026-10-18T05:10:01+03:30, sha256 `3f0eba353d8ce96b…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
