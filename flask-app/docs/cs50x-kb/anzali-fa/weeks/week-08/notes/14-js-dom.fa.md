---
id: w08-n14
type: note
title: 'تغییر DOM: keyup، سبک و زمان‌سنج (JavaScript: Changing the DOM)'
title_fa: 'تغییر DOM: keyup، سبک و زمان‌سنج'
title_en: 'JavaScript: Changing the DOM'
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: JavaScript
official_anchor: javascript
source_url: https://cs50.harvard.edu/x/2026/notes/8/#javascript
source_refs:
- src-notes-8#javascript
- src-transcript-8
- src-short-dom
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-js-variables
- w08-c-js-conditionals
- w08-c-truthy-string
- w08-c-keyup
- w08-c-template-literal
- w08-c-innerhtml
- w08-c-style-property
- w08-c-click-event
- w08-c-setinterval
- w08-c-visibility
- w08-c-equality-operators
prev: w08-n13
next: w08-n15
order: 14
video:
  youtube_id: yYst7puZXjw
  start: '2:05:41'
  start_seconds: 7541
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=7541s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'open up hello 5'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# تغییر DOM: keyup، سبک و زمان‌سنج

> **منبع رسمی:** بخش «JavaScript» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#javascript). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۵:۴۱ تا حدود ۲:۱۴:۰۱](https://www.youtube.com/watch?v=yYst7puZXjw&t=7541s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در یادداشت ۷ گفتیم برچسب‌ها درخت می‌سازند و این درخت بعداً به کار می‌آید. حالا وقتش است: مرورگر صفحه را به درختی در حافظه به نام **DOM** تبدیل می‌کند و جاوااسکریپت می‌تواند آن درخت را بخواند و تغییر دهد، بی‌آنکه کاربر صفحه را دوباره بارگذاری کند.

## DOM

- جاوااسکریپت اجازه می‌دهد سند HTMLی را که در حافظه بارگذاری شده پویا بخوانی و تغییر دهی، طوری که کاربر برای دیدن تغییرها لازم نیست صفحه را دوباره بارگذاری کند.

> [!NOTE]
> **از سخنرانی: صندوق ایمیل**
> دیوید می‌پرسد صندوق Gmail یا Outlook با چه برچسبی سطر به سطر ساخته می‌شود؛ احتمالاً جدول. قدیم‌ها برای دیدن ایمیل تازه باید کل صفحه را دوباره بارگذاری می‌کردی. با جاوااسکریپت می‌توان داده را یک بار گرفت و بعد هر وقت ایمیلی رسید، گرهٔ تازه‌ای (یک `tr`) به درخت افزود. به این درخت **مدل شیء سند** (`document object model`) یا DOM می‌گویند.

> [!TIP]
> **از ویدئوی کوتاه: درخت را ببین**
> داگ لوید در [ویدئوی DOM](/kb/d/w08-sh-dom) شیء `document` را ریشهٔ درخت معرفی می‌کند و چند ویژگی گره‌ها را نام می‌برد: `innerHTML` (محتوای درون یک عنصر)، `nodeName`، `id`، `parentNode`، `childNodes`، `attributes` و `style`. او با `document.getElementById` گره پیدا می‌کند و jQuery را هم نشان می‌دهد؛ درس‌نامهٔ ۲۰۲۶ برای همین کار `document.querySelector` را به کار می‌برد که هر گزینشگر CSS را می‌پذیرد (d141).

## واکنش به هر کلید

```html
<!DOCTYPE html>

<!-- Demonstrates keyup and template literals -->

<html lang="en">
    <head>
        <script>

            document.addEventListener('DOMContentLoaded', function() {
                let input = document.querySelector('input');
                input.addEventListener('keyup', function(event) {
                    let name = document.querySelector('p');
                    if (input.value) {
                        name.innerHTML = `hello, ${input.value}`;
                    }
                    else {
                        name.innerHTML = 'hello, whoever you are';
                    }
                });
            });

        </script>
        <title>hello</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus placeholder="Name" type="text">
        </form>
        <p></p>
    </body>
</html>
```

- DOM در حافظه، همزمان با تایپ نام، پویا به‌روز می‌شود. اگر درون `input` مقداری باشد، با هر رویداد `keyup` روی صفحه‌کلید، DOM به‌روز می‌شود؛ وگرنه متن پیش‌فرض نشان داده می‌شود.
- `` `hello, ${input.value}` `` یک **رشتهٔ قالبی** (`template literal`) است: بین بک‌تیک‌ها، `${...}` با مقدار عبارت جایگزین می‌شود؛ مثل f-string پایتون.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: hello5 در jsdom**
> با تایپ `D` متن پاراگراف `hello, D` شد، با تایپ `David` شد `hello, David`، و با پاک کردن جعبه شد `hello, whoever you are`.

