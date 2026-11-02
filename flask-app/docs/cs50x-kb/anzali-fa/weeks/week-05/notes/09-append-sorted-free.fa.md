---
id: w05-n09
type: note
title: 'افزودن به انتها، درج مرتب و آزادسازی (Linked Lists: appending, sorted insertion and freeing)'
title_fa: افزودن به انتها، درج مرتب و آزادسازی
title_en: 'Linked Lists: appending, sorted insertion and freeing'
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
- src-short-doubly-linked-lists
- src-pset-5
- src-anzali-authored-5
- src-srt-5
concept_ids:
- w05-c-append
- w05-c-sorted-insert
- w05-c-free-list
- w05-c-unload-on-error
prev: w05-n08
next: w05-n10
order: 9
video:
  youtube_id: PmAI76OGE_E
  start: '1:03:00'
  start_seconds: 3780
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=3780s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'maybe append to the end of the list'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# افزودن به انتها، درج مرتب و آزادسازی

> **منبع رسمی:** بخش «Linked Lists» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#linked-lists). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۳:۰۰ تا حدود ۱:۲۲:۱۷](https://www.youtube.com/watch?v=PmAI76OGE_E&t=3780s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

افزودن به انتها و درج مرتب نشان می‌دهند که کنترل ترتیب در فهرست پیوندی هزینه دارد. آزاد کردن درست کل فهرست هم مهارتی است که در هر برنامهٔ واقعی، از جمله Speller، لازمت می‌شود.

## افزودن به انتهای فهرست

- می‌توانی عددها را در انتهای فهرست هم بگذاری، مثل این کد:

```c
// Appends numbers to a link list

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

        // If list is empty
        if (list == NULL)
        {
            // This node is the whole list
            list = n;
        }

        // If list has numbers already
        else
        {
            // Iterate over nodes in list
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                // If at end of list
                if (ptr->next == NULL)
                {
                    // Append node
                    ptr->next = n;
                    break;
                }
            }
        }
    }

    // Print numbers
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    // Free memory
    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
    return 0;
}
```

- این کد فهرست را تا انتها **می‌پیماید** تا انتهایش را پیدا کند. وقتی عضوی را به انتها اضافه می‌کنی، کد از مرتبهٔ O(n) اجرا می‌شود، چون پیش از افزودن عضو آخر باید کل فهرست را طی کنی. به متغیر موقت `next` هم دقت کن که حساب `ptr->next` را نگه می‌دارد.

> [!NOTE]
> **یادداشت**
> متغیر `next` در حلقهٔ «Free memory» است: پیش از `free(ptr)` نشانی گرهٔ بعدی را نگه می‌دارد، چون پس از آزاد شدن گره دیگر نباید `ptr->next` را خواند.

## درج مرتب

- می‌توانی فهرست را هنگام افزودن عضوها مرتب هم نگه داری:

```c
// Implements a sorted linked list of numbers

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

        // If list is empty
        if (list == NULL)
        {
            list = n;
        }

        // If number belongs at beginning of list
        else if (n->number < list->number)
        {
            n->next = list;
            list = n; 
        }

        // If number belongs later in list
        else
        {
            // Iterate over nodes in list
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                // If at end of list
                if (ptr->next == NULL)
                {
                    // Append node
                    ptr->next = n;
                    break;
                }

                // If in middle of list
                if (n->number < ptr->next->number)
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;
                }
            }
        }
    }

    // Print numbers
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    // Free memory
    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
    return 0;
}
```

- این فهرست همان‌طور که ساخته می‌شود مرتب است. برای درج یک عضو با این ترتیب، کد همچنان برای هر درج O(n) است، چون در بدترین حالت باید همهٔ عضوهای فعلی را نگاه کنیم.

> [!TIP]
> **تألیفی: چهار حالت جدا**
> کد `list8.c` چهار حالت را از هم جدا می‌کند: فهرست خالی، درج در ابتدا، درج در انتها، درج در وسط. شکستن یک مسئلهٔ مبهم به چند حالت کوچک و مشخص همان «گام‌های کوچکی» است که David در سخنرانی پیشنهاد کرد.

## یک تابع برای آزاد کردن فهرست

- به‌عنوان حرکت پایانی، می‌شود تابعی نوشت که فهرست پیوندی را **unload** کند:

