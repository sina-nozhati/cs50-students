---
id: w02-n04
type: note
title: 'اشکال‌زدایی با printf (Debugging: printf)'
title_fa: اشکال‌زدایی با printf
title_en: 'Debugging: printf'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Debugging
official_anchor: debugging
source_url: https://cs50.harvard.edu/x/2026/notes/2/#debugging
source_refs:
- src-notes-2#debugging
- src-transcript-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-printf-debugging
prev: w02-n03
next: w02-n05
order: 4
video:
  youtube_id: h5Gc1n8ZuU8
  start: '19:46'
  start_seconds: 1186
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=1186s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'I is less than or equal to 3'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# اشکال‌زدایی با printf

> **منبع رسمی:** بخش «Debugging» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#debugging). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۹:۴۶ تا حدود ۲۶:۰۸](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=1186s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

ساده‌ترین ابزار اشکال‌زدایی را از هفتهٔ ۱ می‌شناسی: `printf`. اگر نمی‌دانی متغیری در هر لحظه چه مقداری دارد، **چاپش کن**.

## برنامهٔ باگ‌دار رسمی

درس‌نامه تصویر ستون آجرهای Mario از هفتهٔ پیش را یادآوری می‌کند: یک ستون سه‌آجری. بعد این کد را می‌آورد که عمداً باگ دارد:

```c
// Buggy example for printf

#include <stdio.h>

int main(void)
{
    for (int i = 0; i <= 3; i++)
    {
        printf("#\n");
    }
}
```

- درس‌نامه می‌خواهد با `code buggy.c` فایل را بسازی و همین کد را بنویسی.
- هدف سه آجر بود، اما اجرای برنامه **چهار** آجر چاپ می‌کند. این خطای منطقی است: کامپایلر چیزی نمی‌گوید.

## چاپ مقدار i

```c
// Buggy example for printf

#include <stdio.h>

int main(void)
{
    for (int i = 0; i <= 3; i++)
    {
        printf("i is %i\n", i);
        printf("#\n");
    }
}
```

- این نسخه در هر دور حلقه مقدار `i` را چاپ می‌کند تا ببینی کد واقعاً چه می‌کند.
- خروجی شامل `i is 0`، `i is 1`، `i is 2` و `i is 3` است. چهار دور، نه سه.

## اصلاح

```c
#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("#\n");
    }
}
```

- `<=` با `<` جایگزین شده است. حالا `i` از ۰ تا ۲ می‌رود: دقیقاً سه دور.
- پس از اصلاح، `printf` اضافهٔ اشکال‌زدایی را هم برمی‌داریم.

## گام بعد: باگ در یک تابع

درس‌نامه کد را با جدا کردن کار چاپ در تابعی به نام `print_column` «بهتر» می‌کند، اما باگ هنوز هست:

```c
// Buggy example for debug50

#include <cs50.h>
#include <stdio.h>

void print_column(int height);

int main(void)
{
    int h = get_int("Height: ");
    print_column(h);
}

void print_column(int height)
{
    for (int i = 0; i <= height; i++)
    {
        printf("#\n");
    }
}
```

- کامپایل و اجرای این کد هنوز باگ دارد؛ شرط حلقه دوباره `<=` است.
- **از سخنرانی:** حالا کد پیچیده‌تر شده و `printf` گذاشتن در جای‌جای آن زحمت دارد. برای همین سراغ ابزار دوم می‌رویم: دیباگر.

> **تألیفی:** وقتی حلقه یک دور بیشتر یا کمتر از انتظار اجرا می‌شود، اول شرط پایان (`<` یا `<=`) و مقدار آغاز (`0` یا `1`) را بررسی کن.

## اشتباه‌های رایج

- فراموش کردن پاک کردن `printf`های اشکال‌زدایی پس از رفع باگ.
- چاپ مقدار **بعد** از جایی که باگ رخ می‌دهد؛ مقدار را درست پیش از رفتار مشکوک چاپ کن.

## جمع‌بندی

- `printf` ساده‌ترین راه دیدن حالت درونی برنامه است.
- با دیدن `i is 3` فهمیدیم حلقه یک دور اضافه دارد و `<=` را به `<` تغییر دادیم.

## پیوندها

- قبلی: [باگ و خطاهای کامپایل](/kb/d/w02-n03)
- بعدی: [debug50، نقطهٔ توقف و اردک پلاستیکی](/kb/d/w02-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
