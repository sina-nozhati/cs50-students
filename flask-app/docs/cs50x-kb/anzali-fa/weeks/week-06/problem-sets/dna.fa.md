---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-ps-dna
type: problem-set-guide
title: راهنمای شناسایی DNA
title_fa: شناسایی DNA
title_en: DNA
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/6/dna/
source_refs:
- src-pset-6-dna#problem-to-solve
- src-pset-6-dna#specification
- src-anzali-authored-6
- src-pset-6#what-to-do
- src-pset-6#academic-honesty
concept_ids:
- w06-c-sys-argv
- w06-c-sys-exit
- w06-c-with-open
- w06-c-csv-module
- w06-c-csv-dictreader
- w06-c-list-of-dicts
- w06-c-dict
- w06-c-list
- w06-c-int-conversion
- w06-c-str-dna
- w06-c-def-function
problem_set_ref: weeks/week-06/problem-sets/dna.json
prev: w06-ps-readability
next: w06-pr-bank
order: 25
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای شناسایی DNA

> **منبع رسمی:** [DNA](https://cs50.harvard.edu/x/2026/psets/6/dna/) از پرابلم‌ست ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

DNA از مولکول‌هایی به نام نوکلئوتید ساخته شده که هر کدام یکی از چهار باز A، C، G یا T را دارد. در جاهایی از DNA توالی‌های کوتاهی پشت سر هم تکرار می‌شوند که به آن‌ها **STR** (Short Tandem Repeat) می‌گویند، و تعداد تکرار هر STR از فردی به فرد دیگر خیلی فرق می‌کند. اگر چند STR را با هم بسنجی، احتمال این‌که دو نمونه تصادفاً یکی باشند بسیار کم می‌شود.

در این مسئله برنامهٔ `dna.py` را کامل می‌کنی تا یک پایگاه دادهٔ CSV (هر سطر یک فرد، هر ستون یک STR و عددش طولانی‌ترین تکرار پیاپی آن STR در DNA آن فرد) و یک فایل متنی توالی DNA را بگیرد و بگوید DNA به چه کسی تعلق دارد، یا `No match`.

کد آغازین تابع کمکی `longest_match` را آماده دارد که برای یک توالی و یک STR طولانی‌ترین تکرار پیاپی را برمی‌گرداند. کار تو خواندن فایل‌ها، فراخوانی این تابع برای هر STR و مقایسهٔ نتیجه با سطرهای پایگاه داده است.

> **از سخنرانی و جلسه:** `sys.argv` و `sys.exit` در [یادداشت خط فرمان](/kb/d/w06-n14)، `with open` و ماژول `csv` در [یادداشت CSV و کتابخانه‌ها](/kb/d/w06-n15)، واژه‌نامه در [یادداشت جست‌وجو و واژه‌نامه](/kb/d/w06-n13) و `csv.DictReader` در [جلسهٔ حل تمرین](/kb/d/w06-sec).

## خواسته‌های رسمی

1. در فایل `dna.py` در پوشهٔ `dna` برنامه‌ای بنویس که تشخیص بدهد یک توالی DNA به چه کسی تعلق دارد.
2. آرگومان اول خط فرمان نام فایل CSV شمارهٔ STRهای افراد و آرگومان دوم نام فایل متنی توالی DNA است.
3. اگر تعداد آرگومان‌ها نادرست بود، یک پیام خطای دلخواه (با `print`) چاپ کن.
4. فایل CSV را باز کن و محتوایش را در حافظه بخوان؛ سطر اول نام ستون‌هاست.
5. ستون اول واژهٔ `name` است و ستون‌های بعدی خود توالی‌های STR.
6. فایل توالی DNA را باز کن و محتوایش را در حافظه بخوان.
7. برای هر STR (از سطر اول CSV) طولانی‌ترین تکرار پیاپی آن را در توالی پیدا کن؛ تابع کمکی `longest_match` همین کار را می‌کند.
8. اگر شمارهٔ STRها دقیقاً با یکی از افراد CSV یکی بود، نام او را چاپ کن.
9. اگر با هیچ‌کس دقیقاً یکی نبود، `No match` چاپ کن.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌های آغازین را دانلود کن. پوشه شامل `dna.py`، پوشهٔ `databases` (دو فایل CSV) و پوشهٔ `sequences` (بیست فایل توالی) است. پیش از نوشتن، `dna.py` را کامل بخوان: `main` چند `TODO` دارد و `longest_match` آماده است و نباید آن را تغییر بدهی یا بازنویسی کنی.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/6/dna.zip
unzip dna.zip
rm dna.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd dna
```

## نمونه‌های رسمی ورودی و خروجی

فایل‌ها و پوشه‌ها پس از `ls`:

```text
databases/ dna.py sequences/
```

نمونهٔ رسمی پایگاه دادهٔ CSV (بخش Background):

```text
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

## آزمون‌های رسمی ورودی و خروجی

صفحهٔ رسمی این اجراها و خروجی مورد انتظار را می‌دهد (پیش از check50 خودت بیازما):

- `python dna.py databases/small.csv sequences/1.txt` ← `Bob`
- `python dna.py databases/small.csv sequences/2.txt` ← `No match`
- `python dna.py databases/small.csv sequences/3.txt` ← `No match`
- `python dna.py databases/small.csv sequences/4.txt` ← `Alice`
- `python dna.py databases/large.csv sequences/5.txt` ← `Lavender`
- `python dna.py databases/large.csv sequences/6.txt` ← `Luna`
- `python dna.py databases/large.csv sequences/7.txt` ← `Ron`
- `python dna.py databases/large.csv sequences/8.txt` ← `Ginny`
- `python dna.py databases/large.csv sequences/9.txt` ← `Draco`
- `python dna.py databases/large.csv sequences/10.txt` ← `Albus`
- `python dna.py databases/large.csv sequences/11.txt` ← `Hermione`
- `python dna.py databases/large.csv sequences/12.txt` ← `Lily`
- `python dna.py databases/large.csv sequences/13.txt` ← `No match`
- `python dna.py databases/large.csv sequences/14.txt` ← `Severus`
- `python dna.py databases/large.csv sequences/15.txt` ← `Sirius`
- `python dna.py databases/large.csv sequences/16.txt` ← `No match`
- `python dna.py databases/large.csv sequences/17.txt` ← `Harry`
- `python dna.py databases/large.csv sequences/18.txt` ← `No match`
- `python dna.py databases/large.csv sequences/19.txt` ← `Fred`
- `python dna.py databases/large.csv sequences/20.txt` ← `No match`

## قطعه‌کدهای رسمی راهنما

> **رسمی:** این قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند و ابزار عمومی‌اند، نه بخشی از راه‌حل.

چاپ نام ستون‌های یک CSV با `fieldnames` (از بخش Hints):

```python
import csv

with open("foo.csv") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
```

خواندن همهٔ سطرهای CSV در فهرستی از واژه‌نامه‌ها (از بخش Hints):

```python
import csv

rows = []
with open("foo.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- sys.argv و from sys import argv — [یادداشت](/kb/d/w06-n14) · درس کوتاه `w06-l07` (واحد `w06-l07-u03`)
- sys.exit و وضعیت خروج — [یادداشت](/kb/d/w06-n14) · درس کوتاه `w06-l07` (واحد `w06-l07-u03`)
- with open(...) و بسته‌شدن خودکار فایل — [یادداشت](/kb/d/w06-n15) · درس کوتاه `w06-l07` (واحد `w06-l07-u04`)
- ماژول csv: writer و writerow — [یادداشت](/kb/d/w06-n15) · درس کوتاه `w06-l07` (واحد `w06-l07-u04`)
- csv.DictReader: هر سطر یک dict — [یادداشت](/kb/d/w06-ps-dna)
- فهرستی از دیکشنری‌ها — [یادداشت](/kb/d/w06-n13) · درس کوتاه `w06-l07` (واحد `w06-l07-u02`)
- دیکشنری (dict): جفت‌های کلید و مقدار — [یادداشت](/kb/d/w06-n13) · درس کوتاه `w06-l07` (واحد `w06-l07-u02`)
- فهرست (list): دنباله‌ای تغییرپذیر — [یادداشت](/kb/d/w06-n12) · درس کوتاه `w06-l06` (واحد `w06-l06-u03`)
- تبدیل با int(...) — [یادداشت](/kb/d/w06-n06) · درس کوتاه `w06-l02` (واحد `w06-l02-u04`)
- STR: توالی کوتاه تکرارشونده در DNA — [یادداشت](/kb/d/w06-ps-dna)
- تعریف تابع با def و پارامترها — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. `dna.py` را باز کن و `TODO`ها را به ترتیب بخوان. هر `TODO` یک گام است: بررسی آرگومان‌ها، خواندن CSV، خواندن توالی، یافتن تکرارها، یافتن فرد.
2. برای بررسی آرگومان‌ها، یادداشت خط فرمان را مرور کن: `sys.argv` چند عضو دارد اگر کاربر دو نام فایل بدهد؟
3. برای CSV، دو قطعه‌کد رسمی بالا را ببین: یکی نام ستون‌ها را می‌دهد و دیگری همهٔ سطرها را. از خودت بپرس کدام ستون‌ها STR هستند.
4. برای فایل توالی، صفحهٔ رسمی تابع‌های `open` و `read` را پیشنهاد می‌کند. توالی فقط یک رشتهٔ بلند است.
5. `longest_match` را برای هر STR صدا بزن و نتیجه‌ها را در ساختاری نگه دار که بعداً مقایسه‌اش با یک سطر CSV آسان باشد. صفحهٔ رسمی فهرست یا واژه‌نامه را پیشنهاد می‌کند.
6. یادت باشد هر مقداری که از CSV خوانده می‌شود رشته است، همان‌طور که در جلسهٔ حل تمرین دیدی. عدد `17` و رشتهٔ `"17"` با `==` برابر نیستند.
7. برنامه نباید به `small.csv` وابسته باشد: `large.csv` STRهای بیشتری دارد. با هر دو پایگاه داده آزمایش کن.

## اشتباه‌های رایج

- نوشتن نام STRها در کد به جای خواندن از سطر اول CSV
- مقایسهٔ رشته با عدد و نگرفتن هیچ تطبیقی
- چاپ نام فرد وقتی فقط بخشی از STRها یکی است
- چاپ `No match` درون حلقه برای هر سطر به جای یک بار در پایان
- تغییر یا بازنویسی `longest_match`

## چک‌لیست خودآزمایی

1. فقط `TODO`های `main` را کامل کرده‌ام و از `longest_match` آماده استفاده می‌کنم.
2. با تعداد نادرست آرگومان پیام خطا چاپ می‌شود.
3. نام STRها را از سطر اول CSV می‌خوانم، نه این‌که در کد بنویسم.
4. مقدارهای CSV را پیش از مقایسه با عددهای محاسبه‌شده به نوع درست تبدیل می‌کنم.
5. فقط وقتی نام چاپ می‌شود که همهٔ STRها دقیقاً یکی باشند.
6. در غیر این صورت `No match` چاپ می‌شود.
7. هر بیست اجرای رسمی خروجی درست می‌دهند، هم با `small.csv` و هم با `large.csv`.
8. check50 همه را سبز نشان می‌دهد.
9. style50 تغییری پیشنهاد نمی‌کند.
10. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/dna
```

سبک با style50:

```bash
style50 dna.py
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/dna
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد آغازین `dna.py` (شامل `longest_match`)](https://cdn.cs50.net/2026/x/psets/6/dna.zip): کد آغازین رسمی را دانلود کن و بخوان؛ در این بسته بازتولید نشده است.
- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/watch?v=j84b_EgntcQ): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/j84b_EgntcQ)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/5onE9BNq1zhL2D72gfu9IbdsD)

## پیوند رسمی

- [DNA](https://cs50.harvard.edu/x/2026/psets/6/dna/)
- [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
