---
id: practice-5-trie
type: practice
title: Trie — Practice
week: 5
parent: week-5
children: []
prerequisites:
- week-5-lecture
related:
- concept-pointers
- concept-structs
- concept-tries
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/trie/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:02+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- data-structures
- pointers
- practice
- trie
- tries
checksum: sha256:16ce3cf5e7cef7473bc4e1e2cba778078e9e283530bac491c7d89c4986accaf1
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Trie — Practice

## 1. Source metadata
- **Title:** Trie — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/trie/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:02+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/trie/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="trie"></a>

### Trie

<a id="learning-goals"></a>

#### Learning Goals

* Learn more about data structures
* Work with a trie

![puppies](https://cs50.harvard.edu/x/practice/trie/puppies.jpeg)

<a id="background"></a>

#### Background

Imagine you just rescued a dog and you’re deciding on a name. You found a file online with a list of about 150 of the most popular dog names! You are curious as to whether or not the names you are considering are on this list. Since trie’s are great for data lookups, we’ve given you some (almost!) complete code in `trie.c`. There is one function, `check`, which is not yet implemented. Your job is to complete this function.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/JukHED1VvaJLFHMJbIvLksgF1]

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/5/trie.zip` followed by Enter in order to download a zip called `trie.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip trie.zip` to create a folder called `trie`.
5. You no longer need the ZIP file, so you can execute `rm trie.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

Notice that the trie itself is implemented through the creative use of several `struct`s called `node`. Each `node` in a trie has an array of (potential) children, with size 26—one potential child for each letter of the alphabet! Adding words to this trie, notice that—for every letter in a word—we create a new `node` child whose parent is either the `root` node (for the first letter) or the previous letter (if not the first letter). On the very last letter, we set the `is_word` attribute of the child `node` to `true`. Now, checking if a word is in our trie is as easy as following each letter of that word through our trie. If we get to the final letter and see that `is_word` is true, well, that name is in our trie!

* Hints
  * You probably want to start by setting a `node` pointer, `cursor` to the `root` of the trie.
  * Iterate through every letter in the argument `word` and, as you do, determine the array index that corresponds to that letter.
  * You can use the index for a letter to check if `children[index]` is a `NULL` pointer, meaning the word does not exist in the trie.
  * If `children[index]` is in fact a node, you can reset `cursor` to this node and check for the next letter in its `children` nodes.
  * Remember that the lookup should be case-insensitive. For instance, `A` and `a` should correspond to 0, `B` and `b` corresponds to 1, etc.

<a id="thought-question"></a>

#### Thought Question

* When might you want to use a trie as a data structure? When might you *not*?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave per the examples below.

```
trie/ $ ./trie dog_names.txt
Check word: Molly
Found!
```

```
trie/ $ ./trie dog_names.txt
Check word: Lucy
Found!
```

```
trie/ $ ./trie dog_names.txt
Check word: Prudence
Not Found.
```

No `check50` for this one!

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 trie.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is a practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/5/trie.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `trie/dog_names.txt` | 946 | [yes](trie-distribution/files/trie/dog_names.txt) |
| `trie/trie.c` | 2920 | [yes](trie-distribution/files/trie/trie.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `trie`; files shown on the page: `trie.c`
- check50: No check50 (stated)
- style50: `trie.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم tries، data structures، pointers.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Implement the check function for a trie of about 150 popular dog names, to report whether a given name is in the list.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Week 5 — Data Structures](../week.md) (`week-5`)
- **Prerequisites (generated):** [Week 5 — Lecture notes (Data Structures)](../lecture.md) (`week-5-lecture`)
- **Related:**
  - [Pointers](../../../concepts/pointers.md) (`concept-pointers`)
  - [Structs and Custom Types (typedef)](../../../concepts/structs.md) (`concept-structs`)
  - [Tries](../../../concepts/tries.md) (`concept-tries`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین ساختار داده‌ی trie.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. هر گره برای هر حرف ممکن چه چیزی نگه می‌دارد؟
2. یک کلمه‌ی کوتاه را روی کاغذ وارد trie کن و مسیر را دنبال کن.

### اشتباه‌های رایج (مفهومی)
- نشت حافظه هنگام آزادسازی

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای (در صفحه ذکر نشده) و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این تمرین اختیاری است و قابل ارسال نیست؛ تشویق به حل مستقل بدون فشار نمره.

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/practice/trie/ — retrieved 2026-10-18T05:11:02+03:30, sha256 `16ce3cf5e7cef747…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
