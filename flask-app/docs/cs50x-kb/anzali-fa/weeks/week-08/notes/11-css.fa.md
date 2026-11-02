---
id: w08-n11
type: note
title: 'CSS: ویژگی، انتخابگر و آبشار (CSS)'
title_fa: 'CSS: ویژگی، انتخابگر و آبشار'
title_en: CSS
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: CSS
official_anchor: css
source_url: https://cs50.harvard.edu/x/2026/notes/8/#css
source_refs:
- src-notes-8#css
- src-short-css
- src-pset-8
- src-pset-8-homepage
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-css
- w08-c-css-property
- w08-c-style-attr
- w08-c-div
- w08-c-cascade
- w08-c-semantic-tags
- w08-c-selectors
- w08-c-style-tag
- w08-c-external-css
- w08-c-html-entity
prev: w08-n10
next: w08-n12
order: 11
video:
  youtube_id: yYst7puZXjw
  start: '1:29:39'
  start_seconds: 5379
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=5379s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'namely something called CSS'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# CSS: ویژگی، انتخابگر و آبشار

> **منبع رسمی:** بخش «CSS» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#css). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۹:۳۹ تا حدود ۱:۴۴:۲۸](https://www.youtube.com/watch?v=yYst7puZXjw&t=5379s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

HTML می‌گوید هر چیز چیست؛ اما رنگ، اندازه، فاصله و چیدمان را نمی‌گوید. **CSS** این کار را می‌کند. و همان درسی که از هفتهٔ ۱ دربارهٔ طراحی خوب گرفتیم، یعنی پرهیز از تکرار، اینجا هم مستقیم به کار می‌آید.

## CSS و ویژگی‌ها

- **CSS** یا **برگه‌های سبک آبشاری** (`cascading style sheets`) زبانی برای سبک‌دهی است که اجازه می‌دهد ظاهر فایل‌های HTML را دقیق تنظیم کنی.
- CSS پر از **ویژگی‌ها** (`property`) است که به شکل جفت‌های کلید و مقدارند.
- در ترمینال بنویس `code home.html`:

```html
<!DOCTYPE html>

<!-- Demonstrates inline CSS with P tags -->

<html lang="en">
    <head>
        <title>css</title>
    </head>
    <body>
        <p style="font-size: large; text-align: center;">
            John Harvard
        </p>
        <p style="font-size: medium; text-align: center;">
            Welcome to my home page!
        </p>
        <p style="font-size: small; text-align: center;">
            Copyright &#169; John Harvard
        </p>
    </body>
</html>
```

- به برچسب‌های `<p>` ویژگی `style` داده شده است. `font-size` روی `large`، `medium` یا `small` و `text-align` روی center تنظیم شده است.

## پرهیز از تکرار

- کد بالا درست است، اما خوب طراحی نشده. می‌توانیم تکرار را حذف کنیم:

```html
<!DOCTYPE html>

<!-- Removes outer DIV -->

<html lang="en">
    <head>
        <title>css</title>
    </head>
    <body style="text-align: center">
        <div style="font-size: large">
            John Harvard
        </div>
        <div style="font-size: medium">
            Welcome to my home page!
        </div>
        <div style="font-size: small">
            Copyright &#169; John Harvard
        </div>
    </body>
</html>
```

- برچسب‌های `<div>` فایل را به بخش‌های مشخص تقسیم می‌کنند. `text-align: center` روی کل `body` اعمال شده است. چون همه‌چیز درون `body` فرزند آن است، این **ویژگی** (نه «attribute»؛ d133) به فرزندان **آبشار** می‌شود.

> [!NOTE]
> **از ویدئوی کوتاه: آبشار یعنی چه**
> داگ لوید در [ویدئوی CSS](/kb/d/w08-sh-css) توضیح می‌دهد که سبکِ یک عنصر به فرزندانش می‌رسد مگر آنکه قاعدهٔ دقیق‌تری آن را بازنویسی کند. نام «آبشاری» از همین می‌آید.

## کلاس‌ها و برچسب style

```html
<!DOCTYPE html>

<!-- Demonstrates class selectors -->

<html lang="en">
    <head>
        <style>

            .centered
            {
                text-align: center;
            }

            .large
            {
                font-size: large;
            }

            .medium
            {
                font-size: medium;
            }

            .small
            {
                font-size: small;
            }

        </style>
        <title>css</title>
    </head>
    <body class="centered">
        <header class="large">
            John Harvard
        </header>
        <main class="medium">
            Welcome to my home page!
        </main>
        <footer class="small">
            Copyright &#169; John Harvard
        </footer>
    </body>
</html>
```