> [!WARNING]
> **تألیفی: innerHTML و ورودی کاربر**
> `innerHTML` رشته را به‌عنوان HTML تفسیر می‌کند. اگر کاربر `<b>x</b>` تایپ کند، hello5 آن را پررنگ نشان می‌دهد؛ کاربر می‌تواند در صفحه برچسب بگذارد. برای این نمایش ساده مشکلی نیست، اما در صفحه‌ای که ورودی کسی به دیگران نشان داده می‌شود، همان هشدار هفتهٔ ۷ برقرار است: به ورودی کاربر اعتماد نکن. `textContent` متن را بدون تفسیر می‌گذارد.

## تغییر سبک با کد

```html
<!DOCTYPE html>

<!-- Demonstrates programmatic changes to style -->

<html lang="en">
    <head>
        <title>background</title>
    </head>
    <body>
        <button id="red">R</button>
        <button id="green">G</button>
        <button id="blue">B</button>
        <script>

            let body = document.querySelector('body');
            document.querySelector('#red').addEventListener('click', function() {
                body.style.backgroundColor = 'red';
            });
            document.querySelector('#green').addEventListener('click', function() {
                body.style.backgroundColor = 'green';
            });
            document.querySelector('#blue').addEventListener('click', function() {
                body.style.backgroundColor = 'blue';
            });

        </script>
    </body>
</html>
```

- جاوااسکریپت منتظر کلیک روی یک دکمهٔ مشخص می‌ماند. با کلیک، برخی ویژگی‌های سبک صفحه تغییر می‌کنند. `body` بدنهٔ صفحه تعریف شده، سپس برای کلیک هر دکمه یک شنونده منتظر است و `body.style.backgroundColor` عوض می‌شود.
- این `script` پایین `body` است؛ برای همین بدون `DOMContentLoaded` هم دکمه‌ها از پیش وجود دارند.

> [!TIP]
> **تألیفی: نام‌های CSS در جاوااسکریپت**
> ویژگی CSS `background-color` در جاوااسکریپت `backgroundColor` می‌شود، چون `-` در نام متغیر جاوااسکریپت معنای تفریق دارد. قاعده: خط تیره را حذف کن و حرف بعدی را بزرگ بنویس.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: background در jsdom**
> پس از کلیک روی دکمهٔ `G`، `document.body.style.backgroundColor` برابر `green` بود.

## چشمک زدن با زمان‌سنج

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <script>

            // Toggles visibility of greeting
            function blink()
            {
                let body = document.querySelector('body');
                if (body.style.visibility == 'hidden')
                {
                    body.style.visibility = 'visible';
                }
                else
                {
                    body.style.visibility = 'hidden';
                }
            }

            // Blink every 500ms
            window.setInterval(blink, 500);

        </script>
        <title>blink</title>
    </head>
    <body>
        hello, world
    </body>
</html>
```

- این مثال متنی را در فاصله‌های مشخص چشمک‌زن می‌کند. `window.setInterval` دو آرگومان می‌گیرد: تابعی که باید صدا زده شود و فاصلهٔ انتظار (به میلی‌ثانیه) بین فراخوانی‌ها.
- `blink` بدون پرانتز داده شده است: خودِ تابع را می‌دهیم تا مرورگر بعداً صدایش بزند، نه نتیجهٔ صدا زدنش را.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: blink در jsdom**
> پس از حدود ۷۰۰ میلی‌ثانیه (یک فراخوانی) مقدار `visibility` برابر `hidden` بود و پس از حدود ۱۲۰۰ میلی‌ثانیه (دو فراخوانی) دوباره `visible`. jsdom چیدمان و نمایش واقعی ندارد؛ فقط مقدار ویژگی سبک بررسی شد.

## اشتباه‌های رایج

- نوشتن `setInterval(blink(), 500)`؛ تابع یک بار همان لحظه اجرا می‌شود و نتیجه‌اش (`undefined`) به زمان‌سنج داده می‌شود.
- نوشتن `body.style.background-color`.
- استفاده از `innerHTML` برای متنی که از کاربر آمده و قرار است به دیگران نمایش داده شود.

## جمع‌بندی

- DOM درخت صفحه در حافظه است و جاوااسکریپت آن را بی‌بارگذاری دوباره تغییر می‌دهد.
- `querySelector` گره را پیدا می‌کند، `innerHTML` محتوا و `style` سبک را تغییر می‌دهد.
- رویدادهای `keyup` و `click` و زمان‌سنج `setInterval` کد را در زمان درست اجرا می‌کنند.

## پیوندها

- قبلی: [جاوااسکریپت: رویداد و DOMContentLoaded](/kb/d/w08-n13)
- بعدی: [تکمیل خودکار و جمع‌بندی جاوااسکریپت](/kb/d/w08-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
