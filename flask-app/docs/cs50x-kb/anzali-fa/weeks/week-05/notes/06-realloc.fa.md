---
id: w05-n06
type: note
title: 'realloc و هزینهٔ کپی (Arrays: realloc)'
title_fa: realloc و هزینهٔ کپی
title_en: 'Arrays: realloc'
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Arrays
official_anchor: arrays
source_url: https://cs50.harvard.edu/x/2026/notes/5/#arrays
source_refs:
- src-notes-5#arrays
- src-transcript-5
- src-manual
- src-srt-5
concept_ids:
- w05-c-realloc
- w05-c-realloc-null
- w05-c-overallocation
prev: w05-n05
next: w05-n07
order: 6
video:
  youtube_id: PmAI76OGE_E
  start: '27:37'
  start_seconds: 1657
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=1657s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'called Reallock'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# realloc و هزینهٔ کپی

> **منبع رسمی:** بخش «Arrays» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#arrays). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۷:۳۷ تا حدود ۳۲:۱۱](https://www.youtube.com/watch?v=PmAI76OGE_E&t=1657s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`realloc` همان کار کپی دستی را برایت انجام می‌دهد، ولی قاعدهٔ `tmp` و بررسی `NULL` هنوز پابرجاست. این یادداشت پایان داستان آرایه‌های پویا و آغاز انگیزهٔ فهرست پیوندی است.

## realloc

- یکی از راه‌های کپی کردن آرایه بدون حلقهٔ `for` استفاده از `realloc` است:

```c
// Implements a list of numbers with an array of dynamic size using realloc

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // List of size 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Initialize list of size 3 with numbers
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Resize list to be of size 4
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }
    list = tmp;

    // Add number to list
    list[3] = 4;

    // Print list
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Free list
    free(list);
    return 0;
}
```

- فهرست با `realloc` به آرایه‌ای تازه بازتخصیص داده می‌شود.
- شاید وسوسه شوی خیلی بیشتر از نیاز حافظه بگیری، مثلاً ۳۰ عضو به‌جای ۳ یا ۴. اما این طراحی بدی است، چون منابع سیستم را بی‌جهت مصرف می‌کند. از آن گذشته، تضمینی هم نیست که روزی بیش از ۳۰ عضو لازم نشود.

> [!WARNING]
> **هشدار**
> هیچ‌وقت ننویس `list = realloc(list, ...)`. اگر `realloc` شکست بخورد، `NULL` برمی‌گرداند و به حافظهٔ اصلی دست نمی‌زند؛ آن وقت `list` را با `NULL` پوشانده‌ای و نشانی حافظهٔ اصلی را برای همیشه گم کرده‌ای. برای همین در `list2.c` نتیجه اول در `tmp` می‌رود.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت `realloc` «باهوش‌تر» است: اگر بتواند، همان تکهٔ موجود را بزرگ می‌کند؛ اگر جا نباشد، تکه‌ای تازه پیدا می‌کند و داده‌ها را **خودش** کپی می‌کند.
- **از سخنرانی:** او اعتراف کرد بار اول آرگومان اول `realloc` را فراموش کرده بود؛ طبق مستندات، باید نشانی تکه‌ای را که پیش‌تر `malloc` کرده‌ای به آن بدهی.
- **از سخنرانی:** در پاسخ به پرسشی گفت `realloc` می‌داند چقدر کپی کند، چون کتابخانهٔ استاندارد حساب تکه‌هایی را که قبلاً تخصیص داده نگه می‌دارد، مثل یک جدول جست‌وجو.
- **از سخنرانی:** پس از استراحت جمع‌بندی کرد: بزرگ کردن با `malloc` یا `realloc` شدنی است، اما اگر به‌جای ۳ مقدار، ۳ میلیون مقدار باشد، کپی کردن وقت زیادی می‌گیرد.

برای جزئیات `realloc` به [manual.cs50.io](https://manual.cs50.io/) سر بزن.

## اشتباه‌های رایج

- نوشتن `list = realloc(list, ...)` بدون متغیر موقت.
- فراموش کردن بررسی `NULL` پس از `realloc`.
- گرفتن حافظهٔ خیلی زیاد «برای احتیاط»؛ درس‌نامه این را طراحی بد می‌داند.

## جمع‌بندی

- `realloc` حلقهٔ کپی را حذف می‌کند، اما بررسی `NULL` و متغیر `tmp` همچنان لازم است.
- هزینهٔ کپی در آرایه‌های بزرگ انگیزهٔ ساختاری است که لازم نباشد چیزی را جابه‌جا کند: فهرست پیوندی.

## پیوندها

- قبلی: [بزرگ کردن آرایه با malloc و کپی](/kb/d/w05-n05)
- بعدی: [گره و عملگر پیکان (->)](/kb/d/w05-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
