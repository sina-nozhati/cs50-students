---
id: w01-n04
type: note
title: 'سلام دنیا در C: نوشتن، کامپایل و اجرا (Hello World)'
title_fa: 'سلام دنیا در C: نوشتن، کامپایل و اجرا'
title_en: Hello World
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Hello World
official_anchor: hello-world
source_url: https://cs50.harvard.edu/x/notes/1/#hello-world
source_refs:
- src-notes-1#hello-world
- src-transcript-1
- src-pset-1
- src-srt-1
concept_ids:
- w01-c-code-make-run
- w01-c-main
- w01-c-debugging-errors
prev: w01-n03
next: w01-n05
order: 4
video:
  youtube_id: SlqjA04_dpk
  start: '9:42'
  start_seconds: 582
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=582s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'code hello.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# سلام دنیا در C: نوشتن، کامپایل و اجرا

> **منبع رسمی:** بخش «Hello World» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#hello-world). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۹:۴۲ تا حدود ۱۴:۳۳](https://www.youtube.com/watch?v=SlqjA04_dpk&t=582s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اولین برنامهٔ C را با سه فرمان می‌نویسی، می‌سازی و اجرا می‌کنی. این چرخه را در تمام هفته تکرار خواهی کرد.

## سه فرمان

درس‌نامه این فرمان‌ها را به ترتیب در ترمینال می‌آورد:

```text
code hello.c

make hello

./hello
```

- `code hello.c` یک فایل تازه به نام `hello.c` در ویرایشگر باز می‌کند (یا می‌سازد).
- `make hello` کد را کامپایل می‌کند. توجه کن: `make hello` می‌نویسی، نه `make hello.c`. فرمان `make` خودش دنبال `hello.c` می‌گردد.
- `./hello` برنامهٔ ساخته‌شده را اجرا می‌کند. `.` یعنی «همین پوشه».

## برنامهٔ رسمی

درس‌نامه از تو می‌خواهد کد زیر را دقیقاً بنویسی:

```c
// A program that says hello to the world

#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

بعد از `make hello` و `./hello` باید `hello, world` را در ترمینال ببینی.

درس‌نامه دقت می‌کند که نام فایل تماماً با حروف کوچک و با پسوند `.c` نوشته شود، و هر نویسه در کد هدفی دارد؛ اگر نادرست تایپ شود، برنامه اجرا نمی‌شود.

## دو فایل در کاوشگر

حالا در کاوشگر فایل دو فایل می‌بینی:

- `hello.c`: کد منبع، که انسان و کامپایلر آن را می‌خوانند.
- `hello`: فایل **اجرایی** (executable) که کد ماشین دارد و کامپیوتر مستقیماً اجرایش می‌کند.

## اگر خطا دیدی

- اگر `make hello` خطا داد، درس‌نامه می‌گوید کد را دوباره با دقت بررسی کن؛ کد تو باید **دقیقاً** مثل نمونه باشد.
- جزئی‌ترین تفاوت، مثل یک نقطه‌ویرگول جاافتاده، کامپایل را متوقف می‌کند.
- **از صفحهٔ پرابلم‌ست ۱:** اگر هنگام کامپایل با `make` خطا دیدی، اول روی درست کردن **اولین** خطا تمرکز کن؛ در صورت نیاز صفحه را به بالا بکش تا آن را ببینی.

## سخنرانی چه می‌گوید

**از سخنرانی:** بخش `int main(void)` با بلوک «when green flag clicked» در Scratch هم‌خوان است: نقطه‌ای که برنامه از آنجا شروع می‌شود. معنای کامل `int` و `void` را در هفته‌های بعد می‌بینی.

## اشتباه‌های رایج

- نوشتن `make hello.c` به‌جای `make hello`.
- اجرای `hello` به‌جای `./hello`.
- فراموش کردن ذخیرهٔ فایل یا کامپایل دوباره پس از ویرایش.

## جمع‌بندی

- چرخهٔ هر برنامه: `code` ← `make` ← `./`.
- کد را دقیقاً بنویس؛ پیام خطا را از اولی بخوان.

## پیوندها

- قبلی: [VS Code برای CS50: فایل‌ها، ویرایشگر و ترمینال](/kb/d/w01-n03)
- بعدی: [از Scratch به C: printf و دنبالهٔ گریز](/kb/d/w01-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
