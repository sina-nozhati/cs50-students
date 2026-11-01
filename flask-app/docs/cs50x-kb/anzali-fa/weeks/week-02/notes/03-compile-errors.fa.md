---
id: w02-n03
type: note
title: 'باگ و خطاهای کامپایل (Debugging: compile errors)'
title_fa: باگ و خطاهای کامپایل
title_en: 'Debugging: compile errors'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Debugging
official_anchor: debugging
source_url: https://cs50.harvard.edu/x/2026/notes/2/#debugging
source_refs:
- src-notes-2#debugging
- src-transcript-2
- src-srt-2
concept_ids:
- w02-c-bug
- w02-c-compile-error
- w02-c-logical-error
prev: w02-n02
next: w02-n04
order: 3
video:
  youtube_id: h5Gc1n8ZuU8
  start: '9:22'
  start_seconds: 562
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=562s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'buggy'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# باگ و خطاهای کامپایل

> **منبع رسمی:** بخش «Debugging» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#debugging). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۹:۲۲ تا حدود ۱۹:۴۶](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=562s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

درس‌نامه صریح می‌گوید: **همه** هنگام کدنویسی اشتباه می‌کنند. مهم این است که بدانی اشتباه را چطور پیدا کنی. **اشکال‌زدایی** (`debugging`) یعنی پیدا کردن و برداشتن **باگ‌ها** (`bugs`) از کد.

## سخنرانی چه می‌گوید

**از سخنرانی:** David واژهٔ bug را به Dr. Grace Hopper پیوند می‌دهد، دریاسالار نیروی دریایی آمریکا و از نخستین برنامه‌نویسان Harvard Mark I. تیم او روی Harvard Mark II یادداشتی در دفتر ثبت کار گذاشت: یک **بید** (moth) واقعی در مدار کامپیوتر گیر کرده بود.

## سه خطای کامپایل رسمی

### سرآیند جاافتاده

```c
// Missing #include for stdio.h

int main(void)
{
    printf("hello, world\n");
}
```

- `#include` برای `stdio.h` نیامده است. `printf` در همین فایل سرآیند تعریف شده.
- بدون آن کامپایلر `printf` را نمی‌شناسد و **خطا** می‌دهد.

### غلط املایی در نام سرآیند

```c
// Misspelled stdio.h

#include <studio.h>

int main(void)
{
    printf("hello, world\n");
}
```

- `stdio.h` به اشتباه `studio.h` نوشته شده است.
- کامپایلر فایلی به نام `studio.h` پیدا نمی‌کند و کامپایل شکست می‌خورد. نام درست `stdio.h` است، کوتاه‌شدهٔ standard input/output.

### چند خطا با هم

```c
// Missing cs50.h, variable's type, semicolon, %s, and second printf argument.

#include <stdio.h>

int main(void)
{
    name = get_string("What's your name? ")
    printf("hello, world\n");
}
```

درس‌نامه چهار مشکل را برمی‌شمارد:

1. نوع متغیر `name` اعلان نشده است.
2. کتابخانهٔ `cs50.h` نیامده، پس نوع `string` شناخته نمی‌شود.
3. پس از فراخوانی `get_string` نقطه‌ویرگول نیست.
4. `printf` اصلاً از `name` استفاده نمی‌کند.

> **توجه:** توضیح بالای همین کد رسمی در درس‌نامه از «`%s` و آرگومان دوم printf» هم نام می‌برد؛ یعنی مورد چهارم در واقع دو تغییر لازم دارد.

## دو نوع باگ

- برخی باگ‌ها **پیام خطا** می‌دهند؛ مثل سه نمونهٔ بالا که کامپایلر جلویشان را می‌گیرد.
- برخی دیگر **خطای منطقی** (`logical error`) هستند: پیامی نمی‌بینی، اما برنامه رفتار غیرمنتظره دارد. برای این‌ها به ابزارهای یادداشت‌های بعدی نیاز داری.

## اشتباه‌های رایج

- خواندن آخرین پیام خطا به‌جای اولین. معمولاً خطای اول بقیه را می‌سازد.
- تصور این‌که «کامپایل شد» یعنی «درست است». خطای منطقی از کامپایلر رد می‌شود.

## جمع‌بندی

- باگ یعنی اشتباه در کد؛ اشکال‌زدایی یعنی یافتن و برداشتنش.
- خطای کامپایل را کامپایلر گزارش می‌کند؛ خطای منطقی را باید خودت با آزمودن کشف کنی.

## پیوندها

- قبلی: [سطح خوانایی متن و رمزنگاری: دو مسئلهٔ این هفته](/kb/d/w02-n02)
- بعدی: [اشکال‌زدایی با printf](/kb/d/w02-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
