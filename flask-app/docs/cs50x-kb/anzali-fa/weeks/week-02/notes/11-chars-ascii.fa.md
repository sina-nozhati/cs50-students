---
id: w02-n11
type: note
title: 'نویسه‌ها و ASCII (Strings: chars and ASCII)'
title_fa: نویسه‌ها و ASCII
title_en: 'Strings: chars and ASCII'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Strings
official_anchor: strings
source_url: https://cs50.harvard.edu/x/2026/notes/2/#strings
source_refs:
- src-notes-2#strings
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-char-ascii
prev: w02-n10
next: w02-n12
order: 11
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:30:20'
  start_seconds: 5420
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=5420s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'strings are double quotes'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# نویسه‌ها و ASCII

> **منبع رسمی:** بخش «Strings» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#strings). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۳۰:۲۰ تا حدود ۱:۳۸:۴۱](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=5420s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برای فهمیدن رشته باید اول `char` را دوباره ببینی. حرف تازهٔ این هفته: هر نویسه در حافظه فقط یک **عدد** است. همان کدهای ASCII هفتهٔ ۰.

## سه نویسه

- درس‌نامه می‌گوید: `string` چیزی نیست جز **آرایه‌ای از مقدارهای نوع `char`**.
- برای بررسی `char` و `string`، با `code hi.c` این کد را بنویس:

```c
// Prints chars

#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    printf("%c%c%c\n", c1, c2, c3);
}
```

- خروجی رشته‌ای از نویسه‌هاست: `HI!`.

## همان نویسه‌ها، به شکل عدد

```c
// Prints chars' ASCII codes

#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    printf("%i %i %i\n", c1, c2, c3);
}
```

- با جایگزین کردن `%c` با `%i`، **کدهای ASCII** چاپ می‌شوند: `72 73 33`.
- **تألیفی:** نوع متغیر عوض نشده است؛ فقط شیوهٔ **نمایش** را با کد قالب تغییر داده‌ایم. `%c` آن عدد را به شکل نویسه نشان می‌دهد و `%i` به شکل عدد صحیح.

## بخشی از جدول ASCII

> **تألیفی:** درس‌نامه جدول کامل ASCII را در بخش String Length آورده است. اینجا فقط ردیف‌های لازم را خلاصه کرده‌ایم.

| نویسه | کد |
| --- | --- |
| `NUL` | ۰ |
| `!` | ۳۳ |
| `0` تا `9` | ۴۸ تا ۵۷ |
| `A` تا `Z` | ۶۵ تا ۹۰ |
| `a` تا `z` | ۹۷ تا ۱۲۲ |

> **توجه:** در جدول رسمی، نویسهٔ ۳۴ به شکل `”` و ۳۹ به شکل `’` (نقل‌قول خمیده) نمایش داده شده‌اند؛ در ASCII واقعی این دو `"` و `'` صاف‌اند (ناهمخوانی d28).

## اشتباه‌های رایج

- نوشتن نویسه با نقل‌قول دوتایی (`"H"`)؛ این رشته است، نه `char`. برای `char` نقل‌قول تکی لازم است: `'H'`.
- تصور این‌که `'0'` همان عدد ۰ است؛ کد ASCII آن ۴۸ است.

## جمع‌بندی

- `char` یک بایت است و آن بایت یک عدد را نگه می‌دارد.
- `%c` همان عدد را به شکل نویسه چاپ می‌کند و `%i` به شکل عدد.

## پیوندها

- قبلی: [ثابت سراسری و آرایه به‌عنوان آرگومان تابع](/kb/d/w02-n10)
- بعدی: [رشته، آرایه‌ای از نویسه‌ها و NUL](/kb/d/w02-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
