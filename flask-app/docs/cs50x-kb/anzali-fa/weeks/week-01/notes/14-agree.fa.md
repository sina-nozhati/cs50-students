---
id: w01-n14
type: note
title: 'agree.c: نویسه‌ها و عملگرهای منطقی (agree.c)'
title_fa: 'agree.c: نویسه‌ها و عملگرهای منطقی'
title_en: agree.c
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: agree.c
official_anchor: agreec
source_url: https://cs50.harvard.edu/x/notes/1/#agreec
source_refs:
- src-notes-1#agreec
- src-transcript-1
- src-short-operators
- src-srt-1
concept_ids:
- w01-c-char
- w01-c-equality-vs-assignment
- w01-c-logical-operators
prev: w01-n13
next: w01-n15
order: 14
video:
  youtube_id: SlqjA04_dpk
  start: '1:17:21'
  start_seconds: 4641
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=4641s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'agree'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# agree.c: نویسه‌ها و عملگرهای منطقی

> **منبع رسمی:** بخش «agree.c» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#agreec). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۷:۲۱ تا حدود ۱:۲۲:۳۳](https://www.youtube.com/watch?v=SlqjA04_dpk&t=4641s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برنامه‌ها اغلب پاسخ «بله» یا «نه» می‌گیرند. این بخش نوع `char`، تفاوت `==` و `=`، و **عملگرهای منطقی** (logical operators) را نشان می‌دهد.

## char در برابر string

- **رشته** (`string`) دنباله‌ای از نویسه‌هاست؛ `char` فقط **یک** نویسه است.
- برنامهٔ تازه را با `code agree.c` شروع کن.

```c
// Comparing against lowercase char

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'n')
    {
        printf("Not agreed.\n");
    }
}
```

- نویسهٔ تکی داخل **نقل‌قول تکی** می‌آید (`'y'`)، رشته داخل نقل‌قول دوتایی.
- `==` بررسی می‌کند که دو چیز **برابر** باشند. یک `=` تنها در C کار کاملاً متفاوتی می‌کند (انتساب).
- برای آزمایش: `make agree` و سپس `./agree`.

## بزرگ و کوچک

```c
// Comparing against lowercase and uppercase char

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'Y')
    {
        printf("Agreed.\n");
    }
    else
    {
        printf("Not agreed.\n");
    }
}
```

- حالا `Y` بزرگ هم پذیرفته می‌شود.
- درس‌نامه می‌گوید این کد **کارآمد نیست**: دو شاخه کار یکسانی می‌کنند.

## عملگر منطقی ||

```c
// Logical operators

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'Y' || c == 'y')
    {
        printf("Agreed.\n");
    }
    else
    {
        printf("Not agreed.\n");
    }
}
```

- `||` یعنی «یا». شرط وقتی درست است که دست‌کم یکی از دو طرف درست باشد.

## نکته‌های ویدئوی کوتاه Operators

| عملگر | نام | درست است وقتی |
| --- | --- | --- |
| `&&` | و (AND) | هر دو طرف درست باشند |
| `\|\|` | یا (OR) | دست‌کم یکی درست باشد |
| `!` | نقیض (NOT) | عبارت نادرست باشد |

- در C هر مقدار غیرصفر «درست» و صفر «نادرست» به شمار می‌آید.

## سخنرانی چه می‌گوید

**از سخنرانی:** چرا `&&` در اینجا درست نیست؟ چون متغیر `c` نمی‌تواند هم‌زمان هم `'Y'` باشد هم `'y'`؛ پس شرط با «و» هیچ‌وقت درست نمی‌شود.

## اشتباه‌های رایج

- `if (c = 'y')` به‌جای `if (c == 'y')`.
- نوشتن `"y"` با نقل‌قول دوتایی برای مقایسه با `char`.
- نوشتن `c == 'Y' || 'y'`؛ هر طرف `||` باید یک مقایسهٔ کامل باشد.

## جمع‌بندی

- `char` با نقل‌قول تکی؛ `string` با نقل‌قول دوتایی.
- `==` مقایسه است، `=` انتساب.
- `||` دو شرط را با «یا» ترکیب می‌کند و از تکرار کد جلوگیری می‌کند.

## پیوندها

- قبلی: [compare.c: مقایسهٔ دو عدد صحیح](/kb/d/w01-n13)
- بعدی: [حلقه‌ها و meow.c](/kb/d/w01-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
