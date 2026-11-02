---
id: w04-n10
type: note
title: 'Valgrind: یافتن خطاهای حافظه (Valgrind)'
title_fa: 'Valgrind: یافتن خطاهای حافظه'
title_en: Valgrind
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Valgrind
official_anchor: valgrind
source_url: https://cs50.harvard.edu/x/2026/notes/4/#valgrind
source_refs:
- src-notes-4#valgrind
- src-transcript-4
- src-pset-4
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-sizeof
- w04-c-valgrind
- w04-c-buffer-overflow-write
- w04-c-memory-leak
prev: w04-n09
next: w04-n11
order: 10
video:
  youtube_id: db0H0U13YsA
  start: '1:14:04'
  start_seconds: 4444
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=4444s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'another tool called Valgrind'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# Valgrind: یافتن خطاهای حافظه

> **منبع رسمی:** بخش «Valgrind» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#valgrind). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۴:۰۴ تا حدود ۱:۲۳:۲۱](https://www.youtube.com/watch?v=db0H0U13YsA&t=4444s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

خطاهای حافظه اغلب بی‌صدا هستند: برنامه اجرا می‌شود و جواب درست هم می‌دهد، ولی مشکل دارد. **Valgrind** ابزاری است که این خطاهای پنهان را آشکار می‌کند.

## Valgrind

*Valgrind* ابزاری است که بررسی می‌کند برنامه‌ای که در آن از `malloc` استفاده کرده‌ای مشکل حافظه دارد یا نه. به‌خصوص بررسی می‌کند که همهٔ حافظه‌ای را که گرفته‌ای `free` کرده‌ای یا نه. این کد `memory.c` را ببین:

```c
// Demonstrates memory errors via valgrind

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[1] = 72;
    x[2] = 73;
    x[3] = 33;
}
```

- اجرای این برنامه هیچ خطایی نشان نمی‌دهد. با اینکه `malloc` برای یک آرایه حافظه گرفته، کد آن را `free` نکرده است.
- `3 * sizeof(int)` یعنی جا برای سه عدد صحیح؛ `sizeof` اندازهٔ یک نوع را به بایت می‌دهد.

اگر `make memory` و بعد `valgrind ./memory` را بزنی، گزارشی می‌گیری که نشان می‌دهد کجا حافظه گم شده است:

- یک خطا این است که مقدار `33` را در `x[3]` گذاشتیم، در حالی که فقط آرایه‌ای به اندازهٔ `3` گرفته بودیم (`x[0]`، `x[1]` و `x[2]`).
- خطای دیگر این است که `x` هیچ‌وقت آزاد نشده است.

با آزاد کردن `x` کد را درست می‌کنیم:

```c
// Demonstrates memory errors via valgrind

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;
    free(x);
}
```

- حالا اجرای دوبارهٔ valgrind هیچ نشت حافظه یا خطایی نشان نمی‌دهد.

> [!NOTE]
> **نکته**
> روی cs50.dev، `valgrind` نصب است. ما برای ساخت این بسته همین دو برنامه را با valgrind روی یک ماشین لینوکسی اجرا کردیم (تألیفی): نسخهٔ اول ۲ خطا گزارش داد، یکی «Invalid write of size 4» برای `x[3]` و دیگری «12 bytes ... definitely lost»؛ نسخهٔ دوم خطای صفر و «All heap blocks were freed». جزئیات در `validation/compile-checks.week-04.json` است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David خلاصهٔ نشت را در خروجی Valgrind خواند: «definitely lost 12 bytes in one block». او گفت 12 بایت باید آشنا باشد: هر `int` چهار بایت است و ما سه تا گرفتیم.
- **از سخنرانی:** او گفت خروجی Valgrind بسیار پرحرف است، ولی بخش مهمش شمارهٔ خطی است که منشأ خطاست؛ مثل ردپایی که تو را به سمت باگ می‌برد.

## اشتباه‌های رایج

- فکر کردن به اینکه چون برنامه درست اجرا شد، خطای حافظه ندارد.
- نوشتن `malloc(3)` به‌جای `malloc(3 * sizeof(int))`؛ این فقط ۳ بایت است، نه جای سه `int`.
- دیدن «definitely lost» و نادیده گرفتنش.

## جمع‌بندی

- `valgrind ./program` نوشتن بیرون از محدوده و نشت حافظه را گزارش می‌دهد.
- `sizeof(int)` اندازهٔ یک `int` است و `malloc` باید با آن ضرب شود.
- اگر از `malloc` استفاده می‌کنی، بی‌نشت بودن را با Valgrind بسنج؛ پرابلم‌ست‌های این هفته هم همین را می‌خواهند.

## پیوندها

- قبلی: [malloc، free، strcpy و NULL](/kb/d/w04-n09)
- بعدی: [مقدارهای زباله و Binky](/kb/d/w04-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
