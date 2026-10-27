---
id: practice-9-helloflask
type: practice
title: Hello, Flask — Practice
week: 9
parent: week-9
children: []
prerequisites:
- week-9-lecture
related:
- concept-flask-and-routes
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/helloflask/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:11+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- Python/Flask + HTML/Jinja
tags:
- flask
- hello-flask
- jinja-templates
- practice
- routes
checksum: sha256:d7a7e01ca6392a7d412bf7b9474bb3b45343659a7c33ef88804e5a449e90d2e8
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Hello, Flask — Practice

## 1. Source metadata
- **Title:** Hello, Flask — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/helloflask/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:11+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/helloflask/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="hello-flask"></a>

### Hello, Flask

<a id="learning-goals"></a>

#### Learning Goals

* Build a simple flask app to gain an understanding of how to use this framework
* Become familiar with Jinja, a templating language used with Flask

![FlaskLogo](https://cs50.harvard.edu/x/practice/helloflask/flask-logo.png)

<a id="background"></a>

#### Background

[Flask](https://flask.palletsprojects.com/), a [microframework](https://en.wikipedia.org/wiki/Microframework) used for web development, can be confusing when starting out. There are multiple files of different types, and they must reside in specific folders. In this problem, we’ll start with the absolute minimum—a single Python file. From there we will move on to create your first full-fledged web app!

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/9/helloflask.zip` followed by Enter in order to download a zip called `helloflask.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip helloflask.zip` to create a folder called `helloflask`.
5. You no longer need the ZIP file, so you can execute `rm helloflask.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

The most simple Flask app uses just one file, `app.py`. This will create an html page and say hello. Add the following into `app.py` to get started.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"
```

This bit of code starts by importing `Flask` from the `flask` library. Though we don’t need to get too far into the weeds here, `Flask` is what programmers call a “[class](https://cs50.harvard.edu/python/2022/notes/8/#classes)”. Suffice to say for now, it’s like a template for the application we’ll be building. The line `app = Flask(__name__)` tells Python to create a particular app, henceforth called “app”, from the template. To create the particular application, we give the `Flask` class the name of the current Python file (represented by `__name__`), which allows our application to find other files we might later add to it. In this case, the name of the file is also “app” for consistency.

The most mysterious line in the application you’ve written is probably the one where you wrote:

```python
@app.route("/")
```

This kind of function is called a decorator. Decorators allow you to take a basic function, like `app.route`, and extend its functionality with something custom: the function you write after the decorator. You can [read more](https://realpython.com/primer-on-python-decorators/) about decorators if you want, or you can just keep using them for now.

This line tells Flask that if an HTTP request comes in for “/”, the `index` function should be run. Note that, if we renamed the function to be `homepage`, this line would tell Flask that—every time it receives an HTTP request for “/”—it should run the `homepage` function.

Notice that the `index` function returns a piece of text, “Hello, World!”. This text is what Flask will render to the user when their request to the “/” route is complete. The returned text could be (and often is!) the text of an entire HTML file, which the browser then renders accordingly. But it’s just a piece of text for now, for brevity’s sake.

To run your app, type `flask run` into the terminal, and you will get a link to click, similar to when you run `http-server`. You’ve written a Flask app! Try returning different text, like `<h1>Hello, World!</h1>`. How does this change what you see?

<a id="templates"></a>

##### Templates

Instead of putting HTML code right into our Python programs, it’s best to move our HTML into separate files, to keep separate concerns separate. Since our app will likely include a number of similar HTML files, we can create one `layout.html` file which all our HTML files “extend”. “Extending” an HTML file means to keep all of the content of that HTML file while also adding some custom content, specific to a particular page.

By convention, Flask puts all HTML files inside of a `templates` folder. Inside the `helloflask` folder, make a folder called `templates` using `mkdir templates`. All your HTML files will go in this `templates` folder.

Inside `templates`, create a `layout.html` file that looks like this:

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>Hello, Flask</title>
    </head>
    <body>
        <h1>Hello, Flask</h1>
        {% block body %}{% endblock %}
    </body>
</html>
```

The `{% block body %}{% endblock %}` syntax comes from [Jinja](https://palletsprojects.com/p/jinja/), which is a “template engine” for Python. The line with `{% block body %}{% endblock %}` is what makes this a layout file. If another HTML file extends `layout.html` and defines a block called “body”, we’ll insert that block into this section of the `layout.html`. A layout file can contain as many blocks as you want. Just give each one a different name.

Now create `index.html` so that it extends the template `layout.html`, like this:

```html
{% extends "layout.html" %}

{% block body %}
    <p>Next we'll put a form here and get some POST action!</p>
{% endblock %}
```

Finally, we’ll go back to `app.py` to see these changes come to life. In the initial import, we’ll need a few more functions from Flask (as shown below). Then, replace the direct return of text with a call to Flask’s `render_template` function. The purpose of the `render_template` function is to preprocess `index.html` such that, when we give it to the browser, it also includes the HTML it “inherits” from `layout.html`.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

When you run your application now (type `flask run`!), you’ll get a little more out of your app. But it isn’t really interactive yet!

<a id="forms"></a>

##### Forms

HTML forms allow the user to enter data into input fields and send the data to the server, often using the POST method of the HTTP protocol. You can learn more about HTML Forms [here](https://www.w3schools.com/html/html_forms.asp).

Add a form to `index.html` so that it looks like this:

```html
{% extends "layout.html" %}

{% block body %}
    <form action="/" method="post">
        What is your favorite color?
        <select name="color">
            <option value="red">Harvard Crimson</option>
            <option value="blue">Yale Blue</option>
        </select>
        <button type="submit">Submit</button>
    </form>
{% endblock %}
```

Note that each form element has both a *name* and a *value*. The name an element is what we’ll use to refer to that element. Its value is the value submitted by the form. Each get passed into `app.py` for our use when the form is submitted.

Run your app, visit the `/` route, and submit the form. Oops! You should see the message “Method not allowed”. So we’ll first need to make sure Flask allows the use of the POST method on `/`.

<a id="post"></a>

##### POST

In `app.py`, we need to adjust our route to handle the POST request. Here is what our new `app.py` looks like.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("Form submitted!")
        color = request.form.get("color")
        return render_template("color.html", color=color)
```

This example has some logic in it: if the user submits a GET request, we’ll show them the basic `index.html` with a form to submit. If, though, they submit a POST request, we’ll do a few different things:

* `print` “Form submitted!” to the terminal, for debugging’s sake. We should later remove this once we’re satisfied our program works as intended.
* Store the *value* of the “color” input in a variable also called `color`, as via `color = request.form.get("color")`.
* Render a new HTML file, `color.html`, and pass the value of the `color` variable into the file under the very same name, `color`.

Let’s create `color.html` for our application to work:

```html
{% extends "layout.html" %}

{% block body %}
    <p style="color: {{ color }}">Your favorite color is {{ color }}.</p>
{% endblock %}
```

Notice how we can insert the value of `color` anywhere in our HTML we’d like—whether as text in a sentence, or as a placeholder for the value of some CSS property.

We’ll likely want to add some additional input validation, however, instead of simply trusting our users to send only the values “blue” or “red” via POST. What additional code could you add to ensure the colors we receive are valid colors?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

Your program should behave as per the examples above.

No `check50` for this one!

<a id="how-to-submit"></a>

#### How to Submit

No need to submit. This is a practice problem!

*Adapted from 27 Classrooms, by Mark Sobkowicz, Lincoln Sudbury Regional High School*

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/9/helloflask.zip

_No files inventoried._

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): Python/Flask + HTML/Jinja
- Folder: `helloflask`; files shown on the page: `app.py`, `color.html`, `index.html`, `layout.html`
- check50: No check50 (stated)
- style50: not stated
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Getting Started, Implementation Details, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم Flask، Jinja templates، routes.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Build a minimal Flask app from scratch, starting with a single Python file and growing it into templates (layout, index, color) with Jinja.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 9 — Flask](../week.md) (`week-9`)
- **Prerequisites (generated):** [Week 9 — Lecture notes (Flask)](../lecture.md) (`week-9-lecture`)
- **Related:**
  - [Flask, Routes and Templates (Jinja)](../../../concepts/flask-and-routes.md) (`concept-flask-and-routes`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین ساده‌ی Flask: route، فرم و قالب.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. مسیر داده را از فرم تا قالب دنبال کن.

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
- https://cs50.harvard.edu/x/practice/helloflask/ — retrieved 2026-10-18T05:11:11+03:30, sha256 `d7a7e01ca6392a7d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
