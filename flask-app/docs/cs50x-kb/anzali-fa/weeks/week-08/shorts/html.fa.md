---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-html
type: short-summary
title: 'ویدئوی کوتاه: HTML (HTML)'
title_fa: HTML
title_en: HTML
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/html/
source_refs:
- src-short-html
- src-anzali-inference-8
concept_ids:
- w08-c-html
- w08-c-tag
- w08-c-attribute
- w08-c-doctype-structure
- w08-c-whitespace-ignored
- w08-c-headings
- w08-c-lists
- w08-c-table
- w08-c-form
- w08-c-anchor-link
- w08-c-void-elements
- w08-c-html-comment
- w08-c-div
prev: w08-sh-http
next: w08-sh-css
order: 22
video:
  youtube_id: YK78KhMf7bs
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: HTML یک زبان نشانه‌گذاری'
    evidence_en: null
  - start: '2:39'
    start_seconds: 159
    title_fa: 'صفحهٔ ساده: head و body'
    evidence_en: head tag
  - start: '4:21'
    start_seconds: 261
    title_fa: فاصله‌ها اهمیتی ندارند
    evidence_en: white space is data
  - start: '5:27'
    start_seconds: 327
    title_fa: 'ابزار توسعه‌دهنده: Elements'
    evidence_en: Elements tab
  - start: '6:20'
    start_seconds: 380
    title_fa: b، i، u
    evidence_en: B tags
  - start: '7:18'
    start_seconds: 438
    title_fa: بند و سرعنوان
    evidence_en: paragraph tags
  - start: '9:23'
    start_seconds: 563
    title_fa: فهرست‌ها
    evidence_en: unordered lists
  - start: '10:56'
    start_seconds: 656
    title_fa: جدول
    evidence_en: table of information
  - start: '12:49'
    start_seconds: 769
    title_fa: فرم و div
    evidence_en: HTML form
  - start: '16:17'
    start_seconds: 977
    title_fa: پیوند و تصویر
    evidence_en: hyperlinks
  - start: '17:14'
    start_seconds: 1034
    title_fa: DOCTYPE و توضیح
    evidence_en: doctype
  - start: '20:04'
    start_seconds: 1204
    title_fa: HTML خوش‌ساخت
    evidence_en: well formed
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: HTML (HTML)

