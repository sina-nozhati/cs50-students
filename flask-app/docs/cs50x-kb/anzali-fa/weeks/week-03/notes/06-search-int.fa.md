---
id: w03-n06
type: note
title: 'search.c: جست‌وجوی خطی اعداد در C (search.c: integers)'
title_fa: 'search.c: جست‌وجوی خطی اعداد در C'
title_en: 'search.c: integers'
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: search.c
official_anchor: searchc
source_url: https://cs50.harvard.edu/x/2026/notes/3/#searchc
source_refs:
- src-notes-3#searchc
- src-transcript-3
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-search-int
- w03-c-return-from-main
prev: w03-n05
next: w03-n07
order: 6
video:
  youtube_id: 6Svu_ae5ebk
  start: '38:54'
  start_seconds: 2334
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=2334s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'create a program called Search.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# search.c: جست‌وجوی خطی اعداد در C

> **منبع رسمی:** بخش «search.c» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#searchc). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۸:۵۴ تا حدود ۴۳:۵۲](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=2334s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

شبه‌کد قفسه‌ها را دیدی؛ حالا وقتش است جست‌وجوی خطی را واقعاً در C پیاده کنیم. خبر خوب: تقریباً هیچ ابزار تازه‌ای لازم نیست. یک آرایه، یک حلقهٔ `for` و یک `if` کافی است.

## search.c

درس‌نامه می‌گوید با `code search.c` در ترمینال این برنامه را بنویس:

```c
// Implements linear search for integers

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // An array of integers
    int numbers[] = {20, 500, 10, 5, 100, 1, 50};

    // Search for number
    int n = get_int("Number: ");
    for (int i = 0; i < 7; i++)
    {
        if (numbers[i] == n)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
```

- خطی که با `int numbers[]` شروع می‌شود اجازه می‌دهد مقدار هر خانهٔ آرایه را **همان لحظهٔ ساختن** آرایه تعیین کنی. اندازه را ننوشته‌ایم، چون کامپایلر از تعداد مقدارها می‌فهمد.
- حلقهٔ `for` خودِ **پیاده‌سازی جست‌وجوی خطی** است.
- `return 0` نشانهٔ **موفقیت** است و از برنامه خارج می‌شود. `return 1` برای خروج با خطا (شکست) به کار می‌رود.

> [!NOTE]
> **نکته**
> این همان **وضعیت خروج** (`exit status`) هفتهٔ ۲ است. بعد از اجرا با `echo $?` می‌توانی ببینی برنامه `0` برگرداند یا `1`.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David عددهای آرایه را همان اسکناس‌های قفسه‌ها گذاشت: ۲۰، ۵۰۰، ۱۰، ۵، ۱۰۰، ۱ و ۵۰.
- **از سخنرانی:** دربارهٔ `i < 7` گفت نوشتن عدد ثابت در کد عالی نیست، اما چون عدد ۷ فقط **یک بار** آمده، برای این نمایش قابل قبول است.
- **از سخنرانی:** `return 0` در `main` تقریباً معادل برگرداندن `true` است؛ اما `main` باید `int` برگرداند.

> [!TIP]
> **راهنما**
> برنامه را با یک عدد موجود (مثلاً `50`) و یک عدد ناموجود (مثلاً `7`) آزمایش کن. هر دو مسیر باید درست کار کنند: یکی `Found` و دیگری `Not found`.

## اشتباه‌های رایج

- گذاشتن `printf("Not found\n")` داخل حلقه؛ آن وقت برای هر عدد نامساوی یک بار «پیدا نشد» چاپ می‌شود.
- فراموش کردن `return 0` بعد از `Found`؛ برنامه به حلقه ادامه می‌دهد و در آخر `Not found` هم چاپ می‌کند.
- نوشتن `i <= 7`؛ آرایهٔ هفت‌خانه‌ای اندیس `7` ندارد.

## جمع‌بندی

- جست‌وجوی خطی در C یعنی یک حلقه روی همهٔ اندیس‌ها و مقایسهٔ هر خانه با مقدار هدف.
- `0` یعنی موفقیت و `1` یعنی شکست، همان قرارداد وضعیت خروج.

## پیوندها

- قبلی: [امگا و تتا: کران پایین و کران دقیق](/kb/d/w03-n05)
- بعدی: [جست‌وجوی رشته‌ها، strcmp و خطای segmentation](/kb/d/w03-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
