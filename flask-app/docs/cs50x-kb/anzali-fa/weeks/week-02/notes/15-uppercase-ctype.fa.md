---
id: w02-n15
type: note
title: 'بزرگ‌کردن حروف و ctype.h (String Length: uppercase and ctype.h)'
title_fa: بزرگ‌کردن حروف و ctype.h
title_en: 'String Length: uppercase and ctype.h'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: String Length
official_anchor: string-length
source_url: https://cs50.harvard.edu/x/2026/notes/2/#string-length
source_refs:
- src-notes-2#string-length
- src-section-2
- src-manual
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-ascii-case
- w02-c-ctype
prev: w02-n14
next: w02-n16
order: 15
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:59:46'
  start_seconds: 7186
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=7186s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'uppercase'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# بزرگ‌کردن حروف و ctype.h

> **منبع رسمی:** بخش «String Length» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#string-length). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۹:۴۶ تا حدود ۲:۰۷:۴۴](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=7186s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حالا که می‌دانی نویسه‌ها عددند، می‌توانی با آن‌ها **حساب** کنی. این یادداشت یک رشته را به حروف بزرگ تبدیل می‌کند؛ اول با حساب ASCII، بعد با کتابخانهٔ `ctype.h`. همین مهارت در Caesar و Substitution به کارت می‌آید.

## نسخهٔ ۱: کم کردن ۳۲

درس‌نامه می‌خواهد با `code uppercase.c` بنویسی:

```c
// Uppercases a string

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
```

- این کد روی تک‌تک مقدارهای رشته **پیمایش** (`iterate`) می‌کند.
- اگر نویسه حرف کوچک باشد، ۳۲ از کد ASCII آن کم می‌شود تا به حرف بزرگ تبدیل شود.
- در جدول ASCII، `a` برابر ۹۷ و `A` برابر ۶۵ است: فاصله دقیقاً ۳۲.
- درس‌نامه تأکید می‌کند: کم کردن ۳۲ فقط برای حروف ASCII از a تا z کار می‌کند، نه برای حروف تکیه‌دار یا غیر ASCII.

> **تألیفی:** به `int i = 0, n = strlen(s)` دقت کن. طول رشته **یک بار** حساب و در `n` نگه داشته می‌شود، نه در هر دور حلقه. جلسهٔ حل تمرین همین را یک نکتهٔ طراحی می‌داند؛ [جلسهٔ حل تمرین ۲](/kb/d/w02-sec) را ببین.

## نسخهٔ ۲: ctype.h

```c
// Uppercases string using ctype library (and an unnecessary condition)

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (islower(s[i]))
        {
            printf("%c", toupper(s[i]));
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
```

- برنامه روی هر نویسه پیمایش می‌کند. `s[i]` به تابع `toupper` داده می‌شود و هر نویسه، **اگر کوچک باشد**، بزرگ می‌شود.
- `islower` بررسی می‌کند که نویسه حرف کوچک است یا نه.

## نسخهٔ ۳: بدون شرط اضافه

درس‌نامه می‌گوید `toupper` خودش می‌داند فقط حروف کوچک را بزرگ کند. پس:

```c
// Uppercases string using ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}
```

- همهٔ قابلیت‌های کتابخانهٔ `ctype` را در [Manual Pages](https://manual.cs50.io/#ctype.h) بخوان.

## اشتباه‌های رایج

- کم کردن ۳۲ از هر نویسه، حتی `!` یا فاصله.
- فراموش کردن `#include <ctype.h>`.
- تصور این‌که `toupper(s[i])` خود رشته را تغییر می‌دهد؛ نویسهٔ تازه را **برمی‌گرداند**.

## جمع‌بندی

- `'a' - 32` برابر `'A'` است، اما `toupper` امن‌تر و خواناتر است.
- برای هر تابع کتابخانه‌ای اول صفحهٔ راهنمایش را بخوان.

## پیوندها

- قبلی: [طول رشته و strlen](/kb/d/w02-n14)
- بعدی: [آرگومان‌های خط فرمان: argc و argv](/kb/d/w02-n16)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
