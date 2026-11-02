---
id: w08-n07
type: note
title: 'HTML: تگ، ویژگی و درخت سند (HTML: Tags, Attributes and the Tree)'
title_fa: 'HTML: تگ، ویژگی و درخت سند'
title_en: 'HTML: Tags, Attributes and the Tree'
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: HTML
official_anchor: html
source_url: https://cs50.harvard.edu/x/2026/notes/8/#html
source_refs:
- src-notes-8#html
- src-transcript-8
- src-short-html
- src-html-spec
- src-markup-validator
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-html
- w08-c-tag
- w08-c-attribute
- w08-c-doctype-structure
- w08-c-html-comment
- w08-c-http-server
- w08-c-dom-tree
- w08-c-whitespace-ignored
- w08-c-headings
prev: w08-n06
next: w08-n08
order: 7
video:
  youtube_id: yYst7puZXjw
  start: '39:50'
  start_seconds: 2390
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=2390s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'hypertext markup language,'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# HTML: تگ، ویژگی و درخت سند

> **منبع رسمی:** بخش «HTML» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#html). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۹:۵۰ تا حدود ۵۹:۴۹](https://www.youtube.com/watch?v=yYst7puZXjw&t=2390s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هر صفحه‌ای که در مرورگر می‌بینی، از جست‌وجوی گوگل تا صفحهٔ خانگی‌ای که در مجموعه‌تمرین این هفته می‌سازی، در نهایت یک فایل متنی **HTML** است. HTML زبان برنامه‌نویسی نیست؛ **زبان نشانه‌گذاری** (`markup language`) است: حلقه و شرط ندارد، فقط می‌گوید هر تکه از صفحه چیست.

## برچسب‌ها و ویژگی‌ها

- **HTML** یا **زبان نشانه‌گذاری ابرمتن** (`hypertext markup language`) از **برچسب‌ها** (`tag`) ساخته شده است و هر برچسب ممکن است چند **ویژگی** (`attribute`) داشته باشد که آن را توصیف می‌کنند.
- در ترمینال بنویس `code hello.html` و این کد را بنویس:

```html
<!DOCTYPE html>

<!-- Demonstrates HTML -->

<html lang="en">
    <head>
        <title>hello, title</title>
    </head>
    <body>
        hello, body
    </body>
</html>
```

- برچسب `html` فایل را هم باز می‌کند و هم می‌بندد. ویژگی `lang` رفتار برچسب `html` را تغییر می‌دهد. برچسب‌های `head` و `body` هم هستند. تورفتگی لازم نیست، اما سلسله‌مراتب را نشان می‌دهد.

> [!TIP]
> **تألیفی: یک ترفند برای خواندن**
> `head` چیزهایی است که دربارهٔ صفحه است (مثل عنوانی که روی زبانهٔ مرورگر می‌آید) و `body` چیزهایی که درون صفحه دیده می‌شود. `<!DOCTYPE html>` در سطر اول به مرورگر می‌گوید این سند HTML نسخهٔ ۵ است. برای صفحه‌ای فارسی، همین ساختار با `lang="fa"` و `dir="rtl"` روی برچسب `html` کار می‌کند.

## اجرای سرور

- می‌توانی کدت را با نوشتن `http-server` ارائه کنی. محتوای ارائه‌شده روی یک نشانی بسیار بلند در دسترس است؛ اگر رویش کلیک کنی، وب‌سایتی را که کد خودت ساخته می‌بینی.
- در این نشانی، نام فایل `hello.html` در انتها می‌آید. همچنین از روی نشانی پیداست که سرور از درگاه `8080` استفاده می‌کند.

> [!NOTE]
> **از سخنرانی: چرا 8080 و نه 80؟**
> دیوید می‌گوید درگاه ۸۰ برای HTTP پیش‌فرض است، اما ده‌ها هزار شمارهٔ درگاه دیگر هم می‌شود به کار برد؛ برنامهٔ `http-server` در cs50.dev روی ۸۰۸۰ گوش می‌دهد. این همان مفهوم درگاه از [یادداشت ۳](/kb/d/w08-n03) است.

## سلسله‌مراتب: درخت

- سلسله‌مراتب برچسب‌ها را می‌توان به شکل درخت نشان داد: `html` ریشه است، `head` و `body` فرزندان آن‌اند و `title` فرزند `head`.
- دانستن این سلسله‌مراتب بعداً، وقتی جاوااسکریپت یاد می‌گیریم، به کار می‌آید.
- مرورگر فایل HTML را از بالا به پایین و از چپ به راست می‌خواند.

نمودار تألیفی زیر همان درخت را برای `hello0` نشان می‌دهد؛ تألیفی
```text
html
├── head
│   └── title
│       └── hello, title
└── body
    └── hello, body
```

> [!WARNING]
> **از ویدئوی کوتاه: برچسب‌ها را درست تودرتو کن**
> داگ لوید در [ویدئوی HTML](/kb/d/w08-sh-html) تأکید می‌کند که برچسبی که آخر باز شده باید اول بسته شود؛ مثل پرانتزها. `<b><i>x</b></i>` نادرست است و `<b><i>x</i></b>` درست. مرورگرها بسیار بخشنده‌اند و صفحهٔ نادرست را هم نشان می‌دهند، پس برای پیدا کردن چنین خطاهایی از **اعتبارسنج** (`validator`) استفاده کن.

> [!NOTE]
> **از ویدئوی کوتاه: نکتهٔ نسخه (d143)**
> آن ویدئو از ۲۰۱۷ است و برچسب‌هایی مثل `input` را «خودبسته» (self-closing) با `/>` معرفی می‌کند. در HTML5 این عناصر **عنصر تهی** (`void element`) نام دارند و نیازی به `/` ندارند؛ کدهای درس‌نامهٔ ۲۰۲۶ هم بدون آن نوشته شده‌اند.

## اشتباه‌های رایج

- جا انداختن `<!DOCTYPE html>`؛ مرورگر صفحه را در حالت سازگاری قدیمی (quirks mode) نشان می‌دهد.
- گذاشتن محتوای دیدنی در `head` به جای `body`.
- بستن برچسب‌ها با ترتیب نادرست.

## جمع‌بندی

- HTML زبان نشانه‌گذاری است: برچسب‌ها با ویژگی‌ها.
- هر سند `<!DOCTYPE html>`، `html`، `head` (با `title`) و `body` دارد.
- `http-server` صفحه‌ها را روی درگاه ۸۰۸۰ ارائه می‌کند.
- برچسب‌ها درختی می‌سازند که بعداً با جاوااسکریپت دست‌کاری می‌کنیم.

## پیوندها

- قبلی: [HTTP و HTTPS: نشانی، درخواست و کد وضعیت](/kb/d/w08-n06)
- بعدی: [فهرست، جدول، تصویر، ویدئو و پیوند](/kb/d/w08-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
