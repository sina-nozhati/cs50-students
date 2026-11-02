---
id: w04-n08
type: note
title: 'کپی کردن رشته: چرا t = s کپی نیست (Copying and malloc: the problem)'
title_fa: 'کپی کردن رشته: چرا t = s کپی نیست'
title_en: 'Copying and malloc: the problem'
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Copying and malloc
official_anchor: copying-and-malloc
source_url: https://cs50.harvard.edu/x/2026/notes/4/#copying-and-malloc
source_refs:
- src-notes-4#copying-and-malloc
- src-transcript-4
- src-srt-4
concept_ids:
- w04-c-pointer-copy
prev: w04-n07
next: w04-n09
order: 8
video:
  youtube_id: db0H0U13YsA
  start: '57:31'
  start_seconds: 3451
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=3451s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'let me open up how about copy.c'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# کپی کردن رشته: چرا t = s کپی نیست

> **منبع رسمی:** بخش «Copying and malloc» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#copying-and-malloc). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۷:۳۱ تا حدود ۱:۰۲:۳۳](https://www.youtube.com/watch?v=db0H0U13YsA&t=3451s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

کپی کردن رشته کاری روزمره است، اما با چیزی که دربارهٔ اشاره‌گرها فهمیدیم، `t = s` دیگر کپی نیست. این بخش مشکل را نشان می‌دهد و بخش بعد راه‌حل را.

## copy.c

در ترمینال `code copy.c` را بزن و این را بنویس:

```c
// Capitalizes a string

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get a string
    string s = get_string("s: ");

    // Copy string's address
    string t = s;

    // Capitalize first letter in string
    t[0] = toupper(t[0]);

    // Print string twice
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

- `string t = s` **نشانی** `s` را در `t` کپی می‌کند. این چیزی نیست که می‌خواستیم: رشته کپی نشده، فقط نشانی کپی شده است.
- به `ctype.h` هم دقت کن؛ `toupper` از آنجا می‌آید.
- تصویر درس‌نامه نشان می‌دهد که `s` و `t` هنوز به **همان** بلوک‌های حافظه اشاره می‌کنند. این کپی واقعی نیست؛ دو اشاره‌گر به یک رشته‌اند. برای همین بزرگ کردن حرف اول `t`، رشتهٔ `s` را هم تغییر می‌دهد.

## پرهیز از segmentation fault

پیش از حل این مشکل باید مطمئن شویم که به خطای *segmentation fault* نمی‌خوریم، یعنی دست زدن به حافظه‌ای که وجود ندارد. با `strlen` کمک می‌گیریم:

```c
// Capitalizes a string, checking length first

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get a string
    string s = get_string("s: ");

    // Copy string's address
    string t = s;

    // Capitalize first letter in string
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print string twice
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

- `strlen` بررسی می‌کند که رشتهٔ `t` محتوا داشته باشد. اگر نداشته باشد، چیزی بزرگ نمی‌شود.

> [!NOTE]
> **نکته**
> اگر کاربر چیزی تایپ نکند، `t[0]` همان `\0` است. این برنامه با بررسی `strlen(t) > 0` از تغییر دادن آن پرهیز می‌کند.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David برنامه را اجرا کرد و `hi` را با حروف کوچک تایپ کرد. با تعجب دیدیم که هم `s` و هم `t` بزرگ شدند، در حالی که او فقط به `t[0]` دست زده بود. توضیحش این بود که `t[0]` درست همان تکه حافظه‌ای است که `s` به آن اشاره می‌کند.

## اشتباه‌های رایج

- انتظار اینکه `t = s` رشته را کپی کند.
- دست زدن به `t[0]` بدون بررسی طول رشته.

## جمع‌بندی

- انتساب یک `char *` به دیگری فقط نشانی را کپی می‌کند.
- برای کپی واقعی به حافظهٔ تازه نیاز داریم: `malloc` در بخش بعد.

## پیوندها

- قبلی: [مقایسهٔ رشته‌ها: == در برابر strcmp](/kb/d/w04-n07)
- بعدی: [malloc، free، strcpy و NULL](/kb/d/w04-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
