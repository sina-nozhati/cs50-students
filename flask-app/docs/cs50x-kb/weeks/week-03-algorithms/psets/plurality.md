---
id: pset-3-plurality
type: pset
title: Plurality — Problem Set 3
week: 3
parent: pset-3
children: []
prerequisites:
- week-3-lecture
related:
- concept-arrays
- concept-functions
- concept-linear-search
- concept-structs
source_urls:
- https://cs50.harvard.edu/x/psets/3/plurality/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:25+03:30'
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
- functions
- linear-search
- plurality
- pset
- strcmp
- structs
checksum: sha256:0aaae47161afb05d6e69b37ad7494082375835519d2d5eef527c641fb0bd1e04
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Plurality — Problem Set 3

## 1. Source metadata
- **Title:** Plurality — Problem Set 3
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/3/plurality/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:25+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/3/plurality/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="plurality"></a>

### Plurality

<a id="problem-to-solve"></a>

#### Problem to Solve

Elections come in all shapes and sizes. In the UK, the [Prime Minister](https://www.parliament.uk/education/about-your-parliament/general-elections/) is officially appointed by the monarch, who generally chooses the leader of the political party that wins the most seats in the House of Commons. The United States uses a multi-step [Electoral College](https://www.archives.gov/federal-register/electoral-college/about.html) process where citizens vote on how each state should allocate Electors who then elect the President.

Perhaps the simplest way to hold an election, though, is via a method commonly known as the “plurality vote” (also known as “first-past-the-post” or “winner take all”). In the plurality vote, every voter gets to vote for one candidate. At the end of the election, whichever candidate has the greatest number of votes is declared the winner of the election.

For this problem, you’ll implement a program that runs a plurality election, per the below.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/o2EXEqiz7iqfDB31wYxBOWjs8]

<a id="distribution-code"></a>

#### Distribution Code

For this problem, you’ll extend the functionality of “distribution code” provided to you by CS50’s staff.

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
> wget https://cdn.cs50.net/2026/x/psets/3/plurality.zip
> ```
>
> in order to download a ZIP called `plurality.zip` into your codespace.
>
> Then execute
>
> ```
> unzip plurality.zip
> ```
>
> to create a folder called `plurality`. You no longer need the ZIP file, so you can execute
>
> ```
> rm plurality.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd plurality
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> plurality/ $
> ```
>
> If all was successful, you should execute
>
> ```
> ls
> ```
>
> and see a file named `plurality.c`. Executing `code plurality.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

> **Understand the code in plurality.c** *(collapsible block on the source page)*
>
> Whenever you’ll extend the functionality of existing code, it’s best to be sure you first understand it in its present state.
>
> Look first at the top of the file. The line `#define MAX 9` is some syntax used here to mean that `MAX` is a constant (equal to `9`) that can be used throughout the program. Here, it represents the maximum number of candidates an election can have.
>
> ```c
> // Max number of candidates
> #define MAX 9
> ```
>
> Notice that `plurality.c` then uses this constant to define a global array—that is, an array that any function can access.
>
> ```c
> // Array of candidates
> candidate candidates[MAX];
> ```
>
> But what, in this case, is a `candidate`? In `plurality.c`, a `candidate` is a `struct`. Each `candidate` has two fields: a `string` called `name` representing the candidate’s name, and an `int` called `votes` representing the number of votes the candidate has.
>
> ```c
> // Candidates have name and vote count
> typedef struct
> {
>     string name;
>     int votes;
> }
> candidate;
> ```
>
> Now, take a look at the `main` function itself. See if you can find where the program sets a global variable `candidate_count` representing the number of candidates in the election.
>
> ```c
> // Number of candidates
> int candidate_count;
> ```
>
> What about where it copies command-line arguments into the array `candidates`?
>
> ```c
> // Populate array of candidates
> candidate_count = argc - 1;
> if (candidate_count > MAX)
> {
>     printf("Maximum number of candidates is %i\n", MAX);
>     return 2;
> }
> for (int i = 0; i < candidate_count; i++)
> {
>     candidates[i].name = argv[i + 1];
>     candidates[i].votes = 0;
> }
> ```
>
> And where it asks the user to type in the number of voters?
>
> ```c
> int voter_count = get_int("Number of voters: ");
> ```
>
> Then, the program lets every voter type in a vote, calling the `vote` function on each candidate voted for. Finally, `main` makes a call to the `print_winner` function to print out the winner (or winners) of the election. We’ll leave it to you to identify the code that implements this functionality.
>
> If you look further down in the file, though, you’ll notice that the `vote` and `print_winner` functions have been left blank.
>
> ```c
> // Update vote totals given a new vote
> bool vote(string name)
> {
>     // TODO
>     return false;
> }
>
> // Print the winner (or winners) of the election
> void print_winner(void)
> {
>     // TODO
>     return;
> }
> ```
>
> This part is up to you to complete! **You should not modify anything else in `plurality.c` other than the implementations of the `vote` and `print_winner` functions (and the inclusion of additional header files, if you’d like).**

