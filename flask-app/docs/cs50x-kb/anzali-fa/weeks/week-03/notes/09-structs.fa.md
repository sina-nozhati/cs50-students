---
id: w03-n09
type: note
title: 'ساختارها (struct): نوع دادهٔ خودت را بساز (Structs)'
title_fa: 'ساختارها (struct): نوع دادهٔ خودت را بساز'
title_en: Structs
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Structs
official_anchor: structs
source_url: https://cs50.harvard.edu/x/2026/notes/3/#structs
source_refs:
- src-notes-3#structs
- src-transcript-3
- src-pset-3
- src-section-3
- src-section-3-transcript
- src-srt-3
concept_ids:
- w03-c-struct
- w03-c-dot-notation
- w03-c-array-of-structs
- w03-c-encapsulation
prev: w03-n08
next: w03-n10
order: 9
video:
  youtube_id: 6Svu_ae5ebk
  start: '56:09'
  start_seconds: 3369
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=3369s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'Data structures.'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ساختارها (struct): نوع دادهٔ خودت را بساز

> **منبع رسمی:** بخش «Structs» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#structs). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۶:۰۹ تا حدود ۱:۰۳:۲۰](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=3369s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

C از ما می‌خواهد با نوع‌های آماده مثل `int` و `string` کار کنیم، اما دنیای واقعی پر از چیزهایی است که چند ویژگی دارند: یک شخص نام **و** شماره دارد، یک نامزد انتخاباتی نام **و** تعداد رأی. **struct** راهی است که خودت نوع داده بسازی. پرابلم‌ست‌های این هفته پر از struct هستند.

## ساختن نوع person

- C اجازه می‌دهد با `struct` **نوع دادهٔ خودمان** را بسازیم.
- آیا مفید نیست نوعی به نام `person` داشته باشیم که درونش یک `name` و یک `number` باشد؟

```c
typedef struct
{
    string name;
    string number;
} person;
```

- این نوع دادهٔ خودمان به نام `person` است که یک رشته به نام `name` و یک رشتهٔ دیگر به نام `number` دارد.

## دفترچهٔ تلفن با struct

برنامهٔ قبلی را این‌طور بهتر می‌کنیم:

```c
// Implements a phone book with structs

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
} person;

int main(void)
{
    person people[3];

    people[0].name = "Kelly";
    people[0].number = "+1-617-495-1000";

    people[1].name = "David";
    people[1].number = "+1-617-495-1000";

    people[2].name = "John";
    people[2].number = "+1-949-468-2750";

    // Search for name
    string name = get_string("Name: ");
    for (int i = 0; i < 3; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
```

- کد با `typedef struct` شروع می‌شود که نوع تازه‌ای به نام `person` تعریف می‌کند.
- در `main` آرایه‌ای به نام `people` از نوع `person` با اندازهٔ ۳ می‌سازیم.
- سپس نام و شمارهٔ سه نفر را در آرایهٔ `people` به‌روز می‌کنیم.
- از همه مهم‌تر: **نماد نقطه** (`dot notation`)، مثل `people[0].name`، اجازه می‌دهد به `person` در جایگاه صفرم دسترسی داشته باشیم و به او نام بدهیم.

> [!IMPORTANT]
> **مهم**
> `people[i].name` را از چپ به راست بخوان: «در آرایهٔ `people` برو به خانهٔ `i`، و از آن شخص، فیلد `name` را بده.»

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت این نسخه زمان و خط بیشتری برد، اما **طراحی بهتری** دارد: در `people[0]` یک شخص واقعی با همهٔ اطلاعاتش هست. به این **کپسوله‌سازی** (`encapsulation`) می‌گوییم؛ آکولادها مثل یک بغل داده‌ها را کنار هم نگه می‌دارند.

## جلسهٔ حل تمرین: candidate

- **از جلسهٔ حل تمرین:** Kelly یک struct به نام `candidate` با `name` و `votes` ساخت و تابعی به نام `get_candidate` نوشت که اطلاعات را از کاربر می‌گیرد و یک `candidate` **برمی‌گرداند**. کد کاملش را در [صفحهٔ جلسهٔ حل تمرین](/kb/d/w03-sec) می‌بینی.
- **از جلسهٔ حل تمرین:** وقتی تابع را بعد از `main` تعریف کرد، خطای «call to undeclared function» گرفت؛ همان **پیش‌اعلان** (`prototype`) هفتهٔ ۱ که فراموش شده بود.

> [!WARNING]
> **هشدار**
> تعریف `typedef struct` باید **قبل از** هر جایی بیاید که از آن نوع استفاده می‌کنی، معمولاً بالای `main`. بعد از نام نوع (`} person;`) نقطه‌ویرگول را فراموش نکن.

## اشتباه‌های رایج

- نوشتن `people.name[0]` به‌جای `people[0].name`.
- فراموش کردن نقطه‌ویرگول بعد از `} person`.
- استفاده از نوع struct پیش از تعریف آن.

## جمع‌بندی

- `typedef struct { ... } name;` نوع دادهٔ تازه می‌سازد.
- با نماد نقطه به فیلدها دسترسی پیدا کن و آرایه‌ای از structها را مثل هر آرایهٔ دیگری با اندیس بگرد.

## پیوندها

- قبلی: [phonebook.c: دفترچهٔ تلفن با دو آرایه](/kb/d/w03-n08)
- بعدی: [مرتب‌سازی و مرتب‌سازی انتخابی](/kb/d/w03-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
