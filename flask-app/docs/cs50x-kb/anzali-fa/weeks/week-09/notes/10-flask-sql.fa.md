---
id: w09-n10
type: note
title: 'Flask و SQL: ذخیرهٔ ماندگار و getlist (Flask and SQL)'
title_fa: 'Flask و SQL: ذخیرهٔ ماندگار و getlist'
title_en: Flask and SQL
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Flask and SQL
official_anchor: flask-and-sql
source_url: https://cs50.harvard.edu/x/2026/notes/9/#flask-and-sql
source_refs:
- src-notes-9#flask-and-sql
- src-transcript-9
- src-flask-docs
- src-src9-index
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-flask-sql
- w09-c-getlist
- w09-c-checkbox
- w09-c-hidden-input
- w09-c-post-for-changes
- w09-c-sql-in-route
prev: w09-n09
next: w09-n11
order: 10
video:
  youtube_id: am7POvSZ4GE
  start: '1:32:03'
  start_seconds: 5523
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=5523s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase "let's assume that the database shall be called"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# Flask و SQL: ذخیرهٔ ماندگار و getlist

> **منبع رسمی:** بخش «Flask and SQL» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#flask-and-sql). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۳۲:۰۳ تا حدود ۱:۵۵:۵۰](https://www.youtube.com/watch?v=am7POvSZ4GE&t=5523s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

همان‌طور که در هفتهٔ ۷ دیدی پایتون با پایگاه دادهٔ SQL کار می‌کند، اینجا Flask و پایتون و SQL را با هم ترکیب می‌کنیم تا داده **ماندگار** شود و با راه‌اندازی دوبارهٔ سرور از بین نرود.

## گام‌ها

- این [پایگاه دادهٔ SQL](https://cdn.cs50.net/2025/fall/lectures/9/src9/froshims7/froshims.db) را در پوشهٔ `froshims` بارگیری کن.
- در ترمینال `sqlite3 froshims.db` را اجرا کن و `.schema` را بزن تا محتوای فایل پایگاه داده را ببینی. سپس `SELECT * FROM registrants;` را بزن. می‌بینی که فعلاً هیچ ثبت‌نامی در فایل نیست.
- `requirements.txt` را تغییر بده:

```text
cs50
Flask
```

- `index.html` را تغییر بده:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Register</h1>
    <form action="/register" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        {% for sport in sports %}
            <input name="sport" type="checkbox" value="{{ sport }}"> {{ sport }}
        {% endfor %}
        <button type="submit">Register</button>
    </form>
{% endblock %}
```

- `layout.html` را تغییر بده:

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

- مطمئن شو `error.html` این‌طور است:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Error</h1>
    <p>{{ message }}</p>
    <img alt="Grumpy Cat" src="/static/cat.jpg">
{% endblock %}
```

- `registrants.html` را تغییر بده:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Registrants</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Sport</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            {% for registrant in registrants %}
                <tr>
                    <td>{{ registrant.name }}</td>
                    <td>{{ registrant.sport }}</td>
                    <td>
                        <form action="/deregister" method="post">
                            <input name="id" type="hidden" value="{{ registrant.id }}">
                            <button type="submit">Deregister</button>
                        </form>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

- مقدار پنهان `registrant.id` اضافه شده تا بعداً بتوان از این `id` در `app.py` استفاده کرد.
- در پایان `app.py` را تغییر بده:

```python
# Implements a registration form, storing registrants in a SQLite database, with support for multiple sports and deregistration

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")

@app.route("/register", methods=["POST"])
def register():

    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    # Validate sports
    sports = request.form.getlist("sport")
    if not sports:
        return render_template("error.html", message="Missing sport")
    for sport in sports:
        if sport not in SPORTS:
            return render_template("error.html", message="Invalid sport")

    # Remember registrant
    for sport in sports:
        db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
```

- کتابخانهٔ `cs50` به کار رفته است. مسیری برای `register` با روش `post` هست. این مسیر نام و ورزش را از فرم می‌گیرد و با یک پرس‌وجوی SQL `name` و `sport` را به جدول `registrants` اضافه می‌کند. مسیر `deregister` با یک پرس‌وجوی SQL `id` کاربر را می‌گیرد و با آن ثبت‌نام او را حذف می‌کند.
- `flask run` را اجرا کن و نتیجه را بررسی کن. [پیاده‌سازی ما](https://cdn.cs50.net/2025/fall/lectures/9/src9/froshims7/) و [مستندات Flask](https://flask.palletsprojects.com) هم در دسترس‌اند.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت (با پایگاه دادهٔ تألیفی): checkbox و getlist**
> با جدول خالی `registrants`، یک POST با `name=David` و دو مقدار `sport` (Soccer و Basketball) دو سطر ساخت (id 1 و 2). سپس POST به `/deregister` با `id=1` سطر اول را حذف کرد و فقط `2|David|Basketball` ماند. `request.form.getlist("sport")` همهٔ تیک‌ها را برمی‌گرداند؛ `get` فقط اولی را.

> [!IMPORTANT]
> **از سخنرانی و اجراشده روی جعبهٔ ساخت: حذف با GET نه**
> دیوید می‌پرسد چرا بد است بتوان با GET کسی را حذف کرد: با GET هر مسیر را می‌توان با یک پیوند ساده باز کرد؛ اگر مهاجمی نشانی‌ای مثل `/deregister?id=4` را در ایمیلی برای مسئول برنامه بفرستد و او بی‌احتیاط روی آن کلیک کند، کسی بی‌خبر حذف می‌شود (نمونه‌ای از حملهٔ فیشینگ). درخواست‌های GET نباید دادهٔ سرور را تغییر دهند؛ برای POST معمولاً باید روی دکمه‌ای کلیک کرد. برای همین `/deregister` فقط POST می‌پذیرد؛ روی جعبهٔ ساخت `GET /deregister` پاسخ 405 داد.

## اشتباه‌های رایج

- ساختن SQL با f-string به جای جای‌نگهدار `?` (تزریق SQL، هفتهٔ ۷).
- `request.form.get("sport")` برای checkbox؛ فقط یک مقدار می‌دهد.
- اعتبارسنجی نکردن تک‌تک ورزش‌های رسیده.

## جمع‌بندی

- `db = SQL("sqlite:///froshims.db")` و `db.execute(..., ?)` داده را در فایل ماندگار می‌کند.
- checkbox چند مقدار با یک `name` می‌فرستد و `getlist` همه را می‌خواند.
- input پنهان `id` را برای حذف می‌فرستد و تغییر داده با POST انجام می‌شود.

## پیوندها

- قبلی: [دیکشنری ثبت‌نام‌ها، redirect و پیام خطا](/kb/d/w09-n09)
- بعدی: [MVC، کوکی و جلسه (session)](/kb/d/w09-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
