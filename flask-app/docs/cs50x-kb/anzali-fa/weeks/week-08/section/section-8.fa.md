---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۸ (Section 8)
title_fa: جلسهٔ حل تمرین هفتهٔ ۸
title_en: Section 8
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly, read in full); chapter times from section8.srt (inference for boundaries); one short verbatim excerpt of scoreboard.html (official, uses == as in the file; d150, D70); callout on = vs === authored
source_url: https://cs50.harvard.edu/x/sections/8/
source_refs:
- src-section-8#week-8-html-css-javascript
- src-section-8-transcript
- src-section-8-video
- src-section-8-slides
- src-section-8-code
- src-mdn-js
- src-anzali-inference-8
- src-anzali-authored-8
concept_ids:
- w08-c-http
- w08-c-html
- w08-c-tag
- w08-c-attribute
- w08-c-doctype-structure
- w08-c-lists
- w08-c-div
- w08-c-css
- w08-c-selectors
- w08-c-css-property
- w08-c-devtools-network
- w08-c-javascript
- w08-c-script-tag
- w08-c-js-variables
- w08-c-js-function
- w08-c-queryselector
- w08-c-innerhtml
- w08-c-click-event
- w08-c-js-conditionals
- w08-c-alert
- w08-c-equality-operators
prev: w08-summary
next: w08-sh-internet-primer
order: 17
video:
  youtube_id: coRcSVIx5hc
  chapters:
  - start: 0:18
    start_seconds: 18
    title_fa: خوش‌آمد و مرور HTTP
    evidence_en: first talking about HTTP
  - start: '1:39'
    start_seconds: 99
    title_fa: 'پروژهٔ جلسه: صفحهٔ امتیاز (scoreboard)'
    evidence_en: scoreboard
  - start: '4:52'
    start_seconds: 292
    title_fa: 'ساختار HTML: چیدمان دیداری صفحه'
    evidence_en: structured visually
  - start: '6:16'
    start_seconds: 376
    title_fa: آزمایش با افزودن عنصرها
    evidence_en: experiment by adding some elements
  - start: '9:22'
    start_seconds: 562
    title_fa: فهرست نامرتب (ul)
    evidence_en: unordered list
  - start: '11:49'
    start_seconds: 709
    title_fa: رفتن سراغ CSS
    evidence_en: move to CSS
  - start: '12:55'
    start_seconds: 775
    title_fa: 'انتخابگر شناسه با #'
    evidence_en: pound sign
  - start: '13:52'
    start_seconds: 832
    title_fa: انتخابگر کلاس
    evidence_en: classes which are
  - start: '16:25'
    start_seconds: 985
    title_fa: رنگ پس‌زمینه (background)
    evidence_en: background
  - start: '18:32'
    start_seconds: 1112
    title_fa: ترازبندی متن (text-align)
    evidence_en: text a line
  - start: '21:08'
    start_seconds: 1268
    title_fa: Inspect Element در مرورگر
    evidence_en: inspect element
  - start: '22:41'
    start_seconds: 1361
    title_fa: قلم‌ها (fonts)
    evidence_en: fonts
  - start: '25:12'
    start_seconds: 1512
    title_fa: 'بخش آخر: جاوااسکریپت'
    evidence_en: last piece which is JavaScript
  - start: '28:05'
    start_seconds: 1685
    title_fa: کلیدواژهٔ let
    evidence_en: let keyword
  - start: '31:32'
    start_seconds: 1892
    title_fa: وقتی امتیاز به ۱۰ می‌رسد
    evidence_en: reaches 10
  - start: '33:31'
    start_seconds: 2011
    title_fa: سه علامت مساوی (===)
    evidence_en: 3 equal signs
  - start: '34:21'
    start_seconds: 2061
    title_fa: دو یا یک علامت مساوی
    evidence_en: 2 or 1 equal sign
  chapters_origin: inference
code_files:
- file: scoreboard.html
  policy: excerpt-verbatim
  reason: short official excerpt only; full file linked from src-section-8-code
- file: section8.pdf
  policy: link-only
  reason: slides
---

# جلسهٔ حل تمرین هفتهٔ ۸ (Section)

