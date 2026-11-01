---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-ps-birthdays
type: problem-set-guide
title: راهنمای زادروزها (Birthdays)
title_fa: زادروزها (Birthdays)
title_en: Birthdays
parent: w09-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/9/birthdays/
source_refs:
- src-pset-9-birthdays#implementation-details
- src-pset-9-birthdays#testing
- src-anzali-authored-9
- src-pset-9
concept_ids:
- w09-c-flask-run
- w09-c-request-method
- w09-c-request-form
- w09-c-form-to-route
- w09-c-flask-sql
- w09-c-sql-in-route
- w09-c-render-template
- w09-c-jinja-for
- w09-c-redirect
- w09-c-post-redirect-get
- w09-c-server-validation
- w09-c-hidden-input
- w09-c-post-for-changes
problem_set_ref: weeks/week-09/problem-sets/birthdays.json
prev: w09-sh-ajax
next: w09-ps-finance
order: 26
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای زادروزها (Birthdays)

> **منبع رسمی:** [Birthdays](https://cs50.harvard.edu/x/2026/psets/9/birthdays/) از پرابلم‌ست ۹ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

یک برنامهٔ وب Flask می‌سازی که تولد دوستانت را نگه دارد. برنامهٔ آغازین یک مسیر `/` دارد که هم GET و هم POST را می‌پذیرد، یک پایگاه دادهٔ `birthdays.db` با جدول `birthdays` (ستون‌های `id`، `name`، `month` و `day`) که چند سطر دارد، یک `styles.css` و قالب `index.html`.

در GET باید همهٔ تولدها در یک جدول نشان داده شوند؛ در POST باید تولد تازه‌ای به پایگاه داده اضافه شود و دوباره صفحهٔ اصلی نمایش یابد. این راهنما کد هیچ بخشی از راه‌حل را ندارد: نه فرم، نه پرس‌وجوی SQL و نه حلقهٔ قالب. همهٔ ابزارهای لازم در یادداشت‌ها و درس‌های کوتاه این هفته روی نمونه‌های دیگر (froshims، store، shows) تمرین شده‌اند.

> **از سخنرانی:** فرم POST و `request.form.get` در [یادداشت روش‌های درخواست](/kb/d/w09-n06)؛ `redirect` در [یادداشت ثبت‌نام‌ها](/kb/d/w09-n09)؛ `db.execute` با `?`، input پنهان و حذف با POST در [یادداشت Flask و SQL](/kb/d/w09-n10)؛ `{% for %}` در [یادداشت اعتبارسنجی](/kb/d/w09-n08). [جلسهٔ حل تمرین](/kb/d/w09-sec) همین برنامه را گام‌به‌گام می‌سازد؛ پیش از تلاش خودت تماشایش نکن.

## خواسته‌های رسمی

1. برنامهٔ وبی را کامل کن که کاربر بتواند تولدها را ذخیره و پیگیری کند.
2. وقتی `/` با GET خواسته شود، همهٔ افراد پایگاه داده همراه تولدشان در یک جدول نشان داده شوند.
3. در `app.py`، در بخش GET، همهٔ تولدها را از `birthdays.db` بخوان و همه را به قالب `index.html` بده.
4. در `index.html` هر تولد را یک سطر جدول کن با دو ستون: نام و تاریخ تولد.
5. وقتی `/` با POST خواسته شود، تولد تازه به پایگاه داده اضافه شود و سپس صفحهٔ اصلی دوباره نمایش داده شود.
6. در `index.html` فرمی بساز که نام، ماه و روز تولد را بگیرد و به `/` (action) با روش `post` بفرستد.
7. در `app.py`، در بخش POST، بر اساس دادهٔ کاربر یک سطر تازه با `INSERT` به جدول `birthdays` اضافه کن.
8. اختیاری: امکان حذف یا ویرایش تولدها، یا هر امکان دیگری به انتخاب خودت.
9. check50 ندارد؛ چند تولد اضافه کن و ببین در جدول درست ظاهر می‌شوند. در پوشهٔ `birthdays` فرمان `flask run` را اجرا کن.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. پس از `ls` باید `app.py`، `birthdays.db`، `static/` و `templates/` را ببینی. برای دیدن برنامه در پوشهٔ `birthdays` فرمان `flask run` را اجرا کن. اکنون مسیر POST فقط به `/` برمی‌گرداند (redirect)؛ صفحهٔ رسمی می‌گوید پس از POST صفحه «re-render» شود، اما کد آغازین با redirect دوباره به GET می‌رود (d174).

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/9/birthdays.zip
unzip birthdays.zip
rm birthdays.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd birthdays
ls
```

## نمونه‌های رسمی ورودی و خروجی

خروجی رسمی `ls`:

```text
app.py  birthdays.db  static/  templates/
```

## راهنمایی‌های رسمی

> **رسمی:** بازنویسی فارسی بخش Hints صفحهٔ رسمی.

- صفحهٔ رسمی در بخش Hints گام‌به‌گام فرم، خواندن دادهٔ فرم، `INSERT`، اعتبارسنجی و حلقهٔ قالب را نشان می‌دهد. چون این گام‌ها روی هم تقریباً کل راه‌حل‌اند، در این بسته فقط پیوند داده شده‌اند (بخش «فقط پیوند» پایین).

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- اجرای برنامه با flask run در cs50.dev — [یادداشت](/kb/d/w09-n02) · درس کوتاه `w09-l01` (واحد `w09-l01-u02`)
- یک مسیر برای GET و POST و تشخیص با request.method — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u02`)
- request.form.get برای داده‌های POST — [یادداشت](/kb/d/w09-n06) · درس کوتاه `w09-l03` (واحد `w09-l03-u01`)
- فرمی که با action داده را به مسیر دیگری مثل /greet می‌فرستد — [یادداشت](/kb/d/w09-n04) · درس کوتاه `w09-l02` (واحد `w09-l02-u01`)
- Flask با کتابخانهٔ cs50 و db.execute برای ماندگاری داده — [یادداشت](/kb/d/w09-n10) · درس کوتاه `w09-l05` (واحد `w09-l05-u01`)
- جای‌نگهدار ? در db.execute داخل مسیر — [یادداشت](/kb/d/w09-n10) · درس کوتاه `w09-l05` (واحد `w09-l05-u01`)
- render_template برای فرستادن یک قالب HTML با متغیرها — [یادداشت](/kb/d/w09-n03) · درس کوتاه `w09-l01` (واحد `w09-l01-u03`)
- {% for %} ... {% endfor %} برای ساختن تکرارشونده‌ها در قالب — [یادداشت](/kb/d/w09-n08) · درس کوتاه `w09-l04` (واحد `w09-l04-u01`)
- redirect و پاسخ 302 به مسیری دیگر — [یادداشت](/kb/d/w09-n09) · درس کوتاه `w09-l04` (واحد `w09-l04-u02`)
- الگوی POST سپس redirect سپس GET — [یادداشت](/kb/d/w09-ps-birthdays)
- اعتبارسنجی سمت سرور: بررسی وجود و مجاز بودن مقدار — [یادداشت](/kb/d/w09-n08) · درس کوتاه `w09-l04` (واحد `w09-l04-u01`)
- input پنهان (type=hidden) برای فرستادن id — [یادداشت](/kb/d/w09-n10) · درس کوتاه `w09-l05` (واحد `w09-l05-u02`)
- تغییر داده (حذف، ثبت) با POST، نه GET — [یادداشت](/kb/d/w09-n10) · درس کوتاه `w09-l05` (واحد `w09-l05-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول کد آغازین را بخوان: کدام شاخهٔ `if` مال POST و کدام مال GET است؟ هر کدام اکنون چه برمی‌گرداند؟ با `sqlite3 birthdays.db` و `.schema` ستون‌های جدول را ببین.
2. از GET شروع کن، چون بدون فرم هم آزمودنی است. در store و froshims دیدی چطور نتیجهٔ `db.execute` (فهرستی از دیکشنری‌ها) را با یک نام به `render_template` بدهی.
3. در قالب، برای هر عضو فهرست یک `<tr>` لازم داری. در یادداشت اعتبارسنجی دیدی `{% for %}` چطور برای هر عضو یک تکه HTML تکرار می‌کند؛ از هر دیکشنری کلیدهای لازم را بخوان.
4. برای فرم از خودت بپرس: هر ورودی چه `name`ی باید داشته باشد تا در `app.py` پیدایش کنی؟ `type` مناسب برای ماه و روز چیست؟ `action` و `method` فرم چه باید باشند؟
5. در POST سه مقدار را با `request.form.get` بخوان و پیش از نوشتن در پایگاه داده فکر کن اگر خالی یا خارج از بازه باشند چه کنی. یادت باشد اعتبارسنجی سمت سرور لازم است، چون HTML را می‌شود دور زد.
6. برای `INSERT` الگوی froshims را به یاد بیاور: یک رشتهٔ SQL با `?` و مقدارها به‌عنوان آرگومان‌های بعدی. پس از آن، همان کاری را نگه دار که کد آغازین می‌کند (برگشت به `/`).

## اشتباه‌های رایج

- نوشتن پرس‌وجو با f-string یا `+` به جای `?` (خطر تزریق SQL)
- فراموش کردن `method="post"` در فرم؛ فرم با GET فرستاده می‌شود و شاخهٔ POST اجرا نمی‌شود
- نام‌گذاری ورودی‌های فرم متفاوت با آنچه `request.form.get` می‌خواند
- فرستادن فهرست به قالب با نامی و خواندنش با نامی دیگر
- رندر کردن مستقیم قالب پس از POST به جای redirect؛ بارگذاری دوباره فرم را دوباره می‌فرستد
- نپذیرفتن ورودی خالی فقط در HTML و نه در سرور

## چک‌لیست خودآزمایی

1. `GET /` جدولی با همهٔ سطرهای `birthdays.db` نشان می‌دهد.
2. هر سطر جدول دقیقاً دو ستون دارد: نام و تاریخ تولد.
3. فرم سه ورودی نام، ماه و روز دارد و با `post` به `/` فرستاده می‌شود.
4. پس از فرستادن فرم، تولد تازه در جدول دیده می‌شود (و با `sqlite3 birthdays.db` هم در جدول هست).
5. پرس‌وجوها با جای‌نگهدار `?` نوشته شده‌اند، نه با f-string یا `+`.
6. فرم خالی یا ماه و روز نامعتبر سطر خرابی به پایگاه داده اضافه نمی‌کند.
7. پس از POST، بارگذاری دوبارهٔ صفحه فرم را دوباره نمی‌فرستد (redirect به GET).
8. چند تولد را با `flask run` در مرورگر آزموده‌ام.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با `flask run` و چک‌لیست بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/birthdays
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های گام‌به‌گام صفحهٔ رسمی (Hints)](https://cs50.harvard.edu/x/psets/9/birthdays/#hints): این بلوک‌ها فرم، `INSERT`، اعتبارسنجی، `SELECT` و حلقهٔ قالب را با کد نشان می‌دهند و روی هم تقریباً کل راه‌حل‌اند (D75)؛ بازتولید نشده‌اند. اول خودت تلاش کن.
- [ویدئوی راهنمای گام‌به‌گام](https://video.cs50.io/HXwvj8x1Fcs): ویدئوی رسمی؛ در زمان CS50 IDE ضبط شده است (d175). فقط پیوند.
- [ویدئوی راه‌حل («Not sure how to solve?»)](https://video.cs50.io/lVwv4o8vmvI): **هشدار:** این ویدئو راه‌حل کامل را نشان می‌دهد. فقط پس از اینکه خودت برنامه را ساختی یا واقعاً گیر کردی نگاهش کن. در نسخهٔ ذخیره‌شدهٔ صفحه نبود و فقط در صفحهٔ زنده یافت شد (d176).

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/HXwvj8x1Fcs)

## پیوند رسمی

- [Birthdays](https://cs50.harvard.edu/x/2026/psets/9/birthdays/)
- [پرابلم‌ست ۹](https://cs50.harvard.edu/x/2026/psets/9/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
