---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-ps-volume
type: problem-set-guide
title: راهنمای تغییر بلندی صدا (Volume)
title_fa: تغییر بلندی صدا (Volume)
title_en: Volume
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/4/volume/
source_refs:
- src-pset-4-volume#implementation-details
- src-anzali-authored-4
- src-pset-4#what-to-do
concept_ids:
- w04-c-file-pointer
- w04-c-fopen-null-check
- w04-c-fread-fwrite
- w04-c-fprintf-fclose
- w04-c-stdint-types
- w04-c-file-header
- w04-c-sizeof
- w04-c-address-of
- w04-c-memory-leak
problem_set_ref: weeks/week-04/problem-sets/volume.json
prev: w04-sh-file-pointers
next: w04-ps-filter-less
order: 23
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای تغییر بلندی صدا (Volume)

> **منبع رسمی:** [Volume](https://cs50.harvard.edu/x/2026/psets/4/volume/) از پرابلم‌ست ۴ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

فایل WAV صدا را به‌شکل دنباله‌ای از «نمونه‌ها» (sample) نگه می‌دارد: عددهایی که مقدار سیگنال صدا را در لحظه‌های پشت سر هم نشان می‌دهند. هر فایل WAV با یک **سرآیند** (header) ۴۴ بایتی شروع می‌شود که اطلاعاتی دربارهٔ خود فایل دارد، و بعد از آن نمونه‌ها می‌آیند.

اگر هر نمونه در یک ضریب ضرب شود، بلندی صدا عوض می‌شود: ضریب ۲ صدا را دو برابر بلند و ضریب ۰٫۵ آن را نصف می‌کند. در این مسئله `volume.c` را کامل می‌کنی تا یک فایل ورودی، یک فایل خروجی و یک ضریب بگیرد و نسخهٔ تغییریافته را بسازد.

> **از سخنرانی:** `fopen`، `fclose`، `fread` و `fwrite` را در [یادداشت ورودی و خروجی فایل](/kb/d/w04-n15) دیدی؛ نوع‌های اندازه‌دقیق مثل `uint8_t` و `int16_t` در خود صفحهٔ رسمی معرفی می‌شوند.

## خواسته‌های رسمی

1. برنامه سه آرگومان خط فرمان می‌گیرد: نام فایل ورودی، نام فایل خروجی و ضریب.
2. اول سرآیند را از فایل ورودی بخوان و در فایل خروجی بنویس.
3. بعد بقیهٔ داده را نمونه‌به‌نمونه (هر نمونه ۱۶ بیت، یعنی ۲ بایت) بخوان، در ضریب ضرب کن و در خروجی بنویس.
4. می‌توانی فرض کنی نمونه‌ها عدد علامت‌دار ۱۶ بیتی‌اند.
5. اگر از `malloc` استفاده کردی، نباید حافظه نشت کند.

## شروع کار

در ترمینال cs50.dev اول `cd` را تنها اجرا کن، بعد فایل‌های آغازین را دانلود کن. در پوشه باید `volume.c` و یک فایل نمونهٔ `input.wav` باشد. پیش از نوشتن، `volume.c` را بخوان: بررسی آرگومان‌ها، باز کردن دو فایل، تبدیل ضریب به `float` و بستن فایل‌ها از قبل نوشته شده‌اند و فقط دو `TODO` مانده است.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/4/volume.zip
unzip volume.zip
rm volume.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd volume
ls
```

## نمونه‌های رسمی ورودی و خروجی

دو برابر کردن بلندی صدا:

```text
$ ./volume input.wav output.wav 2.0
```

نصف کردن بلندی صدا:

```text
$ ./volume input.wav output.wav 0.5
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- FILE * و fopen با حالت r، w، a — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- بررسی NULL پس از fopen — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- fread و fwrite: خواندن و نوشتن بایت‌ها — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)
- fprintf برای نوشتن در فایل و fclose برای بستن — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- نوع‌های اندازه‌دقیق stdint.h: uint8_t و int16_t — [یادداشت](/kb/d/w04-ps-volume) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)
- سرآیند فایل: فرادادهٔ ابتدای فایل (WAV و BMP) — [یادداشت](/kb/d/w04-ps-volume) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)
- sizeof برای اندازهٔ یک نوع به بایت — [یادداشت](/kb/d/w04-n10) · درس کوتاه `w04-l05` (واحد `w04-l05-u01`)
- عملگر & : نشانی یک متغیر — [یادداشت](/kb/d/w04-n04) · درس کوتاه `w04-l02` (واحد `w04-l02-u01`)
- نشت حافظه: malloc بدون free — [یادداشت](/kb/d/w04-n10) · درس کوتاه `w04-l05` (واحد `w04-l05-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. فایل را دو بخش ببین: یک تکهٔ ثابت در ابتدا که باید دست‌نخورده کپی شود، و یک دنبالهٔ بلند از نمونه‌های هم‌اندازه. هر بخش یک `TODO` است.
2. برای سرآیند: چند بایت است، و چه نوعی دقیقاً یک بایت بدون علامت را نشان می‌دهد؟ صفحهٔ رسمی این را در `stdint.h` نشانت می‌دهد.
3. `fread` و `fwrite` چهار ورودی دارند: نشانی جایی که داده از آن‌جا یا به آن‌جا می‌رود، اندازهٔ هر قلم، تعداد قلم‌ها و فایل. برای هر بخش این چهار را روی کاغذ بنویس.
4. برای نمونه‌ها: هر بار فقط یک نمونه را در یک متغیر بخوان. یادداشت swap را به یاد بیاور: تابعی که باید مقدار متغیر تو را پر کند، به چه چیزی از آن متغیر نیاز دارد؟
5. کی باید خواندن را متوقف کنی؟ صفحهٔ راهنمای `fread` بگو چه برمی‌گرداند وقتی چیزی برای خواندن نماند.
6. اول با ضریب ۱ امتحان کن: خروجی باید دقیقاً مثل ورودی باشد. بعد ۲ و ۰٫۵ را بیازما.

## اشتباه‌های رایج

- دست زدن به سرآیند (ضرب کردن آن در ضریب)
- خواندن نمونه‌ها با نوعی که ۱۶ بیتی نیست
- خواندن فقط یک نمونه به‌جای همهٔ آن‌ها
- فرستادن خود متغیر به‌جای نشانی‌اش به `fread`
- فراموش کردن این‌که ضریب `float` است

## چک‌لیست خودآزمایی

1. برنامه با تعداد آرگومان نادرست پیام راهنما می‌دهد و ۱ برمی‌گرداند (کد آغازین؛ دست نزده‌ام).
2. ۴۴ بایت سرآیند بدون تغییر در خروجی نوشته می‌شود.
3. همهٔ نمونه‌ها، نه فقط اولی، خوانده و نوشته می‌شوند.
4. برای نمونه‌ها نوع ۱۶ بیتی علامت‌دار را به کار برده‌ام.
5. خروجی با ضریب ۲ بلندتر و با ضریب ۰٫۵ آرام‌تر شنیده می‌شود.
6. اگر `malloc` دارم، `valgrind` نشتی نشان نمی‌دهد.
7. check50 همه را سبز نشان می‌دهد.
8. style50 تغییری پیشنهاد نمی‌کند.
9. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/volume
```

سبک با style50:

```bash
style50 volume.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/volume
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های رسمی «Copy WAV header» و «Update a file’s volume»](https://cs50.harvard.edu/x/2026/psets/4/volume/#hints): این بخش‌ها کد کامل دو TODO را نشان می‌دهند؛ طبق سیاست بدون راه‌حل فقط پیوند داده شده‌اند (D28).
- [ویدئوی راهنمای گام‌به‌گام](https://video.cs50.io/LiGhjz9ColQ): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/LiGhjz9ColQ)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/mc2hPhYDt1spoMjlqNMuqC4Uc)

## پیوند رسمی

- [Volume](https://cs50.harvard.edu/x/2026/psets/4/volume/)
- [پرابلم‌ست ۴](https://cs50.harvard.edu/x/psets/4/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
