---
id: practice-3-snackbar
type: practice
title: Snackbar — Practice
week: 3
parent: week-3
children: []
prerequisites:
- week-3-lecture
related:
- concept-linear-search
- concept-structs
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/snackbar/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:59+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- C
tags:
- linear-search
- practice
- snackbar
- strcasecmp
- structs
checksum: sha256:a26aac48d4714e57dd98dff13984ec770eb9dd5600a464182b0a739cd49783d2
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Snackbar — Practice

## 1. Source metadata
- **Title:** Snackbar — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/snackbar/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:59+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/snackbar/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="snackbar"></a>

### Snackbar

<a id="learning-goals"></a>

#### Learning Goals

* Practice using `struct`s
* Write a linear search algorithm

![Beach Image](https://cs50.harvard.edu/x/practice/snackbar/beach-g1e2b206d7_1280.jpg)

<a id="background"></a>

#### Background

Imagine you’re at the beach and want to order a number of items from the snack bar. You have a limited amount of cash on you, and you want to get a total cost for your items before ordering. In `snackbar.c` you will complete two functions. First is `add_items` which will add at least the first 4 items on the Beach Burger Shack menu. Then you will complete `get_cost` which will implement a linear search algorithm to search for each item you choose, and return the corresponding price.

* Hints
  * You can hard code the menu items and prices in the `add_items` function.
  * There is a function in [`strings.h`](https://manual.cs50.io/#strings.h) that may come in handy here.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/sNDasPt6uPRp8mWF12ZePqNn1]

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/3/snackbar.zip` followed by Enter in order to download a zip called `snackbar.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip snackbar.zip` to create a folder called `snackbar`.
5. You no longer need the ZIP file, so you can execute `rm snackbar.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

The `main` function is already complete. After calling `add_items` to initialize the `menu` array, it will print out the menu items and their prices, prompting you to keep selecting items until you press enter without typing anything in. You are to complete two functions, `add_items`, which adds at least the first four menu items, and `get_cost` to return the cost of each item. When you are creating a linear search algorithm in `get_cost`, do make sure that it is case insentive.

<a id="thought-question"></a>

#### Thought Question

* Why is an array of `struct`s a better solution here than multiple arrays?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave as follows:

```
snackbar/ $ ./snackbar

Welcome to Beach Burger Shack!
Choose from the following menu to order. Press enter when done.

Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: burger
Enter a food item: fries
Enter a food item: soda
Enter a food item: 

Your total cost is: $16.50
```

```
snackbar/ $ ./snackbar

Welcome to Beach Burger Shack!
Choose from the following menu to order. Press enter when done.

Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: cold brew
Enter a food item: hot dog
Enter a food item: 

Your total cost is: $8.00
```

*Note that the menu should only print out the items that you saved in the `menu` array.*

No `check50` for this one!

To evaluate that the style of your code, type in the following at the `$` prompt.

```
style50 snackbar.c
```

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is an optional practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/3/snackbar.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `snackbar/beach-g1e2b206d7_1280.jpg` | 193354 | no — binary/media/data file (inventory only) |
| `snackbar/README.md` | 2941 | [yes](snackbar-distribution/files/snackbar/README.md) |
| `snackbar/snackbar.c` | 1557 | [yes](snackbar-distribution/files/snackbar/snackbar.c) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): C
- Folder: `snackbar`; files shown on the page: `snackbar.c`
- check50: No check50 (stated)
- style50: `snackbar.c`
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Demo, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم structs، linear search، strcasecmp.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete add_items to fill a snack-bar menu of structs and get_cost, a linear search returning an item's price, to total an order.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Week 3 — Algorithms](../week.md) (`week-3`)
- **Prerequisites (generated):** [Week 3 — Lecture notes (Algorithms)](../lecture.md) (`week-3-lecture`)
- **Related:**
  - [Linear Search](../../../concepts/linear-search.md) (`concept-linear-search`)
  - [Structs and Custom Types (typedef)](../../../concepts/structs.md) (`concept-structs`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین struct و جستجوی خطی در آرایه.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. منو را چطور در آرایه‌ای از struct ذخیره می‌کنی؟
2. مقایسه‌ی نام‌ها باید به بزرگی و کوچکی حروف حساس باشد یا نه؟

### اشتباه‌های رایج (مفهومی)
- (none)

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
- https://cs50.harvard.edu/x/practice/snackbar/ — retrieved 2026-10-18T05:10:59+03:30, sha256 `a26aac48d4714e57…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
