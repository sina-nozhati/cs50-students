---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-pr-redo
type: practice-guide
title: راهنمای بازطراحی Radio Shack (Redo)
title_fa: بازطراحی Radio Shack (Redo)
title_en: Radio Shack Redo
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/redo/
source_refs:
- src-practice-redo#background
- src-practice-redo#implementation-details
- src-anzali-authored-8
concept_ids:
- w08-c-web-history
- w08-c-http-server
- w08-c-bootstrap
- w08-c-bootstrap-navbar
- w08-c-responsive
- w08-c-markup-validation
- w08-c-table
problem_set_ref: weeks/week-08/problem-sets/redo.json
prev: w08-ps-homepage
next: null
order: 28
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای بازطراحی Radio Shack (Redo)

> **منبع رسمی:** [Radio Shack Redo](https://cs50.harvard.edu/x/2026/practice/redo/) از مسئله‌های تمرینی هفتهٔ ۸ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

وب آن‌طور که می‌شناسیم فقط از میانهٔ دههٔ ۱۹۹۰ وجود دارد. ابزارهای آن زمان محدود بودند: CSS و جاوااسکریپت نبود و هر مرورگر HTML را جور دیگری نمایش می‌داد. نخستین وب‌سایت RadioShack (۱۹۹۶) دکمه‌های زمخت و پس‌زمینهٔ تکراری داشت و دکمه‌هایش در واقع یک تصویر بزرگ با `map` بودند. نسخهٔ ۱۹۹۷ همهٔ صفحه را با یک جدول و تصویر شفاف یک‌پیکسلی (`dot_clear.gif`) چیده بود.

کار تو بازطراحی صفحهٔ اصلی RadioShack با ابزارهای امروزی در پوشهٔ `radiotoday/` است: بدون جدول، بدون `map` و بدون لوگوی چرخان. صفحهٔ رسمی پیشنهاد می‌کند با نوار پیمایش (Navbar) Bootstrap شروع کنی و سپس ستون‌ها، تصویرهای واکنش‌گرا و چرخ‌فلک (carousel) را امتحان کنی. طراحی با خودت است.

> **توجه (d137، d138، d147):** این مسئلهٔ تمرینی از آزمایشگاه‌های CS50 پاییز ۲۰۲۲ آمده است؛ فایل آغازین نشانی ۲۰۲۲ دارد و پیوندهای Bootstrap آن به نسخهٔ 5.2 می‌روند. صفحهٔ رسمی می‌گوید check50 ندارد و تحویل لازم نیست.

> **از سخنرانی:** Bootstrap و کلاس‌های آماده در [یادداشت چارچوب‌ها](/kb/d/w08-n12)؛ اعتبارسنجی HTML در [راهنمای Homepage](/kb/d/w08-ps-homepage).

## خواسته‌های رسمی

1. صفحهٔ اصلی RadioShack را با ابزارهای امروزی توسعهٔ وب بازطراحی کن (فقط صفحهٔ اصلی کافی است).
2. جدول، `map` و لوگوی چرخان نه!
3. نسخهٔ خودت را در پوشهٔ `radiotoday/` بساز.
4. با امکان Navbar در Bootstrap شروع کن و گزینه‌های منو را به گزینه‌های مناسب صفحهٔ RadioShack تغییر بده.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. سه پوشه دریافت می‌کنی: `radio1996/`، `radio1997/` و `radiotoday/`. دو پوشهٔ اول نسخه‌های تاریخی‌اند که می‌توانی کاوششان کنی؛ کار خودت در `radiotoday/` است.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/8/redo.zip
unzip redo.zip
rm redo.zip
```

## فرمان‌ها و قطعه‌های رسمی صفحه

> **رسمی:** این فرمان‌ها و قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند.

نقشهٔ تصویر (`map`) صفحهٔ ۱۹۹۶، فقط برای شناخت تاریخ؛ در بازطراحی به کار نبر:

```html
<map name="rsmap">
<area shape="rect" coords="8,246,122,297" href="https://www.radioshack.com/rsstorelocator/rszip?1">
<area shape="rect" coords="123,246,240,297" href="https://www.radioshack.com/rsfuture.html">
<area shape="rect" coords="241,246,358,297" href="https://www.tandy.com/contacts/">
<area shape="rect" coords="359,246,475,297" href="https://www.tandy.com/press.html">
<area shape="rect" coords="476,246,599,297" href="https://www.radioshack.com/history/">
</map>
```

نوار پیمایش سادهٔ Bootstrap که صفحهٔ رسمی پیشنهاد می‌کند در بالای `body` فایل `index.html` بگذاری:

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

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- طراحی وب دههٔ ۹۰: جدول برای چیدمان و تصویر به جای قلم — [یادداشت](/kb/d/w08-pr-redo)
- اجرای http-server و درگاه 8080 — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- Bootstrap: افزودن با link و استفاده از کلاس‌هایش مثل table — [یادداشت](/kb/d/w08-n12) · درس کوتاه `w08-l05` (واحد `w08-l05-u03`)
- navbar و ستون‌های Bootstrap به جای جدول — [یادداشت](/kb/d/w08-pr-redo)
- ظاهر مناسب روی تلفن همراه و رایانه — [یادداشت](/kb/d/w08-ps-homepage)
- بررسی درستی HTML با Markup Validation Service — [یادداشت](/kb/d/w08-ps-homepage)
- جدول با table، tr و td — [یادداشت](/kb/d/w08-n08) · درس کوتاه `w08-l03` (واحد `w08-l03-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول فایل‌های `radio1996/index.html` و `radio1997/index.html` را باز کن و ببین چیدمان چطور با جدول و تصویر ساخته شده است. همین تفاوت هدف مسئله است.
2. نوار پیمایش رسمی را بگذار و فقط متن گزینه‌ها را عوض کن. اگر صفحهٔ دیگری نمی‌سازی، `href` می‌تواند `#` بماند.
3. برای چیدمان چندستونی، صفحهٔ «columns» مستندات Bootstrap را ببین؛ به جای جدول، از کلاس‌های ردیف و ستون استفاده می‌شود.
4. اندازهٔ پنجره را تغییر بده یا حالت موبایل ابزار توسعه‌دهنده را روشن کن و ببین تصویرها و ستون‌ها چطور رفتار می‌کنند.

## اشتباه‌های رایج

- چیدن صفحه با `<table>` مثل ۱۹۹۷
- فراموش کردن پیوند CSS و JS Bootstrap در `<head>`
- باقی گذاشتن گزینه‌های نمونهٔ Features و Pricing
- ساختن صفحه در پوشهٔ اشتباه

## چک‌لیست خودآزمایی

1. صفحه‌ام در `radiotoday/index.html` است و با `http-server` باز می‌شود.
2. هیچ `<table>`، `<map>` یا لوگوی چرخانی برای چیدمان به کار نرفته است.
3. نوار پیمایش Bootstrap دارم و گزینه‌هایش مال RadioShack است، نه Features و Pricing.
4. چیدمان با ستون‌های Bootstrap است و در حالت موبایل هم درست دیده می‌شود.
5. HTML را در اعتبارسنج W3C آزموده‌ام.
6. به پرسش فکری پاسخ داده‌ام.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با `http-server` و چک‌لیست بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: به نظرت چرا این‌همه طراح به جای نوشتن CSS خودشان از Bootstrap استفاده می‌کنند؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [نمونهٔ کد جدول ۱۹۹۷ در صفحهٔ رسمی](https://cs50.harvard.edu/x/practice/redo/#background): این بلوک ناقص است (با `...` بریده شده) و فقط نمونهٔ تاریخی است؛ بازتولید نشده است.
- [طراحی‌های دیگر دههٔ ۹۰](https://www.justinmind.com/blog/10-90s-websites-designs-you-wont-believe-existed/): پیوند بیرونی صفحهٔ رسمی.

## پیوند رسمی

- [Radio Shack Redo](https://cs50.harvard.edu/x/2026/practice/redo/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
