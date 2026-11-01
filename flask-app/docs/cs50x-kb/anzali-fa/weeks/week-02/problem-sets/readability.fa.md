---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-ps-readability
type: problem-set-guide
title: راهنمای سطح خوانایی (Readability)
title_fa: سطح خوانایی (Readability)
title_en: Readability
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/2/readability/
source_refs:
- src-pset-2-readability#problem-to-solve
- src-pset-2-readability#advice
- src-anzali-authored-2
- src-pset-2#what-to-do
concept_ids:
- w02-c-reading-level
- w02-c-string-char-array
- w02-c-strlen
- w02-c-ctype
- w02-c-function-anatomy
- w02-c-array-parameter
problem_set_ref: weeks/week-02/problem-sets/readability.json
prev: w02-ps-scrabble
next: w02-ps-caesar
order: 29
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای سطح خوانایی (Readability)

> **منبع رسمی:** [Readability](https://cs50.harvard.edu/x/2026/psets/2/readability/) از پرابلم‌ست ۲ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

سطح خوانایی یک کتاب را معمولاً یک کارشناس تعیین می‌کند، اما الگوریتم هم می‌تواند. برنامه‌ای در `readability.c` (پوشهٔ `readability`) بنویس که تقریب پایهٔ تحصیلی لازم برای فهم یک متن را حساب کند و `Grade X` چاپ کند.

صفحهٔ رسمی از شاخص Coleman-Liau استفاده می‌کند. در این فرمول `L` میانگین تعداد حرف‌ها در هر ۱۰۰ واژه و `S` میانگین تعداد جمله‌ها در هر ۱۰۰ واژه است.

## خواسته‌های رسمی

1. فایل `readability.c` در پوشهٔ `readability`
2. خروجی `Grade X` باشد که X پایهٔ محاسبه‌شده، گردشده به نزدیک‌ترین عدد صحیح است.
3. اگر پایه ۱۶ یا بیشتر بود، `Grade 16+` چاپ شود.
4. اگر پایه کمتر از ۱ بود، `Before Grade 1` چاپ شود.
5. واژه یعنی هر دنباله از نویسه‌ها که با فاصله جدا شده است.
6. جمله یعنی هر دنباله که با `.` یا `!` یا `?` تمام شود.

## شروع کار

پوشهٔ `readability` را بساز، واردش شو و `code readability.c` را اجرا کن. کد آغازین برای دانلود ندارد.

## نمونه‌های رسمی ورودی و خروجی

فرمول رسمی Coleman-Liau:

```text
index = 0.0588 * L - 0.296 * S - 15.8
```

## متن‌های آزمون رسمی

صفحهٔ رسمی این متن‌ها و پایهٔ مورد انتظارشان را برای آزمودن برنامه فهرست می‌کند:

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

- سطح خوانایی متن — [یادداشت](/kb/d/w02-n02) · درس کوتاه `w02-l01` (واحد `w02-l01-u01`)
- رشته، آرایه‌ای از char — [یادداشت](/kb/d/w02-n12) · درس کوتاه `w02-l06` (واحد `w02-l06-u02`)
- strlen و string.h — [یادداشت](/kb/d/w02-n14) · درس کوتاه `w02-l07` (واحد `w02-l07-u02`)
- کتابخانهٔ ctype.h: islower و toupper — [یادداشت](/kb/d/w02-n15) · درس کوتاه `w02-l07` (واحد `w02-l07-u04`)
- اجزای اعلان تابع: نوع بازگشتی، نام، فهرست آرگومان‌ها — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)
- آرایه به‌عنوان پارامتر تابع — [یادداشت](/kb/d/w02-n10) · درس کوتاه `w02-l05` (واحد `w02-l05-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. مسئله را به چند مسئلهٔ کوچک‌تر بشکن؛ صفحهٔ رسمی چهار گام پیشنهاد می‌کند.
2. برای هر شمارش یک تابع جدا در نظر بگیر؛ هر تابع یک رشته می‌گیرد و یک عدد برمی‌گرداند.
3. برای تشخیص حرف بودن یک نویسه، صفحه‌های manual.cs50.io دربارهٔ ctype.h را بگرد.
4. با فرض‌های صفحهٔ رسمی (بدون فاصلهٔ پشت سر هم)، چه رابطه‌ای بین تعداد واژه‌ها و تعداد فاصله‌ها هست؟
5. تقسیم دو int در C اعشار را دور می‌ریزد. یادداشت scores3 و `(float)` را دوباره ببین.
6. برای گرد کردن، صفحهٔ رسمی تابعی از math.h را نام می‌برد.

## اشتباه‌های رایج

- تقسیم int بر int و از دست رفتن اعشار
- شمردن رقم یا علامت به‌عنوان حرف
- فراموش کردن گرد کردن
- چاپ `Grade 0` به‌جای `Before Grade 1`
- کپی کردن متن آزمون با فاصلهٔ اضافه

## چک‌لیست خودآزمایی

1. فایل در پوشهٔ درست است.
2. خروجی دقیقاً `Grade X` با X گردشده است.
3. حالت `Grade 16+` را امتحان کرده‌ام.
4. حالت `Before Grade 1` را امتحان کرده‌ام.
5. واژهٔ خط‌تیره‌دار مثل sister-in-law یک واژه شمرده می‌شود.
6. همهٔ متن‌های آزمون صفحهٔ رسمی پایهٔ درست می‌دهند.
7. check50 همه را سبز نشان می‌دهد.
8. style50 تغییری پیشنهاد نمی‌کند.
9. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/readability
```

سبک با style50:

```bash
style50 readability.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/readability
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [کد گام‌به‌گام «Advice» صفحهٔ رسمی](https://cs50.harvard.edu/x/psets/2/readability/#advice): این بخش ساختار کامل برنامه و توابع را نشان می‌دهد و به راه‌حل بسیار نزدیک است؛ در این بسته فقط پیوند داده شده است.
- [ویدئوی راهنمای گام‌به‌گام](https://www.youtube.com/watch?v=AOVyZEh9zgE): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/AOVyZEh9zgE)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj)

## پیوند رسمی

- [Readability](https://cs50.harvard.edu/x/2026/psets/2/readability/)
- [پرابلم‌ست ۲](https://cs50.harvard.edu/x/psets/2/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
