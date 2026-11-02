---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۹ (Section 9)
title_fa: جلسهٔ حل تمرین هفتهٔ ۹
title_en: Section 9
parent: w09-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian conceptual summary of the official section video/transcript (Kelly, read in full); the session solves Birthdays, so no session code is reproduced (D75); chapter times from section9.srt (inference for boundaries); callout on client-side validation authored
source_url: https://cs50.harvard.edu/x/sections/9/
source_refs:
- src-section-9#week-9-flask
- src-section-9-transcript
- src-section-9-video
- src-section-9-slides
- src-section-9-code
- src-flask-docs
- src-anzali-inference-9
- src-anzali-authored-9
concept_ids:
- w09-c-mvc
- w09-c-static-folder
- w09-c-templates-folder
- w09-c-route
- w09-c-render-template
- w09-c-flask-run
- w09-c-get-in-url
- w09-c-methods-param
- w09-c-form-to-route
- w09-c-request-form
- w09-c-server-validation
- w09-c-flask-sql
- w09-c-sql-in-route
- w09-c-jinja-for
- w09-c-jinja-placeholder
- w09-c-redirect
prev: w09-summary
next: w09-sh-flask
order: 17
video:
  youtube_id: xbguARtzOeI
  chapters:
  - start: 0:02
    start_seconds: 2
    title_fa: 'خوش‌آمد: آخرین جلسهٔ محتوای تازه'
    evidence_en: Welcome to CS 50 week 9
  - start: '1:22'
    start_seconds: 82
    title_fa: مدل MVC در Birthdays
    evidence_en: view of the web application
  - start: '2:43'
    start_seconds: 163
    title_fa: ساختار پوشه‌های Birthdays
    evidence_en: structure of the folder
  - start: '4:16'
    start_seconds: 256
    title_fa: مسیرها و render_template
    evidence_en: talk a little bit about routes
  - start: '6:23'
    start_seconds: 383
    title_fa: 'فرم‌ها: GET یا POST؟'
    evidence_en: request methods, post and get
  - start: '9:25'
    start_seconds: 565
    title_fa: action، method و input
    evidence_en: action and then the route
  - start: '10:57'
    start_seconds: 657
    title_fa: رفتن به VS Code
    evidence_en: move over to VS code
  - start: '16:11'
    start_seconds: 971
    title_fa: ساختن فرم و placeholder
    evidence_en: placeholder
  - start: '20:36'
    start_seconds: 1236
    title_fa: min و max و دور زدن آن‌ها
    evidence_en: inspect element
  - start: '24:54'
    start_seconds: 1494
    title_fa: request.form.get و SQL
    evidence_en: request.form
  - start: '26:29'
    start_seconds: 1589
    title_fa: پرس‌وجو با ? و WHERE
    evidence_en: question mark
  - start: '28:30'
    start_seconds: 1710
    title_fa: اعتبارسنجی ورودی در app.py
    evidence_en: validate user input
  - start: '35:17'
    start_seconds: 2117
    title_fa: 'TypeError: رشته در برابر عدد'
    evidence_en: not supported between
  - start: '41:14'
    start_seconds: 2474
    title_fa: درج در پایگاه داده
    evidence_en: insert these values
  - start: '43:43'
    start_seconds: 2623
    title_fa: 'Jinja: for و نقطه'
    evidence_en: Jinja
  - start: '49:18'
    start_seconds: 2958
    title_fa: نمایش جدول تولدها
    evidence_en: birthday.name
  - start: '51:33'
    start_seconds: 3093
    title_fa: جلوگیری از ورودی خالی و نامعتبر
    evidence_en: last few minutes
  chapters_origin: inference
code_files:
- file: birthdays.zip
  policy: link-only
  reason: Birthdays distribution code; the code written in the session is part of the Birthdays solution (D75)
- file: section9.pdf
  policy: link-only
  reason: slides
---

# جلسهٔ حل تمرین هفتهٔ ۹ (Section)

