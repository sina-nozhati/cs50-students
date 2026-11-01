---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-pr-bank
type: practice-guide
title: راهنمای بانک (Bank)
title_fa: بانک (Bank)
title_en: Home Federal Savings Bank
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/bank/
source_refs:
- src-practice-bank#home-federal-savings-bank
- src-anzali-authored-6
concept_ids:
- w06-c-input-returns-str
- w06-c-string-methods
- w06-c-method-returns-new
- w06-c-elif
problem_set_ref: weeks/week-06/problem-sets/bank.json
prev: w06-ps-dna
next: w06-pr-figlet
order: 26
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای بانک (Bank)

> **منبع رسمی:** [Home Federal Savings Bank](https://cs50.harvard.edu/x/2026/practice/bank/) از مسئله‌های تمرینی هفتهٔ ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

در قسمتی از سریال Seinfeld، بانکی قول می‌دهد به هر کسی که با «hello» خوشامد گفته نشود ۱۰۰ دلار بدهد. Kramer با «hey» خوشامد گفته می‌شود و مدیر بانک با ۲۰ دلار به توافق می‌رسد، چون خوشامد دست‌کم با «h» شروع شده بود.

در فایل `bank.py` برنامه‌ای بنویس که خوشامد را بپرسد: اگر با «hello» شروع شد `$0`، اگر با «h» شروع شد (ولی نه «hello») `$20` و در غیر این صورت `$100` چاپ کند. فاصله‌های ابتدای ورودی نادیده گرفته می‌شوند و بزرگی و کوچکی حروف مهم نیست.

> **از سخنرانی:** متدهای رشته مثل `lower` و `strip` در [یادداشت شیءگرایی](/kb/d/w06-n08) و `elif` در [یادداشت شرط‌ها](/kb/d/w06-n07).

## خواسته‌های رسمی

1. در فایل `bank.py` برنامه‌ای بنویس که از کاربر خوشامدی بخواهد.
2. اگر خوشامد با «hello» شروع شد، `$0` چاپ کن.
3. اگر با «h» شروع شد (ولی نه «hello»)، `$20` چاپ کن.
4. در غیر این صورت `$100` چاپ کن.
5. فاصله‌های ابتدای خوشامد را نادیده بگیر و به بزرگی و کوچکی حروف حساس نباش.

> **توجه (d107):** این مسئلهٔ تمرینی از CS50P سال ۲۰۲۲ آمده است؛ فایل آغازین و دستور check50 آن نشانی ۲۰۲۲ دارند و همان‌طور که در صفحهٔ رسمی هست نقل شده‌اند.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل آغازین را دانلود کن. صفحهٔ رسمی پیشنهاد می‌کند فهرست متدهای رشته را در مستندات پایتون ببینی.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/6/bank.zip
unzip bank.zip
rm bank.zip
```

## آزمون‌های رسمی ورودی و خروجی

صفحهٔ رسمی این ورودی‌ها و خروجی‌ها را می‌دهد (برنامه را با `python bank.py` اجرا کن):

- `Hello` ← `$0`
- `Hello, Newman` ← `$0`
- `How you doing?` ← `$20`
- `What's happening?` ← `$100`

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- input همیشه str برمی‌گرداند — [یادداشت](/kb/d/w06-n06) · درس کوتاه `w06-l02` (واحد `w06-l02-u04`)
- متدهای رشته: lower، upper، capitalize — [یادداشت](/kb/d/w06-n08) · درس کوتاه `w06-l03` (واحد `w06-l03-u03`)
- متد رشته رشتهٔ تازه برمی‌گرداند و اصل را تغییر نمی‌دهد — [یادداشت](/kb/d/w06-n08) · درس کوتاه `w06-l03` (واحد `w06-l03-u03`)
- if، elif، else — [یادداشت](/kb/d/w06-n07) · درس کوتاه `w06-l03` (واحد `w06-l03-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. سه حالت داری؛ ترتیب بررسی آن‌ها مهم است. کدام حالت باید اول بررسی شود تا «hello» به اشتباه `$20` نگیرد؟
2. برای نادیده گرفتن فاصلهٔ ابتدا و بزرگی حروف، در مستندات متدهای رشته دنبال متدهایی بگرد که رشتهٔ تازه برمی‌گردانند.
3. متدی هم هست که می‌سنجد آیا رشته با پیشوند معینی شروع می‌شود؛ مستندات را ببین.
4. یادت باشد متد رشته، رشتهٔ اصلی را تغییر نمی‌دهد؛ نتیجه را باید نگه داری.

## اشتباه‌های رایج

- بررسی «h» پیش از «hello»
- فراموش کردن این‌که `"Hello"` و `"hello"` برابر نیستند
- صدا زدن متد بدون نگه داشتن نتیجه‌اش

## چک‌لیست خودآزمایی

1. ورودی `Hello` و `Hello, Newman` هر دو `$0` می‌دهند.
2. `How you doing?` خروجی `$20` می‌دهد.
3. `What's happening?` خروجی `$100` می‌دهد.
4. ورودی با فاصله در ابتدا یا با حروف بزرگ هم درست کار می‌کند.
5. check50 همه را سبز نشان می‌دهد.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2022/python/bank
```

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

این مسئله تحویل ندارد.

## ویدئو و نمایش

- [صحنهٔ سریال Seinfeld (از صفحهٔ رسمی)](https://youtu.be/IN6cJ_wGmsk)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/Pes7djS4b1GmwpwqNu2vj6LgY)

## پیوند رسمی

- [Home Federal Savings Bank](https://cs50.harvard.edu/x/2026/practice/bank/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
