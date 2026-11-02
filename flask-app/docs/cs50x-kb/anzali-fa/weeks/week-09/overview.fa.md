---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-fa
type: week-overview
title: هفتهٔ ۹ — Flask (پایگاه دانش فارسی)
title_fa: هفتهٔ ۹ — Flask
title_en: Week 9 — Flask
parent: week-9
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/9/
source_refs:
- src-week-9#week-9-flask
- src-notes-9#lecture-9
- src-pset-9
- src-short-flask
- src-short-ajax
- src-anzali-authored-9
- src-anzali-inference-9
children:
- w09-n01
- w09-n02
- w09-n03
- w09-n04
- w09-n05
- w09-n06
- w09-n07
- w09-n08
- w09-n09
- w09-n10
- w09-n11
- w09-n12
- w09-n13
- w09-n14
- w09-n15
- w09-summary
- w09-sec
- w09-sh-flask
- w09-sh-ajax
- w09-ps-birthdays
- w09-ps-finance
- w09-pr-helloflask
objective_ids:
- w09-o01
- w09-o02
- w09-o03
- w09-o04
- w09-o05
- w09-o06
- w09-o07
- w09-o08
- w09-o09
- w09-o10
---

# هفتهٔ ۹ — Flask

> **منبع رسمی:** [صفحهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/weeks/9/) و [درس‌نامهٔ هفتهٔ ۹](https://cs50.harvard.edu/x/2026/notes/9/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

هفتهٔ ۸ همه‌چیز سمت مرورگر بود و فرم‌هایت داده را به سایت دیگری می‌فرستادند. این هفته **سرور خودت** را با پایتون و **Flask** می‌نویسی. اول تفاوت صفحهٔ **ایستا** و **پویا** را می‌بینی، بعد با `@app.route` مسیر می‌سازی، با `render_template` و **Jinja** قالب پر می‌کنی و با `request.args` و `request.form` دادهٔ **GET** و **POST** را می‌خوانی.

سپس برنامهٔ ثبت‌نام **froshims** گام‌به‌گام بزرگ می‌شود: منوی کشویی، اعتبارسنجی سمت سرور، `redirect`، و در پایان ذخیره در پایگاه دادهٔ SQLite با `db.execute`. بعد **کوکی** و **جلسه** (session) را برای ورود و سبد خرید یاد می‌گیری و در آخر با **Ajax** و **JSON** جست‌وجویی می‌سازی که بدون بارگذاری دوبارهٔ صفحه نتیجه نشان می‌دهد.

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

Flask. مسیر. تزئین‌گرها. درخواست‌ها و پاسخ‌ها. جلسه‌ها. کوکی‌ها. (Flask. Route. Decorators. Requests, Responses. Sessions. Cookies.)

> **توجه:** دو ویدئوی کوتاه این هفته (Doug Lloyd) در سال ۲۰۱۷ و با CS50 IDE ضبط شده‌اند؛ `application.py`، `export FLASK_APP` و `XMLHttpRequest` و jQuery مال آن زمان‌اند (d167، d169). خلاصهٔ فارسی هر ویدئو این تفاوت‌ها را نشان می‌دهد.

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه، سخنرانی، جلسهٔ حل تمرین و پرابلم‌ست ۹ استخراج کرده است.

- **w09-o01** — تفاوت صفحهٔ ایستا و پویا را توضیح بدهی و بگویی سرور با یک مسیر و رشتهٔ پرس‌وجو چه می‌کند.
- **w09-o02** — یک برنامهٔ Flask با `app.py`، `requirements.txt`، `@app.route` و `flask run` بسازی.
- **w09-o03** — با `render_template` و Jinja (`{{ }}`، `{% if %}`، `{% for %}`) قالب پر کنی و بدانی Jinja خودکار escape می‌کند.
- **w09-o04** — با `layout.html`، `{% extends %}` و `{% block %}` تکرار HTML را حذف کنی.
- **w09-o05** — GET و POST را جدا کنی، `request.args` و `request.form` را بخوانی، `methods` را تنظیم کنی و خطای 405 را بفهمی.
- **w09-o06** — ورودی را سمت سرور با فهرست مجاز اعتبارسنجی کنی و بدانی چرا اعتبارسنجی HTML کافی نیست.
- **w09-o07** — با `redirect` و الگوی POST سپس redirect سپس GET کار کنی.
- **w09-o08** — دادهٔ فرم را با `db.execute` و `?` در SQLite ذخیره کنی، `getlist` و input پنهان را به کار ببری و تغییر داده را با POST انجام بدهی.
- **w09-o09** — کوکی و جلسه را توضیح بدهی و با `session` ورود، خروج و سبد خرید بسازی.
- **w09-o10** — با `fetch` و `jsonify` یک جست‌وجوی Ajax بسازی، رشتهٔ پرس‌وجو را encode کنی و HTML ساخته‌شده در مرورگر را escape کنی.

## پیش‌نیازها

- هفتهٔ ۶: پایتون، تابع، دیکشنری و `try`/`except`. ([نمای کلی هفتهٔ ۶](/kb/d/w06-fa))
- هفتهٔ ۷: SQL، `SELECT`، `INSERT`، `DELETE`، `LIKE` و جای‌نگهدار `?`. ([نمای کلی هفتهٔ ۷](/kb/d/w07-fa))
- هفتهٔ ۸: HTTP، کدهای وضعیت، HTML، فرم‌ها و جاوااسکریپت. ([نمای کلی هفتهٔ ۸](/kb/d/w08-fa))

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: سرور خودت
  ایستا و پویا -> Flask و app.py -> @app.route -> flask run

مرحلهٔ ۲: قالب‌ها
  render_template -> {{ name }} و escape -> request.args -> layout، extends، block

مرحلهٔ ۳: فرم‌ها و روش‌ها
  action -> GET و POST -> methods و 405 -> request.method -> مقدار پیش‌فرض get

مرحلهٔ ۴: froshims
  select و radio -> اعتبارسنجی سمت سرور -> error.html -> redirect و 302

مرحلهٔ ۵: Flask و SQL
  db.execute با ? -> checkbox و getlist -> input پنهان -> حذف با POST

مرحلهٔ ۶: جلسه
  MVC -> کوکی -> session -> ورود و خروج -> سبد خرید و IN (?)

مرحلهٔ ۷: Ajax و JSON
  LIKE و if q -> fetch و await -> قالب تکه‌ای -> jsonify -> escape در مرورگر
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۵ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران.
3. ویدئوهای کوتاه را کنار یادداشت‌ها ببین: [Flask](/kb/d/w09-sh-flask) پس از یادداشت ۶ و [Ajax](/kb/d/w09-sh-ajax) پس از یادداشت ۱۴.
4. مسئلهٔ تمرینی [Hello, Flask](/kb/d/w09-pr-helloflask) را پس از یادداشت ۶ امتحان کن.
5. [جلسهٔ حل تمرین (Section)](/kb/d/w09-sec) بخش نخست پرابلم‌ست، Birthdays، را حل می‌کند؛ اگر می‌خواهی خودت حلش کنی، پس از تلاش خودت ببینش.
6. چالش‌های کوتاه هفته را امتحان کن، آزمون تسلط را بده و بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۹

طبق صفحهٔ رسمی پرابلم‌ست ۹:

- [Birthdays](/kb/d/w09-ps-birthdays) را **تحویل بده**.
- [Finance](/kb/d/w09-ps-finance) را **تحویل بده**.
- پیش از شروع، `update50` را در codespace اجرا کن و وقتی پرسیده شد، **Rebuild now** را بزن.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

مسئلهٔ تمرینی اختیاری: [Hello, Flask](/kb/d/w09-pr-helloflask). صفحهٔ آن می‌گوید check50 ندارد و تحویل لازم نیست.

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود. کد آغازین Finance، سایت راه‌حل کارکنان و ویدئوی راهنما فقط پیوند داده شده‌اند (D74). راهنمایی‌های گام‌به‌گام صفحهٔ رسمی Birthdays و ویدئوی راه‌حل آن روی هم تقریباً کل راه‌حل‌اند و فقط پیوند داده شده‌اند (D75). همهٔ نمونه‌های Flask این بسته با کلاینت آزمایشی Flask و پایگاه‌های دادهٔ تألیفی روی جعبهٔ ساخت اجرا شده‌اند (D72، D73).

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی هر دو پرابلم‌ست کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۹](https://cs50.harvard.edu/x/weeks/9/) · [درس‌نامه](https://cs50.harvard.edu/x/2026/notes/9/) · [ویدئوی سخنرانی](https://video.cs50.io/am7POvSZ4GE)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/9/lecture9.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/9/src9.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/9/lang/en/lecture9.srt)
- [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/9/) · [پرابلم‌ست ۹](https://cs50.harvard.edu/x/2026/psets/9/)
- [مستندات Flask](https://flask.palletsprojects.com/en/stable/) · [مستندات Jinja](https://jinja.palletsprojects.com/en/stable/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
