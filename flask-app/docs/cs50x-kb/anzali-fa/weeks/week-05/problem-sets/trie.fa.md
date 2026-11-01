---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-pr-trie
type: practice-guide
title: راهنمای نام سگ‌ها در ترای (Trie)
title_fa: نام سگ‌ها در ترای (Trie)
title_en: Trie
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/trie/
source_refs:
- src-practice-trie#background
- src-practice-trie#implementation-details
- src-anzali-authored-5
concept_ids:
- w05-c-trie
- w05-c-trie-lookup
- w05-c-trie-memory
- w05-c-list-null-end
- w05-c-case-insensitive
problem_set_ref: weeks/week-05/problem-sets/trie.json
prev: w05-ps-speller
next: null
order: 25
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای نام سگ‌ها در ترای (Trie)

> **منبع رسمی:** [Trie](https://cs50.harvard.edu/x/2026/practice/trie/) از مسئله‌های تمرینی هفتهٔ ۵ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

تازه سگی را از پناهگاه آورده‌ای و دنبال اسم برایش هستی. فایلی با حدود ۱۵۰ اسم پرطرفدار سگ پیدا کرده‌ای و می‌خواهی ببینی اسم‌هایی که در ذهن داری در این فهرست هستند یا نه. چون ترای برای جست‌وجو عالی است، کد تقریباً کاملی در `trie.c` به تو داده شده است.

در کد آغازین، ترای از چند `struct` به نام `node` ساخته شده است؛ هر گره آرایه‌ای ۲۶تایی از فرزندان بالقوه دارد، یکی برای هر حرف. هنگام افزودن اسم‌ها، برای هر حرف گرهٔ فرزند تازه‌ای ساخته می‌شود و روی آخرین حرف، فیلد `is_word` برابر `true` می‌شود. تنها تابعی که باید بنویسی `check` است.

> **از سخنرانی:** ترای، آرایهٔ `children[26]` و جست‌وجوی حرف به حرف در [یادداشت ترای‌ها](/kb/d/w05-n12) و ویدئوی کوتاه [ترای‌ها](/kb/d/w05-sh-tries) آمده‌اند.

## خواسته‌های رسمی

1. تابع `check` را در `trie.c` کامل کن.
2. بررسی یک اسم یعنی دنبال کردن حرف‌های آن در ترای؛ اگر به حرف آخر رسیدی و `is_word` درست بود، اسم در ترای هست.
3. جست‌وجو باید به بزرگی و کوچکی حروف حساس نباشد: `A` و `a` هر دو به ۰ می‌رسند، `B` و `b` به ۱ و الی آخر.

> **توجه:** نشانی دانلود این مسئله از آزمایشگاه‌های پاییز ۲۰۲۲ (`2022/fall/labs/5`) است، نه از مسیر ۲۰۲۶. صفحهٔ رسمی هم می‌گوید این مسئله check50 ندارد (ناهمخوانی d93).

## شروع کار

در ترمینال cs50.dev اول `cd` را تنها اجرا کن، بعد فایل آغازین را با فرمان بالا دانلود کن و با `cd trie` وارد پوشه شو. پوشه `trie.c` و `dog_names.txt` (۱۵۱ اسم) دارد. پیش از نوشتن، ببین کد آغازین چطور اسم‌ها را در ترای می‌گذارد؛ `check` تقریباً همان مسیر را می‌رود.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/5/trie.zip
unzip trie.zip
rm trie.zip
```

## نمونه‌های رسمی ورودی و خروجی

اسمی که در فهرست هست:

```text
trie/ $ ./trie dog_names.txt
Check word: Molly
Found!
```

اسم دیگری که در فهرست هست:

```text
trie/ $ ./trie dog_names.txt
Check word: Lucy
Found!
```

اسمی که در فهرست نیست:

```text
trie/ $ ./trie dog_names.txt
Check word: Prudence
Not Found.
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- ترای: درختی از آرایه‌ها — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- جست‌وجو در ترای: حرف به حرف، مستقل از تعداد کلمه‌ها — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- هزینهٔ حافظهٔ ترای — [یادداشت](/kb/d/w05-n12) · درس کوتاه `w05-l07` (واحد `w05-l07-u03`)
- NULL پایان فهرست را نشان می‌دهد — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- مقایسهٔ بی‌حساس به حروف بزرگ و کوچک (strcasecmp) — [یادداشت](/kb/d/w05-ps-speller)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. از ریشهٔ ترای شروع کن و برای حرکت یک اشاره‌گر جداگانه به کار ببر تا ریشه را گم نکنی.
2. برای هر حرف اسم، باید بدانی کدام خانهٔ آرایهٔ فرزندان مال آن است. حرف بزرگ و کوچک باید به یک خانه برسند.
3. در هر گام دو حالت داری: فرزند آن حرف وجود ندارد، یا وجود دارد. هر حالت دربارهٔ وجود اسم چه می‌گوید؟
4. رسیدن به حرف آخر کافی نیست؛ به یادداشت ترای و مثال bat و batch در ویدئوی کوتاه فکر کن.
5. صفحهٔ رسمی راهنمایی‌های گام‌به‌گام دقیق‌تری دارد؛ اگر گیر کردی آن‌ها را آن‌جا بخوان.

## اشتباه‌های رایج

- حرکت دادن خود اشاره‌گر ریشه به‌جای یک اشاره‌گر کمکی
- محاسبهٔ اندیس فقط برای حروف کوچک
- رفتن به نشانی فرزندی که `NULL` است
- برگرداندن «پیدا شد» فقط با رسیدن به حرف آخر، بدون سنجیدن `is_word`

## چک‌لیست خودآزمایی

1. فقط تابع `check` را نوشته‌ام.
2. `Molly` و `Lucy` پیدا می‌شوند و `Prudence` نه.
3. `molly` و `MOLLY` هم پیدا می‌شوند.
4. اگر در میانهٔ مسیر به `NULL` برسم، بدون رفتن به آن نشانی «پیدا نشد» برمی‌گردانم.
5. پیشوند یک اسم (اگر خودش اسم نباشد) «پیدا نشد» است، چون `is_word` را می‌سنجم.
6. style50 تغییری پیشنهاد نمی‌کند.
7. به پرسش فکری پاسخ داده‌ام.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با نمونه‌های رسمی بالا خودت آزمایش کن.

سبک با style50:

```bash
style50 trie.c
```

این مسئله تحویل ندارد.

## پرسش فکری

صفحهٔ رسمی می‌پرسد: چه وقت ممکن است بخواهی از ترای به‌عنوان ساختمان داده استفاده کنی؟ چه وقت نه؟

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های گام‌به‌گام رسمی (Hints در Implementation Details)](https://cs50.harvard.edu/x/2026/practice/trie/#implementation-details): این راهنمایی‌ها تقریباً همهٔ گام‌های `check` را می‌گویند؛ این بسته فقط در سطح کلی بازنویسی‌شان کرده است (D37).

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/JukHED1VvaJLFHMJbIvLksgF1)

## پیوند رسمی

- [Trie](https://cs50.harvard.edu/x/2026/practice/trie/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
