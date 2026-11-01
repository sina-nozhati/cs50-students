---
id: w08-n09
type: note
title: 'فرم‌ها: form و input (HTML: Forms)'
title_fa: 'فرم‌ها: form و input'
title_en: 'HTML: Forms'
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
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-form
- w08-c-input-name
- w08-c-query-string
- w08-c-input-attrs
prev: w08-n08
next: w08-n10
order: 9
video:
  youtube_id: yYst7puZXjw
  start: '1:15:49'
  start_seconds: 4549
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=4549s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'you want to search for something'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# فرم‌ها: form و input

> **منبع رسمی:** بخش «HTML» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#html). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۵:۴۹ تا حدود ۱:۲۲:۲۲](https://www.youtube.com/watch?v=yYst7puZXjw&t=4549s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا صفحه‌ها فقط نمایش می‌دادند. **فرم** (`form`) راهی است که کاربر چیزی به سرور بفرستد: جست‌وجو، ثبت‌نام، پاسخ یک پرسش. در هفتهٔ ۹ سرور خودت را با Flask می‌سازی که همین فرم‌ها را دریافت می‌کند؛ امروز سمت مرورگر را می‌بینیم.

## یک فرم جست‌وجو

- می‌توانی فرم‌هایی شبیه جست‌وجوی گوگل بسازی:

```html
<!DOCTYPE html>

<!-- Demonstrates form -->

<html lang="en">
    <head>
        <title>search</title>
    </head>
    <body>
        <form action="https://www.google.com/search" method="get">
            <input name="q" type="search">
            <input type="submit" value="Google Search">
        </form>
    </body>
</html>
```

- برچسب `form` باز می‌شود و ویژگی `action` می‌گوید فرم به کجا فرستاده شود. فیلد `input` با نام `q` و نوع `search` آمده است.

> [!NOTE]
> **از سخنرانی: داده در نشانی**
> دیوید توضیح می‌دهد که یکی از راه‌های فرستادن ورودی به سرور، گذاشتن آن در خود نشانی است. وقتی فرم بالا را با کلمهٔ `cats` بفرستی، مرورگر به نشانی‌ای مثل `https://www.google.com/search?q=cats` می‌رود: بعد از `?` نام فیلد (`q`)، یک `=` و مقدار. به این جفت کلید و مقدار **پارامتر HTTP** (`HTTP parameter`) می‌گویند و اگر چند ورودی باشد، جفت‌ها با `&` از هم جدا می‌شوند. این همان درخواست `GET` از [یادداشت ۶](/kb/d/w08-n06) است.

> [!TIP]
> **اجراشده روی جعبهٔ ساخت: نشانی ساخته‌شده**
> در Node، `new URLSearchParams({q: "cats and dogs"}).toString()` مقدار `q=cats+and+dogs` را برمی‌گرداند: فاصله‌ها در نشانی رمزگذاری می‌شوند. مرورگر همین کار را هنگام فرستادن فرم انجام می‌دهد.

## فرم بهتر

```html
<!DOCTYPE html>

<!-- Demonstrates additional form attributes -->

<html lang="en">
    <head>
        <title>search</title>
    </head>
    <body>
        <form action="https://www.google.com/search" method="get">
            <input autocomplete="off" autofocus name="q" placeholder="Query" type="search">
            <button>Google Search</button>
        </form>
    </body>
</html>
```

- `autocomplete` روی `off` است و `autofocus` فعال است: مرورگر پیشنهادهای قبلی را نشان نمی‌دهد و نشانگر از اول در فیلد قرار می‌گیرد. `placeholder` متن راهنمای کم‌رنگی است که تا تایپ نکرده‌ای دیده می‌شود.

> [!IMPORTANT]
> **تألیفی: name کلید است**
> سرور فقط چیزی را می‌بیند که `name` داشته باشد. اگر `name="q"` را حذف کنی، فرم فرستاده می‌شود اما مقدار جست‌وجو همراهش نمی‌رود. `id` برای CSS و جاوااسکریپت است؛ `name` برای سرور.

- این‌ها فقط چند عنصر از عنصرهای فراوان HTML بودند. اگر چیزی می‌خواهی که ندیده‌ایم (دکمه، فایل صوتی و ...)، «X in HTML» را جست‌وجو کن. می‌توانی از [cs50.ai](https://cs50.ai) هم برای کشف ویژگی‌های بیشتر HTML کمک بگیری.

## اشتباه‌های رایج

- جا انداختن `name` روی `input`.
- فراموش کردن `action`، که در آن صورت فرم به همان صفحه فرستاده می‌شود.
- فکر کردن به اینکه `placeholder` مقدار پیش‌فرض است؛ مقداری فرستاده نمی‌شود.

## جمع‌بندی

- `form` با `action` (مقصد) و `method` (پیش‌فرض `get`).
- `input` با `name`، `type` و ویژگی‌هایی مثل `autocomplete`، `autofocus` و `placeholder`.
- با GET، داده به شکل `?name=value` در نشانی می‌رود.

## پیوندها

- قبلی: [فهرست، جدول، تصویر، ویدئو و پیوند](/kb/d/w08-n08)
- بعدی: [عبارت باقاعده و اعتبارسنجی فرم](/kb/d/w08-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
