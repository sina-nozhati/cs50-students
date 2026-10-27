---
id: pset-6-dna
type: pset
title: DNA — Problem Set 6
week: 6
parent: pset-6
children: []
prerequisites:
- week-6-lecture
related:
- concept-command-line-arguments
- concept-dictionaries
- concept-file-io
- concept-python-basics
- concept-strings
source_urls:
- https://cs50.harvard.edu/x/psets/6/dna/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:41+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python
tags:
- command-line-arguments
- dicts-and-lists
- dna
- file-i-o
- pset
- python-csv-module
- string-searching
checksum: sha256:0d15f67a07cab491e22e2a0935d5882f09451f03597dc5a320fc77b46a72e463
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# DNA — Problem Set 6

## 1. Source metadata
- **Title:** DNA — Problem Set 6
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/6/dna/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:41+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/6/dna/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="dna"></a>

### DNA

<a id="problem-to-solve"></a>

#### Problem to Solve

DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work? Given a sequence of DNA, how can forensic investigators identify to whom it belongs?

In a file called `dna.py` in a folder called `dna`, implement a program that identifies to whom a sequence of DNA belongs.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/5onE9BNq1zhL2D72gfu9IbdsD]

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
> wget https://cdn.cs50.net/2026/x/psets/6/dna.zip
> ```
>
> in order to download a ZIP called `dna.zip` into your codespace.
>
> Then execute
>
> ```
> unzip dna.zip
> ```
>
> to create a folder called `dna`. You no longer need the ZIP file, so you can execute
>
> ```
> rm dna.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd dna
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> dna/ $
> ```
>
> Execute `ls` by itself, and you should see a few files and folders:
>
> ```
> databases/ dna.py sequences/
> ```
>
> If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

<a id="background"></a>

#### Background

DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence (i.e., genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for example, Alice has the STR `AGAT` repeated four times in her DNA, while Bob has the same STR repeated five times.

![Sample STRs](https://cs50.harvard.edu/x/psets/6/dna/strs.png)

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, the FBI’s [DNA database](https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet), uses 20 different STRs as part of its DNA profiling process.

What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

The data in the above file would suggest that Alice has the sequence `AGAT` repeated 28 times consecutively somewhere in her DNA, the sequence `AATG` repeated 42 times, and `TATC` repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated `AGAT`s and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of `AATG` is 22 repeats long, and the longest sequence of `TATC` is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.

In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we’ll ignore that detail for this problem.

Your task is to write a program that will take a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.

<a id="specification"></a>

#### Specification

* The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
  * If your program is executed with the incorrect number of command-line arguments, your program should print an error message of your choice (with `print`). If the correct number of arguments are provided, you may assume that the first argument is indeed the filename of a valid CSV file and that the second argument is the filename of a valid text file.
* Your program should open the CSV file and read its contents into memory.
  * You may assume that the first row of the CSV file will be the column names. The first column will be the word `name` and the remaining columns will be the STR sequences themselves.
* Your program should open the DNA sequence and read its contents into memory.
* For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify. Notice that we’ve defined a helper function for you, `longest_match`, which will do just that!
* If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
  * You may assume that the STR counts will not match more than one individual.
  * If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print `No match`.

<a id="hints"></a>

#### Hints

* You may find Python’s [`csv`](https://docs.python.org/3/library/csv.html) module helpful for reading CSV files into memory. Of particular help might be [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).
  * For instance, if a file like `foo.csv` has a header row, wherein each string is the name of some field, here’s how you might print those `fieldnames` as a `list`:

    ```py
    import csv

    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)
    ```
  * And here’s how you read all of the (other) rows from a CSV into a `list`, wherein each element is a `dict` that represents that row:

    ```py
    import csv

    rows = []
    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    ```
* The [`open`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) and [`read`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) functions might also prove useful for reading text files into memory.
* Consider what data structures might be helpful for keeping track of information in your program. A [`list`](https://docs.python.org/3/tutorial/introduction.html#lists) or a [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) may prove useful.
* Remember we’ve defined a function (`longest_match`) that, given both a DNA sequence and an STR as inputs, returns the maximum number of times that the STR repeats. You can then use that function in other parts of your program!

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/j84b_EgntcQ](https://www.youtube.com/embed/j84b_EgntcQ)

<a id="how-to-test"></a>

#### How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

* Run your program as `python dna.py databases/small.csv sequences/1.txt`. Your program should output `Bob`.
* Run your program as `python dna.py databases/small.csv sequences/2.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/small.csv sequences/3.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/small.csv sequences/4.txt`. Your program should output `Alice`.
* Run your program as `python dna.py databases/large.csv sequences/5.txt`. Your program should output `Lavender`.
* Run your program as `python dna.py databases/large.csv sequences/6.txt`. Your program should output `Luna`.
* Run your program as `python dna.py databases/large.csv sequences/7.txt`. Your program should output `Ron`.
* Run your program as `python dna.py databases/large.csv sequences/8.txt`. Your program should output `Ginny`.
* Run your program as `python dna.py databases/large.csv sequences/9.txt`. Your program should output `Draco`.
* Run your program as `python dna.py databases/large.csv sequences/10.txt`. Your program should output `Albus`.
* Run your program as `python dna.py databases/large.csv sequences/11.txt`. Your program should output `Hermione`.
* Run your program as `python dna.py databases/large.csv sequences/12.txt`. Your program should output `Lily`.
* Run your program as `python dna.py databases/large.csv sequences/13.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/large.csv sequences/14.txt`. Your program should output `Severus`.
* Run your program as `python dna.py databases/large.csv sequences/15.txt`. Your program should output `Sirius`.
* Run your program as `python dna.py databases/large.csv sequences/16.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/large.csv sequences/17.txt`. Your program should output `Harry`.
* Run your program as `python dna.py databases/large.csv sequences/18.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/large.csv sequences/19.txt`. Your program should output `Fred`.
* Run your program as `python dna.py databases/large.csv sequences/20.txt`. Your program should output `No match`.

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/dna
```

