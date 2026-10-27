---
id: w00-n05
type: note
title: یونیکد و ایموجی (Unicode)
title_fa: یونیکد و ایموجی
title_en: Unicode
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Unicode
official_anchor: unicode
source_url: https://cs50.harvard.edu/x/notes/0/#unicode
source_refs:
- src-notes-0#unicode
- src-transcript-0
- src-wiki-unicode
- src-wiki-emoji
concept_ids:
- w00-c-unicode
prev: w00-n04
next: w00-n06
order: 5
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# یونیکد و ایموجی

> **منبع رسمی:** بخش «Unicode» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#unicode). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

ما فارسی می‌نویسیم و ایموجی می‌فرستیم، اما ASCII فقط ۱۲۸ نویسه دارد. **یونیکد** (Unicode) همان استانداردی است که اجازه می‌دهد «سلام» و ایموجی روی هر دستگاهی درست نمایش داده شوند.

## یونیکد طبق درس‌نامه

- با گذشت زمان، راه‌های بیشتر و بیشتری برای ارتباط متنی پیدا شده است.
- چون بیت‌های کافی برای نمایش همهٔ نویسه‌های انسانی نبود، استاندارد **یونیکد** تعداد بیت‌هایی را که کامپیوترها می‌فرستند و می‌فهمند افزایش داد. یونیکد نه‌تنها نویسه‌های خاص، بلکه **ایموجی** (emoji) را هم شامل می‌شود.
- الگوی صفر و یکِ هر ایموجی در یونیکد استاندارد است، اما **هر سازندهٔ دستگاه ممکن است آن را کمی متفاوت نمایش دهد.**
- قابلیت‌های تازه مدام به یونیکد اضافه می‌شود تا نویسه‌ها و ایموجی‌های بیشتری را نمایش دهد.
- برای مطالعهٔ بیشتر: [ویکی‌پدیا: Unicode](https://en.wikipedia.org/wiki/Unicode) و [ویکی‌پدیا: Emoji](https://en.wikipedia.org/wiki/Emoji).

> **نکتهٔ طراحی محتوا:** درس‌نامهٔ رسمی چند ردیف ایموجی را به‌عنوان نمونه نشان می‌دهد. طبق سیستم طراحی پنل CS50x Anzali (ممنوعیت ایموجی در پایگاه دانش)، آن‌ها را اینجا تکرار نکرده‌ایم. برای دیدنشان به [درس‌نامهٔ رسمی](https://cs50.harvard.edu/x/notes/0/#unicode) سر بزن.

## نکته‌های تکمیلی از سخنرانی

- یونیکد «ابرمجموعه» (superset) ASCII است؛ یعنی ASCII را در خود دارد.
- یونیکد به‌جای ۷ یا ۸ بیت، ممکن است برای هر نویسه ۱۶، ۲۴ یا حتی ۳۲ بیت استفاده کند. با ۳۲ بیت حدود ۴ میلیارد الگو ممکن است.
- هدف کنسرسیوم یونیکد (Unicode Consortium) نمایش دیجیتال همهٔ زبان‌های انسانی است: گذشته، حال و آینده.
- ایموجی‌ها در واقع **نویسه** هستند، نه تصویر. فقط با «فونتی» رنگی و گرافیکی نمایش داده می‌شوند. برای همین ایموجی «صورت با اشک شوق» (face with tears of joy) روی iOS، اندروید و تلگرام کمی متفاوت دیده می‌شود، اما الگوی بیت‌هایش یکی است.

## مثال تألیفی

حرف «س» فارسی در ASCII وجود ندارد، چون ASCII فقط ۱۲۸ کد دارد. در یونیکد، «س» یک کد مشخص دارد و هر دستگاهی که یونیکد را بشناسد آن را «س» نشان می‌دهد. شکل دقیقش به فونت بستگی دارد، مثلاً Vazirmatn در همین پنل.

## اشتباه‌های رایج

- اینکه فکر کنی ایموجی یک «عکس کوچک» است که فرستاده می‌شود. در یونیکد، ایموجی نویسه است.
- انتظار اینکه ایموجی روی همهٔ گوشی‌ها دقیقاً یک شکل باشد.
- فرض اینکه یونیکد همیشه دقیقاً ۳۲ بیت برای هر نویسه مصرف می‌کند. سخنرانی از «۱۶، ۲۴ یا ۳۲ بیت» حرف می‌زند. شیوه‌های دقیق رمزگذاری (encoding) در این هفته مطرح نمی‌شود.

## محدودیت‌ها

درس‌نامه وارد جزئیات کدگذاری‌هایی مثل UTF-8 نمی‌شود. ما هم وارد نمی‌شویم تا از متن رسمی جلو نزنیم.

## جمع‌بندی

- یونیکد استانداردی گسترده‌تر از ASCII است و ایموجی و نویسه‌های همهٔ زبان‌ها را پوشش می‌دهد.
- الگوی بیت استاندارد است؛ ظاهر نمایش به سازنده و فونت بستگی دارد.

## سؤال‌های خودآزمایی

1. چرا ASCII برای فارسی کافی نیست؟
2. چرا یک ایموجی روی دو گوشی مختلف ممکن است متفاوت دیده شود؟
3. درست یا نادرست: یونیکد ASCII را هم در بر می‌گیرد.

**پاسخ کوتاه:** ۱) فقط ۱۲۸ نویسه دارد که برای حروف انگلیسی و علائم کافی است. ۲) الگوی بیت یکسان است، اما هر سازنده طراحی گرافیکی خودش را دارد. ۳) درست (طبق سخنرانی، یونیکد ابرمجموعهٔ ASCII است).

## پیوندها

- قبلی: [اَسکی: نمایش حروف با عدد](/kb/d/w00-n04)
- بعدی: [RGB، پیکسل، ویدئو و موسیقی](/kb/d/w00-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
