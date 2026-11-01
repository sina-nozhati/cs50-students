---
id: w02-n10
type: note
title: 'ثابت سراسری و آرایه به‌عنوان آرگومان تابع (Arrays: const and array parameters)'
title_fa: ثابت سراسری و آرایه به‌عنوان آرگومان تابع
title_en: 'Arrays: const and array parameters'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Arrays
official_anchor: arrays
source_url: https://cs50.harvard.edu/x/2026/notes/2/#arrays
source_refs:
- src-notes-2#arrays
- src-transcript-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-global-const
- w02-c-array-parameter
prev: w02-n09
next: w02-n11
order: 10
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:19:41'
  start_seconds: 4781
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=4781s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'constant'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# ثابت سراسری و آرایه به‌عنوان آرگومان تابع

> **منبع رسمی:** بخش «Arrays» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#arrays). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۹:۴۱ تا حدود ۱:۳۰:۲۰](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=4781s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

آرایه فقط ظرف نیست؛ می‌شود آن را **به تابع داد**. این یادداشت دو بهبود طراحی را با هم نشان می‌دهد: یک **ثابت** برای اندازهٔ آرایه، و تابعی که میانگین را حساب می‌کند.

## کد رسمی

```c
// Averages three numbers using an array, a constant, and a helper function

#include <cs50.h>
#include <stdio.h>

// Constant
const int N = 3;

// Prototype
float average(int length, int array[]);

int main(void)
{
    // Get scores
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Print average
    printf("Average: %f\n", average(N, scores));
}

float average(int length, int array[])
{
    // Calculate average
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
```

## سه نکتهٔ درس‌نامه

- تابع تازه‌ای به نام `average` اعلان شده است. محاسبهٔ میانگین را **انتزاع** (`abstract away`) کرده‌ایم.
- یک مقدار `const`، یعنی **ثابت**، به نام `N` اعلان شده است. چون بیرون از همهٔ تابع‌ها آمده، در کل فایل دیده می‌شود.
- مهم‌تر از همه: `average` پارامتر `int array[]` می‌گیرد؛ یعنی تابع می‌تواند **آرایه** را به‌عنوان پارامتر دریافت کند.

درس‌نامه جمع‌بندی می‌کند: آرایه‌ها نه‌تنها ظرف‌اند، بلکه می‌شود آن‌ها را بین تابع‌ها جابه‌جا کرد.

## چرا طول را جدا می‌دهیم؟

- `average(N, scores)` دو چیز می‌گیرد: طول و خود آرایه.
- **تألیفی:** در C، آرایه‌ای که به تابع داده می‌شود طول خودش را با خودش نمی‌برد. پس تابع باید طول را جدا بگیرد تا بداند حلقه تا کجا برود.
- **تألیفی:** `sum / (float) length` همان **تبدیل نوع** (`type casting`) هفتهٔ ۱ است؛ بدون آن، تقسیم دو `int` بخش اعشاری را می‌برد.

## ثابت سراسری

- `const int N = 3;` بالای فایل، پیش از `main`، نوشته شده است. حالا اگر بخواهی پنج نمره بگیری، فقط **یک** جا را تغییر می‌دهی.
- **از سخنرانی:** David نام ثابت‌ها را با حروف بزرگ می‌نویسد تا مشخص باشد مقدارشان عوض نمی‌شود؛ این یک قرارداد است، نه قاعدهٔ زبان.

## اشتباه‌های رایج

- نوشتن `average(scores)` بدون طول.
- تکرار عدد `3` به‌جای استفاده از `N`؛ همان **عدد جادویی** هفتهٔ ۱.
- تلاش برای تغییر `N` در طول برنامه؛ `const` اجازه نمی‌دهد.

## جمع‌بندی

- `float average(int length, int array[])` نشان می‌دهد آرایه با `[]` در فهرست پارامترها می‌آید.
- طول آرایه را همراهش بفرست، و اندازه را در یک ثابت نگه دار.

## پیوندها

- قبلی: [آرایه‌ها و حلقه‌ها](/kb/d/w02-n09)
- بعدی: [نویسه‌ها و ASCII](/kb/d/w02-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
