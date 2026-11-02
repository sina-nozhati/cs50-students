---
id: w03-n07
type: note
title: 'جست‌وجوی رشته‌ها، strcmp و خطای segmentation (search.c: strings and strcmp)'
title_fa: جست‌وجوی رشته‌ها، strcmp و خطای segmentation
title_en: 'search.c: strings and strcmp'
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
- src-manual
- src-srt-3
concept_ids:
- w03-c-search-strings
- w03-c-strcmp-return
- w03-c-hardcoded-length
prev: w03-n06
next: w03-n08
order: 7
video:
  youtube_id: 6Svu_ae5ebk
  start: '43:52'
  start_seconds: 2632
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=2632s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'battleship'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جست‌وجوی رشته‌ها، strcmp و خطای segmentation

> **منبع رسمی:** بخش «search.c» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#searchc). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۳:۵۲ تا حدود ۵۰:۲۲](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=2632s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

جست‌وجوی عدد آسان بود. حالا می‌خواهیم دنبال یک **رشته** بگردیم و همین‌جا یکی از معروف‌ترین تله‌های C سر راهت سبز می‌شود: `==` برای رشته‌ها کار نمی‌کند.

## جست‌وجوی رشته

درس‌نامه می‌گوید کد را این‌طور تغییر بده:

```c
// Implements linear search for strings

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // An array of strings
    string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "top hat"};

    // Search for string
    string s = get_string("String: ");
    for (int i = 0; i < 6; i++)
    {
        if (strcmp(strings[i], s) == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
```

- این بار نمی‌توانیم مثل نسخهٔ قبل از `==` استفاده کنیم.
- به‌جایش از `strcmp` استفاده می‌کنیم که از کتابخانهٔ `string.h` می‌آید.
- `strcmp` اگر دو رشته **یکسان** باشند، `0` برمی‌گرداند. پس شرط درست `strcmp(...) == 0` است.
- طول آرایه، یعنی `6`، در کد **سخت‌کد** (`hard-coded`) شده و درس‌نامه صریحاً می‌گوید این روش خوبی در برنامه‌نویسی نیست.

> [!WARNING]
> **هشدار**
> اگر به **خطای segmentation** (`segmentation fault`) برخوردی، یعنی برنامه‌ات به بخشی از حافظه دست زده که اجازهٔ دسترسی به آن را نداشته، مطمئن شو که در کد بالا `i < 6` نوشته‌ای، نه `i < 7`.

- دربارهٔ `strcmp` در [صفحه‌های راهنمای CS50](https://manual.cs50.io/3/strcmp) بیشتر بخوان.

## سخنرانی چه می‌گوید

- **از سخنرانی:** رشته‌ها مهره‌های بازی Monopoly بودند: battleship، boot، cannon، iron، thimble و top hat.
- **از سخنرانی:** David اول با `==` نوشت، برنامه کامپایل شد، اما برای `battleship`، `boot` و حتی `top hat` گفت `Not found`. علت: مقایسهٔ دو عدد برای کامپیوتر ساده است، اما رشته چندین نویسه است و باید نویسه‌به‌نویسه مقایسه شود.

> [!NOTE]
> **نکته**
> `strcmp` را هفتهٔ پیش هم در کنار `strlen` دیدی. یادت باشد خروجی‌اش «درست یا نادرست» نیست؛ **صفر** یعنی برابر. نوشتن `if (strcmp(a, b))` یعنی «اگر **نابرابر** بودند».

## اشتباه‌های رایج

- مقایسهٔ رشته‌ها با `==` و تعجب از اینکه هیچ‌وقت پیدا نمی‌شوند.
- فراموش کردن `#include <string.h>`.
- عدد ثابت ۶ یا ۷ نادرست در شرط حلقه و خطای segmentation.

## جمع‌بندی

- برای مقایسهٔ رشته‌ها از `strcmp` استفاده کن و نتیجه را با `0` بسنج.
- عدد سخت‌کد طول آرایه شکننده است؛ یک اشتباه کوچک یعنی دسترسی به حافظه‌ای که مال تو نیست.

## پیوندها

- قبلی: [search.c: جست‌وجوی خطی اعداد در C](/kb/d/w03-n06)
- بعدی: [phonebook.c: دفترچهٔ تلفن با دو آرایه](/kb/d/w03-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
