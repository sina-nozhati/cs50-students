---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-fa
type: week-overview
title: هفتهٔ ۲ — آرایه‌ها (پایگاه دانش فارسی)
title_fa: هفتهٔ ۲ — آرایه‌ها
title_en: Week 2 — Arrays
parent: week-2
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/2/
source_refs:
- src-week-2#week-2-arrays
- src-notes-2#lecture-2
- src-pset-2#what-to-do
- src-pset-2#when-to-do-it
- src-anzali-authored-2
children:
- w02-n01
- w02-n02
- w02-n03
- w02-n04
- w02-n05
- w02-n06
- w02-n07
- w02-n08
- w02-n09
- w02-n10
- w02-n11
- w02-n12
- w02-n13
- w02-n14
- w02-n15
- w02-n16
- w02-n17
- w02-n18
- w02-summary
- w02-sec
- w02-sh-functions
- w02-sh-variables-and-scope
- w02-sh-debugging-step-through
- w02-sh-debugging-step-into
- w02-sh-arrays
- w02-sh-command-line-arguments
- w02-ps-scrabble
- w02-ps-readability
- w02-ps-caesar
- w02-ps-substitution
- w02-pr-hours
- w02-pr-no-vowels
- w02-pr-password
objective_ids:
- w02-o01
- w02-o02
- w02-o03
- w02-o04
- w02-o05
- w02-o06
- w02-o07
- w02-o08
- w02-o09
- w02-o10
- w02-o11
- w02-o12
---

# هفتهٔ ۲ — آرایه‌ها

