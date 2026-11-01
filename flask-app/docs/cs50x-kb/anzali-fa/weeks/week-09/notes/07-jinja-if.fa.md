---
id: w09-n07
type: note
title: 'مقدار پیش‌فرض در قالب: if/else در Jinja (Request Methods: Defaults in Templates)'
title_fa: 'مقدار پیش‌فرض در قالب: if/else در Jinja'
title_en: 'Request Methods: Defaults in Templates'
week: 9
parent: w09-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Request Methods
official_anchor: request-methods
source_url: https://cs50.harvard.edu/x/2026/notes/9/#request-methods
source_refs:
- src-notes-9#request-methods
- src-src9-index
- src-flask-box-9
- src-anzali-authored-9
- src-anzali-inference-9
- src-srt-9
concept_ids:
- w09-c-get-default-missing-key
- w09-c-jinja-if
prev: w09-n06
next: w09-n08
order: 7
video:
  youtube_id: am7POvSZ4GE
  start: '52:14'
  start_seconds: 3134
  url: https://www.youtube.com/watch?v=am7POvSZ4GE&t=3134s
  origin: inference
  basis: first lecture9.srt cue (after the previous note's cue) containing the phrase "I've been passing in this default value of world"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python, Jinja/HTML and other code copied exactly from the official notes (fence language python, jinja, html or text); results marked «اجراشده روی جعبهٔ ساخت» were run with the Flask test client (Flask 3.1.3, Flask-Session 0.8.0, cs50 9.5.0, Jinja2 3.1.6) against authored SQLite fixtures, or with Node, on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مقدار پیش‌فرض در قالب: if/else در Jinja

> **منبع رسمی:** بخش «Request Methods» از [درس‌نامهٔ هفتهٔ ۹ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/9/#request-methods). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۲:۱۴ تا حدود ۵۵:۲۹](https://www.youtube.com/watch?v=am7POvSZ4GE&t=3134s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برنامهٔ یادداشت قبل یک اشکال دارد: اگر کاربر چیزی ننویسد و دکمه را بزند، فقط `hello,` می‌بیند. باید بفهمی چرا مقدار پیش‌فرض `world` کار نکرد و چطور می‌شود منطق پیش‌فرض را به قالب برد.

## اشکال: hello, بدون نام

- با پیاده‌سازی تازه، وقتی کسی در فرم نامی ننویسد، `Hello,` بدون نام نشان داده می‌شود (در کد خروجی با حرف کوچک `hello,` است؛ d157).

> [!IMPORTANT]
> **اجراشده روی جعبهٔ ساخت: چرا "world" نیامد؟**
> فرم حتی وقتی خالی است فیلد `name` را می‌فرستد، با مقدار رشتهٔ خالی `""`. `request.form.get("name", "world")` فقط وقتی `world` برمی‌گرداند که کلید `name` **اصلاً نباشد**. روی جعبهٔ ساخت: POST با `name=""` خروجی `hello,` داد و POST بدون فیلد `name` خروجی `hello, world`.

## انتقال پیش‌فرض به قالب

- `app.py` را این‌طور ویرایش کن:

```python
# Moves default value to template

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))
    return render_template("index.html")
```

- عبارت `name=request.form.get("name")` تغییر کرده است (d158).
- در پایان `greet.html` را این‌طور تغییر بده:

```jinja
{% extends "layout.html" %}

{% block body %}

    hello,
    {% if name %}
        {{ name }}
    {% else %}
        world
    {% endif %}

{% endblock %}
```

- `hello, {{ name }}` تغییر کرده تا وقتی نامی نیست، خروجی پیش‌فرض نشان داده شود.
- چون فایل‌های زیادی را تغییر دادی، می‌توانی کد نهایی‌ات را با [کد نهایی ما](https://cdn.cs50.net/2025/fall/lectures/9/src9/hello10/) مقایسه کنی.

> [!TIP]
> **تألیفی، اجراشده روی جعبهٔ ساخت: چرا این بار درست شد؟**
> در Jinja، مانند پایتون، رشتهٔ خالی و `None` هر دو «نادرست» به حساب می‌آیند. پس `{% if name %}` هم برای فیلد خالی و هم برای فیلد نبوده به شاخهٔ `else` می‌رود. روی جعبهٔ ساخت POST با `name=""` این بار `hello,` و سپس `world` را نوشت (هر کدام در سطر خودش، چون قالب چندسطری است).

## اشتباه‌های رایج

- اعتماد به پیش‌فرض `get` برای فیلدهای فرم.
- فراموش کردن `{% endif %}`.
- نوشتن `{% if name == "" %}`؛ برای `None` کار نمی‌کند (استنتاجی).

## جمع‌بندی

- فیلد خالی فرم `""` است و پیش‌فرض `get` را فعال نمی‌کند.
- `{% if name %} ... {% else %} ... {% endif %}` منطق نمایش را به قالب می‌برد.

## پیوندها

- قبلی: [GET و POST، request.form و request.method](/kb/d/w09-n06)
- بعدی: [Frosh IMs: منوی select، حلقهٔ for و اعتبارسنجی سمت سرور](/kb/d/w09-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-09/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
