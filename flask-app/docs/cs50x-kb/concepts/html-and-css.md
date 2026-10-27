---
id: concept-html-and-css
type: concept
title: HTML and CSS
week: 8
parent: concepts
children: []
prerequisites: []
related:
- practice-8-redo
- pset-8-homepage
- pset-8-trivia
- pset-9-birthdays
- short-css
- short-html
- week-8-lecture
source_urls:
- https://cs50.harvard.edu/x/notes/8/
source_type: mixed
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:10:41+03:30'
review_status: partially-verified
difficulty: null
generated_difficulty: null
languages: []
tags:
- concept
- html-and-css
checksum: sha256:5e15c4987f577b7360ea4d0fc2b887c3a67d4b40bf991910a02985545915d41e
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# HTML and CSS

## 1. Source metadata
- **Title:** HTML and CSS
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/8/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:41+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/8/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> Notice that the input tag includes attributes that designate that this is of type email. The browser knows to double-check that the input is an email address. You can download this code here.
>
> — Week 8 notes, section “Regular Expressions” (<https://cs50.harvard.edu/x/notes/8/#regular-expressions>; KB: [week-8-lecture](../weeks/week-08-html-css-javascript/lecture.md#regular-expressions))

> CSS, or cascading style sheet, is a style sheet language that allows you to fine-tune the aesthetics of your HTML files.
>
> — Week 8 notes, section “CSS” (<https://cs50.harvard.edu/x/notes/8/#css>; KB: [week-8-lecture](../weeks/week-08-html-css-javascript/lecture.md#css))

> Notice that <div> tags are used to divide up this HTML file into specific regions. text-align: center is invoked on the entire body of the HTML. Because everything inside body is a child of body, the center attribute cascades down to those children. You can download this code here.
>
> — Week 8 notes, section “CSS” (<https://cs50.harvard.edu/x/notes/8/#css>; KB: [week-8-lecture](../weeks/week-08-html-css-javascript/lecture.md#css))

> Notice all the style tags are placed up in the head in the style tag wrapper. Also, notice that we’ve assigned classes, called centered, large, medium, and small to our elements, and that we select those classes by placing a dot before the name, as in.centered You can download this code here.
>
> — Week 8 notes, section “CSS” (<https://cs50.harvard.edu/x/notes/8/#css>; KB: [week-8-lecture](../weeks/week-08-html-css-javascript/lecture.md#css))

> It turns out that we can move all our style code into a special file called a CSS file. We can create a file called style.css and paste our classes there:
>
> — Week 8 notes, section “CSS” (<https://cs50.harvard.edu/x/notes/8/#css>; KB: [week-8-lecture](../weeks/week-08-html-css-javascript/lecture.md#css))

### Other lecture sections that mention this concept

- Week 9: [APIs](../weeks/week-09-flask/lecture.md#apis), [Cookies and Session](../weeks/week-09-flask/lecture.md#cookies-and-session), [Flask](../weeks/week-09-flask/lecture.md#flask), [Flask and SQL](../weeks/week-09-flask/lecture.md#flask-and-sql), [Forms](../weeks/week-09-flask/lecture.md#forms), [Frosh IMs](../weeks/week-09-flask/lecture.md#frosh-ims)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 8؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [Radio Shack Redo — Practice](../weeks/week-08-html-css-javascript/practice/redo.md) (`practice-8-redo`)
  - [Homepage — Problem Set 8](../weeks/week-08-html-css-javascript/psets/homepage.md) (`pset-8-homepage`)
  - [Trivia — Problem Set 8](../weeks/week-08-html-css-javascript/psets/trivia.md) (`pset-8-trivia`)
  - [Birthdays — Problem Set 9](../weeks/week-09-flask/psets/birthdays.md) (`pset-9-birthdays`)
  - [Short: CSS](../weeks/week-08-html-css-javascript/shorts/css.md) (`short-css`)
  - [Short: HTML](../weeks/week-08-html-css-javascript/shorts/html.md) (`short-html`)
  - [Week 8 — Lecture notes (HTML, CSS, JavaScript)](../weeks/week-08-html-css-javascript/lecture.md) (`week-8-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
HTML ساختار و معنای صفحه را با تگ‌ها تعریف می‌کند و CSS ظاهر آن را با انتخابگرها و ویژگی‌ها کنترل می‌کند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- ابتدا تعریف رسمی (بخش ۲) را با ذکر هفته و بخش جزوه بیاور، سپس با مثال ساده‌ی فارسی توضیح بده.
- برای تمرین، به shortها و مسائل مرتبط در بخش ۴ ارجاع بده؛ راه‌حل مسائل را ارائه نکن.

### ایده‌های پیاده‌سازی در سایت
- صفحه‌ی «مفهوم» با تعریف رسمی، توضیح فارسی، و فهرست مسائلی که این مفهوم را تمرین می‌دهند.
- استفاده در نقشه‌ی مفاهیم (concept map) بر اساس `edges.json`.

## 6. References, review, gaps
- https://cs50.harvard.edu/x/notes/8/ — retrieved 2026-10-18T05:10:41+03:30, sha256 `5e15c4987f577b73…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- Passages were matched automatically with the regex `\bHTML\b|\bCSS\b|\btags?\b|\bselectors?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
