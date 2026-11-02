---
id: w09-n06
type: note
title: GET و POST، request.form و request.method (Request Methods)
title_fa: GET و POST، request.form و request.method
title_en: Request Methods
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Request Methods
official_anchor: request-methods
source_url: https://cs50.harvard.edu/x/2026/notes/9/#request-methods
source_refs:
- src-notes-9#request-methods
- src-transcript-9
- src-pset-9
- src-pset-9-birthdays
- src-pset-9-finance
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-get-in-url
- w09-c-methods-param
- w09-c-request-form
- w09-c-405
- w09-c-request-method
prev: w09-n05
next: w09-n07
order: 6
video:
  youtube_id: am7POvSZ4GE
  start: '44:03'
  start_seconds: 2643
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=2643s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase "but there's also something called post"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# GET و POST، request.form و request.method

> **منبع رسمی:** بخش «Request Methods» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#request-methods). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۴:۰۳ تا حدود ۵۲:۱۴](https://www.youtube.com/watch?v=am7POvSZ4GE&t=2643s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

با GET هر چیزی که در فرم نوشته شود در نشانی و تاریخچهٔ مرورگر دیده می‌شود. برای گذرواژه یا هر دادهٔ حساسی این خوب نیست. **POST** داده را «عمیق‌تر» در پاکت مجازی درخواست می‌گذارد.

## از GET به POST

- می‌توانی موقعیت‌هایی را تصور کنی که GET امن نیست؛ نام کاربری و گذرواژه در نشانی دیده می‌شوند.
- با تغییر `app.py` از روش `post` استفاده کن:

```python
# Switches to POST

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))
```

- `POST` به مسیر `/greet` اضافه شده و به جای `request.args.get` از `request.form.get` استفاده می‌کنیم.
- این به سرور می‌گوید در پاکت مجازی **عمیق‌تر** را نگاه کند و داده‌های `post` را در نشانی نشان ندهد.

> [!NOTE]
> **از سخنرانی و اجراشده روی جعبهٔ ساخت: Method Not Allowed**
> اگر فرم هنوز با `method="get"` بفرستد، یا خودت `/greet` را در نوار نشانی باز کنی، مسیری که فقط POST می‌پذیرد پاسخ **405 Method Not Allowed** می‌دهد. روی جعبهٔ ساخت `GET /greet` با این `app.py` دقیقاً همین را داد. پس `method="post"` فرم هم باید عوض شود.

## یک مسیر برای هر دو

- می‌توان کد را بهتر کرد و GET و POST را در **یک مسیر** انجام داد:

```python
# Uses a single route

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template("index.html")
```

- هر دو در یک مسیر انجام می‌شوند؛ `request.method` نشان می‌دهد کاربر کدام نوع درخواست را فرستاده است.
- بنابراین `index.html` را این‌طور تغییر بده:

```jinja
{% extends "layout.html" %}

{% block body %}

    <form action="/" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Greet</button>
    </form>

{% endblock %}
```

- `action` فرم عوض شده است.

> [!TIP]
> **تألیفی: GET یعنی «نشان بده»، POST یعنی «این را بگیر»**
> وقتی کاربر صفحه را باز می‌کند (GET) فرم را نشان بده؛ وقتی فرم را می‌فرستد (POST) داده را پردازش کن. این الگو در Birthdays و Finance بارها تکرار می‌شود.

## اشتباه‌های رایج

- اضافه کردن `methods=["POST"]` و فراموش کردن `"GET"` در مسیری که باید فرم را هم نشان دهد.
- خواندن داده‌های POST با `request.args` (نتیجه `None` است).
- فکر کردن به اینکه POST یعنی رمزگذاری؛ داده فقط در نشانی نیست. برای امنیت انتقال HTTPS لازم است (هفتهٔ ۸).

## جمع‌بندی

- `methods=["GET", "POST"]` روش‌های مجاز مسیر را تعیین می‌کند؛ روش دیگر ۴۰۵ می‌گیرد.
- داده‌های GET در `request.args` و داده‌های POST در `request.form` هستند.
- `request.method` اجازه می‌دهد یک تابع هر دو حالت را مدیریت کند.

## پیوندها

- قبلی: [قالب مادر: layout.html، block و extends](/kb/d/w09-n05)
- بعدی: [مقدار پیش‌فرض در قالب: if/else در Jinja](/kb/d/w09-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
