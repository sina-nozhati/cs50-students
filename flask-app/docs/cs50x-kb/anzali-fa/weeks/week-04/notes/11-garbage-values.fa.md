---
id: w04-n11
type: note
title: مقدارهای زباله و Binky (Garbage Values and Binky)
title_fa: مقدارهای زباله و Binky
title_en: Garbage Values and Binky
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Garbage Values
official_anchor: garbage-values
source_url: https://cs50.harvard.edu/x/2026/notes/4/#garbage-values
source_refs:
- src-notes-4#garbage-values
- src-transcript-4
- src-notes-4#pointer-fun-with-binky
- src-binky
- src-srt-4
concept_ids:
- w04-c-garbage-values
- w04-c-uninitialized-pointer
prev: w04-n10
next: w04-n12
order: 11
video:
  youtube_id: db0H0U13YsA
  start: '1:23:21'
  start_seconds: 5001
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=5001s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'create a program called Garbage.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مقدارهای زباله و Binky

> **منبع رسمی:** بخش «Garbage Values» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#garbage-values). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۳:۲۱ تا حدود ۱:۳۴:۴۴](https://www.youtube.com/watch?v=db0H0U13YsA&t=5001s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حافظه‌ای که می‌گیری «خالی» نیست. اگر قبل از خواندن به آن مقدار ندهی، هر چه از قبل آنجا بوده می‌خوانی. همین دربارهٔ اشاره‌گرها خطرناک‌تر است.

## مقدارهای زباله

- وقتی از کامپایلر بلوکی از حافظه می‌خواهی، هیچ تضمینی نیست که خالی باشد.
- کاملاً ممکن است حافظه‌ای که گرفتی قبلاً استفاده شده باشد. برای همین ممکن است مقدارهای *بی‌معنی* یا **زباله** (garbage values) ببینی. این نتیجهٔ گرفتن حافظه بدون مقداردهی اولیه است. این کد `garbage.c` را ببین:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int scores[1024];
    for (int i = 0; i < 1024; i++)
    {
        printf("%i\n", scores[i]);
    }
}
```

- این کد ۱۰۲۴ مکان حافظه برای آرایه می‌گیرد، اما حلقهٔ `for` احتمالاً نشان می‌دهد که همهٔ مقدارها `0` نیستند.
- بهترین کار این است که همیشه حواست به احتمال مقدارهای زباله باشد، وقتی بلوک‌های حافظه را با صفر یا مقدار دیگری مقداردهی نکرده‌ای.

> [!WARNING]
> **هشدار**
> اشاره‌گری که مقداردهی نشده، یک **نشانی زباله** دارد. نوشتن در `*p` در این حالت یعنی نوشتن در جای نامعلومی از حافظه. اول اشاره‌گر را به جایی معتبر بفرست، مثلاً با `&` یا `malloc`، بعد از آن استفاده کن.

## Binky و اشاره‌گرها

درس‌نامه می‌گوید در کلاس [ویدئویی از دانشگاه استنفورد](https://www.youtube.com/watch?v=5VnDaHBi8dM) دیدیم که به تصور و فهم اشاره‌گرها کمک می‌کند (فقط پیوند).

## سخنرانی چه می‌گوید

- **از سخنرانی:** ویدئو یک خمیربازی (claymation) از Nick Parlante در استنفورد بود به اسم Binky. در آن، دو اشاره‌گر `x` و `y` تعریف می‌شوند؛ برای `x` یک «pointee» (حافظه‌ای که به آن اشاره کند) گرفته می‌شود ولی برای `y` نه.
- **از سخنرانی:** وقتی Binky سعی می‌کند عدد 13 را از طریق `y` ذخیره کند، کار خراب می‌شود؛ چون ساختن pointee مرحلهٔ جداگانه‌ای است که برای `y` هیچ‌وقت انجام نشده بود. درس: dereference کردن اشاره‌گری که به جایی معتبر اشاره نمی‌کند، فاجعه است.

## اشتباه‌های رایج

- انتظار صفر بودن آرایه‌ای که مقداردهی نشده است.
- تعریف اشاره‌گر و نوشتن فوری در `*p` بدون اینکه به حافظه‌ای معتبر اشاره کند.

## جمع‌بندی

- حافظهٔ مقداردهی‌نشده ممکن است مقدارهای زباله داشته باشد.
- اشاره‌گر هم تا وقتی به pointee معتبری اشاره نکند، نباید dereference شود.

## پیوندها

- قبلی: [Valgrind: یافتن خطاهای حافظه](/kb/d/w04-n10)
- بعدی: [جابه‌جایی، پشته و هیپ](/kb/d/w04-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
