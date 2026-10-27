---
id: concept-sessions-and-cookies
type: concept
title: Sessions and Cookies
week: 9
parent: concepts
children: []
prerequisites: []
related:
- pset-9-finance
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
- sessions-and-cookies
checksum: sha256:97ceb6d0e8e004aac38fcd65227b3bcf1b99c37f2ff0b9bf7d0f83036d455ecb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Sessions and Cookies

## 1. Source metadata
- **Title:** Sessions and Cookies
- **Type:** concept
- **Source type:** mixed
- **Official link(s):** <https://cs50.harvard.edu/x/notes/9/>
- **Review status:** partially-verified
- **Retrieved:** 2026-10-18T05:10:45+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/notes/9/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Verbatim passages from the lecture notes (auto-selected by keyword; definitional sentences preferred)

> We can actually implement this itself using cookies. Cookies are small pieces of data that are stored in your browser such that your browser can communicate with the server and effectively say, “I’m an authorized user that has already logged in.” This authorization through this cookie is called a session.
>
> — Week 9 notes, section “Cookies and Session” (<https://cs50.harvard.edu/x/notes/9/#cookies-and-session>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#cookies-and-session))

> Cookies may be stored as follows:
>
> — Week 9 notes, section “Cookies and Session” (<https://cs50.harvard.edu/x/notes/9/#cookies-and-session>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#cookies-and-session))

> Here, a session id is stored with a particular value representing that session.
>
> — Week 9 notes, section “Cookies and Session” (<https://cs50.harvard.edu/x/notes/9/#cookies-and-session>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#cookies-and-session))

> Notice that in addition to Flask, we also include Flask-Session, which is required to support login sessions.
>
> — Week 9 notes, section “Cookies and Session” (<https://cs50.harvard.edu/x/notes/9/#cookies-and-session>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#cookies-and-session))

> Notice that this file looks to see if session["name"] exists (elaborated further in app.py below). If it does, it will display a welcome message. If not, it will recommend you browse to a page to log in.
>
> — Week 9 notes, section “Cookies and Session” (<https://cs50.harvard.edu/x/notes/9/#cookies-and-session>; KB: [week-9-lecture](../weeks/week-09-flask/lecture.md#cookies-and-session))

### Other lecture sections that mention this concept

- Week 1: [Welcome!](../weeks/week-01-c/lecture.md#welcome)
- Week 2: [Welcome!](../weeks/week-02-arrays/lecture.md#welcome)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**هفته‌ی اصلی (تولیدشده):** Week 9؛ پیش‌نیاز: هفته‌های پیش از آن.

## 4. Relationships
- **Parent:** [Concepts (index)](README.md) (`concepts`)
- **Related:**
  - [C$50 Finance — Problem Set 9](../weeks/week-09-flask/psets/finance.md) (`pset-9-finance`)
  - [Week 9 — Lecture notes (Flask)](../weeks/week-09-flask/lecture.md) (`week-9-lecture`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### توضیح مفهومی (تولیدشده)
کوکی‌ها داده‌ی کوچکی هستند که مرورگر نگه می‌دارد و سشن‌ها با کمک آن‌ها وضعیت هر کاربر (مثلاً ورود به سیستم) را بین درخواست‌ها حفظ می‌کنند.

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
- Passages were matched automatically with the regex `\bsessions?\b|\bcookies?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
