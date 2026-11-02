---
id: w04-n04
type: note
title: 'اشاره‌گرها: & و * (Pointers)'
title_fa: 'اشاره‌گرها: & و *'
title_en: Pointers
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Pointers
official_anchor: pointers
source_url: https://cs50.harvard.edu/x/2026/notes/4/#pointers
source_refs:
- src-notes-4#pointers
- src-transcript-4
- src-short-pointers
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-address-of
- w04-c-percent-p
- w04-c-pointer
- w04-c-dereference
- w04-c-pointer-size
prev: w04-n03
next: w04-n05
order: 4
video:
  youtube_id: db0H0U13YsA
  start: '16:02'
  start_seconds: 962
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=962s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'One is a single ampersand'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# اشاره‌گرها: & و *

> **منبع رسمی:** بخش «Pointers» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#pointers). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۶:۰۲ تا حدود ۳۰:۵۸](https://www.youtube.com/watch?v=db0H0U13YsA&t=962s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اشاره‌گر (pointer) مهم‌ترین ایدهٔ این هفته است. رشته‌ها، `malloc`، جابه‌جایی واقعی دو متغیر و کار با فایل همه روی همین ایده سوارند.

## دو عملگر تازه

زبان C دو عملگر قدرتمند دارد که به حافظه مربوط‌اند:

```text
& Provides the address of something stored in memory.
* Instructs the compiler to go to a location in memory.
```

- `&` نشانی چیزی را که در حافظه ذخیره شده است به ما می‌دهد.
- `*` به کامپایلر می‌گوید «برو به آن مکان در حافظه».

با این دانسته‌ها کد قبلی را تغییر می‌دهیم:

```c
// Prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);
}
```

- `%p` اجازه می‌دهد نشانی یک مکان حافظه را ببینیم.
- `&n` را می‌شود این‌طور خواند: «نشانی `n`». اجرای این کد نشانی‌ای چاپ می‌کند که با `0x` شروع می‌شود.

## اشاره‌گر چیست؟

**اشاره‌گر** متغیری است که نشانی چیزی را نگه می‌دارد. به زبان خلاصه، اشاره‌گر یک نشانی در حافظهٔ کامپیوتر است. این تکه را ببین:

```text
int n = 50;
int *p = &n;
```

`p` اشاره‌گری است که نشانی عدد صحیح `n` را در خود دارد. حالا کد را این‌طور تغییر بده:

```c
// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
}
```

این کد همان اثر کد قبلی را دارد؛ فقط از `&` و `*` در تعریف `p` استفاده کردیم. درس‌نامه همین برنامه را یک بار دیگر هم برای توضیح `*` می‌آورد:

```c
// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
}
```

- خط `printf` نشانی عدد صحیح را چاپ می‌کند.
- `int *p` اشاره‌گری می‌سازد که کارش نگه داشتن نشانی یک `int` است.

> [!IMPORTANT]
> **مهم**
> در `int *p = &n;` ستاره بخشی از **نوع** است: «`p` اشاره‌گری به `int` است». اما در عبارتی مثل `*p` در وسط کد، ستاره عملگر **رفتن به نشانی** (dereference) است. یک علامت، دو نقش.

## اندازهٔ اشاره‌گر

- در تصویر درس‌نامه، `p` بزرگ‌تر از `n` کشیده شده است. در واقع اشاره‌گر معمولاً یک مقدار **۸ بایتی** است و `p` نشانی آن `50` را نگه می‌دارد.
- دقیق‌تر این است که اشاره‌گر را مثل یک **پیکان** تصور کنیم: یک نشانی که به نشانی دیگری اشاره می‌کند.

> [!TIP]
> **تألیفی: هر دو نقش در یک برنامه**
> برنامهٔ کوتاه زیر (تألیفی) هم نشانی و هم مقدارِ پشت نشانی را چاپ می‌کند.

```c
// تألیفی: نشانی و مقدار
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
    printf("%i\n", *p);
}
```

خط اول خروجی یک نشانی مثل `0x7ffd...` است که در هر اجرا ممکن است فرق کند؛ خط دوم همیشه `50` است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت ستاره چند کاربرد متفاوت دارد، اما `&` کاربردی ساده و سرراست دارد: گرفتن نشانی یک متغیر در حافظه. او در `addresses.c` به‌جای `n` نوشت `&n`.
- **از سخنرانی:** او تأکید کرد که برنامه‌نویس‌ها وقتی روی تخته دربارهٔ طراحی حرف می‌زنند، به ندرت به خود عدد نشانی اهمیت می‌دهند؛ مهم این است که متغیر **در یک نشانی** است. برای همین اشاره‌گر را معمولاً با یک پیکان می‌کشند.
- **از سخنرانی:** او گفت شکل ستاره در `int *p` کمی شبیه ضرب است ولی ضرب نیست؛ طراحان C دهه‌ها پیش این علامت را انتخاب کردند.

ویدئوی کوتاه [Pointers](/kb/d/w04-sh-pointers) همین ایده‌ها را با مثال‌های بیشتر، از جمله اشاره‌گر `NULL`، مرور می‌کند.

## اشتباه‌های رایج

- چاپ اشاره‌گر با `%i` به‌جای `%p`. کامپایلر هشدار می‌دهد و خروجی بی‌معناست.
- قاطی کردن `*` در تعریف (نوع) با `*` در عبارت (رفتن به نشانی).
- انتظار نشانی ثابت: نشانی‌ها در اجراهای مختلف ممکن است فرق کنند.

## جمع‌بندی

- `&x` نشانی `x` است و `*p` یعنی مقداری که در نشانی `p` است.
- اشاره‌گر متغیری است که نشانی نگه می‌دارد و معمولاً ۸ بایت است.
- `%p` برای چاپ نشانی‌هاست.

## پیوندها

- قبلی: [حافظه و نشانی‌ها](/kb/d/w04-n03)
- بعدی: [رشته‌ها همان char * هستند](/kb/d/w04-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
