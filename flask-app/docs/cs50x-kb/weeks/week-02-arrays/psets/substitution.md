---
id: pset-2-substitution
type: pset
title: Substitution (more comfortable) — Problem Set 2
week: 2
parent: pset-2
children: []
prerequisites:
- week-2-lecture
related:
- concept-arrays
- concept-command-line-arguments
- concept-data-types
- pset-2-caesar
source_urls:
- https://cs50.harvard.edu/x/psets/2/substitution/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:23+03:30'
review_status: verified-against-source
difficulty: more comfortable
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- arrays
- command-line-arguments
- cryptography
- ctypeh
- input-validation
- pset
- substitution
checksum: sha256:102418769aa961eb1bdcf5cf5d19edf26db188cf01440245646146d6869a924f
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Substitution (more comfortable) — Problem Set 2

## 1. Source metadata
- **Title:** Substitution (more comfortable) — Problem Set 2
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/2/substitution/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:23+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/2/substitution/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="substitution"></a>

### Substitution

<a id="problem-to-solve"></a>

#### Problem to Solve

In a substitution cipher, we “encrypt” (i.e., conceal in a reversible way) a message by replacing every letter with another letter. To do so, we use a *key*: in this case, a mapping of each of the letters of the alphabet to the letter it should correspond to when we encrypt it. To “decrypt” the message, the receiver of the message would need to know the key, so that they can reverse the process: translating the encrypt text (generally called *ciphertext*) back into the original message (generally called *plaintext*).

A key, for example, might be the string `NQXPOMAFTRHLZGECYJIUWSKDVB`. This 26-character key means that `A` (the first letter of the alphabet) should be converted into `N` (the first character of the key), `B` (the second letter of the alphabet) should be converted into `Q` (the second character of the key), and so forth.

A message like `HELLO`, then, would be encrypted as `FOLLE`, replacing each of the letters according to the mapping determined by the key.

In a file called `substitution.c` in a folder called `substitution`, create a program that enables you to encrypt messages using a substitution cipher. At the time the user executes the program, they should decide, by providing a command-line argument, on what the key should be in the secret message they’ll provide at runtime.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY]

<a id="specification"></a>

#### Specification

Design and implement a program, `substitution`, that encrypts messages using a substitution cipher.

* Implement your program in a file called `substitution.c` in a directory called `substitution`.
* Your program must accept a single command-line argument, the key to use for the substitution. The key itself should be case-insensitive, so whether any character in the key is uppercase or lowercase should not affect the behavior of your program.
* If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` (which tends to signify an error) immediately.
* If the key is invalid (as by not containing 26 characters, containing any character that is not an alphabetic character, or not containing each letter exactly once), your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` immediately.
* Your program must output `plaintext:` (without a newline) and then prompt the user for a `string` of plaintext (using `get_string`).
* Your program must output `ciphertext:` (without a newline) followed by the plaintext’s corresponding ciphertext, with each alphabetical character in the plaintext substituted for the corresponding character in the ciphertext; non-alphabetical characters should be outputted unchanged.
* Your program must preserve case: capitalized letters must remain capitalized letters; lowercase letters must remain lowercase letters.
* After outputting ciphertext, you should print a newline. Your program should then exit by returning `0` from `main`.

You might find one or more functions declared in `ctype.h` to be helpful, per [manual.cs50.io](https://manual.cs50.io/).

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/cXAoZAsgxJ4](https://www.youtube.com/embed/cXAoZAsgxJ4)

<a id="how-to-test"></a>

#### How to Test

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/substitution
```

> **How to Use debug50** *(collapsible block on the source page)*
>
> Looking to run `debug50`? You can do so as follows, after compiling your code successfully with `make`,
>
> ```
> debug50 ./substitution KEY
> ```
>
> wherein `KEY` is the key you give as a command-line argument to your program. Note that running
>
> ```
> debug50 ./substitution
> ```
>
> will (ideally!) cause your program end by prompting the user for a key.

<a id="style"></a>

##### Style

```
style50 substitution.c
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/substitution
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): more comfortable
- Choice group: pset2-choice1 — “Substitution , if feeling more comfortable”
- Language (derived from files/commands on the page): C
- Folder: `substitution`; files shown on the page: `substitution.c`
- check50: `cs50/problems/2026/x/substitution`
- style50: `substitution.c`
- submit50: `cs50/problems/2026/x/substitution`
- Page sections (order on source): Problem to Solve, Demo, Specification, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/cXAoZAsgxJ4
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty / comfort level as stated: more comfortable

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم command-line arguments، cryptography، arrays، input validation، ctype.h.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write substitution.c that encrypts text with a substitution cipher, where a 26-letter key given on the command line maps each letter of the alphabet to another. The key must be validated (exactly 26 alphabetic characters, each letter once) or the program exits with an error. Case must be preserved and non-letters left unchanged.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Problem Set 2](README.md) (`pset-2`)
- **Prerequisites (generated):** [Week 2 — Lecture notes (Arrays)](../lecture.md) (`week-2-lecture`)
- **Related:**
  - [Arrays](../../../concepts/arrays.md) (`concept-arrays`)
  - [Command-Line Arguments (argc, argv)](../../../concepts/command-line-arguments.md) (`concept-command-line-arguments`)
  - [Data Types](../../../concepts/data-types.md) (`concept-data-types`)
  - [Caesar (less comfortable) — Problem Set 2](caesar.md) (`pset-2-caesar`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
اعتبارسنجی دقیق ورودی و نگاشت حروف؛ نسخه‌ی چالشی‌تر Caesar.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. همه‌ی شرط‌های اعتبار کلید را از صورت مسئله فهرست کن و هرکدام را جدا بررسی کن.
2. چطور می‌توان تکراری بودن حروف در کلید را تشخیص داد؟
3. حفظ بزرگی/کوچکی حرف اصلی در متن رمز را فراموش نکن.

### اشتباه‌های رایج (مفهومی)
- نپذیرفتن کلید با حروف ترکیبی بزرگ و کوچک
- پذیرفتن کلید با حروف تکراری

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/substitution` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/2/substitution/ — retrieved 2026-10-18T05:11:23+03:30, sha256 `102418769aa961eb…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
