---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-fa
type: week-overview
title: هفتهٔ ۱ — C (پایگاه دانش فارسی)
title_fa: هفتهٔ ۱ — C
title_en: Week 1 — C
parent: week-1
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/1/
source_refs:
- src-week-1#week-1-c
- src-notes-1#lecture-1
- src-pset-1#what-to-do
- src-pset-1#when-to-do-it
- src-anzali-authored-1
children:
- w01-n01
- w01-n02
- w01-n03
- w01-n04
- w01-n05
- w01-n06
- w01-n07
- w01-n08
- w01-n09
- w01-n10
- w01-n11
- w01-n12
- w01-n13
- w01-n14
- w01-n15
- w01-n16
- w01-n17
- w01-n18
- w01-n19
- w01-summary
- w01-sec
- w01-sh-data-types
- w01-sh-operators
- w01-sh-conditional-statements
- w01-sh-loops
- w01-sh-command-line
- w01-sh-magic-numbers
- w01-ps-world
- w01-ps-me
- w01-ps-mario-less
- w01-ps-mario-more
- w01-ps-cash
- w01-ps-credit
- w01-pr-debug
- w01-pr-half
- w01-pr-prime
objective_ids:
- w01-o01
- w01-o02
- w01-o03
- w01-o04
- w01-o05
- w01-o06
- w01-o07
- w01-o08
- w01-o09
- w01-o10
- w01-o11
- w01-o12
---

# هفتهٔ ۱ — C

