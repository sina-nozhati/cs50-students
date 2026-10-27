---
id: week-2
type: week
title: Week 2 — Arrays
week: 2
parent: course
children:
- week-2-lecture
- week-2-section
- short-functions
- short-variables-and-scope
- short-debugging-step-through
- short-debugging-step-into
- short-arrays
- short-command-line-arguments
- week-2-source-code
- pset-2
- practice-2-hours
- practice-2-no-vowels
- practice-2-password
prerequisites:
- week-1
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/2/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:09:57+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- arrays
- assembling
- command-line-arguments
- compiling
- cryptography
- debugging
- linking
- preprocessing
- strings
- week
checksum: sha256:b350664816a30ff4ad53867f05022c8ea9a49348a5620997ab05154646236edf
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 2 — Arrays

## 1. Source metadata
- **Title:** Week 2 — Arrays
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/2/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:09:57+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/2/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-2-arrays"></a>

### Week 2 *Arrays*

Preprocessing. Compiling. Assembling. Linking. Debugging. Arrays. Strings. Command-Line Arguments. Cryptography.

[Embedded video: https://video.cs50.io/h5Gc1n8ZuU8](https://video.cs50.io/h5Gc1n8ZuU8)

> **How to download source code into Visual Studio Code** *(collapsible block on the source page)*
>
> 1. Log into [cs50.dev](https://cs50.dev/).
> 2. In your terminal window, type
>
>    ```
>    wget https://cdn.cs50.net/2025/fall/lectures/2/src2.zip
>    ```
>
>    followed by Enter in order to download a Zip file of lecture’s source code into your codespace.
> 3. In your terminal window, type
>
>    ```
>    unzip src2.zip
>    ```
>
>    followed by Enter to unzip (i.e., decompress) that Zip file.
> 4. In your terminal window, type
>
>    ```
>    cd src2
>    ```
>
>    followed by Enter in order to “change directory” into that `src2` directory (i.e., folder).
> 5. In your terminal window, type, e.g.,
>
>    ```
>    make hello0
>    ```
>
>    followed by Enter in order to compile, e.g., `hello0.c` (source code) into `hello0` (machine code).
> 6. In your terminal window, type, e.g.,
>
>    ```
>    ./hello0
>    ```
>
>    followed by Enter in order to run, e.g., `hello0`.

* Lecture
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/2/lecture2.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/2/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1_9dmbiA2uAsnYJb3zkb7-U4u36-cIpsYbbiQ_UKWikg/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/2/lecture2.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/2/src2/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/2/src2.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/2/src2.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/2/lang/en/lecture2.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/2/lang/pt/aula2.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/2/lang/es/clase2.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/2/lang/en/lecture2.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/2/lang/pt/aula2.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/2/lang/es/clase2.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/h5Gc1n8ZuU8)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/2/lecture2-4k.mp4)
      * [YouTube](https://youtu.be/h5Gc1n8ZuU8)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/vdCJU-1mB-A)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/2/pt/aula2-4k.mp4)
      * [YouTube](https://youtu.be/vdCJU-1mB-A)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/G7erq8mRYdk)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/2/es/clase2-4k.mp4)
      * [YouTube](https://youtu.be/G7erq8mRYdk)
* Shorts
  1. [Functions](https://cs50.harvard.edu/x/shorts/functions/)
  2. [Variables and Scope](https://cs50.harvard.edu/x/shorts/variables_and_scope/)
  3. [Debugging (“Step through”)](https://cs50.harvard.edu/x/shorts/debugging_step_through/)
  4. [Debugging (“Step into”)](https://cs50.harvard.edu/x/shorts/debugging_step_into/)
  5. [Arrays](https://cs50.harvard.edu/x/shorts/arrays/)
  6. [Command Line Arguments](https://cs50.harvard.edu/x/shorts/command_line_arguments/)
* [Section](https://cs50.harvard.edu/x/sections/2/)
* [Problem Set 2](https://cs50.harvard.edu/x/psets/2/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- Preprocessing
- Compiling
- Assembling
- Linking
- Debugging
- Arrays
- Strings
- Command-Line Arguments
- Cryptography

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: Preprocessing، Compiling، Assembling، Linking، Debugging، Arrays، Strings، Command-Line Arguments، Cryptography.

**پیش‌نیاز (تولیدشده):** Week 1.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 2 — Lecture notes (Arrays)](lecture.md) (`week-2-lecture`)
  - [Week 2 — Section](sections.md) (`week-2-section`)
  - [Short: Functions](shorts/functions.md) (`short-functions`)
  - [Short: Variables and Scope](shorts/variables-and-scope.md) (`short-variables-and-scope`)
  - [Short: Debugging (“Step through”)](shorts/debugging-step-through.md) (`short-debugging-step-through`)
  - [Short: Debugging (“Step into”)](shorts/debugging-step-into.md) (`short-debugging-step-into`)
  - [Short: Arrays](shorts/arrays.md) (`short-arrays`)
  - [Short: Command Line Arguments](shorts/command-line-arguments.md) (`short-command-line-arguments`)
  - [Week 2 — Lecture source code](source-code/README.md) (`week-2-source-code`)
  - [Problem Set 2](psets/README.md) (`pset-2`)
  - [Hours — Practice](practice/hours.md) (`practice-2-hours`)
  - [N0 V0w3ls — Practice](practice/no-vowels.md) (`practice-2-no-vowels`)
  - [Password — Practice](practice/password.md) (`practice-2-password`)
- **Prerequisites (generated):** [Week 1 — C](../week-01-c/week.md) (`week-1`)
- **Backlinks (auto-generated):**
  - [Week 3 — Algorithms](../week-03-algorithms/week.md) (`week-3`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
آرایه‌ها، رشته‌ها، آرگومان‌های خط فرمان، کامپایل در چند مرحله و اشکال‌زدایی. مفهوم «رشته = آرایه‌ای از کاراکترها» پایه‌ی هفته‌های بعد است.

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
- https://cs50.harvard.edu/x/weeks/2/ — retrieved 2026-10-18T05:09:57+03:30, sha256 `b350664816a30ff4…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
