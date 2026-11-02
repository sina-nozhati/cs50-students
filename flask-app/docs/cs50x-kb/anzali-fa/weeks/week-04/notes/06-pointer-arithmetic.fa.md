---
id: w04-n06
type: note
title: حساب اشاره‌گرها (Pointer Arithmetic)
title_fa: حساب اشاره‌گرها
title_en: Pointer Arithmetic
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Pointer Arithmetic
official_anchor: pointer-arithmetic
source_url: https://cs50.harvard.edu/x/2026/notes/4/#pointer-arithmetic
source_refs:
- src-notes-4#pointer-arithmetic
- src-transcript-4
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-pointer-arithmetic
- w04-c-bracket-as-pointer
prev: w04-n05
next: w04-n07
order: 6
video:
  youtube_id: db0H0U13YsA
  start: '45:00'
  start_seconds: 2700
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=2700s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'concept known as pointer arithmetic'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# حساب اشاره‌گرها

> **منبع رسمی:** بخش «Pointer Arithmetic» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#pointer-arithmetic). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۵:۰۰ تا حدود ۴۸:۰۶](https://www.youtube.com/watch?v=db0H0U13YsA&t=2700s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اگر اشاره‌گر فقط یک عدد (نشانی) است، می‌شود روی آن حساب کرد. همین ایده نشان می‌دهد براکت‌های `s[i]` که از هفتهٔ ۲ می‌نویسی در واقع چه می‌کنند.

## حساب روی نشانی‌ها

**حساب اشاره‌گر** (pointer arithmetic) یعنی توانایی انجام محاسبه روی مکان‌های حافظه. اول هر کاراکتر را با براکت چاپ می‌کنیم:

```c
// Prints a string's chars

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
}
```

حالا همین کار را با حساب اشاره‌گر:

```c
// Prints a string's chars via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
}
```

- اول کاراکتری که در مکان `s` است چاپ می‌شود، بعد کاراکتر مکان `s + 1` و همین‌طور تا آخر.

همین ایده برای آرایه‌ای از عددها:

```c
// Prints substrings via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s);
    printf("%s\n", s + 1);
    printf("%s\n", s + 2);
}
```

- این کد مقدارهای ذخیره‌شده در چند مکان حافظه را، با شروع از `numbers`، چاپ می‌کند.

> [!IMPORTANT]
> **مهم**
> `s[i]` و `*(s + i)` یک معنا دارند. در آرایهٔ `int`، عبارت `numbers + 1` یک **بایت** جلو نمی‌رود، بلکه یک **int** (چهار بایت) جلو می‌رود. کامپایلر نوع اشاره‌گر را می‌داند و اندازه را خودش حساب می‌کند.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David با حساب اشاره‌گر دوباره `HI!` را چاپ کرد و گفت نماد آرایه، یعنی براکت‌ها، چیزی است که به آن «نحو شیرین» (syntactic sugar) می‌گویند: فقط شکل خواناتری از همین کار.
- **از سخنرانی:** او گفت هیچ‌کس دوست ندارد کدی مثل `*(s + 1)` بنویسد چون خواندنش ذهن را کمی می‌پیچاند؛ `s[0]` سرراست‌تر است، اما کامپیوتر در عمل نماد براکت را برای ما به همین شکل تبدیل می‌کند.

> [!TIP]
> **تألیفی: یک تمرین ذهنی**
> اگر `char *s = "CAT";` باشد، `*(s + 2)` چیست؟ و `*(s + 3)`؟ پاسخ: `T` و کاراکتر `\0`.

## اشتباه‌های رایج

- نوشتن `*s + 1` به‌جای `*(s + 1)`. اولی یعنی «کاراکتر اول به‌علاوهٔ یک» (مثلاً `I` برای `H`)، نه کاراکتر دوم.
- فکر کردن به اینکه حساب اشاره‌گر همیشه یک بایت جلو می‌رود.
- رفتن فراتر از `\0` یا انتهای آرایه.

## جمع‌بندی

- `s + i` نشانی عنصر `i` است و `*(s + i)` مقدار آن.
- براکت‌ها شکل خواناتر همین حساب‌اند.

## پیوندها

- قبلی: [رشته‌ها همان char * هستند](/kb/d/w04-n05)
- بعدی: [مقایسهٔ رشته‌ها: == در برابر strcmp](/kb/d/w04-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
