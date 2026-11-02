---
id: practice-4-license
type: practice
title: License — Practice
week: 4
parent: week-4
children: []
prerequisites:
- week-4-lecture
related:
- concept-arrays
- concept-debugging
- concept-file-io
- concept-memory-errors-and-valgrind
- concept-pointers
- concept-strings
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/license/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:01+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- debug50
- file-pointers
- license
- practice
- strings-arrays
- valgrind
checksum: sha256:53dcf8ea828f0955e54846b341ec57fc705b224790fabb7851a6453b78d9b3af
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# License — Practice

## 1. Source metadata
- **Title:** License — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/license/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:01+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/license/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="license"></a>

### License

<a id="learning-goals"></a>

#### Learning Goals

* Practice working with files and file pointers
* More work with strings and arrays
* Debugging with `debug50`
* Use `valgrind` to check for memory leaks

<a id="background"></a>

#### Background

Suppose you work for a company that develops AI-enhanced license plate recognition technology. As you develop your technology, you may want to use actual license plate numbers as test data. You have a text file with some plate numbers you want to analyze, so you first try reading from that text file and printing out the license plates, to test your file-reading logic. But when you run your program, only the last number prints 8 times! What went wrong?

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/ITMqFWOktPyhwPuK8l6z2poZm]

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/4/license.zip` followed by Enter in order to download a zip called `license.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip license.zip` to create a folder called `license`.
5. You no longer need the ZIP file, so you can execute `rm license.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

If you open the `plates.txt` file, you’ll notice that there are actually 8 different license plate numbers. There are a few errors in the distribution code that are causing this to happen. Let’s start by walking through the code.

We first check for command-line arguments, since `argv[1]` should be the text file that contains the license plates. We then create a character array of length 7, since the plate numbers are 6 `char`s long and we need to save space for the NUL terminator. Now we create an array of `char *`’s (character pointers, otherwise known as `string`s!) to store the 8 plate numbers. We create a file pointer to our external text file, create a variable to hold the index of each array element, and begin reading the file and saving the plate numbers to the array. Finally, to test that we did this correctly, we print out the values in the array.

However, when we compile and execute this code, something is clearly wrong. You’ll need to make the appropriate corrections!

<a id="debugging"></a>

##### Debugging

Take a close look at what values are actually being added to the array. You can experiment with `debug50` to find the error in the distribution code.

* Hints
  * What exactly does the variable `buffer` hold that’s being assigned to each element of the `plates` array?
  * Note that the `plates` array as an array of `char *`’s or string pointers.
  * So when we assign the char array `buffer` to a `char *`, what actually happens?

Is there a better way to copy license plate numbers to the `license` array?

* More Hints
  * Would `strcpy` come in useful here?
  * If you copy data to a pointer, where will that data go?
  * Is `malloc` required here?

<a id="checking-for-memory-leaks"></a>

##### Checking for Memory Leaks

Once your program seems to be working properly, run valgrind to make sure there are no memory leaks.

```
valgrind ./license plates.txt
```

You may end up with something like this:

```
==24478== HEAP SUMMARY:
==24478==     in use at exit: 528 bytes in 9 blocks
==24478==   total heap usage: 10 allocs, 1 frees, 4,624 bytes allocated
==24478== 
==24478== 56 bytes in 8 blocks are definitely lost in loss record 1 of 2
==24478==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==24478==    by 0x109207: main (license.c:30)
==24478== 
==24478== 472 bytes in 1 blocks are still reachable in loss record 2 of 2
==24478==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==24478==    by 0x4A086CD: __fopen_internal (iofopen.c:65)
==24478==    by 0x4A086CD: fopen@@GLIBC_2.2.5 (iofopen.c:86)
==24478==    by 0x1091CD: main (license.c:20)
==24478== 
==24478== LEAK SUMMARY:
==24478==    definitely lost: 56 bytes in 8 blocks
==24478==    indirectly lost: 0 bytes in 0 blocks
==24478==      possibly lost: 0 bytes in 0 blocks
==24478==    still reachable: 472 bytes in 1 blocks
==24478==         suppressed: 0 bytes in 0 blocks
==24478== 
==24478== For lists of detected and suppressed errors, rerun with: -s
==24478== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

There seem to be two kinds of memory errors here that need to be corrected!

* Hint
  * Your line numbers may be different, but note here that there seems to be a memory problem in `main` on line 30 (something to do with `malloc`?), and line 20 (a problem related to `fopen`?). What might the distribution code be missing?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
license/ $ ./license plates.txt
11ZT00
1KAD21
78ZZ01
99ZZ11
72ZZ21
98ZZ31
44ZW41
34ZZ51
```

You can check your code using `check50`, a program that CS50 will use to test your code when you submit, by typing in the following at the `$` prompt. But be sure to test it yourself as well!

```
check50 cs50/labs/2023/x/license
```

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 license.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/4/license.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `license/plates.txt` | 56 | [yes](license-distribution/files/license/plates.txt) |
| `license/license.c` | 644 | [yes](license-distribution/files/license/license.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `license`; files shown on the page: `license.c`, `plates.txt`
- check50: `cs50/labs/2023/x/license`
- style50: `license.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم file pointers، strings/arrays، debug50، valgrind.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Debug a program that reads license plate numbers from a text file but prints them incorrectly, and fix memory issues using debug50 and valgrind.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 4 — Memory](../week.md) (`week-4`)
- **Prerequisites (generated):** [Week 4 — Lecture notes (Memory)](../lecture.md) (`week-4-lecture`)
- **Related:**
  - [Arrays](../../../concepts/arrays.md) (`concept-arrays`)
  - [Debugging (printf, debug50, rubber duck)](../../../concepts/debugging.md) (`concept-debugging`)
  - [File I/O (fopen, fread, fwrite, fclose)](../../../concepts/file-io.md) (`concept-file-io`)
  - [Memory Errors, Leaks and Valgrind](../../../concepts/memory-errors-and-valgrind.md) (`concept-memory-errors-and-valgrind`)
  - [Pointers](../../../concepts/pointers.md) (`concept-pointers`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین اشاره‌گرها، حافظه‌ی پویا و رفع اشکال حافظه.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. بررسی کن هر رشته کجا در حافظه ذخیره می‌شود و چه مدت معتبر است.
2. valgrind را برای پیدا کردن نشت حافظه اجرا کن.

### اشتباه‌های رایج (مفهومی)
- (none)

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/labs/2023/x/license` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/license/ — retrieved 2026-10-18T05:11:01+03:30, sha256 `53dcf8ea828f0955…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
