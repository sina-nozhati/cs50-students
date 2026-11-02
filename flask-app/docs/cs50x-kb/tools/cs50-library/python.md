---
id: tool-cs50-library-python
type: tool
title: CS50 Library for Python
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/libraries/cs50/python/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:37+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- cs50-library-python
- tool
checksum: sha256:b1227aec6ff4eb0cadf562663ad2abf9358b9ba7f3972bea097da1224443ed34
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# CS50 Library for Python

## 1. Source metadata
- **Title:** CS50 Library for Python
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/libraries/cs50/python/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/libraries/cs50/python/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="cs50-library-for-python"></a>

### CS50 Library for Python

<a id="installation"></a>

#### Installation

```
$ pip3 install cs50
```

<a id="usage"></a>

#### Usage

Note

To use these functions, be sure to include `import cs50` atop your file.

cs50.get_float(*prompt*)
:   Parameters
    :   **prompt** – the `str` with which to prompt the user for input

    Returns
    :   the `float` equivalent to the line read from stdin as precisely as possible, or None on error

    Prompts user for a line of text from standard input and returns the equivalent `float`;
    if text does not represent a floating-point value or would cause overflow or underflow, user is reprompted.

    Example usage:

    ```
    f = get_float("Input a floating-point number: ")
    ```

cs50.get_int(*prompt*)
:   Parameters
    :   **prompt** – the `str` with which to prompt the user for input

    Returns
    :   the `int` equivalent to the line read from stdin, or None on error

    Prompts user for a line of text from standard input and returns the equivalent `int`;
    if text does not represent an integer, user is reprompted.

    Example usage:

    ```
    f = get_int("Input an integer: ")
    ```

cs50.get_string(*prompt*)
:   Parameters
    :   **prompt** – the `str` with which to prompt the user for input

    Returns
    :   the read line as a string sans line endings, or None on EOF.

    Prompts user for a line of text from standard input and returns it as a `str`,
    sans trailing line ending. Supports CR (`\r`), LF (`\n`), and CRLF (`\r\n`) as line
    endings.

    Example usage:

    ```
    s = get_string("Input a string: ")
    ```

cs50.SQL(*url*)
:   Parameters
    :   **url** – a `str` that indicates database dialect and connection arguments

    Returns
    :   a [`cs50.SQL`](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL "cs50.SQL") object that represents a connection to a database

    Example usage:

    ```
    db = cs50.SQL("sqlite:///file.db")  # For SQLite, file.db must exist
    db = cs50.SQL("mysql://username:password@host:port/database")  # For MySQL
    db = cs50.SQL("postgres://username:password@host:port/database")  # For PostgreSQL
    ```

