---
id: w09-n14
type: note
title: جست‌وجوی برنامه‌ها، LIKE و Ajax (Shows and APIs)
title_fa: جست‌وجوی برنامه‌ها، LIKE و Ajax
title_en: Shows and APIs
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Shows
official_anchor: shows
source_url: https://cs50.harvard.edu/x/2026/notes/9/#shows
source_refs:
- src-notes-9#shows
- src-notes-9#apis
- src-transcript-9
- src-mdn-js
- src-sqlite-docs
- src-src9-index
- src-flask-box-9
- src-anzali-authored-9
- src-anzali-inference-9
- src-srt-9
concept_ids:
- w09-c-like-search
- w09-c-none-guard
- w09-c-api
- w09-c-ajax
- w09-c-fetch-await
- w09-c-partial-template
- w09-c-encode-uri
prev: w09-n13
next: w09-n15
order: 14
video:
  youtube_id: am7POvSZ4GE
  start: '2:15:59'
  start_seconds: 8159
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=8159s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'I have lastly a directory called shows'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جست‌وجوی برنامه‌ها، LIKE و Ajax

> **منبع رسمی:** بخش «Shows» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#shows). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۱۵:۵۹ تا حدود ۲:۲۱:۱۱](https://www.youtube.com/watch?v=am7POvSZ4GE&t=8159s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

جست‌وجو یکی از رایج‌ترین کارهای وب است. در این بخش اول جست‌وجویی می‌بینی که با هر جست‌وجو صفحهٔ تازه‌ای می‌سازد، سپس نسخه‌ای که با **Ajax** همان‌طور که تایپ می‌کنی فقط فهرست نتایج را عوض می‌کند.

## shows: جست‌وجو با LIKE

- برنامه‌ای ازپیش‌ساخته به نام `shows` را در `app.py` دیدیم:

```python
# Searches for shows using LIKE

from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///shows.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + "%")
    return render_template("search.html", shows=shows)
```

- مسیر `search` راهی برای جست‌وجوی یک `show` فراهم می‌کند. این جست‌وجو دنبال عنوان‌هایی می‌گردد که `LIKE` عبارت کاربر باشند.
- `index.html` را هم بررسی کردیم:

```jinja
{% extends "layout.html" %}

{% block body %}

    <form action="/search" method="get">
        <input autocomplete="off" autofocus name="q" placeholder="Query" type="search">
        <button type="submit">Search</button>
    </form>

{% endblock %}
```

- بقیهٔ فایل‌ها در [کد منبع](https://cdn.cs50.net/2025/fall/lectures/9/src9/shows1/) هستند.

> [!WARNING]
> **اجراشده روی جعبهٔ ساخت (با پایگاه دادهٔ تألیفی): /search بدون q (d159)**
> `GET /search?q=office` دو عنوان تألیفی `The Office` و `Office Ladies` را برگرداند (LIKE در SQLite برای حروف انگلیسی به بزرگی و کوچکی حساس نیست). اما `GET /search` بدون `q` در سطر ۱۶ خطای `TypeError: can only concatenate str (not "NoneType") to str` داد و پاسخ 500 شد. نسخهٔ بعدی (پایین) با `if q:` همین را درست می‌کند.

## API و Ajax

- **رابط برنامه‌نویسی کاربردی** (application program interface) یا **API** مجموعه‌ای از مشخصات است که به تو اجازه می‌دهد با خدمت دیگری کار کنی. مثلاً می‌توانستیم از API سایت IMDb برای کار با پایگاه داده‌اش استفاده کنیم، یا APIهایی برای انواع خاصی از داده که از سرور بارگیری می‌شوند به کار ببریم.
- در نسخهٔ بهترشدهٔ `app.py` برای `shows` این را دیدیم:

```python
# Searches for shows using Ajax

from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///shows.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
    else:
        shows = []
    return render_template("search.html", shows=shows)
```

- مسیر `search` یک پرس‌وجوی SQL اجرا می‌کند.
- `search.html` بسیار ساده است:

```jinja
{% for show in shows %}
    <li>{{ show["title"] }}</li>
{% endfor %}
```

- این قالب فقط چند مورد فهرست نقطه‌دار می‌سازد؛ بدون `<html>` و `<body>`، چون قرار است درون صفحهٔ موجود نشانده شود.
- در پایان، در `index.html` کد **Ajax** جست‌وجو را پیش می‌برد:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>shows</title>
    </head>

    <body>

        <input autocomplete="off" autofocus placeholder="Query" type="search">

        <ul></ul>

        <script>
            let input = document.querySelector('input');
            input.addEventListener('input', async function() {
                let response = await fetch('/search?q=' + input.value);
                let shows = await response.text();
                document.querySelector('ul').innerHTML = shows;
            });
        </script>

    </body>

</html>
```

- یک شنوندهٔ رویداد به کار رفته تا هر بار با پرس‌وجو از سرور فهرستی هم‌خوان با عنوان واردشده بگیرد. این کد تگ `ul` را در HTML پیدا می‌کند و صفحه را طوری تغییر می‌دهد که فهرست نتایج را داشته باشد.
- درس‌نامه برای مطالعهٔ بیشتر به [مستندات Ajax](https://api.jquery.com/category/ajax/) پیوند می‌دهد؛ آن صفحه دربارهٔ jQuery است، در حالی که کد بالا از `fetch` خود مرورگر استفاده می‌کند. برای `fetch` صفحهٔ [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) مناسب‌تر است (d162).

> [!NOTE]
> **از سخنرانی: زبانهٔ Network**
> دیوید در ابزار توسعه‌دهنده نشان می‌دهد که با هر حرفی که تایپ می‌کند یک درخواست تازه به `/search?q=...` فرستاده می‌شود و پاسخ فقط چند `<li>` است، نه یک صفحهٔ کامل.

> [!TIP]
> **تألیفی، اجراشده روی جعبهٔ ساخت: رشتهٔ پرس‌وجو را encode کن (d161)**
> کد بالا `input.value` را مستقیم به نشانی می‌چسباند. اگر کاربر `Tom & Jerry` بنویسد، Flask فقط `q='Tom '` دریافت می‌کند، چون `&` جداکنندهٔ پارامترهاست. با `encodeURIComponent(input.value)` نشانی `Tom%20%26%20Jerry` می‌شود و Flask همان `Tom & Jerry` را می‌گیرد.

> [!TIP]
> **استنتاجی: LIMIT بدون ORDER BY (d164)**
> `LIMIT 50` بدون `ORDER BY` مشخص نمی‌کند کدام ۵۰ سطر برگردد؛ SQLite معمولاً به ترتیب rowid برمی‌گرداند، اما این تضمین SQL نیست.

## اشتباه‌های رایج

- استفاده از مقدار `request.args.get("q")` بدون بررسی `None`.
- برگرداندن یک صفحهٔ کامل با `<html>` برای قطعه‌ای که درون `ul` نشانده می‌شود.
- فراموش کردن `await` پیش از `fetch` یا `response.text()`.

## جمع‌بندی

- `LIKE ?` با `"%" + q + "%"` عنوان‌های شامل عبارت را پیدا می‌کند؛ `if q:` جلوی خطای `None` را می‌گیرد.
- Ajax یعنی جاوااسکریپت بدون بارگذاری دوبارهٔ صفحه از سرور داده می‌گیرد.
- `fetch` و `await` پاسخ را می‌گیرند و `innerHTML` فهرست را به‌روز می‌کند.

## پیوندها

- قبلی: [سبد خرید با session و IN (?)](/kb/d/w09-n13)
- بعدی: [JSON و jsonify: جمع‌بندی](/kb/d/w09-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
