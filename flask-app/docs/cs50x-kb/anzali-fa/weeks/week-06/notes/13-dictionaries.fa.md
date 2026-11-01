---
id: w06-n13
type: note
title: جست‌وجو، in و دیکشنری (Searching and Dictionaries)
title_fa: جست‌وجو، in و دیکشنری
title_en: Searching and Dictionaries
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Searching and Dictionaries
official_anchor: searching-and-dictionaries
source_url: https://cs50.harvard.edu/x/2026/notes/6/#searching-and-dictionaries
source_refs:
- src-notes-6#searching-and-dictionaries
- src-short-python
- src-python-docs
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-linear-search-py
- w06-c-for-else
- w06-c-dict
- w06-c-list-of-dicts
- w06-c-dict-lookup
prev: w06-n12
next: w06-n14
order: 13
video:
  youtube_id: Rl0ludWTLxs
  start: '1:54:45'
  start_seconds: 6885
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=6885s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'improved version of our phone book'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جست‌وجو، in و دیکشنری

> **منبع رسمی:** بخش «Searching and Dictionaries» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#searching-and-dictionaries). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۴:۴۵ تا حدود ۲:۰۸:۵۱](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=6885s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در هفته‌های ۳ و ۵ جست‌وجوی خطی، جدول درهم‌سازی و واژه‌نامه را از صفر ساختی. پایتون عملگر `in` و نوع `dict` را آماده دارد. این یادداشت نشان می‌دهد کدام انتخاب برای دفترچهٔ تلفن مناسب‌تر است و هزینهٔ هرکدام چیست.

## جست‌وجو و واژه‌نامه‌ها

- می‌توانیم درون یک ساختمان داده هم جست‌وجو کنیم. برنامه‌ای به نام `phonebook.py` را در نظر بگیر:

```python
# Implements linear search for names using loop

# A list of names
names = ["Kelly", "David", "John"]

# Ask for name
name = input("Name: ")

# Search for name
for n in names:
    if name == n:
        print("Found")
        break
else:
    print("Not found")
```

- این کد برای هر نام **جست‌وجوی خطی** انجام می‌دهد. به `else` حلقهٔ `for` دقت کن: این `else` فقط وقتی اجرا می‌شود که حلقه **بدون** `break` تمام شود.
- اما لازم نیست روی فهرست پیمایش کنیم. در پایتون جست‌وجوی خطی را این‌طور می‌شود انجام داد:

```python
# Implements linear search for names using `in`

# A list of names
names = ["Kelly", "David", "John"]

# Ask for name
name = input("Name: ")

# Search for name
if name in names:
    print("Found")
else:
    print("Not found")
```

- اینجا `in` جست‌وجوی خطی را انجام می‌دهد.
- با این حال، این کد را می‌شود بهتر کرد.
- به یاد داری که **واژه‌نامه** یا `dict` مجموعه‌ای از جفت‌های **کلید** و **مقدار** است. می‌توانی واژه‌نامه را در پایتون این‌طور پیاده کنی:

```python
# Implements a phone book as a list of dictionaries, without a variable

from cs50 import get_string

people = [
    {"name": "Kelly", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]

# Search for name
name = get_string("Name: ")
for person in people:
    if person["name"] == name:
        print(f"Found {person['number']}")
        break
else:
    print("Not found")
```

- هر عضو این فهرست، واژه‌نامه‌ای با دو کلید `name` و `number` است.
- بهتر از این، در واقع به هر دو `name` و `number` نیاز نداریم. می‌شود کد را این‌طور ساده کرد:

```python
# Implements a phone book using a dictionary

from cs50 import get_string

people = {
    "Kelly": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

# Search for name
name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")
else:
    print("Not found")
```

- واژه‌نامه با آکولاد ساخته شده است. سپس `if name in people` بررسی می‌کند آیا `name` در واژه‌نامهٔ `people` هست یا نه. در دستور `print` هم می‌توانیم با مقدار `name` در واژه‌نامهٔ `people` نمایه‌گذاری کنیم (`people[name]`).
- به همین ترتیب می‌شود فهرستی از واژه‌نامه‌ها ساخت:

```python
# Implements a phone book as a list of dictionaries

people = [
    {"name": "Kelly", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]

# Search for name
name = input("Name: ")
for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}")
        break
else:
    print("Not found")
```

- `people` فهرستی از واژه‌نامه‌هاست که با ویرگول از هم جدا شده‌اند.
- دربارهٔ واژه‌نامه‌ها در [مستندات پایتون](https://docs.python.org/3/library/stdtypes.html#dict) بیشتر بخوان.

> [!NOTE]
> **یادداشت**
> درس‌نامه می‌گوید پایتون تمام تلاشش را کرده تا با جست‌وجوهای داخلی‌اش به **زمان ثابت** برسد. این برای `in` روی `dict` و `set` (که با جدول درهم‌سازی پیاده شده‌اند) به‌طور میانگین درست است، اما `in` روی `list`، مثل `phonebook1.py`، همچنان **جست‌وجوی خطی** با زمان O(n) است؛ خود درس‌نامه هم آن را «جست‌وجوی خطی» نامیده است (d105).

> [!TIP]
> **تألیفی: in روی dict کلیدها را می‌گردد**
> `"Kelly" in people` در `phonebook4.py` درست است، اما `"+1-617-495-1000" in people` نادرست است، چون `in` روی واژه‌نامه فقط **کلیدها** را بررسی می‌کند. برای مقدارها باید `people.values()` را بگردی. `people["Brian"]` برای کلیدی که نیست خطای `KeyError` می‌دهد؛ برای همین برنامه پیش از نمایه‌گذاری با `in` بررسی می‌کند (استنتاجی، اجراشده روی جعبهٔ ساخت).

> [!NOTE]
> **از ویدئوی کوتاه: واژه‌نامه و جدول درهم‌سازی**
> Doug Lloyd در ویدئوی کوتاه می‌گوید واژه‌نامه از نظر روحیه به جدول درهم‌سازی نزدیک است و عضوها را با کلید (مثلاً نام پیتزا) نمایه می‌کند، نه با عدد.

## اشتباه‌های رایج

- فرض اینکه `in` روی هر ساختمان داده‌ای زمان ثابت است.
- نوشتن `print("Not found")` درون حلقه به جای `else` حلقه؛ برای هر نام ناهمخوان یک بار چاپ می‌شود.
- استفاده از نقل‌قول دوتایی درون f-stringی که خودش با نقل‌قول دوتایی ساخته شده (مثل `f"{person["number"]}"`)؛ این کار پیش از پایتون ۳٫۱۲ خطای نحوی می‌دهد. `phonebook2.py` درون f-string از `'number'` با نقل‌قول تکی استفاده می‌کند که در همهٔ نسخه‌های پایتون ۳ کار می‌کند (استنتاجی، بر پایهٔ مستندات پایتون).

## جمع‌بندی

- `in` روی `list` جست‌وجوی خطی است؛ روی `dict` و `set` به‌طور میانگین زمان ثابت.
- `dict` جفت‌های کلید-مقدار است؛ `people[key]` مقدار را می‌دهد.
- `for ... else`: بخش `else` فقط بدون `break` اجرا می‌شود.

## پیوندها

- قبلی: [فهرست‌ها (list)، sum و len](/kb/d/w06-n12)
- بعدی: [آرگومان خط فرمان و وضعیت خروج](/kb/d/w06-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
