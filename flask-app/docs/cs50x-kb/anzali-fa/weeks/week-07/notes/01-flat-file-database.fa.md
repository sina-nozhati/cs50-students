---
id: w07-n01
type: note
title: 'پایگاه دادهٔ تخت: CSV و شمارش با پایتون (Welcome! and Flat-File Database)'
title_fa: 'پایگاه دادهٔ تخت: CSV و شمارش با پایتون'
title_en: Welcome! and Flat-File Database
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Flat-File Database
official_anchor: flat-file-database
source_url: https://cs50.harvard.edu/x/2026/notes/7/#flat-file-database
source_refs:
- src-notes-7#flat-file-database
- src-notes-7#welcome
- src-transcript-7
- src-python-docs
- src-anzali-authored-7
- src-anzali-inference-7
- src-srt-7
concept_ids:
- w07-c-flat-file-db
- w07-c-csv-format
- w07-c-csv-quoting
- w07-c-csv-reader-header
- w07-c-dictreader-columns
- w07-c-count-with-dict
- w07-c-keyerror-try
- w07-c-sorted-key-reverse
prev: w07-fa
next: w07-n02
order: 1
video:
  youtube_id: oqRU2So6Z2Y
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# پایگاه دادهٔ تخت: CSV و شمارش با پایتون

> **منبع رسمی:** بخش «Flat-File Database» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#flat-file-database). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۲۴:۱۲](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا داده‌ها یا در متغیرهای برنامه بودند یا در فایل‌هایی که خودت می‌خواندی. این هفته سراغ **داده** به‌عنوان موضوع اصلی می‌رویم: اول با یک فایل CSV و پایتون، و بعد با پایگاه داده و زبان SQL. این یادداشت نشان می‌دهد شمارش و مرتب‌سازی داده با پایتون چقدر کد می‌خواهد تا در یادداشت‌های بعدی ببینی SQL همین کار را چطور در یک خط انجام می‌دهد.

## خوش آمدی و پایگاه دادهٔ تخت

- در هفتهٔ گذشته با پایتون آشنا شدی؛ زبانی سطح بالا که از همان بلوک‌های سازندهٔ C استفاده می‌کند. هدف یاد گرفتن «فقط یک زبان دیگر» نبود: بعضی ابزارها برای بعضی کارها بهترند و برای بعضی کارها نه.
- این هفته نحو بیشتری از پایتون می‌بینی، آن را با **داده** ترکیب می‌کنی و در پایان با **SQL** (زبان پرس‌وجوی ساخت‌یافته) آشنا می‌شوی؛ زبانی مخصوص یک حوزه برای کار با داده و تغییر آن.
- یکی از هدف‌های کل درس این است که برنامه‌نویسی را به‌طور کلی یاد بگیری، نه فقط زبان‌های همین درس را.
- داده را معمولاً می‌شود با الگوی **ستون‌ها و سطرها** توصیف کرد. صفحه‌گسترده‌هایی مثل Microsoft Excel و Google Sheets را می‌شود به فایل `csv` (مقدارهای جداشده با ویرگول) خروجی گرفت.
- فایل `csv` «تخت» است: همهٔ داده در یک جدول و در یک فایل متنی ذخیره شده است. به این شکل از داده **پایگاه دادهٔ تخت** (flat-file database) می‌گوییم. داده سطر به سطر ذخیره می‌شود و ستون‌ها با ویرگول (یا نویسهٔ دیگری) از هم جدا می‌شوند.
- پایتون پشتیبانی داخلی از فایل‌های `csv` دارد. درس‌نامه از تو می‌خواهد فایل `favorites.csv` را از پیوند رسمی بگیری و در cs50.dev بارگذاری کنی. سطر اول خاص است: نام ستون‌ها را تعریف می‌کند. بعد هر رکورد در یک سطر می‌آید.
- در ترمینال `code favorites.py` را اجرا کن و این کد را بنویس:

```python
# Prints all favorites in CSV using csv.reader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(row[1])
```

- `csv.reader` فایل باز را می‌گیرد و هر سطر را به شکل یک فهرست برمی‌گرداند. `next(reader)` سطر سرستون را رد می‌کند و `row[1]` ستون دوم (زبان برنامه‌نویسی) را چاپ می‌کند.
- می‌توانی کد را این‌طور بهتر کنی:

```python
# Stores favorite in a variable

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        favorite = row[1]
        print(favorite)
```

- یکی از ضعف‌های این روش این است که اعتماد کرده‌ایم `row[1]` همیشه همان علاقه‌مندی است. اگر ستون‌ها جابه‌جا شده باشند چه؟
- این مشکل را می‌شود حل کرد. پایتون اجازه می‌دهد سطر را با **نام ستون** نمایه کنی. کد را این‌طور تغییر بده:

