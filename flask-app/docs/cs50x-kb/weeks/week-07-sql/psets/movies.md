---
id: pset-7-movies
type: pset
title: Movies — Problem Set 7
week: 7
parent: pset-7
children: []
prerequisites:
- week-7-lecture
related:
- concept-sql-basics
- concept-sql-joins-and-keys
source_urls:
- https://cs50.harvard.edu/x/psets/7/movies/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:43+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 3
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- SQL
tags:
- aggregates
- joins
- movies
- nested-queries
- pset
- relational-schema
- sql-select
checksum: sha256:a0915423d0c9423c76899a11f2df906d0810fa41b92b00ff7fcb15f583531803
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Movies — Problem Set 7

## 1. Source metadata
- **Title:** Movies — Problem Set 7
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/7/movies/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:43+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/7/movies/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="movies"></a>

### Movies

**Changes for 2026:** `5.sql` now requires matching movies that begin with “Harry Potter and the “ (not just “Harry Potter”). `9.sql` now requires outputting **two columns** (the ID and name of each person), not just names. If you started this problem prior to 2026, be sure to update your queries accordingly!

![IMDb Logo](https://cs50.harvard.edu/x/psets/7/movies/imdb.png)

<a id="problem-to-solve"></a>

#### Problem to Solve

Provided to you is a file called `movies.db`, a SQLite database that stores data from [IMDb](https://www.imdb.com/) about movies, the people who directed and starred in them, and their ratings. Write SQL queries to answer questions about this database of movies.

<a id="demo"></a>

#### Demo

[Terminal demo recording (asciinema): https://asciinema.org/a/uPWDqSe0NjjqXLF3qxzpsMnfv]

<a id="getting-started"></a>

#### Getting Started

For this problem, you’ll use a database provided to you by CS50’s staff.

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
> wget https://cdn.cs50.net/2026/x/psets/7/movies.zip
> ```
>
> in order to download a ZIP called `movies.zip` into your codespace.
>
> Then execute
>
> ```
> unzip movies.zip
> ```
>
> to create a folder called `movies`. You no longer need the ZIP file, so you can execute
>
> ```
> rm movies.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd movies
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> movies/ $
> ```
>
> Execute `ls` by itself, and you should see 13 .sql files, as well as `movies.db`.
>
> If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

<a id="specification"></a>

#### Specification

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You **should not** assume anything about the `id`s of any particular movies or people: your queries should be accurate even if the `id` of any particular movie or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of movies, for example, then your query should not also output each movie’s release year.

You’re welcome to check your queries’ results against [IMDb](https://www.imdb.com/) itself, but realize that ratings on the website might differ from those in `movies.db`, as more votes might have been cast since we downloaded the data!

1. In `1.sql`, write a SQL query to list the titles of all movies released in 2008.
   * Your query should output a table with a single column for the title of each movie.
2. In `2.sql`, write a SQL query to determine the birth year of Emma Stone.
   * Your query should output a table with a single column and a single row (not counting the header) containing Emma Stone’s birth year.
   * You may assume that there is only one person in the database with the name Emma Stone.
3. In `3.sql`, write a SQL query to list the titles of all movies with a release date on or after 2018, in alphabetical order.
   * Your query should output a table with a single column for the title of each movie.
   * Movies released in 2018 should be included, as should movies with release dates in the future.
4. In `4.sql`, write a SQL query to determine the number of movies with an IMDb rating of 10.0.
   * Your query should output a table with a single column and a single row (not counting the header) containing the number of movies with a 10.0 rating.
5. In `5.sql`, write a SQL query to list the titles and release years of all Harry Potter movies, in chronological order.
   * Your query should output a table with two columns, one for the title of each movie and one for the release year of each movie.
   * You may assume that the title of all Harry Potter movies will begin with the words “Harry Potter and the “, and that if a movie title begins with the words “Harry Potter and the “, it is a Harry Potter movie.
6. In `6.sql`, write a SQL query to determine the average rating of all movies released in 2012.
   * Your query should output a table with a single column and a single row (not counting the header) containing the average rating.
7. In `7.sql`, write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title.
   * Your query should output a table with two columns, one for the title of each movie and one for the rating of each movie.
   * Movies that do not have ratings should not be included in the result.
8. In `8.sql`, write a SQL query to list the names of all people who starred in Toy Story.
   * Your query should output a table with a single column for the name of each person.
   * You may assume that there is only one movie in the database with the title Toy Story.
9. In `9.sql`, write a SQL query to list the ID and names of all people who starred in a movie released in 2004, ordered by birth year.
   * Your query should output a table with two columns: one for the ID and one for the name of each person.
   * People with the same birth year may be listed in any order.
   * No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
   * If a person appeared in more than one movie in 2004, they should only appear in your results once.
10. In `10.sql`, write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
    * Your query should output a table with a single column for the name of each person.
    * If a person directed more than one movie that received a rating of at least 9.0, they should only appear in your results once.
11. In `11.sql`, write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
    * Your query should output a table with a single column for the title of each movie.
    * You may assume that there is only one person in the database with the name Chadwick Boseman.
12. In `12.sql`, write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.
    * Your query should output a table with a single column for the title of each movie.
    * You may assume that there is only one person in the database with the name Bradley Cooper.
    * You may assume that there is only one person in the database with the name Jennifer Lawrence.
13. In `13.sql`, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
    * Your query should output a table with a single column for the name of each person.
    * There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
    * Kevin Bacon himself should not be included in the resulting list.

<a id="hints"></a>

#### Hints

> **Understand the schema of movies.db** *(collapsible block on the source page)*
>
> Whenever you engage with a new database, it’s best to first understand its *schema*. In a terminal window, run `sqlite3 movies.db` so that you can begin executing queries on the database.
>
> First, when `sqlite3` prompts you to provide a query, type `.schema` and press enter. This will output the `CREATE TABLE` statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.
>
> Notice that the `movies` table has an `id` column that uniquely identifies each movie, as well as columns for the `title` of a movie and the `year` in which the movie was released. The `people` table also has an `id` column, and also has columns for each person’s `name` and `birth` year.
>
> Movie ratings, meanwhile, are stored in the `ratings` table. The first column in the table is `movie_id`: a foreign key that references the `id` of the `movies` table. The rest of the row contains data about the `rating` for each movie and the number of `votes` the movie has received on IMDb.
>
> Finally, the `stars` and `directors` tables match people to the movies in which they acted or directed. (Only [principal](https://www.imdb.com/interfaces/) stars and directors are included.) Each table has just two columns: `movie_id` and `person_id`, which reference a specific movie and person, respectively.
>
> The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables.

> **Consistently style your queries** *(collapsible block on the source page)*
>
> See [sqlstyle.guide](https://www.sqlstyle.guide/) for pointers on good style in SQL, especially as your queries get more complex!

> **List the titles of all movies released in 2008** *(collapsible block on the source page)*
>
> Recall that you can select one (or more) columns from a database using `SELECT`, per the example below,
>
> ```sql
> SELECT column0, column1 FROM table;
> ```
>
> where `column0` is the title of one column, and `column1` is the title of another.
>
> And recall that you can filter the rows returned in a query with the `WHERE` keyword, followed by a condition. You can use `=`, `>`, `<`, and [other operators](https://www.w3schools.com/sql/sql_operators.asp) too.
>
> ```sql
> SELECT column FROM table
> WHERE condition;
> ```
>
> See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!

> **Determine the birth year of Emma Stone** *(collapsible block on the source page)*
>
> Recall that a `WHERE` clause can evaluate conditions not just with numbers, but with strings.

> **List the titles of all movies with a release date on or after 2018, in alphabetical order** *(collapsible block on the source page)*
>
> Try breaking this query into two steps. First, find the movies with a release date on or after 2018. Then, put those movies’ titles in alphabetical order.
>
> To find the movies with a release date on or after 2018, recall that a condition in SQL supports the use of many common [comparison operators](https://www.w3schools.com/sql/sql_operators.asp), including `>=` for “greater than or equal to.” Check to see if your query returns the correct number of movies, per [How to Test](https://cs50.harvard.edu/x/psets/7/movies/#how-to-test).
>
> Finally, sort the query’s results alphabetically by title. Recall that `ORDER BY` can sort data by a column in your results, per the example below.
>
> ```sql
> ...
> ORDER BY column;
> ```

> **Determine the number of movies with an IMDb rating of 10.0** *(collapsible block on the source page)*
>
> Notice this question asks you not for *individual* movies with a rating of 10.0, but for the *number* of movies with such a rating. In other words, you should collect (“aggregate”) the results of your query into a single number (the number of rows). Recall that SQL supports an “aggregation function” called `COUNT`, which you can use on a column per the example below.
>
> ```sql
> SELECT COUNT(column)
> FROM table;
> ```

> **List the titles and release years of all Harry Potter movies, in chronological order** *(collapsible block on the source page)*
>
> For this query, you’ll likely want to make use of SQL’s `LIKE` keyword. Recall that `LIKE` can make use of so-called “wildcard characters”, such as `%`, that will match any character (or sequence thereof).
>
> ```sql
> SELECT column0, column1
> FROM table
> WHERE column1 LIKE pattern;
> ```

> **Determine the average rating of all movies released in 2012** *(collapsible block on the source page)*
>
> Here’s another example of a query in which you’ll need to aggregate data. Consider SQL’s `AVG` aggregation function, to compute an average.
>
> Consider, too, that this query makes use of data stored in two separate tables: `ratings` and `movies`. Recall that—so long as one table has a foreign key that matches a column in another table—you can combine two tables using SQL’s `JOIN` keyword. To use the `JOIN` keyword, you should specify the table you’d like to join and the column by which to do so.
>
> ```sql
> SELECT column0
> FROM table0
> JOIN table1 ON table0.column1 = table1.column2
> ```

> **List all movies released in 2010 and their ratings, in descending order by rating** *(collapsible block on the source page)*
>
> Recall that `ORDER BY` need not always sort in ascending order. You can specify that your results be sorted in *descending* order by appending `DESC`.
>
> ```sql
> ...
> ORDER BY column DESC;
> ```

> **List the names of all people who starred in Toy Story** *(collapsible block on the source page)*
>
> When you see a more complex query such as this one, it’s best to break it down into smaller pieces. Ultimately, your query should arrive at a list of names, per the below.
>
> ```sql
> -- Select names
> SELECT name
> FROM people
> WHERE ...
> ```
>
> But how’s best to arrive at the names of those who starred in Toy Story? Consider that the `people` table alone doesn’t have this information (but the `stars` table might!). Indeed, the `stars` table combines two columns, `person_id` and `movie_id`: any person with a `person_id` that is associated with Toy Story’s `movie_id` starred in Toy Story.
>
> ```sql
> -- Select names
> SELECT name
> FROM people
> WHERE ...
>
> -- Select person IDs
> SELECT person_id
> FROM stars
> WHERE movie_id = ...
> ```
>
> A natural next step, then, is to find Toy Story’s movie ID.
>
> ```sql
> -- Select names
> SELECT name
> FROM people
> WHERE ...
>
> -- Select person IDs
> SELECT person_id
> FROM stars
> WHERE movie_id = ...
>
> -- Find Toy Story's ID
> SELECT id
> FROM movies
> WHERE title = 'Toy Story';
> ```
>
> Of course, you’ve presently written three *separate* queries. But notice that some queries (the first two) would be complete by including results of the query directly below them. The process of making a query that depends on the results of a “subquery” is called “nesting” queries. It’s quite the hint, but here’s one way to nest the above queries!
>
> ```sql
> -- Select names
> SELECT name
> FROM people
> WHERE id IN
> (
>     -- Select person IDs
>     SELECT person_id
>     FROM stars
>     WHERE movie_id = (
>
>         -- Select Toy Story's ID
>         SELECT id
>         FROM movies
>         WHERE title = 'Toy Story'
>     )
> );
> ```

> **List the ID and names of all people who starred in a movie released in 2004, ordered by birth year** *(collapsible block on the source page)*
>
> Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…
>
> 1. Find the IDs of movies released in 2004
> 2. Find the IDs of people who starred in those movies
> 3. Find the IDs and names of people with those people IDs
>
> Then, try nesting those queries to arrive at a single query that returns all the IDs and names of people who starred in a movie released in 2004. Consider how you might then order the results of your query.
>
> As a closing note, keep in mind that multiple people can have the same name. Although each person should only appear in your results once, two stars having the same name does not necessarily mean they are the same person.

> **List the names of all people who have directed a movie that received a rating of at least 9.0** *(collapsible block on the source page)*
>
> Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…
>
> 1. Find the IDs of movies with at least a 9.0 rating
> 2. Find the IDs of people who directed those movies
> 3. Find the names of people with those people IDs
>
> Then, try nesting those queries to arrive at a single query that returns the names of all people who have directed a movie that received a rating of at least 9.0.

> **List the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated** *(collapsible block on the source page)*
>
> Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…
>
> 1. Find the ID of Chadwick Boseman
> 2. Find the IDs of movies associated with Chadwick Boseman’s ID
> 3. Find the movie titles with those movie IDs
>
> Then, try nesting those queries to arrive at a single query that returns the titles of Chadwick Boseman’s movies.
>
> From there, you’ll need to determine the ratings of those titles and sort those titles by rating, in descending order. Consider how you could combine a relevant table (likely `ratings`!) and order the results by a relevant column.
>
> Finally, read up on SQL’s [`LIMIT`](https://www.sqlitetutorial.net/sqlite-limit/) keyword, which will return the top \(n\) rows in a query.

> **List the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred** *(collapsible block on the source page)*
>
> Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…
>
> 1. Find the ID of Bradley Cooper
> 2. Find the ID of Jennifer Lawrence
> 3. Find the IDs of movies associated with Bradley Cooper’s ID
> 4. Find the IDs of movies associated with Jennifer Lawrence’s ID
> 5. Find movie titles from the movie IDs associated with *both* Bradley Cooper and Jennifer Lawrence
>
> Then, try nesting those queries to arrive at a single query that returns the movies in which both Bradley Cooper and Jennifer Lawrence starred.
>
> Recall that you can build compound conditions in SQL using `AND` or `OR`.

> **List the names of all people who starred in a movie in which Kevin Bacon also starred** *(collapsible block on the source page)*
>
> Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…
>
> 1. Find the ID of Kevin Bacon (the one born in 1958!)
> 2. Find the IDs of movies associated with Kevin Bacon’s ID
> 3. Find the IDs of people associated with those movie IDs
> 4. Find the names of people with those people IDs
>
> Then, try nesting those queries to arrive at a single query that returns the names of all people who starred in a movie in which Kevin Bacon also starred. **Keep in mind that you’ll want to exclude Kevin Bacon himself from the results!**

<a id="walkthrough"></a>

#### Walkthrough

[Embedded video: https://www.youtube.com/embed/v5_A3giDlQs](https://www.youtube.com/embed/v5_A3giDlQs)

<a id="usage"></a>

#### Usage

To test your queries in VS Code, you can query the database by running

```
$ cat filename.sql | sqlite3 movies.db
```

where `filename.sql` is the file containing your SQL query.

You can also run

```
$ cat filename.sql | sqlite3 movies.db > output.txt
```

to redirect the output of the query to a text file called `output.txt`. (This can be useful for checking how many rows are returned by your query!)

<a id="how-to-test"></a>

#### How to Test

While `check50` is available for this problem, you’re encouraged to instead test your code on your own for each of the following. You can run `sqlite3 movies.db` to run additional queries on the database to ensure that your result is correct.

If you’re using the `movies.db` database provided in this problem set’s distribution, you should find that

* Executing `1.sql` results in a table with 1 column and 10,647 rows.
* Executing `2.sql` results in a table with 1 column and 1 row.
* Executing `3.sql` results in a table with 1 column and 154,665 rows.
* Executing `4.sql` results in a table with 1 column and 1 row.
* Executing `5.sql` results in a table with 2 columns and 18 rows.
* Executing `6.sql` results in a table with 1 column and 1 row.
* Executing `7.sql` results in a table with 2 columns and 7,386 rows.
* Executing `8.sql` results in a table with 1 column and 10 rows.
* Executing `9.sql` results in a table with 2 columns and 36,219 rows.
* Executing `10.sql` results in a table with 1 column and 4,675 rows.
* Executing `11.sql` results in a table with 1 column and 5 rows.
* Executing `12.sql` results in a table with 1 column and 4 rows.
* Executing `13.sql` results in a table with 1 column and 550 rows.

Note that row counts do not include header rows that only show column names.

If your query returns a number of rows that is slightly different from the expected output, be sure that you’re properly handling duplicates! For queries that ask for a list of names, no one person should be listed twice, but two different people who have the same name should each be listed.

<a id="correctness"></a>

##### Correctness

```
check50 cs50/problems/2026/x/movies
```

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/movies
```

<a id="acknowledgements"></a>

#### Acknowledgements

Information courtesy of
IMDb
([imdb.com](https://www.imdb.com)).
Used with permission.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/7/movies.zip

_Not inventoried: zip skipped: too large (77017284 bytes > 62914560)_

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): SQL
- Folder: `movies`; files shown on the page: `1.sql`, `2.sql`, `3.sql`, `4.sql`, `5.sql`, `6.sql`, `7.sql`, `8.sql`, `9.sql`, `10.sql`, `11.sql`, `12.sql`, `13.sql`, `movies.db`
- check50: `cs50/problems/2026/x/movies`
- style50: not stated
- submit50: `cs50/problems/2026/x/movies`
- Page sections (order on source): Problem to Solve, Demo, Getting Started, Specification, Hints, Walkthrough, Usage, How to Test, How to Submit, Acknowledgements
- Walkthrough videos: https://www.youtube.com/embed/v5_A3giDlQs
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم SQL SELECT، JOINs، nested queries، aggregates، relational schema.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Write thirteen SQL queries (1.sql to 13.sql) against movies.db, an IMDb-derived SQLite database of movies, people, stars, directors and ratings. Each answers a specific question, one query per file, returning exactly the requested data.

**سطح دشواری تخمینی (تولیدشده):** 3 از ۵

## 4. Relationships
- **Parent:** [Problem Set 7](README.md) (`pset-7`)
- **Prerequisites (generated):** [Week 7 — Lecture notes (SQL)](../lecture.md) (`week-7-lecture`)
- **Related:**
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)
  - [Primary Keys, Foreign Keys and JOINs](../../../concepts/sql-joins-and-keys.md) (`concept-sql-joins-and-keys`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
پرس‌وجوهای چندجدولی، JOIN و زیرپرس‌وجو.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. رابطه‌ی جدول‌های people، movies، stars و directors را روی کاغذ رسم کن.
2. پرس‌وجوهای پیچیده را از داخل به بیرون بساز: اول بخش کوچک را جدا اجرا و بررسی کن.
3. مراقب نتایج تکراری باش.

### اشتباه‌های رایج (مفهومی)
- تکرار نتایج به دلیل JOIN
- فرض یکتا بودن نام‌ها

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای `check50 cs50/problems/2026/x/movies` و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/7/movies/ — retrieved 2026-10-18T05:11:43+03:30, sha256 `a0915423d0c9423c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- https://cdn.cs50.net/2026/x/psets/7/movies.zip: zip skipped: too large (77017284 bytes > 62914560)
