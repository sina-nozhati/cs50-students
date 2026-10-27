---
id: week-9
type: week
title: Week 9 — Flask
week: 9
parent: course
children:
- week-9-lecture
- week-9-section
- short-flask
- short-ajax
- week-9-source-code
- pset-9
- practice-9-helloflask
prerequisites:
- week-8
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/9/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:05+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- cookies
- decorators
- flask
- requests-responses
- route
- sessions
- week
checksum: sha256:c8116d924e3c9179cc413b20f2bd927b8c601ba8926dfc952844630b56828531
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 9 — Flask

## 1. Source metadata
- **Title:** Week 9 — Flask
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/9/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:05+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/9/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-9-flask"></a>

### Week 9 *Flask*

Flask. Route. Decorators. Requests, Responses. Sessions. Cookies.

[Embedded video: https://video.cs50.io/am7POvSZ4GE](https://video.cs50.io/am7POvSZ4GE)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/9/lecture9.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/9/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1WZ3kAMUcku8g-pR80RRM1OjPL4AAaBvfNK4-ERdjv5g/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/9/lecture9.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/9/src9/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/9/src9.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/9/src9.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/9/lang/en/lecture9.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/9/lang/pt/aula9.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/9/lang/es/clase9.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/9/lang/en/lecture9.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/9/lang/pt/aula9.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/9/lang/es/clase9.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/am7POvSZ4GE)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/9/lecture9-4k.mp4)
      * [YouTube](https://youtu.be/am7POvSZ4GE)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/Uddye35TNp4)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/9/pt/aula9-4k.mp4)
      * [YouTube](https://youtu.be/Uddye35TNp4)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/7Yd_xMuzPHE)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/9/es/clase9-4k.mp4)
      * [YouTube](https://youtu.be/7Yd_xMuzPHE)
* Shorts
  1. [Flask](https://cs50.harvard.edu/x/shorts/flask/)
  2. [AJAX](https://cs50.harvard.edu/x/shorts/ajax/)
* [Section](https://cs50.harvard.edu/x/sections/9/)
* [Problem Set 9](https://cs50.harvard.edu/x/psets/9/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Flask
- Route
- Decorators
- Requests, Responses
- Sessions
- Cookies

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Flask، Route، Decorators، Requests, Responses، Sessions، Cookies.

**پیش‌نیاز (تولیدشده):** Week 8.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 9 — Lecture notes (Flask)](lecture.md) (`week-9-lecture`)
  - [Week 9 — Section](sections.md) (`week-9-section`)
  - [Short: Flask](shorts/flask.md) (`short-flask`)
  - [Short: AJAX](shorts/ajax.md) (`short-ajax`)
  - [Week 9 — Lecture source code](source-code/README.md) (`week-9-source-code`)
  - [Problem Set 9](psets/README.md) (`pset-9`)
  - [Hello, Flask — Practice](practice/helloflask.md) (`practice-9-helloflask`)
- **Prerequisites (generated):** [Week 8 — HTML, CSS, JavaScript](../week-08-html-css-javascript/week.md) (`week-8`)
- **Backlinks (auto-generated):**
  - [Final Project](../../final-project/README.md) (`final-project`)
  - [Week 10](../week-10/week.md) (`week-10`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
Flask: برنامه‌ی وب سمت سرور، فرم‌ها، سشن و پایگاه داده؛ پل اصلی به پروژه‌ی نهایی.

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
- https://cs50.harvard.edu/x/weeks/9/ — retrieved 2026-10-18T05:10:05+03:30, sha256 `c8116d924e3c9179…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
