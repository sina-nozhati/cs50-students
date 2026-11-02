---
id: w01-n05
type: note
title: 'از Scratch به C: printf و دنبالهٔ گریز (From Scratch to C)'
title_fa: 'از Scratch به C: printf و دنبالهٔ گریز'
title_en: From Scratch to C
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: From Scratch to C
official_anchor: from-scratch-to-c
source_url: https://cs50.harvard.edu/x/notes/1/#from-scratch-to-c
source_refs:
- src-notes-1#from-scratch-to-c
- src-srt-1
concept_ids:
- w01-c-printf
- w01-c-syntax
- w01-c-escape-sequence
- w01-c-recompile
prev: w01-n04
next: w01-n06
order: 5
video:
  youtube_id: SlqjA04_dpk
  start: '14:33'
  start_seconds: 873
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=873s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'tease apart'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# از Scratch به C: printf و دنبالهٔ گریز

> **منبع رسمی:** بخش «From Scratch to C» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#from-scratch-to-c). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۴:۳۳ تا حدود ۲۵:۱۱](https://www.youtube.com/watch?v=SlqjA04_dpk&t=873s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حالا می‌بینیم برنامهٔ `hello.c` چطور با بلوک‌های Scratch هم‌خوان است، و چرا جزئیاتی مثل `\n` مهم‌اند.

## say در Scratch، printf در C

- در Scratch بلوک `say` هر متنی را روی صفحه نشان می‌داد.
- در C تابع `printf` همین کار را می‌کند. خط اصلی برنامه این است:

```c
printf("hello, world\n");
```

درس‌نامه اجزای این خط را این‌طور توضیح می‌دهد:

- `printf` تابعی است که متن را چاپ می‌کند.
- `"hello, world\n"` آرگومان (ورودی) آن است و داخل نقل‌قول دوتایی می‌آید.
- `\n` یعنی «برو به خط بعد».
- خط با `;` پایان می‌یابد.

## اگر \n نباشد چه می‌شود؟

درس‌نامه نسخهٔ زیر را نشان می‌دهد:

```c
// \n is missing

#include <stdio.h>

int main(void)
{
    printf("hello, world");
}
```

بعد از `make hello` و `./hello`، علامت فرمان بعدی (`$`) درست کنار متن می‌چسبد، چون مکان‌نما به خط بعد نرفته است. یادت باشد: **بعد از هر تغییر باید دوباره کامپایل کنی.**

## دنباله‌های گریز

`\n` یک **دنبالهٔ گریز** (escape sequence) است: نویسه‌ای که مستقیم نمی‌شود تایپش کرد و با `\` شروع می‌شود. فهرست درس‌نامه:

```text
\n  create a new line
\r  return to the start of a line
\"  print a double quote
\'  print a single quote
\\  print a backslash
```

| دنباله | معنا |
| --- | --- |
| `\n` | خط تازه |
| `\r` | بازگشت به ابتدای خط (carriage return) |
| `\"` | نقل‌قول دوتایی |
| `\'` | نقل‌قول تکی |
| `\\` | خودِ بک‌اسلش |

## برنامهٔ اصلاح‌شده

درس‌نامه برنامه را به حالت اول برمی‌گرداند:

```c
// A program that says hello to the world

#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

## اشتباه‌های رایج

- فراموش کردن `;`: کامپایلر خطا می‌دهد.
- استفاده از نقل‌قول تکی برای متن؛ متن در C داخل `"` می‌آید.
- تغییر کد بدون `make` دوباره: برنامهٔ قدیمی اجرا می‌شود.

## جمع‌بندی

- `printf` معادل `say` است.
- `\n` مکان‌نما را به خط بعد می‌برد؛ دنباله‌های گریز با `\` شروع می‌شوند.

## پیوندها

- قبلی: [سلام دنیا در C: نوشتن، کامپایل و اجرا](/kb/d/w01-n04)
- بعدی: [فایل‌های سرآیند، کتابخانه‌ها و راهنمای CS50](/kb/d/w01-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