> **منبع رسمی:** [صفحهٔ Short «HTML» در CS50x](https://cs50.harvard.edu/x/shorts/html/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

HTML (Hypertext Markup Language) زبان است، اما زبان **برنامه‌نویسی** نیست: متغیر، منطق و تابع ندارد. با **تگ‌ها** متن را نشانه‌گذاری می‌کند تا مرورگر بداند هر بخش را چطور نمایش بدهد. صفحهٔ نمونه `<html>`، `<head>` با `<title>` (که در زبانهٔ مرورگر دیده می‌شود) و `<body>` با محتوای دیدنی دارد. فاصله‌ها و تورفتگی اهمیتی ندارند؛ فقط ترتیب باز و بسته شدن تگ‌ها مهم است.

سپس تگ‌های رایج: `<b>`، `<i>` و `<u>`؛ `<p>` برای بند (چون Enter نادیده گرفته می‌شود)؛ `<h1>` تا `<h6>`؛ `<ul>` و `<ol>` با `<li>`، و ویژگی `start` برای شروع شماره از عددی دیگر؛ جدول با `<table>`، `<tr>` و `<td>` (td یعنی «دادهٔ جدول»)؛ `<div>` برای بخشی دلخواه بدون نشانهٔ دیداری؛ و `<form>` با `<input>`‌هایی از نوع text، password، radio، checkbox و submit.

`<input>` و `<img>` تگ بسته ندارند. پیوند با `<a href=...>` ساخته می‌شود (a یعنی anchor؛ تگ `<link>` چیز دیگری است)، چه درونی (`hello.html`) چه بیرونی (`https://...`). `<!DOCTYPE html>` اعلام می‌کند صفحه HTML5 است و `<!-- -->` توضیح است. در پایان: HTML باید **خوش‌ساخت** باشد و تگ‌ها به ترتیب عکس بسته شوند. خطای نحوی همیشه صفحه را خراب نمی‌کند، پس از اعتبارسنج آنلاین کمک بگیر.

## نکته‌های کلیدی

- HTML زبان نشانه‌گذاری است، نه برنامه‌نویسی.
- `<head>` اطلاعات صفحه را دارد و `<body>` محتوای دیدنی را.
- فاصله و تورفتگی در HTML اثری ندارند؛ برای بند جدید `<p>` لازم است.
- فهرست با `<ul>` یا `<ol>` و `<li>`؛ جدول با `<table>`، `<tr>` و `<td>`.
- پیوند با `<a href>`؛ `<img>` و `<input>` تگ بسته ندارند.
- تگ‌ها را به ترتیب عکس ببند و صفحه را با اعتبارسنج بررسی کن.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`html.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: HTML یک زبان نشانه‌گذاری](https://www.youtube.com/watch?v=YK78KhMf7bs&t=0s)
- [۲:۳۹ — صفحهٔ ساده: head و body](https://www.youtube.com/watch?v=YK78KhMf7bs&t=159s)
- [۴:۲۱ — فاصله‌ها اهمیتی ندارند](https://www.youtube.com/watch?v=YK78KhMf7bs&t=261s)
- [۵:۲۷ — ابزار توسعه‌دهنده: Elements](https://www.youtube.com/watch?v=YK78KhMf7bs&t=327s)
- [۶:۲۰ — b، i، u](https://www.youtube.com/watch?v=YK78KhMf7bs&t=380s)
- [۷:۱۸ — بند و سرعنوان](https://www.youtube.com/watch?v=YK78KhMf7bs&t=438s)
- [۹:۲۳ — فهرست‌ها](https://www.youtube.com/watch?v=YK78KhMf7bs&t=563s)
- [۱۰:۵۶ — جدول](https://www.youtube.com/watch?v=YK78KhMf7bs&t=656s)
- [۱۲:۴۹ — فرم و div](https://www.youtube.com/watch?v=YK78KhMf7bs&t=769s)
- [۱۶:۱۷ — پیوند و تصویر](https://www.youtube.com/watch?v=YK78KhMf7bs&t=977s)
- [۱۷:۱۴ — DOCTYPE و توضیح](https://www.youtube.com/watch?v=YK78KhMf7bs&t=1034s)
- [۲۰:۰۴ — HTML خوش‌ساخت](https://www.youtube.com/watch?v=YK78KhMf7bs&t=1204s)

> [!NOTE]
> **یادداشت (d143، d149)**
> ویدئو `<input>` و `<img>` را «خودبسته» با `/` پیش از `>` معرفی می‌کند؛ در HTML5 این‌ها عنصرهای تهی (void) هستند و `/` اختیاری است. همچنین می‌گوید بدون DOCTYPE نمی‌شود از تگ‌های HTML5 استفاده کرد؛ در واقع مرورگر به «حالت سازگاری» (quirks mode) می‌رود. ویدئو اول می‌گوید سرعنوان‌ها «بزرگ‌تر و بزرگ‌تر» می‌شوند و بلافاصله اصلاح می‌کند: `<h1>` بزرگ‌ترین و `<h6>` کوچک‌ترین است.

> [!TIP]
> **نکته (d141)**
> نمونه‌های ویدئو در CS50 IDE قدیم با «Preview» دیده می‌شوند و فرم‌ها به ویدئوی PHP حواله داده می‌شوند. در CS50x 2026 صفحه را با `http-server` در codespace باز می‌کنی و فرم‌ها در هفتهٔ ۹ با Flask پردازش می‌شوند.

## مفاهیم مرتبط

- HTML: زبان نشانه‌گذاری با تگ و ویژگی — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- تگ آغاز و پایان، مثل <p> و </p> — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- ویژگی (attribute) مثل lang که رفتار تگ را تغییر می‌دهد — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- ساختار سند: DOCTYPE، html، head، title و body — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- فاصله و تورفتگی در HTML نادیده گرفته می‌شود؛ پاراگراف با <p> — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- سرعنوان‌ها از h1 تا h6 — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u02`)
- فهرست بی‌ترتیب ul و باترتیب ol با li — [یادداشت](/kb/d/w08-n08) · درس کوتاه `w08-l03` (واحد `w08-l03-u02`)
- جدول با table، tr و td — [یادداشت](/kb/d/w08-n08) · درس کوتاه `w08-l03` (واحد `w08-l03-u02`)
- فرم: form با action و method — [یادداشت](/kb/d/w08-n09) · درس کوتاه `w08-l04` (واحد `w08-l04-u01`)
- پیوند با تگ a و ویژگی href — [یادداشت](/kb/d/w08-n08) · درس کوتاه `w08-l03` (واحد `w08-l03-u03`)
- عنصرهای بدون تگ پایان مثل img و input — [یادداشت](/kb/d/w08-n08) · درس کوتاه `w08-l03` (واحد `w08-l03-u03`)
- توضیح در HTML با <!-- --> — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- div برای تقسیم صفحه به ناحیه‌ها — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/YK78KhMf7bs) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/html/html.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/html/lang/en/html.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/html/lang/en/html.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