> **منبع رسمی:** [صفحهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/weeks/1/) و [درس‌نامهٔ هفتهٔ ۱](https://cs50.harvard.edu/x/notes/1/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

در هفتهٔ ۰ با بلوک‌های Scratch برنامه ساختی. در هفتهٔ ۱ همان بلوک‌های سازنده (تابع، شرط، حلقه و متغیر) را در زبان **C** می‌نویسی: یک زبان متنی که باید **کامپایل** (compile) شود تا کامپیوتر بتواند اجرایش کند.

درس‌نامه این هفته را «سیل‌آسا» (firehose) توصیف می‌کند: مفهوم‌های تازه زیادند و طبیعی است که همه یک‌باره جا نیفتند. سرعت را خودت تنظیم کن و هر بخش را با تمرین تثبیت کن.

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

C، کد منبع (Source Code)، کد ماشین (Machine Code)، کامپایلر (Compiler)، درستی، طراحی و سبک (Correctness, Design, Style)، Visual Studio Code، رنگ‌آمیزی نحو (Syntax Highlighting)، دنباله‌های گریز (Escape Sequences)، فایل‌های سرآیند (Header Files)، کتابخانه‌ها (Libraries)، صفحه‌های راهنما (Manual Pages)، انواع داده (Types)، شرط‌ها (Conditionals)، متغیرها (Variables)، حلقه‌ها (Loops)، لینوکس (Linux)، رابط گرافیکی (GUI)، رابط خط فرمان (CLI)، ثابت‌ها (Constants)، توضیح‌ها (Comments)، شبه‌کد (Pseudocode)، عملگرها (Operators)، سرریز عدد صحیح (Integer Overflow)، عدم دقت اعداد اعشاری (Floating-Point Imprecision).

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه و پرابلم‌ست ۱ استخراج کرده است.

- **w01-o01** — توضیح بدهی کد منبع، کد ماشین و کامپایلر چیست و چرخهٔ `code` ← `make` ← `./` را اجرا کنی.
- **w01-o02** — با بخش‌های VS Code (کاوشگر فایل، ویرایشگر، ترمینال) و فرمان‌های پایهٔ لینوکس کار کنی.
- **w01-o03** — با `printf`، دنبالهٔ گریز `\n` و نحو C (نقطه‌ویرگول، پرانتز، آکولاد) خروجی بسازی.
- **w01-o04** — نقش فایل سرآیند، `#include` و کتابخانهٔ CS50 را بدانی و از صفحه‌های راهنما استفاده کنی.
- **w01-o05** — متغیر با نوع مناسب اعلان کنی و با کد قالب درست (`%i`، `%s`، `%c`، `%f`، `%li`) چاپ کنی.
- **w01-o06** — شرط‌ها را با `if`، `else if`، `else` و عملگرهای مقایسه‌ای و منطقی بنویسی.
- **w01-o07** — حلقه‌های `while`، `for` و `do while` را انتخاب و ردگیری کنی.
- **w01-o08** — ورودی کاربر را اعتبارسنجی کنی و تا دریافت ورودی معتبر دوباره بپرسی.
- **w01-o09** — تابع با پیش‌نمونه، پارامتر و مقدار بازگشتی تعریف کنی و حوزهٔ متغیر را توضیح بدهی.
- **w01-o10** — مسئله را به گام‌های کوچک بشکنی و با حلقهٔ تودرتو، ثابت و تابع کمکی طراحی بهتری بسازی.
- **w01-o11** — سرریز، بریدن در تقسیم صحیح، تبدیل نوع و عدم دقت اعشاری را تشخیص بدهی.
- **w01-o12** — کد را روی سه محور درستی، طراحی و سبک با `check50`، `design50` و `style50` بسنجی و پیام خطای کامپایلر را بخوانی.

## پیش‌نیازها

- هفتهٔ ۰: تابع، آرگومان، مقدار بازگشتی، شرط، حلقه، متغیر و انتزاع. ([نمای کلی هفتهٔ ۰](/kb/d/w00-fa))
- یک حساب GitHub برای ورود به cs50.dev و submit.cs50.io.

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum/learning-map.json` است.

```text
مرحلهٔ ۱: ابزار و نخستین برنامه
  کد منبع -> کامپایلر -> کد ماشین
  VS Code + ترمینال -> code / make / ./
  printf + \n + نحو C

مرحلهٔ ۲: ورودی، متغیر و نوع
  #include + کتابخانه -> get_string / get_int
  متغیر + نوع -> کد قالب (%s %i %c %f %li)

مرحلهٔ ۳: کنترل جریان
  عملگرهای مقایسه‌ای و منطقی -> if / else if / else
  while -> for -> do while -> اعتبارسنجی ورودی

مرحلهٔ ۴: طراحی
  تابع + پیش‌نمونه + پارامتر + return -> حوزه
  حلقهٔ تودرتو + const + تابع کمکی (Mario)

مرحلهٔ ۵: محدودیت‌های ماشین
  اندازهٔ نوع -> سرریز
  تقسیم صحیح -> بریدن -> تبدیل نوع -> عدم دقت اعشاری
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۹ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران.
3. ویدئوهای کوتاه (Shorts) را بعد از بخش مربوط ببین: [انواع داده](/kb/d/w01-sh-data-types)، [عملگرها](/kb/d/w01-sh-operators)، [دستورهای شرطی](/kb/d/w01-sh-conditional-statements)، [حلقه‌ها](/kb/d/w01-sh-loops)، [خط فرمان](/kb/d/w01-sh-command-line)، [عددهای جادویی](/kb/d/w01-sh-magic-numbers).
4. [جلسهٔ حل تمرین (Section)](/kb/d/w01-sec) را پیش از پرابلم‌ست ببین.
5. آزمون تسلط هفته را بده، بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۱

طبق صفحهٔ رسمی پرابلم‌ست ۱:

- [Hello, World](/kb/d/w01-ps-world) را **انجام بده** (تحویل لازم نیست).
- [Hello, It's Me](/kb/d/w01-ps-me) را **تحویل بده**.
- **یکی** از دو نسخهٔ Mario را تحویل بده: [نسخهٔ آسان‌تر](/kb/d/w01-ps-mario-less) یا [نسخهٔ چالشی‌تر](/kb/d/w01-ps-mario-more).
- **یکی** از این دو را تحویل بده: [Cash](/kb/d/w01-ps-cash) یا [Credit](/kb/d/w01-ps-credit).
- اگر هر دو نسخه را تحویل بدهی، نمرهٔ بالاتر ثبت می‌شود.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

مسئله‌های تمرینی اختیاری: [Debug](/kb/d/w01-pr-debug)، [Half](/kb/d/w01-pr-half)، [Prime](/kb/d/w01-pr-prime).

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود. راهنماها فقط مسئله را توضیح می‌دهند، مفاهیم لازم را به درس‌ها پیوند می‌دهند و چک‌لیست خودآزمایی دارند.

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم.

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی پرابلم‌ست‌های انتخابی کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۱](https://cs50.harvard.edu/x/weeks/1/) · [درس‌نامه](https://cs50.harvard.edu/x/notes/1/) · [ویدئوی سخنرانی](https://video.cs50.io/SlqjA04_dpk)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/1/lecture1.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/1/src1.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/1/lang/en/lecture1.srt)
- [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/1/) · [پرابلم‌ست ۱](https://cs50.harvard.edu/x/psets/1/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
