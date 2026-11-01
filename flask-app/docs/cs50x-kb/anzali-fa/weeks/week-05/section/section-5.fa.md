---
week: 5
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
generated_at: '2026-10-28T19:30:00+03:30'
review_status: draft-needs-human-review
id: w05-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۵ (Section 5)
title_fa: جلسهٔ حل تمرین هفتهٔ ۵
title_en: Section 5
parent: w05-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly, read in full); chapter times from section5.srt (inference for boundaries); list.c verbatim (lecture-pattern code, not a pset solution); hash.c link-only (two-letter hash function close to the Speller hash task, D35)
source_url: https://cs50.harvard.edu/x/sections/5/
source_refs:
- src-section-5#week-5-data-structures
- src-section-5-transcript
- src-section-5-video
- src-section-5-code
- src-anzali-inference-5
- src-anzali-authored-5
concept_ids:
- w05-c-structure-choice
- w05-c-time-space-tradeoff
- w05-c-node
- w05-c-linked-list
- w05-c-list-null-end
- w05-c-prepend
- w05-c-link-before-move
- w05-c-list-traversal
- w05-c-prepend-reverses
- w05-c-free-list
- w05-c-hash-table
- w05-c-hash-function
- w05-c-bucket
- w05-c-collision
- w05-c-good-hash-properties
prev: w05-summary
next: w05-sh-structures
order: 14
video:
  youtube_id: sLrnELP1nT0
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: خوش‌آمد و پرسش‌های جلسه
    evidence_en: null
  - start: '1:13'
    start_seconds: 73
    title_fa: 'سناریو: واژه‌های بیدارباش دستیار صوتی'
    evidence_en: digital assistant
  - start: '2:31'
    start_seconds: 151
    title_fa: 'عملیات اصلی: حذف، درج، جست‌وجو'
    evidence_en: primary operations
  - start: '3:34'
    start_seconds: 214
    title_fa: 'سه نامزد: فهرست پیوندی، جدول درهم‌سازی، ترای'
    evidence_en: linked list would look
  - start: '4:50'
    start_seconds: 290
    title_fa: 'Big Board: بده‌بستان زمان و حافظه'
    evidence_en: big board
  - start: '6:05'
    start_seconds: 365
    title_fa: گره چیست؟
    evidence_en: define a node like a struct
  - start: '6:54'
    start_seconds: 414
    title_fa: 'ساختن فهرست: NULL، malloc و next'
    evidence_en: how do we go about creating a linked list
  - start: '10:08'
    start_seconds: 608
    title_fa: 'تمرین: برنامهٔ list.c'
    evidence_en: program called List.c
  - start: '17:12'
    start_seconds: 1032
    title_fa: 'پرسش و پاسخ: عدد جادویی و شکست malloc'
    evidence_en: magic number
  - start: '18:16'
    start_seconds: 1096
    title_fa: افزودن گره به ابتدای فهرست
    evidence_en: inserting nodes
  - start: '21:19'
    start_seconds: 1279
    title_fa: چرا free(list) کافی نیست
    evidence_en: what is wrong with freeing just list
  - start: '23:31'
    start_seconds: 1411
    title_fa: پیمایش و چاپ فهرست
    evidence_en: try to print all of my nodes
  - start: '30:33'
    start_seconds: 1833
    title_fa: 'اجرا: ترتیب برعکس'
    evidence_en: first in, last out
  - start: '31:32'
    start_seconds: 1892
    title_fa: 'جدول درهم‌سازی: آرایه‌ای از فهرست‌ها'
    evidence_en: talk a bit about hash tables
  - start: '34:24'
    start_seconds: 2064
    title_fa: درهم‌سازی بر اساس طول
    evidence_en: different hash function
  - start: '35:20'
    start_seconds: 2120
    title_fa: ویژگی‌های تابع درهم‌ساز خوب
    evidence_en: good hash function has certain properties
  - start: '37:55'
    start_seconds: 2275
    title_fa: 'تمرین: برنامهٔ hash.c'
    evidence_en: create our own hash function
  - start: '43:33'
    start_seconds: 2613
    title_fa: حالت‌های مرزی
    evidence_en: issues with this function
  - start: '48:50'
    start_seconds: 2930
    title_fa: خطای prototype و اجرا
    evidence_en: undeclared function hash
  - start: '50:57'
    start_seconds: 3057
    title_fa: 'بهبود: دو حرف اول'
    evidence_en: small
  - start: '54:52'
    start_seconds: 3292
    title_fa: برخورد AC و BB و جمع‌بندی
    evidence_en: Multiply that by 100
  - start: '56:52'
    start_seconds: 3412
    title_fa: پایان جلسه
    evidence_en: moving to Python
  chapters_origin: inference
