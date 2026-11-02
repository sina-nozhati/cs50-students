---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-ps-readability
type: problem-set-guide
title: راهنمای خوانایی متن (Sentimental Readability)
title_fa: خوانایی متن (Sentimental Readability)
title_en: Readability
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/6/readability/
source_refs:
- src-pset-6-readability#problem-to-solve
- src-pset-6-readability#specification
- src-anzali-authored-6
- src-pset-6#what-to-do
- src-pset-6#academic-honesty
concept_ids:
- w06-c-port-c-to-python
- w06-c-cs50-library-py
- w06-c-iterate-string
- w06-c-string-methods
- w06-c-true-division
- w06-c-elif
problem_set_ref: weeks/week-06/problem-sets/readability.json
prev: w06-ps-credit
next: w06-ps-dna
order: 24
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای خوانایی متن (Sentimental Readability)

> **منبع رسمی:** [Readability](https://cs50.harvard.edu/x/2026/psets/6/readability/) از پرابلم‌ست ۶ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

همان مسئلهٔ خوانایی پرابلم‌ست ۲، این بار به پایتون: برنامه‌ای در فایل `readability.py` و پوشهٔ `sentimental-readability` که متنی از کاربر می‌گیرد و پایهٔ تحصیلی لازم برای خواندن آن را طبق فرمول Coleman-Liau چاپ می‌کند.

فرمول رسمی `0.0588 * L - 0.296 * S - 15.8` است که در آن `L` میانگین تعداد حروف در هر ۱۰۰ واژه و `S` میانگین تعداد جمله‌ها در هر ۱۰۰ واژه است. حرف یعنی `a` تا `z` یا `A` تا `Z`؛ هر دنباله‌ای از نویسه‌ها که با فاصله جدا شده یک واژه است؛ و هر نقطه، علامت تعجب یا علامت سؤال پایان یک جمله است. خروجی `Grade X` است، با `Grade 16+` برای ۱۶ یا بیشتر و `Before Grade 1` برای کمتر از ۱. صفحهٔ رسمی پرابلم‌ست ۶ می‌گوید نگاه کردن به پیاده‌سازی C خودت یا دیگران برای این مسئله معقول است، اما نگاه کردن به پیاده‌سازی پایتونِ دیگران معقول نیست. این راهنما هیچ کد پایتونی از برنامهٔ خواسته‌شده ندارد.

> **از سخنرانی:** متدهای رشته در [یادداشت شیءگرایی](/kb/d/w06-n08)، پیمایش رشته در [یادداشت حلقه‌ها](/kb/d/w06-n09) و تقسیم بدون بریدن در [یادداشت تقسیم و استثنا](/kb/d/w06-n10).

> **از هفتهٔ ۲:** راهنمای فارسی نسخهٔ C این مسئله در [پرابلم‌ست ۲](/kb/d/w02-fa) هست.

## خواسته‌های رسمی

1. برنامه‌ای بنویس که اول از کاربر متنی بخواهد و بعد پایهٔ تحصیلی متن را طبق فرمول Coleman-Liau چاپ کند.
2. شاخص Coleman-Liau برابر `0.0588 * L - 0.296 * S - 15.8` است؛ `L` میانگین حروف در هر ۱۰۰ واژه و `S` میانگین جمله‌ها در هر ۱۰۰ واژه.
3. ورودی را با `get_string` از کتابخانهٔ CS50 بگیر و پاسخ را با `print` چاپ کن.
4. تعداد حروف، واژه‌ها و جمله‌های متن را بشمار.
5. حرف یعنی هر نویسهٔ کوچک `a` تا `z` یا بزرگ `A` تا `Z`؛ هر دنباله از نویسه‌ها که با فاصله جدا شده یک واژه است؛ و هر نقطه، علامت تعجب یا علامت سؤال پایان جمله است.
6. خروجی `"Grade X"` باشد که `X` شاخص Coleman-Liau گردشده به نزدیک‌ترین عدد صحیح است.
7. اگر شاخص ۱۶ یا بیشتر بود `"Grade 16+"` و اگر کمتر از ۱ بود `"Before Grade 1"` چاپ کن.

> **استنتاج (مستندات پایتون):** تابع داخلی `round` در پایتون ۳ عددهایی را که دقیقاً وسط دو عدد صحیح‌اند به عدد **زوج** نزدیک‌تر گرد می‌کند (`round(2.5)` برابر `2` است)، در حالی که `round` در C آن‌ها را از صفر دور می‌کند. در متن‌های رسمی شاخص دقیقاً روی ۰٫۵ نمی‌افتد، ولی اگر نتیجه‌ات با نسخهٔ C فرق داشت، به این تفاوت فکر کن.

## شروع کار

این مسئله کد آغازین ندارد. پوشهٔ `sentimental-readability` را بساز و فایل `readability.py` را در آن بنویس.

## متن‌های آزمون رسمی

صفحهٔ رسمی این متن‌ها و پایهٔ مورد انتظارشان را برای آزمودن برنامه فهرست می‌کند (برنامه را با `python readability.py` اجرا کن):

- `One fish. Two fish. Red fish. Blue fish.` ← `Before Grade 1`
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` ← `Grade 2`
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` ← `Grade 3`
- `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` ← `Grade 5`
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` ← `Grade 7`
- `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` ← `Grade 8`
- `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` ← `Grade 8`
- `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` ← `Grade 9`
- `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` ← `Grade 10`
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` ← `Grade 16+`

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- بازنویسی برنامهٔ C در پایتون (Sentimental) — [یادداشت](/kb/d/w06-ps-hello)
- کتابخانهٔ CS50 در پایتون: get_string، get_int، get_float — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)
- پیمایش حرف‌به‌حرف رشته: for c in s — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u02`)
- متدهای رشته: lower، upper، capitalize — [یادداشت](/kb/d/w06-n08) · درس کوتاه `w06-l03` (واحد `w06-l03-u03`)
- تقسیم / در پایتون ۳ همیشه float می‌دهد (بدون بریدن) — [یادداشت](/kb/d/w06-n10) · درس کوتاه `w06-l05` (واحد `w06-l05-u01`)
- if، elif، else — [یادداشت](/kb/d/w06-n07) · درس کوتاه `w06-l03` (واحد `w06-l03-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. منطق شمارش همان منطق برنامهٔ C خودت از پرابلم‌ست ۲ است. ببین در پایتون کدام بخش‌ها کوتاه‌تر می‌شوند: پیمایش رشته و متدهای رشته‌ای که حرف بودن یک نویسه را می‌سنجند.
2. سه شمارنده لازم داری. برای هر کدام تعریف رسمی را دقیق بخوان: مثلاً آپاستروف و ویرگول حرف نیستند.
3. در پایتون ۳ تقسیم `/` بریده نمی‌شود، پس نگرانی تبدیل به `float` در C این‌جا کمتر است. با این حال ترتیب ضرب و تقسیم را برای «در هر ۱۰۰ واژه» روی کاغذ چک کن.
4. پیش از گرد کردن، شاخص را برای یکی از متن‌های رسمی با دست حساب کن و با خروجی برنامه مقایسه کن.
5. مرزها را جداگانه بیازما: متنی که باید `Before Grade 1` و متنی که باید `Grade 16+` بدهد.