- همهٔ سبک‌ها در `head` درون برچسب `style` قرار گرفته‌اند. به عنصرها **کلاس‌هایی** (`class`) با نام `centered`، `large`، `medium` و `small` داده‌ایم و این کلاس‌ها را با گذاشتن یک نقطه پیش از نام انتخاب می‌کنیم، مثل `.centered`.
- برچسب‌های `header`، `main` و `footer` **برچسب‌های معنایی** (`semantic tag`) تازه‌تر HTML هستند: مثل `div` بخش می‌سازند، اما نامشان می‌گوید هر بخش چه نقشی دارد.

> [!NOTE]
> **استنتاجی: کدام جمله دربارهٔ کدام چیز است (d134)**
> جملهٔ درس‌نامه دربارهٔ این مثال با «برچسب‌های معنایی تازه‌تر» شروع می‌شود، اما توضیحش دربارهٔ برچسب `style` و کلاس‌هاست. در خود کد، برچسب‌های معنایی همان `header`، `main` و `footer` هستند که جای `div`های مثال قبل نشسته‌اند.

> [!TIP]
> **از ویدئوی کوتاه: سه نوع گزینشگر**
> ویدئوی CSS سه نوع **گزینشگر** (`selector`) را نشان می‌دهد: نام برچسب (`body`)، شناسه با `#` (برای یک عنصر یکتا با `id`) و کلاس با `.` (برای چند عنصر). ساختار هر قاعده: گزینشگر، آکولاد باز، جفت‌های `property: value;` و آکولاد بسته. توضیح در CSS فقط به شکل `/* ... */` است.

نمونهٔ تألیفی کوچک از هر سه گزینشگر:
```css
body
{
    color: black;
}

#title
{
    font-size: x-large;
}

.note
{
    background-color: lightyellow;
}
```

## فایل جدا

- می‌توانیم همهٔ کد سبک را به فایل ویژه‌ای به نام فایل *CSS* ببریم. فایلی به نام `style.css` می‌سازیم و کلاس‌ها را آنجا می‌گذاریم:

```css
.centered
{
    text-align: center;
}

.large
{
    font-size: large;
}

.medium
{
    font-size: medium;
}

.small
{
    font-size: small;
}
```

- این دقیقاً همان چیزی است که در فایل HTML بود.
- بعد به مرورگر می‌گوییم CSS این فایل HTML کجاست:

```html
<!DOCTYPE html>

<!-- Demonstrates external stylesheets -->

<html lang="en">
    <head>
        <link href="style.css" rel="stylesheet">
        <title>css</title>
    </head>
    <body class="centered">
        <header class="large">
            John Harvard
        </header>
        <main class="medium">
            Welcome to my home page!
        </main>
        <footer class="small">
            Copyright &#169; John Harvard
        </footer>
    </body>
</html>
```

- `style.css` به‌عنوان یک برگهٔ سبک (`stylesheet`) به این فایل HTML پیوند داده شده است.

> [!IMPORTANT]
> **تألیفی: چرا فایل جدا**
> با یک `style.css` مشترک، همهٔ صفحه‌های سایت یک ظاهر دارند و اگر رنگی را عوض کنی، فقط یک جا را ویرایش می‌کنی. مجموعه‌تمرین Homepage دقیقاً همین را می‌خواهد: دست‌کم چهار صفحه و دست‌کم یک فایل سبک ساختهٔ خودت (`styles.css`).

## اشتباه‌های رایج

- تکرار همان `style` روی ده عنصر به جای یک کلاس.
- جا انداختن نقطه پیش از نام کلاس در گزینشگر، یا گذاشتن نقطه در ویژگی `class` خود HTML.
- استفاده از `id` تکراری؛ هر `id` باید در صفحه یکتا باشد.
- نوشتن توضیح با `//` در CSS؛ CSS فقط `/* */` را می‌شناسد.

## جمع‌بندی

- CSS ویژگی‌های کلید و مقدار است: `font-size`، `text-align`، `color` و ...
- سبک‌ها از والد به فرزند آبشار می‌شوند.
- سه جای نوشتن CSS: ویژگی `style`، برچسب `style` در `head` و فایل جدا با `link`.
- گزینشگرها: نام برچسب، `#id` و `.class`.

## پیوندها

- قبلی: [عبارت باقاعده و اعتبارسنجی فرم](/kb/d/w08-n10)
- بعدی: [چارچوب‌ها: Bootstrap](/kb/d/w08-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
