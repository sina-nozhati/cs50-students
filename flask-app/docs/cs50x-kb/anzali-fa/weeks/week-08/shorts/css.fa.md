---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-css
type: short-summary
title: 'ویدئوی کوتاه: CSS (CSS)'
title_fa: CSS
title_en: CSS
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/css/
source_refs:
- src-short-css
- src-anzali-inference-8
concept_ids:
- w08-c-css
- w08-c-css-property
- w08-c-selectors
- w08-c-style-tag
- w08-c-external-css
prev: w08-sh-html
next: w08-sh-javascript
order: 23
video:
  youtube_id: Ub3FKU21ubk
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: CSS برای ظاهر'
    evidence_en: null
  - start: '1:36'
    start_seconds: 96
    title_fa: ساختار یک قاعده
    evidence_en: selector
  - start: '2:19'
    start_seconds: 139
    title_fa: حاشیه و رنگ
    evidence_en: border
  - start: '3:39'
    start_seconds: 219
    title_fa: قلم و تراز متن
    evidence_en: font size
  - start: '5:26'
    start_seconds: 326
    title_fa: انتخابگر شناسه و کلاس
    evidence_en: ID selector
  - start: '6:46'
    start_seconds: 406
    title_fa: style یا فایل جدا
    evidence_en: two options for writing stylesheets
  - start: '8:34'
    start_seconds: 514
    title_fa: جدول ضرب با CSS
    evidence_en: table2
  - start: '9:53'
    start_seconds: 593
    title_fa: فایل table.css
    evidence_en: table3
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: CSS (CSS)

> **منبع رسمی:** [صفحهٔ Short «CSS» در CS50x](https://cs50.harvard.edu/x/shorts/css/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

اگر HTML محتوای صفحه را سازمان می‌دهد، CSS (Cascading Style Sheets) ظاهر آن را تعیین می‌کند. CSS هم زبان برنامه‌نویسی نیست. هر **قاعده** یک **انتخابگر** دارد (مثل `body`) و بین آکولادها فهرستی از جفت‌های «ویژگی: مقدار» که هر کدام یک **اعلان** است و با `;` جدا می‌شود؛ مثلاً `background-color: blue;`.

ویژگی‌های رایج: `border` (سبک، رنگ و پهنا)، `background-color` و `color` با نام رنگ یا شش رقم شانزده‌شانزدهی مثل `#ff0000`، `font-size` با کلیدواژه، pt، درصد یا `smaller`، `font-family` با قلم‌های امن وب مثل Arial و Georgia، و `text-align` (چپ، راست، وسط و تراز دوطرفه).

انتخابگرها سه نوع‌اند: **نوع** (`body`)، **شناسه** با `#` که فقط عنصری با آن `id` را می‌گیرد، و **کلاس** با `.` که روی چند عنصر با یک `class` اثر دارد. CSS را می‌شود در تگ `<style>` درون `<head>` نوشت یا، بهتر، در فایل جدای `.css` که با `<link rel="stylesheet">` وصل می‌شود؛ شبیه `#include` در C. نمونهٔ پایانی جدول ضرب ۴ در ۴ است: `border` روی `table` فقط دور جدول را می‌گیرد، و برای خانه‌ها باید `td` را هدف گرفت. توضیح در CSS فقط `/* */` است.

## نکته‌های کلیدی

- قاعده = انتخابگر + اعلان‌های «ویژگی: مقدار;» بین آکولادها.
- رنگ با نام یا `#` و شش رقم شانزده‌شانزدهی.
- انتخابگر نوع، شناسه (`#`) و کلاس (`.`).
- CSS در `<style>` یا، بهتر، در فایل `.css` با `<link>`.
- سبکِ `table` فقط خود جدول را می‌گیرد؛ خانه‌ها `td` هستند.
- توضیح در CSS فقط `/* ... */` است.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`css.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: CSS برای ظاهر](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=0s)
- [۱:۳۶ — ساختار یک قاعده](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=96s)
- [۲:۱۹ — حاشیه و رنگ](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=139s)
- [۳:۳۹ — قلم و تراز متن](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=219s)
- [۵:۲۶ — انتخابگر شناسه و کلاس](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=326s)
- [۶:۴۶ — style یا فایل جدا](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=406s)
- [۸:۳۴ — جدول ضرب با CSS](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=514s)
- [۹:۵۳ — فایل table.css](https://www.youtube.com/watch?v=Ub3FKU21ubk&t=593s)

> [!NOTE]
> **یادداشت (d154)**
> ویدئو سبک `ridge` حاشیه را «خط موج‌دار» می‌نامد؛ `ridge` در واقع حاشیه‌ای برجسته و سه‌بعدی‌نماست (استنتاجی، از مرجع CSS). ویدئو همچنین ویژگی `opacity` را «تگ» می‌نامد؛ `opacity` یک ویژگی CSS است.

## مفاهیم مرتبط

- CSS: زبان سبک برای ظاهر صفحه — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u01`)
- ویژگی CSS به شکل کلید: مقدار، مثل font-size و text-align — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u01`)
- انتخابگر: نوع تگ، کلاس (.name) و شناسه (#name) — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u02`)
- تگ style در head — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u02`)
- فایل CSS جدا با <link href rel="stylesheet"> — [یادداشت](/kb/d/w08-n11) · درس کوتاه `w08-l05` (واحد `w08-l05-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/Ub3FKU21ubk) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/css/css.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/css/lang/en/css.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/css/lang/en/css.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
