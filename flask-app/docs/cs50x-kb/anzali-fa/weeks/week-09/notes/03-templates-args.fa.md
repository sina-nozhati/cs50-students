---
id: w09-n03
type: note
title: 'render_template، پوشهٔ templates و request.args (Flask: Templates and request.args)'
title_fa: render_template، پوشهٔ templates و request.args
title_en: 'Flask: Templates and request.args'
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Flask
official_anchor: flask
source_url: https://cs50.harvard.edu/x/2026/notes/9/#flask
source_refs:
- src-notes-9#flask
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-templates-folder
- w09-c-render-template
- w09-c-request-args
- w09-c-jinja-placeholder
- w09-c-jinja-autoescape
prev: w09-n02
next: w09-n04
order: 3
video:
  youtube_id: am7POvSZ4GE
  start: '18:24'
  start_seconds: 1104
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=1104s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'A second argument to the render template function'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# render_template، پوشهٔ templates و request.args

> **منبع رسمی:** بخش «Flask» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#flask). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۸:۲۴ تا حدود ۳۰:۲۹](https://www.youtube.com/watch?v=am7POvSZ4GE&t=1104s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

نوشتن HTML درون رشته‌های پایتون زود شلوغ می‌شود. Flask به تو اجازه می‌دهد HTML را در فایل‌های جدا، به نام **قالب** (template)، نگه داری و فقط مقدارهای متغیر را از پایتون بفرستی.

## پوشهٔ templates و render_template

- پوشه‌ای به نام `templates` بساز و درون آن فایلی به نام `index.html` با این کد:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <title>hello</title>
    </head>

    <body>
        hello, world
    </body>

</html>
```

- سپس در همان پوشه‌ای که `templates` در آن است، `app.py` را بساز:

```python
# Uses request.args.get

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)
```

- این کد `app` را برنامهٔ Flask تعریف می‌کند. سپس مسیر `/` را طوری تعریف می‌کند که محتوای `index.html` را با آرگومان `name` برگرداند. `request.args.get` دنبال `name` در نشانی می‌گردد؛ اگر نامی داده نشده باشد، مقدار پیش‌فرض `world` به کار می‌رود. به `@app.route` تزئین‌گر می‌گویند.
- برنامه را با `flask run` اجرا کن. اگر اجرا نشد، نحو هر فایل را بررسی کن و مطمئن شو فایل‌ها این‌طور چیده شده‌اند:

```text
/templates
    index.html
app.py
requirements.txt
```

- وقتی برنامه اجرا شد، روی پیوند کلیک کن و `?name=[Your Name]` را به انتهای نشانی اضافه کن.

> [!WARNING]
> **اجراشده روی جعبهٔ ساخت: چرا نامت را نمی‌بینی؟ (d155)**
> فایل `index.html` بالا هیچ جای‌نگهداری برای `name` ندارد و همیشه `hello, world` می‌نویسد. روی جعبهٔ ساخت، درخواست `GET /?name=David` با همین دو فایل باز هم `hello, world` داد. برای اینکه آزمایش درس‌نامه کار کند، در `index.html` به جای `hello, world` بنویس:
>
> ```jinja
> hello, {{ name }}
> ```
>
> (تغییر تألیفی؛ نسخه‌های بعدی کد منبع رسمی همین کار را می‌کنند.)

## جای‌نگهدار {{ }} و escape خودکار

- آنچه بین `{{` و `}}` می‌آید **جای‌نگهدار** (placeholder) زبان قالب **Jinja** است؛ Flask مقدار متغیر را آنجا می‌نشاند.

> [!TIP]
> **تألیفی، اجراشده روی جعبهٔ ساخت: Jinja نویسه‌های ویژه را escape می‌کند**
> اگر کاربر به جای نام `<b>x</b>` بفرستد، Flask آن را `&lt;b&gt;x&lt;/b&gt;` می‌نویسد و مرورگر متن را نشان می‌دهد، نه تگ را. این کار جلوی بخش بزرگی از حمله‌ها را می‌گیرد؛ بعداً در جاوااسکریپت باید خودت این کار را بکنی.

## اشتباه‌های رایج

- گذاشتن `index.html` کنار `app.py` به جای درون `templates`.
- انتظار دیدن نام در صفحه‌ای که `{{ name }}` ندارد.
- فراموش کردن `request` در `from flask import ...`.

## جمع‌بندی

- قالب‌ها در پوشهٔ `templates` قرار می‌گیرند و با `render_template("index.html", name=...)` فرستاده می‌شوند.
- `request.args.get("name", "world")` پارامتر نشانی را می‌خواند و اگر نباشد `world` می‌دهد.
- `{{ name }}` در قالب جای مقدار است و Jinja آن را escape می‌کند.

## پیوندها

- قبلی: [Flask: نخستین برنامه، مسیر و تزئین‌گر](/kb/d/w09-n02)
- بعدی: [فرم‌ها و مسیر دوم /greet](/kb/d/w09-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
