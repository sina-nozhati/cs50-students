---
id: w08-n13
type: note
title: 'جاوااسکریپت: رویداد و DOMContentLoaded (JavaScript: Events)'
title_fa: 'جاوااسکریپت: رویداد و DOMContentLoaded'
title_en: 'JavaScript: Events'
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
- src-short-javascript
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-javascript
- w08-c-script-tag
- w08-c-js-function
- w08-c-alert
- w08-c-queryselector
- w08-c-value-property
- w08-c-onsubmit
- w08-c-event-listener
- w08-c-anonymous-function
- w08-c-domcontentloaded
- w08-c-prevent-default
prev: w08-n12
next: w08-n14
order: 13
video:
  youtube_id: yYst7puZXjw
  start: '1:50:44'
  start_seconds: 6644
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=6644s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'one last language for the day'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جاوااسکریپت: رویداد و DOMContentLoaded

> **منبع رسمی:** بخش «JavaScript» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#javascript). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۰:۴۴ تا حدود ۲:۰۵:۴۱](https://www.youtube.com/watch?v=yYst7puZXjw&t=6644s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

HTML و CSS صفحه را می‌سازند و می‌آرایند، اما صفحه هنوز «مرده» است: کاری نمی‌کند مگر آنکه دوباره بارگذاری شود. **جاوااسکریپت** (`JavaScript`) زبان برنامه‌نویسی واقعی‌ای است که درون مرورگر اجرا می‌شود و صفحه را به رویدادهای کاربر واکنش‌پذیر می‌کند. خبر خوب: نحوش بیشتر از آنچه فکر می‌کنی شبیه C است.

## جاوااسکریپت سمت کاربر

- جاوااسکریپت زبان برنامه‌نویسی دیگری است که امکان تعامل را درون صفحه‌های وب فراهم می‌کند.

> [!NOTE]
> **از سخنرانی: کد روی سرور، اجرا روی دستگاه تو**
> دیوید جاوااسکریپت را زبانی «سمت کاربر» (client side) معرفی می‌کند: انسان‌ها کد را روی سرور می‌نویسند، اما مرورگرت آن را دانلود می‌کند و روی مک، رایانه یا گوشی خودت اجرا می‌کند. او اضافه می‌کند که جاوااسکریپت امروز روی سرور هم بسیار محبوب است. جعبهٔ ساخت این بسته هم کدهای تألیفی را با Node (جاوااسکریپت بیرون از مرورگر) اجرا کرده است.

## نحو در یک نگاه

- **شرط‌ها** تقریباً همان C هستند: آکولادها برگشته‌اند و تورفتگی، برخلاف پایتون، فقط برای خوانایی است. `else if` هم مثل C نوشته می‌شود، نه `elif`.
- **متغیرها** را با `let` می‌سازی و نوعشان را نمی‌نویسی: `let counter = 0;`. نقطه‌ویرگول‌ها هم برگشته‌اند.
- `counter = counter + 1`، `counter += 1` و `counter++` همه کار می‌کنند؛ `++` مثل C هست، برخلاف پایتون.
- **حلقه‌ها** مثل C هستند، فقط به جای نوع از `let` استفاده می‌کنی؛ حلقهٔ بی‌پایان هم `while (true)` است.

نمونهٔ تألیفی که همهٔ این‌ها را کنار هم می‌گذارد (`console.log` همان `printf` یا `print` است و خروجی را در کنسول می‌نویسد):
```javascript
let counter = 0;
counter = counter + 1;
counter += 1;
counter++;
for (let i = 0; i < 3; i++)
{
    console.log('meow');
}
console.log(counter);
```

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: خروجی نمونهٔ بالا**
> Node سه بار `meow` و سپس `3` چاپ کرد، هر کدام در یک سطر.

> [!WARNING]
> **از ویدئوی کوتاه: + برای رشته‌ها (d141)**
> داگ لوید در [ویدئوی جاوااسکریپت](/kb/d/w08-sh-javascript) هشدار می‌دهد که `+` هم جمع است و هم الحاق رشته. روی جعبهٔ ساخت، `console.log(1 + '1')` خروجی `11` داد، نه `2`. برای تبدیل رشته به عدد از `parseInt` استفاده کن. آن ویدئو از ۲۰۱۷ است و `var` به کار می‌برد؛ درس‌نامهٔ ۲۰۲۶ `let` را ترجیح می‌دهد.

