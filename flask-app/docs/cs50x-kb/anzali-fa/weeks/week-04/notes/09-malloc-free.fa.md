---
id: w04-n09
type: note
title: 'malloc، free، strcpy و NULL (Copying and malloc: malloc and free)'
title_fa: malloc، free، strcpy و NULL
title_en: 'Copying and malloc: malloc and free'
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Copying and malloc
official_anchor: copying-and-malloc
source_url: https://cs50.harvard.edu/x/2026/notes/4/#copying-and-malloc
source_refs:
- src-notes-4#copying-and-malloc
- src-transcript-4
- src-short-dynamic-memory-allocation
- src-srt-4
concept_ids:
- w04-c-malloc
- w04-c-free
- w04-c-malloc-null-check
- w04-c-strcpy
- w04-c-nul-byte-room
prev: w04-n08
next: w04-n10
order: 9
video:
  youtube_id: db0H0U13YsA
  start: '1:02:33'
  start_seconds: 3753
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=3753s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'so I could do Malloch of 4'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# malloc، free، strcpy و NULL

> **منبع رسمی:** بخش «Copying and malloc» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#copying-and-malloc). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۲:۳۳ تا حدود ۱:۱۴:۰۴](https://www.youtube.com/watch?v=db0H0U13YsA&t=3753s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برای کپی واقعی یک رشته باید **حافظهٔ تازه** بگیریم. `malloc` و `free` اولین ابزارهایی‌اند که با آن‌ها خودت حافظه را مدیریت می‌کنی؛ همان چیزی که `get_string` تا حالا پنهانی برایت انجام می‌داد.

## malloc و free

برای ساختن یک کپی واقعی از رشته به دو ابزار تازه نیاز داریم:

- `malloc` به تو، برنامه‌نویس، اجازه می‌دهد بلوکی از حافظه با اندازهٔ مشخص **تخصیص** بدهی.
- `free` به کامپیوتر می‌گوید بلوکی را که قبلاً تخصیص داده بودی **آزاد** کند.

```c
// Capitalizes a copy of a string

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory, including '\0'
    for (int i = 0; i <= strlen(s); i++)
    {
        t[i] = s[i];
    }

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

- `malloc(strlen(s) + 1)` بلوکی به طول رشتهٔ `s` به‌علاوهٔ یک می‌سازد. این یک بایت اضافه برای کاراکتر *null*، یعنی `\0`، در رشتهٔ کپی‌شده است.
- حلقهٔ `for` در رشتهٔ `s` جلو می‌رود و هر مقدار را در همان مکان رشتهٔ `t` می‌گذارد. به `<=` دقت کن: `\0` هم کپی می‌شود.

## کمی کارآمدتر

```c
// Capitalizes a copy of a string, defining n in loop too

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory, including '\0'
    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

- حالا `n = strlen(s)` در سمت چپ حلقهٔ `for` تعریف شده است. بهتر است تابع‌های غیرضروری را در شرط وسط حلقه صدا نزنیم، چون بارها و بارها اجرا می‌شود. با این تغییر `strlen` فقط یک بار اجرا می‌شود.

## strcpy

زبان C تابع آماده‌ای برای کپی رشته دارد به اسم `strcpy`:

```c
// Capitalizes a copy of a string using strcpy

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory
    strcpy(t, s);

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

- `strcpy` همان کاری را می‌کند که حلقهٔ `for` ما می‌کرد.

## NULL و free

هم `get_string` و هم `malloc` در صورت بروز مشکل `NULL` برمی‌گردانند؛ مقدار ویژه‌ای در حافظه. می‌توانی برای این حالت این‌طور بررسی کنی:

```c
// Capitalizes a copy of a string without memory errors

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    // Copy string into memory
    strcpy(t, s);

    // Capitalize copy
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Free memory
    free(t);
    return 0;
}
```

- اگر `malloc` شکست بخورد، `NULL` برمی‌گرداند و برنامه با `return 1` خارج می‌شود.
- `free` به کامپیوتر می‌گوید کارت با بلوکی که با `malloc` ساختی تمام شده است.

> [!WARNING]
> **هشدار**
> درس‌نامه در توضیح این کد می‌گوید «اگر رشتهٔ دریافت‌شده طولش `0` باشد ... `NULL` برگردانده می‌شود». اما در خود کد، رشتهٔ خالی `NULL` نیست؛ `get_string` فقط در صورت بروز خطا `NULL` می‌دهد و برای رشتهٔ خالی، کد فقط از بزرگ کردن حرف اول صرف‌نظر می‌کند (`strlen(t) > 0`). این ناهمخوانی در `sources.json` ثبت شده است.

> [!IMPORTANT]
> **مهم**
> هر `malloc` موفق دقیقاً یک `free` لازم دارد. رشته‌هایی را که `get_string` برمی‌گرداند خودت آزاد نکن؛ کتابخانهٔ CS50 این کار را انجام می‌دهد.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David توضیح داد که با `malloc(4)` چهار بایت جایی در آن شبکهٔ حافظه می‌گیری؛ نمی‌دانی کجا و برایت مهم هم نیست، چون مقدار بازگشتی `malloc` نشانی اولین بایت آن بلوک است.
- **از سخنرانی:** او گفت وقتی کارت با `t` تمام شد باید `free` را با همان نشانی صدا بزنی تا سیستم‌عامل آن حافظه را پس بگیرد. اگر نکنی، به آن **نشت حافظه** (memory leak) می‌گویند.
- **از سخنرانی:** بعد از استراحت کسی پرسید آیا باید `s` را هم آزاد می‌کرد. جواب کوتاه «نه» بود: کتابخانهٔ CS50 عمداً حافظهٔ `get_string` را خودش مدیریت می‌کند.

ویدئوی کوتاه [Dynamic Memory Allocation](/kb/d/w04-sh-dynamic-memory-allocation) قانون‌های `free` و فرق حافظهٔ پویا با متغیرهای معمولی را مفصل‌تر می‌گوید.

## اشتباه‌های رایج

- `malloc(strlen(s))` بدون `+ 1`؛ جایی برای `\0` نمی‌ماند.
- بررسی نکردن `NULL` پس از `malloc`.
- فراموش کردن `free`، یا آزاد کردن دوبارهٔ یک بلوک.

## جمع‌بندی

- `malloc(n)` نشانی یک بلوک `n` بایتی می‌دهد یا در صورت شکست `NULL`.
- برای کپی رشته `strlen(s) + 1` بایت بگیر و با `strcpy` یا حلقه کپی کن.
- هر بلوک `malloc` را وقتی کارت تمام شد با `free` آزاد کن.

## پیوندها

- قبلی: [کپی کردن رشته: چرا t = s کپی نیست](/kb/d/w04-n08)
- بعدی: [Valgrind: یافتن خطاهای حافظه](/kb/d/w04-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
