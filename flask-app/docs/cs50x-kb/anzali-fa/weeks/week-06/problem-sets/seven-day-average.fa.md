---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-pr-seven-day-average
type: practice-guide
title: راهنمای میانگین هفت‌روزه
title_fa: میانگین هفت‌روزه
title_en: Seven Day Averages
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/seven-day-average/
source_refs:
- src-practice-seven-day-average#implementation-details
- src-practice-seven-day-average#calculate
- src-anzali-authored-6
concept_ids:
- w06-c-csv-dictreader
- w06-c-dict
- w06-c-list
- w06-c-append
- w06-c-string-slicing
- w06-c-sum-len
- w06-c-try-except
- w06-c-exception
problem_set_ref: weeks/week-06/problem-sets/seven-day-average.json
prev: w06-pr-jar
next: w06-pr-taqueria
order: 29
choice_group: null
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای میانگین هفت‌روزه

> **منبع رسمی:** [Seven Day Averages](https://cs50.harvard.edu/x/2026/practice/seven-day-average/) از مسئله‌های تمرینی هفتهٔ ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

یکی از رایج‌ترین روش‌های دنبال کردن موارد کووید میانگین هفت‌روزه است، چون برخی ایالت‌ها فقط هفته‌ای یک بار گزارش می‌دهند. برنامهٔ آغازین داده‌های تجمعی مخزن New York Times را با کتابخانهٔ `requests` می‌گیرد و با `DictReader` می‌خواند.

تو دو تابع را کامل می‌کنی: `calculate` که واژه‌نامهٔ `new_cases` را می‌سازد (برای هر ایالت موارد تازهٔ ۱۴ روز اخیر، که از تفاضل روزهای پیاپی داده‌های تجمعی به دست می‌آید)، و `comparative_averages` که میانگین هفت روز اخیر را با هفت روز پیش از آن مقایسه می‌کند و درصد افزایش یا کاهش را چاپ می‌کند.

> **از سخنرانی و جلسه:** واژه‌نامه در [یادداشت جست‌وجو و واژه‌نامه](/kb/d/w06-n13)، فهرست و برش در [یادداشت فهرست‌ها](/kb/d/w06-n12) و [جلسهٔ حل تمرین](/kb/d/w06-sec)، و `try`/`except` در [یادداشت تقسیم و استثنا](/kb/d/w06-n10).

## خواسته‌های رسمی

1. دو تابع `calculate` و `comparative_averages` را کامل کن.
2. در `calculate` واژه‌نامهٔ `new_cases` را بساز که موارد تازهٔ ۱۴ روز را برای هر ایالت نگه دارد.
3. چون داده‌ها تجمعی‌اند، موارد تازهٔ هر روز با کم کردن موارد روز قبل به دست می‌آید.
4. `calculate` در پایان واژه‌نامهٔ `new_cases` را برمی‌گرداند.
5. درصد افزایش یا کاهش را با تقسیم تفاضل دو میانگین هفت‌روزه بر میانگین هفتهٔ گذشته حساب کن.

> **توجه (d107):** این مسئلهٔ تمرینی از CS50P سال ۲۰۲۲ آمده است؛ فایل آغازین و دستور check50 آن نشانی ۲۰۲۲ دارند و همان‌طور که در صفحهٔ رسمی هست نقل شده‌اند.

> **ناهمخوانی (d111):** راهنمایی رسمی می‌گوید `values[3:5]` «عضوهای سوم تا چهارم نمایه‌دار» را برمی‌گرداند. منظور عضوهای با **نمایهٔ** ۳ و ۴ است، یعنی عضوهای چهارم و پنجم اگر از یک بشماری.

> **استنتاج:** مخزن داده‌های کووید New York Times از سال ۲۰۲۳ به‌روزرسانی نمی‌شود، پس «دادهٔ زنده» در عمل دادهٔ ثابت پایانی است.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل آغازین را دانلود کن. برنامه دادهٔ زنده را از اینترنت می‌گیرد، پس عددهای خروجی تو با نمونه‌های رسمی یکی نخواهند بود.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/6/seven-day-average.zip
unzip seven-day-average.zip
rm seven-day-average.zip
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی اجرا (عددها هر روز فرق می‌کنند):

```text
seven-day-average/ $ python seven-day-average.py
Choose one or more states to view average COVID cases.
Press enter when done.

State: Massachusetts
State: New York
State: 

Seven-Day Averages
Massachusetts had a 7-day average of 1646 and an increase of 46%.
New York had a 7-day average of 7502 and a decrease of 1%.
```

نمونهٔ رسمی دوم:

```text
seven-day-average/ $ python seven-day-average.py
Choose one or more states to view average COVID cases.
Press enter when done.

State: Maine
State: California
State: 

Seven-Day Averages
California had a 7-day average of 20461 and a decrease of 8%.
Maine had a 7-day average of 196 and a decrease of 10%.
```

## قطعه‌کدهای رسمی راهنما

> **رسمی:** این قطعه‌ها عیناً از صفحهٔ رسمی آمده‌اند و ابزار عمومی‌اند، نه بخشی از راه‌حل.

گرفتن تقسیم بر صفر با `try` و `except` (از بخش Hints):

```python
try:
    numerator / denominator
except ZeroDivisionError:
    ...
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- csv.DictReader: هر سطر یک dict — [یادداشت](/kb/d/w06-ps-dna)
- دیکشنری (dict): جفت‌های کلید و مقدار — [یادداشت](/kb/d/w06-n13) · درس کوتاه `w06-l07` (واحد `w06-l07-u02`)
- فهرست (list): دنباله‌ای تغییرپذیر — [یادداشت](/kb/d/w06-n12) · درس کوتاه `w06-l06` (واحد `w06-l06-u03`)
- متد append برای افزودن به انتهای فهرست — [یادداشت](/kb/d/w06-n12) · درس کوتاه `w06-l06` (واحد `w06-l06-u03`)
- اندیس و برش رشته (phrase[1:]) و range با گام — [یادداشت](/kb/d/w06-sec) · درس کوتاه `w06-l06` (واحد `w06-l06-u04`)
- تابع‌های داخلی sum و len — [یادداشت](/kb/d/w06-n12) · درس کوتاه `w06-l06` (واحد `w06-l06-u03`)
- try و except برای گرفتن استثنا — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u03`)
- استثنا (exception) و ValueError — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. کد آغازین را بخوان و ببین `calculate` چه چیزی ورودی می‌گیرد: هر سطر CSV یک واژه‌نامه با کلیدهای ستون‌هاست.
2. صفحهٔ رسمی پیشنهاد می‌کند واژه‌نامهٔ دومی (`previous_cases`) داشته باشی تا عدد تجمعی روز قبل هر ایالت را به خاطر بسپاری.
3. برای نگه داشتن فقط ۱۴ عدد، صفحهٔ رسمی می‌گوید عدد تازه را به انتهای فهرست بیفزا و اگر طول از ۱۴ بیشتر شد، عضو اول را حذف کن.
4. برای میانگین‌ها، برش فهرست را مرور کن. نمایه‌های منفی هم در پایتون معنا دارند.
5. اگر میانگین هفتهٔ قبل صفر باشد چه می‌شود؟ قطعهٔ رسمی `try`/`except` را ببین.

