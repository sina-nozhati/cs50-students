---
id: week-7-lecture
type: lecture
title: Week 7 — Lecture notes (SQL)
week: 7
parent: week-7
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/notes/7/
- https://cs50.harvard.edu/x/weeks/7/
- https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:37+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- lecture
- notes
checksum: sha256:a8e4860d454734029be5ba3feb3c875257e82350407e2ee739be9b075a92e6d7
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Week 7 — Lecture notes (SQL)

## 1. Source metadata
- **Title:** Week 7 — Lecture notes (SQL)
- **Type:** lecture
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/notes/7/>, <https://cs50.harvard.edu/x/weeks/7/>, <https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:10:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/7/>, <https://cs50.harvard.edu/x/weeks/7/>, <https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Lecture materials (as linked from the week page)

- CS50 Video Player (English): <https://video.cs50.io/oqRU2So6Z2Y>
- YouTube (English): <https://youtu.be/oqRU2So6Z2Y>
- MP4 1080p (English; not downloaded): <https://cdn.cs50.net/2025/fall/lectures/7/lecture7-1080p.mp4>
- Audio MP3 (not downloaded): <https://cdn.cs50.net/2025/fall/lectures/7/lecture7.mp3>
- Slides (Google Slides): <https://docs.google.com/presentation/d/1LIwdwxj6Byq9RMe2Pwz9RiurtWDBX1YDrCgju_uirEI/edit?usp=sharing>
- Slides (PDF; not downloaded): <https://cdn.cs50.net/2025/fall/lectures/7/lecture7.pdf>
- Source code (directory index): <https://cdn.cs50.net/2025/fall/lectures/7/src7/>
- Source code (PDF): <https://cdn.cs50.net/2025/fall/lectures/7/src7.pdf>
- Source code (ZIP): <https://cdn.cs50.net/2025/fall/lectures/7/src7.zip>
- Subtitles .srt (English; URL only): <https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.srt>
- Transcript .txt (English): <https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.txt>
- Local transcript copy: [transcripts/lecture-en.txt](transcripts/lecture-en.txt)

### Lecture notes (verbatim)

<a id="lecture-7"></a>

### Lecture 7

<a id="welcome"></a>

#### Welcome!

* In previous weeks, we introduced you to Python, a high-level programming language that utilized the same building blocks we learned in C. However, we introduced this new language not for the purpose of learning “just another language.” Instead, we do so because some tools are better for some jobs and not so great for others!
* This week, we will be continuing with more syntax related to Python.
* Further, we will be integrating this knowledge with data.
* Finally, we will be discussing *SQL* or *Structured Query Language*, a domain-specific way by which we can interact with and modify data.
* Overall, one of the goals of this course is to learn to program generally – not simply how to program in the languages described in this course.

<a id="flat-file-database"></a>

#### Flat-File Database

* As you have likely seen before, data can often be described in patterns of columns and rows.
* Spreadsheets like those created in Microsoft Excel and Google Sheets can be outputted to a `csv` or *comma-separated values* file.
* If you look at a `csv` file, you’ll notice that the file is flat in that all of our data is stored in a single table represented by a text file. We call this form of data a *flat-file database*.
* All data is stored row by row. Each column is separated by a comma or another value.
* Python comes with native support for `csv` files.
* First, download [favorites.csv](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites.csv?download) and upload it to your file explorer inside [cs50.dev](https://cs50.dev). Second, examining this data, notice that the first row is special in that it defines each column. Then, each record is stored row by row.
* In your terminal window, type `code favorites.py` and write code as follows:

  ```py
  # Prints all favorites in CSV using csv.reader

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create reader
      reader = csv.reader(file)

      # Skip header row
      next(reader)

      # Iterate over CSV file, printing each favorite
      for row in reader:
          print(row[1])
  ```

  Notice that the `csv` library is imported. Further, we created a `reader` that will hold the result of `csv.reader(file)`. The `csv.reader` function reads each row from the file, and in our code, we store the results in `reader`. `print(row[1])`, therefore, will print the language from the `favorites.csv` file. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites0.py?download).
* You can improve your code as follows:

  ```py
  # Stores favorite in a variable

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create reader
      reader = csv.reader(file)

      # Skip header row
      next(reader)

      # Iterate over CSV file, printing each favorite
      for row in reader:
          favorite = row[1]
          print(favorite)
  ```

  Notice that `favorite` is stored and then printed. Also, notice that we use the `next` function to skip to the next line of our reader. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites1.py?download).
