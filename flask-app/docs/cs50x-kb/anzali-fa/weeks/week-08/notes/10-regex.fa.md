---
id: w08-n10
type: note
title: عبارت باقاعده و اعتبارسنجی فرم (Regular Expressions)
title_fa: عبارت باقاعده و اعتبارسنجی فرم
title_en: Regular Expressions
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Regular Expressions
official_anchor: regular-expressions
source_url: https://cs50.harvard.edu/x/2026/notes/8/#regular-expressions
source_refs:
- src-notes-8#regular-expressions
- src-mdn-js
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-regex
- w08-c-input-email
- w08-c-pattern-attr
- w08-c-client-validation-limits
prev: w08-n09
next: w08-n11
order: 10
video:
  youtube_id: yYst7puZXjw
  start: '1:22:22'
  start_seconds: 4942
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=4942s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'what are called regular expressions'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# عبارت باقاعده و اعتبارسنجی فرم

> **منبع رسمی:** بخش «Regular Expressions» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#regular-expressions). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۲:۲۲ تا حدود ۱:۲۹:۳۹](https://www.youtube.com/watch?v=yYst7puZXjw&t=4942s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

کاربرها هر چیزی تایپ می‌کنند: ایمیل بدون `@`، شمارهٔ تلفن با حروف، فیلد خالی. پیش از آنکه داده به سرور برسد، مرورگر می‌تواند قالب آن را بررسی کند. ابزار اصلی این بررسی **عبارت باقاعده** (`regular expression`) است که در هفتهٔ ۶ در پایتون هم دیدی.

## عبارت‌های باقاعده

- **عبارت‌های باقاعده** یا `regex` راهی هستند برای اطمینان از اینکه داده‌ای که کاربر می‌دهد قالب مشخصی دارد.
- می‌توانیم صفحهٔ ثبت‌نام خودمان را بسازیم:

```html
<!DOCTYPE html>

<!-- Demonstrates type="email" -->

<html lang="en">
    <head>
        <title>register</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus name="email" placeholder="Email" type="email">
            <button>Register</button>
        </form>
    </body>
</html>
```

- برچسب `input` ویژگی‌هایی دارد که می‌گویند نوعش `email` است. مرورگر می‌داند باید بررسی کند که ورودی نشانی ایمیل باشد.

## ویژگی pattern

- مرورگر با همین ویژگی‌های داخلی نشانی ایمیل را بررسی می‌کند، اما می‌توانیم ویژگی `pattern` را هم اضافه کنیم تا فقط دادهٔ مشخصی در نشانی ایمیل قرار گیرد:

```html
<!DOCTYPE html>

<!-- Demonstrates pattern attribute for email -->

<html lang="en">
    <head>
        <title>register</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus name="email" pattern=".+@.+\.edu" placeholder="Email" type="email">
            <button>Register</button>
        </form>
    </body>
</html>
```

- به ویژگی `pattern` یک عبارت باقاعده داده شده که می‌گوید نشانی ایمیل باید `@` و `.edu` داشته باشد.

> [!TIP]
> **تألیفی: خواندن الگو تکه‌به‌تکه**
> در `.+@.+\.edu`: نقطهٔ `.` یعنی «هر نویسه‌ای»، `+` یعنی «یک یا چند بار»، `@` خودِ نویسهٔ @ است و `\.` یعنی نقطهٔ واقعی (با بک‌اسلش تا معنای ویژه‌اش را از دست بدهد). پس الگو می‌گوید: چیزی، بعد @، بعد چیزی، بعد `.edu`.

> [!IMPORTANT]
> **اجراشده روی جعبهٔ ساخت: کل مقدار باید جور شود (d146)**
> مرورگر الگوی `pattern` را بر **کل** مقدار فیلد اعمال می‌کند، انگار اول آن `^` و آخرش `$` باشد. در jsdom با همین فرم: `malan@harvard.edu` معتبر بود، اما `malan@harvard.edu.com` و `a@b.edux` نامعتبر. پس «باید `.edu` داشته باشد» دقیق‌تر یعنی «باید با `.edu` تمام شود».

> [!WARNING]
> **تألیفی: بررسی مرورگر امنیت نیست**
> هر کسی می‌تواند با ابزار توسعه‌دهنده ویژگی `pattern` را پاک کند یا با `curl` مستقیم به سرور درخواست بفرستد. بررسی سمت مرورگر برای راحتی کاربر است؛ همان‌طور که در هفتهٔ ۷ گفتیم، هرگز به ورودی کاربر اعتماد نکن و داده را روی سرور (هفتهٔ ۹) دوباره بررسی کن.

- برای یادگیری بیشتر دربارهٔ عبارت‌های باقاعده، [مستندات Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) را ببین. از [cs50.ai](https://cs50.ai) هم می‌توانی راهنمایی بگیری.

## اشتباه‌های رایج

- فراموش کردن بک‌اسلش پیش از نقطه؛ `.edu` بدون آن با `xedu` هم جور می‌شود.
- گذاشتن `^` و `$` و فکر کردن به اینکه بدون آن‌ها الگو بخشی از مقدار را می‌پذیرد.
- اکتفا به بررسی سمت مرورگر.

## جمع‌بندی

- `type="email"` بررسی داخلی مرورگر را فعال می‌کند.
- `pattern` یک عبارت باقاعده می‌گیرد و کل مقدار باید با آن جور شود.
- بررسی مرورگر جای بررسی سرور را نمی‌گیرد.

## پیوندها

- قبلی: [فرم‌ها: form و input](/kb/d/w08-n09)
- بعدی: [CSS: ویژگی، انتخابگر و آبشار](/kb/d/w08-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
