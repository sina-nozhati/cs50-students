---
id: pset-9-birthdays
type: pset
title: Birthdays — Problem Set 9
week: 9
parent: pset-9
children: []
prerequisites:
- week-9-lecture
related:
- concept-flask-and-routes
- concept-forms-get-post
- concept-html-and-css
- concept-sql-basics
source_urls:
- https://cs50.harvard.edu/x/psets/9/birthdays/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:48+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python/Flask + SQL + HTML/Jinja
tags:
- birthdays
- flask-routes
- get-vs-post
- html-forms
- jinja-templates
- pset
- sql-insert-select
checksum: sha256:2c3a3388128dfdb79983274f1d9d10901b6666e0f582b87b532daf0443ddbb8a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Birthdays — Problem Set 9

## 1. Source metadata
- **Title:** Birthdays — Problem Set 9
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/9/birthdays/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:48+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/9/birthdays/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="birthdays"></a>

### Birthdays

![screenshot of birthdays website](https://cs50.harvard.edu/x/psets/9/birthdays/birthdays.png)

<a id="problem-to-solve"></a>

#### Problem to Solve

Create a web application to keep track of friends’ birthdays.

<a id="getting-started"></a>

#### Getting Started

> **Download the distribution code** *(collapsible block on the source page)*
>
> Open [cs50.dev](https://cs50.dev/).
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
> wget https://cdn.cs50.net/2026/x/psets/9/birthdays.zip
> ```
>
> followed by Enter in order to download a ZIP called `birthdays.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
>
> Now execute
>
> ```
> unzip birthdays.zip
> ```
>
> to create a folder called `birthdays`. You no longer need the ZIP file, so you can execute
>
> ```
> rm birthdays.zip
> ```
>
> and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.
>
> Now type
>
> ```
> cd birthdays
> ```
>
> followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.
>
> ```
> birthdays/ $
> ```
>
> If all was successful, you should execute
>
> ```
> ls
> ```
>
> and you should see the following files and folders:
>
> ```
> app.py  birthdays.db  static/  templates/
> ```
>
> If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

<a id="understanding"></a>

#### Understanding

In `app.py`, you’ll find the start of a Flask web application. The application has one route (`/`) that accepts both `POST` requests (after the `if`) and `GET` requests (after the `else`). Currently, when the `/` route is requested via `GET`, the `index.html` template is rendered. When the `/` route is requested via `POST`, the user is redirected back to `/` via `GET`.

`birthdays.db` is a SQLite database with one table, `birthdays`, that has four columns: `id`, `name`, `month`, and `day`. There are a few rows already in this table, though ultimately your web application will support the ability to insert rows into this table!

In the `static` directory is a `styles.css` file containing the CSS code for this web application. No need to edit this file, though you’re welcome to if you’d like!

In the `templates` directory is an `index.html` file that will be rendered when the user views your web application.

<a id="implementation-details"></a>

#### Implementation Details

Complete the implementation of a web application to let users store and keep track of birthdays.

* When the `/` route is requested via `GET`, your web application should display, in a table, all of the people in your database along with their birthdays.
  * First, in `app.py`, add logic in your `GET` request handling to query the `birthdays.db` database for all birthdays. Pass all of that data to your `index.html` template.
  * Then, in `index.html`, add logic to render each birthday as a row in the table. Each row should have two columns: one column for the person’s name and another column for the person’s birthday.
* When the `/` route is requested via `POST`, your web application should add a new birthday to your database and then re-render the index page.
  * First, in `index.html`, add an HTML form. The form should let users type in a name, a birthday month, and a birthday day. Be sure the form submits to `/` (its “action”) with a method of `post`.
  * Then, in `app.py`, add logic in your `POST` request handling to `INSERT` a new row into the `birthdays` table based on the data supplied by the user.

Optionally, you may also:

* Add the ability to delete and/or edit birthday entries.
* Add any additional features of your choosing!

<a id="hints"></a>

#### Hints

> **Create a form via which users can submit birthdays** *(collapsible block on the source page)*
>
> In `index.html`, notice the following TODO:
>
> ```html
> <!-- TODO: Create a form for users to submit a name, a month, and a day -->
> ```
>
> Recall that, to create a form, you can use the `form` HTML element. You can create a `form` HTML element with the following opening and closing tags:
>
> ```html
> <form>
> </form>
> ```
>
> Of course, a form still needs input fields (and a button via which the user can submit the form!). Recall that HTML `input` elements create, among other things, input boxes within a form. You can specify their `type` attribute to allow them to accept `text` or `number`s. Also give the `input` elements a `name` attribute so you can differentiate them.
>
> ```html
> <form>
>     <input name="name" type="text">
>     <input name="month" type="number">
>     <input name="day" type="number">
> </form>
> ```
>
> Your form might benefit from a button the user could click to submit their data. Add an `input` element of type `submit`, which will allow the user to do just that. If you’d like the button itself to have explanatory text, try setting the `value` attribute.
>
> ```html
> <form>
>     <input name="name" type="text">
>     <input name="month" type="number">
>     <input name="day" type="number">
>     <input type="submit" value="Add Birthday">
> </form>
> ```
>
> Where will the user’s data be submitted? Currently, nowhere! Recall that you can specify a form’s `action` attribute to dictate which route should be requested after the form is submitted. The form data will be submitted along with the resulting request. The `method` attribute specifies which HTTP request method to use when submitting the form.
>
> ```html
> <form action="/" method="post">
>     <input name="name" type="text">
>     <input name="month" type="number">
>     <input name="day" type="number">
>     <input type="submit" value="Add Birthday">
> </form>
> ```
>
> With that, your form should be perfectly functional, though it could still be improved! Consider adding `placeholder` values to spruce things up a bit:
>
> ```html
> <form action="/" method="post">
>     <input name="name" placeholder="Name" type="text">
>     <input name="month" placeholder="Month" type="number">
>     <input name="day" placeholder="Day" type="number">
>     <input type="submit" value="Add Birthday">
> </form>
> ```
>
> And consider adding some *client-side validation*, to ensure the user cooperates with the intent of your form. For example, an `input` field of type `number` can also have a `min` and `max` attribute specified, which determine the minimum and maximum value a user can enter.
>
> ```html
> <form action="/" method="post">
>     <input name="name" placeholder="Name" type="text">
>     <input name="month" placeholder="Month" type="number" min="1" max="12">
>     <input name="day" placeholder="Day" type="number" min="1" max="31">
>     <input type="submit" value="Add Birthday">
> </form>
> ```

> **Add a user's form submission to the database** *(collapsible block on the source page)*
>
> In `app.py`, notice the following TODO:
>
> ```py
> # TODO: Add the user's entry into the database
> ```
>
> Recall that Flask has some handy methods to access form data submitted via `POST`! In particular:
>
> ```py
> # Access form data
> request.form.get(NAME)
> ```
>
> where `NAME` refers to the `name` attribute of the particular `input` element with submitted data. If your `input` elements were named `name`, `month`, and `day`, you could access (and store!) their values respectively with the following:
>
> ```py
> # Access form data
> name = request.form.get("name")
> month = request.form.get("month")
> day = request.form.get("day")
> ```
>
> Now the values submitted by the user in the `name`, `month`, and `day` input elements are available to you as Python variables.
>
> The next step is to add these values to your database! Thanks to this particular line
>
> ```py
> db = SQL("sqlite:///birthdays.db")
> ```
>
> `app.py` has already established a connection to `birthdays.db` under the name `db`. You can now execute SQL queries by calling `db.execute` with a valid SQL query. If you wanted to add Carter’s birthday on January 1st, you might run the following SQL statement:
>
> ```sql
> INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);
> ```
>
> Configure `app.py` to run that same query, but with placeholders for the values to insert, as follows:
>
> ```py
> # Access form data
> name = request.form.get("name")
> month = request.form.get("month")
> day = request.form.get("day")
>
> # Insert data into database
> db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
> ```
>
> And that should do it! Try submitting the form, opening `birthdays.db`, and using a `SELECT` query to view the contents of the `birthdays` table. You should see the submitted form data available to you.
>
> As you create more advanced applications, you’ll also want to add *server-side validation*: that is, a way to check whether the user’s data is valid *before* doing anything else! One of the first validations you might make is whether the user submitted any data at all! Should you try to retrieve form data with `request.form.get` where the user didn’t submit any, `request.form.get` will return an empty string. You can check for this value in Python as follows:
>
> ```py
> # Access form data
> name = request.form.get("name")
> if not name:
>     return redirect("/")
>
> month = request.form.get("month")
> if not month:
>     return redirect("/")
>
> day = request.form.get("day")
> if not day:
>     return redirect("/")
>
> # Insert data into database
> db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
> ```
>
> Now, you won’t insert a row until you’re sure the user has provided all the data you need.
>
> A few more things could still go wrong! What if the user doesn’t, in fact, provide a numeric value for `month` or `day`? One way to check is to `try` to convert the value to an integer with `int` and, if the conversion fails, to redirect the user back to the homepage.
>
> ```py
> # Access form data
> name = request.form.get("name")
> if not name:
>     return redirect("/")
>
> month = request.form.get("month")
> if not month:
>     return redirect("/")
> try:
>     month = int(month)
> except ValueError:
>     return redirect("/")
>
> day = request.form.get("day")
> if not day:
>     return redirect("/")
> try:
>     day = int(day)
> except ValueError:
>     return redirect("/")
>
> # Insert data into database
> db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
> ```
>
> And even if the user has entered a number, best to check it’s in the right range!
>
> ```py
> # Access form data
> name = request.form.get("name")
> if not name:
>     return redirect("/")
>
> month = request.form.get("month")
> if not month:
>     return redirect("/")
> try:
>     month = int(month)
> except ValueError:
>     return redirect("/")
> if month < 1 or month > 12:
>     return redirect("/")
>
> day = request.form.get("day")
> if not day:
>     return redirect("/")
> try:
>     day = int(day)
> except ValueError:
>     return redirect("/")
> if day < 1 or day > 31:
>     return redirect("/")
>
> # Insert data into database
> db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
> ```

> **Render birthdays in birthdays.db** *(collapsible block on the source page)*
>
> Once a user can submit birthdays and store them in `birthdays.db`, your next task is to ensure those birthdays are rendered in `index.html`.
>
> First, you’ll need to retrieve all birthdays from `birthdays.db`. You could so with the SQL query:
>
> ```sql
> SELECT * FROM birthdays;
> ```
>
> See the following TODO in `app.py`:
>
> ```py
> # TODO: Display the entries in the database on index.html
> ```
>
> Consider configuring `app.py` to run this SQL query each time the page is loaded with a `GET` request:
>
> ```py
> # Query for all birthdays
> birthdays = db.execute("SELECT * FROM birthdays")
> ```
>
> Now, all birthdays in the `birthdays` table of `birthdays.db` are available to you in a Python variable named `birthdays`. In particular, the results of the SQL query are stored as a list of dictionaries. Each dictionary represents one row returned by the query, and each key in the dictionary corresponds to a column name of the `birthdays` table (i.e., “name”, “month”, and “day”).
>
> To render these birthdays in `index.html`, you can rely on Flask’s `render_template` function. You can specify that `index.html` should be rendered with the `birthdays` variable by specifying a keyword argument, also called `birthdays`, and setting it equal to the `birthdays` variable you just recently created.
>
> ```py
> # Query for all birthdays
> birthdays = db.execute("SELECT * FROM birthdays")
>
> # Render birthdays page
> return render_template("index.html", birthdays=birthdays)
> ```
>
> To be clear, the name on the left-hand side of the `=`, `birthdays`, is the name under which you can access the birthdays data within `index.html` itself.
>
> Now that `index.html` is being rendered with access to the birthdays data, you can use Jinja to render the data properly. Jinja, like Python, can loop through elements of a list. And Jinja, like Python, can access elements a dictionary by their keys. In this case, the Jinja syntax to do so is the name of the dictionary, followed by a `.`, then the name of the key to access.
>
> ```html
> {% for birthday in birthdays %}
>     <tr>
>         <td>{{ birthday.name }}</td>
>         <td>{{ birthday.month }}/{{ birthday.day }}</td>
>     </tr>
> {% endfor %}
> ```
>
> And that’s it! Try reloading the page to see the birthdays rendered.

<a id="walkthrough"></a>

##### Walkthrough

This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!

[Embedded video: https://video.cs50.io/HXwvj8x1Fcs](https://video.cs50.io/HXwvj8x1Fcs)

> **Not sure how to solve?** *(collapsible block on the source page)*
>

<a id="testing"></a>

##### Testing

No `check50` for this problem set! But be sure to test your web application by adding some birthdays and ensuring that the data appears in your table as expected.

Run `flask run` in your terminal while in your `birthdays` directory to start a web server that serves your Flask application.

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/birthdays
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/9/birthdays.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `birthdays/birthdays.db` | 8192 | no — binary/media/data file (inventory only) |
| `birthdays/app.py` | 899 | [yes](birthdays-distribution/files/birthdays/app.py) |
| `birthdays/static/styles.css` | 1661 | [yes](birthdays-distribution/files/birthdays/static/styles.css) |
| `birthdays/templates/index.html` | 1107 | [yes](birthdays-distribution/files/birthdays/templates/index.html) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python/Flask + SQL + HTML/Jinja
- Folder: `birthdays`; files shown on the page: `app.py`, `birthdays.db`, `index.html`, `styles.css`
- check50: No check50 (stated)
- style50: not stated
- submit50: `cs50/problems/2026/x/birthdays`
- Page sections (order on source): Problem to Solve, Getting Started, Understanding, Implementation Details, Hints, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Flask routes، GET vs POST، Jinja templates، SQL INSERT/SELECT، HTML forms.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Complete a small Flask app that stores birthdays in birthdays.db. On GET /, query all rows and render them in a table in index.html. On POST /, insert a new name, month and day from a form, then redirect. There is no check50; test by running flask run.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 9](README.md) (`pset-9`)
- **Prerequisites (generated):** [Week 9 — Lecture notes (Flask)](../lecture.md) (`week-9-lecture`)
- **Related:**
  - [Flask, Routes and Templates (Jinja)](../../../concepts/flask-and-routes.md) (`concept-flask-and-routes`)
  - [Forms, GET and POST](../../../concepts/forms-get-post.md) (`concept-forms-get-post`)
  - [HTML and CSS](../../../concepts/html-and-css.md) (`concept-html-and-css`)
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
اولین برنامه‌ی Flask با پایگاه داده: GET و POST، فرم و قالب Jinja.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. مسیر درخواست را دنبال کن: فرم → route → پایگاه داده → قالب.
2. برای GET و POST در یک route چه کار متفاوتی انجام می‌شود؟
3. داده‌ی ورودی کاربر را قبل از درج در پایگاه داده بررسی کن و از placeholder استفاده کن.

### اشتباه‌های رایج (مفهومی)
- ساختن SQL با الحاق رشته
- نمایش ندادن داده‌های تازه پس از درج

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.
- برای بررسی درستی، دانشجو را به اجرای (در صفحه ذکر نشده) و `style50` (در صورت ذکر در صفحه) راهنمایی کن؛ خروجی آن‌ها را تفسیر کن، نه اینکه کد درست را بنویسی.
- این مسئله بخشی از نمره‌ی گواهی است؛ حداقل ۷۰٪ لازم است (مطابق صفحه‌ی گواهی).

### ایده‌های پیاده‌سازی در سایت
- رکورد `Assignment` با فیلدهای: عنوان، هفته، لینک رسمی، نام فایل/پوشه، دستور check50/submit50، وضعیت اجباری/اختیاری و گروه انتخابی (choice group).
- نمایش «نردبان راهنمایی» بالا با باز شدن مرحله‌به‌مرحله و ثبت اینکه دانشجو چند راهنمایی دیده است.
- لینک مستقیم به جزوه‌ی هفته و shortهای مرتبط از بخش «ارتباطات».


## 6. References, review, gaps
- https://cs50.harvard.edu/x/psets/9/birthdays/ — retrieved 2026-10-18T05:11:48+03:30, sha256 `2c3a3388128dfdb7…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
