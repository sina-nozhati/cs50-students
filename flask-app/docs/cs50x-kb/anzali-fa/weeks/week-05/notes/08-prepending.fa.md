---
id: w05-n08
type: note
title: 'ساختن فهرست پیوندی با افزودن به ابتدا (Linked Lists: prepending)'
title_fa: ساختن فهرست پیوندی با افزودن به ابتدا
title_en: 'Linked Lists: prepending'
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Linked Lists
official_anchor: linked-lists
source_url: https://cs50.harvard.edu/x/2026/notes/5/#linked-lists
source_refs:
- src-notes-5#linked-lists
- src-transcript-5
- src-srt-5
concept_ids:
- w05-c-prepend
- w05-c-link-before-move
- w05-c-list-traversal
- w05-c-prepend-reverses
- w05-c-list-complexity
- w05-c-list-tradeoffs
prev: w05-n07
next: w05-n09
order: 8
video:
  youtube_id: PmAI76OGE_E
  start: '40:16'
  start_seconds: 2416
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=2416s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'implement the first of our link lists'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ساختن فهرست پیوندی با افزودن به ابتدا

> **منبع رسمی:** بخش «Linked Lists» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#linked-lists). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۰:۱۶ تا حدود ۱:۰۳:۰۰](https://www.youtube.com/watch?v=PmAI76OGE_E&t=2416s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

افزودن به ابتدای فهرست ساده‌ترین درج است، اما ترتیب دو خط آن حیاتی است. اگر جابه‌جا شوند، بخشی از فهرست برای همیشه گم می‌شود.

## ساختن فهرست با افزودن به ابتدا

- می‌توانیم `list.c` را دوباره و با فهرست پیوندی بنویسیم:

```c
// Start to build a linked list by prepending nodes

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    // Memory for numbers
    node *list = NULL;

    // Build list
    for (int i = 0; i < 3; i++)
    {
        // Allocate node for number
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }
        n->number = get_int("Number: ");
        n->next = NULL;

        // Prepend node to list
        n->next = list;
        list = n;
    }
    return 0;
}
```

- اول، `node` به‌صورت یک `struct` تعریف می‌شود. برای هر عضو فهرست، با `malloc` به اندازهٔ یک گره حافظه گرفته می‌شود. به `n->number` (فیلد number گرهٔ `n`) یک عدد صحیح داده می‌شود و به `n->next` (فیلد next گرهٔ `n`) مقدار `NULL`. سپس گره در ابتدای فهرست، در محل `list`، قرار می‌گیرد.

> [!WARNING]
> **هشدار**
> `list3.c` گره‌ها را هیچ‌وقت آزاد نمی‌کند. این برنامه نمونهٔ آموزشی یک مرحلهٔ میانی است؛ بررسی ما با valgrind برای سه عدد ورودی نشت ۴۸ بایت را نشان داد: ۱۶ بایت «definitely lost» (گرهٔ سر فهرست) و ۳۲ بایت «indirectly lost» (دو گرهٔ دیگر که فقط از راه گرهٔ سر قابل دسترس بودند). آزاد کردن را در یادداشت بعد می‌بینی.

## قدم به قدم در تصویر

- می‌توانیم روند ساختن فهرست پیوندی را مفهومی تصور کنیم. اول، `node *list` اعلان می‌شود، اما مقدار زباله دارد.
- بعد، گره‌ای به اسم `n` در حافظه گرفته می‌شود.
- بعد، به `number` آن گره مقدار `1` داده می‌شود و به فیلد `next` مقدار `NULL`.
- بعد، `list` به همان جایی اشاره می‌کند که `n` اشاره می‌کند. حالا `n` و `list` هر دو به یک جا اشاره می‌کنند.
- سپس گرهٔ تازه‌ای ساخته می‌شود. هر دو فیلد `number` و `next` آن مقدار زباله دارند. `number` گرهٔ تازه `2` می‌شود و فیلد `next` هم به‌روز می‌شود.
- مهم‌تر از همه، نباید ارتباطمان با هیچ‌کدام از این گره‌ها قطع شود، وگرنه برای همیشه گم می‌شوند. برای همین فیلد `next` گرهٔ `n` به همان جایی اشاره می‌کند که `list` اشاره می‌کند.
- سرانجام `list` به‌روز می‌شود تا به `n` اشاره کند. حالا یک فهرست پیوندی دوعضوی داریم.

> [!WARNING]
> **هشدار**
> درس‌نامه می‌گوید `node *list` «مقدار زباله دارد»، اما در خود کد `node *list = NULL;` نوشته شده است. در سخنرانی هم David گفت اعلان بدون مقداردهی زباله می‌سازد و **برای همین** در کد واقعی `NULL` گذاشته است. این تفاوت در `sources.json` ثبت شده است.

> [!IMPORTANT]
> **مهم**
> ترتیب درست این است: اول `n->next = list;` و بعد `list = n;`. اگر اول `list = n;` بنویسی، دیگر هیچ متغیری به فهرست قبلی اشاره نمی‌کند و آن گره‌ها **یتیم** و نشتی می‌شوند.

## پیمایش و چاپ

