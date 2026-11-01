---
id: w05-n07
type: note
title: 'گره و عملگر پیکان (->) (Linked Lists: nodes and the arrow operator)'
title_fa: گره و عملگر پیکان (->)
title_en: 'Linked Lists: nodes and the arrow operator'
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
- src-short-structures
- src-short-singly-linked-lists
- src-anzali-authored-5
- src-anzali-inference-5
- src-srt-5
concept_ids:
- w05-c-arrow-operator
- w05-c-linked-list
- w05-c-node
- w05-c-self-referential-struct
- w05-c-list-null-end
- w05-c-head-pointer
prev: w05-n06
next: w05-n08
order: 7
video:
  youtube_id: PmAI76OGE_E
  start: '32:11'
  start_seconds: 1931
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=1931s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'few new pieces of syntax'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# گره و عملگر پیکان (->)

> **منبع رسمی:** بخش «Linked Lists» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#linked-lists). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۲:۱۱ تا حدود ۴۰:۱۶](https://www.youtube.com/watch?v=PmAI76OGE_E&t=1931s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

فهرست پیوندی اولین ساختار این هفته است که داده‌ها را **ناپیوسته** نگه می‌دارد. پایه‌اش عملگر تازهٔ `->` و `struct`ی است که به نوع خودش اشاره می‌کند؛ هر دو در Speller لازمت می‌شوند.

## دو ابزار قدیمی و یک عملگر تازه

- در هفته‌های اخیر سه ابزار مفید یاد گرفتی. `struct` نوع داده‌ای است که خودت تعریف می‌کنی. `.` در **نشانه‌گذاری نقطه‌ای** به متغیرهای درون آن ساختار دسترسی می‌دهد. عملگر `*` برای اعلان اشاره‌گر یا ارجاع‌زدایی به کار می‌رود.
- امروز با عملگر `->` آشنا می‌شوی. این یک پیکان است: به یک نشانی می‌رود و درون یک ساختار را نگاه می‌کند.

> [!TIP]
> **تألیفی: دو نگارش برای یک کار**
> `n->number` دقیقاً همان `(*n).number` است. برنامهٔ کوتاه زیر (تألیفی) با یکی می‌نویسد و با دیگری می‌خواند.

```c
// تألیفی: دو نگارش برای یک کار
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    (*n).number = 50;
    n->next = NULL;
    printf("%i\n", n->number);
    free(n);
    return 0;
}
```

خروجی برنامه `50` است. پرانتز در `(*n).number` لازم است، چون `.` از `*` اولویت بالاتری دارد.

## فهرست پیوندی

- **فهرست پیوندی** (linked list) یکی از قدرتمندترین ساختمان‌های داده در C است. اجازه می‌دهد مقدارهایی را نگه داری که در جاهای مختلف حافظه‌اند و فهرست را هر وقت خواستی بزرگ و کوچک کنی.
- سه مقدار را در سه جای مختلف حافظه تصور کن. چطور می‌شود آن‌ها را در یک فهرست به هم دوخت؟
- می‌توانیم کمی حافظهٔ بیشتر مصرف کنیم و با یک اشاره‌گر نگه داریم عضو بعدی کجاست. `NULL` نشان می‌دهد که در فهرست چیزی **بعدی** نیست.
- طبق قرارداد، یک عنصر دیگر هم در حافظه نگه می‌داریم: اشاره‌گری که حساب اولین عضو فهرست را نگه می‌دارد و به آن **head** (سر فهرست) می‌گویند.
- اگر نشانی‌ها را کنار بگذاریم، فهرست مثل جعبه‌هایی است که هر کدام با پیکانی به بعدی اشاره می‌کند تا جعبه‌ها تمام شوند (تصویرها در `media.json`، فقط پیوند).
- به این جعبه‌ها **گره** (node) می‌گویند. هر گره هم یک **عضو** دارد و هم اشاره‌گری به اسم `next`. در کد می‌شود گره را این‌طور تصور کرد:

```c
typedef struct node
{
    int number;
    struct node *next;
}
node;
```

- عضوِ درون این گره یک عدد صحیح به اسم `number` است. دوم، اشاره‌گری به یک گره به اسم `next` هست که به گرهٔ دیگری جایی در حافظه اشاره خواهد کرد.

> [!NOTE]
> **یادداشت**
> چرا `struct node` دو بار نوشته می‌شود؟ کامپایلر کد را از بالا به پایین می‌خواند و نام کوتاه `node` تا آخرین خط `typedef` هنوز وجود ندارد. با نام دادن `struct node` در خط اول، می‌شود درون آکولادها `struct node *next` نوشت. این را **ساختار خودارجاع** می‌گویند.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David داده و **فراداده** (metadata) را جدا کرد: عدد داده‌ای است که برایمان مهم است و اشاره‌گر `next` فراداده‌ای است که برای نگه داشتن داده لازم داریم؛ مثل نقشهٔ گنج یا ردّ خرده‌نان.
- **از سخنرانی:** او گفت شکل‌ها به مقیاس نیستند: عدد صحیح معمولاً ۴ بایت است و اشاره‌گر ۸ بایت.
- **از سخنرانی:** او مقایسه کرد که برای اضافه کردن عضو چهارم کافی است پیکانی را به‌روز کنی؛ هیچ داده‌ای کپی نمی‌شود.
- **از سخنرانی:** او ریشهٔ ضرورت `struct node` را با نمونهٔ اعلان تابع (prototype) در هفته‌های قبل مقایسه کرد: کامپایلر باید نام را پیش از استفاده دیده باشد.

> [!WARNING]
> **هشدار**
> در سخنرانی گفته شد فهرست در Python «در واقع یک فهرست پیوندی است». در پیاده‌سازی رایج Python (CPython)، `list` آرایه‌ای پویاست که خودکار بزرگ می‌شود، نه فهرست پیوندی. این برداشت تحریریهٔ CS50x انزلی است (استنتاجی) و در `sources.json` ثبت شده است.

ویدئوی کوتاه [Structures](/kb/d/w05-sh-structures) مرور خوبی بر `struct`، نقطه و پیکان است و [Singly-Linked Lists](/kb/d/w05-sh-singly-linked-lists) عملیات فهرست پیوندی را قدم به قدم نشان می‌دهد.

## اشتباه‌های رایج

- نوشتن `*n.number` به‌جای `(*n).number` یا `n->number`.
- نوشتن `node *next;` درون `struct` پیش از اینکه `node` تعریف شده باشد.
- فکر کردن به اینکه `next` خودِ گرهٔ بعدی است؛ `next` فقط **نشانی** آن است.

## جمع‌بندی

- `->` یعنی «برو به نشانی و درون ساختار را نگاه کن».
- هر گره یک داده و یک اشاره‌گر `next` دارد؛ آخرین گره `NULL` دارد و متغیر سر فهرست نشانی اولین گره است.

## پیوندها

- قبلی: [realloc و هزینهٔ کپی](/kb/d/w05-n06)
- بعدی: [ساختن فهرست پیوندی با افزودن به ابتدا](/kb/d/w05-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