## اشتباه‌های رایج

- استفاده از عددهای تجمعی به جای موارد تازه
- نگه داشتن بیش یا کم از ۱۴ عدد
- اشتباه یک‌واحدی در برش (پایان برش ناشامل است)
- تقسیم بر صفر برای ایالتی بدون مورد تازه

## چک‌لیست خودآزمایی

1. `calculate` برای هر ایالت فهرستی از دقیقاً ۱۴ عدد موارد تازه می‌سازد.
2. موارد تازه از تفاضل روزهای پیاپی محاسبه می‌شوند، نه خود عددهای تجمعی.
3. `calculate` واژه‌نامه را برمی‌گرداند.
4. میانگین هفتهٔ اخیر از هفت عدد آخر و میانگین هفتهٔ قبل از هفت عدد اول فهرست است.
5. تقسیم بر صفر با `try` و `except` گرفته می‌شود.
6. style50 تغییری پیشنهاد نمی‌کند.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

سبک با style50:

```bash
style50 seven-day-average.py
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چرا فکر می‌کنی برخی وب‌سایت‌ها، مثل The Washington Post، برای «میانگین موارد تازهٔ روزانه» و «تغییر میانگین در هفت روز گذشته» برای بعضی ایالت‌ها عددهایی متفاوت با برنامهٔ تو و برای بعضی دیگر همان عددها را نشان می‌دهند؟

## پیوند رسمی

- [Seven Day Averages](https://cs50.harvard.edu/x/2026/practice/seven-day-average/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
