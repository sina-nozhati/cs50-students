---
id: concept-forms-get-post
type: concept
title: Forms, GET and POST
week: 9
parent: concepts
children: []
prerequisites: []
related:
- practice-4-bottomup
- pset-1-mario-more
- pset-1-me
- pset-5-speller
- pset-6-mario-more
- pset-9-birthdays
- week-8-lecture
- week-9-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/9/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:45+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- forms-get-post
checksum: sha256:97ceb6d0e8e004aac38fcd65227b3bcf1b99c37f2ff0b9bf7d0f83036d455ecb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Forms, GET and POST

## 1. Source metadata
- **Title:** Forms, GET and POST
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/9/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:45+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/9/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that this code defines app as the Flask application. Then, it defines the / route of app as returning the contents of index.html with the argument of name. By default, the request.args.get function will look for the name being provided by the user. If no name is provided, it will default to world. @app.route is otherwise known as a decorator.
>
> — Week 9 notes, section “Flask” (<https://cs50.harvard.edu/x/notes/9/#flask>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#flask))

> Notice that a form is now created that takes the user’s name and then passes it off to a route called /greet. autocomplete is turned off. Further, a placeholder with the text name is included.
>
> — Week 9 notes, section “Forms” (<https://cs50.harvard.edu/x/notes/9/#forms>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#forms))

> Still, there is a bug in this code. With our new implementation, when someone types in no name into the form, Hello, is displayed without a name. We can improve our code by editing app.py as follows:
>
> — Week 9 notes, section “Request Methods” (<https://cs50.harvard.edu/x/notes/9/#request-methods>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#request-methods))

> In the simplest form, we can implement this by creating a folder called login and then adding the following files.
>
> — Week 9 notes, section “Cookies and Session” (<https://cs50.harvard.edu/x/notes/9/#cookies-and-session>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#cookies-and-session))

> JavaScript Object Notation or JSON is a text file of dictionaries with keys and values. This is a raw, computer-friendly way to get lots of data.
>
> — Week 9 notes, section “JSON” (<https://cs50.harvard.edu/x/notes/9/#json>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#json))

### Other lecture sections that mention this concept

- Week 0: [Computer Science and Problem Solving](../weeks/week-00-scratch/lecture.md#computer-science-and-problem-solving), [Conditionals](../weeks/week-00-scratch/lecture.md#conditionals), [Ivy’s Hardest Game](../weeks/week-00-scratch/lecture.md#ivys-hardest-game), [Oscartime](../weeks/week-00-scratch/lecture.md#oscartime), [Scratch](../weeks/week-00-scratch/lecture.md#scratch), [Visual Studio Code and chat.py](../weeks/week-00-scratch/lecture.md#visual-studio-code-and-chatpy)
- Week 1: [Functions](../weeks/week-01-c/lecture.md#functions), [Header Files and CS50 Manual Pages](../weeks/week-01-c/lecture.md#header-files-and-cs50-manual-pages), [Hello, You](../weeks/week-01-c/lecture.md#hello-you), [compare.c](../weeks/week-01-c/lecture.md#comparec)
- Week 2: [Exit Status](../weeks/week-02-arrays/lecture.md#exit-status)
- Week 3: [Merge Sort](../weeks/week-03-algorithms/lecture.md#merge-sort)
- Week 4: [Valgrind](../weeks/week-04-memory/lecture.md#valgrind), [Welcome!](../weeks/week-04-memory/lecture.md#welcome), [scanf](../weeks/week-04-memory/lecture.md#scanf)
- Week 5: [Data Structures](../weeks/week-05-data-structures/lecture.md#data-structures), [Queues](../weeks/week-05-data-structures/lecture.md#queues), [Tries](../weeks/week-05-data-structures/lecture.md#tries)
- Week 6: [Exceptions](../weeks/week-06-python/lecture.md#exceptions), [Lists](../weeks/week-06-python/lecture.md#lists), [Searching and Dictionaries](../weeks/week-06-python/lecture.md#searching-and-dictionaries), [Strings](../weeks/week-06-python/lecture.md#strings)
- Week 7: [Flat-File Database](../weeks/week-07-sql/lecture.md#flat-file-database), [INSERT](../weeks/week-07-sql/lecture.md#insert), [Relational Databases](../weeks/week-07-sql/lecture.md#relational-databases), [Summing Up](../weeks/week-07-sql/lecture.md#summing-up)
- Artificial Intelligence: [Deep Learning](../weeks/week-ai-artificial-intelligence/lecture.md#deep-learning)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 9؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Bottom Up — Practice](../weeks/week-04-memory/practice/bottomup.md) (`practice-4-bottomup`)
  - [Mario (more comfortable) — Problem Set 1](../weeks/week-01-c/psets/mario-more.md) (`pset-1-mario-more`)
  - [Hello, It’s Me — Problem Set 1](../weeks/week-01-c/psets/me.md) (`pset-1-me`)
  - [Speller — Problem Set 5](../weeks/week-05-data-structures/psets/speller.md) (`pset-5-speller`)
  - [Mario (more comfortable) — Problem Set 6](../weeks/week-06-python/psets/mario-more.md) (`pset-6-mario-more`)
  - [Birthdays — Problem Set 9](../weeks/week-09-flask/psets/birthdays.md) (`pset-9-birthdays`)
  - [Week 8 — Lecture notes (HTML, CSS, JavaScript)](../weeks/week-08-html-css-javascript/lecture.md) (`week-8-lecture`)
  - [Week 9 — Lecture notes (Flask)](../weeks/week-09-flask/lecture.md) (`week-9-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
فرم‌ها داده‌ی کاربر را به سرور می‌فرستند؛ GET داده را در URL و POST در بدنه‌ی درخواست ارسال می‌کند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/9/ — retrieved 2026-10-18T05:10:45+03:30, sha256 `97ceb6d0e8e004aa…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bGET\b|\bPOST\b|\bforms?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