code_files:
- file: list.c
  policy: verbatim
- file: hash.c
  policy: link-only
  reason: two-letter hash function is the kind of improvement Speller asks students to design themselves (D35)
---

# جلسهٔ حل تمرین هفتهٔ ۵ (Section)

> **منبع رسمی:** [صفحهٔ Section 5 CS50x](https://cs50.harvard.edu/x/sections/5/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/5/lang/en/section5.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، مدرس (preceptor) CS50 در هاروارد، اداره می‌کند و سه پرسش را دنبال می‌کند: بده‌بستان‌های اصلی میان ساختمان‌های داده چیست، عملیات اصلی روی فهرست پیوندی کدام‌اند، و چطور می‌شود جدول درهم‌سازی خودمان را ساخت.

بخش اول یک **سناریو** است: شرکتی دستیار صوتی دارد که با یک «واژهٔ بیدارباش» مثل `hello` فعال می‌شود و حالا باید با واژه‌های بیشتری مثل `hi` یا `hello there` هم بیدار شود. چه ساختمان داده‌ای برای نگه داشتن این واژه‌ها مناسب است؟ Kelly می‌گوید اول باید ببینی **عملیات اصلی** چیست، یعنی حذف، درج و جست‌وجو، و کدام بیشتر استفاده می‌شود و باید سریع‌تر باشد. بعد سه تصویر را مقایسه می‌کند: فهرست پیوندی، جدول درهم‌سازی با سطل‌هایی بر اساس حرف اول، و ترای. با «Big Board» سال‌های گذشتهٔ Speller نشان می‌دهد سریع‌ترین پیاده‌سازی بیشترین حافظه را هم مصرف کرده بود: **زمان در برابر فضا** بده‌بستان اصلی است.

بخش دوم **فهرست پیوندی** است. Kelly گره‌ای با یک `phrase` (رشته) و اشاره‌گر `next` تعریف می‌کند، فهرست را با `node *list = NULL;` شروع می‌کند، با `malloc` گره می‌سازد و چون تنها گره است `next` را `NULL` می‌گذارد و `list` را به آن اشاره می‌دهد. سپس برنامهٔ `list.c` را با شرکت‌کننده‌ها می‌نویسد: سه عدد از کاربر، هر کدام در یک گرهٔ تازه که به **ابتدای** فهرست افزوده می‌شود (`n->next = list;` و بعد `list = n;`). در پرسش و پاسخ دربارهٔ عدد `3` در حلقه می‌گوید عددهای «جادویی» بهتر است ثابت تعریف شوند، و دربارهٔ شکست `malloc` در میانهٔ حلقه می‌گوید باید حافظهٔ گرفته‌شدهٔ قبلی را آزاد کرد؛ او بررسی خطا را برای ساده ماندن مثال از کد برمی‌دارد.

بعد **آزاد کردن** می‌آید: اگر فقط `free(list)` بنویسی، گرهٔ اول آزاد می‌شود و بقیه **یتیم** می‌شوند. راه درست یک اشاره‌گر موقت است که پیش از هر `free` نشانی گرهٔ بعدی را نگه دارد. Kelly پیمایش را با یک حلقهٔ `for` از `list` تا `NULL` می‌نویسد و `ptr->number` را چاپ می‌کند. وقتی برنامه را با `1`، `2`، `3` اجرا می‌کند، خروجی `3`، `2`، `1` است و یکی از شرکت‌کننده‌ها دلیلش را «اول وارد، آخر خارج» می‌گوید.

بخش سوم **جدول درهم‌سازی** است: آرایه‌ای که در هر خانه‌اش یک فهرست پیوندی است. جست‌وجو در فهرست پیوندی O(n) است؛ با سطل‌ها حافظهٔ بیشتری مصرف می‌کنی ولی فقط یک سطل را می‌گردی. تابع درهم‌ساز ورودی را به اندیس سطل نگاشت می‌کند، مثلاً `hey` به سطل `7`. نمونهٔ دوم درهم‌سازی بر اساس **طول** رشته است. Kelly سه ویژگی تابع درهم‌ساز خوب را می‌گوید: برای ورودی یکسان همیشه خروجی یکسان بدهد، توزیعی یکنواخت روی سطل‌ها بسازد، و از همهٔ سطل‌ها استفاده کند. هر دو نمونه به این معیارها نمی‌رسند: سطل‌های خالی (کمتر واژه‌ای با `Z` شروع می‌شود) و **برخوردهای** زیاد.

در پایان Kelly برنامهٔ `hash.c` را می‌نویسد: تابعی که بر اساس حرف اول عددی بین `0` و `25` برمی‌گرداند، با `toupper` برای یکسان کردن حروف و `isalpha` برای حالت‌هایی که نویسهٔ اول حرف نیست. شرکت‌کننده‌ها حالت‌های مرزی را پیدا می‌کنند: رشتهٔ خالی، عدد یا فاصله در ابتدا. کامپایل اول به‌خاطر نبودن prototype و `string.h` شکست می‌خورد. بعد تابع را طوری بهبود می‌دهند که به **دو** حرف اول نگاه کند و نشان می‌دهند جمع ساده دو حرف برخورد می‌سازد. Kelly یادآوری می‌کند که در Speller باید تابع درهم‌ساز **خودت** را بنویسی و به بهتر کردن توزیع سطل‌ها فکر کنی. جلسه با اشاره به هفتهٔ ۶ و Python تمام می‌شود.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section5.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — خوش‌آمد و پرسش‌های جلسه](https://www.youtube.com/watch?v=sLrnELP1nT0&t=0s)
- [۱:۱۳ — سناریو: واژه‌های بیدارباش دستیار صوتی](https://www.youtube.com/watch?v=sLrnELP1nT0&t=73s)
- [۲:۳۱ — عملیات اصلی: حذف، درج، جست‌وجو](https://www.youtube.com/watch?v=sLrnELP1nT0&t=151s)
- [۳:۳۴ — سه نامزد: فهرست پیوندی، جدول درهم‌سازی، ترای](https://www.youtube.com/watch?v=sLrnELP1nT0&t=214s)
- [۴:۵۰ — Big Board: بده‌بستان زمان و حافظه](https://www.youtube.com/watch?v=sLrnELP1nT0&t=290s)
- [۶:۰۵ — گره چیست؟](https://www.youtube.com/watch?v=sLrnELP1nT0&t=365s)
- [۶:۵۴ — ساختن فهرست: NULL، malloc و next](https://www.youtube.com/watch?v=sLrnELP1nT0&t=414s)
- [۱۰:۰۸ — تمرین: برنامهٔ list.c](https://www.youtube.com/watch?v=sLrnELP1nT0&t=608s)
- [۱۷:۱۲ — پرسش و پاسخ: عدد جادویی و شکست malloc](https://www.youtube.com/watch?v=sLrnELP1nT0&t=1032s)
- [۱۸:۱۶ — افزودن گره به ابتدای فهرست](https://www.youtube.com/watch?v=sLrnELP1nT0&t=1096s)
- [۲۱:۱۹ — چرا free(list) کافی نیست](https://www.youtube.com/watch?v=sLrnELP1nT0&t=1279s)
- [۲۳:۳۱ — پیمایش و چاپ فهرست](https://www.youtube.com/watch?v=sLrnELP1nT0&t=1411s)
- [۳۰:۳۳ — اجرا: ترتیب برعکس](https://www.youtube.com/watch?v=sLrnELP1nT0&t=1833s)
- [۳۱:۳۲ — جدول درهم‌سازی: آرایه‌ای از فهرست‌ها](https://www.youtube.com/watch?v=sLrnELP1nT0&t=1892s)
- [۳۴:۲۴ — درهم‌سازی بر اساس طول](https://www.youtube.com/watch?v=sLrnELP1nT0&t=2064s)
- [۳۵:۲۰ — ویژگی‌های تابع درهم‌ساز خوب](https://www.youtube.com/watch?v=sLrnELP1nT0&t=2120s)
- [۳۷:۵۵ — تمرین: برنامهٔ hash.c](https://www.youtube.com/watch?v=sLrnELP1nT0&t=2275s)
- [۴۳:۳۳ — حالت‌های مرزی](https://www.youtube.com/watch?v=sLrnELP1nT0&t=2613s)
- [۴۸:۵۰ — خطای prototype و اجرا](https://www.youtube.com/watch?v=sLrnELP1nT0&t=2930s)
- [۵۰:۵۷ — بهبود: دو حرف اول](https://www.youtube.com/watch?v=sLrnELP1nT0&t=3057s)
- [۵۴:۵۲ — برخورد AC و BB و جمع‌بندی](https://www.youtube.com/watch?v=sLrnELP1nT0&t=3292s)
- [۵۶:۵۲ — پایان جلسه](https://www.youtube.com/watch?v=sLrnELP1nT0&t=3412s)

## کد رسمی جلسه

دو فایل کد منبع جلسه در [src5.zip](https://cdn.cs50.net/2025/fall/sections/5/src5.zip) هست.

`list.c`: ساختن فهرستی پیوندی از سه عدد با افزودن به ابتدا، پیمایش و آزاد کردن. این فایل بخشی از راه‌حل هیچ پرابلم‌ستی نیست و همان الگوی کد سخنرانی است، برای همین متن کاملش اینجا آمده است (تصمیم D35):

```c
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    // Head of linked list
    node *list = NULL;

    // Iteratively create nodes
    for (int i = 0; i < 3; i++)
    {
        int x = get_int("Number: ");

        node *n = malloc(sizeof(node));
        n->number = x;
        n->next = list;

        list = n;
    }

    // Traverse through linked list and print each number
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    // Free the linked list
    node *ptr = list;
    while (ptr != NULL)
    {
        node *tmp = ptr;
        ptr = ptr->next;
        free(tmp);
    }
}
```

> **توجه:** در این فایل پس از `malloc` بررسی `NULL` نیامده است؛ Kelly در جلسه آن را برای ساده ماندن مثال برداشت. در کد خودت همیشه بررسی کن و در مسیر خطا گره‌های قبلی را آزاد کن (ناهمخوانی ثبت‌شده در `sources.json`).

`hash.c`: **فقط پیوند.** نسخهٔ نهایی این فایل تابع درهم‌سازی بر اساس دو حرف اول است، یعنی دقیقاً همان نوع بهبودی که Speller از تو می‌خواهد خودت طراحی کنی. برای همین متنش اینجا بازتولید نشده است: [فهرست src5](https://cdn.cs50.net/2025/fall/sections/5/src5/). این تابع برای حالت‌های خطا عددهای منفی برمی‌گرداند که برای اندیس آرایه مناسب نیست؛ این مورد هم در `sources.json` ثبت شده است.

## نکته‌های کلیدی

- انتخاب ساختمان داده به **عملیات اصلی** (درج، حذف، جست‌وجو) و اولویت آن‌ها بستگی دارد.
- زمان و فضا بده‌بستان اصلی‌اند؛ سریع‌ترین پیاده‌سازی‌های Speller معمولاً حافظهٔ بیشتری مصرف کرده‌اند.
- گرهٔ فهرست پیوندی یک داده و یک اشاره‌گر `next` دارد؛ فهرست خالی یعنی `node *list = NULL;`.
- برای افزودن به ابتدا: اول `n->next = list;` و بعد `list = n;`.
- `free(list)` فقط گرهٔ اول را آزاد می‌کند؛ پیش از هر `free` نشانی گرهٔ بعدی را نگه دار.
- افزودن به ابتدا ترتیب را برعکس می‌کند.
- تابع درهم‌ساز خوب: قطعی، با توزیع یکنواخت، و با استفاده از همهٔ سطل‌ها.
- حالت‌های مرزی تابع درهم‌ساز را از پیش ببین: رشتهٔ خالی، نویسهٔ غیرحرفی، حروف بزرگ و کوچک.

## کاربرد در پرابلم‌ست

> **تألیفی:** پیوند جلسه با مسئله‌های این هفته.

- الگوی ساختن گره، افزودن به ابتدا و آزاد کردن فهرست در [Speller](/kb/d/w05-ps-speller) لازم می‌شود؛ اما کد جلسه بخشی از راه‌حل آن نیست و تو باید آن را در ساختار خود Speller به کار ببری.
- بحث ویژگی‌های تابع درهم‌ساز و برخوردها پایهٔ فکر کردن به تابع درهم‌ساز خودت در Speller است. این بسته هیچ تابع درهم‌سازی پیشنهاد نمی‌کند.
- آزاد کردن تک‌تک گره‌ها با اشاره‌گر موقت همان مهارتی است که در [Inheritance](/kb/d/w05-ps-inheritance) برای آزاد کردن یک ساختار پیوندی لازم داری.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
