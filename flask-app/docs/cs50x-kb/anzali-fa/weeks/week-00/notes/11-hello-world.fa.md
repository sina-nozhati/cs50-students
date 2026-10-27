---
id: w00-n11
type: note
title: 'سلام دنیا: رویداد، تابع، آرگومان و اثر جانبی (Hello World)'
title_fa: 'سلام دنیا: رویداد، تابع، آرگومان و اثر جانبی'
title_en: Hello World
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Hello World
official_anchor: hello-world
source_url: https://cs50.harvard.edu/x/notes/0/#hello-world
source_refs:
- src-notes-0#hello-world
- src-transcript-0
- src-src0-zip
concept_ids:
- w00-c-event
- w00-c-argument
- w00-c-side-effect
- w00-c-function
prev: w00-n10
next: w00-n12
order: 11
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# سلام دنیا: رویداد، تابع، آرگومان و اثر جانبی

> **منبع رسمی:** بخش «Hello World» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#hello-world). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

اولین برنامهٔ تقریباً هر برنامه‌نویسی «hello, world» است. همین برنامهٔ دو بلوکی سه مفهوم کلیدی را نشان می‌دهد: **رویداد** (event)، **تابع** (function) با **آرگومان** (argument)، و **اثر جانبی** (side effect).

## برنامه (عیناً مطابق درس‌نامه)

درس‌نامه می‌گوید: بلوک «when green flag clicked» را به ناحیهٔ برنامه‌نویسی بکش، سپس بلوک `say` را بکش و به بلوک قبلی بچسبان.

```text
when green flag clicked
say [hello, world]
```

## خروجی مورد انتظار

وقتی روی **پرچم سبز** (green flag) بالای صحنه کلیک کنی، گربه در یک حباب گفت‌وگو می‌گوید: «hello, world».

**از سخنرانی:** حباب بعد از اجرا روی صحنه می‌ماند، چون برنامه هرگز نگفته «دیگر نگو». با **علامت توقف قرمز** (stop sign) برنامه متوقف می‌شود.

## تحلیل با مدل «ورودی ← الگوریتم ← خروجی»

![scratch with black box](https://cs50.harvard.edu/x/notes/0/cs50Week0Slide172.png "scratch with black box")

طبق درس‌نامه، ورودی `hello, world` به تابع `say` داده می‌شود و **اثر جانبی** اجرای آن تابع این است که گربه `hello, world` را می‌گوید.

| جزء مدل | در این برنامه |
| --- | --- |
| ورودی (آرگومان) | متن `hello, world` در بیضی سفید |
| الگوریتم / تابع | بلوک `say` (که MIT پیاده‌سازی کرده است) |
| خروجی (اثر جانبی) | حباب گفت‌وگوی گربه روی صحنه |

## مفاهیم از سخنرانی (در درس‌نامه کوتاه آمده)

- **رویداد (event):** بلوک‌های دستهٔ زرد-نارنجی **Events** چیزهایی هستند که هنگام اجرای برنامه «اتفاق می‌افتند». «when green flag clicked» رایج‌ترینِ آن‌هاست. اجرای اسکریپت با رویداد شروع می‌شود.
- **آرگومان یا پارامتر (argument / parameter):** بیضی سفید داخل `say` قابل ویرایش است. چیزی که آنجا می‌نویسی ورودی تابع است و رفتارش را تعیین می‌کند.
- **تابع در برابر الگوریتم:** طبق سخنرانی، الگوریتم «مفهوم» است و تابع «تجسم آن در کد».
- **اثر جانبی (side effect):** چیزی که در نتیجهٔ اجرای تابع دیده یا شنیده می‌شود، مثل حباب گفت‌وگو روی صفحه یا صدایی از بلندگو.
- بلوک‌هایی که شکل سازگار دارند، مثل آهنربا به هم «می‌چسبند».

## مثال تألیفی

```text
when green flag clicked
say [Salam, Anzali!] for (2) seconds
```

این نسخه از بلوک «say … for … seconds» استفاده می‌کند، پس حباب بعد از ۲ ثانیه ناپدید می‌شود. این بلوک دو آرگومان دارد: متن و مدت.

## اشتباه‌های رایج

- بلوک `say` را بدون رویداد در ناحیه رها کنی. با کلیک روی پرچم سبز اتفاقی نمی‌افتد، چون اسکریپت شروع‌کننده ندارد.
- بلوک‌ها از هم جدا مانده باشند. اگر `say` به بلوک رویداد «نچسبیده» باشد، بخشی از آن اسکریپت نیست.
- یکی گرفتن «آرگومان» با «خروجی». آرگومان به تابع **داده می‌شود**؛ اثر جانبی **نتیجه** است.

## محدودیت‌ها

این برنامه همیشه یک چیز را می‌گوید و تعاملی نیست. نسخهٔ تعاملی را در [سلام به تو](/kb/d/w00-n12) می‌بینی.

## جمع‌بندی

- اسکریپت با یک **رویداد** شروع می‌شود (پرچم سبز).
- `say` تابع است، متن داخلش **آرگومان**، و حباب گفت‌وگو **اثر جانبی**.

## سؤال‌های خودآزمایی

1. در برنامهٔ hello, world، آرگومان تابع `say` چیست؟
2. اثر جانبی چیست؟ یک مثال از همین برنامه بزن.
3. اگر بلوک «when green flag clicked» را حذف کنیم، با کلیک روی پرچم سبز چه می‌شود؟

**پاسخ کوتاه:** ۱) `hello, world`. ۲) چیزی که در اثر اجرای تابع دیده یا شنیده می‌شود؛ حباب گفت‌وگوی گربه. ۳) هیچ اتفاقی نمی‌افتد.

## پیوندها

- قبلی: [آشنایی با Scratch: محیط و دستگاه مختصات](/kb/d/w00-n10)
- بعدی: [سلام به تو: ورودی، متغیر و مقدار بازگشتی](/kb/d/w00-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
