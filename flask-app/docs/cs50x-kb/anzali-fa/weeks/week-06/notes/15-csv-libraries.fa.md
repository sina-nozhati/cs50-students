---
id: w06-n15
type: note
title: فایل CSV و کتابخانه‌های شخص ثالث (CSV Files and Third-Party Libraries)
title_fa: فایل CSV و کتابخانه‌های شخص ثالث
title_en: CSV Files and Third-Party Libraries
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: CSV Files
official_anchor: csv-files
source_url: https://cs50.harvard.edu/x/2026/notes/6/#csv-files
source_refs:
- src-notes-6#csv-files
- src-notes-6#third-party-libraries
- src-transcript-6
- src-pset-6
- src-pset-6-dna#hints
- src-python-docs
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-csv-module
- w06-c-with-open
- w06-c-dictwriter
- w06-c-third-party
prev: w06-n14
next: w06-summary
order: 15
video:
  youtube_id: Rl0ludWTLxs
  start: '2:14:27'
  start_seconds: 8067
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=8067s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'Python comes with a library to handle CSV files'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# فایل CSV و کتابخانه‌های شخص ثالث

> **منبع رسمی:** بخش «CSV Files» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#csv-files). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۱۴:۲۷](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=8067s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پایتون برای فایل‌های CSV کتابخانهٔ داخلی دارد و هزاران کتابخانهٔ شخص ثالث دیگر هم با یک دستور نصب می‌شوند. DNA در Problem Set 6 فایل CSV می‌خواند؛ این یادداشت فقط **نوشتن** در CSV را از سخنرانی توضیح می‌دهد و راه‌حل DNA را نمی‌دهد.

## فایل‌های CSV

- پایتون از فایل‌های CSV به‌صورت داخلی پشتیبانی می‌کند.
- کد `phonebook.py` را این‌طور تغییر بده:

```python
import csv

file = open("phonebook.csv", "a")

name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file)
writer.writerow([name,number])

file.close()
```

- `writerow` ویرگول‌ها را خودش در فایل CSV می‌گذارد. حالت `"a"` یعنی **افزودن** (append) به انتهای فایل، نه بازنویسی آن.
- `file = open` و `file.close` در پایتون رایج‌اند، اما این کد را می‌شود بهتر کرد:

```python
# Uses `with`

import csv

# Get name and number
name = input("Name: ")
number = input("Number: ")

# Open CSV file
with open("phonebook.csv", "a") as file:

    # Print to file
    writer = csv.writer(file)
    writer.writerow([name, number])
```

- کد زیر دستور `with` تورفته است. `with` فایل را پس از پایان کار **خودکار می‌بندد**.
- به همین ترتیب می‌شود یک واژه‌نامه را در فایل CSV نوشت:

```python
import csv

name = input("Name: ")
number = input("Number: ")

with open("phonebook.csv", "a") as file:

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
```

- این کد بسیار شبیه نسخهٔ قبلی است، اما به جای `csv.writer` از `csv.DictWriter` استفاده می‌کند و ستون‌ها با `fieldnames` نام‌گذاری می‌شوند.

> [!TIP]
> **تألیفی: نوشتن در برابر خواندن**
> `csv.writer` و `csv.DictWriter` برای **نوشتن** هستند. برای **خواندن** هم دو همتا وجود دارد: `csv.reader` (هر سطر یک فهرست) و `csv.DictReader` (هر سطر یک واژه‌نامه با کلیدهایی از سطر سرستون). صورت مسئلهٔ DNA نمونه‌های کلی `DictReader` را خودش آورده است؛ آنجا را بخوان. یادت باشد هر مقداری که از CSV خوانده می‌شود **رشته** است (استنتاجی، بر پایهٔ مستندات پایتون).

## کتابخانه‌های شخص ثالث

- یکی از برتری‌های پایتون جامعهٔ بزرگ کاربرانش و به همان اندازه شمار زیاد کتابخانه‌های شخص ثالث است.
- اگر پایتون روی رایانه‌ات نصب باشد، می‌توانی کتابخانهٔ CS50 را با `pip install cs50` روی رایانهٔ خودت نصب کنی.
- از میان کتابخانه‌های دیگر، David استفاده از `cowsay` و `qrcode` را نشان داد.

> [!NOTE]
> **از سخنرانی: نصب با pip**
> David یک برنامهٔ کوتاه با کتابخانهٔ `cowsay` نوشت تا گاوی روی صفحه «This is CS50» بگوید، و یک مولد کد QR با کتابخانهٔ `qrcode` ساخت. کد کامل این دو نمونه در درس‌نامه نیامده؛ برای دیدنشان به [ویدئوی سخنرانی](https://www.youtube.com/watch?v=Rl0ludWTLxs) پیوند داده شده است.

## اشتباه‌های رایج

- باز کردن فایل با `"w"` وقتی می‌خواهی اضافه کنی؛ `"w"` محتوای قبلی را پاک می‌کند.
- فراموش کردن `file.close()` در شکل بدون `with`.
- برداشت اینکه `DictWriter` بدون `fieldnames` کار می‌کند؛ `fieldnames` الزامی است.

## جمع‌بندی

- `import csv`؛ `csv.writer` و `writerow([...])`؛ `csv.DictWriter` و `writerow({...})`.
- `with open(...) as file:` فایل را خودکار می‌بندد.
- `pip install` کتابخانه‌های شخص ثالث را نصب می‌کند.

## پیوندها

- قبلی: [آرگومان خط فرمان و وضعیت خروج](/kb/d/w06-n14)
- بعدی: [خلاصهٔ هفته](/kb/d/w06-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