<a id="hints"></a>

#### Hints

Click the below toggles to read some advice!

> **Complete the vote function** *(collapsible block on the source page)*
>
> Next, complete the `vote` function.
>
> * Consider that `vote`’s signature, `bool vote(string name)`, shows it takes a single argument, a `string` called `name`, representing the name of the candidate who was voted for.
> * `vote` should return a `bool`, where `true` indicates a vote was successfully cast and `false` indicates it was not.
>
> One way to approach this problem is to do the following:
>
> 1. Iterate over each candidate
>    1. Check if candidate’s name matches the input, `name`
>       1. If yes, increment that candidate’s votes and return `true`
>       2. If no, continue checking
> 2. If no matches after checking each candidate, return `false`
>
> Let’s write some pseudocode to remind you to do just that:
>
> ```c
> // Update vote totals given a new vote
> bool vote(string name)
> {
>     // Iterate over each candidate
>         // Check if candidate's name matches given name
>             // If yes, increment candidate's votes and return true
>
>     // If no match, return false
> }
> ```
>
> We’ll leave the implementation in code, though, up to you!

> **Complete the print_winner function** *(collapsible block on the source page)*
>
> Finally, complete the `print_winner` function.
>
> * The function should print out the name of the candidate who received the most votes in the election, and then print a newline.
> * The election could end in a tie if multiple candidates each have the maximum number of votes. In that case, you should output the names of each of the winning candidates, each on a separate line.
>
> You might think a sorting algorithm would best solve this problem: imagine sorting candidates by their vote totals and printing the top candidate (or candidates). Recall, though, that sorting can be expensive: even Merge Sort, one of the fastest sorting algorithms, runs in \(O(N \space log(N))\).
>
> Consider that you need only two pieces of information to solve this problem:
>
> 1. The maximum number of votes
> 2. The candidate (or candidates) with that number of votes
>
> As such, a good solution might require only two searches. Write some pseudocode to remind yourself to do just that:
>
> ```c
> // Print the winner (or winners) of the election
> void print_winner(void)
> {
>     // Find the maximum number of votes
>
>     // Print the candidate (or candidates) with maximum votes
>
> }
> ```
>
> We’ll leave the code, though, up to you!

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/ftOapzDjEb8](https://www.youtube.com/embed/ftOapzDjEb8)

<a id="how-to-test"></a>

#### How to Test

Be sure to test your code to make sure it handles…

* An election with any number of candidate (up to the `MAX` of `9`)
* Voting for a candidate by name
* Invalid votes for candidates who are not on the ballot
* Printing the winner of the election if there is only one
* Printing the winner of the election if there are multiple winners

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/plurality
```

<a id="style"></a>

##### Style

```
style50 plurality.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/plurality
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/3/plurality.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `plurality/plurality.c` | 1421 | [yes](plurality-distribution/files/plurality/plurality.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `plurality`; files shown on the page: `plurality.c`
- check50: `cs50/problems/2026/x/plurality`
- style50: `plurality.c`
- submit50: `cs50/problems/2026/x/plurality`
- Page sections (order on source): Problem to Solve, Demo, Distribution Code, Hints, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/ftOapzDjEb8
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم structs، arrays، linear search، strcmp، functions.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete the distribution code in plurality.c for a first-past-the-post election. You implement vote, which records a ballot for a named candidate (returning false for an invalid name), and print_winner, which prints the candidate(s) with the most votes, including ties. Candidates are given as command-line arguments.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 3](README.md) (`pset-3`)
- **Prerequisites (generated):** [Week 3 — Lecture notes (Algorithms)](../lecture.md) (`week-3-lecture`)
- **Related:**
  - [Arrays](../../../concepts/arrays.md) (`concept-arrays`)
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [Linear Search](../../../concepts/linear-search.md) (`concept-linear-search`)
  - [Structs and Custom Types (typedef)](../../../concepts/structs.md) (`concept-structs`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
کار با آرایه‌ای از struct و پیاده‌سازی توابع مشخص‌شده در کد توزیعی.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. کد توزیعی را کامل بخوان و ببین هر تابع چه چیزی باید برگرداند یا تغییر دهد.
2. برای ثبت رأی، نام را با نامزدها مقایسه کن؛ برای مقایسه‌ی رشته‌ها در C چه تابعی وجود دارد؟
3. برای پیدا کردن برنده، فکر کن چند بار باید آرایه را پیمایش کنی.

### اشتباه‌های رایج (مفهومی)
- تغییر دادن main یا امضای توابع
- چاپ نکردن همه‌ی برنده‌ها در حالت تساوی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/plurality` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/3/plurality/ — retrieved 2026-10-18T05:11:25+03:30, sha256 `0aaae47161afb05d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
