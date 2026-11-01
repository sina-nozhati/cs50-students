---
id: w09-n05
type: note
title: 'قالب مادر: layout.html، block و extends (Templates)'
title_fa: 'قالب مادر: layout.html، block و extends'
title_en: Templates
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Templates
official_anchor: templates
source_url: https://cs50.harvard.edu/x/2026/notes/9/#templates
source_refs:
- src-notes-9#templates
- src-transcript-9
- src-flask-box-9
- src-anzali-authored-9
- src-srt-9
concept_ids:
- w09-c-layout
- w09-c-block
- w09-c-extends
prev: w09-n04
next: w09-n06
order: 5
video:
  youtube_id: am7POvSZ4GE
  start: '37:06'
  start_seconds: 2226
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=2226s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase 'inside still my templates directory and by convention'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# قالب مادر: layout.html، block و extends

> **منبع رسمی:** بخش «Templates» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#templates). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۷:۰۶ تا حدود ۴۴:۰۳](https://www.youtube.com/watch?v=am7POvSZ4GE&t=2226s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`index.html` و `greet.html` بیشتر کدشان یکی است: DOCTYPE، head، title... اگر بخواهی عنوان را عوض کنی باید هر دو را ویرایش کنی. **قالب مادر** (layout) این تکرار را حذف می‌کند.

## layout.html و block

- قالب تازه‌ای به نام `layout.html` بساز:

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <title>hello</title>
    </head>

    <body>
        {% block body %}{% endblock %}
    </body>

</html>
```

- `{% block body %}{% endblock %}` اجازه می‌دهد کد فایل‌های HTML دیگر در این نقطه قرار بگیرد.

## extends

- سپس `index.html` را این‌طور تغییر بده:

```jinja
{% extends "layout.html" %}

{% block body %}

    <form action="/greet" method="get">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Greet</button>
    </form>

{% endblock %}
```

- خط `{% extends "layout.html" %}` به سرور می‌گوید چیدمان این صفحه را از کجا بیاورد. سپس `{% block body %}{% endblock %}` مشخص می‌کند چه کدی درون `layout.html` نشانده شود.
- در پایان `greet.html` را هم این‌طور تغییر بده:

```jinja
{% extends "layout.html" %}

{% block body %}
    hello, {{ name }}
{% endblock %}
```

- این کد کوتاه‌تر و جمع‌وجورتر است.

> [!NOTE]
> **از سخنرانی: Jinja عجیب است، اما کوچک**
> دیوید یادآوری می‌کند که `{% ... %}` و `{{ ... }}` نحو **Jinja** است، نه HTML و نه پایتون؛ زبانی کوچک که Flask با آن قالب‌ها را پر می‌کند. `{% %}` برای دستورها (block، extends، if، for) و `{{ }}` برای نوشتن یک مقدار است.

> [!TIP]
> **تألیفی، اجراشده روی جعبهٔ ساخت: نام بلوک باید یکی باشد**
> اگر در `layout.html` بنویسی `{% block body %}` و در صفحهٔ فرزند `{% block content %}`، Jinja خطا نمی‌دهد؛ فقط محتوای فرزند هیچ‌جا نشان داده نمی‌شود، چون بلوکی به نام `content` در قالب مادر نیست. در سخنرانی هم دیوید یک‌بار در نوشتن نام بلوک اشتباه می‌کند (دو کلمه را جابه‌جا می‌نویسد) و می‌گوید «It's supposed to be block body».

## اشتباه‌های رایج

- گذاشتن محتوا بیرون از `{% block body %}` در صفحهٔ فرزند؛ آن محتوا دیده نمی‌شود.
- فراموش کردن `{% endblock %}`؛ Jinja خطای نحوی می‌دهد.
- نوشتن `{% extends layout.html %}` بدون نقل‌قول.

## جمع‌بندی

- `layout.html` بخش مشترک صفحه‌هاست و با `{% block name %}{% endblock %}` جای خالی دارد.
- هر صفحهٔ فرزند با `{% extends "layout.html" %}` شروع می‌شود و همان بلوک را پر می‌کند.

## پیوندها

- قبلی: [فرم‌ها و مسیر دوم /greet](/kb/d/w09-n04)
- بعدی: [GET و POST، request.form و request.method](/kb/d/w09-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
