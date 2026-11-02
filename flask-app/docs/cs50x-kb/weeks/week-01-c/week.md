---
id: week-1
type: week
title: Week 1 — C
week: 1
parent: course
children:
- week-1-lecture
- week-1-section
- short-data-types
- short-operators
- short-conditional-statements
- short-loops
- short-command-line
- short-magic-numbers
- week-1-source-code
- pset-1
- practice-1-debug
- practice-1-half
- practice-1-prime
prerequisites:
- week-0
related: []
source_urls:
- https://cs50.harvard.edu/x/weeks/1/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:09:56+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- c
- command-line-interface-cli
- comments
- compiler
- conditionals
- constants
- correctness-design-style
- escape-sequences
- floating-point-imprecision
- graphical-user-interface-gui
- header-files
- integer-overflow
- libraries
- linux
- loops
- machine-code
- manual-pages
- operators
- pseudocode
- source-code
- syntax-highlighting
- types
- variables
- visual-studio-code
- week
checksum: sha256:c37fbc14b8bcf3a194e83986e9c01706f53f112c66ec29b0f8a57de901f475d9
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 1 — C

## 1. Source metadata
- **Title:** Week 1 — C
- **Type:** week
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/weeks/1/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:09:56+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/weeks/1/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="week-1-c"></a>

### Week 1 *C*

C. Source Code. Machine Code. Compiler. Correctness, Design, Style. Visual Studio Code. Syntax Highlighting. Escape Sequences. Header Files. Libraries. Manual Pages. Types. Conditionals. Variables. Loops. Linux. Graphical User Interface (GUI). Command-Line Interface (CLI). Constants. Comments. Pseudocode. Operators. Integer Overflow. Floating-Point Imprecision.

