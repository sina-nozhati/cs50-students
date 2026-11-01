---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-dom
type: short-summary
title: 'ویدئوی کوتاه: DOM (DOM)'
title_fa: DOM
title_en: DOM
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/dom/
source_refs:
- src-short-dom
- src-anzali-inference-8
concept_ids:
- w08-c-dom-tree
- w08-c-dom-navigation
- w08-c-innerhtml
- w08-c-style-property
- w08-c-queryselector
- w08-c-click-event
prev: w08-sh-javascript
next: w08-ps-trivia
order: 25
video:
  youtube_id: LKWJpgvfH3U
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: شیءهای تودرتو'
    evidence_en: null
  - start: 0:12
    start_seconds: 12
    title_fa: شیء document
    evidence_en: document object
  - start: 0:55
    start_seconds: 55
    title_fa: درخت یک صفحهٔ ساده
    evidence_en: tree structure
  - start: '4:18'
    start_seconds: 258
    title_fa: console.dir در مرورگر
    evidence_en: console.dir
  - start: '6:22'
    start_seconds: 382
    title_fa: ویژگی‌های رایج
    evidence_en: InnerHTML
  - start: '8:54'
    start_seconds: 534
    title_fa: روش‌های رایج
    evidence_en: getElementById
  - start: '10:23'
    start_seconds: 623
    title_fa: حرف d کوچک
    evidence_en: lowercase
  - start: '11:20'
    start_seconds: 680
    title_fa: jQuery
    evidence_en: jQuery
  - start: '13:46'
    start_seconds: 826
    title_fa: چهار روش تغییر رنگ
    evidence_en: four different ways
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: DOM (DOM)

> **منبع رسمی:** [صفحهٔ Short «DOM» در CS50x](https://cs50.harvard.edu/x/shorts/dom/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

شیءها می‌توانند شیءهای دیگر را درون خود داشته باشند و درختی بسازند، مثل درخت‌هایی که در C دیدی. **شیء document** کل محتوای یک صفحه را در یک شیء جاوااسکریپت سازمان می‌دهد: `html` فرزند document است، `head` و `body` فرزندان `html`، و همین‌طور تا متن درون هر تگ. داگ لوید با `console.dir(document)` در کنسول کروم ویژگی `children` را باز می‌کند و همین درخت را نشان می‌دهد.

ویژگی‌های رایج هر گره: `innerHTML` (HTML درون تگ)، `nodeName`، `id`، `parentNode`، `childNodes`، `attributes` و `style`. روش‌های رایج: `getElementById`، `getElementsByTagName`، `appendChild` و `removeChild`. هشدار مشهور ویدئو: در `getElementById` حرف d کوچک است و `ID` خطا می‌دهد.

سپس jQuery، کتابخانه‌ای برای کوتاه‌تر نوشتن همان کارها، معرفی می‌شود: `$('#colorDiv').css(...)` به جای زنجیرهٔ بلند جاوااسکریپت خام. نمونهٔ پایانی صفحه‌ای است با چهار دسته دکمه که رنگ پس‌زمینهٔ یک بخش را به چهار روش عوض می‌کنند: پنج تابع جدا، یک تابع با پارامتر رنگ، یک گردانندهٔ رویداد که `innerHTML` دکمه را با `toLowerCase` به نام رنگ تبدیل می‌کند، و نسخهٔ jQuery.

## نکته‌های کلیدی

- شیء document کل صفحه را به شکل درخت نشان می‌دهد.
- `console.dir(document)` درخت را در کنسول نشان می‌دهد.
- ویژگی‌ها: `innerHTML`، `nodeName`، `id`، `parentNode`، `childNodes`، `attributes`، `style`.
- روش‌ها: `getElementById`، `getElementsByTagName`، `appendChild`، `removeChild`.
- در `getElementById` حرف d کوچک است.
- با `style.backgroundColor` رنگ یک عنصر را از جاوااسکریپت عوض می‌کنی.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`dom.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: شیءهای تودرتو](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=0s)
- [۰:۱۲ — شیء document](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=12s)
- [۰:۵۵ — درخت یک صفحهٔ ساده](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=55s)
- [۴:۱۸ — console.dir در مرورگر](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=258s)
- [۶:۲۲ — ویژگی‌های رایج](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=382s)
- [۸:۵۴ — روش‌های رایج](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=534s)
- [۱۰:۲۳ — حرف d کوچک](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=623s)
- [۱۱:۲۰ — jQuery](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=680s)
- [۱۳:۴۶ — چهار روش تغییر رنگ](https://www.youtube.com/watch?v=LKWJpgvfH3U&t=826s)

> [!NOTE]
> **یادداشت (d141)**
> این ویدئو مال ۲۰۱۷ است: jQuery را «احتمالاً محبوب‌ترین کتابخانه» می‌نامد و به ویدئویی دربارهٔ AJAX حواله می‌دهد که جزو این هفته نیست. درس‌نامهٔ ۲۰۲۶ به جای `getElementById` از `querySelector` و `querySelectorAll` استفاده می‌کند و jQuery را درس نمی‌دهد؛ فقط فایل آغازین Homepage آن را بارگذاری می‌کند (d136).

## مفاهیم مرتبط

- درخت سند (DOM): رابطهٔ والد و فرزند بین تگ‌ها — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- parentElement، children و پیمایش درخت DOM — [یادداشت](/kb/d/w08-sh-dom) · درس کوتاه `w08-l07` (واحد `w08-l07-u03`)
- innerHTML برای تغییر محتوای یک عنصر — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l07` (واحد `w08-l07-u01`)
- element.style.backgroundColor: نام camelCase — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l07` (واحد `w08-l07-u02`)
- document.querySelector با انتخابگر CSS — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)
- رویداد click روی دکمه — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l07` (واحد `w08-l07-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/LKWJpgvfH3U) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/dom/dom.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/dom/lang/en/dom.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/dom/lang/en/dom.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
