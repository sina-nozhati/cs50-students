---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-ps-credit
type: problem-set-guide
title: راهنمای کارت اعتباری (Sentimental Credit)
title_fa: کارت اعتباری (Sentimental Credit)
title_en: Credit
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/6/credit/
source_refs:
- src-pset-6-credit#problem-to-solve
- src-pset-6-credit#specification
- src-anzali-authored-6
- src-pset-6#what-to-do
- src-pset-6#academic-honesty
concept_ids:
- w06-c-port-c-to-python
- w06-c-cs50-library-py
- w06-c-iterate-string
- w06-c-int-conversion
- w06-c-string-slicing
- w06-c-floor-division
- w06-c-regex-validation
problem_set_ref: weeks/week-06/problem-sets/credit.json
prev: w06-ps-cash
next: w06-ps-readability
order: 23
choice_group: cash-or-credit
submission: choose-one
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای کارت اعتباری (Sentimental Credit)

> **منبع رسمی:** [Credit](https://cs50.harvard.edu/x/2026/psets/6/credit/) از پرابلم‌ست ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از دو نسخه را تحویل بده؛ اگر هر دو را تحویل بدهی، نمرهٔ بالاتر ثبت می‌شود. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

همان مسئلهٔ کارت اعتباری پرابلم‌ست ۱، این بار به پایتون: برنامه‌ای در فایل `credit.py` و پوشهٔ `sentimental-credit` که شمارهٔ کارت را می‌گیرد و می‌گوید شمارهٔ معتبر American Express، MasterCard یا Visa است یا نه. آخرین سطر خروجی باید دقیقاً یکی از `AMEX`، `MASTERCARD`، `VISA` یا `INVALID` باشد.

می‌توانی فرض کنی ورودی فقط رقم است. صفحهٔ رسمی می‌گوید بسته به شیوهٔ پیاده‌سازی‌ات `get_int` یا `get_string` را به کار ببر، و به‌عنوان راهنمایی اختیاری ماژول `re` (عبارت‌های منظم) را برای سنجیدن ورودی پیشنهاد می‌کند. صفحهٔ رسمی پرابلم‌ست ۶ می‌گوید نگاه کردن به پیاده‌سازی C خودت یا دیگران برای این مسئله معقول است، اما نگاه کردن به پیاده‌سازی پایتونِ دیگران معقول نیست. این راهنما هیچ کد پایتونی از برنامهٔ خواسته‌شده ندارد.

> **از سخنرانی:** پیمایش رشته در [یادداشت حلقه‌ها](/kb/d/w06-n09)، برش در [جلسهٔ حل تمرین](/kb/d/w06-sec) و `//` در [یادداشت تقسیم و استثنا](/kb/d/w06-n10).

> **از هفتهٔ ۱:** راهنمای فارسی نسخهٔ C این مسئله در [پرابلم‌ست ۱](/kb/d/w01-fa) هست. منطق همان است؛ فقط نحو عوض می‌شود.

## خواسته‌های رسمی

1. برنامه‌ای بنویس که شمارهٔ کارت اعتباری را بپرسد و (با `print`) بگوید شمارهٔ معتبر American Express، MasterCard یا Visa است یا نه.
2. آخرین سطر خروجی باید `AMEX\n` یا `MASTERCARD\n` یا `VISA\n` یا `INVALID\n` باشد، نه بیشتر و نه کمتر.
3. می‌توانی فرض کنی ورودی کاربر فقط رقم است (بدون خط تیره).
4. بسته به شیوهٔ پیاده‌سازی، `get_int` یا `get_string` کتابخانهٔ CS50 را برای گرفتن ورودی به کار ببر.

> **توجه (d106):** متن رسمی چند غلط تایپی دارد (مثلاً «In a filed called» و «how you to decide»). در خواسته‌ها متن انگلیسی همان‌طور که هست نقل شده و بازنویسی فارسی درست خوانده می‌شود.

## شروع کار

این مسئله کد آغازین ندارد. پوشهٔ `sentimental-credit` را بساز و فایل `credit.py` را در آن بنویس.

## آزمون‌های رسمی ورودی و خروجی

صفحهٔ رسمی این شماره‌ها و خروجی‌های مورد انتظار را می‌دهد (برنامه را با `python credit.py` اجرا کن):

- `378282246310005` ← `AMEX`
- `371449635398431` ← `AMEX`
- `5555555555554444` ← `MASTERCARD`
- `5105105105105100` ← `MASTERCARD`
- `4111111111111111` ← `VISA`
- `4012888888881881` ← `VISA`
- `1234567890` ← `INVALID`

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- بازنویسی برنامهٔ C در پایتون (Sentimental) — [یادداشت](/kb/d/w06-ps-hello)
- کتابخانهٔ CS50 در پایتون: get_string، get_int، get_float — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)
- پیمایش حرف‌به‌حرف رشته: for c in s — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u02`)
- تبدیل با int(...) — [یادداشت](/kb/d/w06-n06) · درس کوتاه `w06-l02` (واحد `w06-l02-u04`)
- اندیس و برش رشته (phrase[1:]) و range با گام — [یادداشت](/kb/d/w06-sec) · درس کوتاه `w06-l06` (واحد `w06-l06-u04`)
- تقسیم صحیح با // (جزء صحیحِ رو به پایین) — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u01`)
- ماژول re برای اعتبارسنجی ورودی (اختیاری) — [یادداشت](/kb/d/w06-ps-credit)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. الگوریتم Luhn و قاعده‌های طول و رقم‌های آغازین هر شبکه همان‌هایی‌اند که در پرابلم‌ست ۱ پیاده کردی. صفحهٔ رسمی نگاه کردن به کد C خودت را معقول می‌داند.
2. اول تصمیم بگیر شماره را به شکل عدد نگه داری یا رشته. هر کدام کار با رقم‌ها را به شکل متفاوتی آسان می‌کند: با عدد از `%` و `//`، با رشته از نمایه، برش و پیمایش.
3. اگر رشته را انتخاب کنی، یادت باشد هر نویسه هنوز `str` است و پیش از جمع زدن باید به عدد تبدیل شود.
4. در پایتون عدد صحیح سرریز نمی‌کند، پس نگرانی `long` در C این‌جا وجود ندارد.
5. اختیاری: صفحهٔ رسمی ماژول `re` را برای سنجیدن این‌که ورودی فقط رقم و با طول مناسب است پیشنهاد می‌کند. مستندات `re` را خودت بخوان.
6. شماره‌هایی بساز که طول یا رقم آغازین درست ولی جمع‌آزمای نادرست دارند، و برعکس، تا هر شاخهٔ برنامه را بیازمایی.

