---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-ps-filter-less
type: problem-set-guide
title: راهنمای فیلتر تصویر، نسخهٔ آسان‌تر (Filter less)
title_fa: فیلتر تصویر، نسخهٔ آسان‌تر (Filter less)
title_en: Filter (less comfortable)
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/4/filter/less/
source_refs:
- src-pset-4-filter-less#specification
- src-anzali-authored-4
- src-pset-4#what-to-do
concept_ids:
- w04-c-pixel-art
- w04-c-rgb-hex-color
- w04-c-hex-byte
- w04-c-bmp-rgbtriple
- w04-c-file-header
- w04-c-byte-type
- w04-c-typedef-struct
problem_set_ref: weeks/week-04/problem-sets/filter-less.json
prev: w04-ps-volume
next: w04-ps-filter-more
order: 24
submission: one-of-filter
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای فیلتر تصویر، نسخهٔ آسان‌تر (Filter less)

> **منبع رسمی:** [Filter (less comfortable)](https://cs50.harvard.edu/x/2026/psets/4/filter/less/) از پرابلم‌ست ۴ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** یکی از دو نسخهٔ Filter (آسان‌تر یا چالشی‌تر) را تحویل بده. صفحهٔ رسمی دربارهٔ تحویل هر دو چیزی نمی‌گوید (استنتاج D27: نمرهٔ بالاتر). مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

ساده‌ترین راه نمایش تصویر شبکه‌ای از پیکسل‌هاست. در BMP بیست‌وچهار بیتی، هر پیکسل ۸ بیت برای قرمز، ۸ بیت برای سبز و ۸ بیت برای آبی دارد؛ همان RGB. فایل BMP با دو سرآیند (`BITMAPFILEHEADER` با ۱۴ بایت و `BITMAPINFOHEADER` با ۴۰ بایت) شروع می‌شود و بعد پیکسل‌ها، به ترتیب BGR، می‌آیند.

کد آغازین فایل را می‌خواند، پیکسل‌ها را در آرایه‌ای دوبعدی از `RGBTRIPLE` به نام `image` می‌ریزد و بعد تابع فیلتر انتخابی را صدا می‌زند. تو فقط تابع‌های `helpers.c` را کامل می‌کنی: سیاه‌وسفید، قهوه‌ای قدیمی (sepia)، قرینه و محو.

> **از سخنرانی:** پیکسل، RGB و هگزادسیمال در [هنر پیکسلی](/kb/d/w04-n01) و [مبنای شانزده](/kb/d/w04-n02) آمدند؛ `struct` و `typedef` را از [هفتهٔ ۳](/kb/d/w03-n09) داری.

## خواسته‌های رسمی

1. تابع‌های `helpers.c` را طوری پیاده کن که کاربر بتواند فیلتر سیاه‌وسفید، sepia، قرینه یا محو را روی تصویر بزند.
2. `grayscale` نسخهٔ سیاه‌وسفید همان تصویر را بسازد.
3. `sepia` نسخهٔ sepia همان تصویر را بسازد.
4. `reflect` تصویر را افقی قرینه کند.
5. `blur` نسخهٔ box-blur همان تصویر را بسازد.
6. امضای تابع‌ها را تغییر نده و هیچ فایلی جز `helpers.c` را عوض نکن.

> **استنتاج:** صفحهٔ پرابلم‌ست ۴ فقط می‌گوید «یکی» از دو نسخهٔ Filter را تحویل بده و دربارهٔ تحویل هر دو چیزی نمی‌گوید. این بسته فرض می‌کند نمرهٔ بالاتر ثبت می‌شود (مثل Runoff و Tideman در هفتهٔ ۳)؛ این فرض تأیید رسمی ندارد (تصمیم D27).

## شروع کار

فایل‌های آغازین را با فرمان‌های رسمی دانلود کن. در پوشه `bmp.h`، `filter.c`، `helpers.h`، `helpers.c`، `Makefile` و پوشهٔ `images` هست. پیش از نوشتن، `bmp.h` را بخوان تا ببینی `RGBTRIPLE` چه فیلدهایی دارد، و در `filter.c` ببین کدام حرف خط فرمان کدام تابع را صدا می‌زند.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/4/filter-less.zip
unzip filter-less.zip
rm filter-less.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd filter-less
```

## نمونه‌های رسمی ورودی و خروجی

کامپایل (طبق Makefile):

```text
$ make filter
```

اجرای فیلتر سیاه‌وسفید روی یک تصویر نمونه:

```text
$ ./filter -g images/yard.bmp out.bmp
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- تصویر به‌شکل شبکه‌ای از پیکسل‌ها (هنر پیکسلی) — [یادداشت](/kb/d/w04-n01) · درس کوتاه `w04-l01` (واحد `w04-l01-u01`)
- رنگ RGB با سه عدد هگزادسیمال: #FF0000 — [یادداشت](/kb/d/w04-n02) · درس کوتاه `w04-l01` (واحد `w04-l01-u02`)
- هر رقم هگزادسیمال ۴ بیت است و دو رقم یک بایت؛ FF یعنی 255 — [یادداشت](/kb/d/w04-n02) · درس کوتاه `w04-l01` (واحد `w04-l01-u02`)
- BMP، RGBTRIPLE و ترتیب BGR — [یادداشت](/kb/d/w04-ps-filter-less) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)
- سرآیند فایل: فرادادهٔ ابتدای فایل (WAV و BMP) — [یادداشت](/kb/d/w04-ps-volume) · درس کوتاه `w04-l07` (واحد `w04-l07-u03`)
- نوع BYTE با typedef unsigned char — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)
- typedef همراه struct برای ساختن نوع دلخواه — [یادداشت](/kb/d/w04-sh-defining-custom-types) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. `image[i][j]` پیکسل سطر `i` و ستون `j` است و هر پیکسل سه فیلد `rgbtRed`، `rgbtGreen` و `rgbtBlue` دارد. همهٔ فیلترها با پیمایش همهٔ پیکسل‌ها شروع می‌شوند؛ دو حلقهٔ تودرتو.
2. مقدار مؤلفه‌ها عدد صحیح‌اند. اگر وسط محاسبه عدد اعشاری ساختی، پیش از ذخیره گرد کن؛ و اگر ممکن است از ۲۵۵ بیشتر شود، چه باید بکنی؟
3. برای قرینه: پیکسل ستون اول با ستون آخر جابه‌جا می‌شود. حلقه تا کجای سطر باید برود تا هر جفت فقط یک بار جابه‌جا شود؟ جابه‌جایی با متغیر موقت را از یادداشت swap داری.
4. برای محو (و لبه): اگر پیکسل‌ها را درجا عوض کنی، همسایهٔ بعدی مقدار عوض‌شده را می‌بیند. پیش از شروع به چه چیزی نیاز داری؟
5. در لبه‌ها و گوشه‌ها همسایه‌های کمتری هست. پیش از دسترسی به `image[i + 1]` بررسی کن که آن سطر وجود دارد.
6. صفحهٔ رسمی می‌گوید هر فیلتر را جدا روی تصویرهای نمونه امتحان کن. یک فیلتر را کامل کن، با `make filter` کامپایل کن، نتیجه را ببین و بعد سراغ بعدی برو.

