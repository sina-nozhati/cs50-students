---
id: w04-n14
type: note
title: 'scanf: ورودی بدون کتابخانهٔ CS50 (scanf)'
title_fa: 'scanf: ورودی بدون کتابخانهٔ CS50'
title_en: scanf
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: scanf
official_anchor: scanf
source_url: https://cs50.harvard.edu/x/2026/notes/4/#scanf
source_refs:
- src-notes-4#scanf
- src-transcript-4
- src-srt-4
concept_ids:
- w04-c-scanf
- w04-c-scanf-string-danger
prev: w04-n13
next: w04-n15
order: 14
video:
  youtube_id: db0H0U13YsA
  start: '1:51:25'
  start_seconds: 6685
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=6685s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'a function called scanF'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# scanf: ورودی بدون کتابخانهٔ CS50

> **منبع رسمی:** بخش «scanf» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#scanf). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۱:۲۵ تا حدود ۲:۰۲:۵۶](https://www.youtube.com/watch?v=db0H0U13YsA&t=6685s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`get_int` و `get_string` چرخ‌های کمکی‌اند. با `scanf` می‌بینیم که چرا گرفتن یک عدد آسان است اما گرفتن یک رشته به‌طور امن سخت.

## get_int با scanf

- در CS50 تابع‌هایی مثل `get_int` ساختیم تا گرفتن ورودی از کاربر ساده شود.
- `scanf` تابع آماده‌ای است که می‌تواند ورودی کاربر را بگیرد.
- می‌توانیم `get_int` را خیلی ساده با `scanf` دوباره بسازیم:

```c
// Gets an int from user using scanf

#include <stdio.h>

int main(void)
{
    int n;
    printf("n: ");
    scanf("%i", &n);
    printf("n: %i\n", n);
}
```

- مقدار `n` در خط `scanf("%i", &n)` در **مکان** `n` ذخیره می‌شود. برای همین `&n` لازم است: `scanf` باید بداند کجا بنویسد.

## get_string سخت است

```c
// Dangerously gets a string from user using scanf with array

#include <stdio.h>

int main(void)
{
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}
```

- اینجا `&` لازم نیست، چون اسم آرایه در C مثل اشاره‌گر عمل می‌کند.
- با این حال این برنامه هر بار درست کار نمی‌کند. هیچ جای این برنامه حافظهٔ کافی برای رشتهٔ مورد نظر نگرفته‌ایم. در واقع نمی‌دانیم کاربر چه رشتهٔ بلندی تایپ می‌کند! و نمی‌دانیم در آن مکان چه مقدارهای زباله‌ای هست.

می‌شود کد را این‌طور تغییر داد، اما باز باید از قبل مقداری حافظه برای رشته کنار بگذاریم:

```c
// Using malloc

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = malloc(4);
    if (s == NULL)
    {
        return 1;
    }
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
    free(s);
    return 0;
}
```

- اگر رشته‌ای چهار بایتی وارد شود، *ممکن است* خطا بگیری.

ساده‌تر کنیم تا مشکل اصلیِ «پیش‌تخصیص» را بهتر بفهمیم:

```c
#include <stdio.h>

int main(void)
{
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}
```

- اگر آرایه‌ای به اندازهٔ `4` از قبل بگیریم، می‌توانیم `cat` تایپ کنیم و برنامه کار می‌کند. اما رشته‌ای بزرگ‌تر از این *ممکن است* خطا بدهد.
- گاهی کامپایلر یا سیستمی که برنامه را اجرا می‌کند بیش از مقدار گفته‌شده حافظه می‌دهد. اما اساساً این کد **ناامن** است: نمی‌توانیم اعتماد کنیم که کاربر رشته‌ای وارد کند که در حافظهٔ از پیش گرفته‌شدهٔ ما جا شود.

> [!WARNING]
> **هشدار**
> `cat` سه حرف است، اما با `\0` چهار بایت لازم دارد؛ پس آرایهٔ `char s[4]` دقیقاً پر می‌شود. `"cats"` به پنج بایت نیاز دارد و بیرون از آرایه نوشته می‌شود. این همان buffer overflow بخش قبل است. برای همین CS50 در `get_string` حافظه را به اندازهٔ ورودی کاربر تخصیص می‌دهد.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت `scanf` برای خواندن از صفحه‌کلید به `&n` نیاز دارد چون باید بتواند مقدار را در نشانی `n` بگذارد؛ همان اصل `swap` با اشاره‌گر، این بار برای `scanf`.
- **از سخنرانی:** او گفت برداشتن چرخ کمکی `get_string` سخت‌تر از `get_int` است، چون از قبل نمی‌دانیم کاربر چند کاراکتر تایپ می‌کند.

## اشتباه‌های رایج

- فراموش کردن `&` در `scanf("%i", &n)`.
- خواندن رشته با `scanf("%s", s)` در آرایه‌ای که ممکن است کوچک باشد.
- فرض اینکه چون یک بار کار کرد، امن است.

## جمع‌بندی

- `scanf("%i", &n)` عدد را در نشانی `n` می‌نویسد.
- `scanf("%s", s)` نمی‌داند `s` چقدر جا دارد؛ رشتهٔ بلند بیرون از آن نوشته می‌شود.
- `get_string` این مشکل را برای تو حل کرده است.

## پیوندها

- قبلی: [سرریز پشته و هیپ](/kb/d/w04-n13)
- بعدی: [ورودی و خروجی فایل](/kb/d/w04-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
