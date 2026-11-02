---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-fa
type: week-overview
title: هفتهٔ ۴ — حافظه (پایگاه دانش فارسی)
title_fa: هفتهٔ ۴ — حافظه
title_en: Week 4 — Memory
parent: week-4
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/4/
source_refs:
- src-week-4#week-4-memory
- src-notes-4#lecture-4
- src-pset-4#what-to-do
- src-pset-4#when-to-do-it
- src-short-call-stacks
- src-anzali-authored-4
- src-anzali-inference-4
children:
- w04-n01
- w04-n02
- w04-n03
- w04-n04
- w04-n05
- w04-n06
- w04-n07
- w04-n08
- w04-n09
- w04-n10
- w04-n11
- w04-n12
- w04-n13
- w04-n14
- w04-n15
- w04-summary
- w04-sec
- w04-sh-hexadecimal
- w04-sh-pointers
- w04-sh-defining-custom-types
- w04-sh-dynamic-memory-allocation
- w04-sh-file-pointers
- w04-ps-volume
- w04-ps-filter-less
- w04-ps-filter-more
- w04-ps-recover
- w04-pr-bottomup
- w04-pr-license
objective_ids:
- w04-o01
- w04-o02
- w04-o03
- w04-o04
- w04-o05
- w04-o06
- w04-o07
- w04-o08
- w04-o09
- w04-o10
cross_links:
- id: w03-sh-call-stacks
  reason: Call Stacks short is listed on both the week 3 and week 4 pages; covered once in week 3 (d67)
---

# هفتهٔ ۴ — حافظه

