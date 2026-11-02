---
id: w05-n03
type: note
title: 'صف: اول وارد، اول خارج (FIFO) (Queues)'
title_fa: 'صف: اول وارد، اول خارج (FIFO)'
title_en: Queues
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Queues
official_anchor: queues
source_url: https://cs50.harvard.edu/x/2026/notes/5/#queues
source_refs:
- src-notes-5#queues
- src-transcript-5
- src-short-queues
- src-srt-5
concept_ids:
- w05-c-queue
- w05-c-fifo
- w05-c-enqueue-dequeue
- w05-c-capacity-vs-size
prev: w05-n02
next: w05-n04
order: 3
video:
  youtube_id: PmAI76OGE_E
  start: '3:58'
  start_seconds: 238
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=238s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'consider for instance'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# صف: اول وارد، اول خارج (FIFO)

> **منبع رسمی:** بخش «Queues» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#queues). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳:۵۸ تا حدود ۷:۲۲](https://www.youtube.com/watch?v=PmAI76OGE_E&t=238s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

صف اولین نوع انتزاعی این هفته است. با آن تفاوت «ظرفیت» و «اندازهٔ فعلی» را می‌بینی و اولین محدودیت آرایهٔ ثابت را لمس می‌کنی.

## صف‌ها

- **صف** (queue) یکی از شکل‌های ساختمان دادهٔ انتزاعی است.
- صف ویژگی‌های مشخصی دارد: **FIFO** است، یعنی «اول وارد، اول خارج». خودت را در صف یک وسیلهٔ بازی در شهربازی تصور کن: نفر اول صف اول سوار می‌شود و نفر آخر آخر از همه.
- صف عملیات مشخصی دارد: یک عضو را می‌شود **enqueue** کرد، یعنی به صف اضافه کرد؛ و وقتی به سر صف رسید می‌شود **dequeue** کرد، یعنی از صف بیرون آورد.
- در کد می‌شود صف را این‌طور تصور کرد:

```c
const int CAPACITY = 50;

typedef struct
{
    person people[CAPACITY];
    int size;
}
queue;
```

- آرایه‌ای به اسم `people` از نوع `person` است. `CAPACITY` بیشترین اندازه‌ای است که صف می‌تواند داشته باشد. عدد صحیح `size` نشان می‌دهد صف واقعاً چقدر پر است، صرف‌نظر از اینکه چقدر **می‌تواند** جا بدهد.

> [!NOTE]
> **یادداشت**
> این کد یک قطعه است، نه برنامهٔ کامل: نوع `person` در آن تعریف نشده است و باید پیش از آن، مثل هفته‌های ۳ و ۴، یک `struct` به اسم `person` تعریف شده باشد.

> [!WARNING]
> **هشدار**
> این `struct` فقط `size` را نگه می‌دارد. ویدئوی کوتاه [Queues](/kb/d/w05-sh-queues) برای صفِ مبتنی بر آرایه یک فیلد `front` هم لازم می‌داند تا معلوم باشد سر صف کجاست، و در سخنرانی هم David گفت باید به‌نوعی حساب سر صف را نگه داشت. این تفاوت در `sources.json` ثبت شده است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت صف را هر جا که برای چیزی در صف ایستاده‌ای تجربه می‌کنی و معمولاً از صف انتظار **انصاف** داریم: هر که اول آمده، اول وارد شود.
- **از سخنرانی:** او پرسید این پیاده‌سازی چه محدودیتی دارد. جواب: فقط ۵۰ نفر را جا می‌دهد. اگر عدد را به ۵۰۰ یا ۵۰۰۰ تغییر بدهی و دوباره کامپایل کنی، یا باز هم کم می‌آوری یا، اگر فقط چند نفر بیایند، حافظه را هدر می‌دهی.
- **از سخنرانی:** او این تخصیص را **ایستا** (static) خواند: اندازه از پیش و هنگام کامپایل تعیین می‌شود. بهتر است صف بتواند هنگام نیاز بزرگ و کوچک شود و از سیستم‌عامل حافظه بگیرد و پس بدهد.

ویدئوی کوتاه [Queues](/kb/d/w05-sh-queues) دو پیاده‌سازی صف، با آرایه و با فهرست پیوندی دوطرفه، را با جزئیات نشان می‌دهد.

## اشتباه‌های رایج

- یکی گرفتن `CAPACITY` و `size`: اولی ظرفیت است و دومی تعداد اعضای فعلی.
- فراموش کردن اینکه در صف، خروج از **سر** صف است، نه از انتهای آن.

## جمع‌بندی

- صف FIFO است و دو عمل اصلی دارد: enqueue و dequeue.
- پیاده‌سازی با آرایهٔ ثابت ساده است ولی ظرفیتش از پیش تعیین شده است.

## پیوندها

- قبلی: [ساختمان داده و نوع دادهٔ انتزاعی](/kb/d/w05-n02)
- بعدی: [پشته: آخر وارد، اول خارج (LIFO)](/kb/d/w05-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