## اشتباه‌های رایج

- تقسیم عدد صحیح بر عدد صحیح و از دست رفتن بخش اعشاری پیش از گرد کردن
- فراموش کردن محدود کردن مقدار به ۲۵۵
- قرینه کردن تا انتهای سطر، که پیکسل‌ها را دو بار جابه‌جا و به جای اول برمی‌گرداند
- محو با مقدارهایی که در همان گذر عوض شده‌اند
- دسترسی به اندیس منفی یا بیرون از تصویر در لبه‌ها
- تغییر فایلی جز `helpers.c`

## چک‌لیست خودآزمایی

1. فقط `helpers.c` را تغییر داده‌ام و امضای تابع‌ها همان است.
2. سیاه‌وسفید: هر سه مؤلفهٔ هر پیکسل برابرند و روشنایی کلی حفظ شده.
3. مقدار هر مؤلفه یک عدد صحیح بین ۰ تا ۲۵۵ است (گرد شده و در صورت نیاز محدود شده).
4. sepia: نتیجه را روی تصویر نمونه با چشم بررسی کرده‌ام.
5. قرینه: پیکسل‌های چپ و راست جابه‌جا شده‌اند و ستون میانی (اگر عرض فرد است) سر جایش مانده.
6. محو: میانگین هر پیکسل از مقدارهای **اصلی** همسایه‌ها حساب شده، نه مقدارهایی که همین حالا عوض کرده‌ام.
7. محو: پیکسل‌های لبه و گوشه فقط همسایه‌های موجود را شمرده‌اند.
8. همهٔ فیلترها را روی همهٔ تصویرهای نمونه امتحان کرده‌ام.
9. check50 همه را سبز نشان می‌دهد.
10. style50 تغییری پیشنهاد نمی‌کند.
11. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/filter/less
```

سبک با style50:

```bash
style50 helpers.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/filter/less
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های رسمی «Implement grayscale / sepia / reflect / blur»](https://cs50.harvard.edu/x/2026/psets/4/filter/less/#hints): کد اسکلت هر تابع و فرمول sepia در این بخش است؛ طبق سیاست بدون راه‌حل فقط پیوند داده شده (D28).
- [فهرست پخش ویدئوهای راهنمای Filter (۵ ویدئو)](https://www.youtube.com/playlist?list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough، اولین ویدئوی فهرست پخش)](https://youtu.be/K0v9byp9jd0)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/QnLel70SPmbW9nswXTb9Yu9ZD)

## پیوند رسمی

- [Filter (less comfortable)](https://cs50.harvard.edu/x/2026/psets/4/filter/less/)
- [پرابلم‌ست ۴](https://cs50.harvard.edu/x/psets/4/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