```python
# Prints all favorites in CSV using csv.DictReader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        favorite = row["language"]
        print(favorite)
```

- این کد را می‌شود ساده‌تر هم نوشت:

```python
# Prints all favorites in CSV using csv.DictReader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(row["language"])
```

> [!NOTE]
> **یادداشت**
> درس‌نامه می‌گوید پایتون اجازه می‌دهد «با کلیدهای یک list» نمایه کنی. در واقع `csv.DictReader` هر سطر را به شکل یک **dict** برمی‌گرداند و `row["language"]` کلید آن dict است؛ فهرست‌ها فقط با عدد نمایه می‌شوند. سخنرانی هم می‌گوید DictReader سطر سرستون را خودش مصرف می‌کند و برای همین `next` لازم نیست (d117).

- برای شمردن تعداد هر زبان در فایل می‌توانیم این‌طور عمل کنیم:

```python
# Counts favorites using variables

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    scratch, c, python = 0, 0, 0

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

# Print counts
print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")
```

- پایتون اجازه می‌دهد برای شمارش `counts` هر زبان از یک واژه‌نامه استفاده کنیم. این بهبود را ببین:

```python
# Counts favorites using dictionary

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
```

- می‌توانیم برای استثناهای احتمالی از `try` و `except` هم استفاده کنیم:

```python
# Uses try/except instead

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        try:
            counts[favorite] += 1
        except KeyError:
            counts[favorite] = 1

# Print counts
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
```

- پایتون مرتب‌سازی `counts` را هم ممکن می‌کند. کد را این‌طور بهتر کن:

```python
# Sorts favorites by key

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")
```

- اگر پارامترهای تابع `sorted` را در مستندات پایتون نگاه کنی، پارامترهای داخلی زیادی می‌بینی. می‌توانی از بعضی از آن‌ها این‌طور استفاده کنی:

```python
# Sorts favorites by value using .get

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
```

- دربارهٔ [sorted](https://docs.python.org/3/howto/sorting.html) در [مستندات پایتون](https://docs.python.org/3/howto/sorting.html) بیشتر بخوان.

> [!TIP]
> **تألیفی: sorted(counts) روی کلیدها کار می‌کند**
> `sorted(counts)` کلیدهای واژه‌نامه را به ترتیب الفبا برمی‌گرداند، نه مقدارها را. `key=counts.get` می‌گوید برای مقایسه به جای خود کلید، مقدار آن (`counts.get(favorite)`) را به کار ببر؛ `reverse=True` ترتیب را نزولی می‌کند. اگر دو زبان تعداد برابر داشته باشند، `sorted` پایدار است و آن‌ها را به همان ترتیبی که در واژه‌نامه آمده‌اند نگه می‌دارد (استنتاجی، بر پایهٔ مستندات پایتون).

> [!TIP]
> **تألیفی: مقدار ویرگول‌دار در CSV**
> پاسخ‌هایی مثل `Hello, World` خودشان ویرگول دارند. در فایل CSV چنین مقداری داخل نقل‌قول دوتایی نوشته می‌شود (`"Hello, World"`) و ماژول `csv` آن را یک ستون می‌خواند، نه دو ستون. برای همین بهتر است فایل CSV را با ماژول `csv` بخوانی، نه با `split(",")`.

## اشتباه‌های رایج

- فراموش کردن `next(reader)` با `csv.reader`؛ سطر سرستون هم مثل یک پاسخ چاپ یا شمرده می‌شود.
- اضافه کردن `next(reader)` به کد DictReader؛ این کار اولین پاسخ واقعی را دور می‌ریزد، چون DictReader سرستون را خودش خوانده است.
- نوشتن `counts[favorite] += 1` بدون بررسی یا `try`؛ برای کلیدی که هنوز نیست خطای `KeyError` می‌دهد.
- انتظار اینکه `sorted(counts)` بر اساس تعداد مرتب کند؛ بدون `key=counts.get` بر اساس نام کلید مرتب می‌کند.

## جمع‌بندی

- فایل CSV یک پایگاه دادهٔ تخت است: یک جدول در یک فایل متنی.
- `csv.reader` سطر را به شکل فهرست می‌دهد و `csv.DictReader` به شکل dict با نام ستون‌ها.
- شمارش با dict، و مرتب‌سازی با `sorted(..., key=counts.get, reverse=True)`.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w07-fa)
- بعدی: [پایگاه دادهٔ رابطه‌ای و sqlite3](/kb/d/w07-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
