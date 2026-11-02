---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-ps-inheritance
type: problem-set-guide
title: راهنمای وراثت گروه خونی (Inheritance)
title_fa: وراثت گروه خونی (Inheritance)
title_en: Inheritance
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/5/inheritance/
source_refs:
- src-pset-5-inheritance#implementation-details
- src-pset-5-inheritance#hints
- src-anzali-authored-5
- src-pset-5#what-to-do
concept_ids:
- w05-c-blood-type-alleles
- w05-c-struct-pointer-array
- w05-c-self-referential-struct
- w05-c-arrow-operator
- w05-c-random-modulo
- w05-c-tree
- w05-c-bst-search
- w05-c-free-list
- w05-c-unload-on-error
problem_set_ref: weeks/week-05/problem-sets/inheritance.json
prev: w05-sh-data-structures
next: w05-ps-speller
order: 23
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای وراثت گروه خونی (Inheritance)

> **منبع رسمی:** [Inheritance](https://cs50.harvard.edu/x/2026/psets/5/inheritance/) از پرابلم‌ست ۵ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

گروه خونی هر فرد را دو **آلل** (دو شکل از یک ژن) تعیین می‌کند. سه آلل ممکن A، B و O است و هر فرد دو تا از آن‌ها دارد (شاید یکسان، شاید متفاوت). هر والد یکی از دو آلل خود را به‌تصادف به فرزند می‌دهد؛ پس ترکیب‌های ممکن OO، OA، OB، AO، AA، AB، BO، BA و BB هستند.

مثلاً اگر یک والد AO و دیگری BB باشد، فرزند AB یا OB می‌شود. در این مسئله `inheritance.c` را کامل می‌کنی تا برای یک خانوادهٔ سه‌نسلی، هر فرد را با `malloc` بسازد، والدهایش را به او وصل کند و گروه خونی‌اش را شبیه‌سازی کند، و در پایان همهٔ حافظه را آزاد کند.

در کد آغازین، هر `person` آرایه‌ای از دو اشاره‌گر به والدهایش (`parents`) و آرایه‌ای از دو نویسه برای آلل‌ها (`alleles`) دارد. `main` آماده است: مولد عدد تصادفی را مقداردهی می‌کند، `create_family` را صدا می‌زند، درخت خانواده را چاپ می‌کند و `free_family` را صدا می‌زند. بدنهٔ `create_family` و `free_family` با توضیح‌های `TODO` چارچوب‌بندی شده است (کد آغازین حتی دو فراخوانی بازگشتی برای ساختن والدها را دارد)؛ تکمیل این `TODO`ها با توست.

> **از سخنرانی:** ساختار خودارجاع و عملگر `->` در [یادداشت گره‌ها](/kb/d/w05-n07)، آزاد کردن تک‌تک گره‌ها در [یادداشت آزادسازی](/kb/d/w05-n09) و ساختار درختی با جست‌وجوی بازگشتی در [یادداشت درخت‌ها](/kb/d/w05-n10) آمده‌اند. بازگشت را از [هفتهٔ ۳](/kb/d/w03-fa) به یاد داری.

## خواسته‌های رسمی

1. `inheritance.c` را در پوشهٔ `inheritance` کامل کن تا خانواده‌ای با تعداد نسل مشخص بسازد و به هر عضو آلل‌های گروه خونی بدهد.
2. آلل‌های قدیمی‌ترین نسل به‌تصادف تعیین می‌شوند.
3. `create_family` یک عدد صحیح (`generations`) می‌گیرد، برای هر عضو خانواده یک `person` با `malloc` می‌سازد و اشاره‌گری به فرد جوان‌ترین نسل برمی‌گرداند.
4. مثلاً `create_family(3)` اشاره‌گری به فردی با دو والد برمی‌گرداند که هر والد هم دو والد دارد.
5. قدیمی‌ترین نسل آلل‌هایش را با `random_allele` می‌گیرد؛ نسل‌های جوان‌تر از هر والد یک آلل (به‌تصادف) به ارث می‌برند.
6. در قدیمی‌ترین نسل هر دو `parents` برابر `NULL` است؛ در نسل‌های جوان‌تر `parents` دو اشاره‌گر به دو والد متفاوت است.
7. `free_family` اشاره‌گری به یک `person` می‌گیرد، حافظهٔ او و به‌صورت بازگشتی حافظهٔ همهٔ نیاکانش را آزاد می‌کند.

> **توجه:** صفحهٔ رسمی می‌گوید `random()` عددی بین `0` و `RAND_MAX`، «یعنی `32767`»، برمی‌گرداند. `32767` فقط کمینهٔ مجاز استاندارد C است؛ در محیط cs50.dev (glibc) مقدار `RAND_MAX` برابر `2147483647` است. برای این مسئله فرقی نمی‌کند، چون فقط باقی‌ماندهٔ تقسیم بر ۲ لازم است (ناهمخوانی d89).

## شروع کار

در ترمینال cs50.dev اول `cd` را تنها اجرا کن، بعد فایل‌های آغازین را دانلود کن. در پوشه فقط `inheritance.c` هست. پیش از نوشتن، کل فایل را بخوان: تعریف `person`، ثابت `GENERATIONS`، `main`، `print_family` و `random_allele` آماده‌اند و `TODO`ها فقط در `create_family` و `free_family` هستند.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2026/x/psets/5/inheritance.zip
unzip inheritance.zip
rm inheritance.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd inheritance
```

## نمونه‌های رسمی ورودی و خروجی

نمونهٔ رسمی خروجی برای خانوادهٔ سه‌نسلی:

```text
$ ./inheritance
Child (Generation 0): blood type OO
    Parent (Generation 1): blood type AO
        Grandparent (Generation 2): blood type OA
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OB
        Grandparent (Generation 2): blood type AO
        Grandparent (Generation 2): blood type BO
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- گروه خونی با دو آلل؛ فرزند از هر والد یکی می‌گیرد — [یادداشت](/kb/d/w05-ps-inheritance)
- آرایه‌ای از اشاره‌گر در struct (parents[2]) — [یادداشت](/kb/d/w05-ps-inheritance)
- struct خودارجاع: struct node *next — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u01`)
- عملگر پیکان -> : رفتن به نشانی و نگاه به فیلد — [یادداشت](/kb/d/w05-n07) · درس کوتاه `w05-l03` (واحد `w05-l03-u02`)
- random() % 2 برای انتخاب ۰ یا ۱ — [یادداشت](/kb/d/w05-ps-inheritance)
- درخت: گره‌هایی با فرزند — [یادداشت](/kb/d/w05-n10) · درس کوتاه `w05-l06` (واحد `w05-l06-u01`)
- جست‌وجوی بازگشتی در درخت — [یادداشت](/kb/d/w05-n10) · درس کوتاه `w05-l06` (واحد `w05-l06-u02`)
- آزاد کردن کل فهرست با next موقت — [یادداشت](/kb/d/w05-n09) · درس کوتاه `w05-l05` (واحد `w05-l05-u03`)
- آزادسازی در مسیر خطا هم (unload) — [یادداشت](/kb/d/w05-n09) · درس کوتاه `w05-l05` (واحد `w05-l05-u03`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول خروجی رسمی را با تعریف `person` تطبیق بده: هر خط یک `person` است و تورفتگی نسل را نشان می‌دهد. چند `person` برای سه نسل لازم است؟
2. کد آغازین دو فراخوانی بازگشتی را آماده دارد. از خودت بپرس: هر فراخوانی چه چیزی برمی‌گرداند، و پس از آن‌ها چه کارهایی برای فرد فعلی مانده است؟ کِی دیگر نسلی برای ساختن نمی‌ماند (حالت پایه)؟
3. دو حالت را از هم جدا کن: فردی که هنوز نسل‌هایی پشت سرش هست، و فردی در قدیمی‌ترین نسل. در هر حالت `parents` و `alleles` باید چه باشند؟ خواسته‌های ۵ و ۶ را دوباره بخوان.
4. برای انتخاب تصادفی یکی از دو آلل یک والد، به عددی نیاز داری که فقط ۰ یا ۱ باشد. صفحهٔ رسمی تابعی را برای این کار نام می‌برد. یادداشت گره‌ها را برای دسترسی به فیلدِ آرایه‌ای از راه اشاره‌گر مرور کن.
5. برای `free_family` از خودت بپرس: اگر اول خود فرد را آزاد کنی، هنوز می‌توانی به والدهایش برسی؟ ترتیب درست آزاد کردن در یادداشت آزادسازی فهرست هم همین منطق را دارد.
6. حالت پایهٔ `free_family` را فراموش نکن: والدهای قدیمی‌ترین نسل `NULL` هستند.
7. بعد از کامل کردن هر تابع، برنامه را چند بار اجرا کن و آلل‌ها را با دست بررسی کن. سپس `valgrind` را اجرا کن.

## اشتباه‌های رایج

- آزاد کردن فرزند پیش از والدهایش و از دست دادن اشاره‌گرها به آن‌ها
- فراموش کردن حالت پایه و رفتن به نشانی `NULL` (segfault)
- دادن آلل تصادفی به همهٔ نسل‌ها، نه فقط قدیمی‌ترین
- برداشتن هر دو آلل فرزند از یک والد
- مقداردهی نکردن `parents` در نسل آخر
- نسنجیدن نتیجهٔ `malloc`

## چک‌لیست خودآزمایی

1. فقط `TODO`های `create_family` و `free_family` را عوض کرده‌ام؛ بقیهٔ کد آغازین دست‌نخورده است.
2. خروجی سه نسل دارد: یک فرزند، دو والد و چهار پدربزرگ و مادربزرگ.
3. آلل‌های نسل آخر (پدربزرگ‌ها و مادربزرگ‌ها) تصادفی‌اند و در هر اجرا ممکن است عوض شوند.
4. هر آلل هر فرد در نسل‌های جوان‌تر واقعاً از یکی از دو آلل والد مربوط آمده است.
5. والدهای نسل آخر `NULL` هستند و پیش از استفاده از اشاره‌گر، `NULL` نبودنش را می‌سنجم.
6. هر `person` با `malloc` ساخته شده و نتیجهٔ `malloc` را سنجیده‌ام.
7. `free_family` پیش از آزاد کردن هر فرد، نیاکانش را آزاد می‌کند و با `NULL` درست برمی‌گردد.
8. `valgrind ./inheritance` هیچ نشت یا خطای حافظه نشان نمی‌دهد.
9. check50 همه را سبز نشان می‌دهد.
10. style50 تغییری پیشنهاد نمی‌کند.
11. با submit50 تحویل داده‌ام.

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/problems/2026/x/inheritance
```

سبک با style50:

```bash
style50 inheritance.c
```

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/inheritance
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های رسمی «Complete the create_family function» و «Complete the free_family function»](https://cs50.harvard.edu/x/2026/psets/5/inheritance/#hints): کد این راهنمایی‌ها عملاً بدنهٔ کامل دو تابع خواسته‌شده است؛ فقط پیوند (D33).
- [ویدئوی راهنمای گام‌به‌گام](https://video.cs50.io/9p7ddI3ozTY): ویدئوی رسمی؛ فقط پیوند.

## ویدئو و نمایش

- [معرفی مسئله](https://youtu.be/xfZhb6lmxjk)
- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/9p7ddI3ozTY)
- [نمایش ترمینال (asciinema)](https://asciinema.org/a/J9DnbdokgIAjWUbzC2CBqP22N)

## پیوند رسمی

- [Inheritance](https://cs50.harvard.edu/x/2026/psets/5/inheritance/)
- [پرابلم‌ست ۵](https://cs50.harvard.edu/x/psets/5/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
