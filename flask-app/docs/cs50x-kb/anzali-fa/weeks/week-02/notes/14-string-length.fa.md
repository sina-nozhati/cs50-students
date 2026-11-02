---
id: w02-n14
type: note
title: 'طول رشته و strlen (String Length: strlen)'
title_fa: طول رشته و strlen
title_en: 'String Length: strlen'
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
- src-transcript-2
- src-srt-2
concept_ids:
- w02-c-string-length
- w02-c-strlen
prev: w02-n13
next: w02-n15
order: 14
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:48:15'
  start_seconds: 6495
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=6495s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'length.C'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# طول رشته و strlen

> **منبع رسمی:** بخش «String Length» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#string-length). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۸:۱۵ تا حدود ۱:۵۹:۴۶](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=6495s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

یکی از رایج‌ترین مسئله‌های برنامه‌نویسی، به‌ویژه در C، پیدا کردن **طول رشته** است. حالا که NUL را می‌شناسی، خودت می‌توانی بشماری.

## شمردن تا NUL

درس‌نامه می‌خواهد با `code length.c` بنویسی:

```c
// Determines the length of a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");

    // Count number of characters up until '\0' (aka NUL)
    int n = 0;
    while (name[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}
```

- حلقه آن‌قدر ادامه می‌یابد تا به نویسهٔ NUL برسد.
- **از سخنرانی:** David یک «حالت مرزی» (`corner case`) هم آزمود: فقط Enter زد و طول `0` چاپ شد، چون نخستین خانهٔ رشتهٔ خالی خود NUL است.

## انتزاع در یک تابع

```c
// Determines the length of a string using a function

#include <cs50.h>
#include <stdio.h>

int string_length(string s);

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");
    int length = string_length(name);
    printf("%i\n", length);
}

int string_length(string s)
{
    // Count number of characters up until '\0' (aka NUL)
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    return n;
}
```

- تابع تازه‌ای به نام `string_length` نویسه‌ها را تا یافتن NUL می‌شمارد.
- پیش‌نمونهٔ `int string_length(string s);` بالای `main` آمده و بدنهٔ تابع پایین فایل است؛ همان الگوی پیش‌نمونهٔ هفتهٔ ۱.
- تابع طول را با `return n` به `main` برمی‌گرداند.

## strlen

چون این مسئله خیلی رایج است، برنامه‌نویسان دیگر کدی در کتابخانهٔ `string.h` نوشته‌اند که طول رشته را پیدا می‌کند:

```c
// Determines the length of a string using a function

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");
    int length = strlen(name);
    printf("%i\n", length);
}
```

- کتابخانهٔ `string.h` بالای فایل include شده است.
- تابع `strlen` از همین کتابخانه طول رشته‌ای را که به آن داده شود حساب می‌کند. NUL شمرده نمی‌شود.
- درس‌نامه می‌گوید کد ما می‌تواند **روی شانهٔ برنامه‌نویسان پیشین** بایستد و از کتابخانه‌هایشان استفاده کند.

## اشتباه‌های رایج

- فراموش کردن `#include <string.h>` پیش از استفاده از `strlen`.
- انتظار این‌که `strlen("HI!")` چهار باشد؛ سه است، چون NUL شمرده نمی‌شود.

## جمع‌بندی

- طول رشته یعنی تعداد نویسه‌ها پیش از `'\0'`.
- `strlen` از `string.h` همین را برایت می‌شمارد.

## پیوندها

- قبلی: [آرایه‌ای از رشته‌ها](/kb/d/w02-n13)
- بعدی: [بزرگ‌کردن حروف و ctype.h](/kb/d/w02-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
