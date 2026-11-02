---
id: w02-n17
type: note
title: وضعیت خروج (Exit Status)
title_fa: وضعیت خروج
title_en: Exit Status
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Exit Status
official_anchor: exit-status
source_url: https://cs50.harvard.edu/x/2026/notes/2/#exit-status
source_refs:
- src-notes-2#exit-status
- src-transcript-2
- src-pset-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-exit-status
- w02-c-echo-status
prev: w02-n16
next: w02-n18
order: 17
video:
  youtube_id: h5Gc1n8ZuU8
  start: '2:14:54'
  start_seconds: 8094
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=8094s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'exit status'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# وضعیت خروج

> **منبع رسمی:** بخش «Exit Status» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#exit-status). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۱۴:۵۴ تا حدود ۲:۲۰:۲۳](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=8094s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

وقتی برنامه تمام می‌شود، یک عدد ویژه به کامپیوتر می‌دهد. این عدد را معمولاً نمی‌بینی، اما ابزارهایی مثل check50 با همین عدد می‌فهمند برنامه‌ات درست تمام شده یا با خطا.

## وضعیت خروج

- وقتی برنامه تمام می‌شود، یک **کد خروج** ویژه به کامپیوتر داده می‌شود.
- برنامه‌ای که **بدون خطا** تمام شود، وضعیت `0` می‌دهد. اغلب وقتی خطایی باعث پایان برنامه شود، وضعیت `1` داده می‌شود.

با `code status.c` بنویس:

```c
// Returns explicit value from main

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Missing command-line argument\n");
        return 1;
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}
```

- اگر `./status David` را اجرا **نکنی** (مثلاً فقط `./status`)، وضعیت خروج `1` می‌گیری.
- اگر `./status David` را اجرا کنی، وضعیت خروج `0` است.

## دیدن وضعیت خروج

- در ترمینال `echo $?` بزن تا وضعیت خروج آخرین فرمان اجراشده را ببینی.
- درس‌نامه می‌گوید می‌توانی تصور کنی بخش‌هایی از همین برنامه را برای بررسی **تعداد درست** آرگومان‌های خط فرمان به کار ببری.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت دستیاران آموزشی پس از اجرای کد تو می‌توانند با `echo $?` مقدار بازگشتی برنامه‌ات را «پنهانی» ببینند. یکی از راه‌هایی که check50 درستی کد را می‌سنجد، همین وضعیت خروج است.
- **از سخنرانی:** برنامه می‌تواند در حالت‌های مختلف ۱، ۲، ۳ یا عددهای دیگر برگرداند؛ این عدد برای کاربر عادی نمایش داده نمی‌شود و بیشتر به کار برنامه‌نویس می‌آید.

> **تألیفی:** پرابلم‌ست Caesar دقیقاً همین الگو را می‌خواهد: اگر تعداد آرگومان درست نبود، پیام Usage چاپ کن و از `main` مقدار `1` برگردان. جزئیات در [راهنمای Caesar](/kb/d/w02-ps-caesar).

## اشتباه‌های رایج

- `return 1` در یک تابع کمکی به‌جای `main`؛ فقط `return` در `main` وضعیت خروج برنامه را تعیین می‌کند.
- چاپ پیام خطا ولی ادامه دادن برنامه به‌جای `return 1`.

## جمع‌بندی

- `0` یعنی موفقیت، عدد غیرصفر یعنی خطا.
- `echo $?` وضعیت خروج آخرین فرمان را نشان می‌دهد.

## پیوندها

- قبلی: [آرگومان‌های خط فرمان: argc و argv](/kb/d/w02-n16)
- بعدی: [رمزنگاری: متن ساده، کلید و متن رمز (از سخنرانی)](/kb/d/w02-n18)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
