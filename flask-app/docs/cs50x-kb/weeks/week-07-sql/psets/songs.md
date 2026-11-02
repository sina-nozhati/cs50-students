---
id: pset-7-songs
type: pset
title: Songs — Problem Set 7
week: 7
parent: pset-7
children: []
prerequisites:
- week-7-lecture
related:
- concept-functions
- concept-sql-basics
- concept-sql-joins-and-keys
source_urls:
- https://cs50.harvard.edu/x/psets/7/songs/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:42+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- SQL
tags:
- aggregate-functions
- joins-subqueries
- pset
- songs
- sql-select
- where-order-by-limit
checksum: sha256:e2b4a8a9e451da1bd0605899e2aa0fd05966ad4c27f1cd76b69e714d6675b8b8
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Songs — Problem Set 7

## 1. Source metadata
- **Title:** Songs — Problem Set 7
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/7/songs/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:42+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/7/songs/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="songs"></a>

### Songs

![Spotify Wrapped '22 Logo](https://cs50.harvard.edu/x/psets/7/songs/wrapped.png)

<a id="problem-to-solve"></a>

#### Problem to Solve

Write SQL queries to answer questions about a database of the 100 most-streamed songs on [Spotify](https://en.wikipedia.org/wiki/Spotify) in 2018.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/DsiNSGFrMq2J6t9aDYhIQUQHy]

<a id="getting-started"></a>

#### Getting Started

For this problem, you’ll use a database provided to you by CS50’s staff.

> **Download the distribution code** *(collapsible block on the source page)*
>
> Open [VS Code](https://cs50.dev/).
>
> Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.
>
> ```
> $
> ```
>
> Click inside of that terminal window and then execute
>
> ```
> wget https://cdn.cs50.net/2026/x/psets/7/songs.zip
> ```
>
> followed by Enter in order to download a ZIP called `songs.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
>
> Now execute
>
> ```
> unzip songs.zip
> ```
>
> to create a folder called `songs`. You no longer need the ZIP file, so you can execute
>
> ```
> rm songs.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd songs
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> songs/ $
> ```
>
> If all was successful, you should execute
>
> ```
> ls
> ```
>
> and you should see 8 .sql files, `songs.db`, and `answers.txt`.
>
> If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

<a id="understanding"></a>

#### Understanding

Provided to you is a file called `songs.db`, a SQLite database that stores data from [Spotify](https://developer.spotify.com/documentation/web-api/) about songs and their artists. This dataset contains the top 100 streamed songs on Spotify in 2018. In a terminal window, run `sqlite3 songs.db` so that you can begin executing queries on the database.

First, when `sqlite3` prompts you to provide a query, type `.schema` and press enter. This will output the `CREATE TABLE` statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.

Notice that every `artist` has an `id` and a `name`. Notice, too, that every song has a `name`, an `artist_id` (corresponding to the `id` of the artist of the song), as well as values for the danceability, energy, key, loudness, speechiness (presence of spoken words in a track), valence, tempo, and duration of the song (measured in milliseconds).

The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables. After you do so, you’ll reflect on the ways Spotify might use this same data in their annual [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) campaign to characterize listeners’ habits.

<a id="implementation-details"></a>

#### Implementation Details

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You **should not** assume anything about the `id`s of any particular songs or artists: your queries should be accurate even if the `id` of any particular song or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of songs, for example, then your query should not also output each song’s tempo.

1. In `1.sql`, write a SQL query to list the names of all songs in the database.
   * Your query should output a table with a single column for the name of each song.
2. In `2.sql`, write a SQL query to list the names of all songs in increasing order of tempo.
   * Your query should output a table with a single column for the name of each song.
3. In `3.sql`, write a SQL query to list the names of the top 5 longest songs, in descending order of length.
   * Your query should output a table with a single column for the name of each song.
4. In `4.sql`, write a SQL query that lists the names of any songs that have danceability, energy, and valence greater than 0.75.
   * Your query should output a table with a single column for the name of each song.
5. In `5.sql`, write a SQL query that returns the average energy of all the songs.
   * Your query should output a table with a single column and a single row containing the average energy.
6. In `6.sql`, write a SQL query that lists the names of songs that are by Post Malone.
   * Your query should output a table with a single column for the name of each song.
   * You should not make any assumptions about what Post Malone’s `artist_id` is.
7. In `7.sql`, write a SQL query that returns the average energy of songs that are by Drake.
   * Your query should output a table with a single column and a single row containing the average energy.
   * You should not make any assumptions about what Drake’s `artist_id` is.
8. In `8.sql`, write a SQL query that lists the names of the songs that feature other artists.
   * Songs that feature other artists will include “feat.” in the name of the song.
   * Your query should output a table with a single column for the name of each song.

<a id="hints"></a>

#### Hints

See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!

> **List the names of all songs in the database** *(collapsible block on the source page)*
>
> Recall that, to select all values in a table’s column, you can use SQL’s `SELECT` keyword. `SELECT` is followed by the column (or columns) you’d like to select, which is in turn followed by `FROM table` where `table` is the name of the table you’d like to select from.
>
> In `1.sql`, then, try writing the following:
>
> ```sql
> -- All songs in the database.
> SELECT name
> FROM songs;
> ```

> **List the names of all songs in increasing order of tempo** *(collapsible block on the source page)*
>
> Recall that SQL has an `ORDER BY` keyword, by which you can order the results of your query by the value in a certain column. For example, `ORDER BY tempo` will order results by the column `tempo`.
>
> In `2.sql`, then, try writing the following:
>
> ```sql
> -- All songs in increasing order of tempo.
> SELECT name
> FROM songs
> ORDER BY tempo;
> ```

> **List the names of the top 5 longest songs, in descending order of length** *(collapsible block on the source page)*
>
> Recall that `ORDER BY` need not always sort in ascending order. You can specify that your results be sorted in *descending* order by appending `DESC`. For example, `ORDER BY duration_ms DESC` will list results in descending order, by duration.
>
> And recall, too, that `LIMIT n` can specify that you only want the first \(n\) rows that match a specific query. For example, `LIMIT 5` will return only the first five results of the query.
>
> In `3.sql`, then, try writing the following:
>
> ```sql
> -- The names of the top 5 longest songs, in descending order of length.
> SELECT name
> FROM songs
> ORDER BY duration_ms DESC
> LIMIT 5;
> ```

> **List the names of any songs that have danceability, energy, and valence greater than 0.75** *(collapsible block on the source page)*
>
> Recall that you can filter results in SQL with `WHERE` clauses, which are followed by some condition which typically tests the values in a row’s columns.
>
> Recall, too, that SQL’s operators function much the same way as C’s. For example, `>` evaluates to “true” when the value on the left is greater than the value on the right. You may chain these expressions together, using `AND` or `OR`, to form one larger condition.
>
> In `4.sql`, then, try writing the following:
>
> ```sql
> -- The names of any songs that have danceability, energy, and valence greater than 0.75.
> SELECT name
> FROM songs
> WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;
> ```

> **Find average energy of all the songs** *(collapsible block on the source page)*
>
> Recall that SQL supports keywords not just to select particular rows, but also to *aggregate* the data in those rows. In particular, you might find the `AVG` keyword (to compute averages) useful. To aggregate the results of a column, just apply the aggregation function to that column. For example, `SELECT AVG(energy)` will find the average of the values in the energy column for the given query.
>
> In `5.sql`, then, try writing the following:
>
> ```sql
> -- The average energy of all the songs.
> SELECT AVG(energy)
> FROM songs;
> ```

> **List the names of songs that are by Post Malone** *(collapsible block on the source page)*
>
> Notice that, if you execute `.schema songs` in your sqlite prompt, the `songs` table has song names but not artist names! Instead, `songs` has an `artist_id` column. To list the names of songs by Post Malone, then, you’ll first need to identify Post Malone’s artist id.
>
> ```sql
> -- Identify Post Malone's artist id
> SELECT id
> FROM artists
> WHERE name = 'Post Malone';
> ```
>
> This query returns 54. Now, you could query the `songs` table for any song with Post Malone’s id.
>
> ```sql
> SELECT name
> FROM songs
> WHERE artist_id = 54;
> ```
>
> But, per the specification, you should be mindful not to assume knowledge of any ids. You could improve the design of this query by *nesting* your two queries.
>
> In `6.sql`, then, try writing the following:
>
> ```sql
> -- The names of songs that are by Post Malone.
> SELECT name
> FROM songs
> WHERE artist_id =
> (
>     SELECT id
>     FROM artists
>     WHERE name = 'Post Malone'
> );
> ```

> **Find the average energy of songs that are by Drake** *(collapsible block on the source page)*
>
> Notice that, similar to the previous query, you’ll need to combine multiple tables to successfully run this query. You could again use nested subqueries, but consider another approach too!
>
> Recall that you can use SQL’s `JOIN` keyword to combine multiple tables into one, so long as you specify which columns across those tables should ultimately match. For example, the following query joins the `songs` and `artists` tables, indicating that the `artist_id` column in the `songs` table and the `id` column in the `artists` table should match:
>
> ```sql
> SELECT *
> FROM songs
> JOIN artists ON songs.artist_id = artists.id
> ```
>
> With these two tables combined, it’s only a matter of filtering your selection to find the average energy of songs by Drake.
>
> In `7.sql`, then, try writing the following:
>
> ```sql
> -- The average energy of songs that are by Drake
> SELECT AVG(energy)
> FROM songs
> JOIN artists ON songs.artist_id = artists.id
> WHERE artists.name = 'Drake';
> ```

> **List the names of the songs that feature other artists** *(collapsible block on the source page)*
>
> For this query, note that songs which feature other artists typically have some mention of “feat.” in their title. Recall that SQL’s `LIKE` keyword can be used to match strings with certain phrases (like “feat.”!). To do so, you can use `%`: a wildcard character that matches any sequence of characters.
>
> In `8.sql`, then, try writing the following:
>
> ```sql
> -- The names of songs that feature other artists.
> SELECT name
> FROM songs
> WHERE name LIKE '%feat.%';
> ```

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://video.cs50.io/wgKPUd_95AA](https://video.cs50.io/wgKPUd_95AA)

> **Not sure how to solve?** *(collapsible block on the source page)*
>

<a id="spotify-wrapped"></a>

#### Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) is a feature presenting Spotify users’ 100 most played songs from the past year. In 2021, Spotify Wrapped calculated an [“Audio Aura”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) for each user, a “reading of [their] two most prominent moods as dictated by [their] top songs and artists of the year.” Suppose Spotify determines an audio aura by looking at the average energy, valence, and danceability of a person’s top 100 songs from the past year. In `answers.txt`, reflect on the following questions:

* If `songs.db` contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
* Hypothesize about why the way you’ve calculated this aura might *not* be very representative of the listener. What better ways of calculating this aura would you propose?

Be sure to submit `answers.txt` along with each of your `.sql` files!

<a id="how-to-test"></a>

#### How to Test

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/songs
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/songs
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/7/songs.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `songs/4.sql` | 0 | [yes](songs-distribution/files/songs/4.sql) |
| `songs/5.sql` | 0 | [yes](songs-distribution/files/songs/5.sql) |
| `songs/7.sql` | 0 | [yes](songs-distribution/files/songs/7.sql) |
| `songs/6.sql` | 0 | [yes](songs-distribution/files/songs/6.sql) |
| `songs/2.sql` | 0 | [yes](songs-distribution/files/songs/2.sql) |
| `songs/3.sql` | 0 | [yes](songs-distribution/files/songs/3.sql) |
| `songs/1.sql` | 0 | [yes](songs-distribution/files/songs/1.sql) |
| `songs/8.sql` | 0 | [yes](songs-distribution/files/songs/8.sql) |
| `songs/answers.txt` | 0 | [yes](songs-distribution/files/songs/answers.txt) |
| `songs/songs.db` | 24576 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): SQL
- Folder: `songs`; files shown on the page: `1.sql`, `2.sql`, `3.sql`, `4.sql`, `5.sql`, `6.sql`, `7.sql`, `8.sql`, `answers.txt`, `songs.db`
- check50: `cs50/problems/2026/x/songs`
- style50: not stated
- submit50: `cs50/problems/2026/x/songs`
- Page sections (order on source): Problem to Solve, Demo, Getting Started, Understanding, Implementation Details, Hints, Walkthrough, Spotify Wrapped, How to Test, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم SQL SELECT، WHERE / ORDER BY / LIMIT، aggregate functions، JOINs / subqueries.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write eight SQL queries (1.sql to 8.sql) against songs.db, a database of the 100 most-streamed Spotify songs of 2018. Each file holds a single query, possibly nested, that returns only the requested columns without assuming specific ids. In answers.txt, reflect on how to characterise a listener's 'audio aura' from this data and the limits of that approach.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 7](README.md) (`pset-7`)
- **Prerequisites (generated):** [Week 7 — Lecture notes (SQL)](../lecture.md) (`week-7-lecture`)
- **Related:**
  - [Functions](../../../concepts/functions.md) (`concept-functions`)
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)
  - [Primary Keys, Foreign Keys and JOINs](../../../concepts/sql-joins-and-keys.md) (`concept-sql-joins-and-keys`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
اولین پرس‌وجوهای SQL روی یک پایگاه داده‌ی واقعی.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. اول با دستور .schema ساختار جدول‌ها را ببین.
2. هر سؤال را به این تبدیل کن: کدام ستون‌ها، از کدام جدول، با چه شرط، با چه ترتیب؟
3. اگر به داده‌ی دو جدول نیاز داری، کلید مشترک آن‌ها چیست؟

### اشتباه‌های رایج (مفهومی)
- برگرداندن ستون‌های اضافه

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/songs` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/7/songs/ — retrieved 2026-10-18T05:11:42+03:30, sha256 `e2b4a8a9e451da1b…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