> [!TIP]
> **تألیفی: == یا ===؟**
> `blink` در یادداشت بعد از `==` استفاده می‌کند. در جاوااسکریپت `==` پیش از مقایسه نوع‌ها را تبدیل می‌کند و `===` نه. روی جعبهٔ ساخت، `console.log(1 == '1', 1 === '1')` خروجی `true false` داد. برای مقایسهٔ دو رشته هر دو کار می‌کنند، اما `===` غافلگیری کمتری دارد.

## جای کد در صفحه

- کد جاوااسکریپت درون برچسب `script` می‌آید: در `head` (مثل `style`)، در فایلی جدا با `src`، یا پایین `body`.

> [!IMPORTANT]
> **از سخنرانی: کدی که زود اجرا می‌شود**
> دیوید هشدار می‌دهد اگر `script` در `head` باشد و بخواهد عنصری را تغییر دهد که پایین‌تر تعریف شده، آن عنصر هنوز وجود ندارد؛ او این را نوعی شرایط مسابقه (race condition) می‌نامد و به مشکل پیش‌نمونه‌ها در C تشبیه می‌کند. یک راه: گذاشتن `script` درست پیش از بسته شدن `body`. راه دیگر، `DOMContentLoaded`، را کمی پایین‌تر می‌بینیم.

## رویداد ارسال فرم

- این پیاده‌سازی `hello.html` هم جاوااسکریپت دارد و هم HTML:

```html
<!DOCTYPE html>

<!-- Demonstrates onsubmit -->

<html lang="en">
    <head>
        <script>

            function greet()
            {
                alert('hello, ' + document.querySelector('#name').value);
            }

        </script>
        <title>hello</title>
    </head>
    <body>
        <form onsubmit="greet(); return false;">
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```

- این فرم با ویژگی `onsubmit` اسکریپتی را در بالای فایل اجرا می‌کند. اسکریپت با `alert` پنجرهٔ هشدار باز می‌کند. `document.querySelector('#name').value` جعبهٔ متنی با `id` برابر `name` را انتخاب می‌کند و مقداری را که کاربر تایپ کرده می‌گیرد. `return false` جلوی فرستادن واقعی فرم را می‌گیرد.

## گوش دادن به رویدادها

- معمولاً آمیختن `onsubmit` با جاوااسکریپت طراحی بدی به شمار می‌آید. می‌توانیم کد را پیش ببریم:

```html
<!DOCTYPE html>

<!-- Demonstrates DOMContentLoaded -->

<html lang="en">
    <head>
        <script>

            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('form').addEventListener('submit', function(e) {
                    alert('hello, ' + document.querySelector('#name').value);
                    e.preventDefault();
                });
            });

        </script>
        <title>hello</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
    </body>
</html>
```

- این نسخه با `addEventListener` به **رویداد** (`event`) `submit` فرم گوش می‌دهد. `DOMContentLoaded` تضمین می‌کند که کل صفحه پیش از اجرای جاوااسکریپت بارگذاری شده باشد. `e.preventDefault()` همان کار `return false` را می‌کند.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: hello3 در jsdom**
> با تایپ `David` و ارسال فرم، پیام `hello, David` در `alert` ثبت شد و `defaultPrevented` برابر `true` بود؛ یعنی صفحه به جای دیگری نرفت.

> [!TIP]
> **تألیفی: تابع بی‌نام**
> `function() { ... }` که به `addEventListener` داده می‌شود نام ندارد: **تابع بی‌نام** (`anonymous function`). تو آن را صدا نمی‌زنی؛ مرورگر هر وقت رویداد رخ داد صدایش می‌زند. همان ایدهٔ «وقتی پرچم سبز کلیک شد» در Scratch.

## اشتباه‌های رایج

- نوشتن `elif` یا جا انداختن آکولاد به عادت پایتون.
- فراموش کردن `preventDefault` (یا `return false`) و دیدن اینکه صفحه بلافاصله دوباره بارگذاری می‌شود.
- گذاشتن `querySelector` در `head` بدون `DOMContentLoaded` و گرفتن `null`.
- جمع زدن عدد با رشته و گرفتن الحاق.

## جمع‌بندی

- جاوااسکریپت در مرورگر اجرا می‌شود و نحوش به C نزدیک است: `let`، آکولاد، `++`، `for`.
- `script` در `head`، در فایل جدا یا پایین `body`.
- `onsubmit` کار می‌کند، اما `addEventListener` همراه با `DOMContentLoaded` طراحی بهتری است.

## پیوندها

- قبلی: [چارچوب‌ها: Bootstrap](/kb/d/w08-n12)
- بعدی: [تغییر DOM: keyup، سبک و زمان‌سنج](/kb/d/w08-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
