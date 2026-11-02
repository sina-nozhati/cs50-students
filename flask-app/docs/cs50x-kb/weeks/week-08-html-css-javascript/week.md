---
id: week-8
type: week
title: Week 8 — HTML, CSS, JavaScript
week: 8
parent: course
children:
- week-8-lecture
- week-8-section
- short-internet-primer
- short-ip
- short-tcp
- short-http
- short-html
- short-css
- short-javascript
- short-dom
- week-8-source-code
- pset-8
- practice-8-redo
prerequisites:
- week-ai
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/8/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:04+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- css-properties-selectors
- events
- frameworks
- html-tags-attributes
- http-urls-get-post
- internet-routers-tcp-ip-dns
- javascript-variables-conditionals-loops
- regular-expressions
- servers
- week
checksum: sha256:175c52bd624df6ac548b6f851b510d0f110b889f384b36a33fc142cff2e69e15
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 8 — HTML, CSS, JavaScript

## 1. Source metadata
- **Title:** Week 8 — HTML, CSS, JavaScript
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/8/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:04+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/8/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-8-html-css-javascript"></a>

### Week 8 *HTML, CSS, JavaScript*

Internet: Routers; TCP/IP; DNS. HTTP: URLs, GET, POST. HTML: Tags; Attributes. Servers. Regular Expressions. CSS: Properties; Selectors. Frameworks. JavaScript: Variables; Conditionals; Loops. Events.

[Embedded video: https://video.cs50.io/yYst7puZXjw](https://video.cs50.io/yYst7puZXjw)

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/8/lecture8.mp3)
  * Demos
    * [Passing TCP/IP Packet](https://youtu.be/cUJlRNRguAM)
      * [Outtakes](https://www.youtube.com/watch?v=mofAEZ6fWLc)
  * [Notes](https://cs50.harvard.edu/x/notes/8/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1vG7P0wmMl6KRzXOs5w7qop2FPijnHGHUh7VNrCNc3Ww/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/8/lecture8.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/8/src8/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/8/src8.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/8/src8.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/8/lang/en/lecture8.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/8/lang/pt/aula8.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/8/lang/es/clase8.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/8/lang/en/lecture8.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/8/lang/pt/aula8.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/8/lang/es/clase8.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/yYst7puZXjw)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/8/lecture8-4k.mp4)
      * [YouTube](https://youtu.be/yYst7puZXjw)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/i_GmZgveqpw)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/8/pt/aula8-4k.mp4)
      * [YouTube](https://youtu.be/i_GmZgveqpw)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/3Ph5G_sfrFM)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/8/es/clase8-4k.mp4)
      * [YouTube](https://youtu.be/3Ph5G_sfrFM)
* Shorts
  1. [Internet Primer](https://cs50.harvard.edu/x/shorts/internet_primer/)
  2. [IP](https://cs50.harvard.edu/x/shorts/ip/)
  3. [TCP](https://cs50.harvard.edu/x/shorts/tcp/)
  4. [HTTP](https://cs50.harvard.edu/x/shorts/http/)
  5. [HTML](https://cs50.harvard.edu/x/shorts/html/)
  6. [CSS](https://cs50.harvard.edu/x/shorts/css/)
  7. [JavaScript](https://cs50.harvard.edu/x/shorts/javascript/)
  8. [DOM](https://cs50.harvard.edu/x/shorts/dom/)
* [Section](https://cs50.harvard.edu/x/sections/8/)
* [Problem Set 8](https://cs50.harvard.edu/x/psets/8/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Internet: Routers; TCP/IP; DNS
- HTTP: URLs, GET, POST
- HTML: Tags; Attributes
- Servers
- Regular Expressions
- CSS: Properties; Selectors
- Frameworks
- JavaScript: Variables; Conditionals; Loops
- Events

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Internet: Routers; TCP/IP; DNS، HTTP: URLs, GET, POST، HTML: Tags; Attributes، Servers، Regular Expressions، CSS: Properties; Selectors، Frameworks، JavaScript: Variables; Conditionals; Loops، Events.

**پیش‌نیاز (تولیدشده):** Artificial Intelligence.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 8 — Lecture notes (HTML, CSS, JavaScript)](lecture.md) (`week-8-lecture`)
  - [Week 8 — Section](sections.md) (`week-8-section`)
  - [Short: Internet Primer](shorts/internet-primer.md) (`short-internet-primer`)
  - [Short: IP](shorts/ip.md) (`short-ip`)
  - [Short: TCP](shorts/tcp.md) (`short-tcp`)
  - [Short: HTTP](shorts/http.md) (`short-http`)
  - [Short: HTML](shorts/html.md) (`short-html`)
  - [Short: CSS](shorts/css.md) (`short-css`)
  - [Short: JavaScript](shorts/javascript.md) (`short-javascript`)
  - [Short: DOM](shorts/dom.md) (`short-dom`)
  - [Week 8 — Lecture source code](source-code/README.md) (`week-8-source-code`)
  - [Problem Set 8](psets/README.md) (`pset-8`)
  - [Radio Shack Redo — Practice](practice/redo.md) (`practice-8-redo`)
- **Prerequisites (generated):** [Artificial Intelligence — Artificial Intelligence](../week-ai-artificial-intelligence/week.md) (`week-ai`)
- **Backlinks (auto-generated):**
  - [Week 9 — Flask](../week-09-flask/week.md) (`week-9`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
وب: اینترنت، HTTP، HTML، CSS و JavaScript؛ پایه‌ی پروژه‌های وب.

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
- https://cs50.harvard.edu/x/weeks/8/ — retrieved 2026-10-18T05:10:04+03:30, sha256 `175c52bd624df6ac…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