* One of the disadvantages of the above approach is that we are trusting that `row[1]` is always the favorite. However, what would happen if the columns had been moved around?
* We can fix this potential issue. Python also allows you to index by the keys of a list. Modify your code as follows:

  ```py
  # Prints all favorites in CSV using csv.DictReader

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Iterate over CSV file, printing each favorite
      for row in reader:
          favorite = row["language"]
          print(favorite)
  ```

  Notice that this example directly utilizes the `language` key in the print statement. `favorite` is assigned the value of `row["language"]`. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites2.py?download).
* This could be further simplified to:

  ```py
  # Prints all favorites in CSV using csv.DictReader

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Iterate over CSV file, printing each favorite
      for row in reader:
          print(row["language"])
  ```

  You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites3.py?download).
* To count the number of favorite languages expressed in the `csv` file, we can do the following:

  ```py
  # Counts favorites using variables

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Counts
      scratch, c, python = 0, 0, 0

      # Iterate over CSV file, counting favorites
      for row in reader:
          favorite = row["language"]
          if favorite == "Scratch":
              scratch += 1
          elif favorite == "C":
              c += 1
          elif favorite == "Python":
              python += 1

  # Print counts
  print(f"Scratch: {scratch}")
  print(f"C: {c}")
  print(f"Python: {python}")
  ```

  Notice that each language is counted using `if` statements. Further, notice the double equal `==` signs in those `if` statements. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites4.py?download).
* Python allows us to use a dictionary to count the `counts` of each language. Consider the following improvement upon our code:

  ```py
  # Counts favorites using dictionary

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Counts
      counts = {}

      # Iterate over CSV file, counting favorites
      for row in reader:
          favorite = row["language"]
          if favorite in counts:
              counts[favorite] += 1
          else:
              counts[favorite] = 1

  # Print counts
  for favorite in counts:
      print(f"{favorite}: {counts[favorite]}")
  ```

  Notice that the value in `counts` with the key `favorite` is incremented when it exists already. If it does not exist, we define `counts[favorite]` and set it to 1. Further, the formatted string has been improved to present the `counts[favorite]`. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites5.py?download).
* We can also utilize `try` and `except` to account for potential exceptions:

  ```py
  # Uses try/except instead

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Counts
      counts = {}

      # Iterate over CSV file, counting favorites
      for row in reader:
          favorite = row["language"]
          try:
              counts[favorite] += 1
          except KeyError:
              counts[favorite] = 1

  # Print counts
  for favorite in counts:
      print(f"{favorite}: {counts[favorite]}")
  ```

  Notice how the `if` and `else` have been replaced with `try` and `except`. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites6.py?download).
* Python also allows sorting `counts`. Improve your code as follows:

  ```py
  # Sorts favorites by key

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Counts
      counts = {}

      # Iterate over CSV file, counting favorites
      for row in reader:
          favorite = row["language"]
          if favorite in counts:
              counts[favorite] += 1
          else:
              counts[favorite] = 1

  # Print counts
  for favorite in sorted(counts):
      print(f"{favorite}: {counts[favorite]}")
  ```

  Notice the `sorted(counts)` at the bottom of the code. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites7.py?download).
* If you look at the parameters for the `sorted` function in the Python documentation, you will find it has many built-in parameters. You can leverage some of these built-in parameters as follows:

  ```py
  # Sorts favorites by value using .get

  import csv

  # Open CSV file
  with open("favorites.csv", "r") as file:

      # Create DictReader
      reader = csv.DictReader(file)

      # Counts
      counts = {}

      # Iterate over CSV file, counting favorites
      for row in reader:
          favorite = row["language"]
          if favorite in counts:
              counts[favorite] += 1
          else:
              counts[favorite] = 1

  # Print counts
  for favorite in sorted(counts, key=counts.get, reverse=True):
      print(f"{favorite}: {counts[favorite]}")
  ```

  Notice the arguments passed to `sorted`. The `key` argument allows you to tell Python the method you wish to use to sort items. In this case, `counts.get` is used to sort by the values. `reverse=True` tells `sorted` to sort from largest to smallest. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites8.py?download).
