---
id: w09-n13
type: note
title: سبد خرید با session و IN (?) (Shopping Cart)
title_fa: سبد خرید با session و IN (?)
title_en: Shopping Cart
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Shopping Cart
official_anchor: shopping-cart
source_url: https://cs50.harvard.edu/x/2026/notes/9/#shopping-cart
source_refs:
- src-notes-9#shopping-cart
- src-src9-index
- src-flask-box-9
- src-anzali-authored-9
- src-anzali-inference-9
- src-srt-9
concept_ids:
- w09-c-session-list
- w09-c-sql-in-list
prev: w09-n12
next: w09-n14
order: 13
video:
  youtube_id: am7POvSZ4GE
  start: '2:09:20'
  start_seconds: 7760
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=7760s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'of e-commerce site that has an actual shopping cart'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# سبد خرید با session و IN (?)

> **منبع رسمی:** بخش «Shopping Cart» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#shopping-cart). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۹:۲۰ تا حدود ۲:۱۵:۵۹](https://www.youtube.com/watch?v=am7POvSZ4GE&t=7760s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

جلسه فقط برای نام کاربر نیست؛ هر داده‌ای که باید بین درخواست‌ها بماند، مثل **سبد خرید**، می‌تواند در `session` باشد. این آخرین مثال از توانایی Flask در فعال کردن جلسه است.

## store

- کد `store` در `app.py` را دیدیم:

```python
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")
    return render_template("books.html", books=books)

@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exists
    if "cart" not in session:
        session["cart"] = []

    # POST
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)
```

- `cart` با یک فهرست پیاده‌سازی شده است. با دکمه‌های `Add to Cart` در `books.html` کالا به این فهرست اضافه می‌شود. با کلیک روی چنین دکمه‌ای روش `post` فراخوانی می‌شود و `id` کالا به `cart` افزوده می‌شود. هنگام دیدن سبد، با روش `get`، یک پرس‌وجوی SQL اجرا می‌شود تا فهرست کتاب‌های سبد نشان داده شود.
- محتوای `books.html` را هم دیدیم:

```jinja
{% extends "layout.html" %}

{% block body %}

    <h1>Books</h1>
    {% for book in books %}
        <h2>{{ book["title"] }}</h2>
        <form action="/cart" method="post">
            <input name="id" type="hidden" value="{{ book['id'] }}">
            <button type="submit">Add to Cart</button>
        </form>
    {% endfor %}

{% endblock %}
```

- این کد با `for book in books` برای هر کتاب امکان `Add to Cart` می‌سازد.
- بقیهٔ فایل‌های این پیاده‌سازی در [کد منبع](https://cdn.cs50.net/2025/fall/lectures/9/src9/store/) هستند.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت (با پایگاه دادهٔ تألیفی دوکتابی): IN (?) با فهرست**
> با یک `cart.html` سادهٔ تألیفی: سبد خالی هیچ کتابی نشان نداد (کتابخانهٔ cs50 نسخهٔ 9.5.0 با فهرست خالی هم پرس‌وجو را اجرا کرد). سه POST به ترتیب با `id=2`، `id=1` و دوباره `id=2` هر کدام 302 به `/cart` دادند و سبد در پایان `Book A` و `Book B` را نشان داد: به ترتیب id، نه ترتیب افزودن، و `Book B` فقط یک‌بار. کتابخانهٔ cs50 فهرست را به‌جای `?` در `IN (?)` به چند مقدار تبدیل می‌کند (d166).

> [!TIP]
> **استنتاجی: ترتیب سبد**
> همان‌طور که در اجرای بالا دیدی، `WHERE id IN (...)` هر ردیف جدول را حداکثر یک‌بار برمی‌گرداند و بدون `ORDER BY` ترتیب افزودن را تضمین نمی‌کند. برای نشان دادن تعداد هر کتاب باید آن را خودت بشماری.

## اشتباه‌های رایج

- فرض اینکه `session["cart"]` همیشه وجود دارد؛ کد اول آن را می‌سازد.
- ساختن `IN (...)` با الحاق رشته به جای `?`.
- دور انداختن `redirect` پس از POST.

## جمع‌بندی

- فهرست در `session` سبد خرید هر کاربر را جدا نگه می‌دارد.
- input پنهان `id` هر کتاب را به `/cart` می‌فرستد.
- `WHERE id IN (?)` با یک فهرست، چند ردیف را با یک پرس‌وجو می‌آورد.

## پیوندها

- قبلی: [ورود و خروج با session](/kb/d/w09-n12)
- بعدی: [جست‌وجوی برنامه‌ها، LIKE و Ajax](/kb/d/w09-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
