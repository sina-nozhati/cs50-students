---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-pr-helloflask
type: practice-guide
title: راهنمای سلام، Flask (Hello, Flask)
title_fa: سلام، Flask (Hello, Flask)
title_en: Hello, Flask
parent: w09-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/helloflask/
source_refs:
- src-practice-helloflask#implementation-details
- src-practice-helloflask#templates
- src-practice-helloflask#forms
- src-practice-helloflask#post
- src-anzali-authored-9
concept_ids:
- w09-c-flask-forms-practice
- w09-c-flask
- w09-c-flask-app-object
- w09-c-decorator
- w09-c-return-text-html
- w09-c-flask-run
- w09-c-templates-folder
- w09-c-render-template
- w09-c-layout
- w09-c-block
- w09-c-extends
- w09-c-select-menu
- w09-c-405
- w09-c-methods-param
- w09-c-request-method
- w09-c-request-form
- w09-c-server-validation
problem_set_ref: weeks/week-09/problem-sets/helloflask.json
prev: w09-ps-finance
next: null
order: 28
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای سلام، Flask (Hello, Flask)

> **منبع رسمی:** [Hello, Flask](https://cs50.harvard.edu/x/2026/practice/helloflask/) از مسئله‌های تمرینی هفتهٔ ۹ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

یک تمرین راهنمادار: از کوچک‌ترین برنامهٔ Flask با یک فایل `app.py` شروع می‌کنی که «Hello, World!» برمی‌گرداند، سپس قالب‌ها و `layout.html` را اضافه می‌کنی، یک فرم با منوی کشویی رنگ می‌سازی و در پایان مسیر `/` را برای پذیرفتن POST تغییر می‌دهی تا رنگ انتخاب‌شده در صفحهٔ `color.html` نشان داده شود.

هدف‌های رسمی: ساختن یک برنامهٔ سادهٔ Flask برای شناخت این چارچوب و آشنایی با Jinja. صفحهٔ رسمی خودش کد هر گام را می‌دهد؛ این راهنما فقط گام نخست را بازتولید می‌کند و بقیه را پیوند می‌دهد (D76). کار واقعی تو پرسش پایانی است: اعتبارسنجی رنگ.

> **از سخنرانی:** برنامهٔ hello در [یادداشت Flask](/kb/d/w09-n02)؛ قالب‌ها در [یادداشت قالب‌ها](/kb/d/w09-n03)؛ `layout.html` در [یادداشت layout](/kb/d/w09-n05)؛ POST و 405 در [یادداشت روش‌های درخواست](/kb/d/w09-n06)؛ اعتبارسنجی با فهرست مجاز در [یادداشت اعتبارسنجی](/kb/d/w09-n08).

## خواسته‌های رسمی

1. ساده‌ترین برنامهٔ Flask فقط یک فایل `app.py` دارد که صفحه‌ای می‌سازد و سلام می‌کند؛ با `flask run` اجرایش کن و بعد متن دیگری مثل `<h1>Hello, World!</h1>` برگردان.
2. پوشهٔ `templates` با `layout.html` و `index.html` (که از layout ارث می‌برد) بساز و `index` را طوری تغییر بده که `render_template` کند.
3. به `index.html` فرمی با منوی کشویی `color` اضافه کن که با POST به `/` فرستاده شود؛ پیش از تغییر مسیر، پیام «Method not allowed» می‌بینی.
4. مسیر `/` را برای GET و POST تنظیم کن: GET فرم را نشان دهد و POST رنگ را بخواند و `color.html` را با آن رنگ رندر کند.
5. فکر کن چه کدی اضافه کنی تا فقط رنگ‌های معتبر (مثلاً `red` و `blue`) پذیرفته شوند.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل را دانلود کن. فایل آغازین از نشانی پاییز ۲۰۲۲ می‌آید (d177). صفحهٔ رسمی می‌گوید check50 ندارد و تحویل لازم نیست.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/9/helloflask.zip
unzip helloflask.zip
rm helloflask.zip
```

## فرمان‌ها و قطعه‌های رسمی صفحه

> **رسمی:** این فرمان‌ها و قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند.

گام نخست: کوچک‌ترین `app.py` رسمی:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"
```

تزئین‌گری که مسیر `/` را به تابع وصل می‌کند:

```python
@app.route("/")
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- از متن ساده تا قالب و فرم POST در Hello, Flask — [یادداشت](/kb/d/w09-pr-helloflask)
- Flask: کتابخانهٔ شخص ثالث و ریزچارچوب وب در پایتون — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- app = Flask(__name__): ساختن برنامه از روی کلاس Flask — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- تزئین‌گر @app.route("/") که تابع را به یک مسیر وصل می‌کند — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- مقدار بازگشتی تابع مسیر، متن یا HTML پاسخ است — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- اجرای برنامه با flask run در cs50.dev — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- پوشهٔ templates و ساختار پوشه‌های برنامه — [یادداشت](/kb/d/w09-n03) · درس کوتاه `w09-l01` (واحد `w09-l01-u03`)
- render_template برای فرستادن یک قالب HTML با متغیرها — [یادداشت](/kb/d/w09-n03) · درس کوتاه `w09-l01` (واحد `w09-l01-u03`)
- قالب مادر layout.html برای بخش مشترک صفحه‌ها — [یادداشت](/kb/d/w09-n05) · درس کوتاه `w09-l02` (واحد `w09-l02-u02`)
- {% block body %}{% endblock %}: جای خالی برای محتوای هر صفحه — [یادداشت](/kb/d/w09-n05) · درس کوتاه `w09-l02` (واحد `w09-l02-u02`)
- {% extends "layout.html" %}: ارث‌بری از قالب مادر — [یادداشت](/kb/d/w09-n05) · درس کوتاه `w09-l02` (واحد `w09-l02-u02`)
- منوی کشویی select و option با value — [یادداشت](/kb/d/w09-n08) · درس کوتاه `w09-l04` (واحد `w09-l04-u01`)
- خطای 405 Method Not Allowed وقتی روش درخواست مجاز نیست — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u01`)
- methods=["POST"] در @app.route — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u01`)
- یک مسیر برای GET و POST و تشخیص با request.method — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u02`)
- request.form.get برای داده‌های POST — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u01`)
- اعتبارسنجی سمت سرور: بررسی وجود و مجاز بودن مقدار — [یادداشت](/kb/d/w09-n08) · درس کوتاه `w09-l04` (واحد `w09-l04-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. گام‌ها را به ترتیب صفحهٔ رسمی پیش ببر و پس از هر گام برنامه را اجرا کن؛ هر گام فقط یک چیز تازه دارد.
2. اگر «TemplateNotFound» دیدی، نام و جای پوشهٔ `templates` را بررسی کن.
3. وقتی «Method not allowed» دیدی، از خودت بپرس مسیر `/` اکنون کدام روش‌ها را می‌پذیرد و چطور می‌شود آن را عوض کرد.
4. برای اعتبارسنجی، الگوی `SPORTS` در froshims را به یاد بیاور: یک فهرست ثابت از مقدارهای مجاز و بررسی عضویت پیش از استفاده.