- با نگاه به نمودار می‌بینیم آخرین عدد اضافه‌شده اولین عددی است که در فهرست می‌آید. پس اگر فهرست را از اولین گره چاپ کنیم، ترتیب برعکس است.
- فهرست را می‌شود این‌طور چاپ کرد:

```c
// Print nodes in a linked list with a while loop

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    // Memory for numbers
    node *list = NULL;

    // Build list
    for (int i = 0; i < 3; i++)
    {
        // Allocate node for number
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }
        n->number = get_int("Number: ");
        n->next = NULL;

        // Prepend node to list
        n->next = list;
        list = n;
    }

    // Print numbers
    node *ptr = list;
    while (ptr != NULL)
    {
        printf("%i\n", ptr->number);
        ptr = ptr->next;
    }
    return 0;
}
```

- `node *ptr = list` متغیری موقت می‌سازد که به همان جایی اشاره می‌کند که `list` اشاره می‌کند. حلقهٔ `while` چیزی را که `ptr` به آن اشاره می‌کند چاپ می‌کند و بعد `ptr` را به گرهٔ `next` در فهرست می‌برد.

> [!WARNING]
> **هشدار**
> درس‌نامه پیش از این کد می‌گوید «فهرست را می‌شود با ترتیب درست چاپ کرد»، اما `list4.c` همچنان به ابتدا اضافه می‌کند؛ اگر `1`، `2` و `3` وارد کنی، خروجی `3`، `2`، `1` است. «ترتیب درست» در افزودن به انتها (`list7.c`) و درج مرتب (`list8.c`) می‌آید. `list4.c` هم گره‌ها را آزاد نمی‌کند. هر دو مورد در `sources.json` ثبت شده‌اند.

## پیچیدگی زمانی و بده‌بستان

- در این مثال درج در فهرست همیشه از مرتبهٔ O(1) است، چون افزودن به ابتدای فهرست فقط چند گام کوچک دارد.
- زمان جست‌وجوی این فهرست از مرتبهٔ O(n) است، چون در بدترین حالت کل فهرست باید گشته شود. زمان افزودن عضو تازه به جایی بستگی دارد که اضافه می‌شود.
- فهرست‌های پیوندی در بلوک پیوسته‌ای از حافظه نیستند و تا جایی که منابع سیستم اجازه بدهد بزرگ می‌شوند. عیبش این است که برای نگه داشتن فهرست حافظهٔ بیشتری از آرایه لازم است: برای هر عضو هم مقدار و هم اشاره‌گر به گرهٔ بعدی. همچنین نمی‌شود مثل آرایه با اندیس به عضو رسید، چون برای رسیدن به عضو nام باید از n - 1 عضو اول گذشت. پس فهرست بالا باید خطی جست‌وجو شود و **جست‌وجوی دودویی ممکن نیست**.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David فهرست را به رشته‌ای از ذرت بوداده تشبیه کرد که با نخ به هم دوخته می‌شوند: هیچ‌وقت نباید بخشی از رشته را رها کنی.
- **از سخنرانی:** او پیمایش را با یک حلقهٔ `for` هم نوشت: `for (node *ptr = list; ptr != NULL; ptr = ptr->next)`، و گفت این نسخه فشرده‌تر است ولی نسخهٔ `while` خواناتر.
- **از سخنرانی:** در پاسخ به پرسشی دربارهٔ حافظه گفت این ساختار تقریباً دو برابر حافظه مصرف می‌کند؛ در ازای پویایی، فضا می‌دهی. زمان، فضا، هزینهٔ مالی و وقت انسان همه منابعی‌اند که باید سنجید.
- **از سخنرانی:** او اندازهٔ گره را «احتمالاً ۱۲ بایت، ۴ برای int و ۸ برای اشاره‌گر» گفت و افزود `sizeof` جواب دقیق را می‌دهد.

> [!NOTE]
> **یادداشت**
> روی سامانه‌های ۶۴ بیتی رایج `sizeof(node)` معمولاً ۱۶ است، نه ۱۲، چون کامپایلر برای هم‌ترازی اشاره‌گر چهار بایت پُرکننده (padding) اضافه می‌کند. گزارش valgrind ما هم تکه‌های ۱۶ بایتی نشان داد. همین دلیل است که در کد همیشه `sizeof(node)` بنویس، نه یک عدد ثابت.

## اشتباه‌های رایج

- جابه‌جا نوشتن `list = n;` و `n->next = list;`.
- انتظار ترتیب ورود در خروجی، در حالی که افزودن به ابتدا ترتیب را برعکس می‌کند.
- پیمایش با خود `list` به‌جای یک متغیر موقت؛ با این کار سر فهرست گم می‌شود.

## جمع‌بندی

- افزودن به ابتدا O(1) است؛ جست‌وجو و پیمایش O(n).
- فهرست پیوندی پویاست اما اندیس‌گذاری و جست‌وجوی دودویی ندارد و به ازای هر عضو یک اشاره‌گر اضافه مصرف می‌کند.

## پیوندها

- قبلی: [گره و عملگر پیکان (->)](/kb/d/w05-n07)
- بعدی: [افزودن به انتها، درج مرتب و آزادسازی](/kb/d/w05-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
