---
id: pset-8-homepage
type: pset
title: Homepage — Problem Set 8
week: 8
parent: pset-8
children: []
prerequisites:
- week-8-lecture
related:
- concept-html-and-css
- concept-javascript-and-dom
- concept-sql-basics
source_urls:
- https://cs50.harvard.edu/x/psets/8/homepage/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:46+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 2
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- HTML/CSS/JavaScript
tags:
- bootstrap
- css-selectors
- homepage
- html
- javascript
- multi-page-sites
- pset
checksum: sha256:97bddadc8eb8dce27b1330c5f2a7c75eb2b721648f03d385353e0c1e364a7acf
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Homepage — Problem Set 8

## 1. Source metadata
- **Title:** Homepage — Problem Set 8
- **Type:** pset
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/psets/8/homepage/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:46+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/psets/8/homepage/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="homepage"></a>

### Homepage

Build a simple homepage using HTML, CSS, and JavaScript.

<a id="background"></a>

#### Background

The internet has enabled incredible things: we can use a search engine to research anything imaginable, communicate with friends and family members around the globe, play games, take courses, and so much more. But it turns out that nearly all pages we may visit are built on three core languages, each of which serves a slightly different purpose:

1. HTML, or *HyperText Markup Language*, which is used to describe the content of websites;
2. CSS, *Cascading Style Sheets*, which is used to describe the aesthetics of websites; and
3. JavaScript, which is used to make websites interactive and dynamic.

Create a simple homepage that introduces yourself, your favorite hobby or extracurricular, or anything else of interest to you.

<a id="getting-started"></a>

