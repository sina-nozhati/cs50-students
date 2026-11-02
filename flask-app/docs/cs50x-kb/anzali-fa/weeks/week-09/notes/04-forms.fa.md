---
id: w09-n04
type: note
title: فرم‌ها و مسیر دوم /greet (Forms)
title_fa: فرم‌ها و مسیر دوم /greet
title_en: Forms
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Forms
official_anchor: forms
source_url: https://cs50.harvard.edu/x/2026/notes/9/#forms
source_refs:
- src-notes-9#forms
- src-transcript-9
- src-flask-box-9
- src-anzali-authored-9
- src-anzali-inference-9
- src-srt-9
concept_ids:
- w09-c-form-to-route
- w09-c-second-route
- w09-c-template-not-found
prev: w09-n03
next: w09-n05
order: 4
video:
  youtube_id: am7POvSZ4GE
  start: '30:29'
  start_seconds: 1829
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=1829s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'and if you go to example.com/greet'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# فرم‌ها و مسیر دوم /greet

> **منبع رسمی:** بخش «Forms» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#forms). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۰:۲۹ تا حدود ۳۷:۰۶](https://www.youtube.com/watch?v=am7POvSZ4GE&t=1829s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

بیشتر کاربران در نوار نشانی `?name=` تایپ نمی‌کنند؛ آن‌ها فرم پر می‌کنند. در این بخش فرمی می‌سازی که داده را به یک **مسیر دوم** می‌فرستد و صفحهٔ دوم پاسخ را نشان می‌دهد.

## فرمی که به /greet می‌رود

- `index.html` را این‌طور تغییر بده:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <title>hello</title>
    </head>

    <body>
        <form action="/greet" method="get">
            <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
            <button type="submit">Greet</button>
        </form>
    </body>

</html>
```

- اکنون فرمی ساخته شده که نام کاربر را می‌گیرد و آن را به مسیری به نام `/greet` می‌فرستد. `autocomplete` خاموش است و یک `placeholder` با متن `Name` دارد.
- سپس `app.py` را این‌طور تغییر بده:

```python
# Adds a form, second route

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))
```

- مسیر پیش‌فرض (`/`) فرم را نشان می‌دهد و مسیر `/greet` مقدار `name` را به صفحهٔ وب می‌فرستد.
- برای کامل شدن کار، قالب دیگری به نام `greet.html` در پوشهٔ `templates` لازم است:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>hello</title>
    </head>

    <body>
        hello, {{ name }}
    </body>

</html>
```

- این مسیر حالا خوشامد را همراه با نام کاربر نشان می‌دهد.

> [!NOTE]
> **از سخنرانی: TemplateNotFound**
> دیوید پیش از ساختن `greet.html` روی دکمه کلیک می‌کند و Flask خطای `TemplateNotFound` می‌دهد: مسیر وجود دارد، اما قالبی که `render_template` خواسته هنوز ساخته نشده است.

> [!TIP]
> **اجراشده روی جعبهٔ ساخت: فیلد خالی با فیلد نبوده فرق دارد**
> با همین سه فایل، `GET /greet?name=` (فرمی که خالی فرستاده شود) صفحه‌ای با `hello,` می‌دهد، اما `GET /greet` (بدون پارامتر) `hello, world` می‌دهد. مقدار پیش‌فرض `get` فقط وقتی به کار می‌رود که کلید اصلاً در نشانی نباشد. در یادداشت ۷ همین مشکل حل می‌شود.

## اشتباه‌های رایج

- یکی نبودن `name="name"` در فرم و کلیدی که در `request.args.get("name")` می‌خوانی.
- نوشتن `action="greet"` به جای `action="/greet"`؛ نشانی نسبی بسته به صفحهٔ فعلی جای دیگری می‌رود (استنتاجی).
- فراموش کردن ساختن قالب دوم.

## جمع‌بندی

- `action` فرم مشخص می‌کند داده به کدام مسیر برود و `name` هر input کلید آن داده است.
- هر مسیر تابع و (معمولاً) قالب خودش را دارد.
- فیلد خالی رشتهٔ `""` می‌فرستد، نه «هیچ».

## پیوندها

- قبلی: [render_template، پوشهٔ templates و request.args](/kb/d/w09-n03)
- بعدی: [قالب مادر: layout.html، block و extends](/kb/d/w09-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
