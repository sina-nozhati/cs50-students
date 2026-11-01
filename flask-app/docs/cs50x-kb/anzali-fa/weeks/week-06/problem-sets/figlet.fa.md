---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-pr-figlet
type: practice-guide
title: راهنمای حروف بزرگ FIGlet
title_fa: حروف بزرگ FIGlet
title_en: Frank, Ian and Glen’s Letters
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/figlet/
source_refs:
- src-practice-figlet#frank-ian-and-glens-letters
- src-anzali-authored-6
concept_ids:
- w06-c-sys-argv
- w06-c-sys-exit
- w06-c-third-party
- w06-c-import
- w06-c-in-list
problem_set_ref: weeks/week-06/problem-sets/figlet.json
prev: w06-pr-bank
next: w06-pr-jar
order: 27
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای حروف بزرگ FIGlet

> **منبع رسمی:** [Frank, Ian and Glen’s Letters](https://cs50.harvard.edu/x/2026/practice/figlet/) از مسئله‌های تمرینی هفتهٔ ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

FIGlet برنامه‌ای از اوایل دههٔ ۱۹۹۰ است که از متن معمولی حروف بزرگ هنری (ASCII art) می‌سازد، و نسخهٔ پایتونی آن ماژولی به نام `pyfiglet` است.

در فایل `figlet.py` برنامه‌ای بنویس که صفر یا دو آرگومان خط فرمان بگیرد: بدون آرگومان، متن را با قلمی تصادفی چاپ کند؛ با دو آرگومان، اولی `-f` یا `--font` و دومی نام قلم باشد. اگر آرگومان‌ها نادرست بودند، برنامه با `sys.exit` و یک پیام خطا خارج شود.

> **از سخنرانی:** `sys.argv` و `sys.exit` در [یادداشت خط فرمان](/kb/d/w06-n14) و نصب کتابخانهٔ شخص ثالث با `pip` در [یادداشت CSV و کتابخانه‌ها](/kb/d/w06-n15).

## خواسته‌های رسمی

1. برنامه صفر یا دو آرگومان خط فرمان می‌گیرد.
2. صفر، اگر کاربر می‌خواهد متن با قلمی تصادفی چاپ شود.
3. دو، اگر کاربر قلم مشخصی می‌خواهد؛ اولی `-f` یا `--font` و دومی نام قلم.
4. از کاربر یک `str` متن بخواه.
5. متن را با قلم خواسته‌شده چاپ کن.
6. اگر دو آرگومان داده شد و اولی `-f` یا `--font` نبود یا دومی نام قلم نبود، با `sys.exit` و پیام خطا خارج شو.

> **توجه (d107):** این مسئلهٔ تمرینی از CS50P سال ۲۰۲۲ آمده است؛ فایل آغازین و دستور check50 آن نشانی ۲۰۲۲ دارند و همان‌طور که در صفحهٔ رسمی هست نقل شده‌اند.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل آغازین را دانلود کن. سپس `pyfiglet` را با `pip` نصب کن (قطعهٔ رسمی پایین).

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/6/figlet.zip
unzip figlet.zip
rm figlet.zip
```

## نمونه‌های رسمی ورودی و خروجی

`python figlet.py test`:

```text
Invalid usage
```

`python figlet.py -f slant` با ورودی `CS50`:

```text
   ___________ __________
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ /
\____//____/_____/\____/
```

## قطعه‌کدهای رسمی راهنما

> **رسمی:** این قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند و ابزار عمومی‌اند، نه بخشی از راه‌حل.

نصب ماژول (از بخش Hints):

```bash
pip install pyfiglet
```

ساختن شیء `Figlet` (از بخش Hints):

```python
from pyfiglet import Figlet

figlet = Figlet()
```

فهرست قلم‌ها:

```python
figlet.getFonts()
```

تعیین قلم؛ `f` نام قلم است:

```python
figlet.setFont(font=f)
```

چاپ متن با قلم؛ `s` متن است:

```python
print(figlet.renderText(s))
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- sys.argv و from sys import argv — [یادداشت](/kb/d/w06-n14) · درس کوتاه `w06-l07` (واحد `w06-l07-u03`)
- sys.exit و وضعیت خروج — [یادداشت](/kb/d/w06-n14) · درس کوتاه `w06-l07` (واحد `w06-l07-u03`)
- کتابخانهٔ شخص ثالث و pip install — [یادداشت](/kb/d/w06-n15) · درس کوتاه `w06-l07` (واحد `w06-l07-u04`)
- import و from ... import — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)
- عضویت با in در یک فهرست — [یادداشت](/kb/d/w06-n07) · درس کوتاه `w06-l03` (واحد `w06-l03-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول تعداد آرگومان‌ها را بسنج: `len(sys.argv)` برای صفر آرگومان کاربر چند است؟ برای دو آرگومان چند؟
2. برای سنجیدن نام قلم، فهرست قلم‌ها را از `getFonts` بگیر و عضویت را با `in` بسنج.
3. برای انتخاب تصادفی، صفحهٔ رسمی ماژول `random` را پیشنهاد می‌کند؛ در مستنداتش تابعی برای برداشتن یک عضو تصادفی از فهرست پیدا کن.
4. `sys.exit` می‌تواند پیام را هم بگیرد؛ مستندات را ببین.

## اشتباه‌های رایج

- فراموش کردن حالت یک آرگومان یا بیش از دو آرگومان
- سنجیدن فقط `-f` و فراموش کردن `--font`
- نصب نکردن `pyfiglet` و گرفتن `ModuleNotFoundError`

## چک‌لیست خودآزمایی

1. بدون آرگومان، متن با قلمی تصادفی چاپ می‌شود.
2. `-f slant` و `--font slant` هر دو کار می‌کنند.
3. `test`، `-a slant` و `-f invalid_font` با `sys.exit` و پیام خطا خارج می‌شوند.
4. متن را از کاربر می‌گیرم و با قلم درست چاپ می‌کنم.
5. check50 همه را سبز نشان می‌دهد.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2022/python/figlet
```

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/LIo5QcHpUiXepVFiL4fTBwmuE)

## پیوند رسمی

- [Frank, Ian and Glen’s Letters](https://cs50.harvard.edu/x/2026/practice/figlet/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