[Embedded video: https://video.cs50.io/SlqjA04_dpk](https://video.cs50.io/SlqjA04_dpk)

> **How to download source code into VS Code** *(collapsible block on the source page)*
>
> 1. Log into [cs50.dev](https://cs50.dev/).
> 2. In your terminal window, type
>
>    ```
>    wget https://cdn.cs50.net/2025/fall/lectures/1/src1.zip
>    ```
>
>    followed by Enter in order to download a Zip file of lecture’s source code into your codespace.
> 3. In your terminal window, type
>
>    ```
>    unzip src1.zip
>    ```
>
>    followed by Enter to unzip (i.e., decompress) that Zip file.
> 4. In your terminal window, type
>
>    ```
>    cd src1
>    ```
>
>    followed by Enter in order to “change directory” into that `src1` directory (i.e., folder).
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
  * [Audio](https://cdn.cs50.net/2025/fall/lectures/1/lecture1.mp3)
  * [Notes](https://cs50.harvard.edu/x/notes/1/)
  * Slides
    * [Google Slides](https://docs.google.com/presentation/d/1dwmy6Vm-fzKdUShsAhmHMPwE_O6LfA6o9EgMN_zWmvs/edit?usp=sharing)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/1/lecture1.pdf)
  * Source Code
    * [Index](https://cdn.cs50.net/2025/fall/lectures/1/src1/)
    * [PDF](https://cdn.cs50.net/2025/fall/lectures/1/src1.pdf)
    * [Zip](https://cdn.cs50.net/2025/fall/lectures/1/src1.zip)
  * Subtitles
    * [English](https://cdn.cs50.net/2025/fall/lectures/1/lang/en/lecture1.srt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/1/lang/pt/aula1.srt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/1/lang/es/clase1.srt)
  * Transcripts
    * [English](https://cdn.cs50.net/2025/fall/lectures/1/lang/en/lecture1.txt)
    * [Portuguese](https://cdn.cs50.net/2025/fall/lectures/1/lang/pt/aula1.txt)
    * [Spanish](https://cdn.cs50.net/2025/fall/lectures/1/lang/es/clase1.txt)
  * Video
    * English
      * [CS50 Video Player](https://video.cs50.io/SlqjA04_dpk)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/1/lecture1-4k.mp4)
      * [YouTube](https://youtu.be/SlqjA04_dpk)
    * Portuguese
      * [CS50 Video Player](https://video.cs50.io/eepzDoovmAw)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/1/pt/aula1-4k.mp4)
      * [YouTube](https://youtu.be/eepzDoovmAw)
    * Spanish
      * [CS50 Video Player](https://video.cs50.io/7hxVvUoo-PI)
      * MP4
        * HDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-360p-hdr.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-720p-hdr.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-1080p-hdr.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-4k-hdr.mp4)
        * SDR
          * [360p](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-360p.mp4)
          * [720p](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-720p.mp4)
          * [1080p](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-1080p.mp4)
          * [4K](https://cdn.cs50.net/2025/fall/lectures/1/es/clase1-4k.mp4)
      * [YouTube](https://youtu.be/7hxVvUoo-PI)
* Shorts
  1. [Data Types](https://cs50.harvard.edu/x/shorts/data_types/)
  2. [Operators](https://cs50.harvard.edu/x/shorts/operators/)
  3. [Conditional Statements](https://cs50.harvard.edu/x/shorts/conditional_statements/)
  4. [Loops](https://cs50.harvard.edu/x/shorts/loops/)
  5. [Command Line](https://cs50.harvard.edu/x/shorts/command_line/)
  6. [Magic Numbers](https://cs50.harvard.edu/x/shorts/magic_numbers/)
* [Section](https://cs50.harvard.edu/x/sections/1/)
* [Problem Set 1](https://cs50.harvard.edu/x/psets/1/)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Topics listed for this week on the source (order as on source):**

- C
- Source Code
- Machine Code
- Compiler
- Correctness, Design, Style
- Visual Studio Code
- Syntax Highlighting
- Escape Sequences
- Header Files
- Libraries
- Manual Pages
- Types
- Conditionals
- Variables
- Loops
- Linux
- Graphical User Interface (GUI)
- Command-Line Interface (CLI)
- Constants
- Comments
- Pseudocode
- Operators
- Integer Overflow
- Floating-Point Imprecision

- Lecture recording term (from media URLs): 2025/fall
- Video languages: English, Portuguese, Spanish
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده از فهرست موضوعات):** پس از این هفته دانشجو باید بتواند هر یک از این موضوعات را توضیح دهد و در تمرین‌ها به کار ببرد: C، Source Code، Machine Code، Compiler، Correctness, Design, Style، Visual Studio Code، Syntax Highlighting، Escape Sequences، Header Files، Libraries، Manual Pages، Types، Conditionals، Variables، Loops، Linux، Graphical User Interface (GUI)، Command-Line Interface (CLI)، Constants، Comments، Pseudocode، Operators، Integer Overflow، Floating-Point Imprecision.

**پیش‌نیاز (تولیدشده):** Week 0.

## 4. Relationships
- **Parent:** [CS50x 2026 — course home (CS50’s Introduction to Computer Science)](../../course/README.md) (`course`)
- **Children:**
  - [Week 1 — Lecture notes (C)](lecture.md) (`week-1-lecture`)
  - [Week 1 — Section](sections.md) (`week-1-section`)
  - [Short: Data Types](shorts/data-types.md) (`short-data-types`)
  - [Short: Operators](shorts/operators.md) (`short-operators`)
  - [Short: Conditional Statements](shorts/conditional-statements.md) (`short-conditional-statements`)
  - [Short: Loops](shorts/loops.md) (`short-loops`)
  - [Short: Command Line](shorts/command-line.md) (`short-command-line`)
  - [Short: Magic Numbers](shorts/magic-numbers.md) (`short-magic-numbers`)
  - [Week 1 — Lecture source code](source-code/README.md) (`week-1-source-code`)
  - [Problem Set 1](psets/README.md) (`pset-1`)
  - [Debug — Practice](practice/debug.md) (`practice-1-debug`)
  - [Half — Practice](practice/half.md) (`practice-1-half`)
  - [Prime — Practice](practice/prime.md) (`practice-1-prime`)
- **Prerequisites (generated):** [Week 0 — Scratch](../week-00-scratch/week.md) (`week-0`)
- **Backlinks (auto-generated):**
  - [Week 2 — Arrays](../week-02-arrays/week.md) (`week-2`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
ورود به C: کامپایل، انواع داده، شرط، حلقه و توابع. بیشترین چالش دانشجویان مبتدی در این هفته محیط ترمینال و نحو C است؛ کارگاه عملی کار با VS Code پیشنهاد می‌شود.

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
- https://cs50.harvard.edu/x/weeks/1/ — retrieved 2026-10-18T05:09:56+03:30, sha256 `c37fbc14b8bcf3a1…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
