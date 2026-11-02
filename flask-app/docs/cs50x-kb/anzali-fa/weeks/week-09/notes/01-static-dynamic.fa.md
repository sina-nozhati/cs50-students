---
id: w09-n01
type: note
title: صفحهٔ ایستا، صفحهٔ پویا و http-server (Welcome! and http-server)
title_fa: صفحهٔ ایستا، صفحهٔ پویا و http-server
title_en: Welcome! and http-server
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: http-server
official_anchor: http-server
source_url: https://cs50.harvard.edu/x/2026/notes/9/#http-server
source_refs:
- src-notes-9#http-server
- src-notes-9#welcome
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-static-page
- w09-c-dynamic-page
- w09-c-route
prev: w09-fa
next: w09-n02
order: 1
video:
  youtube_id: am7POvSZ4GE
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# صفحهٔ ایستا، صفحهٔ پویا و http-server

> **منبع رسمی:** بخش «http-server» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#http-server). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۴:۵۴](https://www.youtube.com/watch?v=am7POvSZ4GE&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا هفتهٔ پیش هر صفحه‌ای که ساختی **ایستا** بود: همان HTMLی که نوشته بودی، بی‌کم‌وکاست به مرورگر می‌رسید. این هفته یاد می‌گیری صفحه را **سمت سرور** و با کد پایتون بسازی؛ یعنی صفحه‌ای که بسته به ورودی کاربر هر بار فرق می‌کند. این هفته HTML و CSS و SQL و پایتون و جاوااسکریپت کنار هم قرار می‌گیرند و شاید پایهٔ پروژهٔ پایانی‌ات هم بشوند.

## از «کلاس C» تا «کلاس برنامه‌نویسی»

- در هفته‌های گذشته زبان‌ها، فن‌ها و راهبردهای زیادی دیدی. این درس بیشتر از آنکه «کلاس C» یا «کلاس پایتون» باشد، **کلاس برنامه‌نویسی** است تا بتوانی روندهای آینده را هم دنبال کنی؛ در واقع یاد گرفتی *چطور برنامه‌نویسی را یاد بگیری*.
- امروز از HTML و CSS فراتر می‌رویم و با ترکیب HTML، CSS، SQL، پایتون و جاوااسکریپت **برنامهٔ وب** (web application) خودت را می‌سازی.

## صفحهٔ ایستا و صفحهٔ پویا

- تا اینجا همهٔ HTMLها ازپیش‌نوشته و **ایستا** (static) بودند: مرورگر صفحه را بارگیری می‌کرد و تو آن را می‌دیدی. آنچه در HTML نوشته شده دقیقاً همان چیزی است که کاربر **سمت کاربر** (client-side) در مرورگرش دریافت می‌کند.
- صفحه‌های **پویا** (dynamic) یعنی پایتون و زبان‌های مشابه HTML را **در لحظه** بسازند؛ صفحه **سمت سرور** (server-side) و بر اساس ورودی یا رفتار کاربر تولید می‌شود.
- پیش‌تر برای فرستادن صفحه‌ها از `http-server` استفاده کردی. امروز سروری به کار می‌بریم که می‌تواند نشانی وب را تجزیه کند و بر اساس آن **کاری انجام دهد**.
- هفتهٔ پیش نشانی‌هایی مثل این دیدی:

```text
https://www.example.com/folder/file.html
```

- در این نشانی `file.html` یک فایل HTML درون پوشه‌ای به نام `folder` روی `example.com` است؛ سرور فقط فایل را پیدا می‌کند و می‌فرستد.

> [!TIP]
> **تألیفی: یک مقایسهٔ کوتاه**
> `http-server` مثل کتابداری است که فقط کتاب خواسته‌شده را از قفسه برمی‌دارد. Flask مثل نویسنده‌ای است که همان لحظه، با توجه به نام و سؤال تو، یک صفحهٔ تازه می‌نویسد. هر دو در پایان HTML می‌فرستند؛ فرق در این است که HTML از کجا می‌آید.

## اشتباه‌های رایج

- فکر کردن به اینکه «پویا» یعنی جاوااسکریپت. در این هفته «پویا» یعنی HTML را **سرور** می‌سازد؛ جاوااسکریپت در مرورگر اجرا می‌شود.
- انتظار اینکه `http-server` به `?name=...` واکنش نشان دهد؛ این سرور فقط فایل می‌فرستد.

## جمع‌بندی

- صفحهٔ ایستا: همان فایل HTML، سمت کاربر نمایش داده می‌شود.
- صفحهٔ پویا: HTML سمت سرور و بر اساس ورودی ساخته می‌شود.
- این هفته با Flask سروری می‌سازیم که نشانی را می‌فهمد و پاسخ مناسب می‌سازد.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w09-fa)
- بعدی: [Flask: نخستین برنامه، مسیر و تزئین‌گر](/kb/d/w09-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
