---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-ps-plurality
type: problem-set-guide
title: راهنمای انتخابات اکثریت نسبی (Plurality)
title_fa: انتخابات اکثریت نسبی (Plurality)
title_en: Plurality
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/3/plurality/
source_refs:
- src-pset-3-plurality#distribution-code
- src-pset-3-plurality#hints
- src-anzali-authored-3
- src-pset-3#what-to-do
concept_ids:
- w03-c-struct
- w03-c-dot-notation
- w03-c-array-of-structs
- w03-c-search-strings
- w03-c-strcmp-return
- w03-c-linear-search
- w03-c-big-o
problem_set_ref: weeks/week-03/problem-sets/plurality.json
prev: w03-ps-sort
next: w03-ps-runoff
order: 29
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای انتخابات اکثریت نسبی (Plurality)

> **منبع رسمی:** [Plurality](https://cs50.harvard.edu/x/2026/psets/3/plurality/) از پرابلم‌ست ۳ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

ساده‌ترین روش برگزاری انتخابات «رأی اکثریت نسبی» (plurality، که «first-past-the-post» یا «winner take all» هم نامیده می‌شود) است: هر رأی‌دهنده به یک نامزد رأی می‌دهد و هر کس بیشترین رأی را داشت برنده است.

کد آغازین `plurality.c` نامزدها را از آرگومان‌های خط فرمان در آرایه‌ای از struct `candidate` (با فیلدهای `name` و `votes`) می‌ریزد. تو فقط دو تابع `vote` و `print_winner` را کامل می‌کنی.

## خواسته‌های رسمی

1. فقط پیاده‌سازی `vote` و `print_winner` را تغییر بده (افزودن فایل سرآیند مجاز است).
2. `vote` نام نامزد را می‌گیرد و اگر رأی ثبت شد `true`، وگرنه `false` برمی‌گرداند.
3. `print_winner` نام نامزد با بیشترین رأی و بعد یک خط تازه چاپ کند.
4. در حالت تساوی، نام همهٔ برنده‌ها هر کدام در یک خط چاپ شود.

## شروع کار

فایل آغازین را با فرمان‌های رسمی دانلود کن، وارد پوشه شو و با `ls` ببین `plurality.c` آنجاست. پیش از نوشتن، `main` را بخوان: کجا نامزدها پر می‌شوند و کجا `vote` صدا زده می‌شود؟

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/3/plurality.zip
unzip plurality.zip
rm plurality.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd plurality
ls
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- ساختار داده با typedef struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- دسترسی به فیلدها با نماد نقطه — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- آرایه‌ای از struct — [یادداشت](/kb/d/w03-n09) · درس کوتاه `w03-l04` (واحد `w03-l04-u02`)
- جست‌وجو در آرایهٔ رشته‌ها با strcmp — [یادداشت](/kb/d/w03-n07) · درس کوتاه `w03-l03` (واحد `w03-l03-u02`)
- مقدار بازگشتی strcmp: صفر یعنی برابر — [یادداشت](/kb/d/w03-n07) · درس کوتاه `w03-l03` (واحد `w03-l03-u02`)
- جست‌وجوی خطی — [یادداشت](/kb/d/w03-n02) · درس کوتاه `w03-l01` (واحد `w03-l01-u02`)
- نماد O بزرگ: کران بالا یا بدترین حالت — [یادداشت](/kb/d/w03-n04) · درس کوتاه `w03-l02` (واحد `w03-l02-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. `vote` در اصل یک جست‌وجوست: دنبال نامی در آرایه‌ای از struct می‌گردی. کدام یادداشت این هفته همین کار را با شماره تلفن کرد؟
2. نام‌ها رشته‌اند. یادت هست چرا `==` در search.c کار نکرد؟
3. برای `print_winner` صفحهٔ رسمی می‌گوید لازم نیست مرتب کنی؛ دو چیز کافی است. آن دو چیز را با دو گذر جدا روی آرایه به دست بیاور.
4. تساوی را از اول در نظر بگیر: اگر چند نفر رأی برابرِ بیشینه دارند، طراحی‌ات باید بدون تغییر همه را چاپ کند.
5. با مثال‌های کوچک (سه نامزد، چهار رأی‌دهنده) هر دو حالت یک برنده و تساوی را با دست دنبال کن.

## اشتباه‌های رایج

- مقایسهٔ رشته‌ها با `==`
- برگرداندن `false` پیش از دیدن همهٔ نامزدها
- چاپ فقط یک برنده در حالت تساوی
- تغییر دادن `main` یا امضای توابع
- مرتب کردن آرایه در حالی که لازم نیست

## چک‌لیست خودآزمایی

1. فقط بدنهٔ `vote` و `print_winner` را تغییر داده‌ام.
2. رأی به نامی که در فهرست نیست ثبت نمی‌شود و `vote` مقدار `false` برمی‌گرداند.
3. یک برنده درست چاپ می‌شود.
4. تساوی چند نفره را امتحان کرده‌ام و همه چاپ می‌شوند.
5. انتخاباتی با ۹ نامزد (حداکثر `MAX`) را امتحان کرده‌ام.
6. check50 همه را سبز نشان می‌دهد.
7. style50 تغییری پیشنهاد نمی‌کند.
8. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/plurality
```

سبک با style50:

```bash
style50 plurality.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/plurality
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [شبه‌کد راهنمای `vote` و `print_winner` در «Hints» صفحهٔ رسمی](https://cs50.harvard.edu/x/psets/3/plurality/#hints): شبه‌کد رسمی گام‌های تابع را مستقیم نشان می‌دهد؛ برای اینکه اول خودت فکر کنی در این بسته بازتولید نشده است.
- [کد آغازین `plurality.c`](https://cs50.harvard.edu/x/psets/3/plurality/#distribution-code): کد رسمی را خودت دانلود و بخوان؛ اینجا تکرار نمی‌شود.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/ftOapzDjEb8)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/o2EXEqiz7iqfDB31wYxBOWjs8)

## پیوند رسمی

- [Plurality](https://cs50.harvard.edu/x/2026/psets/3/plurality/)
- [پرابلم‌ست ۳](https://cs50.harvard.edu/x/psets/3/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
