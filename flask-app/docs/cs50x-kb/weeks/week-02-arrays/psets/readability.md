---
id: pset-2-readability
type: pset
title: Readability — Problem Set 2
week: 2
parent: pset-2
children: []
prerequisites:
- week-2-lecture
related:
- concept-data-types
- concept-functions
- concept-strings
- pset-6-readability
source_urls:
- https://cs50.harvard.edu/x/psets/2/readability/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:21+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- counting-characters
- functions
- mathh-round
- pset
- readability
- string-iteration
- type-casting-floats
checksum: sha256:c533f737698f08ebb3a938c6678521a351c0f99c7533c64b4b41a8f7466e1fde
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Readability — Problem Set 2

## 1. Source metadata
- **Title:** Readability — Problem Set 2
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/2/readability/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:21+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/2/readability/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="readability"></a>

### Readability

![Charlotte's Web Cover](https://cs50.harvard.edu/x/psets/2/readability/charlottes_web.jpg)

<a id="problem-to-solve"></a>

#### Problem to Solve

According to [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), E.B. White’s *Charlotte’s Web* is between a second- and fourth-grade reading level, and Lois Lowry’s *The Giver* is between an eighth- and twelfth-grade reading level. What does it mean, though, for a book to be at a particular reading level?

Well, in many cases, a human expert might read a book and make a decision on the grade (i.e., year in school) for which they think the book is most appropriate. But an algorithm could likely figure that out too!

In a file called `readability.c` in a folder called `readability`, you’ll implement a program that calculates the approximate grade level needed to comprehend some text. Your program should print as output “Grade X” where “X” is the grade level computed, rounded to the nearest integer. If the grade level is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output “Grade 16+” instead of giving the exact index number. If the grade level is less than 1, your program should output “Before Grade 1”.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj]

<a id="background"></a>

#### Background

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too.

A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the *Coleman-Liau index*. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is

```
index = 0.0588 * L - 0.296 * S - 15.8
```

where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.

<a id="advice"></a>

#### Advice

> **Write some code that you know will compile** *(collapsible block on the source page)*
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <math.h>
> #include <stdio.h>
> #include <string.h>
>
> int main(void)
> {
>
> }
> ```
>
> Notice that you’ve now included a few header files that will give you access to functions which might help you solve this problem.

> **Write some pseudocode before writing more code** *(collapsible block on the source page)*
>
> If unsure how to solve the problem itself, break it down into smaller problems that you can probably solve first. For instance, this problem is really only a handful of problems:
>
> 1. Prompt the user for some text
> 2. Count the number of letters, words, and sentences in the text
> 3. Compute the Coleman-Liau index
> 4. Print the grade level
>
> Let’s write some pseudcode as comments to remind you to do just that:
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <math.h>
> #include <stdio.h>
> #include <string.h>
>
> int main(void)
> {
>     // Prompt the user for some text
>
>     // Count the number of letters, words, and sentences in the text
>
>     // Compute the Coleman-Liau index
>
>     // Print the grade level
> }
> ```

