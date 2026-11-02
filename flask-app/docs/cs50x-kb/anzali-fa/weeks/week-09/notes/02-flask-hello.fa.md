---
id: w09-n02
type: note
title: 'Flask: نخستین برنامه، مسیر و تزئین‌گر (Flask: app.py and Routes)'
title_fa: 'Flask: نخستین برنامه، مسیر و تزئین‌گر'
title_en: 'Flask: app.py and Routes'
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
- src-transcript-9
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-flask
- w09-c-flask-run
- w09-c-app-py-requirements
- w09-c-flask-app-object
- w09-c-decorator
- w09-c-return-text-html
prev: w09-n01
next: w09-n03
order: 2
video:
  youtube_id: am7POvSZ4GE
  start: '4:54'
  start_seconds: 294
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=294s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'are going to use something called Flask'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# Flask: نخستین برنامه، مسیر و تزئین‌گر

> **منبع رسمی:** بخش «Flask» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#flask). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴:۵۴ تا حدود ۱۸:۲۴](https://www.youtube.com/watch?v=am7POvSZ4GE&t=294s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برای ساختن صفحهٔ پویا باید برنامه‌ای داشته باشی که درخواست‌ها را بگیرد و برای هر **مسیر** پاسخی بسازد. Flask کوچک‌ترین راه برای این کار در پایتون است.

## مسیرها و Flask

- این هفته با **مسیرها** (routes) کار می‌کنیم، مثل `https://www.example.com/route?key=value`؛ سرور بر اساس کلیدها و مقدارهای نشانی کاری را انجام می‌دهد.
- **Flask** یک کتابخانهٔ شخص ثالث است که با آن می‌توانی برنامهٔ وب را با چارچوب Flask، یا به تعبیر دقیق‌تر یک **ریزچارچوب** (micro-framework)، در پایتون میزبانی کنی.
- در [cs50.dev](https://cs50.dev) با دستور `flask run` در پنجرهٔ ترمینال Flask را اجرا می‌کنی.
- برای این کار دو فایل لازم است: `app.py` که کدی دارد که به Flask می‌گوید برنامهٔ وب‌ات را چطور اجرا کند (d156)، و `requirements.txt` که فهرست کتابخانه‌های لازم برای اجرای برنامه است.
- نمونهٔ `requirements.txt`:

```text
Flask
```

- فقط `Flask` در فایل آمده، چون برای اجرای برنامهٔ Flask فقط خود Flask لازم است.

## نخستین برنامه

- یک برنامهٔ بسیار ساده در `app.py`:

```python
# Says hello to world by returning a string of text

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world"
```

- مسیر `/` فقط متن `hello, world` را برمی‌گرداند. (اجراشده روی جعبهٔ ساخت: درخواست `GET /` با کلاینت آزمایشی Flask پاسخ `hello, world` می‌دهد.)
- می‌توانی به جای متن ساده HTML هم برگردانی:

```python
# Says hello to world by returning a string of HTML

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<!DOCTYPE html><html lang="en"><head><title>hello</title></head><body>hello, world</body></html>'
```

> [!NOTE]
> **از سخنرانی: سه خط اول**
> دیوید خط به خط توضیح می‌دهد: `from flask import Flask` تابع (در واقع کلاس) `Flask` را می‌آورد؛ `app = Flask(__name__)` برنامه‌ای از روی همین فایل می‌سازد؛ و `@app.route("/")` که به آن **تزئین‌گر** (decorator) می‌گویند، به Flask می‌گوید هر وقت درخواستی برای `/` آمد، تابع زیرش را اجرا کند.

> [!TIP]
> **تألیفی: نام تابع مهم نیست، مسیر مهم است**
> اگر تابع `index` را `homepage` بنامی، باز هم درخواست `/` به همان تابع می‌رسد؛ چیزی که مسیر را تعیین می‌کند رشتهٔ داخل `@app.route` است. تمرین «Hello, Flask» هم همین را می‌گوید.

## اشتباه‌های رایج

- اجرای `flask run` بیرون از پوشه‌ای که `app.py` در آن است.
- فراموش کردن `requirements.txt` وقتی برنامه کتابخانهٔ دیگری لازم دارد.
- گذاشتن چیزی میان تزئین‌گر و `def`؛ تزئین‌گر درست روی تعریف تابع می‌نشیند.

## جمع‌بندی

- Flask یک ریزچارچوب وب در پایتون است و با `flask run` اجرا می‌شود.
- `app.py` منطق برنامه و `requirements.txt` فهرست کتابخانه‌هاست.
- `@app.route("/")` تابع را به مسیر وصل می‌کند و مقدار بازگشتی تابع، پاسخ است.

## پیوندها

- قبلی: [صفحهٔ ایستا، صفحهٔ پویا و http-server](/kb/d/w09-n01)
- بعدی: [render_template، پوشهٔ templates و request.args](/kb/d/w09-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