## اشتباه‌های رایج

- گذاشتن `layout.html` بیرون از `templates`
- نام بلوک متفاوت در layout و صفحهٔ فرزند (صفحه خالی می‌ماند)
- فراموش کردن `request` در import
- اعتماد به اینکه منوی کشویی فقط `red` یا `blue` می‌فرستد

## چک‌لیست خودآزمایی

1. `flask run` برنامه را اجرا می‌کند و `/` متن سلام را نشان می‌دهد.
2. برگرداندن `<h1>...</h1>` را امتحان کرده‌ام و تفاوت را دیده‌ام.
3. `index.html` از `layout.html` ارث می‌برد و محتوایش درون `block` است.
4. پیش از افزودن `methods`، فرستادن فرم خطای 405 می‌دهد.
5. پس از تغییر مسیر، انتخاب رنگ صفحه‌ای با همان رنگ نشان می‌دهد.
6. رنگی خارج از فهرست مجاز (مثلاً با ابزار توسعه‌دهنده) پذیرفته نمی‌شود.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با `flask run` و چک‌لیست بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چه کد دیگری می‌توانی اضافه کنی تا مطمئن شوی رنگ‌هایی که دریافت می‌کنی رنگ‌های معتبری‌اند؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [بقیهٔ گام‌های رسمی (Templates، Forms، POST)](https://cs50.harvard.edu/x/practice/helloflask/#templates): صفحهٔ رسمی کد کامل `layout.html`، `index.html`، `color.html` و `app.py` نهایی را می‌دهد؛ در این بسته بازتولید نشده‌اند (D76).

## پیوند رسمی

- [Hello, Flask](https://cs50.harvard.edu/x/2026/practice/helloflask/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