#### Getting Started

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
wget https://cdn.cs50.net/2026/x/psets/8/homepage.zip
```

in order to download a ZIP called `homepage.zip` into your codespace.

Then execute

```
unzip homepage.zip
```

to create a folder called `homepage`. You no longer need the ZIP file, so you can execute

```
rm homepage.zip
```

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

```
cd homepage
```

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

```
homepage/ $
```

Execute `ls` by itself, and you should see a few files:

```
index.html  styles.css
```

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong! You can immediately start a server to view your site by running

```
http-server
```

in the terminal window. Then, command-click (if on Mac) or control-click (if on PC) on the first link that appears:

```
http-server running on LINK
```

Where LINK is the address of your server.

<a id="specification"></a>

#### Specification

Implement in your `homepage` directory a website that must:

* Contain at least four different `.html` pages, at least one of which is `index.html` (the main page of your website), and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.
* Use at least ten (10) distinct HTML tags besides `<html>`, `<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those ten!
* Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. See [Bootstrap’s documentation](https://getbootstrap.com/docs/5.3/) to get started. In particular, you might find some of [Bootstrap’s components](https://getbootstrap.com/docs/5.3/components/) of interest. To add Bootstrap to your site, it suffices to include

  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-4.0.0.js" integrity="sha256-9fsHeVnKBvqh3FB2HYu7g2xseAZ5MlN6Kz/qnkASV8U=" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  ```

  in your pages’ `<head>`, below which you can also include

  ```html
  <link href="styles.css" rel="stylesheet">
  ```

  to link your own CSS.
* Have at least one stylesheet file of your own creation, `styles.css`, which uses at least five (5) different CSS selectors (e.g. tag (`example`), class (`.example`), or ID (`#example`)), and within which you use a total of at least five (5) different CSS properties, such as `font-size`, or `margin`; and
* Integrate one or more features of JavaScript into your site to make your site more interactive. For example, you can use JavaScript to add alerts, to have an effect at a recurring interval, or to add interactivity to buttons, dropdowns, or forms. Feel free to be creative!
* Ensure that your site looks nice on browsers both on mobile devices as well as laptops and desktops.

You should also create a text file, `specification.txt`, which lists the 10 HTML tags and 5 CSS properties you’ve used, as well as a brief (one-sentence) description of how you chose to use JavaScript and Bootstrap.

<a id="testing"></a>

#### Testing

If you want to see how your site looks while you work on it, you can run `http-server`. Command- or control-click on the first link presented by http-server, which should open your webpage in a new tab. You should then be able to refresh the tab containing your webpage to see your latest changes.

Recall also that by opening Developer Tools in Google Chrome, you can *simulate* visiting your page on a mobile device by clicking the phone-shaped icon to the left of **Elements** in the developer tools window, or, once the Developer Tools tab has already been opened, by typing `Ctrl`+`Shift`+`M` on a PC or `Cmd`+`Shift`+`M` on a Mac, rather than needing to visit your site on a mobile device separately!

<a id="assessment"></a>

#### Assessment

No `check50` for this assignment! Instead, your site’s correctness will be assessed based on whether you meet the requirements of the specification as outlined above, and whether your HTML is well-formed and valid. To ensure that your pages are, you can use this [Markup Validation Service](https://validator.w3.org/#validate_by_input), copying and pasting your HTML directly into the provided text box. Take care to eliminate any warnings or errors suggested by the validator before submitting!

Consider also:

* whether the aesthetics of your site are such that it is intuitive and straightforward for a user to navigate;
* whether your CSS has been factored out into a separate CSS file(s); and
* whether you have avoided repetition and redundancy by “cascading” style properties from parent tags.

Afraid `style50` does not support HTML files, and so it is incumbent upon you to indent and align your HTML tags cleanly. Know also that you can create an HTML comment with:

```html
<!-- Comment goes here -->
```

but commenting your HTML code is not as imperative as it is when commenting code in, say, C or Python. You can also comment your CSS, in CSS files, with:

```css
/* Comment goes here */
```

<a id="hints"></a>

#### Hints

For fairly comprehensive guides on the languages introduced in this problem, check out these tutorials:

* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)

<a id="how-to-submit"></a>

#### How to Submit

In your terminal, execute the below to submit your work, answering the prompts that come up as well.

```
submit50 cs50/problems/2026/x/homepage
```

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2026/x/psets/8/homepage.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `homepage/index.html` | 632 | [yes](homepage-distribution/files/homepage/index.html) |
| `homepage/styles.css` | 0 | [yes](homepage-distribution/files/homepage/styles.css) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: problem set problem
- Required for certificate: True
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): HTML/CSS/JavaScript
- Folder: `homepage`; files shown on the page: `index.html`, `styles.css`
- check50: No check50 (stated)
- style50: not stated
- submit50: `cs50/problems/2026/x/homepage`
- Page sections (order on source): Background, Getting Started, Specification, Testing, Assessment, Hints, How to Submit
- Walkthrough videos: none
- Deadline: course deadline 2027-06-30T23:59:00+00:00 UTC = 2027-07-01 03:29 (Asia/Tehran) (per problem-set page)
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم HTML، CSS selectors، Bootstrap، JavaScript، multi-page sites.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Build a personal homepage of at least four linked .html pages, including index.html. It must use at least ten distinct HTML tags (besides html/head/body/title), at least one Bootstrap feature, at least one CSS file with five or more different selectors and properties, and some JavaScript. There is no check50 or style50 for HTML; preview with http-server.

**سطح دشواری تخمینی (تولیدشده):** 2 از ۵

## 4. Relationships
- **Parent:** [Problem Set 8](README.md) (`pset-8`)
- **Prerequisites (generated):** [Week 8 — Lecture notes (HTML, CSS, JavaScript)](../lecture.md) (`week-8-lecture`)
- **Related:**
  - [HTML and CSS](../../../concepts/html-and-css.md) (`concept-html-and-css`)
  - [JavaScript and the DOM](../../../concepts/javascript-and-dom.md) (`concept-javascript-and-dom`)
  - [SQL and Relational Databases](../../../concepts/sql-basics.md) (`concept-sql-basics`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
ساخت یک وب‌سایت چندصفحه‌ای شخصی؛ تمرین HTML معنایی، CSS و Bootstrap.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. الزامات صفحه را فهرست کن (تعداد صفحه‌ها، عناصر، CSS، JavaScript) و طراحی‌ات را بر اساس آن بچین.
2. از اعتبارسنج HTML برای پیدا کردن خطاهای ساختاری استفاده کن.

### اشتباه‌های رایج (مفهومی)
- کمتر بودن تعداد صفحه‌ها یا عناصر خواسته‌شده

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
- https://cs50.harvard.edu/x/psets/8/homepage/ — retrieved 2026-10-18T05:11:46+03:30, sha256 `97bddadc8eb8dce2…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
