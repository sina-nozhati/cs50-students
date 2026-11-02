---
id: practice-8-redo
type: practice
title: Radio Shack Redo — Practice
week: 8
parent: week-8
children: []
prerequisites:
- week-8-lecture
related:
- concept-html-and-css
- course-practice-index
source_urls:
- https://cs50.harvard.edu/x/practice/redo/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:11:10+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty:
  value: 1
  scale: 1 (easy) – 5 (hard)
  note: GENERATED estimate by KB builder; not stated by CS50
languages:
- HTML/CSS/JavaScript
tags:
- bootstrap
- css-layout
- html
- practice
- radio-shack-redo
checksum: sha256:7ca9a505719ae78169375c6d401a2393c233c0e414bb04a11a25af2c76d99459
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Radio Shack Redo — Practice

## 1. Source metadata
- **Title:** Radio Shack Redo — Practice
- **Type:** practice
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/practice/redo/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:11:10+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/practice/redo/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="radio-shack-redo"></a>

### Radio Shack Redo

<a id="learning-goals"></a>

#### Learning Goals

* Become aquainted with the history of web design
* Learn to use modern web development tools

<a id="background"></a>

#### Background

The world wide web as we know it has only been around since the mid 1990’s. Early tools to develop websites were very limited: there was no CSS or JavaScript and HTML was rendered differently on different browsers. One of the earliest sites was [amazon.com](https://amazon.com).

![amazon](https://cs50.harvard.edu/x/practice/redo/amazon.png)

Quite a different look than today!

Another early site was RadioShack. Their first website in 1996 had a look very similar to websites of that time. The hottest design elements were clunky-looking buttons and repeating background patterns.

![RadioShack1996](https://cs50.harvard.edu/x/practice/redo/radio1996.png)

A common feature on early sites was a link to a “text only” version of the web page. Because internet connections were so slow, images could be very slow to load! The oversized RadioShack logo and its corresponding buttons are actually one image here: the buttons are activated using an html `map` feature, which is still available today, but rarely used.

```html
<map name="rsmap">
<area shape="rect" coords="8,246,122,297" href="https://www.radioshack.com/rsstorelocator/rszip?1">
<area shape="rect" coords="123,246,240,297" href="https://www.radioshack.com/rsfuture.html">
<area shape="rect" coords="241,246,358,297" href="https://www.tandy.com/contacts/">
<area shape="rect" coords="359,246,475,297" href="https://www.tandy.com/press.html">
<area shape="rect" coords="476,246,599,297" href="https://www.radioshack.com/history/">
</map>
```

There was very little control over typography and the only fonts available were those that resided on a visitor’s computer. So a web designer had to be careful to use only very common, standard fonts.

By 1997, RadioShack significantly upgraded the look of their site, and it now looked like this. Note the 3-D spinning “R”, another popular feature on websites of that time!

![radio1997](https://cs50.harvard.edu/x/practice/redo/spinningR.gif)

To create a layout like this with columns and rows, the entire page is constructed from an HTML table, with a 1-by-1 pixel image, `dot_clear.gif`, to control the visual layout of HTML elements on a web page, since the HTML standard at the time did not allow this. Tables were not created for this purpose, but designers had few options for controling the layout of the page.

```html
<table border="0" cellspacing="0" cellpadding="0" width="969"><tr valign="top" align="left">
	<td colspan="1" width="10"><img src="dot_clear.gif" width="10" height="1" border="0"></td>
	<td colspan="1" width="2"><img src="dot_clear.gif" width="2" height="1" border="0"></td>
	<td colspan="1" width="35"><img src="dot_clear.gif" width="35" height="1" border="0"></td
 ...
```

Since there was still limited choices for fonts, all of the type you see on this page that is not the standard “Times Roman” was created as an image and imported into the web page.

[Take a look at some other website designs from the 90’s.](https://www.justinmind.com/blog/10-90s-websites-designs-you-wont-believe-existed/)

Now you’ll re-design RadioShack’s website (just the homepage is fine!) using modern web development tools. No tables, html maps or spinning logos please!

<a id="getting-started"></a>

#### Getting Started

1. Log into [cs50.dev](https://cs50.dev/) using your GitHub account.
2. Click inside the terminal window and execute `cd`.
3. Execute `wget https://cdn.cs50.net/2022/fall/labs/8/redo.zip` followed by Enter in order to download a zip called `redo.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!
4. Now execute `unzip redo.zip` to create a folder called `redo`.
5. You no longer need the ZIP file, so you can execute `rm redo.zip` and respond with “y” followed by Enter at the prompt.

<a id="implementation-details"></a>

#### Implementation Details

Notice that you’ve received three folders, `radio1996/`, `radio1997/`, and `radiotoday/`. You can explore implementations of Radio Shack’s website from 1996 and 1997, but you’ll ultimately create your own iteration in `radiotoday/`.

One of the most popular front-end web development tools in use these days is [Bootstrap](https://getbootstrap.com/docs/). It’s free, open-source, and designed to enable responsive development of websites and web apps. It’s built on top of CSS and JavaScript to allow developers to create websites quickly and without having to recreate commonly used features such as interactive buttons, navigation systems, columns and grids.

Start your redesign by trying out bootstrap’s [Navbar](https://getbootstrap.com/docs/5.2/components/navbar/) feature to easily create a custom navigation bar to handle all the menu options. Scoll down on this bootstrap documentation until you see a simple navigation bar with minimal code and copy this code to the top of the `body` section of `index.html`.

```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Pricing</a>
        <a class="nav-link disabled">Disabled</a>
      </div>
    </div>
  </div>
</nav>
```

When you run `http-server` to preview your web page, you’ll see menu items on top such as “Features”, “Pricing”, etc. Change these to represent the appropriate menu items for your RadioShack homepage. You don’t need to create additional pages for these to link to, but if you did, you would change `href=#` in each of these menu items to link to the appropriage html pages.

Next, take a look at other bootstrap features. Check out how to [create columns](https://getbootstrap.com/docs/5.2/layout/columns/) without using tables as was done in the 90’s.

You may want to take a look at how to create [responsive images](https://getbootstrap.com/docs/5.2/content/images/) that shrink and expand as the page size changes so they look good on any size device.

And while you are thinking about images for your homepage, check out how to create a [carousel](https://getbootstrap.com/docs/5.2/components/carousel/) to automatically cycle through more than one image.

You are the designer, the design here is up to you. Have fun and see what you can create! A more recent RadioShack logo is included if you want to use it.

<a id="thought-question"></a>

#### Thought Question

* Why do you think so many designers use Bootstrap, rather than creating their own CSS?

<a id="how-to-test-your-code"></a>

#### How to Test Your Code

No `check50` for this assignment! To ensure that the code on your pages is valid, you can use this [Markup Validation Service](https://validator.w3.org/#validate_by_input), copying and pasting your HTML directly into the provided text box.

<a id="how-to-submit"></a>

#### How to Submit

No need to submit! This is practice problem.

### Distribution code inventory (downloaded files)

#### https://cdn.cs50.net/2022/fall/labs/8/redo.zip

| File | Bytes | Stored in KB |
|---|---:|---|
| `redo/radiotoday/index.html` | 667 | [yes](redo-distribution/files/redo/radiotoday/index.html) |
| `redo/radiotoday/radioshack-logo.png` | 20970 | no — binary/media/data file (inventory only) |
| `redo/radio1997/anmclr.gif` | 12241 | no — binary/media/data file (inventory only) |
| `redo/radio1997/steve_logo.gif` | 1097 | no — binary/media/data file (inventory only) |
| `redo/radio1997/index.html` | 19739 | [yes](redo-distribution/files/redo/radio1997/index.html) |
| `redo/radio1997/dot_clear.gif` | 42 | no — binary/media/data file (inventory only) |
| `redo/radio1997/about_logo.gif` | 1032 | no — binary/media/data file (inventory only) |
| `redo/radio1997/wall.gif` | 2020 | no — binary/media/data file (inventory only) |
| `redo/radio1997/dth_sat.gif` | 916 | no — binary/media/data file (inventory only) |
| `redo/radio1997/sun.jpeg` | 13390 | no — binary/media/data file (inventory only) |
| `redo/radio1997/img_40f7b7a4.gif` | 1123 | no — binary/media/data file (inventory only) |
| `redo/radio1997/support_logo.gif` | 1170 | no — binary/media/data file (inventory only) |
| `redo/radio1997/computer.gif` | 1150 | no — binary/media/data file (inventory only) |
| `redo/radio1997/you_got.gif` | 1440 | no — binary/media/data file (inventory only) |
| `redo/radio1997/2_dots.gif` | 664 | no — binary/media/data file (inventory only) |
| `redo/radio1997/new_Sizz.gif` | 5866 | no — binary/media/data file (inventory only) |
| `redo/radio1997/srevices_logo.gif` | 1091 | no — binary/media/data file (inventory only) |
| `redo/radio1997/75.gif` | 2744 | no — binary/media/data file (inventory only) |
| `redo/radio1997/red_ball_2.gif` | 182 | no — binary/media/data file (inventory only) |
| `redo/radio1997/radioshack.gif` | 981 | no — binary/media/data file (inventory only) |
| `redo/radio1997/family_radio.gif` | 1094 | no — binary/media/data file (inventory only) |
| `redo/radio1997/storelocator_logo.gif` | 936 | no — binary/media/data file (inventory only) |
| `redo/radio1997/1_dots.gif` | 731 | no — binary/media/data file (inventory only) |
| `redo/radio1997/repair_logo.gif` | 872 | no — binary/media/data file (inventory only) |
| `redo/radio1997/cellular.gif` | 956 | no — binary/media/data file (inventory only) |
| `redo/radio1996/index.html` | 2495 | [yes](redo-distribution/files/redo/radio1996/index.html) |
| `redo/radio1996/mclogo.gif` | 3979 | no — binary/media/data file (inventory only) |
| `redo/radio1996/longall.gif` | 8390 | no — binary/media/data file (inventory only) |
| `redo/radio1996/rsfetur2.gif` | 24463 | no — binary/media/data file (inventory only) |
| `redo/radio1996/big_rgrey1.gif` | 1584 | no — binary/media/data file (inventory only) |
| `redo/spinningR.gif` | 879124 | no — binary/media/data file (inventory only) |

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
- Kind: optional practice problem (not submittable, per practice page)
- Required for certificate: False
- Variant / comfort level (as stated): not stated
- Choice group: none
- Language (derived from files/commands on the page): HTML/CSS/JavaScript
- Folder: `redo`; files shown on the page: `index.html`
- check50: No check50 (stated)
- style50: not stated
- submit50: not stated
- Page sections (order on source): Learning Goals, Background, Getting Started, Implementation Details, Thought Question, How to Test Your Code, How to Submit
- Walkthrough videos: none
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
**اهداف یادگیری (تولیدشده):** تمرین مفاهیم HTML، Bootstrap، CSS layout.

**خلاصه‌ی بازنویسی‌شده (انگلیسی، paraphrase سازنده‌ی KB — نه متن CS50):** Study RadioShack's 1996 and 1997 websites (provided folders), then build your own modern version in radiotoday/ using a front-end framework such as Bootstrap.

**سطح دشواری تخمینی (تولیدشده):** 1 از ۵

## 4. Relationships
- **Parent:** [Week 8 — HTML, CSS, JavaScript](../week.md) (`week-8`)
- **Prerequisites (generated):** [Week 8 — Lecture notes (HTML, CSS, JavaScript)](../lecture.md) (`week-8-lecture`)
- **Related:**
  - [HTML and CSS](../../../concepts/html-and-css.md) (`concept-html-and-css`)
  - [Practice Problems](../../../course/practice-index.md) (`course-practice-index`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
تمرین HTML/CSS/JavaScript.

### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)
> این راهنمایی‌ها عمداً کلی‌اند و هیچ بخشی از راه‌حل را لو نمی‌دهند. به ترتیب و فقط در صورت نیاز باز شوند.

1. ساختار، ظاهر و رفتار را جدا نگه دار.

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
- https://cs50.harvard.edu/x/practice/redo/ — retrieved 2026-10-18T05:11:10+03:30, sha256 `7ca9a505719ae781…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
