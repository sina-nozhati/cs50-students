---
id: concept-flask-and-routes
type: concept
title: Flask, Routes and Templates (Jinja)
week: 9
parent: concepts
children: []
prerequisites: []
related:
- practice-9-helloflask
- pset-9-birthdays
- pset-9-finance
- short-flask
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
- flask-and-routes
checksum: sha256:97ceb6d0e8e004aac38fcd65227b3bcf1b99c37f2ff0b9bf7d0f83036d455ecb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Flask, Routes and Templates (Jinja)

## 1. Source metadata
- **Title:** Flask, Routes and Templates (Jinja)
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/9/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:45+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/9/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Flask is a third-party library that allows you to host web applications using the Flask framework, or a micro-framework, within Python.
>
> — Week 9 notes, section “Flask” (<https://cs50.harvard.edu/x/notes/9/#flask>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#flask))

> Here is a very simple Flask application in app.py:
>
> — Week 9 notes, section “Flask” (<https://cs50.harvard.edu/x/notes/9/#flask>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#flask))

> Improving our application, we can also serve HTML based upon templates by creating a folder called templates and creating a file called index.html with the following code within that folder:
>
> — Week 9 notes, section “Flask” (<https://cs50.harvard.edu/x/notes/9/#flask>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#flask))

> Then, in the same folder that the templates folder appears, create a file called app.py and add the following code:
>
> — Week 9 notes, section “Flask” (<https://cs50.harvard.edu/x/notes/9/#flask>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#flask))

> Notice that this code defines app as the Flask application. Then, it defines the / route of app as returning the contents of index.html with the argument of name. By default, the request.args.get function will look for the name being provided by the user. If no name is provided, it will default to world. @app.route is otherwise known as a decorator.
>
> — Week 9 notes, section “Flask” (<https://cs50.harvard.edu/x/notes/9/#flask>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#flask))

### Other lecture sections that mention this concept

- Week 8: [DNS](../weeks/week-08-html-css-javascript/lecture.md#dns), [Routers](../weeks/week-08-html-css-javascript/lecture.md#routers)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 9؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Hello, Flask — Practice](../weeks/week-09-flask/practice/helloflask.md) (`practice-9-helloflask`)
  - [Birthdays — Problem Set 9](../weeks/week-09-flask/psets/birthdays.md) (`pset-9-birthdays`)
  - [C$50 Finance — Problem Set 9](../weeks/week-09-flask/psets/finance.md) (`pset-9-finance`)
  - [Short: Flask](../weeks/week-09-flask/shorts/flask.md) (`short-flask`)
  - [Week 9 — Lecture notes (Flask)](../weeks/week-09-flask/lecture.md) (`week-9-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
Flask یک چارچوب وب سبک در Python است؛ route آدرس را به تابع نگاشت می‌کند و Jinja قالب‌های HTML را با داده پر می‌کند.

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
- Passages were matched automatically with the regex `\bFlask\b|\broutes?\b|\bJinja\b|\btemplates?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
