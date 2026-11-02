---
id: w07-n10
type: note
title: SQL در پایتون با کتابخانهٔ CS50 (Using SQL in Python)
title_fa: SQL در پایتون با کتابخانهٔ CS50
title_en: Using SQL in Python
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Using SQL in Python
official_anchor: using-sql-in-python
source_url: https://cs50.harvard.edu/x/2026/notes/7/#using-sql-in-python
source_refs:
- src-notes-7#using-sql-in-python
- src-transcript-7
- src-cs50-sql-docs
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-cs50-sql
- w07-c-execute-returns-rows
- w07-c-placeholder-qmark
prev: w07-n09
next: w07-n11
order: 10
video:
  youtube_id: oqRU2So6Z2Y
  start: '1:46:30'
  start_seconds: 6390
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=6390s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'version of the CS 50 library'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# SQL در پایتون با کتابخانهٔ CS50

> **منبع رسمی:** بخش «Using SQL in Python» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#using-sql-in-python). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۶:۳۰ تا حدود ۱:۵۹:۲۲](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=6390s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`sqlite3` برای کاوش داده عالی است، اما برنامه‌های واقعی (مثل وب‌سایت هفته‌های ۹ و پروژهٔ نهایی) از درون کد با پایگاه داده حرف می‌زنند. اینجا پایتون و SQL را کنار هم می‌گذاری و با جای‌نگهدار `?` آشنا می‌شوی که در یادداشت آخر دلیل امنیتی‌اش را می‌بینی.

## استفاده از SQL در پایتون

- برای کار با SQL در این درس می‌توانی از کتابخانهٔ CS50 در کدت این‌طور استفاده کنی:

```python
from cs50 import SQL
```

- مثل استفاده‌های قبلی از کتابخانهٔ CS50، این کتابخانه مرحله‌های پیچیدهٔ کار با SQL درون کد پایتون را برایت آسان می‌کند.
- دربارهٔ امکانات SQL کتابخانهٔ CS50 در [مستندات](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL) بیشتر بخوان.
- با این دانش تازه، حالا می‌توانیم پایتون را همراه SQL به کار ببریم.
- کد `favorites.py` را این‌طور تغییر بده:

```python
# Searches database for popularity of a problem

from cs50 import SQL

# Open database
db = SQL("sqlite:///favorites.db")

# Prompt user for favorite
favorite = input("Favorite: ")

# Search for title
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

# Get first (and only) row
row = rows[0]

# Print popularity
print(row["n"])
```

- دقت کن که `db = SQL("sqlite:///favorites.db")` محل فایل پایگاه داده را به پایتون می‌دهد. بعد، خطی که با `rows` شروع می‌شود فرمان SQL را با `db.execute` اجرا می‌کند. این فرمان متن درون نقل‌قول را به تابع `db.execute` می‌دهد و با همین نحو می‌شود هر فرمان SQL را اجرا کرد. همچنین دقت کن که `rows` به شکل **فهرستی از واژه‌نامه‌ها** برگردانده می‌شود. در این مثال فقط یک نتیجه، یعنی یک سطر، به شکل یک واژه‌نامه در فهرست `rows` برمی‌گردد. کد را می‌توانی از پیوند رسمی درس‌نامه دانلود کنی.

> [!NOTE]
> **یادداشت**
> توضیح `# Search for title` در کد رسمی باقی‌ماندهٔ نسخهٔ قدیمی‌تر برنامه است؛ پرس‌وجو در واقع ستون `problem` را می‌گردد (d128). کد بدون تغییر نقل شده است.

> [!TIP]
> **تألیفی: اجرای همین برنامه روی پایگاه دادهٔ نمونه**
> اگر `fixtures/favorites.sql` را به `favorites.db` تبدیل کنی (`sqlite3 favorites.db < favorites.sql`) و برنامه را اجرا کنی، با ورودی `Mario` عدد `2` چاپ می‌شود و با ورودی `Hello, It's Me` عدد `1`، هرچند ورودی نقل‌قول تکی دارد (اجراشده روی جعبهٔ ساخت با کتابخانهٔ cs50 نسخهٔ 9.5.0). `AS n` به ستون نتیجه نام `n` می‌دهد تا بشود با `row["n"]` به آن رسید؛ بدون `AS`، کلید واژه‌نامه خود متن `COUNT(*)` می‌شد.

> [!TIP]
> **تألیفی: خروجی db.execute برای فرمان‌های دیگر**
> طبق مستندات کتابخانهٔ CS50، `db.execute` برای `SELECT` فهرستی از واژه‌نامه‌ها برمی‌گرداند، برای `INSERT` شناسهٔ (کلید اصلی) سطر تازه، و برای `UPDATE` و `DELETE` تعداد سطرهایی که تغییر کرده‌اند. هر `?` در رشتهٔ SQL به ترتیب با آرگومان‌های بعدی `db.execute` پر می‌شود.

> [!NOTE]
> **از سخنرانی**
> پیش از نسخهٔ `?`، دیوید همین برنامه را یک بار با f-string می‌نویسد و ورودی کاربر را مستقیم درون متن SQL می‌گذارد. برنامه برای `hello world` کار می‌کند، اما او می‌گوید این «هرگز» راه درست نوشتن کد SQL در پایتون نیست، چون ورودی‌ای مثل `Hello, It's Me` نقل‌قول‌ها را به هم می‌ریزد. یادداشت «حمله‌های تزریق SQL» این خطر را کامل‌تر نشان می‌دهد.

## اشتباه‌های رایج

- نوشتن `SQL("favorites.db")` بدون پیشوند `sqlite:///`.
- انتظار یک عدد از `db.execute("SELECT COUNT(*) ...")`؛ خروجی فهرستی از واژه‌نامه‌هاست و عدد در `rows[0]["n"]` است.
- ساختن متن SQL با f-string یا `+` به جای `?`.

## جمع‌بندی

- `from cs50 import SQL` و `db = SQL("sqlite:///file.db")` پایگاه داده را باز می‌کنند.
- `db.execute(sql, args...)` پرس‌وجو را اجرا می‌کند؛ `SELECT` فهرستی از واژه‌نامه‌ها برمی‌گرداند.
- ورودی کاربر را با `?` به پرس‌وجو بده، نه با f-string.

## پیوندها

- قبلی: [نمایه (index) و B-tree](/kb/d/w07-n09)
- بعدی: [شرایط مسابقه و تراکنش](/kb/d/w07-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
