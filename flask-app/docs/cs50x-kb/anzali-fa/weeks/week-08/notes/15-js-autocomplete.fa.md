---
id: w08-n15
type: note
title: 'تکمیل خودکار و جمع‌بندی جاوااسکریپت (JavaScript: Autocomplete)'
title_fa: تکمیل خودکار و جمع‌بندی جاوااسکریپت
title_en: 'JavaScript: Autocomplete'
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
- src-notes-8#summing-up
- src-transcript-8
- src-short-javascript
- src-mdn-js
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-js-loops
- w08-c-js-array
- w08-c-startswith
- w08-c-build-html-string
- w08-c-script-src
- w08-c-innerhtml-injection
prev: w08-n14
next: w08-summary
order: 15
video:
  youtube_id: yYst7puZXjw
  start: '2:14:01'
  start_seconds: 8041
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=8041s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'autocomplete.'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# تکمیل خودکار و جمع‌بندی جاوااسکریپت

> **منبع رسمی:** بخش «JavaScript» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#javascript). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۱۴:۰۱](https://www.youtube.com/watch?v=yYst7puZXjw&t=8041s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تکمیل خودکار (autocomplete) را هر روز در جست‌وجوگرها می‌بینی. با همان چند قطعه‌ای که در این هفته دیدی، یعنی یک `input`، یک رویداد `keyup`، یک حلقه و `innerHTML`، می‌شود نسخهٔ ساده‌اش را ساخت. این مثال همهٔ هفته را در یک صفحه جمع می‌کند.

## تکمیل خودکار

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <title>autocomplete</title>
    </head>

    <body>

        <input autocomplete="off" autofocus placeholder="Query" type="text">

        <ul></ul>

        <script src="large.js"></script>
        <script>

            let input = document.querySelector('input');
            input.addEventListener('keyup', function(event) {
                let html = '';
                if (input.value) {
                    for (word of WORDS) {
                        if (word.startsWith(input.value)) {
                            html += `<li>${word}</li>`;
                        }
                    }
                }
                document.querySelector('ul').innerHTML = html;
            });

        </script>

    </body>
</html>
```

- این پیاده‌سازی تکمیل خودکار با جاوااسکریپت است. فهرست کلمه‌ها را از فایلی به نام `large.js` (در درس‌نامه نشان داده نشده) می‌گیرد.
- با هر `keyup`، اگر جعبه خالی نباشد، کد همهٔ کلمه‌های `WORDS` را می‌گردد و هر کدام که با متن تایپ‌شده شروع شود (`startsWith`) را به‌صورت یک `<li>` به رشتهٔ `html` می‌افزاید؛ در پایان کل `ul` با `innerHTML` جایگزین می‌شود.

> [!NOTE]
> **از سخنرانی: large.js**
> دیوید توضیح می‌دهد که `large.js` آرایهٔ عظیمی از همهٔ کلمه‌های مجموعه‌تمرین ۵، یعنی غلط‌یاب (بیش از ۱۰۰ هزار کلمه) است که به شکل یک متغیر سراسری جاوااسکریپت (`WORDS`) درآمده.

> [!WARNING]
> **اجراشده روی جعبهٔ ساخت: متغیری که اعلان نشده (d132)**
> در `for (word of WORDS)`، متغیر `word` با `let` اعلان نشده است. در حالت عادی (sloppy) جاوااسکریپت این کار می‌کند و `word` بی‌صدا یک **متغیر سراسری** (`global variable`) می‌شود؛ اما با `'use strict'` در Node خطای `ReferenceError` داد. در کد خودت بنویس `for (let word of WORDS)`.

نمونهٔ تألیفی همان منطق، بدون DOM، برای اجرا در Node:
```javascript
const WORDS = ['cat', 'car', 'dog', 'cart'];
let typed = 'ca';
let html = '';
for (let word of WORDS)
{
    if (word.startsWith(typed))
    {
        html += `<li>${word}</li>`;
    }
}
console.log(html);
```

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: خروجی نمونهٔ بالا**
> Node این سطر را چاپ کرد: `<li>cat</li><li>car</li><li>cart</li>`.

> [!TIP]
> **از ویدئوی کوتاه: for-of یا for-in؟**
> داگ لوید در [ویدئوی جاوااسکریپت](/kb/d/w08-sh-javascript) فرق این دو را روی یک آرایه نشان می‌دهد: `for-of` **مقدارها** را می‌دهد و `for-in` **کلیدها**، یعنی اندیس‌ها. اگر در autocomplete به جای `of` می‌نوشتی `in`، `word` رشته‌هایی مثل `'0'` و `'1'` می‌شد؛ خطایی رخ نمی‌داد، اما هیچ کلمه‌ای پیشنهاد نمی‌شد (روی جعبهٔ ساخت آزموده شد).

> [!IMPORTANT]
> **از سخنرانی: جاوااسکریپت فراتر از این**
> دیوید در ادامه نشان می‌دهد که مرورگر از راه جاوااسکریپت می‌تواند با اجازهٔ کاربر حتی موقعیت جغرافیایی دستگاه (geolocation) را بخواند. امکانات جاوااسکریپت بسیارند و در [مستندات JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) آمده‌اند.

## جمع‌بندی هفته

در این درس یاد گرفتی چطور فایل‌های HTML خودت را بسازی، به آن‌ها سبک بدهی، از چارچوب‌های شخص ثالث استفاده کنی و جاوااسکریپت را به کار ببری. به‌طور مشخص دربارهٔ این‌ها حرف زدیم:

- اینترنت
- مسیریاب‌ها
- DNS
- DHCP
- HTTPS
- HTML
- عبارت‌های باقاعده
- CSS
- چارچوب‌ها
- جاوااسکریپت

تا هفتهٔ بعد!

## اشتباه‌های رایج

- جا انداختن `let` در حلقهٔ `for...of`.
- اضافه کردن `<li>`ها یکی‌یکی به DOM به جای ساختن یک رشته و یک بار جایگزین کردن؛ هر دو کار می‌کنند، اما نسخهٔ درس‌نامه پیش از هر جست‌وجو فهرست قبلی را پاک می‌کند.
- استفاده از `for...in` روی آرایه.

## جمع‌بندی

- autocomplete = `keyup` + حلقه روی `WORDS` + `startsWith` + `innerHTML`.
- `word` اعلان‌نشده در حالت عادی سراسری می‌شود و در حالت سخت‌گیر خطا می‌دهد.
- `for-of` مقدار می‌دهد، `for-in` کلید.

## پیوندها

- قبلی: [تغییر DOM: keyup، سبک و زمان‌سنج](/kb/d/w08-n14)
- بعدی: [خلاصهٔ هفته](/kb/d/w08-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
