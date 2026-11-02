---
id: w05-n05
type: note
title: 'بزرگ کردن آرایه با malloc و کپی (Arrays: growing with malloc and copying)'
title_fa: بزرگ کردن آرایه با malloc و کپی
title_en: 'Arrays: growing with malloc and copying'
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Arrays
official_anchor: arrays
source_url: https://cs50.harvard.edu/x/2026/notes/5/#arrays
source_refs:
- src-notes-5#arrays
- src-transcript-5
- src-srt-5
concept_ids:
- w05-c-array-contiguous
- w05-c-array-resize-copy
- w05-c-tmp-pointer
prev: w05-n04
next: w05-n06
order: 5
video:
  youtube_id: PmAI76OGE_E
  start: '12:22'
  start_seconds: 742
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=742s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'first of the data structures we saw back in week 2'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# بزرگ کردن آرایه با malloc و کپی

> **منبع رسمی:** بخش «Arrays» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#arrays). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۲:۲۲ تا حدود ۲۷:۳۷](https://www.youtube.com/watch?v=PmAI76OGE_E&t=742s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

آرایه اولین ساختمان داده‌ای بود که در هفتهٔ ۲ دیدی. اینجا می‌بینی بزرگ کردن یک آرایه چه زحمتی دارد؛ همین زحمت انگیزهٔ ساختارهای بعدی است.

## آرایه‌ها

- برگردیم به هفتهٔ ۲: آنجا اولین ساختمان داده را دیدی.
- **آرایه** بلوکی از حافظهٔ **پیوسته** (contiguous) است.
- درس‌نامه آرایه را با تصویر سه خانهٔ کنار هم با مقدارهای `1`، `2` و `3` نشان می‌دهد (پیوند تصویر در `media.json`، فقط پیوند).
- در ترمینال بنویس `code list.c` و کد زیر را بنویس:

```c
// Implements a list of numbers with an array of fixed size

#include <stdio.h>

int main(void)
{
    // List of size 3
    int list[3];

    // Initialize list with numbers
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Print list
    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }
}
```

- این کد خیلی شبیه چیزی است که پیش‌تر در این درس یاد گرفتی: حافظه برای سه عضو از پیش گرفته شده است.
- خوب نبود اگر می‌توانستیم `4` را جای دیگری از حافظه بگذاریم؟ طبق تعریف، آن وقت دیگر آرایه نداشتیم، چون `4` دیگر در حافظهٔ پیوسته نبود. چطور می‌شود جاهای مختلف حافظه را به هم وصل کرد؟
- در حافظه مقدارهای دیگری هم هست که برنامه‌ها، تابع‌ها و متغیرهای دیگر گذاشته‌اند. بسیاری از آن‌ها **مقدار زباله**‌اند: زمانی استفاده شده‌اند ولی حالا برای استفاده آزادند.
- فرض کن می‌خواهی مقدار چهارم `4` را در آرایه بگذاری. باید ناحیهٔ تازه‌ای از حافظه بگیری و آرایهٔ قدیمی را به آن منتقل کنی. این ناحیهٔ تازه در ابتدا پر از مقدار زباله است.
- با اضافه شدن مقدارها به ناحیهٔ تازه، زباله‌ها یکی‌یکی رونویسی می‌شوند تا سرانجام همهٔ داده‌های تازه جای آن‌ها را بگیرند.
- یکی از عیب‌های این روش طراحی بد آن است: هر بار که عددی اضافه می‌کنیم، باید آرایه را عضو به عضو کپی کنیم.
- با دانسته‌های تازه‌مان دربارهٔ اشاره‌گرها می‌شود طراحی بهتری ساخت. کد را این‌طور تغییر بده:

```c
// Implements a list of numbers with an array of dynamic size

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // List of size 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Initialize list of size 3 with numbers
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // List of size 4
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    // Copy list of size 3 into list of size 4
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }

    // Add number to list of size 4
    tmp[3] = 4;

    // Free list of size 3
    free(list);

    // Remember list of size 4
    list = tmp;

    // Print list
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Free list
    free(list);
    return 0;
}
```

