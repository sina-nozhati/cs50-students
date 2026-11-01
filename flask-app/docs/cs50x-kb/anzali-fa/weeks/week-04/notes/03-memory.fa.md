---
id: w04-n03
type: note
title: حافظه و نشانی‌ها (Memory)
title_fa: حافظه و نشانی‌ها
title_en: Memory
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Memory
official_anchor: memory
source_url: https://cs50.harvard.edu/x/2026/notes/4/#memory
source_refs:
- src-notes-4#memory
- src-transcript-4
- src-srt-4
concept_ids:
- w04-c-0x-prefix
- w04-c-memory-addresses
prev: w04-n02
next: w04-n04
order: 3
video:
  youtube_id: db0H0U13YsA
  start: '11:44'
  start_seconds: 704
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=704s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'what is meant by memory'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# حافظه و نشانی‌ها

> **منبع رسمی:** بخش «Memory» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#memory). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۱:۴۴ تا حدود ۱۶:۰۲](https://www.youtube.com/watch?v=db0H0U13YsA&t=704s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هفته‌های پیش حافظه را مثل یک شبکه از بایت‌ها کشیدیم. این هفته به هر بایت یک **نشانی** (address) می‌دهیم. بدون این ایده، اشاره‌گرها، رشته‌ها و `malloc` معنا ندارند.

## شماره‌گذاری بایت‌ها با هگزادسیمال

- طرح هفته‌های قبل از بلوک‌های پشت سر هم حافظه را یادت هست؟ اگر این بلوک‌ها را با هگزادسیمال شماره‌گذاری کنیم، شکلی مثل تصویر درس‌نامه به دست می‌آید.
- اما ابهامی پیش می‌آید: آیا بلوک `10` یعنی **مکان** شمارهٔ ۱۰ در حافظه یا **مقدار** 10؟
- برای همین، طبق قرارداد، عددهای هگزادسیمال را با پیشوند `0x` می‌نویسند: `0x10` یعنی نشانی یا عدد هگزادسیمال، نه ده دهدهی.

## addresses.c

در ترمینال `code addresses.c` را بزن و این کد را بنویس:

```c
// Prints an integer

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", n);
}
```

- `n` با مقدار `50` جایی در حافظه ذخیره شده است.
- درس‌نامه این را این‌طور تصویر می‌کند: یک خانهٔ حافظه که مقدار 50 در آن است و نشانی‌اش با هگزادسیمال نوشته شده است.

> [!NOTE]
> **نکته**
> یک `int` چهار بایت جا می‌گیرد، پس `n` در واقع چهار بایت پشت سر هم را اشغال می‌کند. «نشانی `n`» نشانی اولین بایت از این چهار بایت است. اندازه‌ها را در هفتهٔ ۱ دیدی.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David همان «بوم حافظه» هفتهٔ قبل را دوباره نشان داد و گفت می‌توانیم بایت‌ها را به‌طور دلخواه ولی منطقی شماره‌گذاری کنیم: اولی 0، بعدی 1 و همین‌طور تا آخر، فقط این بار با هگزادسیمال.

## اشتباه‌های رایج

- فکر کردن به اینکه نشانی‌ها از ۱ شروع می‌شوند یا ترتیبشان مهم نیست؛ در تصویر درس‌نامه نشانی‌ها پشت سر هم‌اند.
- یکی گرفتن **مقدار** یک متغیر با **نشانی** آن. `n` مقدار 50 دارد؛ نشانی‌اش عدد دیگری است.

## جمع‌بندی

- هر بایت حافظه یک نشانی دارد که معمولاً با هگزادسیمال و پیشوند `0x` نوشته می‌شود.
- متغیر `n` هم مقدار دارد و هم جایی در حافظه، یعنی یک نشانی.

## پیوندها

- قبلی: [مبنای شانزده (هگزادسیمال)](/kb/d/w04-n02)
- بعدی: [اشاره‌گرها: & و *](/kb/d/w04-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
