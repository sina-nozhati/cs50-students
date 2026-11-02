---
id: pset-4-volume
type: pset
title: Volume — Problem Set 4
week: 4
parent: pset-4
children: []
prerequisites:
- week-4-lecture
related:
- concept-binary
- concept-data-types
- concept-file-io
- concept-pointers
source_urls:
- https://cs50.harvard.edu/x/psets/4/volume/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:28+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- binary-data
- file-i-o-fopen-fread-fwrite
- pointers
- pset
- stdinth-types
- volume
checksum: sha256:7e2eb487f5f47a94c0682a57acf8f4c2f5293c0a94e7b63d46a09f6e35021a62
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Volume — Problem Set 4

## 1. Source metadata
- **Title:** Volume — Problem Set 4
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/4/volume/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/4/volume/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="volume"></a>

### Volume

![WAV file waveform](https://cs50.harvard.edu/x/psets/4/volume/wav_file.png)

<a id="problem-to-solve"></a>

#### Problem to Solve

[WAV files](https://docs.fileformat.com/audio/wav/) are a common file format for representing audio. WAV files store audio as a sequence of “samples”: numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte “header” that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single 2-byte (16-bit) integer representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

In a file called `volume.c` in a folder called `volume`, write a program to modify the volume of an audio file.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/mc2hPhYDt1spoMjlqNMuqC4Uc]

<a id="distribution-code"></a>

#### Distribution Code

For this problem, you’ll extend the functionality of code provided to you by CS50’s staff.

> **Download the distribution code** *(collapsible block on the source page)*
>
> Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:
>
> ```
> $
> ```
>
> Next execute
>
> ```
> wget https://cdn.cs50.net/2026/x/psets/4/volume.zip
> ```
>
> in order to download a ZIP called `volume.zip` into your codespace.
>
> Then execute
>
> ```
> unzip volume.zip
> ```
>
> to create a folder called `volume`. You no longer need the ZIP file, so you can execute
>
> ```
> rm volume.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd volume
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> volume/ $
> ```
>
> If all was successful, you should execute
>
> ```
> ls
> ```
>
> and see a file named `volume.c`. Executing `code volume.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

<a id="implementation-details"></a>

#### Implementation Details

Complete the implementation of `volume.c`, such that it changes the volume of a sound file by a given factor.

* The program should accept three command-line arguments. The first is `input`, which represents the name of the original audio file. The second is `output`, which represents the name of the new audio file that should be generated. The third is `factor`, which is the amount by which the volume of the original audio file should be scaled.
  * For example, if `factor` is `2.0`, then your program should double the volume of the audio file in `input` and save the newly generated audio file in `output`.
* Your program should first read the header from the input file and write the header to the output file.
* Your program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Your program should multiply each sample by the `factor` and write the new sample to the output file.
  * You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we’ll assume 16-bit samples for this problem.
* Your program, if it uses `malloc`, must not leak any memory.

<a id="hints"></a>

#### Hints

> **Understand the code in volume.c** *(collapsible block on the source page)*
>
> Notice first that `volume.c` is already set up to take three command-line arguments, `input`, `output`, and `factor`.
>
> * `main` takes both an `int`, `argc`, and an array of `char *`s (strings!), `argv`.
> * If `argc`, the number of arguments at the command-line including the program itself, is not equal to 4, the program will print its proper usage and exit with status code 1.
>
> ```c
> int main(int argc, char *argv[])
> {
>     // Check command-line arguments
>     if (argc != 4)
>     {
>         printf("Usage: ./volume input.wav output.wav factor\n");
>         return 1;
>     }
>
>     // ...
> }
> ```
>
> Next, `volume.c` uses [`fopen`](https://manual.cs50.io/3/fopen) to open the two files provided as command-line arguments.
>
> * It’s best practice to check if the result of calling `fopen` is `NULL`. If it is, the file wasn’t found or wasn’t able to be opened.
>
> ```c
> // Open files and determine scaling factor
> FILE *input = fopen(argv[1], "r");
> if (input == NULL)
> {
>     printf("Could not open file.\n");
>     return 1;
> }
>
> FILE *output = fopen(argv[2], "w");
> if (output == NULL)
> {
>     printf("Could not open file.\n");
>     return 1;
> }
> ```
>
> Later, these files are closed with `fclose`. Whenever you call `fopen`, you should later call `fclose`!
>
> ```c
> // Close files
> fclose(input);
> fclose(output);
> ```
>
> Before closing the files, though, notice that we have a few TODOs.
>
> ```c
> // TODO: Copy header from input file to output file
>
> // TODO: Read samples from input file and write updated data to output file
> ```
>
> Odds are you’ll need to know the factor by which to scale the volume, hence why `volume.c` already converts the third command-line argument to a `float` for you!
>
> ```c
> float factor = atof(argv[3]);
> ```

> **Copy WAV header from input file to output file** *(collapsible block on the source page)*
>
> Your first TODO is to copy the WAV file header from `input` and write it to `output`. First, though, you’ll need to learn about a few special data types.
>
> So far, we’ve seen a number of different types in C, including `int`, `bool`, `char`, `double`, `float`, and `long`. However, inside a header file called `stdint.h` are the declarations of a number of *other* types that allow us to very precisely define the size (in bits) and sign (signed or unsigned) of an integer. Two types in particular will be useful to us when working with WAV files:
>
> * `uint8_t` is a type that stores an 8-bit (hence `8`!) unsigned (i.e., not negative) integer (hence `uint`!). We can treat each byte of a WAV file’s header as a `uint8_t` value.
> * `int16_t` is a type that stores a 16-bit signed (i.e., positive or negative) integer. We can treat each sample of audio in a WAV file as an `int16_t` value.
>
> You’ll likely want to create an array of bytes to store the data from the WAV file header that you’ll read from the input file. Using the `uint8_t` type to represent a byte, you can create an array of `n` bytes for your header with syntax like
>
> ```
> uint8_t header[n];
> ```
>
> replacing `n` with the number of bytes. You can then use `header` as an argument to [`fread`](https://manual.cs50.io/3/fread) or [`fwrite`](https://manual.cs50.io/3/fwrite) to read into or write from the header.
>
> Recall that a WAV file’s header is always exactly 44 bytes long. Note that `volume.c` already defines a variable for you called `HEADER_SIZE`, equal to the number of bytes in the header.
>
> The below is a pretty big hint, but here’s how you could accomplish this TODO!
>
> ```c
> // Copy header from input file to output file
> uint8_t header[HEADER_SIZE];
> fread(header, HEADER_SIZE, 1, input);
> fwrite(header, HEADER_SIZE, 1, output);
> ```

> **Write updated data to output file** *(collapsible block on the source page)*
>
> Your next TODO is to read samples from `input`, update those samples, and write the updated samples to `output`. When reading files, it’s common to create a “buffer” in which to temporarily store data. There, you can modify the data and—once it’s ready—write the buffer’s data to a new file.
>
> Recall that we can use the `int16_t` type to represent a sample of a WAV file. To store an audio sample, then, you can create a buffer variable with syntax like:
>
> ```c
> // Create a buffer for a single sample
> int16_t buffer;
> ```
>
> With a buffer for samples in place, you can now read data into it, one sample at a time. Try using `fread` for this task! You can use `&buffer`, the address of `buffer`, as an argument to `fread` or `fwrite` to read into or write from the buffer. (Recall that the `&` operator is used to get the address of the variable.)
>
> ```c
> // Create a buffer for a single sample
> int16_t buffer;
>
> // Read single sample into buffer
> fread(&buffer, sizeof(int16_t), 1, input);
> ```
>
> Now, to increase (or decrease) the volume of a sample, you need only multiply it by some factor.
>
> ```c
> // Create a buffer for a single sample
> int16_t buffer;
>
> // Read single sample into buffer
> fread(&buffer, sizeof(int16_t), 1, input);
>
> // Update volume of sample
> buffer *= factor;
> ```
>
> And finally, you can write that updated sample to `output`:
>
> ```c
> // Create a buffer for a single sample
> int16_t buffer;
>
> // Read single sample from input into buffer
> fread(&buffer, sizeof(int16_t), 1, input);
>
> // Update volume of sample
> buffer *= factor;
>
> // Write updated sample to new file
> fwrite(&buffer, sizeof(int16_t), 1, output);
> ```
>
> There’s just one problem: you’ll need to *continue* reading a sample into your buffer, updating its volume, and writing the updated sample to the output file while there are still samples left to read.
>
> * Thankfully, per its documentation, `fread` will return the number of items of data successfully read. You may find this useful to check for when you’ve reached the end of the file!
> * Keep in mind there’s no reason you can’t call `fread` inside of a `while` loop’s conditional. You could, for example, make a call to `fread` like the following:
>
>   ```c
>   while (fread(...))
>   {
>
>   }
>   ```
>
> It’s quite the hint, but see the below for an efficient way to solve this problem:
>
> ```c
> // Create a buffer for a single sample
> int16_t buffer;
>
> // Read single sample from input into buffer while there are samples left to read
> while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
> {
>     // Update volume of sample
>     buffer *= factor;
>
>     // Write updated sample to new file
>     fwrite(&buffer, sizeof(int16_t), 1, output);
> }
> ```
>
> Because the version of C you’re using treats non-zero values as `true` and zero values as `false`, you could simplify the above syntax to the following:
>
> ```c
> // Create a buffer for a single sample
> int16_t buffer;
>
> // Read single sample from input into buffer while there are samples left to read
> while (fread(&buffer, sizeof(int16_t), 1, input))
> {
>     // Update volume of sample
>     buffer *= factor;
>
>     // Write updated sample to new file
>     fwrite(&buffer, sizeof(int16_t), 1, output);
> }
> ```

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/LiGhjz9ColQ](https://www.youtube.com/embed/LiGhjz9ColQ)

> **Not sure how to solve?** *(collapsible block on the source page)*
>

<a id="how-to-test"></a>

#### How to Test

Your program should behave per the examples below.

```
$ ./volume input.wav output.wav 2.0
```

When you listen to `output.wav` (as by control-clicking on `output.wav` in the file browser, choosing **Download**, and then opening the file in an audio player on your computer), it should be twice as loud as `input.wav`!

```
$ ./volume input.wav output.wav 0.5
```

When you listen to `output.wav`, it should be half as loud as `input.wav`!

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/volume
```

<a id="style"></a>

##### Style

```
style50 volume.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/volume
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/4/volume.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `volume/volume.c` | 902 | [yes](volume-distribution/files/volume/volume.c) |
| `volume/input.wav` | 352844 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `volume`; files shown on the page: `volume.c`
- check50: `cs50/problems/2026/x/volume`
- style50: `volume.c`
- submit50: `cs50/problems/2026/x/volume`
- Page sections (order on source): Problem to Solve, Demo, Distribution Code, Implementation Details, Hints, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/LiGhjz9ColQ
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم file I/O (fopen/fread/fwrite)، binary data، stdint.h types، pointers.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete volume.c, which takes an input WAV file, an output file name and a scaling factor as command-line arguments. It copies the 44-byte header unchanged, then multiplies every 16-bit sample by the factor and writes it out. This practises binary file I/O.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 4](README.md) (`pset-4`)
- **Prerequisites (generated):** [Week 4 — Lecture notes (Memory)](../lecture.md) (`week-4-lecture`)
- **Related:**
  - [Binary and Representation](../../../concepts/binary.md) (`concept-binary`)
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [File I/O (fopen, fread, fwrite, fclose)](../../../concepts/file-io.md) (`concept-file-io`)
  - [Pointers](../../../concepts/pointers.md) (`concept-pointers`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
اولین کار با فایل‌های باینری: هدر، نمونه‌ها و انواع اندازه‌ثابت.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. فایل WAV از دو بخش تشکیل شده؛ هرکدام را چطور باید کپی یا تغییر داد؟
2. اندازه‌ی هر نمونه چند بایت است و کدام نوع داده با آن جور است؟
3. خواندن و نوشتن را تکه به تکه انجام بده و به مقدار برگشتی توابع توجه کن.

### اشتباه‌های رایج (مفهومی)
- استفاده از نوع با اندازه‌ی نادرست
- دست‌کاری هدر

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/volume` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/4/volume/ — retrieved 2026-10-18T05:11:28+03:30, sha256 `7e2eb487f5f47a94…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
