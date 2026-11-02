---
id: w02-n07
type: note
title: 'چهار مرحلهٔ کامپایل: پیش‌پردازش، کامپایل، اسمبل، پیوند (Compiling: the four steps)'
title_fa: 'چهار مرحلهٔ کامپایل: پیش‌پردازش، کامپایل، اسمبل، پیوند'
title_en: 'Compiling: the four steps'
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
- src-transcript-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-preprocessing
- w02-c-compiling-step
- w02-c-assembling
- w02-c-linking
prev: w02-n06
next: w02-n08
order: 7
video:
  youtube_id: h5Gc1n8ZuU8
  start: '50:06'
  start_seconds: 3006
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=3006s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'preprocess'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# چهار مرحلهٔ کامپایل: پیش‌پردازش، کامپایل، اسمبل، پیوند

> **منبع رسمی:** بخش «Compiling» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#compiling). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۰:۰۶ تا حدود ۱:۰۲:۳۰](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=3006s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

«کامپایل» در واقع یک گام نیست؛ درس‌نامه آن را **چهار مرحلهٔ اصلی** می‌داند. دانستن این مرحله‌ها کمک می‌کند پیام‌های خطا را بهتر بفهمی؛ مثلاً بدانی خطا در پیش‌پردازش است یا در پیوند.

## مرحلهٔ ۱: پیش‌پردازش

- در **پیش‌پردازش** (`preprocessing`) فایل‌های سرآیندی که با `#` مشخص شده‌اند (مثل `#include <cs50.h>`) عملاً در فایل تو **کپی و جای‌گذاری** می‌شوند.
- کد `cs50.h` در برنامه‌ات کپی می‌شود. همین‌طور کدی که جایی روی کامپیوتر در `stdio.h` هست.
- نتیجه را می‌شود این‌طور تصور کرد:

```c
string get_string(string prompt);
int printf(string format, ...);

int main(void)
{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
```

- حالا کامپایلر پیش از `main` می‌داند `get_string` و `printf` چه شکلی دارند.

## مرحلهٔ ۲: کامپایل

- در مرحلهٔ **کامپایل** (`compiling`) برنامه به **کد اسمبلی** (`assembly code`) تبدیل می‌شود:

```text
...
main:
    .cfi_startproc
# BB#0:
    pushq    %rbp
.Ltmp0:
    .cfi_def_cfa_offset 16
.Ltmp1:
    .cfi_offset %rbp, -16
    movq    %rsp, %rbp
.Ltmp2:
    .cfi_def_cfa_register %rbp
    subq    $16, %rsp
    xorl    %eax, %eax
    movl    %eax, %edi
    movabsq    $.L.str, %rsi
    movb    $0, %al
    callq    get_string
    movabsq    $.L.str.1, %rdi
    movq    %rax, -8(%rbp)
    movq    -8(%rbp), %rsi
    movb    $0, %al
    callq    printf
    ...
```

- **تألیفی:** لازم نیست اسمبلی بخوانی. کافی است ببینی نام‌هایی مثل `get_string` و `printf` هنوز در آن پیدا هستند (`callq get_string`).

## مرحلهٔ ۳: اسمبل

- در **اسمبل** (`assembling`)، **اسمبلر** (ابزاری در زنجیرهٔ کامپایل) کد اسمبلی را به کد ماشین تبدیل می‌کند:

```text
01111111010001010100110001000110
00000010000000010000000100000000
00000000000000000000000000000000
00000000000000000000000000000000
00000001000000000011111000000000
00000001000000000000000000000000
00000000000000000000000000000000
...
```

## مرحلهٔ ۴: پیوند

- در مرحلهٔ **پیوند** (`linking`) کد ماشینی از پیش‌کامپایل‌شدهٔ کتابخانه‌هایی که include کرده‌ای با کد تو ترکیب می‌شود و فایل اجرایی نهایی بیرون می‌آید:

```text
01111111010001010100110001000110
00000010000000010000000100000000
00000000000000000000000000000000
00000000000000000000000000000000
00000001000000000011111000000000
00000001000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
10100000000000100000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
01000000000000000000000000000000
00000000000000000100000000000000
00001010000000000000000100000000
01010101010010001000100111100101
01001000100000111110110000010000
00110001110000001000100111000111
01001000101111100000000000000000
00000000000000000000000000000000
00000000000000001011000000000000
11101000000000000000000000000000
00000000010010001011111100000000
00000000000000000000000000000000
00000000000000000000000001001000
...
```

> **از سخنرانی:** David سه فایل را تصویر می‌کند: `hello.c` تو، `cs50.c` و `stdio.c`؛ همه به کد ماشین تبدیل و در یک فایل `hello` ترکیب می‌شوند. اسم فایل‌های کتابخانه در این مثال برای ساده‌سازی است.

## خلاصهٔ چهار مرحله

| مرحله | ورودی | خروجی |
| --- | --- | --- |
| پیش‌پردازش | `hello.c` با `#include` | کد C با اعلان‌های کپی‌شده |
| کامپایل | کد C | کد اسمبلی |
| اسمبل | کد اسمبلی | کد ماشین |
| پیوند | کد ماشین تو و کتابخانه‌ها | فایل اجرایی `hello` |

> **تألیفی:** جدول بالا جمع‌بندی ما از متن درس‌نامه است. خطای `undefined reference` معمولاً یعنی مرحلهٔ پیوند کتابخانه‌ای را پیدا نکرده است؛ مثلاً `-lcs50` جا افتاده.

## اشتباه‌های رایج

- یکی دانستن «کامپایل» به معنای کل فرایند با مرحلهٔ دوم آن.
- تصور این‌که `#include` کل کتابخانه را کامپایل می‌کند؛ پیش‌پردازش اعلان‌ها را می‌آورد و پیوند، کد آماده را.

## جمع‌بندی

- ترتیب: پیش‌پردازش ← کامپایل ← اسمبل ← پیوند.
- `make` و `clang` همهٔ این مرحله‌ها را با یک فرمان انجام می‌دهند.

## پیوندها

- قبلی: [کامپایل: make و clang](/kb/d/w02-n06)
- بعدی: [حافظه و اندازهٔ انواع داده](/kb/d/w02-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
