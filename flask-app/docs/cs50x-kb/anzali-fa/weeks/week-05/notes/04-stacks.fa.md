---
id: w05-n04
type: note
title: 'پشته: آخر وارد، اول خارج (LIFO) (Stacks)'
title_fa: 'پشته: آخر وارد، اول خارج (LIFO)'
title_en: Stacks
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Stacks
official_anchor: stacks
source_url: https://cs50.harvard.edu/x/2026/notes/5/#stacks
source_refs:
- src-notes-5#stacks
- src-transcript-5
- src-short-stacks
- src-srt-5
concept_ids:
- w05-c-stack
- w05-c-lifo
- w05-c-push-pop
- w05-c-fixed-capacity-limit
prev: w05-n03
next: w05-n05
order: 4
video:
  youtube_id: PmAI76OGE_E
  start: '7:22'
  start_seconds: 442
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=442s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'alternative to a'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# پشته: آخر وارد، اول خارج (LIFO)

> **منبع رسمی:** بخش «Stacks» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#stacks). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۷:۲۲ تا حدود ۱۲:۲۲](https://www.youtube.com/watch?v=PmAI76OGE_E&t=442s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پشته رفتاری درست برعکس صف دارد. دیدن اینکه کد پشته و صف در درس‌نامه **یکسان** است کمک می‌کند فرق «رفتار» و «چیدمان در حافظه» را بفهمی.

## پشته‌ها

- صف در برابر **پشته** (stack) قرار می‌گیرد. ویژگی‌های پشته اساساً با صف فرق دارد: پشته **LIFO** است، یعنی «آخر وارد، اول خارج». مثل سینی‌هایی که در سلف روی هم چیده می‌شوند: سینی‌ای که آخر از همه روی پشته گذاشته شده، اولین سینی‌ای است که برداشته می‌شود.
- پشته عملیات مشخصی دارد: **push** چیزی را روی پشته می‌گذارد و **pop** چیزی را از بالای پشته برمی‌دارد.
- در کد می‌شود پشته را این‌طور تصور کرد:

```c
const int CAPACITY = 50;

typedef struct
{
    person people[CAPACITY];
    int size;
}
stack;
```

- آرایه‌ای به اسم `people` از نوع `person` است. `CAPACITY` بیشترین ارتفاع ممکن پشته است و `size` نشان می‌دهد پشته واقعاً چقدر پر است. این کد با کد صف **یکی** است.
- این کد محدودیتی دارد، چون ظرفیت آرایه همیشه از پیش تعیین شده است؛ پس پشته ممکن است همیشه بیش از اندازه بزرگ باشد. تصور کن از ۵۰۰۰ جای پشته فقط یکی را استفاده کنی.
- خوب بود پشتهٔ ما **پویا** بود و با اضافه شدن اعضا بزرگ می‌شد.

> [!WARNING]
> **هشدار**
> درس‌نامه در این بخش از «یک جا از ۵۰۰۰» حرف می‌زند، در حالی که `CAPACITY` در کد بالا `50` است. عدد ۵۰۰۰ از مثال سخنرانی می‌آید (افزایش ظرفیت به ۵۰۰ یا ۵۰۰۰). این تفاوت در `sources.json` ثبت شده است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت LIFO همیشه انصاف ندارد ولی **راحتی** و کارایی دارد. نمونه‌اش صندوق ایمیل است: نامه‌های تازه بالا می‌آیند و اغلب اول به همان‌ها جواب می‌دهیم.
- **از سخنرانی:** او گفت پیاده‌سازی پشته با این `struct` کمی آسان‌تر از صف است، چون همیشه از **انتهای** آرایه برمی‌داری و اولین عضو می‌تواند همیشه در خانهٔ `0` بماند.
- **از سخنرانی:** او تأکید کرد محدودیت ۵۰تایی ویژگی پشته یا صف نیست، ویژگی **این پیاده‌سازی** است؛ همین است که به آن‌ها «انتزاعی» می‌گوییم.

ویدئوی کوتاه [Stacks](/kb/d/w05-sh-stacks) دو پیاده‌سازی پشته، با آرایه و با فهرست پیوندی، را نشان می‌دهد.

## اشتباه‌های رایج

- اشتباه گرفتن LIFO با FIFO.
- فکر کردن به اینکه چون کد پشته و صف یکی است، رفتارشان هم یکی است؛ فرق در این است که عضو از کجا برداشته می‌شود.

## جمع‌بندی

- پشته LIFO است و عملیاتش push و pop است.
- آرایهٔ ثابت برای پشته هم همان محدودیت صف را دارد: ظرفیت از پیش تعیین شده.

## پیوندها

- قبلی: [صف: اول وارد، اول خارج (FIFO)](/kb/d/w05-n03)
- بعدی: [بزرگ کردن آرایه با malloc و کپی](/kb/d/w05-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
