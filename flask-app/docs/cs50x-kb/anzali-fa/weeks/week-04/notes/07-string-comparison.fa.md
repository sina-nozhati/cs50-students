---
id: w04-n07
type: note
title: 'مقایسهٔ رشته‌ها: == در برابر strcmp (String Comparison)'
title_fa: 'مقایسهٔ رشته‌ها: == در برابر strcmp'
title_en: String Comparison
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: String Comparison
official_anchor: string-comparison
source_url: https://cs50.harvard.edu/x/2026/notes/4/#string-comparison
source_refs:
- src-notes-4#string-comparison
- src-transcript-4
- src-srt-4
concept_ids:
- w04-c-compare-addresses
- w04-c-strcmp-content
prev: w04-n06
next: w04-n08
order: 7
video:
  youtube_id: db0H0U13YsA
  start: '48:06'
  start_seconds: 2886
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=2886s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'stircom STR CMP'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مقایسهٔ رشته‌ها: == در برابر strcmp

> **منبع رسمی:** بخش «String Comparison» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#string-comparison). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۸:۰۶ تا حدود ۵۷:۳۱](https://www.youtube.com/watch?v=db0H0U13YsA&t=2886s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هفتهٔ ۳ گفتیم برای مقایسهٔ رشته‌ها از `strcmp` استفاده کن، نه `==`. حالا علتش را واقعاً می‌فهمیم.

## مقایسهٔ عددها

رشته فقط آرایه‌ای از کاراکترهاست که با مکان اولین بایتش شناخته می‌شود. اول یادآوری مقایسهٔ عددهای صحیح، با `code compare.c`:

```c
// Compares two integers

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two integers
    int i = get_int("i: ");
    int j = get_int("j: ");

    // Compare integers
    if (i == j)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

## چرا `==` برای رشته‌ها کار نمی‌کند

- برای رشته‌ها نمی‌شود با عملگر `==` مقایسه کرد.
- `==` مکان‌های حافظهٔ دو رشته را مقایسه می‌کند، نه کاراکترهای داخلشان. برای همین `strcmp` را پیشنهاد کرده بودیم.

```c
// Compares two strings' addresses

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Compare strings' addresses
    if (s == t)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

- اگر برای هر دو رشته `HI!` بنویسی، باز هم خروجی `Different` است.
- علت را تصویر درس‌نامه نشان می‌دهد: دو رشته جداگانه در دو جای حافظه ذخیره شده‌اند، پس کد در واقع بررسی می‌کند که آیا **نشانی‌ها** متفاوت‌اند.

## درست کردن با strcmp

```c
// Compares two strings using strcmp

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Compare strings
    if (strcmp(s, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

- `strcmp` اگر دو رشته یکسان باشند `0` برمی‌گرداند.

برای اینکه ببینیم این دو رشته در دو جا زندگی می‌کنند:

```c
// Prints two strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Print strings
    printf("%s\n", s);
    printf("%s\n", t);
}
```

و با یک تغییر کوچک، `%s` به `%p`، مکانشان را می‌بینیم:

```c
// Prints two strings' addresses

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Print strings' addresses
    printf("%p\n", s);
    printf("%p\n", t);
}
```

> [!WARNING]
> **هشدار**
> `s == t` هیچ خطای کامپایلی نمی‌دهد؛ فقط جواب «اشتباه» می‌دهد چون سؤال دیگری می‌پرسد. اگر می‌خواهی محتوا را مقایسه کنی، همیشه `strcmp(s, t) == 0`.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David پرسید چرا مقایسهٔ رشته‌ها با `strcmp` لازم بود و جواب داد: به `strcmp` نشانی `s` و نشانی `t` داده می‌شود، نه خود رشته‌ها.
- **از سخنرانی:** او گفت `strcmp` کاراکتر به کاراکتر جلو می‌رود و مقایسه می‌کند؛ کاری که کسی دهه‌ها پیش نوشته و ما از آن استفاده می‌کنیم.

## اشتباه‌های رایج

- استفاده از `==` برای مقایسهٔ محتوای رشته‌ها.
- چک کردن `if (strcmp(s, t))` برای «برابری»؛ مقدار غیرصفر یعنی **نابرابر**.

## جمع‌بندی

- `==` روی دو `char *` نشانی‌ها را مقایسه می‌کند.
- `strcmp` محتوا را مقایسه می‌کند و برای رشته‌های برابر `0` برمی‌گرداند.

## پیوندها

- قبلی: [حساب اشاره‌گرها](/kb/d/w04-n06)
- بعدی: [کپی کردن رشته: چرا t = s کپی نیست](/kb/d/w04-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