> **منبع رسمی:** [صفحهٔ Section 9 CS50x](https://cs50.harvard.edu/x/sections/9/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/9/lang/en/section9.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** یا **استنتاجی** برچسب خورده باشد.

> [!WARNING]
> **هشدار: این جلسه بخش نخست پرابلم‌ست را حل می‌کند**
> Kelly در این جلسه Birthdays را از کد آغازین تا برنامهٔ کار‌کننده گام‌به‌گام می‌سازد. این خلاصه فقط ایده‌ها را می‌گوید و کد راه‌حل ندارد (D75). اگر می‌خواهی خودت مسئله را حل کنی، ویدئو را پس از تلاش خودت ببین.

## خلاصه

جلسه را Kelly، مدرس (preceptor) CS50 در هاروارد، اداره می‌کند؛ آخرین جلسهٔ محتوای تازهٔ درس. او می‌گوید Flask جایی است که پایتون، SQL، HTML، CSS و جاوااسکریپت با هم یک برنامهٔ وب تعاملی می‌سازند، و جلسه را روی کد آغازین Birthdays جلو می‌برد.

**MVC و ساختار پوشه.** نما (view) همان صفحه‌ای است که کاربر می‌بیند؛ کنترل‌گر (controller) منطقی است که با زدن دکمهٔ افزودن اجرا می‌شود؛ مدل (model) داده‌ای است که نگه داشته می‌شود. در پوشهٔ `birthdays`، `static/` فایل `styles.css` را دارد، `templates/` قالب‌های HTML را، `app.py` منطق سمت سرور را و `birthdays.db` پایگاه داده را.

**مسیرها و فرم‌ها.** مسیر بخشی از نشانی پس از دامنه است و `@app.route` رفتار هر مسیر را تعیین می‌کند؛ `render_template` یک قالب را برمی‌گرداند و `flask run` برنامه را اجرا می‌کند. Kelly با چند پرسش GET و POST را جدا می‌کند: باز کردن صفحهٔ ورود GET است و فرستادن نام کاربری و گذرواژه POST؛ فرستادن یک تولد هم POST است. در فرم، `action` باید با مسیر سمت پایتون و `method` با روش درخواست جور باشد، و `name` هر ورودی نامی است که سمت سرور با آن مقدار را پیدا می‌کنی.

**اعتبارسنجی.** او به ورودی‌های عددی `min` و `max` می‌دهد، اما سپس با Inspect Element همان محدودیت‌ها را عوض می‌کند و نشان می‌دهد فرم مقدار نامعتبر را هم می‌فرستد؛ پس اعتبارسنجی واقعی باید سمت سرور باشد. سمت سرور، هنگام مقایسهٔ ماه با عدد، خطای `TypeError` می‌بیند: مقدارهای فرم رشته‌اند و باید پیش از مقایسه به عدد تبدیل شوند (با `try` و `except` برای ورودی غیرعددی).

**SQL و Jinja.** `db.execute` با جای‌نگهدار `?` پرس‌وجو را امن اجرا می‌کند و نتیجهٔ `SELECT` فهرستی از دیکشنری‌هاست. در قالب، `{% ... %}` برای دستورهایی مثل حلقه و `{{ ... }}` برای نوشتن یک مقدار است، و Jinja اجازه می‌دهد کلید دیکشنری را با نقطه بخوانی. در پایان Kelly نشان می‌دهد ورودی خالی، متنی یا ماه ۹۹ دیگر به جدول اضافه نمی‌شود.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section9.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۲ — خوش‌آمد: آخرین جلسهٔ محتوای تازه](https://www.youtube.com/watch?v=xbguARtzOeI&t=2s)
- [۱:۲۲ — مدل MVC در Birthdays](https://www.youtube.com/watch?v=xbguARtzOeI&t=82s)
- [۲:۴۳ — ساختار پوشه‌های Birthdays](https://www.youtube.com/watch?v=xbguARtzOeI&t=163s)
- [۴:۱۶ — مسیرها و render_template](https://www.youtube.com/watch?v=xbguARtzOeI&t=256s)
- [۶:۲۳ — فرم‌ها: GET یا POST؟](https://www.youtube.com/watch?v=xbguARtzOeI&t=383s)
- [۹:۲۵ — action، method و input](https://www.youtube.com/watch?v=xbguARtzOeI&t=565s)
- [۱۰:۵۷ — رفتن به VS Code](https://www.youtube.com/watch?v=xbguARtzOeI&t=657s)
- [۱۶:۱۱ — ساختن فرم و placeholder](https://www.youtube.com/watch?v=xbguARtzOeI&t=971s)
- [۲۰:۳۶ — min و max و دور زدن آن‌ها](https://www.youtube.com/watch?v=xbguARtzOeI&t=1236s)
- [۲۴:۵۴ — request.form.get و SQL](https://www.youtube.com/watch?v=xbguARtzOeI&t=1494s)
- [۲۶:۲۹ — پرس‌وجو با ? و WHERE](https://www.youtube.com/watch?v=xbguARtzOeI&t=1589s)
- [۲۸:۳۰ — اعتبارسنجی ورودی در app.py](https://www.youtube.com/watch?v=xbguARtzOeI&t=1710s)
- [۳۵:۱۷ — TypeError: رشته در برابر عدد](https://www.youtube.com/watch?v=xbguARtzOeI&t=2117s)
- [۴۱:۱۴ — درج در پایگاه داده](https://www.youtube.com/watch?v=xbguARtzOeI&t=2474s)
- [۴۳:۴۳ — Jinja: for و نقطه](https://www.youtube.com/watch?v=xbguARtzOeI&t=2623s)
- [۴۹:۱۸ — نمایش جدول تولدها](https://www.youtube.com/watch?v=xbguARtzOeI&t=2958s)
- [۵۱:۳۳ — جلوگیری از ورودی خالی و نامعتبر](https://www.youtube.com/watch?v=xbguARtzOeI&t=3093s)

## کد رسمی جلسه

کد جلسه همان کد آغازین Birthdays است: [birthdays.zip](https://cdn.cs50.net/2026/x/psets/9/birthdays.zip) (`app.py`، `birthdays.db`، `static/styles.css` و `templates/index.html`). کدی که Kelly در جلسه می‌نویسد بخشی از راه‌حل Birthdays است و در این بسته بازتولید نشده است (D75).

> [!NOTE]
> **یادداشت**
> صفحهٔ رسمی Birthdays می‌گوید پس از POST صفحهٔ اصلی «re-render» شود، اما کد آغازین و این جلسه پس از POST به `/` برمی‌گردند (redirect)، که مرورگر را دوباره با GET به همان صفحه می‌برد (d174).

> **تألیفی: چرا فقط min و max کافی نیست؟**
> هر چیزی که در HTML است در دست کاربر است: می‌تواند آن را در ابزار توسعه‌دهنده عوض کند یا درخواست را بدون مرورگر بفرستد. `min` و `max` تجربهٔ کاربری را بهتر می‌کنند، اما فقط بررسی سمت سرور از پایگاه داده محافظت می‌کند. این همان درس volleyball در froshims است.

## نکته‌های کلیدی

- MVC: نما (قالب‌ها)، کنترل‌گر (`app.py`) و مدل (`birthdays.db`).
- `action` فرم باید با مسیر و `method` با روش‌های مجاز آن مسیر جور باشد.
- `name` ورودی همان کلیدی است که `request.form.get` می‌خواند.
- مقدارهای فرم رشته‌اند؛ برای مقایسهٔ عددی باید تبدیلشان کنی.
- اعتبارسنجی سمت مرورگر را می‌شود دور زد؛ سمت سرور هم بسنج.
- در قالب، `{% for %}` تکرار می‌کند و `{{ }}` مقدار می‌نویسد.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