cs50.SQL.execute(*sql*, **args*, ***kwargs*)
:   Parameters
    :   * **sql** – a `str` that represents a single SQL statement, possibly with [parameter markers](https://www.python.org/dev/peps/pep-0249/#paramstyle), with or without a trailing semicolon
        * ***args** – zero or more positional arguments with which any parameter markers should be substituted
        * ****kwargs** – zero or more named arguments with which any parameter markers should be substituted

    Any argument whose value is a `list` or `tuple` of other values is converted to a comma-separated list of those values, formatted for SQL’s `IN` operator. Any argument whose value is None is converted to NULL for SQL.

    Supported placeholders include question marks (qmark style) and named placeholders (named style).

    Returns
    :   * for `CREATE`, `True` on success or `False` on failure
        * for `DELETE`, the number of rows deleted
        * for `INSERT`, the primary key of a newly inserted row (or `None` if none)
        * for `SELECT`, a `list` of `dict` objects, each of which represents a row in the result set
        * for `UPDATE`, the number of rows updated
        * on integrity errors (as when a constraint is violated), a `ValueError` is raised
        * on other errors, a `RuntimeError` is raised

    Example usage:

    ```
    import cs50

    db = cs50.SQL("sqlite:///file.db")

    rows = db.execute("SELECT * FROM foo")

    rows = db.execute("SELECT * FROM foo WHERE bar = ? AND baz = ?", 1, 2)
    rows = db.execute("SELECT * FROM foo WHERE bar IN (?) AND baz IN (?)", [1, 2], [3, 4])

    rows = db.execute("SELECT * FROM foo WHERE bar = :bar AND baz = :baz", bar=1, baz=2)
    rows = db.execute("SELECT * FROM foo WHERE bar IN (:bar) AND baz IN (:baz)", bar=[1, 2], baz=[3, 4])

    id = db.execute("INSERT INTO foo (bar, baz) VALUES(?, ?)", 1, 2)
    id = db.execute("INSERT INTO foo (bar, baz) VALUES(:bar, :baz)", bar=1, baz=2)

    n = db.execute("UPDATE foo SET bar = ?, baz = ?", 1, 2)
    n = db.execute("UPDATE foo SET bar = :bar, baz = :baz", bar=1, baz=2)

    n = db.execute("DELETE FROM foo WHERE bar = ? AND baz = ?", 1, 2)
    n = db.execute("DELETE FROM foo WHERE bar = :bar AND baz = :baz", bar=1, baz=2)
    ```

<a id="faqs"></a>

#### FAQs

<a id="how-can-i-use-with-like"></a>

##### How can I use `%` with `LIKE`?

If `s` is a `str`, you can prepend and/or append `%` to it as follows:

> ```
> rows = db.execute("SELECT * FROM foo WHERE bar LIKE ?", "%" + s + "%")
> ```

<a id="how-can-i-add-optional-clauses-to-a-query"></a>

##### How can I add optional clauses to a query?

Based on user input, you might want to include or not include some clauses in a query. For instance, you might want to include bar and baz in a query only if they have values, in which case the number of placeholders you have in your query might vary. You could thus construct your query dynamically by joining the clauses and unpacking the placeholders’ values as follows:

> ```
> query = "SELECT * FROM foo"
>
> clauses = []
> values = []
>
> if bar:
>     clauses.append("bar = ?")
>     values.append(bar)
> if baz:
>     clauses.append("baz = ?")
>     values.append(baz)
>
> if clauses:
>     query = query + " WHERE " + " AND ".join(clauses)
> rows = db.execute(query, *values)
> ```

The end result is equivalent to:

> ```
> rows = db.execute("SELECT * FROM foo WHERE bar = ? AND baz = ?", bar, baz)
> ```

But you don’t need to know in advance if bar and baz will have values.

<a id="how-come-i-can-t-use-parameter-markers-as-placeholders-for-tables-or-columns-names"></a>

##### How come I can’t use parameter markers as placeholders for tables’ or columns’ names?

Parameter markers (e.g., `?`) can only be used as placeholders for “literals” like integers and strings, not for “identifiers” like tables’ and columns’ names. If a user’s input will determine the table or column on which you execute a statement, you can use a format string (f-string) instead, but **you must validate the user’s input first, to ensure the table or column exists, lest you risk a SQL-injection attack**, as in the below:

> ```
> if column in ["foo", "bar", "baz"]:
>     rows = db.execute(f"SELECT * FROM {column}")
> ```

<a id="how-can-i-enable-logging-of-sql-statements"></a>

##### How can I enable logging of SQL statements?

By default, logging of SQL statements is disabled unless you have an environment variable called `FLASK_ENV`, the value of which is `development`, as is the case in [Visual Studio Code for CS50](https://cs50.readthedocs.io/code/). You can enable logging of SQL statements with code like:

> ```
> import logging
>
> logging.getLogger("cs50").disabled = False
> ```

Statements that succeed will be prefixed with `INFO`. Statements that fail will be prefixed with `ERROR`.

<a id="how-can-i-disable-logging-of-sql-statements"></a>

##### How can I disable logging of SQL statements?

To disable logging of SQL statements, even if you have an environment variable called `FLASK_ENV`, the value of which is `development`, as is the case in [Visual Studio Code for CS50](https://cs50.readthedocs.io/code/), you can use code like:

> ```
> import logging
>
> logging.getLogger("cs50").setLevel("CRITICAL")
> ```

<a id="troubleshooting"></a>

#### Troubleshooting

<a id="modulenotfounderror-no-module-named-sqlite3"></a>

##### ModuleNotFoundError: No module named ‘_sqlite3’

If on an `apt`-based system, try:

> ```
> apt install libsqlite3-dev
> ```

If on a `yum`-based system, try:

> ```
> yum install sqlite-devel
> ```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 tools (index)](../README.md) (`tools`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
مستند ابزار رسمی CS50؛ برای راهنمای فارسی نصب و استفاده و پاسخ‌گویی به سؤال‌های فنی دانشجویان.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.


### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.readthedocs.io/libraries/cs50/python/ — retrieved 2026-10-18T05:40:37+03:30, sha256 `b1227aec6ff4eb0c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
