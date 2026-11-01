---
id: w09-n09
type: note
title: 'دیکشنری ثبت‌نام‌ها، redirect و پیام خطا (Frosh IMs: Registrants and Redirect)'
title_fa: دیکشنری ثبت‌نام‌ها، redirect و پیام خطا
title_en: 'Frosh IMs: Registrants and Redirect'
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
- src-src9-index
- src-flask-box-9
- src-anzali-authored-9
- src-anzali-inference-9
- src-srt-9
concept_ids:
- w09-c-error-template
- w09-c-in-memory-dict
- w09-c-redirect
- w09-c-jinja-dict-loop
- w09-c-static-folder
prev: w09-n08
next: w09-n10
order: 9
video:
  youtube_id: am7POvSZ4GE
  start: '1:22:04'
  start_seconds: 4924
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=4924s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'to make my life easier here called registrants'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# دیکشنری ثبت‌نام‌ها، redirect و پیام خطا

> **منبع رسمی:** بخش «Frosh IMs» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#frosh-ims). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۲:۰۴ تا حدود ۱:۳۲:۰۳](https://www.youtube.com/watch?v=am7POvSZ4GE&t=4924s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا ثبت‌نام فقط پیام «ثبت شدی» نشان می‌داد و چیزی به خاطر نمی‌ماند. حالا ثبت‌نام‌ها را در یک دیکشنری نگه می‌داریم، کاربر را به صفحهٔ فهرست **هدایت** (redirect) می‌کنیم و پیام خطای دقیق‌تری می‌دهیم.

## دیکشنری REGISTRANTS و redirect

- `app.py` را این‌طور بهتر کن:

```python
# Implements a registration form, storing registrants in a dictionary, with error messages

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

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

    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    # Validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    # Remember registrant
    REGISTRANTS[name] = sport

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)
```

- دیکشنری‌ای به نام `REGISTRANTS` با `REGISTRANTS[name]` ورزش انتخاب‌شده را ثبت می‌کند. همچنین `registrants=REGISTRANTS` دیکشنری را به قالب می‌فرستد.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: redirect یعنی 302**
> پس از POST موفق، پاسخ `/register` کد وضعیت **302** با سرآیند `Location: /registrants` است؛ مرورگر خودش درخواست تازه‌ای به `/registrants` می‌فرستد. این همان کدهای 30x هفتهٔ ۸ است.

## قالب خطا و قالب فهرست

- `error.html` را بساز:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Error</h1>
    <p>{{ message }}</p>
    <img alt="Grumpy Cat" src="/static/cat.jpg">
{% endblock %}
```

- و قالب تازهٔ `registrants.html`:

```jinja
{% extends "layout.html" %}

{% block body %}
    <h1>Registrants</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Sport</th>
            </tr>
        </thead>
        <tbody>
            {% for name in registrants %}
                <tr>
                    <td>{{ name }}</td>
                    <td>{{ registrants[name] }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

- `{% for name in registrants %}...{% endfor %}` روی تک‌تک ثبت‌نام‌شده‌ها می‌چرخد. توانایی پیمایش در یک صفحهٔ پویا بسیار قدرتمند است!
- در پایان پوشه‌ای به نام `static` کنار `app.py` بساز و این [تصویر گربه](https://cdn.cs50.net/2025/fall/lectures/9/src9/froshims4/static/cat.jpg) را در آن بگذار.
- `flask run` را اجرا کن و با برنامه کار کن.

> [!TIP]
> **تألیفی: پیمایش دیکشنری در Jinja**
> مانند پایتون، `for name in registrants` روی **کلیدها** می‌چرخد و `registrants[name]` مقدار هر کلید (ورزش) را می‌دهد. روی جعبهٔ ساخت، پس از ثبت `David` برای `Soccer`، صفحهٔ `/registrants` یک سطر جدول با `David` و `Soccer` نشان داد.

## مشکل‌ها

- حالا یک برنامهٔ وب داری! اما چند اشکال امنیتی هست. چون همه‌چیز در حافظه نگه داشته می‌شود، مهاجم می‌تواند HTML را تغییر دهد و وب‌سایت را «هک» کند. افزون بر این، اگر سرور خاموش شود این داده‌ها **ماندگار نیستند**. آیا راهی هست که داده حتی با راه‌اندازی دوبارهٔ سرور باقی بماند؟

> [!NOTE]
> **استنتاجی: یک نام، یک ورزش**
> چون کلید دیکشنری `name` است، اگر همان نام دوباره با ورزش دیگری ثبت شود، ورزش قبلی جایگزین می‌شود. نسخهٔ SQL یادداشت بعد این محدودیت را ندارد.

## اشتباه‌های رایج

- `return render_template("registrants.html")` پس از POST به جای redirect؛ با تازه‌سازی صفحه، فرم دوباره فرستاده می‌شود (استنتاجی).
- فراموش کردن `redirect` در `from flask import ...`.
- گذاشتن تصویر در `templates`؛ فایل‌های ثابت در `static` قرار می‌گیرند.

## جمع‌بندی

- `redirect("/registrants")` پاسخ 302 می‌دهد و مرورگر را به مسیر دیگری می‌برد.
- `error.html` با متغیر `message` یک قالب برای همهٔ خطاهاست.
- دادهٔ درون حافظه با خاموش شدن سرور از بین می‌رود.

## پیوندها

- قبلی: [Frosh IMs: منوی select، حلقهٔ for و اعتبارسنجی سمت سرور](/kb/d/w09-n08)
- بعدی: [Flask و SQL: ذخیرهٔ ماندگار و getlist](/kb/d/w09-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
