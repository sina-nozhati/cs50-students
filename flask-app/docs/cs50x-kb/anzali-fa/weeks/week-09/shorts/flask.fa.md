---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-sh-flask
type: short-summary
title: 'ویدئوی کوتاه: Flask (Flask)'
title_fa: Flask
title_en: Flask
parent: w09-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/flask/
source_refs:
- src-short-flask
- src-anzali-inference-9
concept_ids:
- w09-c-static-page
- w09-c-dynamic-page
- w09-c-flask
- w09-c-flask-app-object
- w09-c-decorator
- w09-c-methods-param
- w09-c-request-method
- w09-c-request-form
- w09-c-redirect
- w09-c-session
- w09-c-render-template
- w09-c-flask-app-env-old
prev: w09-sec
next: w09-sh-ajax
order: 18
video:
  youtube_id: X0dwkDh8kwA
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: چرا پایتون برای وب؟
    evidence_en: null
  - start: 0:49
    start_seconds: 49
    title_fa: چارچوب‌های وب و Flask
    evidence_en: web frameworks
  - start: '2:01'
    start_seconds: 121
    title_fa: محدودیت HTML ایستا
    evidence_en: static
  - start: '3:58'
    start_seconds: 238
    title_fa: نمونهٔ ساعت پویا
    evidence_en: datetime
  - start: '5:26'
    start_seconds: 326
    title_fa: 'شروع: from flask import Flask'
    evidence_en: getting started
  - start: '7:13'
    start_seconds: 433
    title_fa: تزئین‌گر @app.route
    evidence_en: decorator
  - start: '8:29'
    start_seconds: 509
    title_fa: اجرای برنامه در IDE (روش قدیمی)
    evidence_en: export
  - start: '10:38'
    start_seconds: 638
    title_fa: گرفتن داده از نشانی
    evidence_en: show slash
  - start: '11:21'
    start_seconds: 681
    title_fa: فرم و POST
    evidence_en: post requests
  - start: '14:02'
    start_seconds: 842
    title_fa: request.method
    evidence_en: request.method
  - start: '14:35'
    start_seconds: 875
    title_fa: تابع‌های مفید Flask
    evidence_en: URL underscore for
  - start: '15:23'
    start_seconds: 923
    title_fa: session و render_template
    evidence_en: Session is useful
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: Flask (Flask)

