---
id: w00-n10
type: note
title: 'آشنایی با Scratch: محیط و دستگاه مختصات (Scratch)'
title_fa: 'آشنایی با Scratch: محیط و دستگاه مختصات'
title_en: Scratch
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Scratch
official_anchor: scratch
source_url: https://cs50.harvard.edu/x/notes/0/#scratch
source_refs:
- src-notes-0#scratch
- src-transcript-0
- src-scratch-home
concept_ids:
- w00-c-scratch-interface
- w00-c-sprite
- w00-c-coordinates
prev: w00-n09
next: w00-n11
order: 10
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# آشنایی با Scratch: محیط و دستگاه مختصات

> **منبع رسمی:** بخش «Scratch» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#scratch). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

Scratch محیطی است که در آن تمام هفتهٔ ۰ و پرابلم‌ست اول را کار می‌کنی. شناختن بخش‌های محیط و **دستگاه مختصات** (coordinate system) لازم است تا بتوانی اسپرایت‌ها را حرکت بدهی.

## Scratch طبق درس‌نامه

- **Scratch** زبان برنامه‌نویسی بصری‌ای است که در MIT ساخته شده است.
- [Scratch](https://scratch.mit.edu) از همان بلوک‌های سازندهٔ اساسی استفاده می‌کند که پیش‌تر در این درس دیدیم.
- Scratch راه خوبی برای ورود به برنامه‌نویسی است، چون می‌توانی با این بلوک‌ها به‌شکل بصری بازی کنی و نگران نحو (syntax)، مثل آکولاد، نقطه‌ویرگول و پرانتز، نباشی.

## بخش‌های محیط Scratch (IDE)

![scratch interface](https://cs50.harvard.edu/x/notes/0/cs50Week0Slide162.png "scratch interface")

(تصویر از درس‌نامهٔ رسمی؛ فقط پیوند، روی سرور پنل ذخیره نشده است.)

طبق درس‌نامه:

1. **پالت بلوک‌ها** (blocks palette)، سمت چپ: بلوک‌های سازنده‌ای که در برنامه‌ات استفاده می‌کنی.
2. **ناحیهٔ برنامه‌نویسی** (programming area)، کنار پالت: جایی که بلوک‌ها را می‌کشی و برنامه را می‌سازی.
3. **صحنه** (stage)، سمت راست: جایی که گربه ایستاده و برنامه‌ات «زنده می‌شود».

**از سخنرانی:** زیر صحنه فهرست **اسپرایت‌ها** (sprites) دیده می‌شود. اسپرایت به‌طور پیش‌فرض یک گربه است، اما می‌تواند سگ، پرنده، سطل زباله یا هر چیز دیگری باشد. بلوک‌ها **رنگ‌بندی** شده‌اند تا نوع کارشان معلوم باشد (Events، Looks، Sound، Control، Sensing، Operators، Variables و…). استاد می‌گوید در ۲۰ سال هرگز از همهٔ بلوک‌ها استفاده نکرده است.

## دستگاه مختصات

![scratch coordinate system](https://cs50.harvard.edu/x/notes/0/cs50Week0Slide167.png "scratch coordinate system")

- طبق درس‌نامه، مرکز صحنه مختصات `(0,0)` است و گربه اکنون در همان نقطه قرار دارد.
- **از سخنرانی:** بالای صحنه `y = 180`، پایین `y = -180`، چپ `x = -240` و راست `x = 240` است. واحد حرکت پیکسل است: «یک پیکسل یا ده پیکسل بالا برو».

**طرح تألیفی بر پایهٔ سخنرانی:**

```text
            (0, 180)
               |
(-240, 0) -- (0, 0) -- (240, 0)
               |
            (0, -180)
```

## مثال تألیفی

اگر اسپرایت در `(0, 0)` باشد و بلوک `change x by (10)` را سه بار اجرا کنیم، به `(30, 0)` می‌رسد، یعنی ۳۰ پیکسل به راست. `change y by (-10)` اسپرایت را پایین می‌برد.

> **نکتهٔ RTL:** در پنل فارسی، متن راست‌به‌چپ است، اما محور x در Scratch همچنان **از چپ به راست افزایش می‌یابد**. «راست» در Scratch یعنی x مثبت.

## اشتباه‌های رایج

- اینکه فکر کنی `(0,0)` گوشهٔ بالا-چپ صحنه است (مثل خیلی از سیستم‌های گرافیکی دیگر). در Scratch، `(0,0)` **مرکز** است.
- یکی گرفتن افزایش y با پایین رفتن. در Scratch، y مثبت یعنی **بالا**.
- اینکه فکر کنی هر پروژه فقط یک گربه دارد. می‌توانی اسپرایت‌های زیادی بسازی، و پرابلم‌ست دقیقاً همین را می‌خواهد.

## محدودیت‌ها

ابعاد صحنه از سخنرانی آمده است (درس‌نامه فقط مرکز را ذکر می‌کند). جزئیات رابط کاربری Scratch ممکن است با به‌روزرسانی‌های MIT کمی تغییر کند.

## جمع‌بندی

- Scratch = زبان بصری MIT، بدون دردسر نحو.
- سه ناحیه: پالت بلوک‌ها، ناحیهٔ برنامه‌نویسی، صحنه.
- مرکز صحنه `(0,0)`؛ x از ۲۴۰− تا ۲۴۰ و y از ۱۸۰− تا ۱۸۰ (طبق سخنرانی).

## سؤال‌های خودآزمایی

1. صحنه در محیط Scratch چه نقشی دارد؟
2. مختصات مرکز صحنه چیست؟
3. برای بردن اسپرایت به بالای صحنه، y را زیاد می‌کنی یا کم؟

**پاسخ کوتاه:** ۱) جایی که برنامه اجرا و دیده می‌شود. ۲) `(0, 0)`. ۳) زیاد.

## پیوندها

- قبلی: [در ادامهٔ دوره: از Scratch تا C و انتزاع](/kb/d/w00-n09)
- بعدی: [سلام دنیا: رویداد، تابع، آرگومان و اثر جانبی](/kb/d/w00-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
