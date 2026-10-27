---
id: pset-2-scrabble
type: pset
title: Scrabble — Problem Set 2
week: 2
parent: pset-2
children: []
prerequisites:
- week-2-lecture
related:
- concept-arrays
- concept-data-types
- concept-functions
- concept-strings
source_urls:
- https://cs50.harvard.edu/x/psets/2/scrabble/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:20+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- arrays
- ascii-arithmetic
- ctypeh
- functions
- pset
- scrabble
- strings-as-char-arrays
checksum: sha256:a2b576c8f05b76d1dab1d04ddc43f3544b522eca7f3a82463bcf147ee7c6a338
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Scrabble — Problem Set 2

## 1. Source metadata
- **Title:** Scrabble — Problem Set 2
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/2/scrabble/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:20+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/2/scrabble/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="scrabble"></a>

### Scrabble

![Scrabble Board](https://cs50.harvard.edu/x/psets/2/scrabble/scrabble.png)

<a id="problem-to-solve"></a>

#### Problem to Solve

In the game of [Scrabble](https://en.wikipedia.org/wiki/Scrabble), players create words to score points, and the number of points is the sum of the point values of each letter in the word.

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3 | 2 | 1 | 4 | 2 | 4 | 1 | 8 | 5 | 1 | 3 | 1 | 1 | 3 | 10 | 1 | 1 | 1 | 1 | 4 | 4 | 8 | 4 | 10 |

For example, if we wanted to score the word “CODE”, we would note that the ‘C’ is worth 3 points, the ‘O’ is worth 1 point, the ‘D’ is worth 2 points, and the ‘E’ is worth 1 point. Summing these, we get that “CODE” is worth 7 points.

In a file called `scrabble.c` in a folder called `scrabble`, implement a program in C that determines the winner of a short Scrabble-like game. Your program should prompt for input twice: once for “Player 1” to input their word and once for “Player 2” to input their word. Then, depending on which player scores the most points, your program should either print “Player 1 wins!”, “Player 2 wins!”, or “Tie!” (in the event the two players score equal points).

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/74B4kq3ftleKe6AdN0NxFV8CN]

<a id="advice-and-hints"></a>

#### Advice and Hints

> **Write some code that you know will compile** *(collapsible block on the source page)*
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
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
> 1. Prompt for the user for two words
> 2. Compute the score of each word
> 3. Print the winner
>
> Let’s write some pseudcode as comments to remind you to do just that:
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <stdio.h>
> #include <string.h>
>
> int main(void)
> {
>     // Prompt the user for two words
>
>     // Compute the score of each word
>
>     // Print the winner
> }
> ```

Some problems in problem sets, like this one, might contain spoilers (like the next one) that ultimately walk you through the entire solution. While you are permitted to use this code, we really do strongly encourage you to try things out yourself first! The other problems in the problem set won’t have this sort of walkthrough, and typically the problem that contains the “full spoiler” is a warm-up version of the bigger problem you’ll later need to tackle.

> **Convert the pseudocode to code** *(collapsible block on the source page)*
>
> First, consider how you might prompt the user for two words. Recall that `get_string`, a function in the CS50 library, can prompt the user for a string.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <stdio.h>
> #include <string.h>
>
> int main(void)
> {
>     // Prompt the user for two words
>     string word1 = get_string("Player 1: ");
>     string word2 = get_string("Player 2: ");
>
>     // Compute the score of each word
>
>     // Print the winner
> }
> ```
>
> Next consider how to compute the score of each word. Since the same scoring algorithm applies to both words, you have a good opportunity for *abstraction*. Here we’ll define a function called `compute_score` that takes a string, called `word`, as input, and then returns `word`’s score as an `int`.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <stdio.h>
> #include <string.h>
>
> int compute_score(string word);
>
> int main(void)
> {
>     // Prompt the user for two words
>     string word1 = get_string("Player 1: ");
>     string word2 = get_string("Player 2: ");
>
>     // Compute the score of each word
>     int score1 = compute_score(word1);
>     int score2 = compute_score(word2);
>
>     // Print the winner   
> }
>
> int compute_score(string word)
> {
>     // Compute and return score for word
> }
> ```
>
> Now turn to implementing `compute_score`. To compute the score of a word, you need to know the point value of each letter in the word. You can associate letters and their point values with an *array*. Imagine an array of 26 `int`s, called `POINTS`, in which the first number is the point value for ‘A’, the second number is the point value for ‘B’, and so on. By declaring and initializing such an array outside of any single function, you can ensure this array is accessible to any function, including `compute_score`.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <stdio.h>
> #include <string.h>
>
> // Points assigned to each letter of the alphabet
> int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
>
> int compute_score(string word);
>
> int main(void)
> {
>     // Prompt the user for two words
>     string word1 = get_string("Player 1: ");
>     string word2 = get_string("Player 2: ");
>
>     // Compute the score of each word
>     int score1 = compute_score(word1);
>     int score2 = compute_score(word2);
>
>     // Print the winner   
> }
>
> int compute_score(string word)
> {
>     // Compute and return score for word
> }
> ```
>
> To implement `compute_score`, first try to find the point value of a single letter in `word`.
>
> * Recall that to find the character at the nth index of a string, `s`, you can write `s[n]`. So `word[0]`, for example, will give you the first character of `word`.
> * Now, recall that computers represent characters using ASCII, a standard that represents each character as a number.
> * Recall too that the 0th index of `POINTS`, `POINTS[0]`, gives you the point value of ‘A’. Think about how you could transform the numeric representation of ‘A’ into the index of its point value. Now, what about ‘a’? You’ll need to apply different transformations to upper- and lower-case letters, so you may find the functions [`isupper`](https://manual.cs50.io/3/isupper) and [`islower`](https://manual.cs50.io/3/islower) to be helpful to you.
> * Keep in mind that characters that are *not* letters should be given zero points. For example, `!` is worth 0 points.
>
> If you can properly calculate the value of *one* character in `word`, odds are you can use a loop to sum the points for the rest of the characters. Once you’ve tried the above on your own, consider this (quite revealing!) hint below.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <stdio.h>
> #include <string.h>
>
> // Points assigned to each letter of the alphabet
> int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
>
> int compute_score(string word);
>
> int main(void)
> {
>     // Prompt the user for two words
>     string word1 = get_string("Player 1: ");
>     string word2 = get_string("Player 2: ");
>
>     // Compute the score of each word
>     int score1 = compute_score(word1);
>     int score2 = compute_score(word2);
>
>     // Print the winner   
> }
>
> int compute_score(string word)
> {
>     // Keep track of score
>     int score = 0;
>
>     // Compute score for each character
>     for (int i = 0, len = strlen(word); i < len; i++)
>     {
>         if (isupper(word[i]))
>         {
>             score += POINTS[word[i] - 'A'];
>         }
>         else if (islower(word[i]))
>         {
>             score += POINTS[word[i] - 'a'];
>         }
>     }
>
>     return score;
> }
> ```
>
> Finally, finish your pseudocode’s last step: printing the winner. Recall that an `if` statement can be used to check if a condition is true, and that the additional usage of `else if` or `else` can check for other (exclusive) conditions.
>
> ```c
> if (/* Player 1 wins */)
> {
>     // ...
> }
> else if (/* Player 2 wins */)
> {
>     // ...
> }
> else
> {
>     // ...
> }
> ```
>
> And once you’ve tried the above, feel free to take a peek at the hint (or, rather, complete solution!) below.
>
> ```c
> #include <ctype.h>
> #include <cs50.h>
> #include <stdio.h>
> #include <string.h>
>
> // Points assigned to each letter of the alphabet
> int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
>
> int compute_score(string word);
>
> int main(void)
> {
>     // Prompt the user for two words
>     string word1 = get_string("Player 1: ");
>     string word2 = get_string("Player 2: ");
>
>     // Compute the score of each word
>     int score1 = compute_score(word1);
>     int score2 = compute_score(word2);
>
>     // Print the winner   
>     if (score1 > score2)
>     {
>         printf("Player 1 wins!\n");
>     }
>     else if (score1 < score2)
>     {
>         printf("Player 2 wins!\n");
>     }
>     else
>     {
>         printf("Tie!\n");
>     }
> }
>
> int compute_score(string word)
> {
>     // Keep track of score
>     int score = 0;
>
>     // Compute score for each character
>     for (int i = 0, len = strlen(word); i < len; i++)
>     {
>         if (isupper(word[i]))
>         {
>             score += POINTS[word[i] - 'A'];
>         }
>         else if (islower(word[i]))
>         {
>             score += POINTS[word[i] - 'a'];
>         }
>     }
>
>     return score;
> }
> ```

<a id="how-to-test"></a>

#### How to Test

Your program should behave per the examples below.

```
$ ./scrabble
Player 1: Question?
Player 2: Question!
Tie!
```

```
$ ./scrabble
Player 1: red
Player 2: wheelbarrow
Player 2 wins!
```

```
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

```
$ ./scrabble
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/scrabble
```

<a id="style"></a>

##### Style

```
style50 scrabble.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/scrabble
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `scrabble`; files shown on the page: `scrabble.c`
- check50: `cs50/problems/2026/x/scrabble`
- style50: `scrabble.c`
- submit50: `cs50/problems/2026/x/scrabble`
- Page sections (order on source): Problem to Solve, Demo, Advice and Hints, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم arrays، strings as char arrays، ASCII arithmetic، ctype.h، functions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write scrabble.c that asks two players for a word each and scores them with Scrabble letter values, ignoring case and non-letters. It prints "Player 1 wins!", "Player 2 wins!" or "Tie!". The page suggests storing the point values in an array and writing a compute_score function.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 2](README.md) (`pset-2`)
- **Prerequisites (generated):** [Week 2 — Lecture notes (Arrays)](../lecture.md) (`week-2-lecture`)
- **Related:**
  - [Arrays](../../../concepts/arrays.md) (`concept-arrays`)
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
آشنایی با آرایه‌ها به‌عنوان جدول جستجو (lookup) و کار با کاراکترها.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. امتیاز هر حرف را در یک ساختار داده نگه دار که بتوانی با موقعیت حرف به آن برسی.
2. کاراکترها در واقع عدد هستند؛ چطور می‌توانی از این برای پیدا کردن اندیس استفاده کنی؟
3. با حروف بزرگ، کوچک و غیرحرفی چه باید کرد؟ صورت مسئله را دوباره بخوان.

### اشتباه‌های رایج (مفهومی)
- امتیاز دادن به کاراکترهای غیرحرفی
- حساسیت به بزرگی و کوچکی حروف

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/scrabble` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/2/scrabble/ — retrieved 2026-10-18T05:11:20+03:30, sha256 `a2b576c8f05b76d1…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