* You can learn more about [sorted](https://docs.python.org/3/howto/sorting.html) in the [Python Documentation](https://docs.python.org/3/howto/sorting.html).

<a id="relational-databases"></a>

#### Relational Databases

* Google, X, and Meta all use relational databases to store their information at scale.
* Relational databases store data in rows and columns in structures called *tables*.
* SQL allows for four types of commands:

  ```
    Create 
    Read
    Update
    Delete
  ```
* These four operations are affectionately called *CRUD*.
* We can create a database with the SQL syntax `CREATE TABLE table (column type, ...);`. But where do you run this command?
* `sqlite3` is a type of SQL database that has the core features required for this course.
* We can create a SQL database at the terminal by typing `sqlite3 favorites.db`. Upon being prompted, we will agree that we want to create `favorites.db` by pressing `y`.
* You will notice a different prompt as we are now using a program called `sqlite`.
* We can put `sqlite` into `csv` mode by typing `.mode csv`. Then, we can import our data from our `csv` file by typing `.import favorites.csv favorites`. It seems that nothing has happened!
* We can type `.schema` to see the structure of the database.
* You can read items from a table using the syntax `SELECT columns FROM table`.
* For example, you can type `SELECT * FROM favorites;` which will print every row in `favorites`.
* You can get a subset of the data using the command `SELECT language FROM favorites;`.
* SQL supports many commands to access data, including:

  ```
    AVG
    COUNT
    DISTINCT
    LOWER
    MAX
    MIN
    UPPER
  ```
* For example, you can type `SELECT COUNT(*) FROM favorites;`. Further, you can type `SELECT DISTINCT language FROM favorites;` to get a list of the individual languages within the database. You could even type `SELECT COUNT(DISTINCT language) FROM favorites;` to get a count of those.
* SQL offers additional commands we can utilize in our queries:

  ```sql
    WHERE       -- adding a Boolean expression to filter our data
    LIKE        -- filtering responses more loosely
    ORDER BY    -- ordering responses
    LIMIT       -- limiting the number of responses
    GROUP BY    -- grouping responses together
  ```

  Notice that we use `--` to write a comment in SQL.

<a id="select"></a>

#### SELECT

* For example, we can execute `SELECT COUNT(*) FROM favorites WHERE language = 'C';`. A count is presented.
* Further, we could type `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Hello, World';`. Notice how the `AND` is utilized to narrow our results.
* Similarly, we could execute `SELECT language, COUNT(*) FROM favorites GROUP BY language;`. This would offer a temporary table that would show the language and count.
* We could improve this by typing `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);`. This will order the resulting table by the `count`.
* Likewise, we could execute `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND (problem = 'Hello, World' OR problem = 'Hello, It''s Me');`. Do notice that there are two `''` marks to allow the use of single quotes in a way that does not confuse SQL.
* Further, we could execute `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem LIKE 'Hello, %';` to find any problems that start with `Hello,`  (including a space).
* We can order the output as follows: `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC;`.
* We can even create aliases, like variables in our queries: `SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC;`.
* Finally, we can limit our output to 1 or more values: `SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC LIMIT 1;`.
* Notice, by convention, SQL keywords are often typed in caps.

<a id="insert"></a>

#### INSERT

* We can also `INSERT` into a SQL database utilizing the form `INSERT INTO table (column...) VALUES(value, ...);`.
* We can execute `INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');`.
* You can verify the addition of this favorite by executing `SELECT * FROM favorites;`.

<a id="delete"></a>

#### DELETE

* `DELETE` allows you to delete parts of your data. For example, you could `DELETE FROM favorites WHERE Timestamp IS NULL;`. This deletes any record where the `Timestamp` is `NULL`.

<a id="update"></a>

#### UPDATE

* We can also utilize the `UPDATE` command to update your data.
* For example, you can execute `UPDATE favorites SET language = 'SQL', problem = 'Fiftyville';`. This will result in updating all the rows.
* Notice that these queries have immense power. Accordingly, in the real-world setting, you should consider who has permissions to execute certain commands and if you have backups available!

<a id="imdb"></a>

#### IMDb

* We can imagine a database that we might want to create to catalog various TV shows. We could create a spreadsheet with columns like `title`, `star`, `star`, `star`, `star`, and more stars. A problem with this approach is that it has a lot of wasted space. Some shows may have one star. Others may have dozens.
* We could separate our database into multiple sheets. We could have a `shows` sheet, a `stars` sheet, and a `people` sheet. On the `people` sheet, each person could have a unique `id`. On the `shows` sheet, each show could have a unique `id` too. On a third sheet called `stars` we could relate people to shows by having a `show_id` and `person_id`. While this is an improvement, this is not an ideal database.
* IMDb offers a database of people, shows, writers, stars, genres, and ratings. Each of these tables is related to one another as follows:

  ![six boxes that represent various sql tables arrows are drawn to each showing their many relationships with one another](https://cs50.harvard.edu/x/notes/7/cs50Week7Slide025.png "imdb relationships")
* After downloading [`shows.db`](https://cdn.cs50.net/2025/fall/lectures/7/src7/imdb/shows.db?download), you can execute `sqlite3 shows.db` in your terminal window.
* Let’s zero in on the relationship between two tables within the database called `shows` and `ratings`. The relationship between these two tables can be illustrated as follows:

  ![two boxes one called shows and the other called ratings](https://cs50.harvard.edu/x/notes/7/cs50Week7Slide032.png "imdb shows and ratings")
* To illustrate the relationship between these tables, we could execute the following command: `SELECT * FROM ratings LIMIT 10;`. Examining the output, we could execute `SELECT * FROM shows LIMIT 10;`.
* Examining `shows` and `ratings`, we can see these have a one-to-one relationship: One show has one rating.
* To understand the database, upon executing `.schema` you will find not only each of the tables but the individual fields inside each of these tables.
* More specifically, you could execute `.schema shows` to understand the fields inside `shows`. You can also execute `.schema ratings` to see the fields inside `ratings`.
* A reference to the show’s id exists in all tables. In the `shows` table, it is simply called `id`. This common field among all the tables is called a *key*. Primary keys are used to identify a unique record in a table. *Foreign keys* are used to build relationships between tables by pointing to the primary key in another table. You can see in the schema of `ratings` that `show_id` is a foreign key that references `id` in `shows`.
* By storing data in a relational database, as above, data can be more efficiently stored.
* In *sqlite*, we have five data types, including:

  ```sql
    BLOB       -- binary large objects that are groups of ones and zeros
    INTEGER    -- an integer
    NUMERIC    -- for numbers that are formatted specially like dates
    REAL       -- like a float
    TEXT       -- for strings and the like
  ```
* Additionally, columns can be set to add special constraints:

  ```
    NOT NULL
    UNIQUE
  ```
* We can further play with this data to understand these relationships. Execute `SELECT * FROM ratings;`. There are a lot of ratings!
* We can further limit this data down by executing `SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10;`. From this query, you can see that there are 10 shows presented. However, we don’t know what show each `show_id` represents.
* You can discover what shows these are by executing `SELECT * FROM shows WHERE id = 626124;`
* We can refine our query to be more efficient by executing:

  ```sql
  SELECT title
  FROM shows
  WHERE id IN (
      SELECT show_id
      FROM ratings
      WHERE rating >= 6.0
      LIMIT 10
  );
  ```

  Notice that this query nests together two queries. An inner query is used by an outer query.

<a id="joins"></a>

#### `JOIN`s

* We are pulling data from `shows` and `ratings`. Notice how both `shows` and `ratings` have an `id` in common.
* How could we combine tables temporarily? Tables could be joined together using the `JOIN` command.
* Execute the following command:

  ```sql
  SELECT * FROM shows
    JOIN ratings ON shows.id = ratings.show_id
    WHERE rating >= 6.0
    LIMIT 10;
  ```

  Notice this results in a wider table than we have previously seen.
* Where the previous queries have illustrated the *one-to-one* relationship between these keys, let’s examine some *one-to-many* relationships. Focusing on the `genres` table, execute the following:

  ```sql
  SELECT * FROM genres
  LIMIT 10;
  ```

  Notice how this provides us a sense of the raw data. You might notice that one show has three values. This is a one-to-many relationship.
* We can learn more about the `genres` table by typing `.schema genres`.
* Execute the following command to learn more about the various comedies in the database:

  ```sql
  SELECT title FROM shows
  WHERE id IN (
    SELECT show_id FROM genres
    WHERE genre = 'Comedy'
    LIMIT 10
  );
  ```

  Notice how this produces a list of comedies, including *Catweazle*.
* We can learn more about Catweazle by joining various tables:

  ```sql
  SELECT * FROM shows
  JOIN genres
  ON shows.id = genres.show_id
  WHERE id = 63881;
  ```

  Notice that this results in a temporary table. It is fine to have a duplicate table. Further, notice that Catweazle (one title) is assigned *many* genres, including adventure, comedy, and family.
* In contrast to one-to-one and one-to-many relationships, there are *many-to-many* relationships. For example, many people could appear in many shows!
* We can learn more about the show *The Office* and the actors in that show by executing the following command:

  ```sql
  SELECT name FROM people WHERE id IN 
      (SELECT person_id FROM stars WHERE show_id = 
          (SELECT id FROM shows WHERE title = 'The Office' AND year = 2005));
  ```

  Notice that this results in a table that includes the names of various stars through nested queries.
* We can find all the shows in which Steve Carell starred:

  ```sql
  SELECT title FROM shows WHERE id IN 
      (SELECT show_id FROM stars WHERE person_id = 
          (SELECT id FROM people WHERE name = 'Steve Carell'));
  ```

  This results in a list of titles of shows wherein Steve Carell starred.
* This could be expressed as a `JOIN` as:

  ```sql
  SELECT title FROM shows
  JOIN stars ON shows.id = stars.show_id
  JOIN people ON stars.person_id = people.id
  WHERE name = 'Steve Carell';
  ```
* This could also be expressed in this way:

  ```sql
  SELECT title FROM shows, stars, people 
  WHERE shows.id = stars.show_id
  AND people.id = stars.person_id
  AND name = 'Steve Carell';
  ```
* The wildcard `%` operator can be used to find all people whose names start with `Steve C` by employing the following syntax: `SELECT * FROM people WHERE name LIKE 'Steve C%';`.

<a id="indexes"></a>

#### Indexes

* While relational databases have the ability to be faster and more robust than utilizing a `CSV` file, data can be optimized within a table using *indexes*.
* Indexes can be utilized to speed up our queries.
* We can track the speed of our queries by executing `.timer on` in `sqlite3`.
* To understand how indexes can speed up our queries, run the following: `SELECT * FROM shows WHERE title = 'The Office';` Notice the time that displays after the query executes.
* Then, we can create an index with the syntax `CREATE INDEX title_index ON shows (title);`. This tells `sqlite3` to create an index and perform some special under-the-hood optimization relating to this column `title`.
* This will create a data structure called a *B Tree*, a data structure that looks similar to a binary tree. However, unlike a binary tree, there can be more than two child nodes.

  ![one node at the top from which come four children and below that there are three children coming from one of the nodes and two from another two from another and three from another](https://cs50.harvard.edu/x/notes/7/cs50Week7Slide039.png "b tree")
* Further, we can create indexes as follows:

  ```sql
  CREATE INDEX name_index ON people (name);
  CREATE INDEX person_index ON stars (person_id);
  ```
* Run the query and you will notice that the query runs much more quickly!

  ```sql
  SELECT title FROM shows WHERE id IN 
      (SELECT show_id FROM stars WHERE person_id = 
          (SELECT id FROM people WHERE name = 'Steve Carell'));
  ```
* Unfortunately, indexing all columns would result in utilizing more storage space. Therefore, there is a tradeoff for enhanced speed.

<a id="using-sql-in-python"></a>

#### Using SQL in Python

* To assist in working with SQL in this course, the CS50 Library can be utilized as follows in your code:

  ```py
  from cs50 import SQL
  ```
* Similar to previous uses of the CS50 Library, this library will assist with the complicated steps of utilizing SQL within your Python code.
* You can read more about the CS50 Library’s SQL functionality in the [documentation](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL).
* Using our new knowledge, we can now leverage Python alongside SQL.
* Modify your code for `favorites.py` as follows:

  ```py
  # Searches database for popularity of a problem

  from cs50 import SQL

  # Open database
  db = SQL("sqlite:///favorites.db")

  # Prompt user for favorite
  favorite = input("Favorite: ")

  # Search for title
  rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

  # Get first (and only) row
  row = rows[0]

  # Print popularity
  print(row["n"])
  ```

  Notice that `db = SQL("sqlite:///favorites.db")` provides Python the location of the database file. Then, the line that begins with `rows` executes SQL commands utilizing `db.execute`. Indeed, this command passes the syntax within the quotation marks to the `db.execute` function. We can issue any SQL command using this syntax. Further, notice that `rows` is returned as a list of dictionaries. In this case, there is only one result, one row, returned to the rows list as a dictionary. You can download this code [here](https://cdn.cs50.net/2025/fall/lectures/7/src7/favorites/favorites10.py?download).

<a id="race-conditions"></a>

#### Race Conditions

* Utilization of SQL can sometimes result in some problems.
* You can imagine a case where multiple users could be accessing the same database and executing commands at the same time.
* This could result in glitches where code is interrupted by other people’s actions. This could result in a loss of data.
* Built-in SQL features such as `BEGIN TRANSACTION`, `COMMIT`, and `ROLLBACK` help avoid some of these race condition problems.

<a id="sql-injection-attacks"></a>

#### SQL Injection Attacks

* Now, still considering the code above, you might be wondering what the `?` question marks do above. One of the problems that can arise in real-world applications of SQL is what is called an *injection attack*. An injection attack is where a malicious actor could input malicious SQL code.
* For example, consider a login screen as follows:

  ![login screen with username and password fields](https://cs50.harvard.edu/x/notes/7/cs50Week7Slide051.png "login screen")
* Without the proper protections in our own code, a bad actor could run malicious code. Consider the following:

  ```py
  rows = db.execute("SELECT COUNT(*) FROM users WHERE username = ? AND password = ?", username, password)
  ```

  Notice that because the `?` is in place, validation can be run on `username` and `password` before they are blindly accepted by the query.
* Never blindly trust the user’s input.
* Utilizing the CS50 Library, the library will *sanitize* and remove any potentially malicious characters.

<a id="summing-up"></a>

#### Summing Up

In this lesson, you learned more syntax related to Python. Further, you learned how to integrate this knowledge with data in the form of flat-file and relational databases. Finally, you learned about *SQL*. Specifically, we discussed…

* Flat-file databases
* Relational databases
* SQL commands such as `SELECT`, `CREATE`, `INSERT`, `DELETE`, and `UPDATE`.
* Primary and foreign keys
* `JOIN`s
* Indexes
* Using SQL in Python
* Race conditions
* SQL injection attacks

See you next time!

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
**Order of topics** = heading order of the notes (table of contents on the source page).
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** مرور و درک عمیق مفاهیم درس این هفته؛ توانایی توضیح هر بخش جزوه با مثال خود دانشجو.

## 4. Relationships
- **Parent:** [Week 7 — SQL](week.md) (`week-7`)
- **Backlinks (auto-generated):**
  - [SQL and Relational Databases](../../concepts/sql-basics.md) (`concept-sql-basics`)
  - [SQL Injection Attacks and Race Conditions](../../concepts/sql-injection-and-race-conditions.md) (`concept-sql-injection-and-race-conditions`)
  - [Primary Keys, Foreign Keys and JOINs](../../concepts/sql-joins-and-keys.md) (`concept-sql-joins-and-keys`)
  - [Favorites — Practice](practice/favorites.md) (`practice-7-favorites`)
  - [Hall of Prophecy — Practice](practice/prophecy.md) (`practice-7-prophecy`)
  - [Fiftyville — Problem Set 7](psets/fiftyville.md) (`pset-7-fiftyville`)
  - [Movies — Problem Set 7](psets/movies.md) (`pset-7-movies`)
  - [Songs — Problem Set 7](psets/songs.md) (`pset-7-songs`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
SQL و پایگاه داده‌ی رابطه‌ای؛ طراحی جدول، JOIN و خطرات SQL injection.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.

### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/7/ — retrieved 2026-10-18T05:10:37+03:30, sha256 `a8e4860d45473402…`
- https://cs50.harvard.edu/x/weeks/7/ — retrieved 2026-10-18T05:10:02+03:30, sha256 `aea0b1dff42dbb65…`
- https://cdn.cs50.net/2025/fall/lectures/7/lang/en/lecture7.txt — retrieved 2026-10-18T05:40:31+03:30, sha256 `51e779c2190c8014…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
