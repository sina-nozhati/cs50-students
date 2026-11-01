---
id: w02-n06
type: note
title: 'کامپایل: make و clang (Compiling: make and clang)'
title_fa: 'کامپایل: make و clang'
title_en: 'Compiling: make and clang'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Compiling
official_anchor: compiling
source_url: https://cs50.harvard.edu/x/2026/notes/2/#compiling
source_refs:
- src-notes-2#compiling
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-clang
- w02-c-link-flag
- w02-c-make-vs-clang
prev: w02-n05
next: w02-n07
order: 6
video:
  youtube_id: h5Gc1n8ZuU8
  start: '41:57'
  start_seconds: 2517
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=2517s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'clang'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# کامپایل: make و clang

> **منبع رسمی:** بخش «Compiling» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#compiling). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۱:۵۷ تا حدود ۵۰:۰۶](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=2517s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

از هفتهٔ ۱ هر برنامه را با `make` ساختی. این یادداشت نشان می‌دهد `make` پشت صحنه چه کسی را صدا می‌زند: **کامپایلر** `clang`.

## یادآوری: کامپایلر

- هفتهٔ پیش دیدی که **کامپایلر** (`compiler`) برنامه‌ای تخصصی است که **کد منبع** (`source code`) را به **کد ماشین** (`machine code`) تبدیل می‌کند.

```text
flowchart LR
    in["source code"] --> BOX[" compiler "]
    BOX --> out["machine code"]
```

> **توجه:** در درس‌نامهٔ رسمی این نمودار به شکل تصویر یا کد نمودار آمده است. اینجا متن همان نمودار را بدون ترسیم نگه داشته‌ایم.

- برنامه‌ای مثل این را در نظر بگیر:

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

- کامپایلر آن را به کد ماشینی تبدیل می‌کند که چیزی شبیه این است:

```text
01010100 01001000 01001001 01010011
00100000 01001001 01010011 00100000
01000011 01010011 00110101 00110000
```

- درس‌نامه یادآوری می‌کند که این فقط **نمایشی** است؛ کد ماشین واقعی همین برنامه خیلی بلندتر است.

## clang

- VS Code، محیط برنامه‌نویسی CS50، از کامپایلری به نام `clang` استفاده می‌کند، کوتاه‌شدهٔ «C Language Family Frontend».
- می‌توانی در ترمینال بنویسی: `clang -o hello hello.c`.
- `-o hello hello.c` **آرگومان‌های خط فرمان** (`command-line arguments`) هستند که به `clang` داده می‌شوند. `-o hello` یعنی «خروجی را `hello` نام بگذار».
- بعد `./hello` برنامه را درست اجرا می‌کند.

## وقتی کتابخانهٔ CS50 در کار است

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
```

- برای کامپایل این کد باید بنویسی: `clang -o hello hello.c -lcs50`.
- **تألیفی:** `-lcs50` به `clang` می‌گوید کد کتابخانهٔ CS50 را هم **پیوند** بزند؛ معنای دقیق پیوند را در یادداشت بعد می‌بینی.

## make چه می‌کند

- `make hello` فرمانی را اجرا می‌کند که `clang` را صدا می‌زند و فایل خروجی قابل اجرا می‌سازد.
- VS Code از پیش طوری تنظیم شده که `make` شمار زیادی آرگومان خط فرمان را همراه `clang` اجرا کند، تا کار تو راحت باشد.
- درس‌نامه صریح می‌گوید: این توضیح فقط برای فهم عمیق‌تر است؛ استفاده از `make` در CS50 کاملاً درست و **مورد انتظار** است.

## اشتباه‌های رایج

- فراموش کردن `-lcs50` وقتی با `clang` دستی کامپایل می‌کنی و از `get_string` استفاده کرده‌ای.
- جابه‌جا نوشتن نام خروجی و نام فایل: پس از `-o` نام **خروجی** می‌آید.

## جمع‌بندی

- `clang -o hello hello.c` همان کاری را می‌کند که `make hello`، و `make` آرگومان‌های لازم را خودش اضافه می‌کند.
- واژه‌هایی که پس از نام برنامه در خط فرمان می‌نویسی، آرگومان خط فرمان‌اند؛ این ایده در پایان هفته به برنامه‌های خودت هم می‌رسد.

## پیوندها

- قبلی: [debug50، نقطهٔ توقف و اردک پلاستیکی](/kb/d/w02-n05)
- بعدی: [چهار مرحلهٔ کامپایل: پیش‌پردازش، کامپایل، اسمبل، پیوند](/kb/d/w02-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
