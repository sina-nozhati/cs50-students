---
id: w09-n15
type: note
title: 'JSON و jsonify: جمع‌بندی (JSON)'
title_fa: 'JSON و jsonify: جمع‌بندی'
title_en: JSON
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: JSON
official_anchor: json
source_url: https://cs50.harvard.edu/x/2026/notes/9/#json
source_refs:
- src-notes-9#json
- src-notes-9#summing-up
- src-mdn-js
- src-flask-box-9
- src-anzali-authored-9
- src-anzali-inference-9
- src-srt-9
concept_ids:
- w09-c-json
- w09-c-jsonify
- w09-c-response-json
- w09-c-escape-order
prev: w09-n14
next: w09-summary
order: 15
video:
  youtube_id: am7POvSZ4GE
  start: '2:21:11'
  start_seconds: 8471
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=8471s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'or in something called JSON format'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# JSON و jsonify: جمع‌بندی

> **منبع رسمی:** بخش «JSON» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#json). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۲۱:۱۱](https://www.youtube.com/watch?v=am7POvSZ4GE&t=8471s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

فرستادن HTML آماده از سرور ساده است، اما بیشتر APIهای واقعی **داده** می‌فرستند، نه HTML. **JSON** قالب رایج این داده‌هاست و Flask با `jsonify` آن را می‌سازد.

## JSON

- **نشانه‌گذاری شیء جاوااسکریپت** (JavaScript Object Notation) یا **JSON** یک فایل متنی از دیکشنری‌ها با کلید و مقدار است؛ راهی خام و رایانه‌پسند برای گرفتن داده‌های زیاد.
- JSON راه بسیار مفیدی برای گرفتن داده از سرور است.
- این را در `index.html`ی که با هم بررسی کردیم می‌بینی:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>shows</title>
    </head>

    <body>

        <input autocomplete="off" autofocus placeholder="Query" type="text">

        <ul></ul>

        <script>
            let input = document.querySelector('input');
            input.addEventListener('input', async function() {
                let response = await fetch('/search?q=' + input.value);
                let shows = await response.json();
                let html = '';
                for (let i in shows) {
                    let title = shows[i].title.replace('<', '&lt;').replace('&', '&amp;');
                    html += '<li>' + title + '</li>';
                }
                document.querySelector('ul').innerHTML = html;
            });
        </script>

    </body>

</html>
```

- شاید این کد کمی رمزآلود باشد، اما نقطهٔ شروعی است تا خودت دربارهٔ JSON و کاربردش در برنامه‌های وب‌ات تحقیق کنی.
- `app.py` را هم بررسی کردیم تا ببینیم پاسخ JSON چطور ساخته می‌شود:

```python
# Searches for shows using Ajax with JSON

from cs50 import SQL
from flask import Flask, jsonify, render_template, request

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
    return jsonify(shows)
```

- `jsonify` نتیجه را به قالبی خوانا و پذیرفتنی برای برنامه‌های وب امروزی تبدیل می‌کند.
- برای مطالعهٔ بیشتر [مستندات JSON](https://www.json.org/json-en.html) را ببین.
- خلاصه اینکه حالا می‌توانی برنامه‌های وب خودت را با پایتون، Flask، HTML و SQL کامل کنی.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت (با پایگاه دادهٔ تألیفی)**
> `GET /search?q=office` این JSON را داد (اجرای تألیفی روی فیکسچر؛ هر سطر جدول یک شیء؛ ستون‌های خالی `null`):
>
> ```text
> [{"episodes":null,"id":1,"title":"The Office","year":null},{"episodes":null,"id":2,"title":"Office Ladies","year":null}]
> ```
>
> و `GET /search` بدون `q` فقط `[]` داد.

> [!WARNING]
> **اجراشده روی جعبهٔ ساخت: ترتیب escape در کد بالا (d160)**
> سطر `title.replace('<', '&lt;').replace('&', '&amp;')` دو اشکال دارد. اول، `&` را **پس از** `<` escape می‌کند، پس `&lt;` که خودش ساخته دوباره به `&amp;lt;` تبدیل می‌شود: در Node، عنوان `<b>` به `&amp;lt;b>` تبدیل شد و مرورگر متن `&lt;b>` را نشان می‌دهد. دوم، `replace` با الگوی رشته‌ای فقط **اولین** مورد را عوض می‌کند: `a<b<c` شد `a&amp;lt;b<c`. عادت امن‌تر (تألیفی): اول `&` و بعد `<` را با `replaceAll` عوض کن، یا عنوان را با `textContent` در عنصر بگذار تا اصلاً HTML تفسیر نشود.

## جمع‌بندی درس

در این درس یاد گرفتی با پایتون، SQL و Flask برنامهٔ وب بسازی. به‌طور مشخص دربارهٔ این‌ها صحبت کردیم:

- Flask
- فرم‌ها
- قالب‌ها
- روش‌های درخواست
- Flask و SQL
- کوکی و جلسه
- APIها
- JSON

## اشتباه‌های رایج

- فرستادن فهرست پایتون با `return shows` به جای `jsonify(shows)` (استنتاجی؛ Flask فهرست را هم به JSON تبدیل می‌کند، اما `jsonify` نیت را روشن می‌کند).
- فراموش کردن `await response.json()`.
- گذاشتن دادهٔ کاربر در `innerHTML` بدون escape درست.

## جمع‌بندی

- JSON متن ساخت‌یافته از کلید و مقدار است؛ `jsonify` فهرست ردیف‌های `db.execute` را به آن تبدیل می‌کند.
- در مرورگر `response.json()` آن را دوباره به آرایه‌ای از شیءها تبدیل می‌کند.
- ساختن HTML از داده در مرورگر یعنی escape کردن به عهدهٔ توست.

## پیوندها

- قبلی: [جست‌وجوی برنامه‌ها، LIKE و Ajax](/kb/d/w09-n14)
- بعدی: [خلاصهٔ هفته](/kb/d/w09-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
