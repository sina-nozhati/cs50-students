---
id: w02-n16
type: note
title: 'آرگومان‌های خط فرمان: argc و argv (Command-Line Arguments)'
title_fa: 'آرگومان‌های خط فرمان: argc و argv'
title_en: Command-Line Arguments
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Command-Line Arguments
official_anchor: command-line-arguments
source_url: https://cs50.harvard.edu/x/2026/notes/2/#command-line-arguments
source_refs:
- src-notes-2#command-line-arguments
- src-transcript-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-argc-argv
- w02-c-argv0
prev: w02-n15
next: w02-n17
order: 16
video:
  youtube_id: h5Gc1n8ZuU8
  start: '2:07:44'
  start_seconds: 7664
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=7664s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'command line argument'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# آرگومان‌های خط فرمان: argc و argv

> **منبع رسمی:** بخش «Command-Line Arguments» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#command-line-arguments). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۷:۴۴ تا حدود ۲:۱۴:۵۴](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=7664s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا حالا ورودی را **در حین** اجرا با `get_string` می‌گرفتی. **آرگومان‌های خط فرمان** (`command-line arguments`) ورودی را **پیش از** اجرا می‌گیرند؛ درست مثل `clang -o hello hello.c` یا `./caesar 13`.

## تعریف

- آرگومان‌های خط فرمان آن‌هایی‌اند که در خط فرمان به برنامه داده می‌شوند. همهٔ چیزهایی که پس از `clang` تایپ کردی آرگومان خط فرمان بودند. حالا در برنامه‌های خودت هم از آن‌ها استفاده می‌کنی.

## نسخهٔ آشنا

با `code greet.c` بنویس:

```c
// Uses get_string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

- این برنامه به کاربر `hello` می‌گوید، اما نام را **حین** اجرا می‌پرسد.

## argc و argv

درس‌نامه می‌پرسد: خوب نبود اگر می‌شد آرگومان‌ها را پیش از اجرا گرفت؟

```c
// Prints a command-line argument

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hello, %s\n", argv[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}
```

- برنامه دو چیز می‌داند: `argc`، **تعداد** آرگومان‌های خط فرمان، و `argv`، **آرایه‌ای از رشته‌ها** که در خط فرمان داده شده‌اند.
- پس اجرای `./greet David` چاپ می‌کند: `hello, David`.
- **تألیفی:** چرا `argc == 2`؟ چون نام برنامه هم شمرده می‌شود: `./greet` در `argv[0]` و `David` در `argv[1]`.

## چاپ همهٔ آرگومان‌ها

```c
// Prints command-line arguments

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
}
```

- هر آرگومان در یک خط چاپ می‌شود.
- نخستین آرگومان، `argv[0]`، **همیشه نام خود برنامه** است و پس از آن آرگومان‌هایی می‌آیند که هنگام اجرا داده‌ای.

## سخنرانی چه می‌گوید

**از سخنرانی:** David برنامهٔ `cowsay` را نشان داد: یک گاو با «حباب گفت‌وگو» به شکل هنر ASCII. با آرگومان `-f duck` ظاهر گاو به اردک تغییر کرد. خودش گفت «ارزش آموزشی ندارد»، اما نشان می‌دهد آرگومان‌های خط فرمان همه‌جا هستند.

## اشتباه‌های رایج

- خواندن `argv[1]` بدون بررسی `argc`؛ اگر کاربر آرگومانی نداده باشد، این خانه وجود ندارد.
- فراموش کردن این‌که `argv[0]` نام برنامه است و آرگومان کاربر از `argv[1]` شروع می‌شود.
- نوشتن `int main(void)` وقتی به آرگومان نیاز داری.

## جمع‌بندی

- `int main(int argc, string argv[])` امضای `main` برای گرفتن آرگومان است.
- `argc` همیشه دست‌کم ۱ است، چون نام برنامه هم شمرده می‌شود.

## پیوندها

- قبلی: [بزرگ‌کردن حروف و ctype.h](/kb/d/w02-n15)
- بعدی: [وضعیت خروج](/kb/d/w02-n17)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
