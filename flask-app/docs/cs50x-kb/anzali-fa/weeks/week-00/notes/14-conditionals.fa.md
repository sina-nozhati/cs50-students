---
id: w00-n14
type: note
title: شرط‌ها و حلقهٔ همیشگی (Conditionals)
title_fa: شرط‌ها و حلقهٔ همیشگی
title_en: Conditionals
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Conditionals
official_anchor: conditionals
source_url: https://cs50.harvard.edu/x/notes/0/#conditionals
source_refs:
- src-notes-0#conditionals
- src-transcript-0
- src-src0-zip
concept_ids:
- w00-c-forever-loop
- w00-c-conditional
- w00-c-boolean-expression
prev: w00-n13
next: w00-n15
order: 14
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# شرط‌ها و حلقهٔ همیشگی

> **منبع رسمی:** بخش «Conditionals» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#conditionals). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

برنامه‌ها باید بتوانند **تصمیم** بگیرند: «اگر این اتفاق افتاد، آن کار را بکن». **شرط** (conditional) همین است. ترکیب شرط با حلقهٔ **همیشگی** (forever) پایهٔ هر بازی و برنامهٔ تعاملی است.

## شرط طبق درس‌نامه

- شرط‌ها بلوک سازندهٔ اساسی برنامه‌نویسی‌اند: برنامه بررسی می‌کند آیا شرط مشخصی برقرار است. اگر برقرار باشد، کاری انجام می‌دهد.

```text
when green flag clicked
forever
if <touching (mouse-pointer v)?> then
play sound (Meow v) until done
```

- بلوک `forever` باعث می‌شود بلوک `if` بارها و بارها اجرا شود، تا برنامه پیوسته بررسی کند که آیا گربه با نشانگر ماوس تماس دارد. (در Scratch، `if` داخل `forever` است و `play sound` داخل `if`.)

## حسگر ویدئو (عیناً مطابق درس‌نامه)

```text
when video motion > (10)
play sound (Meow v) until done
```

این برنامه از حسگر ویدئو (video sensing) استفاده می‌کند: وقتی حرکت در تصویر دوربین از ۱۰ بیشتر شود، گربه میو می‌کند. درس‌نامه توضیح بیشتری نمی‌دهد. «video sensing» یک افزونهٔ Scratch است و دوربین لازم دارد.

## توصیهٔ درس‌نامه

برنامه‌نویسی اغلب فرایند آزمون و خطاست. اگر کلافه شدی، وقت بگذار و مسئله را برای خودت توضیح بده: دقیقاً روی چه مشکلی کار می‌کنی؟ چه چیزی کار می‌کند؟ چه چیزی کار نمی‌کند؟

## اشکال‌زدایی در سخنرانی: چرا forever لازم است؟

در سخنرانی، استاد عمداً `forever` را حذف کرد. نتیجه این بود که نوازش گربه کار نکرد. چرا؟ برنامه آن‌قدر سریع است که در همان لحظهٔ کلیک روی پرچم سبز شرط را یک بار بررسی کرد. آن لحظه نشانگر روی گربه نبود، پس کار تمام شد. `forever` تضمین می‌کند پرسش **پیوسته** پرسیده شود.

> **مثال اضافه از کد منبع (pet1.sb3):** در فایل رسمی `pet1.sb3` شرط دوشاخه است: اگر نشانگر ماوس با گربه تماس داشته باشد صدای `Roar` پخش می‌شود، وگرنه `Meow` پخش می‌شود و ۱ ثانیه صبر می‌کند. این فایل در درس‌نامه توصیف نشده است (sources.json، d05).

## تعریف‌ها

- **شرط (conditional):** بلوکی مثل `if … then` (یا `if … then … else`) که بر اساس یک پرسش تصمیم می‌گیرد.
- **عبارت بولی (boolean expression):** خود پرسش، مثل `<touching (mouse-pointer)?>`. در Scratch، بلوک‌های بولی **شش‌ضلعی/زاویه‌دار** هستند.
- **حلقهٔ همیشگی (forever):** حلقه‌ای که تا توقف برنامه ادامه دارد.

## مثال تألیفی

```text
when green flag clicked
forever
if <key (space v) pressed?> then
say [Jump!] for (1) seconds
```

تا وقتی برنامه اجرا می‌شود، هر بار که کلید فاصله فشرده شود، اسپرایت «Jump!» می‌گوید.

## اشتباه‌های رایج

- `if` بدون `forever` برای چیزی که باید پیوسته بررسی شود.
- قرار دادن `forever` **داخل** `if`. یک بار بررسی می‌شود و اگر برقرار باشد، برای همیشه تکرار می‌شود، حتی بعد از اینکه شرط دیگر برقرار نیست.
- اگر نشانگر روی گربه بماند، میو مدام تکرار می‌شود. این رفتار درست است (طبق سخنرانی) و اشکال نیست.

## محدودیت‌ها

حسگر ویدئو به دوربین و افزونه نیاز دارد و ممکن است روی همهٔ دستگاه‌ها در دسترس نباشد. برای پرابلم‌ست لازم نیست.

## جمع‌بندی

- شرط = «اگر پرسش درست بود، این کار را بکن».
- `forever` + `if` = بررسی پیوسته.
- آزمون و خطا بخشی طبیعی از برنامه‌نویسی است.

## سؤال‌های خودآزمایی

1. چرا بدون `forever`، نوازش گربه کار نکرد؟
2. در `if <touching (mouse-pointer v)?> then`، عبارت بولی کدام است؟
3. سه پرسشی که درس‌نامه برای وقت کلافگی پیشنهاد می‌کند چیست؟

**پاسخ کوتاه:** ۱) شرط فقط یک بار، در لحظهٔ شروع، بررسی شد. ۲) `touching (mouse-pointer)?`. ۳) دقیقاً روی چه مشکلی کار می‌کنم؟ چه کار می‌کند؟ چه کار نمی‌کند؟

## پیوندها

- قبلی: [میو: حلقه، بلوک سفارشی و انتزاع](/kb/d/w00-n13)
- بعدی: [Oscartime: چند اسپرایت، چند اسکریپت و امتیاز](/kb/d/w00-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