- یک فهرست سه‌عددی ساخته می‌شود و سه خانه مقدارهای `1`، `2` و `3` را می‌گیرند. بعد یک فهرست چهارتایی ساخته می‌شود و فهرست اول در دومی کپی می‌شود. مقدار `4` به فهرست `tmp` اضافه می‌شود. چون بلوکی که `list` به آن اشاره می‌کند دیگر استفاده نمی‌شود، با `free(list)` آزاد می‌شود. سرانجام به اشاره‌گر `list` گفته می‌شود به بلوکی اشاره کند که `tmp` به آن اشاره می‌کند. محتوای `list` چاپ و بعد آزاد می‌شود. به `#include <stdlib.h>` هم دقت کن.
- مفید است `list` و `tmp` را مثل دو تابلو تصور کنی که هر دو به تکه‌ای از حافظه اشاره می‌کنند. `list` زمانی به آرایهٔ سه‌تایی اشاره می‌کرد و در پایان به تکه‌ای چهارتایی. در پایان کد، `tmp` و `list` هر دو به یک بلوک اشاره می‌کنند.

> [!IMPORTANT]
> **مهم**
> در `list1.c` دو بررسی `NULL` هست. اگر `malloc` دوم شکست بخورد، برنامه **اول** `free(list)` را صدا می‌زند و بعد `return 1`؛ وگرنه تکهٔ سه‌تایی بی‌صاحب می‌ماند. این همان قاعدهٔ هفتهٔ ۴ است: هر چه `malloc` کرده‌ای، در هر مسیر خروج آزاد کن.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David توضیح داد چرا نمی‌شود `4` را همین‌طور کنار `3` گذاشت: ممکن است رشتهٔ دیگری مثل `HELLO` درست بعد از آرایه در حافظه باشد و نوشتن روی آن، رشته را خراب کند.
- **از سخنرانی:** او اول نشان داد نوشتن `list = malloc(4 * sizeof(int));` روی همان متغیر کار بدی است، چون نشانی تکهٔ قبلی را گم می‌کنی و **نشت حافظه** می‌سازی؛ راه‌حل، متغیر موقت `tmp` است.
- **از سخنرانی:** او یادآوری کرد `list[0]` همان `*list` است و `list[1]` همان `*(list + 1)`؛ کروشه فقط شکل خواناتر حساب روی نشانی‌هاست.
- **از سخنرانی:** او گفت وقتی برنامه تمام می‌شود حافظه به هر حال به سیستم‌عامل برمی‌گردد، اما برنامه‌هایی که ساعت‌ها یا روزها اجرا می‌شوند با نشت حافظه کند می‌شوند؛ پس باید همیشه درستش کرد.
- **از سخنرانی:** نخستین `make` به خطای «undeclared library function malloc» خورد، چون `stdlib.h` را فراموش کرده بود.

## اشتباه‌های رایج

- نوشتن نتیجهٔ `malloc` تازه مستقیم روی `list` و گم کردن تکهٔ قبلی.
- فراموش کردن `free(list)` پیش از `return 1` در مسیر خطا.
- آزاد کردن `tmp` به‌جای `list` پس از `list = tmp;`؛ آن دو حالا به یک بلوک اشاره می‌کنند و بلوک فقط یک بار باید آزاد شود.

## جمع‌بندی

- آرایه پیوسته است؛ پس بزرگ کردنش یعنی گرفتن تکهٔ تازه، کپی و آزاد کردن تکهٔ قدیمی.
- `tmp` تضمین می‌کند تا موفقیت تخصیص تازه، نشانی قبلی گم نشود.

## پیوندها

- قبلی: [پشته: آخر وارد، اول خارج (LIFO)](/kb/d/w05-n04)
- بعدی: [realloc و هزینهٔ کپی](/kb/d/w05-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
