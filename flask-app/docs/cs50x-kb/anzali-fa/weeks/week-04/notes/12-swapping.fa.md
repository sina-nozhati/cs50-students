---
id: w04-n12
type: note
title: جابه‌جایی، پشته و هیپ (Swapping)
title_fa: جابه‌جایی، پشته و هیپ
title_en: Swapping
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Swapping
official_anchor: swapping
source_url: https://cs50.harvard.edu/x/2026/notes/4/#swapping
source_refs:
- src-notes-4#swapping
- src-transcript-4
- src-short-call-stacks
- src-srt-4
concept_ids:
- w04-c-swap-by-pointer
- w04-c-memory-layout
- w04-c-stack-frame
prev: w04-n11
next: w04-n13
order: 12
video:
  youtube_id: db0H0U13YsA
  start: '1:34:44'
  start_seconds: 5684
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=5684s
  origin: inference
  basis: first lecture4.srt cue containing the phrase "So what I'd like you to do is swap"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جابه‌جایی، پشته و هیپ

> **منبع رسمی:** بخش «Swapping» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#swapping). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۳۴:۴۴ تا حدود ۱:۴۹:۰۷](https://www.youtube.com/watch?v=db0H0U13YsA&t=5684s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هفتهٔ ۳ تابع `swap` را برای مرتب‌سازی تصور کردیم. اما نسخهٔ سادهٔ آن در C کار نمی‌کند. فهمیدن علتش نشان می‌دهد حافظهٔ یک برنامه چطور سازمان یافته است.

## swap.c که کار نمی‌کند

در عمل، جابه‌جا کردن دو مقدار نیازی رایج است. طبیعتاً جابه‌جا کردن دو متغیر بدون یک جای نگه‌داری موقت سخت است. با `code swap.c`:

```c
// Fails to swap two integers

#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(x, y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
```

- این کد اجرا می‌شود، اما کار نمی‌کند: مقدارها حتی پس از فرستادن به تابع `swap` جابه‌جا نمی‌شوند. چرا؟
- وقتی مقدارها را به یک تابع می‌دهی، فقط **کپی** آن‌ها را می‌دهی. *دامنهٔ* (scope) `x` و `y` به تابع `main` محدود است. در کد بالا `x` و `y` **با مقدار** (by value) فرستاده می‌شوند.

## چیدمان حافظه

- تصویر درس‌نامه حافظهٔ یک برنامه را مثل یک مستطیل نشان می‌دهد: بالا **کد ماشین**، بعد **globals**، بعد **heap** و پایین **stack**.
- متغیرهای *سراسری* (global)، که در این دوره از آن‌ها استفاده نکرده‌ایم، در یک جای حافظه زندگی می‌کنند. تابع‌ها هنگام اجرا در `stack`، در بخش دیگری از حافظه، جا می‌گیرند.
- در تصویر بعدی `main` و `swap` دو **قاب** (frame) یا ناحیهٔ جدا از حافظه دارند. پس نمی‌توانیم فقط مقدارها را از یک تابع به تابع دیگر بفرستیم و انتظار تغییرشان را داشته باشیم.

> [!NOTE]
> **نکته**
> `malloc` حافظه را از **heap** می‌دهد و متغیرهای محلی تابع‌ها در **stack** هستند. قاب `swap` پس از بازگشت تابع از بین می‌رود و تغییرهای `a` و `b` هم با آن. ویدئوی کوتاه [Call Stacks](/kb/d/w03-sh-call-stacks) از هفتهٔ ۳ همین قاب‌ها را نشان می‌دهد.

## swap با اشاره‌گر

```c
// Swaps two integers using pointers

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

- حالا متغیرها **با مقدار** فرستاده نمی‌شوند، بلکه **با ارجاع** (by reference): نشانی‌های `x` و `y` به تابع داده می‌شود.
- پس تابع `swap` می‌داند کجا باید تغییر بدهد تا `x` و `y` واقعیِ تابع `main` عوض شوند.

> [!IMPORTANT]
> **مهم**
> سه چیز باید با هم عوض شوند: امضای تابع (`int *a, int *b`)، فراخوانی (`swap(&x, &y)`) و بدنه (`*a` و `*b`). اگر فقط یکی را عوض کنی، کامپایلر هشدار یا خطا می‌دهد یا تابع باز هم روی کپی کار می‌کند.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David از یک داوطلب به اسم Olivia خواست محتوای دو لیوان، یکی آبی و یکی نارنجی، را جابه‌جا کند. بدون جای خالی این کار بدون مخلوط شدن ممکن نبود؛ با یک لیوان سوم خالی، یعنی همان **متغیر موقت**، کار انجام شد.
- **از سخنرانی:** او گفت تابع `swap` دقیقاً همین کار را می‌کند: یک «لیوان خالی» به اسم `tmp` برمی‌دارد، `a` را در آن می‌ریزد، `b` را در `a` و در آخر `tmp` را در `b`.
- **از سخنرانی:** او توضیح داد که کد ماشین برنامه از حافظهٔ پایدار (دیسک) در RAM بارگذاری می‌شود و در بالای این تصویر قرار می‌گیرد، و global ها درست زیر آن، و heap ناحیه‌ای است که `malloc` از آن حافظه می‌دهد.

## اشتباه‌های رایج

- انتظار تغییر متغیرهای `main` با تابعی که فقط کپی مقدارها را می‌گیرد.
- فراخوانی `swap(x, y)` برای نسخهٔ اشاره‌گری؛ باید `swap(&x, &y)` باشد.
- نوشتن `a = b` به‌جای `*a = *b`؛ اولی فقط اشاره‌گرهای محلی را عوض می‌کند.

## جمع‌بندی

- آرگومان‌ها در C با مقدار فرستاده می‌شوند؛ هر تابع قاب خودش را در stack دارد.
- برای تغییر متغیرهای تابع صدازننده، نشانی‌شان را بفرست و در تابع dereference کن.
- حافظه از بالا به پایین: کد ماشین، globals، heap، stack.

## پیوندها

- قبلی: [مقدارهای زباله و Binky](/kb/d/w04-n11)
- بعدی: [سرریز پشته و هیپ](/kb/d/w04-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