> **Convert the pseudocode to code** *(collapsible block on the source page)*
>
> First, consider how you might prompt the user for some text. Recall that `get_string`, a function in the CS50 library, can prompt the user for a string.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <math.h>
> #include <stdio.h>
> #include <string.h>
>
> int main(void)
> {
>     // Prompt the user for some text
>     string text = get_string("Text: ");
>
>     // Count the number of letters, words, and sentences in the text
>
>     // Compute the Coleman-Liau index
>
>     // Print the grade level
> }
> ```
>
> Now that you’ve collected input from the user, you can begin to analyze that input. First, try to count the number of letters in the text. Consider letters to be uppercase or lowercase alphabetical character, not punctuation, digits, or other symbols.
>
> One way to approach this problem is to create a function called `count_letters` that takes a string, `text`, as input, and then returns the number of letters in that text as an `int`.
>
> ```c
> int count_letters(string text)
> {
>     // Return the number of letters in text
> }
> ```
>
> You’ll need to write your own code to count the number of letters in the text. But someone more experienced than you may have already written a function to determine if a character is alphabetical. This is a good opportunity to use the [CS50 manual](https://manual.cs50.io/), a collection of explanations of common functions in the C Standard Library.
>
> You can integrate `count_letters` into the code you’ve already written, as follows.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <math.h>
> #include <stdio.h>
> #include <string.h>
>
> int count_letters(string text);
>
> int main(void)
> {
>     // Prompt the user for some text
>     string text = get_string("Text: ");
>
>     // Count the number of letters, words, and sentences in the text
>     int letters = count_letters(text);
>
>     // Compute the Coleman-Liau index
>
>     // Print the grade level
> }
>
> int count_letters(string text)
> {
>     // Return the number of letters in text
> }
> ```
>
> Next, write a function to count words.
>
> ```c
> int count_words(string text)
> {
>     // Return the number of words in text
> }
> ```
>
> For the purpose of this problem, we’ll consider any sequence of characters separated by a space to be a word (so a hyphenated word like “sister-in-law” should be considered one word, not three). You may assume that a sentence:
>
> * will contain at least one word;
> * will not start or end with a space; and
> * will not have multiple spaces in a row.
>
> Under those assumptions, you might be able to find a relationship between the number words and the number of spaces. You are, of course, welcome to attempt a solution that will tolerate multiple spaces between words or indeed, no words!
>
> You can now integrate `count_words` into your program as follows:
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <math.h>
> #include <stdio.h>
> #include <string.h>
>
> int count_letters(string text);
> int count_words(string text);
>
> int main(void)
> {
>     // Prompt the user for some text
>     string text = get_string("Text: ");
>
>     // Count the number of letters, words, and sentences in the text
>     int letters = count_letters(text);
>     int words = count_words(text);
>
>     // Compute the Coleman-Liau index
>
>     // Print the grade level
> }
>
> int count_letters(string text)
> {
>     // Return the number of letters in text
> }
>
> int count_words(string text)
> {
>     // Return the number of words in text
> }
> ```
>
> Finally, write a function to count sentences. You can consider any sequence of characters that ends with a `.` or a `!` or a `?` to be a sentence.
>
> ```c
> int count_sentences(string text)
> {
>     // Return the number of sentences in text
> }
> ```
>
> You can integrate `count_sentences` into your program as follows:
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <math.h>
> #include <stdio.h>
> #include <string.h>
>
> int count_letters(string text);
> int count_words(string text);
> int count_sentences(string text);
>
> int main(void)
> {
>     // Prompt the user for some text
>     string text = get_string("Text: ");
>
>     // Count the number of letters, words, and sentences in the text
>     int letters = count_letters(text);
>     int words = count_words(text);
>     int sentences = count_sentences(text);
>
>     // Compute the Coleman-Liau index
>
>     // Print the grade level
> }
>
> int count_letters(string text)
> {
>     // Return the number of letters in text
> }
>
> int count_words(string text)
> {
>     // Return the number of words in text
> }
>
> int count_sentences(string text)
> {
>     // Return the number of sentences in text
> }
> ```
>
> Finally, compute the Coleman-Liau index and print the resulting grade level.
>
> * Recall that the Coleman-Liau index is computed using `index = 0.0588 * L - 0.296 * S - 15.8`
> * `L` is the average number of letters per 100 words in the text: that is, the number of letters divided by the number of words, all multiplied by 100.
> * `S` is the average number of sentences per 100 words in the text: that is, the number of sentences divided by the number of words, all multiplied by 100.
> * You’ll want to round the result to the nearest whole number, so recall that `round` is declared in `math.h`, per [manual.cs50.io](https://manual.cs50.io/).
> * Recall that, when dividing values of type `int` in C, the result will also be an `int`, with any remainder (i.e., digits after the decimal point) discarded. Put another way, the result will be “truncated.” You might want to cast your one or more values to `float` before performing division when calculating `L` and `S`!
>
> If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output “Grade 16+” instead of outputting an exact index number. If the index number is less than 1, your program should output “Before Grade 1”.

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/AOVyZEh9zgE](https://www.youtube.com/embed/AOVyZEh9zgE)

<a id="how-to-test"></a>

#### How to Test

Try running your program on the following texts, to ensure you see the specified grade level. Be sure to copy only the text, no extra spaces.

* `One fish. Two fish. Red fish. Blue fish.` (Before Grade 1)
* `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grade 2)
* `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (Grade 3)
* `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` (Grade 5)
* `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (Grade 7)
* `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` (Grade 8)
* `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` (Grade 8)
* `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` (Grade 9)
* `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` (Grade 10)
* `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Grade 16+)

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/readability
```

<a id="style"></a>

##### Style

```
style50 readability.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/readability
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `readability`; files shown on the page: `readability.c`
- check50: `cs50/problems/2026/x/readability`
- style50: `readability.c`
- submit50: `cs50/problems/2026/x/readability`
- Page sections (order on source): Problem to Solve, Demo, Background, Advice, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/AOVyZEh9zgE
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم string iteration، counting characters، type casting / floats، math.h round، functions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write readability.c that asks for some text and estimates the US grade level needed to read it with the Coleman-Liau index (based on average letters and sentences per 100 words). It prints "Grade X" rounded to the nearest integer, "Grade 16+" for 16 or higher, or "Before Grade 1" below 1. Letters, words and sentences are counted by simple rules described on the page.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 2](README.md) (`pset-2`)
- **Prerequisites (generated):** [Week 2 — Lecture notes (Arrays)](../lecture.md) (`week-2-lecture`)
- **Related:**
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)
  - [Readability — Problem Set 6](../../week-06-python/psets/readability.md) (`pset-6-readability`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
شمردن حروف، کلمات و جمله‌ها در متن و به‌کارگیری یک فرمول؛ تمرین تجزیه‌ی متن.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. تعریف دقیق «حرف»، «کلمه» و «جمله» را از صورت مسئله استخراج کن و هرکدام را با یک تابع جدا بشمار.
2. فرمول به میانگین‌ها بر حسب ۱۰۰ کلمه نیاز دارد؛ مراقب نوع داده‌ها هنگام تقسیم باش.
3. نتیجه را چطور گرد می‌کنی و حالت‌های مرزی (کمتر از ۱ و ۱۶ به بالا) چطور چاپ می‌شوند؟

### اشتباه‌های رایج (مفهومی)
- تقسیم صحیح به جای اعشاری
- گرد نکردن نتیجه

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/readability` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/2/readability/ — retrieved 2026-10-18T05:11:21+03:30, sha256 `c533f737698f08eb…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
