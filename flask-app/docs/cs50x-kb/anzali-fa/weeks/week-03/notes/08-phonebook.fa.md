---
id: w03-n08
type: note
title: 'phonebook.c: دفترچهٔ تلفن با دو آرایه (phonebook.c)'
title_fa: 'phonebook.c: دفترچهٔ تلفن با دو آرایه'
title_en: phonebook.c
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: phonebook.c
official_anchor: phonebookc
source_url: https://cs50.harvard.edu/x/2026/notes/3/#phonebookc
source_refs:
- src-notes-3#phonebookc
- src-transcript-3
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-parallel-arrays
- w03-c-numbers-as-strings
prev: w03-n07
next: w03-n09
order: 8
video:
  youtube_id: 6Svu_ae5ebk
  start: '50:22'
  start_seconds: 3022
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=3022s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'code of phonebook.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# phonebook.c: دفترچهٔ تلفن با دو آرایه

> **منبع رسمی:** بخش «phonebook.c» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#phonebookc). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۰:۲۲ تا حدود ۵۶:۰۹](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=3022s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حالا عددها و رشته‌ها را در یک برنامه کنار هم می‌گذاریم و یک دفترچهٔ تلفن کوچک می‌سازیم. برنامه کار می‌کند، اما طراحی‌اش یک ایراد پنهان دارد که بخش بعد، یعنی struct، آن را حل می‌کند.

## phonebook.c

در ترمینال `code phonebook.c` را بزن و بنویس:

```c
// Implements a phone book without structs

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Arrays of strings
    string names[] = {"Kelly", "David", "John"};
    string numbers[] = {"+1-617-495-1000", "+1-617-495-1000", "+1-949-468-2750"};

    // Search for name
    string name = get_string("Name: ");
    for (int i = 0; i < 3; i++)
    {
        if (strcmp(names[i], name) == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
```

- شمارهٔ Kelly با `+1-617` شروع می‌شود، شمارهٔ David هم با `+1-617` و شمارهٔ John با `+1-949`.
- پس `names[0]` همان Kelly است و `numbers[0]` شمارهٔ Kelly. این کد اجازه می‌دهد شمارهٔ یک شخص مشخص را در دفترچه پیدا کنیم.

## مشکل طراحی

- این کد کار می‌کند، اما درس‌نامه می‌گوید **ناکارآمدی‌های زیادی** دارد.
- در واقع این احتمال هست که نام‌ها و شماره‌ها با هم **متناظر** نمانند. دو آرایهٔ جدا فقط با یک «قرار نانوشته» (هم‌اندیس بودن) به هم وصل‌اند.
- آیا عالی نبود اگر می‌توانستیم **نوع دادهٔ خودمان** را بسازیم که یک شخص را به شماره‌اش وصل کند؟

## سخنرانی چه می‌گوید

- **از سخنرانی:** چرا شماره‌ها `string` هستند نه `int`؟ چون شماره تلفن علامت‌هایی مثل `+` و `-` دارد. تازه در بعضی کشورها برای تماس محلی صفر اول می‌گیری و صفرهای اول در یک عدد صحیح ناپدید می‌شوند.
- **از سخنرانی:** شمارهٔ Kelly و David همان شمارهٔ هفتهٔ صفر است و David گفت اگر خواستی، می‌توانی به شمارهٔ John پیامک بدهی یا زنگ بزنی.

> [!TIP]
> **راهنما**
> هر جا دیدی دو یا چند آرایهٔ «موازی» داری که با یک اندیس مشترک به هم ربط دارند، احتمالاً جای یک struct خالی است.

## اشتباه‌های رایج

- ذخیرهٔ شماره تلفن یا کد پستی در `int`.
- اضافه کردن نام تازه به `names` و فراموش کردن شمارهٔ متناظرش در `numbers`؛ همه‌چیز یک خانه جابه‌جا می‌شود.

## جمع‌بندی

- دو آرایهٔ موازی کار می‌کنند، اما شکننده‌اند.
- عددهایی که با آن‌ها حساب نمی‌کنی، مثل شماره تلفن، بهتر است رشته باشند.

## پیوندها

- قبلی: [جست‌وجوی رشته‌ها، strcmp و خطای segmentation](/kb/d/w03-n07)
- بعدی: [ساختارها (struct): نوع دادهٔ خودت را بساز](/kb/d/w03-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