> **منبع رسمی:** [صفحهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/weeks/4/) و [درس‌نامهٔ هفتهٔ ۴](https://cs50.harvard.edu/x/notes/4/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

تا هفتهٔ ۳ با متغیر، آرایه، رشته و `struct` کار کردی و کتابخانهٔ CS50 خیلی از جزئیات را از چشمت پنهان می‌کرد. این هفته آن پرده کنار می‌رود: هر متغیر جایی در **حافظه** دارد، آن جا **نشانی** دارد و تو می‌توانی آن نشانی را نگه داری، جابه‌جا کنی و از طریقش مقدار را تغییر بدهی.

هفته با هنر پیکسلی و **مبنای شانزده** (هگزادسیمال) شروع می‌شود، زبانی که برنامه‌نویس‌ها برای رنگ‌ها و نشانی‌های حافظه به کار می‌برند. بعد **اشاره‌گر** (`pointer`) را می‌بینی و دو عملگر `&` و `*` را. معلوم می‌شود `string` در واقع `char *` است، و برای همین `==` رشته‌ها را مقایسه نمی‌کند و `t = s` رشته را کپی نمی‌کند. برای کپی واقعی حافظه را با `malloc` می‌گیری و با `free` پس می‌دهی، و با `valgrind` خطاهای حافظه را پیدا می‌کنی. سپس جابه‌جایی دو مقدار با اشاره‌گر، چیدمان حافظه (پشته و هیپ)، سرریز، `scanf` و در پایان **ورودی و خروجی فایل** با `fopen`، `fread` و `fwrite` می‌آیند؛ پایهٔ کار با تصویر و صدا در پرابلم‌ست ۴.

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

اشاره‌گرها (Pointers). خطای قطعه‌بندی (Segmentation Faults). تخصیص پویای حافظه (Dynamic Memory Allocation). پشته (Stack). هیپ (Heap). سرریز بافر (Buffer Overflow). ورودی و خروجی فایل (File I/O). تصویرها (Images).

> **توجه:** صفحهٔ هفته شش ویدئوی کوتاه فهرست می‌کند. ویدئوی «Call Stacks» همان ویدئویی است که در هفتهٔ ۳ آمده؛ این بسته آن را تکرار نمی‌کند و به [خلاصهٔ هفتهٔ ۳](/kb/d/w03-sh-call-stacks) پیوند می‌دهد (ناهمخوانی d67).

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه، سخنرانی، جلسهٔ حل تمرین و پرابلم‌ست ۴ استخراج کرده است.

- **w04-o01** — عدد را بین مبنای ده، دو و شانزده تبدیل کنی، بدانی چرا دو رقم هگزادسیمال دقیقاً یک بایت است و رنگ RGB مثل `#FF0000` را بخوانی.
- **w04-o02** — حافظه را دنباله‌ای از بایت‌های نشانی‌دار ببینی و نشانی یک متغیر را با `&` و `%p` چاپ کنی.
- **w04-o03** — اشاره‌گر بسازی، با `*` به مقدار مقصدش بروی و فرق `int *p` (اعلان) و `*p` (رفتن به نشانی) را توضیح بدهی.
- **w04-o04** — توضیح بدهی چرا `string` همان `char *` است، حساب اشاره‌گر را بفهمی (`s[i]` همان `*(s + i)`) و بدانی چرا `==` نشانی‌ها را مقایسه می‌کند و `strcmp` محتوا را.
- **w04-o05** — با `malloc` حافظه بگیری (با جای `\0`)، نتیجه را با `NULL` بسنجی، با `strcpy` کپی کنی و هر چیزی را که گرفتی با `free` پس بدهی.
- **w04-o06** — خروجی `valgrind` را بخوانی و «invalid write» و «definitely lost» را به خط مشخصی از کد نسبت بدهی.
- **w04-o07** — مقدار زباله و اشاره‌گر مقداردهی‌نشده را بشناسی و بدانی چرا ممکن است به segmentation fault برسند.
- **w04-o08** — جابه‌جایی دو مقدار را با فرستادن نشانی‌ها به تابع انجام بدهی و با تصویر پشته و هیپ توضیح بدهی چرا نسخهٔ بدون اشاره‌گر کار نمی‌کند.
- **w04-o09** — با `scanf` عدد بخوانی و خطر خواندن رشته با `scanf` را توضیح بدهی.
- **w04-o10** — فایل را با `fopen` باز کنی، `NULL` را بسنجی، با `fprintf`، `fread` و `fwrite` بنویسی و بخوانی، با `fclose` ببندی و ایدهٔ سرآیند و امضای فایل را توضیح بدهی.

## پیش‌نیازها

- هفتهٔ ۳: `struct` و `typedef`، تابع با پارامتر و مقدار برگشتی، پشتهٔ فراخوانی. ([نمای کلی هفتهٔ ۳](/kb/d/w03-fa))
- هفتهٔ ۲: آرایه، رشته به‌عنوان آرایه‌ای از نویسه‌ها با `\0` در پایان، `strlen` و آرگومان‌های خط فرمان. ([نمای کلی هفتهٔ ۲](/kb/d/w02-fa))
- هفتهٔ ۰: بیت، بایت و مبنای دو. ([نمای کلی هفتهٔ ۰](/kb/d/w00-fa))

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: نمایش داده و نشانی
  پیکسل و RGB -> مبنای شانزده (0x) -> بایت‌های نشانی‌دار

مرحلهٔ ۲: اشاره‌گر
  & (نشانی) -> int *p (اعلان) -> *p (رفتن به نشانی) -> NULL

مرحلهٔ ۳: رشته‌ها دوباره
  string = char * -> s + 1 و s[i] -> == نشانی را می‌سنجد، strcmp محتوا را
  t = s کپی نیست -> malloc(strlen(s) + 1) -> strcpy -> free

مرحلهٔ ۴: خطاهای حافظه
  valgrind (invalid write، definitely lost) -> مقدار زباله -> اشاره‌گر بی‌مقصد

مرحلهٔ ۵: پشته، هیپ و ورودی
  swap با نشانی‌ها -> پشته و هیپ -> سرریز -> scanf با &

مرحلهٔ ۶: فایل‌ها
  FILE * و fopen -> بررسی NULL -> fprintf / fread / fwrite -> fclose
  سرآیند فایل و امضا (WAV، BMP، JPEG)
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۵ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران (۷ درس).
3. ویدئوهای کوتاه (Shorts) را بعد از بخش مربوط ببین: [مبنای شانزده](/kb/d/w04-sh-hexadecimal)، [اشاره‌گرها](/kb/d/w04-sh-pointers)، [تعریف نوع‌های دلخواه](/kb/d/w04-sh-defining-custom-types)، [تخصیص پویای حافظه](/kb/d/w04-sh-dynamic-memory-allocation)، [پشتهٔ فراخوانی (هفتهٔ ۳)](/kb/d/w03-sh-call-stacks)، [اشاره‌گرهای فایل](/kb/d/w04-sh-file-pointers).
4. [جلسهٔ حل تمرین (Section)](/kb/d/w04-sec) را پیش از پرابلم‌ست ببین.
5. چالش‌های کوتاه هفته را امتحان کن، آزمون تسلط را بده و بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۴

طبق صفحهٔ رسمی پرابلم‌ست ۴:

- [Volume](/kb/d/w04-ps-volume) را **تحویل بده**.
- **یکی** از دو نسخهٔ Filter را تحویل بده: [Filter نسخهٔ آسان‌تر](/kb/d/w04-ps-filter-less) اگر کمتر احساس راحتی می‌کنی، یا [Filter نسخهٔ چالشی‌تر](/kb/d/w04-ps-filter-more) اگر بیشتر احساس راحتی می‌کنی.
- [Recover](/kb/d/w04-ps-recover) را **تحویل بده**.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

> **استنتاج:** صفحهٔ پرابلم‌ست ۴ نمی‌گوید اگر هر دو نسخهٔ Filter را تحویل بدهی چه می‌شود. این بسته فعلاً فرض می‌کند، مثل Runoff و Tideman در هفتهٔ ۳، نمرهٔ بالاتر ثبت می‌شود؛ این فرض تأیید رسمی ندارد (تصمیم D27).

مسئله‌های تمرینی اختیاری: [از پایین به بالا (Bottom Up)](/kb/d/w04-pr-bottomup)، [پلاک‌خوان (License)](/kb/d/w04-pr-license).

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود. راهنماها فقط مسئله را توضیح می‌دهند، مفاهیم لازم را به درس‌ها پیوند می‌دهند و چک‌لیست خودآزمایی دارند. صفحه‌های رسمی Volume، Filter و Recover بخش‌هایی از کد نزدیک به راه‌حل را در راهنمایی‌هایشان دارند؛ این بخش‌ها فقط پیوند داده شده‌اند (تصمیم D28).

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی پرابلم‌ست‌های انتخابی کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۴](https://cs50.harvard.edu/x/weeks/4/) · [درس‌نامه](https://cs50.harvard.edu/x/notes/4/) · [ویدئوی سخنرانی](https://video.cs50.io/db0H0U13YsA)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/4/lecture4.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/4/src4.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/4/lang/en/lecture4.srt)
- [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/4/) · [پرابلم‌ست ۴](https://cs50.harvard.edu/x/psets/4/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
