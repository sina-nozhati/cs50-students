---
id: w08-n12
type: note
title: 'چارچوب‌ها: Bootstrap (Frameworks)'
title_fa: 'چارچوب‌ها: Bootstrap'
title_en: Frameworks
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Frameworks
official_anchor: frameworks
source_url: https://cs50.harvard.edu/x/2026/notes/8/#frameworks
source_refs:
- src-notes-8#frameworks
- src-transcript-8
- src-pset-8
- src-pset-8-homepage
- src-practice-redo
- src-bootstrap-docs
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-framework
- w08-c-bootstrap
- w08-c-thead-tbody-th
prev: w08-n11
next: w08-n13
order: 12
video:
  youtube_id: yYst7puZXjw
  start: '1:44:28'
  start_seconds: 6268
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=6268s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'most popular frameworks out there nowadays'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# چارچوب‌ها: Bootstrap

> **منبع رسمی:** بخش «Frameworks» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#frameworks). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۴:۲۸ تا حدود ۱:۵۰:۴۴](https://www.youtube.com/watch?v=yYst7puZXjw&t=6268s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

نوشتن CSS از صفر برای هر دکمه و جدول وقت‌گیر است. همان‌طور که در پایتون از کتابخانه‌های دیگران استفاده کردیم، در وب **چارچوب‌ها** (`framework`) آماده‌اند. مجموعه‌تمرین Homepage از تو می‌خواهد دست‌کم از یکی از امکانات Bootstrap استفاده کنی.

## Bootstrap

- مشابه کتابخانه‌های شخص ثالث در پایتون، کتابخانه‌های شخص ثالثی به نام **چارچوب** هست که می‌توانیم در فایل‌های HTML از آن‌ها استفاده کنیم.
- **Bootstrap** یکی از این چارچوب‌هاست که با آن می‌توانیم HTML را زیبا کنیم و عناصر طراحی را به‌سادگی بی‌نقص کنیم تا صفحه‌ها خواناتر شوند.
- با افزودن این برچسب `link` به `head` فایل HTML می‌توان از Bootstrap استفاده کرد:

```html
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <title>bootstrap</title>
</head>
```

> [!NOTE]
> **تألیفی: بخش‌های این برچسب**
> `href` نشانی فایل CSS روی یک **CDN** (شبکهٔ تحویل محتوا) است و نسخه (`5.3.8`) در خود نشانی آمده. `integrity` چکیده‌ای رمزنگاشتی است تا مرورگر مطمئن شود فایل دست‌کاری نشده و `crossorigin` به آن بررسی کمک می‌کند. برچسب `script` بخش جاوااسکریپت Bootstrap را برای اجزای تعاملی (مثل منوهای کشویی) می‌آورد.

## پیش و پس

- این HTML را در نظر بگیر:

```html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>phonebook</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Number</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kelly</td>
                    <td>+1-617-495-1000</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>+1-617-495-1000</td>
                </tr>
                <tr>
                    <td>John</td>
                    <td>+1-949-468-2750</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
```

- نسخهٔ ارائه‌شدهٔ این صفحه بسیار ساده است.
- حالا HTMLی را ببین که از Bootstrap استفاده می‌کند:

```html
<!DOCTYPE html>

<!-- Demonstrates table with Bootstrap -->

<html lang="en">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
        <title>phonebook</title>
    </head>
    <body>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Number</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kelly</td>
                    <td>+1-617-495-1000</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>+1-949-468-2750</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
```

- این وب‌سایت حالا بسیار زیباتر است. تنها تغییرهای مهم: برچسب `link` و `class="table"` روی جدول.

> [!TIP]
> **از سخنرانی: کلاس‌هایی که دیگران نوشته‌اند**
> دیوید Bootstrap را «مجموعه‌ای از کلاس‌های CSS و امکانات دیگر» و متن‌باز معرفی می‌کند. در کلاس، روی جدول نظرهای دانشجوها، با خواندن مستندات و افزودن `class="table table-striped"` جدول راه‌راه ساخت؛ «دو سطر تغییر». یعنی کسی کلاس‌ها را از پیش نوشته و تو فقط نامشان را در ویژگی `class` می‌گذاری؛ به گفتهٔ او این یعنی ایستادن روی شانهٔ دیگران.

> [!WARNING]
> **استنتاجی: نسخه را یکی نگه دار (d137)**
> درس‌نامه نسخهٔ 5.3.8 را می‌آورد، اما صفحهٔ تمرین Redo به مستندات Bootstrap 5.2 پیوند می‌دهد. اگر کلاسی را در مستندات دیدی و کار نکرد، نسخهٔ مستندات را با نسخهٔ `link` صفحه‌ات مقایسه کن.

- برای یادگیری بیشتر، [مستندات Bootstrap](https://getbootstrap.com/docs/) را ببین.

## اشتباه‌های رایج

- گذاشتن `link` Bootstrap بعد از `style.css` خودت و تعجب از اینکه سبک‌هایت بازنویسی شده‌اند؛ ترتیب مهم است و قاعدهٔ بعدی برنده می‌شود.
- تایپ اشتباه نام کلاس؛ مرورگر هیچ خطایی نشان نمی‌دهد.
- کپی بخشی از `integrity`؛ اگر چکیده با فایل جور نشود، مرورگر فایل را بارگذاری نمی‌کند.

## جمع‌بندی

- چارچوب‌ها کتابخانه‌های آمادهٔ CSS (و گاهی JS) هستند.
- Bootstrap با یک `link` در `head` افزوده می‌شود و با کلاس‌هایی مثل `table` به کار می‌رود.
- مستندات منبع اصلی نام کلاس‌هاست.

## پیوندها

- قبلی: [CSS: ویژگی، انتخابگر و آبشار](/kb/d/w08-n11)
- بعدی: [جاوااسکریپت: رویداد و DOMContentLoaded](/kb/d/w08-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