> **منبع رسمی:** [صفحهٔ Section 8 CS50x](https://cs50.harvard.edu/x/sections/8/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/8/lang/en/section8.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** یا **استنتاجی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، مدرس (preceptor) CS50 در هاروارد، اداره می‌کند و همه‌چیز را روی یک فایل جلو می‌برد: `scoreboard.html`، صفحهٔ امتیاز دو تیم که با `http-server` در codespace باز می‌شود. جلسه چهار بخش دارد: HTTP، HTML، CSS و جاوااسکریپت.

**HTTP و HTML.** Kelly یادآوری می‌کند HTTP یعنی «پروتکل انتقال ابرمتن» و `http-server` روی دستگاه خودت یک سرور می‌سازد. بعد فایل را خط‌به‌خط می‌خواند: `<!DOCTYPE html>`، `lang="en"` که دیده نمی‌شود اما اطلاعات مفیدی است، `<head>` با `<title>` که در زبانهٔ مرورگر دیده می‌شود و `<style>` برای CSS، و `<body>` با یک جدول سه‌سطری (`<tr>` و `<td>`) و یک `<script>`. او ساختار سند را به شکل درخت نشان می‌دهد. سپس با پیشنهاد شرکت‌کننده‌ها عنصر اضافه می‌کند: `<h1>` تا `<h3>`، `<p>`، `<footer>` و یک فهرست. نشان می‌دهد `<ul>` بدون `<li>` فهرستی نمی‌سازد و با عوض کردن `ul` به `ol` گلوله‌ها شماره می‌شوند. وقتی کسی می‌خواهد عنوان وسط‌چین شود، می‌گوید این کار HTML نیست، کار CSS است.

**CSS.** هر قاعده یک انتخابگر و چند ویژگی دارد. انتخابگر نوع مثل `td` همهٔ خانه‌ها را می‌گیرد، شناسه با `#` (مثل `#score1`) فقط یک عنصر را، و کلاس با `.` (مثل `.team`) چند عنصر را. شناسه برای یک عنصر است و کلاس برای چند عنصر. سپس `background-color` را روی `body` امتحان می‌کند و رنگ‌های نام‌دار مثل `blue`، `yellow` و `coral` را نشان می‌دهد. با `text-align: center` و `color: red` عنوان را تغییر می‌دهد، با `margin` میان جدول و بقیهٔ صفحه فاصله می‌گذارد و با ابزار inspect حاشیه‌های پیش‌فرض `<h1>`، `<p>` و `<h3>` را نشان می‌دهد. برای قلم، `font-family` را در w3schools پیدا می‌کند و می‌گوید هیچ‌کس همهٔ ویژگی‌ها را حفظ نیست.

**جاوااسکریپت.** `document.querySelector('#add1')` دکمهٔ تیم ۱ را پیدا می‌کند، `onclick` تابعی را به کلیک وصل می‌کند و `innerHTML` محتوای خانهٔ امتیاز را عوض می‌کند. دو متغیر `team1` و `team2` با `let` ساخته می‌شوند و نوعشان نوشته نمی‌شود. در آخر Kelly شرطی اضافه می‌کند که وقتی امتیاز تیمی به ۱۰ برسد، با `alert` برنده اعلام شود. دربارهٔ `===` می‌گوید برابری سخت‌گیر است. با `==` همان رفتار را می‌بیند، اما با `=` به جای مقایسه انتساب انجام می‌شود و با اولین کلیک پیام برنده نشان داده می‌شود.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section8.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۱۸ — خوش‌آمد و مرور HTTP](https://www.youtube.com/watch?v=coRcSVIx5hc&t=18s)
- [۱:۳۹ — پروژهٔ جلسه: صفحهٔ امتیاز (scoreboard)](https://www.youtube.com/watch?v=coRcSVIx5hc&t=99s)
- [۴:۵۲ — ساختار HTML: چیدمان دیداری صفحه](https://www.youtube.com/watch?v=coRcSVIx5hc&t=292s)
- [۶:۱۶ — آزمایش با افزودن عنصرها](https://www.youtube.com/watch?v=coRcSVIx5hc&t=376s)
- [۹:۲۲ — فهرست نامرتب (ul)](https://www.youtube.com/watch?v=coRcSVIx5hc&t=562s)
- [۱۱:۴۹ — رفتن سراغ CSS](https://www.youtube.com/watch?v=coRcSVIx5hc&t=709s)
- [۱۲:۵۵ — انتخابگر شناسه با #](https://www.youtube.com/watch?v=coRcSVIx5hc&t=775s)
- [۱۳:۵۲ — انتخابگر کلاس](https://www.youtube.com/watch?v=coRcSVIx5hc&t=832s)
- [۱۶:۲۵ — رنگ پس‌زمینه (background)](https://www.youtube.com/watch?v=coRcSVIx5hc&t=985s)
- [۱۸:۳۲ — ترازبندی متن (text-align)](https://www.youtube.com/watch?v=coRcSVIx5hc&t=1112s)
- [۲۱:۰۸ — Inspect Element در مرورگر](https://www.youtube.com/watch?v=coRcSVIx5hc&t=1268s)
- [۲۲:۴۱ — قلم‌ها (fonts)](https://www.youtube.com/watch?v=coRcSVIx5hc&t=1361s)
- [۲۵:۱۲ — بخش آخر: جاوااسکریپت](https://www.youtube.com/watch?v=coRcSVIx5hc&t=1512s)
- [۲۸:۰۵ — کلیدواژهٔ let](https://www.youtube.com/watch?v=coRcSVIx5hc&t=1685s)
- [۳۱:۳۲ — وقتی امتیاز به ۱۰ می‌رسد](https://www.youtube.com/watch?v=coRcSVIx5hc&t=1892s)
- [۳۳:۳۱ — سه علامت مساوی (===)](https://www.youtube.com/watch?v=coRcSVIx5hc&t=2011s)
- [۳۴:۲۱ — دو یا یک علامت مساوی](https://www.youtube.com/watch?v=coRcSVIx5hc&t=2061s)

## کد رسمی جلسه

کد جلسه یک فایل است: [`scoreboard.html`](https://cdn.cs50.net/2025/fall/sections/8/src8/) در [src8.zip](https://cdn.cs50.net/2025/fall/sections/8/src8.zip). این بخش کوچکی از آن است، عیناً از فایل رسمی:

```javascript
document.querySelector('#add1').onclick = function() {
    team1 += 1;
    document.querySelector('#score1').innerHTML = team1;
    if (team1 == 10) {
        alert("Team 1 has won!")
    }
}
```

> [!NOTE]
> **یادداشت**
> فایل منتشرشده `==` دارد، در حالی که Kelly در ویدئو `===` را برابری سخت‌گیر معرفی می‌کند (d150). برای عدد هر دو یک نتیجه می‌دهند؛ این بسته مثل سخنرانی و درس‌نامه `===` را پیشنهاد می‌کند. همچنین در ویدئو گفته می‌شود `em` نسبت به اندازهٔ صفحه حساب می‌شود؛ در واقع `em` نسبت به اندازهٔ قلم عنصر است (d151، استنتاجی). و نام رنگ‌های CSS فاصله ندارند: `lightblue`، نه `light blue` (d152).

> **تألیفی: چرا `=` در شرط فوراً پیام می‌دهد؟**
> `if (team1 = 10)` مقدار ۱۰ را در `team1` می‌گذارد و حاصل عبارت همان ۱۰ است که در شرط «درست» حساب می‌شود. پس شرط همیشه برقرار است. این همان اشتباهی است که در C هم با `=` و `==` دیدی.

## نکته‌های کلیدی

- `<head>` دیده نمی‌شود اما عنوان و سبک صفحه را نگه می‌دارد؛ `<body>` محتوای دیدنی است.
- ساختار HTML درختی است: هر عنصر درون عنصر دیگری است.
- `<ul>` و `<ol>` فقط با `<li>` فهرست می‌سازند.
- وسط‌چین کردن و رنگ کار CSS است، نه HTML.
- انتخابگر نوع همه را می‌گیرد، کلاس (`.`) چند عنصر را و شناسه (`#`) یک عنصر را.
- `querySelector`، `onclick` و `innerHTML` سه ابزار اصلی تغییر صفحه با جاوااسکریپت‌اند.
- در شرط، `===` یا `==` بنویس، نه `=`.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
