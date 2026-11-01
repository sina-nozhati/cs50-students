---
id: w02-n12
type: note
title: 'رشته، آرایه‌ای از نویسه‌ها و NUL (Strings: arrays of chars and NUL)'
title_fa: رشته، آرایه‌ای از نویسه‌ها و NUL
title_en: 'Strings: arrays of chars and NUL'
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
- src-transcript-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-string-char-array
- w02-c-nul
prev: w02-n11
next: w02-n13
order: 12
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:38:41'
  start_seconds: 5921
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=5921s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'null'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# رشته، آرایه‌ای از نویسه‌ها و NUL

> **منبع رسمی:** بخش «Strings» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#strings). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۳۸:۴۱ تا حدود ۱:۴۲:۲۲](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=5921s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

یادت هست جلوی `string` در جدول اندازه‌ها علامت سؤال بود؟ اینجا پاسخ را می‌گیری: رشته آرایه‌ای از `char` است که با یک نویسهٔ ویژه تمام می‌شود.

## رشته و NUL

- درس‌نامه با تصویر نشان می‌دهد که رشته آرایه‌ای از نویسه‌هاست که با نخستین نویسه شروع می‌شود و با نویسه‌ای ویژه به نام **NUL** تمام می‌شود.
- **NUL** با یک L همان نویسهٔ `'\0'` است و با **NULL** با دو L فرق دارد.
- اگر همین آرایه را به شکل دهدهی تصور کنی: `72 73 33 0`.

> **منبع رسمی:** تصویرها: [hi with terminator](https://cs50.harvard.edu/x/notes/2/cs50Week2Slide116.png) و [hi with decimal](https://cs50.harvard.edu/x/notes/2/cs50Week2Slide117.png) (فقط پیوند).

## رشته به‌عنوان آرایه

```c
// Prints string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%s\n", s);
}
```

- همه‌چیز در یک `string` نگه داشته شده است.

```c
// Treats string as array

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%c%c%c\n", s[0], s[1], s[2]);
}
```

- `printf` سه مقدار از آرایه‌ای به نام `s` را نشان می‌دهد: `s[0]`، `s[1]` و `s[2]`. پس با رشته دقیقاً مثل آرایه رفتار می‌کنی.

## دیدن NUL

```c
// Prints string's ASCII codes, including NUL

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);
}
```

- با `%i` کدهای ASCII رشته چاپ می‌شوند، **از جمله NUL**: `72 73 33 0`.
- **تألیفی:** پس رشتهٔ سه‌حرفی `"HI!"` در حافظه **چهار** بایت می‌گیرد. طول یک رشتهٔ n نویسه‌ای در حافظه n + 1 بایت است.

## دو رشته

```c
// Multiple strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    string t = "BYE!";

    printf("%s\n", s);
    printf("%s\n", t);
}
```

- دو رشته اعلان و استفاده شده‌اند. در حافظه پشت‌سرهم قرار می‌گیرند و هرکدام NUL خودش را دارد (تصویر رسمی «hi and bye»، فقط پیوند).
- **از سخنرانی:** David می‌گوید `printf` باید بداند کجا بایستد: نویسه‌به‌نویسه چاپ می‌کند تا به پایان رشته، یعنی NUL، برسد. وقتی دو رشته پشت‌سرهم در حافظه‌اند، همین NUL مرز آن‌هاست.
- **از سخنرانی:** `\0` هشت بیت صفر است؛ مثل `\n` یک نویسهٔ گریز ویژه است، نه رقم ۰ که روی صفحه می‌بینی.

## اشتباه‌های رایج

- یکی دانستن NUL (نویسهٔ `'\0'`) و NULL (مفهومی که بعداً در درس می‌آید).
- فراموش کردن این‌که NUL هم یک بایت جا می‌گیرد.

## جمع‌بندی

- `string` آرایه‌ای از `char` است که آخرش `'\0'` می‌نشیند.
- هر نویسهٔ رشته را با `s[i]` می‌خوانی.

## پیوندها

- قبلی: [نویسه‌ها و ASCII](/kb/d/w02-n11)
- بعدی: [آرایه‌ای از رشته‌ها](/kb/d/w02-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
