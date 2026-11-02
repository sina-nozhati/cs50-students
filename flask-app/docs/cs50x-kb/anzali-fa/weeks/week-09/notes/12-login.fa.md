---
id: w09-n12
type: note
title: 'ورود و خروج با session (Cookies and Session: Login)'
title_fa: ورود و خروج با session
title_en: 'Cookies and Session: Login'
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Cookies and Session
official_anchor: cookies-and-session
source_url: https://cs50.harvard.edu/x/2026/notes/9/#cookies-and-session
source_refs:
- src-notes-9#cookies-and-session
- src-pset-9
- src-pset-9-finance
- src-flask-docs
- src-src9-index
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-flask-session
- w09-c-session-dict
- w09-c-logout-clear
prev: w09-n11
next: w09-n13
order: 12
video:
  youtube_id: am7POvSZ4GE
  start: '2:02:51'
  start_seconds: 7371
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=7371s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'which is just going to be a relatively simple flask application'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ورود و خروج با session

> **منبع رسمی:** بخش «Cookies and Session» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#cookies-and-session). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۲:۵۱ تا حدود ۲:۰۹:۲۰](https://www.youtube.com/watch?v=am7POvSZ4GE&t=7371s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

ساده‌ترین شکل «ورود» این است که نام کاربر را در جلسه نگه داری و در هر صفحه بپرسی: آیا نامی در جلسه هست؟ این همان الگویی است که Finance با `user_id` به کار می‌برد.

## فایل‌های login

- پوشه‌ای به نام `login` بساز و این فایل‌ها را اضافه کن.
- اول `requirements.txt`:

```text
Flask
Flask-Session
```

- افزون بر `Flask`، `Flask-Session` را هم آورده‌ایم که برای پشتیبانی از جلسه‌های ورود لازم است.
- دوم، در پوشهٔ `templates` فایلی به نام `layout.html`:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>login</title>
    </head>

    <body>
        {% block body %}{% endblock %}
    </body>

</html>
```

- این یک چیدمان بسیار ساده با عنوان و بدنه است.
- سوم، فایل `index.html` در `templates`:

```jinja
{% extends "layout.html" %}

{% block body %}

    {% if name %}
        You are logged in as {{ name }}. <a href="/logout">Log out</a>.
    {% else %}
        You are not logged in. <a href="/login">Log in</a>.
    {% endif %}

{% endblock %}
```

- این فایل نگاه می‌کند که آیا نامی هست: اگر باشد پیام خوشامد نشان می‌دهد و اگر نباشد پیشنهاد می‌کند به صفحهٔ ورود بروی. (درس‌نامه می‌گوید این فایل وجود `session["name"]` را بررسی می‌کند؛ دقیق‌تر، قالب متغیر `name` را می‌بیند که `app.py` با `session.get("name")` پر می‌کند؛ d165.)
- چهارم، فایل `login.html`:

```jinja
{% extends "layout.html" %}

{% block body %}

    <form action="/login" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Log In</button>
    </form>

{% endblock %}
```

- این چیدمان یک صفحهٔ ورود ساده است.
- در پایان `app.py`:

```python
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
```

- به importهای تغییریافته در بالای فایل دقت کن، از جمله `session` که پشتیبانی از جلسه را ممکن می‌کند. مهم‌تر از همه، ببین `session["name"]` در مسیرهای `login` و `logout` چطور به کار رفته است. مسیر `login` نام واردشده را در `session["name"]` می‌گذارد. در مسیر `logout`، خروج با پاک کردن `session` انجام می‌شود.
- انتزاع `session` به تو اجازه می‌دهد مطمئن شوی فقط کاربری مشخص به دادهٔ مشخصی دسترسی دارد و هیچ‌کس به جای کاربر دیگری کاری نمی‌کند، چه خوب و چه بد!
- [پیاده‌سازی ما](https://cdn.cs50.net/2025/fall/lectures/9/src9/login/) و توضیح جلسه‌ها در [مستندات Flask](https://flask.palletsprojects.com/en/stable/api/#flask.session) در دسترس‌اند.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: چرخهٔ ورود و خروج**
> با کلاینت آزمایشی Flask که کوکی‌ها را بین درخواست‌ها نگه می‌دارد: `GET /` پیام `You are not logged in.` داد؛ POST به `/login` با `name=David` پاسخ 302 به `/` داد؛ `GET /` بعدی `You are logged in as David.` نوشت؛ `GET /logout` دوباره 302 داد و پس از آن `GET /` باز `You are not logged in.` بود.

> [!TIP]
> **تألیفی: session.get به جای session["name"]**
> `session["name"]` وقتی کاربر هنوز وارد نشده `KeyError` می‌دهد؛ `session.get("name")` در این حالت `None` برمی‌گرداند و قالب به شاخهٔ «وارد نشده‌ای» می‌رود. مسیر `index` به همین دلیل از `get` استفاده می‌کند.

## اشتباه‌های رایج

- فراموش کردن `Session(app)` یا تنظیم `SESSION_TYPE`.
- خواندن `session["name"]` بدون بررسی وجود آن.
- پاک نکردن جلسه هنگام خروج.

## جمع‌بندی

- `session` مثل یک دیکشنری مخصوص هر کاربر است.
- ورود: نوشتن در `session`؛ خروج: `session.clear()`.
- Flask-Session با `SESSION_TYPE = "filesystem"` دادهٔ جلسه را روی دیسک سرور نگه می‌دارد.

## پیوندها

- قبلی: [MVC، کوکی و جلسه (session)](/kb/d/w09-n11)
- بعدی: [سبد خرید با session و IN (?)](/kb/d/w09-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
