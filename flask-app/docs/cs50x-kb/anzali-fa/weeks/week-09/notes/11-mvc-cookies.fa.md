---
id: w09-n11
type: note
title: 'MVC، کوکی و جلسه (session) (Cookies and Session: MVC and Cookies)'
title_fa: MVC، کوکی و جلسه (session)
title_en: 'Cookies and Session: MVC and Cookies'
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Cookies and Session
official_anchor: cookies-and-session
source_url: https://cs50.harvard.edu/x/2026/notes/9/#cookies-and-session
source_refs:
- src-notes-9#cookies-and-session
- src-transcript-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-mvc
- w09-c-cookie
- w09-c-set-cookie-header
- w09-c-session
prev: w09-n10
next: w09-n12
order: 11
video:
  youtube_id: am7POvSZ4GE
  start: '1:55:50'
  start_seconds: 6950
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=6950s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase "So the views that we're referring to here"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# MVC، کوکی و جلسه (session)

> **منبع رسمی:** بخش «Cookies and Session» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#cookies-and-session). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۵:۵۰ تا حدود ۲:۰۲:۵۱](https://www.youtube.com/watch?v=am7POvSZ4GE&t=6950s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

نسخهٔ پایگاه‌داده‌ای froshims برای یک مدیر مفید است، اما روی یک سرور عمومی امن نیست: هر کسی می‌تواند دکمهٔ Deregister دیگران را بزند. برای اینکه هر کاربر فقط به دادهٔ خودش دسترسی داشته باشد، سرور باید **بداند چه کسی** درخواست می‌دهد. **کوکی** و **جلسه** (session) همین کار را می‌کنند.

## MVC

- `app.py` **کنترل‌گر** (controller) به حساب می‌آید. **نما** (view) آن چیزی است که کاربر می‌بیند. **مدل** (model) شیوهٔ ذخیره و دست‌کاری داده است. این سه را با هم **MVC** (model, view, controller) می‌نامند.

> [!TIP]
> **تألیفی: MVC در froshims**
> مدل: `froshims.db` و پرس‌وجوهای SQL. نما: فایل‌های پوشهٔ `templates`. کنترل‌گر: تابع‌های مسیر در `app.py` که ورودی را می‌گیرند، مدل را به‌روز می‌کنند و نما را برمی‌گردانند.

## چرا ورود لازم است

- پیاده‌سازی قبلی froshims از دید اداری مفید است، چون یک مدیر می‌تواند افراد را به پایگاه داده اضافه یا از آن حذف کند؛ اما می‌توان تصور کرد که اجرای این کد روی سرور عمومی امن نیست.
- مثلاً افراد بداندیش می‌توانند با زدن دکمهٔ deregister به جای کاربران دیگر تصمیم بگیرند و پاسخ ثبت‌شدهٔ آن‌ها را از سرور پاک کنند.
- خدمات وبی مثل Google با اطلاعات ورود مطمئن می‌شوند هر کاربر فقط به دادهٔ درست دسترسی دارد.

## کوکی و جلسه

- این کار را با **کوکی‌ها** (cookies) می‌توان انجام داد. کوکی تکه‌دادهٔ کوچکی است که در مرورگرت ذخیره می‌شود تا مرورگر با سرور ارتباط بگیرد و عملاً بگوید: «من کاربر مجازی هستم که پیش‌تر وارد شده.» به این مجوزدهی از راه کوکی **جلسه** (session) می‌گویند.
- کوکی‌ها می‌توانند این‌طور فرستاده شوند:

```text
GET / HTTP/2
Host: accounts.google.com
Cookie: session=value
```

- اینجا یک شناسهٔ `session` با یک `value` مشخص نگه داشته شده که نمایندهٔ آن جلسه است.

> [!NOTE]
> **از سخنرانی: مُهر روی دست**
> دیوید کوکی را با مُهری مقایسه می‌کند که در ورودی شهربازی یا باشگاه روی دستت می‌زنند: یک بار بلیت نشان می‌دهی و از آن پس فقط مُهر را نشان می‌دهی. سرور با سرآیند **Set-Cookie** می‌گوید «این را نگه دار» و مرورگر در درخواست‌های بعدی با سرآیند **Cookie** همان را پس می‌فرستد. او تأکید می‌کند ذخیرهٔ نام کاربری و گذرواژه در کوکی کار بدی است؛ سرور معمولاً فقط یک مقدار تصادفی بزرگ می‌گذارد.

## اشتباه‌های رایج

- یکی دانستن کوکی و جلسه. کوکی سازوکار HTTP است؛ جلسه دادهٔ کاربر است که سرور با کمک شناسهٔ درون کوکی پیدا می‌کند.
- نگه داشتن دادهٔ حساس در خود کوکی.
- فکر کردن به اینکه پنهان کردن دکمه کافی است؛ کنترل دسترسی باید سمت سرور باشد.

## جمع‌بندی

- MVC: مدل (داده)، نما (قالب‌ها)، کنترل‌گر (`app.py`).
- کوکی جفت کلید-مقداری است که سرور می‌گذارد و مرورگر دوباره می‌فرستد.
- جلسه با همین کوکی کاربر را بین درخواست‌ها به یاد می‌آورد.

## پیوندها

- قبلی: [Flask و SQL: ذخیرهٔ ماندگار و getlist](/kb/d/w09-n10)
- بعدی: [ورود و خروج با session](/kb/d/w09-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
