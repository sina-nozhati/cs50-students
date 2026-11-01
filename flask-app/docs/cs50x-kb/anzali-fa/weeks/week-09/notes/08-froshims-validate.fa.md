---
id: w09-n08
type: note
title: 'Frosh IMs: منوی select، حلقهٔ for و اعتبارسنجی سمت سرور (Frosh IMs: Validation)'
title_fa: 'Frosh IMs: منوی select، حلقهٔ for و اعتبارسنجی سمت سرور'
title_en: 'Frosh IMs: Validation'
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Frosh IMs
official_anchor: frosh-ims
source_url: https://cs50.harvard.edu/x/2026/notes/9/#frosh-ims
source_refs:
- src-notes-9#frosh-ims
- src-transcript-9
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-select-menu
- w09-c-jinja-for
- w09-c-server-validation
- w09-c-constant-list
- w09-c-radio-buttons
prev: w09-n07
next: w09-n09
order: 8
video:
  youtube_id: am7POvSZ4GE
  start: '55:29'
  start_seconds: 3329
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=3329s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'selecting the sport for which you want to register'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# Frosh IMs: منوی select، حلقهٔ for و اعتبارسنجی سمت سرور

> **منبع رسمی:** بخش «Frosh IMs» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#frosh-ims). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۵:۲۹ تا حدود ۱:۲۲:۰۴](https://www.youtube.com/watch?v=am7POvSZ4GE&t=3329s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

Frosh IMs (یا froshims) برنامه‌ای است که دانشجویان سال اول با آن برای ورزش‌های درون‌دانشگاهی ثبت‌نام می‌کنند. با این مثال یاد می‌گیری فرم را از فهرستی در پایتون بسازی و، مهم‌تر، ورودی را **سمت سرور** بررسی کنی.

## آماده‌سازی

- پنجره‌های مربوط به `hello` را ببند و با `mkdir froshims` پوشه‌ای بساز، با `cd froshims` واردش شو و درون آن با `mkdir templates` پوشهٔ قالب‌ها را بساز.
- با `code requirements.txt` این فایل را بنویس:

```text
Flask
```

- مانند قبل، برای اجرای برنامهٔ Flask خود Flask لازم است.
- سپس با `code app.py` این کد را بنویس:

```python
# Implements a registration form using a select menu, validating sport server-side

from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    # Confirm registration
    return render_template("success.html")
```

- گزینهٔ `failure` وجود دارد تا اگر فیلد `name` یا `sport` درست پر نشده باشد، پیام شکست به کاربر نشان داده شود.

## قالب‌ها

- با `code templates/index.html` این فایل را بساز:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Register</h1>
    <form action="/register" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <select name="sport">
            <option selected value="">Sport</option>
            {% for sport in sports %}
                <option value="{{ sport }}">{{ sport }}</option>
            {% endfor %}
        </select>
        <button type="submit">Register</button>
    </form>
{% endblock %}
```

- با `code templates/layout.html` قالب مادر را بساز:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>froshims</title>
    </head>

    <body>
        {% block body %}{% endblock %}
    </body>

</html>
```

- چهارم، فایلی به نام `success.html` در templates:

```jinja
{% extends "layout.html" %}

{% block body %}
    You are registered!
{% endblock %}
```

- و در پایان `failure.html`:

```jinja
{% extends "layout.html" %}

{% block body %}
    You are not registered!
{% endblock %}
```

- `flask run` را اجرا کن و برنامه را در این مرحله امتحان کن.

> [!IMPORTANT]
> **از سخنرانی و اجراشده روی جعبهٔ ساخت: چرا بررسی سمت سرور؟**
> دیوید با ابزار توسعه‌دهندهٔ مرورگر یک `option` تازه برای volleyball به منو اضافه می‌کند و Kelly با آن برای ورزشی ثبت‌نام می‌کند که اصلاً در فهرست نبود؛ نتیجه: «هرگز به ورودی کاربر اعتماد نکن». برای همین `app.py` بررسی می‌کند که `sport` در فهرست `SPORTS` باشد. روی جعبهٔ ساخت: POST با `sport=Soccer` پیام `You are registered!` داد، و POST با `sport=""` یا `sport=Chess` پیام `You are not registered!`.

> [!TIP]
> **تألیفی: یک فهرست، دو کار**
> `SPORTS` هم گزینه‌های منو را می‌سازد (با `{% for sport in sports %}`) و هم معیار اعتبارسنجی است. اگر ورزشی اضافه شود، فقط یک جا را عوض می‌کنی.

## دکمه‌های رادیویی

- می‌توانی گزینه‌ها را به شکل دکمهٔ رادیویی نشان دهی. `index.html` را این‌طور بهتر کن:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Register</h1>
    <form action="/register" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        {% for sport in sports %}
            <input name="sport" type="radio" value="{{ sport }}"> {{ sport }}
        {% endfor %}
        <button type="submit">Register</button>
    </form>
{% endblock %}
```

- `type` به `radio` تغییر کرده است. دوباره با `flask run` ببین رابط کاربری چطور عوض شده است.
- چون همهٔ دکمه‌ها `name="sport"` یکسانی دارند، مرورگر فقط یکی را در هر لحظه انتخاب‌شده نگه می‌دارد (از سخنرانی).

## اشتباه‌های رایج

- اعتماد به اینکه منو فقط گزینه‌های مجاز را می‌فرستد.
- نام‌های متفاوت برای دکمه‌های رادیویی یک گروه.
- فراموش کردن گزینهٔ خالی `<option selected value="">` و پیش‌فرض گرفتن یک ورزش.

## جمع‌بندی

- `{% for %}` در قالب گزینه‌ها را از فهرست پایتون می‌سازد.
- اعتبارسنجی سمت سرور لازم است چون HTML در دست کاربر است.
- رادیوها با `name` یکسان فقط یک انتخاب می‌دهند.

## پیوندها

- قبلی: [مقدار پیش‌فرض در قالب: if/else در Jinja](/kb/d/w09-n07)
- بعدی: [دیکشنری ثبت‌نام‌ها، redirect و پیام خطا](/kb/d/w09-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