```c
// Frees memory in cases of error too

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

void unload(node *list);

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
            unload(list);
            return 1;
        }
        n->number = get_int("Number: ");
        n->next = NULL;

        // If list is empty
        if (list == NULL)
        {
            list = n;
        }

        // If number belongs at beginning of list
        else if (n->number < list->number)
        {
            n->next = list;
            list = n; 
        }

        // If number belongs later in list
        else
        {
            // Iterate over nodes in list
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                // If at end of list
                if (ptr->next == NULL)
                {
                    // Append node
                    ptr->next = n;
                    break;
                }

                // If in middle of list
                if (n->number < ptr->next->number)
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;
                }
            }
        }
    }

    // Print numbers
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    // Free memory
    unload(list);
    return 0;
}

void unload(node *list)
{
    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
}
```

- تابع `unload` کل فهرست را آزاد می‌کند. حالا اگر `malloc` در میانهٔ ساختن فهرست شکست بخورد، `unload(list)` گره‌های ساخته‌شدهٔ قبلی را آزاد می‌کند و بعد برنامه `return 1` می‌کند.
- این کد شاید پیچیده به نظر برسد. اما ببین که با اشاره‌گرها و این نحو، می‌توانیم داده‌هایی را که در جاهای مختلف حافظه‌اند به هم بدوزیم.

> [!IMPORTANT]
> **مهم**
> `free(list)` کل فهرست را آزاد نمی‌کند؛ فقط گرهٔ اول را. `free` نمی‌داند فهرست پیوندی چیست. به ازای هر `malloc` باید یک `free` جدا صدا بزنی، و همیشه پیش از آزاد کردن هر گره نشانی گرهٔ بعدی را نگه داری.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت می‌شد یک اشاره‌گر دیگر هم همیشه به انتهای فهرست نگه داشت تا افزودن به انتها سریع شود؛ هزینه‌اش فقط یک اشاره‌گر است.
- **از سخنرانی:** او کد درج مرتب را با تکیه بر نسخهٔ از پیش آماده‌شده نشان داد و گفت بهتر است آن را آهسته و گام به گام در پرابلم‌ست ۵ مرور کنی، چون ترتیب دستکاری اشاره‌گرها مهم است.
- **از سخنرانی:** او ایراد نسخهٔ قبلی را نشان داد: اگر `malloc` در دور دوم یا سوم شکست بخورد، `return 1` گره‌های قبلی را آزاد نمی‌کند. کپی کردن کد آزادسازی در شرط هم نشانهٔ طراحی بد است؛ راه‌حل، تابع `unload` در `list9.c` است.
- **از سخنرانی:** او جمع‌بندی کرد که در این پیاده‌سازی درج، جست‌وجو و حذف همه O(n)اند. پویایی به دست آمد، اما جست‌وجوی دودویی آرایه از دست رفت؛ حتی برای یافتن وسط فهرست باید کل آن را پیمود.
- **از سخنرانی:** او **فهرست پیوندی دوطرفه** (doubly linked list) را هم نام برد: هر گره به بعدی و قبلی اشاره می‌کند. این کار کد را ساده‌تر می‌کند، ولی سرعت را بنیادی تغییر نمی‌دهد.

ویدئوی کوتاه [Doubly-Linked Lists](/kb/d/w05-sh-doubly-linked-lists) فهرست دوطرفه را با جزئیات بررسی می‌کند.

> [!NOTE]
> **یادداشت**
> متن کدهای `list8.c` و `list9.c` همان متن رسمی است، از جمله یک فاصلهٔ اضافه در انتهای خط `list = n;` و توضیح «link list» در `list7.c`. این‌ها عمداً تغییر داده نشده‌اند و در `sources.json` ثبت شده‌اند.

## اشتباه‌های رایج

- آزاد کردن `ptr` و بعد خواندن `ptr->next`.
- فرض کردن اینکه یک `free(list)` کل فهرست را آزاد می‌کند.
- فراموش کردن حالت «فهرست خالی» در درج مرتب.
- رها کردن گره‌های قبلی وقتی `malloc` در میانهٔ کار شکست می‌خورد.

## جمع‌بندی

- افزودن به انتها و درج مرتب هر دو O(n)اند.
- آزادسازی فهرست یعنی پیمایش و `free` تک‌تک گره‌ها، با نگه داشتن نشانی بعدی پیش از هر `free`.
- یک تابع `unload` آزادسازی را در هر مسیر خروج، از جمله مسیر خطا، ممکن می‌کند.

## پیوندها

- قبلی: [ساختن فهرست پیوندی با افزودن به ابتدا](/kb/d/w05-n08)
- بعدی: [درخت‌ها و درخت جست‌وجوی دودویی](/kb/d/w05-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
