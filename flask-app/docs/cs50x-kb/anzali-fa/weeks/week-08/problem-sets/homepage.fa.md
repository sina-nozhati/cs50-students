---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-ps-homepage
type: problem-set-guide
title: راهنمای صفحهٔ شخصی (Homepage)
title_fa: صفحهٔ شخصی (Homepage)
title_en: Homepage
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/8/homepage/
source_refs:
- src-pset-8-homepage#specification
- src-pset-8-homepage#assessment
- src-anzali-authored-8
- src-pset-8
concept_ids:
- w08-c-http-server
- w08-c-multipage-site
- w08-c-anchor-link
- w08-c-tag
- w08-c-bootstrap
- w08-c-external-css
- w08-c-selectors
- w08-c-css-property
- w08-c-cascade
- w08-c-javascript
- w08-c-script-src
- w08-c-responsive
- w08-c-markup-validation
- w08-c-html-comment
problem_set_ref: weeks/week-08/problem-sets/homepage.json
prev: w08-ps-trivia
next: w08-pr-redo
order: 27
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای صفحهٔ شخصی (Homepage)

> **منبع رسمی:** [Homepage](https://cs50.harvard.edu/x/2026/psets/8/homepage/) از پرابلم‌ست ۸ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

یک صفحهٔ شخصی ساده با HTML، CSS و جاوااسکریپت می‌سازی که خودت، سرگرمی یا فعالیت مورد علاقه‌ات یا هر موضوع دیگری را معرفی کند. صفحهٔ رسمی یادآوری می‌کند تقریباً همهٔ صفحه‌های وب روی سه زبان ساخته شده‌اند: HTML برای محتوا، CSS برای ظاهر و جاوااسکریپت برای تعامل.

این مسئله check50 ندارد. درستی بر اساس برآوردن مشخصات و **خوش‌ساخت و معتبر بودن** HTML سنجیده می‌شود، همراه زیبایی و سادگی پیمایش، جدا بودن CSS و بهره گرفتن از آبشار به جای تکرار.

این راهنما فقط مفهوم‌ها و چک‌لیست می‌دهد و کد هیچ صفحه‌ای را ندارد (D65). محتوا و طراحی مال خودت است.

> **از سخنرانی:** تگ‌ها و پیوندها در [یادداشت عنصرهای HTML](/kb/d/w08-n08)؛ انتخابگرها و فایل CSS بیرونی در [یادداشت CSS](/kb/d/w08-n11)؛ Bootstrap در [یادداشت چارچوب‌ها](/kb/d/w08-n12)؛ رویدادها و `setInterval` در [یادداشت رویدادها](/kb/d/w08-n13) و [یادداشت DOM پویا](/kb/d/w08-n14).

## خواسته‌های رسمی

1. دست‌کم چهار صفحهٔ `.html` مختلف داشته باش که یکی `index.html` (صفحهٔ اصلی) است، و از هر صفحه بتوان با یک یا چند پیوند به هر صفحهٔ دیگر رسید.
2. دست‌کم ده تگ HTML **متمایز** غیر از `<html>`، `<head>`، `<body>` و `<title>` به کار ببر؛ تکرار یک تگ فقط یکی حساب می‌شود.
3. یک یا چند امکان Bootstrap را در سایت به کار ببر.
4. دست‌کم یک فایل سبک از خودت، `styles.css`، داشته باش که دست‌کم پنج انتخابگر مختلف و روی هم دست‌کم پنج ویژگی CSS مختلف دارد.
5. یک یا چند امکان جاوااسکریپت را برای تعاملی‌تر کردن سایت به کار ببر.
6. سایت هم روی موبایل و هم روی لپ‌تاپ و رایانهٔ رومیزی خوب دیده شود.
7. فایل متنی `specification.txt` بساز: ده تگ HTML و پنج ویژگی CSS به‌کاررفته، و یک جمله دربارهٔ اینکه جاوااسکریپت و Bootstrap را چطور به کار برده‌ای.
8. HTML باید خوش‌ساخت و معتبر باشد؛ پیش از تحویل همهٔ هشدارها و خطاهای اعتبارسنج را برطرف کن.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. فایل آغازین `index.html` سرآیند Bootstrap را از پیش دارد و `styles.css` خالی است. صفحهٔ رسمی می‌گوید `style50` از HTML پشتیبانی نمی‌کند، پس تورفتگی و ترازبندی تگ‌ها با خودت است.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/8/homepage.zip
unzip homepage.zip
rm homepage.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd homepage
```

## نمونه‌های رسمی ورودی و خروجی

خروجی رسمی `ls`:

```text
index.html  styles.css
```

## راهنمایی‌های رسمی

> **رسمی:** بازنویسی فارسی بخش Hints صفحهٔ رسمی.

- برای راهنمای نسبتاً کامل هر سه زبان، آموزش‌های w3schools را ببین: [HTML](https://www.w3schools.com/html/)، [CSS](https://www.w3schools.com/css/) و [JavaScript](https://www.w3schools.com/js/).
- برای شبیه‌سازی موبایل، در ابزار توسعه‌دهندهٔ کروم روی نماد گوشی سمت چپ **Elements** بزن یا `Ctrl`+`Shift`+`M` (در مک `Cmd`+`Shift`+`M`).

## فرمان‌ها و قطعه‌های رسمی صفحه

> **رسمی:** این فرمان‌ها و قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند.

اجرای سرور برای دیدن سایت (سپس روی نخستین پیوند Command-click یا Control-click کن):

```bash
http-server
```

افزودن Bootstrap در `<head>` هر صفحه (این سرآیند رسمی jQuery را هم بارگذاری می‌کند ولی سرآیند سخنرانی نه؛ d136):

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-4.0.0.js" integrity="sha256-9fsHeVnKBvqh3FB2HYu7g2xseAZ5MlN6Kz/qnkASV8U=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
```

و زیر آن، وصل کردن CSS خودت:

```html
<link href="styles.css" rel="stylesheet">
```

توضیح در HTML:

```html
<!-- Comment goes here -->
```

توضیح در CSS:

```css
/* Comment goes here */
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- اجرای http-server و درگاه 8080 — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- چند صفحه که با پیوند به هم وصل‌اند — [یادداشت](/kb/d/w08-ps-homepage)
- پیوند با تگ a و ویژگی href — [یادداشت](/kb/d/w08-n08) · درس کوتاه `w08-l03` (واحد `w08-l03-u03`)
- تگ آغاز و پایان، مثل <p> و </p> — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- Bootstrap: افزودن با link و استفاده از کلاس‌هایش مثل table — [یادداشت](/kb/d/w08-n12) · درس کوتاه `w08-l05` (واحد `w08-l05-u03`)
- فایل CSS جدا با <link href rel="stylesheet"> — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u03`)
- انتخابگر: نوع تگ، کلاس (.name) و شناسه (#name) — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u02`)
- ویژگی CSS به شکل کلید: مقدار، مثل font-size و text-align — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u01`)
- آبشار: فرزندها سبک والد را به ارث می‌برند — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u02`)
- جاوااسکریپت: زبان برنامه‌نویسی تعامل در صفحه — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u01`)
- <script src> برای بارگیری فایل جاوااسکریپت جدا — [یادداشت](/kb/d/w08-n15) · درس کوتاه `w08-l07` (واحد `w08-l07-u03`)
- ظاهر مناسب روی تلفن همراه و رایانه — [یادداشت](/kb/d/w08-ps-homepage)
- بررسی درستی HTML با Markup Validation Service — [یادداشت](/kb/d/w08-ps-homepage)
- توضیح در HTML با <!-- --> — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. پیش از هر کدی، روی کاغذ چهار صفحه و پیوندهای میانشان را بکش. اگر همهٔ صفحه‌ها یک نوار پیمایش مشترک داشته باشند، شرط «از هر صفحه به هر صفحه» خودبه‌خود برآورده می‌شود.
2. فهرست تگ‌هایی را که این هفته دیدی مرور کن: سرعنوان، بند، فهرست، جدول، تصویر، پیوند، فرم و تگ‌های معنایی. ده تگ متمایز را هنگام ساختن بشمار، نه در پایان.
3. مستندات Bootstrap را باز کن و فقط یک جزء ساده را امتحان کن. ببین کدام کلاس‌ها ظاهر را عوض می‌کنند و کدام جزءها به جاوااسکریپت Bootstrap نیاز دارند.
4. برای پنج انتخابگر، هر سه نوع نوع، کلاس و شناسه را امتحان کن. اگر یک سبک را در چند جا تکرار کرده‌ای، فکر کن آیا می‌توانی آن را یک بار روی عنصر والد بگذاری (آبشار).
5. برای جاوااسکریپت، از ساده شروع کن: یک رویداد روی یک دکمه یا فرم. در یادداشت‌ها دیدی چطور رنگ یا متن را عوض کنی یا با `setInterval` کاری را تکرار کنی.
6. هر صفحه را در اعتبارسنج W3C بگذار و خطاها را از اولی شروع به رفع کن؛ گاهی یک تگ بسته‌نشده چند خطای بعدی را می‌سازد.

## اشتباه‌های رایج

- کمتر از چهار صفحه، یا صفحه‌ای که پیوندی به آن نیست
- شمردن html، head، body یا title جزو ده تگ
- شمردن یک تگ تکراری چند بار
- گذاشتن همهٔ سبک‌ها در ویژگی `style` به جای `styles.css`
- فراموش کردن `alt` برای تصویر یا بستن نادرست تگ‌ها (خطای اعتبارسنج)
- ننوشتن `specification.txt`

## چک‌لیست خودآزمایی

1. دست‌کم چهار فایل `.html` دارم و یکی `index.html` است.
2. از هر صفحه با پیوند به هر صفحهٔ دیگر می‌رسم (مثلاً یک نوار پیمایش مشترک).
3. ده تگ متمایز غیر از html، head، body و title شمرده‌ام.
4. دست‌کم یک امکان Bootstrap به کار رفته و در `specification.txt` توضیح داده شده است.
5. `styles.css` دست‌کم پنج انتخابگر مختلف و پنج ویژگی مختلف دارد و به همهٔ صفحه‌ها وصل است.
6. دست‌کم یک امکان جاوااسکریپت (مثلاً رویداد، هشدار یا زمان‌سنج) کار می‌کند.
7. سایت را در حالت موبایل ابزار توسعه‌دهنده دیده‌ام و به‌هم‌ریخته نیست.
8. `specification.txt` ده تگ، پنج ویژگی و یک جمله دربارهٔ جاوااسکریپت و Bootstrap دارد.
9. HTML هر صفحه را در اعتبارسنج W3C گذاشته‌ام و هیچ خطا یا هشداری نمانده است.
10. سبک‌ها در فایل CSS جدا هستند، نه پراکنده در ویژگی `style`.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با `http-server` و چک‌لیست بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/homepage
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [مستندات Bootstrap 5.3](https://getbootstrap.com/docs/5.3/): مرجع رسمی Bootstrap که صفحهٔ Homepage پیشنهاد می‌کند.
- [سرویس اعتبارسنجی W3C](https://validator.w3.org/#validate_by_input): ابزاری که صفحهٔ رسمی برای سنجش معتبر بودن HTML معرفی می‌کند.

## پیوند رسمی

- [Homepage](https://cs50.harvard.edu/x/2026/psets/8/homepage/)
- [پرابلم‌ست ۸](https://cs50.harvard.edu/x/psets/8/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