## اشتباه‌های رایج

- فراموش کردن تبدیل نویسه به عدد و گرفتن خطای `TypeError`
- بررسی نکردن طول یا رقم‌های آغازین پس از گذشتن از Luhn
- شمارش رقم‌ها از سمت اشتباه (Luhn از رقم یکی مانده به آخر شروع می‌کند)
- چاپ متن اضافه به جز چهار واژهٔ خواسته‌شده

## چک‌لیست خودآزمایی

1. فایل `credit.py` در پوشهٔ `sentimental-credit` است و به پایتون نوشته شده.
2. آخرین سطر خروجی دقیقاً یکی از چهار واژهٔ خواسته‌شده است.
3. ورودی را با `get_int` یا `get_string` می‌گیرم.
4. هر هفت آزمون رسمی خروجی درست می‌دهند.
5. شماره‌ای با طول درست ولی جمع‌آزمای نادرست `INVALID` می‌گیرد.
6. check50 همه را سبز نشان می‌دهد.
7. style50 تغییری پیشنهاد نمی‌کند.
8. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/sentimental/credit
```

سبک با style50:

```bash
style50 credit.py
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/sentimental/credit
```

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/QYLr1R1RDLO9QkPF2XFODLkq4)

## پیوند رسمی

- [Credit](https://cs50.harvard.edu/x/2026/psets/6/credit/)
- [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