> **منبع رسمی:** [صفحهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/weeks/2/) و [درس‌نامهٔ هفتهٔ ۲](https://cs50.harvard.edu/x/notes/2/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

در هفتهٔ ۱ با C برنامه نوشتی و `make` را مثل یک جعبهٔ سیاه به کار بردی. این هفته درِ آن جعبه را باز می‌کنیم: وقتی کامپایل می‌کنی دقیقاً چه اتفاقی می‌افتد؟ داده‌ها در حافظه چطور کنار هم می‌نشینند؟ و چرا یک «رشته» در واقع چیزی جز یک ردیف نویسه نیست؟

ابزار اصلی این هفته **آرایه** (`array`) است: مقدارهای هم‌نوع، پشت سر هم در حافظه. با آرایه می‌توانی نمره‌ها، حرف‌های یک متن یا آرگومان‌های خط فرمان را نگه داری و با یک حلقه روی همه‌شان کار کنی. در کنارش یاد می‌گیری باگ‌ها را با `printf`، `debug50` و اردک پلاستیکی پیدا کنی. هفته با **رمزنگاری** (`cryptography`) تمام می‌شود؛ همان چیزی که در پرابلم‌ست به کارش می‌بری.

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

پیش‌پردازش (Preprocessing)، کامپایل (Compiling)، اسمبل (Assembling)، پیوند (Linking)، اشکال‌زدایی (Debugging)، آرایه‌ها (Arrays)، رشته‌ها (Strings)، آرگومان‌های خط فرمان (Command-Line Arguments)، رمزنگاری (Cryptography).

> **توجه:** درس‌نامه اشکال‌زدایی را پیش از کامپایل می‌آورد و بخشی برای رمزنگاری ندارد؛ رمزنگاری فقط در سخنرانی آمده است (ناهمخوانی d23 و d24). ترتیب درس‌های این بسته از ترتیب سخنرانی پیروی می‌کند.

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه، سخنرانی، جلسهٔ حل تمرین و پرابلم‌ست ۲ استخراج کرده است.

- **w02-o01** — چهار مرحلهٔ کامپایل (پیش‌پردازش، کامپایل، اسمبل، پیوند) را توضیح بدهی و بدانی `make` چطور `clang` را با پرچم‌هایی مثل `-o` و `-lcs50` صدا می‌زند.
- **w02-o02** — پیام خطای کامپایل را بخوانی و از اولین خطا شروع به اصلاح کنی.
- **w02-o03** — با `printf`، `debug50` (نقطهٔ توقف، Step Over، Step Into) و اردک پلاستیکی باگ منطقی را پیدا کنی.
- **w02-o04** — بدانی هر نوع داده چند بایت حافظه می‌گیرد و حافظه را مثل یک شبکهٔ بایت‌ها تصور کنی.
- **w02-o05** — آرایه اعلان کنی، با اندیس از صفر به عنصرهایش دسترسی پیدا کنی و با حلقه رویش حرکت کنی، بی‌آنکه از مرزش بیرون بزنی.
- **w02-o06** — با ثابت سراسری اندازهٔ آرایه را تعیین کنی، آرایه را به تابع بفرستی و تفاوت متغیر محلی، سراسری و فراخوانی با مقدار را توضیح بدهی.
- **w02-o07** — نویسه را عددی در جدول ASCII ببینی و رشته را آرایه‌ای از نویسه‌ها که با `NUL` (`\0`) تمام می‌شود.
- **w02-o08** — طول رشته را با حلقه یا `strlen` حساب کنی و با آرایه‌ای از رشته‌ها کار کنی.
- **w02-o09** — بزرگی و کوچکی حرف را با حساب ASCII یا توابع `ctype.h` تغییر بدهی.
- **w02-o10** — ورودی را از خط فرمان با `argc` و `argv` بگیری و همیشه پیش از دسترسی به `argv[i]` تعداد را بسنجی.
- **w02-o11** — وضعیت خروج (`return 0` و `return 1`) را برگردانی و با `echo $?` بخوانی.
- **w02-o12** — متن ساده، کلید و متن رمز را توضیح بدهی، طراحی خوب (پرهیز از کار تکراری، عدد جادویی و `else` زائد) را به کار ببری و ایدهٔ سنجش سطح خوانایی را بفهمی.

## پیش‌نیازها

- هفتهٔ ۱: متغیر و نوع، شرط، حلقهٔ `for`، تابع با پارامتر و `return`، و چرخهٔ `code` ← `make` ← `./`. ([نمای کلی هفتهٔ ۱](/kb/d/w01-fa))
- آشنایی با کد قالب‌های `%i`، `%c` و `%s`.

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: باگ و کامپایل
  خطای کامپایل -> printf -> debug50 -> اردک
  make -> clang -> پیش‌پردازش / کامپایل / اسمبل / پیوند

مرحلهٔ ۲: حافظه و آرایه
  اندازهٔ نوع‌ها -> آرایه -> اندیس از صفر -> حلقه روی آرایه
  ثابت سراسری -> آرایه به‌عنوان آرگومان -> حوزه و فراخوانی با مقدار

مرحلهٔ ۳: نویسه و رشته
  char = عدد ASCII -> رشته = آرایهٔ نویسه + NUL
  طول رشته -> strlen -> بزرگ و کوچک -> ctype.h

مرحلهٔ ۴: خط فرمان و رمز
  argc / argv -> وضعیت خروج -> echo $?
  متن ساده + کلید -> متن رمز
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۸ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران.
3. ویدئوهای کوتاه (Shorts) را بعد از بخش مربوط ببین: [توابع](/kb/d/w02-sh-functions)، [متغیرها و حوزه](/kb/d/w02-sh-variables-and-scope)، [اجرای گام‌به‌گام](/kb/d/w02-sh-debugging-step-through)، [Step Into](/kb/d/w02-sh-debugging-step-into)، [آرایه‌ها](/kb/d/w02-sh-arrays)، [آرگومان‌های خط فرمان](/kb/d/w02-sh-command-line-arguments).
4. [جلسهٔ حل تمرین (Section)](/kb/d/w02-sec) را پیش از پرابلم‌ست ببین.
5. آزمون تسلط هفته را بده، بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۲

طبق صفحهٔ رسمی پرابلم‌ست ۲:

- [Scrabble](/kb/d/w02-ps-scrabble) را **تحویل بده**.
- [Readability](/kb/d/w02-ps-readability) را **تحویل بده**.
- **یکی** از این دو را تحویل بده: [Caesar](/kb/d/w02-ps-caesar) اگر کمتر احساس راحتی می‌کنی، یا [Substitution](/kb/d/w02-ps-substitution) اگر بیشتر.
- اگر هر دو را تحویل بدهی، نمرهٔ بالاتر ثبت می‌شود.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

مسئله‌های تمرینی اختیاری: [Hours](/kb/d/w02-pr-hours)، [No Vowels](/kb/d/w02-pr-no-vowels)، [Password](/kb/d/w02-pr-password).

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود. راهنماها فقط مسئله را توضیح می‌دهند، مفاهیم لازم را به درس‌ها پیوند می‌دهند و چک‌لیست خودآزمایی دارند.

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی پرابلم‌ست‌های انتخابی کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۲](https://cs50.harvard.edu/x/weeks/2/) · [درس‌نامه](https://cs50.harvard.edu/x/notes/2/) · [ویدئوی سخنرانی](https://video.cs50.io/h5Gc1n8ZuU8)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/2/lecture2.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/2/src2.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/2/lang/en/lecture2.srt)
- [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/2/) · [پرابلم‌ست ۲](https://cs50.harvard.edu/x/psets/2/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
