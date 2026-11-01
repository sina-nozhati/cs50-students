---
id: w04-n13
type: note
title: سرریز پشته و هیپ (Overflow)
title_fa: سرریز پشته و هیپ
title_en: Overflow
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Overflow
official_anchor: overflow
source_url: https://cs50.harvard.edu/x/2026/notes/4/#overflow
source_refs:
- src-notes-4#overflow
- src-transcript-4
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-overflow
prev: w04-n12
next: w04-n14
order: 13
video:
  youtube_id: db0H0U13YsA
  start: '1:49:07'
  start_seconds: 6547
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=6547s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'overflow the stack or equivalently heap'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# سرریز پشته و هیپ

> **منبع رسمی:** بخش «Overflow» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#overflow). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۹:۰۷ تا حدود ۱:۵۱:۲۵](https://www.youtube.com/watch?v=db0H0U13YsA&t=6547s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

heap و stack در یک فضای محدودند. اگر یکی بیش از حد بزرگ شود یا بیرون از محدوده بنویسیم، به خطاهایی می‌خوریم که اسمشان را احتمالاً شنیده‌ای.

## سرریز

- **heap overflow** یعنی سرریز heap: دست زدن به ناحیه‌هایی از حافظه که نباید به آن‌ها دست بزنی.
- **stack overflow** یعنی صدا زدن تابع‌های بیش از حد، تا جایی که حافظهٔ موجود سرریز شود.
- هر دوی این‌ها نوعی **buffer overflow** به حساب می‌آیند.

> [!NOTE]
> **نکته**
> هر فراخوانی تابع یک قاب تازه روی stack می‌گذارد؛ بازگشتی که حالت پایه ندارد (هفتهٔ ۳) قاب‌ها را بی‌پایان روی هم می‌چیند. «بالا» و «پایین» فقط در تصویر هنری معنا دارند؛ در خود کامپیوتر جهتی وجود ندارد.

> [!TIP]
> **تألیفی: یک بازگشت بی‌پایان**
> تابع زیر (تألیفی، اجرا نکن) هیچ حالت پایه‌ای ندارد و آن‌قدر خودش را صدا می‌زند تا stack تمام شود؛ معمولاً برنامه با segmentation fault متوقف می‌شود.

```c
// تألیفی: نمونهٔ stack overflow
void forever(int n)
{
    forever(n + 1);
}
```

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت در این تصویر heap با هر `malloc` به سمت پایین رشد می‌کند و stack با هر فراخوانی تابع به سمت بالا، مثل سینی‌هایی که در سلف روی هم چیده می‌شوند. چون حافظه محدود است، این دو بالاخره ممکن است به هم برخورد کنند.
- **از سخنرانی:** او گفت با استفاده از قاب‌های بیش از حد می‌شود stack یا heap را سرریز کرد و این فقط یک اشتباه برنامه‌نویسی است.
- **از سخنرانی:** او گفت اسم وب‌سایت معروف Stack Overflow هم از همین می‌آید: اشاره به این مشکل بزرگ و رایج در کامپیوترها.

## اشتباه‌های رایج

- فکر کردن به اینکه «buffer overflow» فقط مشکل امنیتی دیگران است؛ `x[3] = 33` در `memory.c` هم نوشتن بیرون از بافر بود.
- بازگشت بدون حالت پایه.

## جمع‌بندی

- heap overflow: دست زدن به حافظهٔ heap که مال تو نیست.
- stack overflow: فراخوانی‌های تابع بیش از حد.
- هر دو buffer overflow هستند.

## پیوندها

- قبلی: [جابه‌جایی، پشته و هیپ](/kb/d/w04-n12)
- بعدی: [scanf: ورودی بدون کتابخانهٔ CS50](/kb/d/w04-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