## اشتباه‌های رایج

- شمردن نشانه‌گذاری یا رقم به عنوان حرف
- شمردن واژه‌ها با تعداد فاصله‌ها بدون در نظر گرفتن واژهٔ آخر
- استفاده از `//` و از دست دادن بخش اعشاری میانگین‌ها
- فراموش کردن مرزهای ۱ و ۱۶

## چک‌لیست خودآزمایی

1. فایل `readability.py` در پوشهٔ `sentimental-readability` است و به پایتون نوشته شده.
2. متن را با `get_string` می‌گیرم.
3. حروف، واژه‌ها و جمله‌ها را طبق تعریف رسمی می‌شمارم.
4. `L` و `S` را «در هر ۱۰۰ واژه» حساب می‌کنم، نه نسبت ساده.
5. خروجی‌ها دقیقاً `Grade X`، `Grade 16+` یا `Before Grade 1` هستند.
6. همهٔ ده متن آزمون رسمی پایهٔ درست را می‌دهند.
7. check50 همه را سبز نشان می‌دهد.
8. style50 تغییری پیشنهاد نمی‌کند.
9. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/sentimental/readability
```

سبک با style50:

```bash
style50 readability.py
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/sentimental/readability
```

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/WnE6pZNnDkDm8NtuxrTqY1Nu4)

## پیوند رسمی

- [Readability](https://cs50.harvard.edu/x/2026/psets/6/readability/)
- [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