> **منبع رسمی:** [صفحهٔ Short «Flask» در CS50x](https://cs50.harvard.edu/x/shorts/flask/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

داگ لوید توضیح می‌دهد چرا پشت بسیاری از وب‌سایت‌ها پایتون است: پایتون برای شبکه و نگه داشتن اتصال‌ها امکانات آماده‌ای دارد که در C با کد بسیار زیاد ممکن است. **چارچوب‌های وب** مثل Django، Pyramid و Flask بخشی از این کار تکراری را هم برمی‌دارند. CS50 از Flask استفاده می‌کند چون سبک و در عین حال پرامکانات است.

محدودیت اصلی HTML این است که **ایستا** است: صفحه‌ای که ساعت فعلی کمبریج را نشان می‌دهد یک دقیقه بعد غلط است و مدیر سایت باید هر دقیقه آن را دستی عوض کند. با پایتون صفحه **پویا** می‌شود؛ ویدئو برنامهٔ کوچکی نشان می‌دهد که با `datetime` و `pytz` تاریخ و ساعت نیویورک را تا ده‌هزارم ثانیه برمی‌گرداند و با هر بارگذاری به‌روز می‌شود.

سپس اجزای یک برنامهٔ Flask را می‌شمارد: `from flask import Flask`، `app = Flask(__name__)`، تابع‌های معمولی پایتون مثل `index` و `sample`، و **تزئین‌گر** `@app.route` که هر تابع را به یک نشانی وصل می‌کند. داده را می‌توان با GET در خود نشانی فرستاد (مسیر `/show/<number>` که عدد را به تابع می‌دهد) یا با فرم و POST؛ برای POST باید `methods=["GET", "POST"]` را در تزئین‌گر نوشت و با `request.method` دو رفتار را جدا کرد.

در پایان چند تابع مفید Flask را معرفی می‌کند: `url_for` برای ساختن نشانی از روی نام تابع، `redirect`، `session` برای داده‌ای که در همهٔ صفحه‌ها در دسترس است (مثلاً اینکه کاربر وارد شده)، و `render_template` برای قالب‌هایی که HTML و Jinja را ترکیب می‌کنند.

## نکته‌های کلیدی

- HTML ایستاست؛ کد سمت سرور صفحه را پویا می‌کند.
- Flask یک چارچوب وب سبک پایتون است.
- `@app.route("/")` یک تابع را به یک نشانی وصل می‌کند.
- `/show/<number>` بخشی از نشانی را به پارامتر تابع تبدیل می‌کند.
- پیش‌فرض Flask فقط GET است؛ برای POST باید `methods` را مشخص کرد.
- `get` در `request.form.get` یعنی «بگیر»، نه روش GET.
- `url_for`، `redirect`، `session` و `render_template` ابزارهای پرکاربرد Flask‌اند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`flask.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — چرا پایتون برای وب؟](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=0s)
- [۰:۴۹ — چارچوب‌های وب و Flask](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=49s)
- [۲:۰۱ — محدودیت HTML ایستا](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=121s)
- [۳:۵۸ — نمونهٔ ساعت پویا](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=238s)
- [۵:۲۶ — شروع: from flask import Flask](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=326s)
- [۷:۱۳ — تزئین‌گر @app.route](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=433s)
- [۸:۲۹ — اجرای برنامه در IDE (روش قدیمی)](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=509s)
- [۱۰:۳۸ — گرفتن داده از نشانی](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=638s)
- [۱۱:۲۱ — فرم و POST](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=681s)
- [۱۴:۰۲ — request.method](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=842s)
- [۱۴:۳۵ — تابع‌های مفید Flask](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=875s)
- [۱۵:۲۳ — session و render_template](https://www.youtube.com/watch?v=X0dwkDh8kwA&t=923s)

> [!NOTE]
> **یادداشت (d167، d168)**
> این ویدئو در ۲۰۱۷ و با CS50 IDE ضبط شده است: نام فایل را `application.py` می‌گذارد و پیش از `flask run` دو فرمان `export FLASK_APP=application.py` و `export FLASK_DEBUG=1` را اجرا می‌کند. در CS50x 2026 فایل `app.py` نام دارد و در cs50.dev فقط `flask run` کافی است. همچنین Finance را «problem set 7» می‌نامد؛ امروز Finance در پرابلم‌ست ۹ است.

> [!TIP]
> **نکته (تألیفی)**
> تکه‌کد login که ویدئو از کد آغازین Finance نشان می‌دهد (بررسی خالی بودن `username` با `request.form.get`) همان الگوی اعتبارسنجی سمت سرور است که در [یادداشت اعتبارسنجی](/kb/d/w09-n08) دیدی.

## مفاهیم مرتبط

- صفحهٔ ایستا: همان HTML ازپیش‌نوشته که در مرورگر (سمت کاربر) نمایش داده می‌شود — [یادداشت](/kb/d/w09-n01) · درس کوتاه `w09-l01` (واحد `w09-l01-u01`)
- صفحهٔ پویا: HTML که سمت سرور با کد و بر اساس ورودی ساخته می‌شود — [یادداشت](/kb/d/w09-n01) · درس کوتاه `w09-l01` (واحد `w09-l01-u01`)
- Flask: کتابخانهٔ شخص ثالث و ریزچارچوب وب در پایتون — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- app = Flask(__name__): ساختن برنامه از روی کلاس Flask — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- تزئین‌گر @app.route("/") که تابع را به یک مسیر وصل می‌کند — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- methods=["POST"] در @app.route — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u01`)
- یک مسیر برای GET و POST و تشخیص با request.method — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u02`)
- request.form.get برای داده‌های POST — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u01`)
- redirect و پاسخ 302 به مسیری دیگر — [یادداشت](/kb/d/w09-n09) · درس کوتاه `w09-l04` (واحد `w09-l04-u02`)
- جلسه (session): یادآوری کاربر بین درخواست‌ها با کمک کوکی — [یادداشت](/kb/d/w09-n11) · درس کوتاه `w09-l06` (واحد `w09-l06-u01`)
- render_template برای فرستادن یک قالب HTML با متغیرها — [یادداشت](/kb/d/w09-n03) · درس کوتاه `w09-l01` (واحد `w09-l01-u03`)
- روش قدیمی export FLASK_APP و application.py در CS50 IDE — [یادداشت](/kb/d/w09-sh-flask)

## منابع

- [ویدئو در YouTube](https://youtu.be/X0dwkDh8kwA) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/flask/flask.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/flask/lang/en/flask.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/flask/lang/en/flask.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
