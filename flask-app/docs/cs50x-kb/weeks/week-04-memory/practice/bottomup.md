---
id: practice-4-bottomup
type: practice
title: Bottom Up — Practice
week: 4
parent: week-4
children: []
prerequisites:
- week-4-lecture
related:
- concept-file-io
- concept-forms-get-post
- concept-structs
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/bottomup/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:00+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- bmp-format
- bottom-up
- file-headers-metadata
- practice
- structs
checksum: sha256:fdec8a04b345f66e6d1dfa18e3269ee162e366dc3910d849e070b36226076758
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Bottom Up — Practice

## 1. Source metadata
- **Title:** Bottom Up — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/bottomup/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:00+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/bottomup/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="bottom-up"></a>

### Bottom Up

<a id="learning-goals"></a>

#### Learning Goals

* Practice working with images
* Learn about metadata
* Learn more about how `struct`s can be useful

<a id="background"></a>

#### Background

Imagine an image you need to present to your boss for a major presentation somehow got corrupted! Upon investigating, you find that the image is mostly intact. Except, when you view the image, it now appears to be upside down!

Recall that a digital image file is just a sequence of bits, arranged in some fashion. A 24-bit BMP file, then, is essentially just a sequence of bits, (almost) every 24 of which happen to represent some pixel’s color. But a BMP file also contains some “metadata,” information like an image’s height and width. That metadata is stored at the beginning of the file in the form of two data structures generally referred to as “headers,” not to be confused with C’s header files. The first of these headers, called `BITMAPFILEHEADER`, is 14 bytes long. (Recall that 1 byte equals 8 bits.) The second of these headers, called `BITMAPINFOHEADER`, is 40 bytes long. Immediately following these headers is the actual bitmap: an array of bytes, triples of which represent a pixel’s color.

Your job is to edit the metadata programmatically so that the bitmap’s top row is first and bottom row last. Best to avoid editing the pixels directly, lest you further corrupt the file!

* Hints
  * Be sure to look carefully at the members of the `BITMAPINFOHEADER` `struct` in `bmp.h`.
  * If you read the [documentation](https://learn.microsoft.com/en-us/previous-versions//dd183376(v=vs.85)) for each of these members, which should you modify? How so?

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/4/bottomup.zip` followed by Enter in order to download a zip called `bottomup.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip bottomup.zip` to create a folder called `bottomup`.
5. You no longer need the ZIP file, so you can execute `rm bottomup.zip` and respond with “y” followed by Enter at the prompt.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/PTWrnMK23dr9co7YhmLzGU1lM]

<a id="implementation-details"></a>

#### Implementation Details

Go ahead and pull up the URLs to which `BITMAPFILEHEADER` and `BITMAPINFOHEADER` are attributed, per the comments in `bmp.h`. Take a close look at the members of the `BITMAPINFOHEADER` `struct`. Use that information to write a bit of code in `bottomup.c` to change the image from bottom-up to top-down. The code in question needn’t be very complicated, particularly if you know what you’re doing!

<a id="thought-question"></a>

#### Thought Question

* Why do image files need metadata?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
bottomup/ $ ./bottomup harvard_bottomup.bmp harvard_topdown.bmp
```

When your program is working correctly, you should see a new file, `harvard_topdown.bmp` in your `bottomup` directory. Open it up and see if the orientation of the image is correct.

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/bottomup
```

To evaluate that the style of your code (indentations and spacing) is correct, type in the following at the `$` prompt.

```
style50 bottomup.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/4/bottomup.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `bottomup/bmp.h` | 1216 | [yes](bottomup-distribution/files/bottomup/bmp.h) |
| `bottomup/bottomup.c` | 2357 | [yes](bottomup-distribution/files/bottomup/bottomup.c) |
| `bottomup/harvard_bottomup.bmp` | 5972022 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `bottomup`; files shown on the page: `bmp.h`, `bottomup.c`
- check50: `cs50/labs/2023/x/bottomup`
- style50: `bottomup.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Getting Started, Demo, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم file headers / metadata، structs، BMP format.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Flip an upside-down BMP image by editing its header metadata (the image height) rather than its pixels.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 4 — Memory](../week.md) (`week-4`)
- **Prerequisites (generated):** [Week 4 — Lecture notes (Memory)](../lecture.md) (`week-4-lecture`)
- **Related:**
  - [File I/O (fopen, fread, fwrite, fclose)](../../../concepts/file-io.md) (`concept-file-io`)
  - [Forms, GET and POST](../../../concepts/forms-get-post.md) (`concept-forms-get-post`)
  - [Structs and Custom Types (typedef)](../../../concepts/structs.md) (`concept-structs`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین فایل‌های BMP و هدرها.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. کدام فیلد هدر جهت ذخیره‌ی سطرها را مشخص می‌کند؟

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/bottomup` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/bottomup/ — retrieved 2026-10-18T05:11:00+03:30, sha256 `fdec8a04b345f66e…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