<a id="style"></a>

##### Style

```
style50 dna.py
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/dna
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/6/dna.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `dna/dna.py` | 1611 | [yes](dna-distribution/files/dna/dna.py) |
| `dna/databases/large.csv` | 740 | [yes](dna-distribution/files/dna/databases/large.csv) |
| `dna/databases/small.csv` | 57 | [yes](dna-distribution/files/dna/databases/small.csv) |
| `dna/sequences/15.txt` | 5757 | [yes](dna-distribution/files/dna/sequences/15.txt) |
| `dna/sequences/14.txt` | 5720 | [yes](dna-distribution/files/dna/sequences/14.txt) |
| `dna/sequences/16.txt` | 5879 | [yes](dna-distribution/files/dna/sequences/16.txt) |
| `dna/sequences/17.txt` | 5747 | [yes](dna-distribution/files/dna/sequences/17.txt) |
| `dna/sequences/13.txt` | 6401 | [yes](dna-distribution/files/dna/sequences/13.txt) |
| `dna/sequences/12.txt` | 6335 | [yes](dna-distribution/files/dna/sequences/12.txt) |
| `dna/sequences/10.txt` | 5782 | [yes](dna-distribution/files/dna/sequences/10.txt) |
| `dna/sequences/11.txt` | 6178 | [yes](dna-distribution/files/dna/sequences/11.txt) |
| `dna/sequences/9.txt` | 5880 | [yes](dna-distribution/files/dna/sequences/9.txt) |
| `dna/sequences/8.txt` | 5894 | [yes](dna-distribution/files/dna/sequences/8.txt) |
| `dna/sequences/5.txt` | 6084 | [yes](dna-distribution/files/dna/sequences/5.txt) |
| `dna/sequences/4.txt` | 200 | [yes](dna-distribution/files/dna/sequences/4.txt) |
| `dna/sequences/6.txt` | 5723 | [yes](dna-distribution/files/dna/sequences/6.txt) |
| `dna/sequences/7.txt` | 6170 | [yes](dna-distribution/files/dna/sequences/7.txt) |
| `dna/sequences/3.txt` | 242 | [yes](dna-distribution/files/dna/sequences/3.txt) |
| `dna/sequences/2.txt` | 301 | [yes](dna-distribution/files/dna/sequences/2.txt) |
| `dna/sequences/1.txt` | 171 | [yes](dna-distribution/files/dna/sequences/1.txt) |
| `dna/sequences/20.txt` | 5872 | [yes](dna-distribution/files/dna/sequences/20.txt) |
| `dna/sequences/19.txt` | 6079 | [yes](dna-distribution/files/dna/sequences/19.txt) |
| `dna/sequences/18.txt` | 6781 | [yes](dna-distribution/files/dna/sequences/18.txt) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python
- Folder: `dna`; files shown on the page: `dna.py`
- check50: `cs50/problems/2026/x/dna`
- style50: `dna.py`
- submit50: `cs50/problems/2026/x/dna`
- Page sections (order on source): Problem to Solve, Demo, Distribution Code, Background, Specification, Hints, Walkthrough, How to Test, How to Submit
- Walkthrough videos: https://www.youtube.com/embed/j84b_EgntcQ
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Python csv module، dicts and lists، file I/O، command-line arguments، string searching.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write dna.py, which takes a CSV database of people's STR (short tandem repeat) counts and a DNA sequence text file as command-line arguments. Load both, compute the longest consecutive run of each STR in the sequence (a longest_match helper is provided), and print the matching person's name or "No match".

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Problem Set 6](README.md) (`pset-6`)
- **Prerequisites (generated):** [Week 6 — Lecture notes (Python)](../lecture.md) (`week-6-lecture`)
- **Related:**
  - [Command-Line Arguments (argc, argv)](../../../concepts/command-line-arguments.md) (`concept-command-line-arguments`)
  - [Dictionaries (dict)](../../../concepts/dictionaries.md) (`concept-dictionaries`)
  - [File I/O (fopen, fread, fwrite, fclose)](../../../concepts/file-io.md) (`concept-file-io`)
  - [Python Basics](../../../concepts/python-basics.md) (`concept-python-basics`)
  - [Strings](../../../concepts/strings.md) (`concept-strings`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
کار با CSV، دیکشنری و جستجو در رشته‌ها در Python.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. ساختار فایل CSV پایگاه داده را بررسی کن: سطر اول چه اطلاعاتی می‌دهد؟
2. برای هر STR باید «طولانی‌ترین تکرار متوالی» را پیدا کنی؛ کد توزیعی در این باره چه چیزی فراهم کرده است؟
3. تطابق یعنی همه‌ی شمارش‌ها برابر باشند؛ اگر هیچ‌کس تطابق نداشت چه چاپ می‌شود؟

### اشتباه‌های رایج (مفهومی)
- مقایسه‌ی عدد با رشته
- ثابت فرض کردن نام ستون‌ها

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/dna` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/6/dna/ — retrieved 2026-10-18T05:11:41+03:30, sha256 `0d15f67a07cab491…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
