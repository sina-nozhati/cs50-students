---
id: pset-8-trivia
type: pset
title: Trivia — Problem Set 8
week: 8
parent: pset-8
children: []
prerequisites:
- week-8-lecture
related:
- concept-html-and-css
- concept-javascript-and-dom
source_urls:
- https://cs50.harvard.edu/x/psets/8/trivia/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:45+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- HTML/CSS/JavaScript
tags:
- css
- dom-manipulation
- html
- javascript-events
- pset
- trivia
checksum: sha256:25691b10074a54db74d3d2ae0fa2ce7653cd21d083f7baae2a5dad9baa8bdaa0
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Trivia — Problem Set 8

## 1. Source metadata
- **Title:** Trivia — Problem Set 8
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/8/trivia/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:45+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/8/trivia/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="trivia"></a>

### Trivia

Write a webpage that lets users answer trivia questions.

![screenshot of trivia questions](https://cs50.harvard.edu/x/psets/8/trivia/questions.png)

<a id="getting-started"></a>

#### Getting Started

Open [cs50.dev](https://cs50.dev).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

```
$
```

Click inside of that terminal window and then execute

```
wget https://cdn.cs50.net/2025/fall/psets/8/trivia.zip
```

followed by Enter in order to download a ZIP called `trivia.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

```
unzip trivia.zip
```

to create a folder called `trivia`. You no longer need the ZIP file, so you can execute

```
rm trivia.zip
```

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

```
cd trivia
```

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

```
trivia/ $
```

If all was successful, you should execute

```
ls
```

and you should see an `index.html` file and a `styles.css` file.

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

<a id="implementation-details"></a>

#### Implementation Details

Design a webpage using HTML, CSS, and JavaScript to let users answer trivia questions.

* In `index.html`, add beneath “Part 1” a multiple-choice trivia question of your choosing with HTML.
  * You should use an `h3` heading for the text of your question.
  * You should have one `button` for each of the possible answer choices. There should be at least three answer choices, of which exactly one should be correct.
* Using JavaScript, add logic so that the buttons change colors when a user clicks on them.
  * If a user clicks on a button with an incorrect answer, the button should turn red and text should appear beneath the question that says “Incorrect”.
  * If a user clicks on a button with the correct answer, the button should turn green and text should appear beneath the question that says “Correct!”.
* In `index.html`, add beneath “Part 2” a text-based free response question of your choosing with HTML.
  * You should use an `h3` heading for the text of your question.
  * You should use an `input` field to let the user type a response.
  * You should use a `button` to let the user confirm their answer.
* Using JavaScript, add logic so that the text field changes color when a user confirms their answer.
  * If the user types an incorrect answer and presses the confirmation button, the text field should turn red and text should appear beneath the question that says “Incorrect”.
  * If the user types the correct answer and presses the confirmation button, the input field should turn green and text should appear beneath the question that says “Correct!”.

Optionally, you may also:

* Edit `styles.css` to change the CSS of your webpage!
* Add additional trivia questions to your trivia quiz if you would like!

<a id="walkthrough"></a>

##### Walkthrough

This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!

[Embedded video: https://video.cs50.io/WGd0Jx7rxUo](https://video.cs50.io/WGd0Jx7rxUo)

<a id="hints"></a>

##### Hints

* Use [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) to query for a single HTML element.
* Use [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) to query for multiple HTML elements that match a query. The function returns an array of all matching elements.

> **Not sure how to solve?** *(collapsible block on the source page)*
>

<a id="testing"></a>

##### Testing

No `check50` for this one, as implementations will vary based on your questions! But be sure to test both incorrect and correct responses for each of your questions to ensure that your webpage responds appropriately.

Run `http-server` in your terminal while in your `trivia` directory to start a web server that serves your webpage.

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/trivia
```

Want to see the staff’s solution? You can find two ways of solving the problem here!

> **Creating event listeners with JavaScript** *(collapsible block on the source page)*
>
> ```html
> <!DOCTYPE html>
>
> <html lang="en">
>     <head>
>         <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
>         <link href="styles.css" rel="stylesheet">
>         <title>Trivia!</title>
>         <script>
>
>             // Wait for DOM content to load
>             document.addEventListener('DOMContentLoaded', function() {
>
>                 // Get all elements with class "correct"
>                 let corrects = document.querySelectorAll('.correct');
>
>                 // Add event listeners to each correct button
>                 for (let i = 0; i < corrects.length; i++) {
>                     corrects[i].addEventListener('click', function() {
>
>                         // Set background color to green
>                         corrects[i].style.backgroundColor = 'Green';
>
>                         // Go to parent element of correct button and find the first element with class "feedback" which has that parent
>                         corrects[i].parentElement.querySelector('.feedback').innerHTML = 'Correct!';
>                     });
>                 }
>
>                 // When any incorrect answer is clicked, change color to red.
>                 let incorrects = document.querySelectorAll(".incorrect");
>                 for (let i = 0; i < incorrects.length; i++) {
>                     incorrects[i].addEventListener('click', function() {
>
>                         // Set background color to green
>                         incorrects[i].style.backgroundColor = 'Red';
>
>                         // Go to parent element of correct button and find the first element with class "feedback" which has that parent
>                         incorrects[i].parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
>                     });
>                 }
>
>                 // Check free response submission
>                 document.querySelector('#check').addEventListener('click', function() {
>                     let input = document.querySelector('input');
>                     if (input.value === 'Switzerland') {
>                         input.style.backgroundColor = 'green';
>                         input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
>                     }
>                     else {
>                         input.style.backgroundColor = 'red';
>                         input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
>                     }
>                 });
>             });
>         </script>
>     </head>
>     <body>
>         <div class="header">
>             <h1>Trivia!</h1>
>         </div>
>
>         <div class="container">
>             <div class="section">
>                 <h2>Part 1: Multiple Choice </h2>
>                 <hr>
>                 <h3>What is the approximate ratio of people to sheep in New Zealand?</h3>
>                 <button class="incorrect">6 people per 1 sheep</button>
>                 <button class="incorrect">3 people per 1 sheep</button>
>                 <button class="incorrect">1 person per 1 sheep</button>
>                 <button class="incorrect">1 person per 3 sheep</button>
>                 <button class="correct">1 person per 6 sheep</button>
>                 <p class="feedback"></p>
>             </div>
>
>             <div class="section">
>                 <h2>Part 2: Free Response</h2>
>                 <hr>
>                 <h3>In which country is it illegal to own only one guinea pig, as a lone guinea pig might get lonely?</h3>
>                 <input type="text"></input>
>                 <button id="check">Check Answer</button>
>                 <p class="feedback"></p>
>             </div>
>         </div>
>     </body>
> </html>
> ```

> **Creating event listeners with HTML** *(collapsible block on the source page)*
>
> ```html
> <!DOCTYPE html>
>
> <html lang="en">
>     <head>
>         <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
>         <link href="styles.css" rel="stylesheet">
>         <title>Trivia!</title>
>         <script>
>             function checkMultiChoice(event) {
>
>                 // Get the element which triggered the event
>                 let button = event.target;
>
>                 // Check if the element's inner HTML matches expected answer
>                 if (button.innerHTML == '1 person per 6 sheep') {
>                     button.style.backgroundColor = 'Green';
>                     button.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
>                 }
>                 else {
>                     button.style.backgroundColor = 'Red';
>                     button.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
>                 }
>             }
>
>             function checkFreeResponse(event) {
>
>                 // Get the element which triggered the event
>                 let button = event.target;
>
>                 // Get the input element corresponding to the button
>                 let input = button.parentElement.querySelector('input');
>
>                 // Check for correct answer
>                 if (input.value === 'Switzerland') {
>                     input.style.backgroundColor = 'Green';
>                     input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
>                 }
>                 else {
>                     input.style.backgroundColor = 'Red';
>                     input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
>                 }
>             }
>         </script>
>     </head>
>     <body>
>         <div class="header">
>             <h1>Trivia!</h1>
>         </div>
>
>         <div class="container">
>             <div class="section">
>                 <h2>Part 1: Multiple Choice </h2>
>                 <hr>
>                 <h3>What is the approximate ratio of people to sheep in New Zealand?</h3>
>                 <button onclick="checkMultiChoice(event)">6 people per 1 sheep</button>
>                 <button onclick="checkMultiChoice(event)">3 people per 1 sheep</button>
>                 <button onclick="checkMultiChoice(event)">1 person per 1 sheep</button>
>                 <button onclick="checkMultiChoice(event)">1 person per 3 sheep</button>
>                 <button onclick="checkMultiChoice(event)">1 person per 6 sheep</button>
>                 <p class="feedback"></p>
>             </div>
>
>             <div class="section">
>                 <h2>Part 2: Free Response</h2>
>                 <hr>
>                 <h3>In which country is it illegal to own only one guinea pig, as a lone guinea pig might get lonely?</h3>
>                 <input type="text"></input>
>                 <button onclick="checkFreeResponse(event)">Check Answer</button>
>                 <p class="feedback"></p>
>             </div>
>         </div>
>     </body>
> </html>
> ```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2025/fall/psets/8/trivia.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `trivia/index.html` | 872 | [yes](trivia-distribution/files/trivia/index.html) |
| `trivia/styles.css` | 1268 | [yes](trivia-distribution/files/trivia/styles.css) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): HTML/CSS/JavaScript
- Folder: `trivia`; files shown on the page: `index.html`, `styles.css`
- check50: No check50 (stated)
- style50: not stated
- submit50: `cs50/problems/2026/x/trivia`
- Page sections (order on source): Getting Started, Implementation Details, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم HTML، CSS، JavaScript events، DOM manipulation.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Build a trivia webpage in index.html and styles.css. Part 1 is a multiple-choice question with at least three buttons: JavaScript turns a clicked button red with 'Incorrect' or green with 'Correct!'. Part 2 is a free-response question checked with JavaScript in a similar way. There is no check50; test it manually with http-server.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 8](README.md) (`pset-8`)
- **Prerequisites (generated):** [Week 8 — Lecture notes (HTML, CSS, JavaScript)](../lecture.md) (`week-8-lecture`)
- **Related:**
  - [HTML and CSS](../../../concepts/html-and-css.md) (`concept-html-and-css`)
  - [JavaScript and the DOM](../../../concepts/javascript-and-dom.md) (`concept-javascript-and-dom`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
HTML، CSS و JavaScript: رویدادها و تغییر DOM.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. ساختار صفحه را اول با HTML بساز و بعد رفتار را با JavaScript اضافه کن.
2. برای هر دکمه چه رویدادی را گوش می‌دهی و در پاسخ چه چیزی از صفحه تغییر می‌کند؟
3. ابزار توسعه‌دهنده‌ی مرورگر را برای دیدن خطاهای JavaScript باز نگه دار.

### اشتباه‌های رایج (مفهومی)
- اجرای اسکریپت قبل از بارگذاری عناصر صفحه

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
- https://cs50.harvard.edu/x/psets/8/trivia/ — retrieved 2026-10-18T05:11:45+03:30, sha256 `25691b10074a54db…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
