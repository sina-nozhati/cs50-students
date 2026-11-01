---
id: w04-n15
type: note
title: ورودی و خروجی فایل (File I/O)
title_fa: ورودی و خروجی فایل
title_en: File I/O
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: File I/O
official_anchor: file-io
source_url: https://cs50.harvard.edu/x/2026/notes/4/#file-io
source_refs:
- src-notes-4#file-io
- src-transcript-4
- src-short-pointers
- src-short-file-pointers
- src-pset-4
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-file-pointer
- w04-c-fopen-null-check
- w04-c-fprintf-fclose
- w04-c-fread-fwrite
- w04-c-byte-type
prev: w04-n14
next: w04-summary
order: 15
video:
  youtube_id: db0H0U13YsA
  start: '2:02:56'
  start_seconds: 7376
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=7376s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'persistent storage or non-volatile'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ورودی و خروجی فایل

> **منبع رسمی:** بخش «File I/O» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#file-io). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۲:۵۶](https://www.youtube.com/watch?v=db0H0U13YsA&t=7376s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا حالا هر چه برنامه‌هایت می‌دانستند با تمام شدن برنامه از بین می‌رفت. با فایل‌ها اطلاعات **ماندگار** می‌شود. هر سه پرابلم‌ست این هفته با فایل کار می‌کنند: صدا در [Volume](/kb/d/w04-ps-volume)، تصویر در [Filter](/kb/d/w04-ps-filter-less) و کارت حافظه در [Recover](/kb/d/w04-ps-recover).

## phonebook.c

می‌توانی فایل‌ها را بخوانی و تغییر بدهی. این موضوع در هفته‌های بعد بیشتر بحث می‌شود، اما این کد `phonebook.c` را ببین:

```c
// Saves names and numbers to a CSV file

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Open CSV file
    FILE *file = fopen("phonebook.csv", "a");

    // Get name and number
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    // Print to file
    fprintf(file, "%s,%s\n", name, number);

    // Close file
    fclose(file);
}
```

- این کد برای دسترسی به فایل از اشاره‌گر استفاده می‌کند: `FILE *`.
- `fopen` فایل را باز می‌کند؛ `"a"` یعنی افزودن (append) به انتهای فایل.
- `fprintf` مثل `printf` است، اما در فایل می‌نویسد. `fclose` فایل را می‌بندد.
- می‌توانی پیش از اجرا فایلی به اسم `phonebook.csv` بسازی یا [phonebook.csv](https://cdn.cs50.net/2025/fall/lectures/4/src4/phonebook.csv?download) را دانلود کنی. پس از اجرای برنامه و وارد کردن یک اسم و شمارهٔ تلفن، می‌بینی که این داده در فایل CSV تو **ماندگار** می‌شود.

اگر بخواهیم مطمئن شویم فایل باز شده است:

```c
// Saves names and numbers to a CSV file, checking for NULL

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Open CSV file
    FILE *file = fopen("phonebook.csv", "a");
    if (file == NULL)
    {
        return 1;
    }

    // Get name and number
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    // Print to file
    fprintf(file, "%s,%s\n", name, number);

    // Close file
    fclose(file);
}
```

- این برنامه با `return 1` در برابر اشاره‌گر `NULL` محافظت می‌کند.

> [!IMPORTANT]
> **مهم**
> `fopen` اگر نتواند فایل را باز کند `NULL` برمی‌گرداند، درست مثل `malloc`. همیشه پیش از استفاده بررسی کن. پرابلم‌ست‌های این هفته صریحاً می‌خواهند اگر فایل باز نشد، پیام بدهی و `1` برگردانی.

## cp.c

می‌توانیم برنامهٔ کپی خودمان را با `code cp.c` بنویسیم:

```c
// Copies a file

#include <stdio.h>

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    FILE *src = fopen(argv[1], "rb");
    FILE *dst = fopen(argv[2], "wb");

    BYTE b;

    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }

    fclose(dst);
    fclose(src);
}
```

- این فایل نوع دادهٔ خودمان به اسم `BYTE` را می‌سازد که هم‌اندازهٔ `uint8_t` است، یعنی یک بایت.
- بعد یک `BYTE` می‌خواند و آن را در فایل دیگری می‌نویسد، تا وقتی `fread` دیگر چیزی برای خواندن نداشته باشد.
- `"rb"` و `"wb"` یعنی خواندن و نوشتن **دودویی** (binary).

> [!NOTE]
> **نکته (تألیفی)**
> `fread(&b, sizeof(b), 1, src)` می‌گوید: «۱ قطعه به اندازهٔ `sizeof(b)` بایت از `src` بخوان و در نشانی `b` بگذار» و تعداد **قطعه‌هایی** را که واقعاً خوانده برمی‌گرداند؛ در انتهای فایل این عدد `0` است. `fwrite` همین چهار آرگومان را دارد. این `cp.c` برای کوتاهی، تعداد آرگومان‌ها و `NULL` بودن فایل‌ها را بررسی نمی‌کند؛ در برنامهٔ واقعی باید بکنی.

- BMPها هم مجموعه‌هایی از داده‌اند که می‌توانیم بررسی و تغییرشان بدهیم. این هفته در پرابلم‌ست‌ها دقیقاً همین کار را می‌کنی!

ویدئوی کوتاه [File Pointers](/kb/d/w04-sh-file-pointers) تابع‌های `fgetc`، `fputc`، `fread` و `fwrite` را یکی‌یکی معرفی می‌کند.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David یادآوری کرد که RAM **فرّار** است: اگر برق قطع شود یا باتری تمام شود، هر چه در RAM است از دست می‌رود؛ اما دیسک سخت یا SSD حافظهٔ **پایدار** است.
- **از سخنرانی:** او توضیح داد که با `"w"` فایل از اولین بایت بازنویسی می‌شود و طبق مستندات `fopen` برای افزودن به انتهای فایل باید `"a"` بنویسی. بعد گفت `phonebook.csv` را می‌شود در Excel، Apple Numbers یا Google Sheets باز کرد.
- **از سخنرانی:** او `BYTE` را `unsigned char` تعریف کرد و گفت `unsigned` به کامپایلر می‌گوید این ۸ بیت را نباید منفی تفسیر کند.

## اشتباه‌های رایج

- بررسی نکردن `NULL` پس از `fopen`.
- فراموش کردن `fclose`.
- استفاده از `"w"` وقتی می‌خواهی به فایل اضافه کنی؛ محتوای قبلی پاک می‌شود.
- فرض اینکه `fread` تعداد **بایت‌ها** را برمی‌گرداند؛ تعداد قطعه‌ها را برمی‌گرداند.

## جمع‌بندی

- `FILE *`، `fopen`، `fprintf`، `fclose` برای فایل‌های متنی؛ `fread` و `fwrite` برای بایت‌ها.
- همیشه بررسی کن `fopen` مقدار `NULL` نداده باشد.
- `typedef unsigned char BYTE;` یک بایت بی‌علامت تعریف می‌کند.

## پیوندها

- قبلی: [scanf: ورودی بدون کتابخانهٔ CS50](/kb/d/w04-n14)
- بعدی: [خلاصهٔ هفته](/kb/d/w04-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
