---
id: w04-n05
type: note
title: رشته‌ها همان char * هستند (Strings)
title_fa: رشته‌ها همان char * هستند
title_en: Strings
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Strings
official_anchor: strings
source_url: https://cs50.harvard.edu/x/2026/notes/4/#strings
source_refs:
- src-notes-4#strings
- src-transcript-4
- src-short-defining-custom-types
- src-srt-4
concept_ids:
- w04-c-string-char-star
- w04-c-typedef
prev: w04-n04
next: w04-n06
order: 5
video:
  youtube_id: db0H0U13YsA
  start: '30:58'
  start_seconds: 1858
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=1858s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'Let me go into addresses.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# رشته‌ها همان char * هستند

> **منبع رسمی:** بخش «Strings» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#strings). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۰:۵۸ تا حدود ۴۵:۰۰](https://www.youtube.com/watch?v=db0H0U13YsA&t=1858s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

از هفتهٔ ۱ با نوع `string` کار کردی. حالا که اشاره‌گر را می‌شناسی، می‌توانیم یکی از ساده‌سازی‌های اول دوره را کنار بزنیم و ببینیم `string` واقعاً چیست.

## رشته کجاست؟

کد را این‌طور تغییر بده:

```c
// Prints a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%s\n", s);
}
```

- رشتهٔ `s` چاپ می‌شود.
- یادت هست رشته فقط آرایه‌ای از کاراکترهاست؟ مثلاً `string s = "HI!"` در حافظه چهار بایت است: `H`، `I`، `!` و `\0`.
- اما خود `s` چیست و کجا ذخیره شده است؟ `s` هم باید جایی در حافظه باشد. درس‌نامه نشان می‌دهد که `s` اشاره‌گری است که به کامپایلر می‌گوید **اولین بایت** رشته کجای حافظه است.

نشانی هر کاراکتر را هم می‌شود دید:

```c
// Prints a string's address as well the addresses of its chars

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
}
```

- `&` نشانی هر عنصر رشته را نشان می‌دهد.
- اگر اجرا کنی، می‌بینی عنصرهای `0`، `1`، `2` و `3` در حافظه **کنار هم**اند. نشانی اول با مقدار `s` یکی است.

## برداشتن چرخ‌های کمکی

همین برنامه را می‌شود با کتابخانهٔ `cs50.h` نوشت:

```c
// Declares a string with CS50 Library

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%s\n", s);
}
```

و حالا بدون آن:

```c
// Declares a string without CS50 Library

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s);
}
```

- `cs50.h` حذف شده است. رشته در C در واقع یک `char *` است.
- این کد رشته‌ای را چاپ می‌کند که از مکان `s` شروع می‌شود. این C خام است، بدون داربست کتابخانهٔ cs50.

## typedef

- هفتهٔ پیش یاد گرفتی با `struct` نوع دادهٔ خودت را بسازی.
- کتابخانهٔ cs50 یک تعریف نوع دارد: `typedef char *string`
- این تعریف نوع، وقتی از کتابخانهٔ cs50 استفاده می‌کنی، نمایش ساده‌شده‌ای است که اجازه می‌دهد از نوع دلخواهی به اسم `string` استفاده کنی.

> [!NOTE]
> **نکته**
> `typedef` نوع تازه‌ای «نمی‌سازد»؛ فقط برای نوعی که وجود دارد **اسم مستعار** می‌گذارد. `string` و `char *` دقیقاً یک چیزند. ویدئوی کوتاه [Defining Custom Types](/kb/d/w04-sh-defining-custom-types) همین را برای `struct` هم نشان می‌دهد.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David نشانی `s` و نشانی تک‌تک کاراکترها را چاپ کرد: نشانی `s` و `&s[0]` دقیقاً یکی بود و هر کاراکتر بعدی، تا `\0`، فقط یک بایت جلوتر بود.
- **از سخنرانی:** او توضیح داد که لازم نیست نشانی همهٔ کاراکترها را داشته باشیم؛ به همین علت قرار شد هر رشته با `\0` تمام شود. اگر ابتدای رشته و نشانهٔ پایانش را داشته باشی، با یک حلقه بقیه را پیدا می‌کنی.
- **از سخنرانی:** او گفت `printf` با یک `char *` می‌داند که باید به آن نشانی برود و چاپ کند تا به `\0` برسد. بعد `cs50.h` را برداشت و برنامه بدون هیچ چرخ کمکی کار کرد.

## اشتباه‌های رایج

- فکر کردن به اینکه `s` خودِ همهٔ کاراکترهاست؛ `s` فقط نشانی اولین کاراکتر است.
- فراموش کردن `\0` در شمارش بایت‌های یک رشته: `"HI!"` چهار بایت است، نه سه.
- فکر کردن به اینکه `string` بخشی از زبان C است؛ از `cs50.h` می‌آید.

## جمع‌بندی

- `string` همان `char *` است و از `typedef char *string` در کتابخانهٔ cs50 می‌آید.
- متغیر رشته نشانی اولین بایت است؛ کاراکترها پشت سر هم و تا `\0` ادامه دارند.

## پیوندها

- قبلی: [اشاره‌گرها: & و *](/kb/d/w04-n04)
- بعدی: [حساب اشاره‌گرها](/kb/d/w04-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
