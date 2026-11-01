---
id: w04-n01
type: note
title: 'خوش آمدید: هنر پیکسلی (Welcome! and Pixel Art)'
title_fa: 'خوش آمدید: هنر پیکسلی'
title_en: Welcome! and Pixel Art
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Pixel Art
official_anchor: pixel-art
source_url: https://cs50.harvard.edu/x/2026/notes/4/#pixel-art
source_refs:
- src-notes-4#pixel-art
- src-transcript-4
- src-pset-4
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-pixel-art
prev: w04-fa
next: w04-n02
order: 1
video:
  youtube_id: db0H0U13YsA
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# خوش آمدید: هنر پیکسلی

> **منبع رسمی:** بخش «Pixel Art» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#pixel-art). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۴:۲۲](https://www.youtube.com/watch?v=db0H0U13YsA&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

درس‌نامه این هفته را با یک جملهٔ صادقانه شروع می‌کند: امروز بسیاری از «چرخ‌های کمکی» را که از اول دوره داشتی برمی‌داریم. تا اینجا با `string` و `get_string` کار کردی بی‌آنکه بدانی زیر کاپوت چه می‌گذرد. این هفته به صفر و یک‌هایی می‌رسیم که تصویرها و فایل‌ها را می‌سازند و یاد می‌گیریم چطور مستقیم به داده‌های ذخیره‌شده در **حافظه** دسترسی پیدا کنیم.

> [!NOTE]
> **نکته**
> درس‌نامه صریحاً می‌گوید مفاهیم این هفته ممکن است کمی طول بکشد تا «جا بیفتند». اگر بار اول همه‌چیز روشن نشد، طبیعی است. یادداشت‌ها را به ترتیب بخوان و مثال‌ها را خودت اجرا کن.

## هنر پیکسلی

- پیکسل‌ها مربع‌ها یا نقطه‌های رنگی کوچکی‌اند که روی یک شبکهٔ بالا و پایین و چپ و راست چیده شده‌اند.
- می‌توانی یک تصویر را مثل **نقشه‌ای از بیت‌ها** (bitmap) تصور کنی: صفر یعنی سیاه و یک یعنی سفید.
- درس‌نامه با تصویر یک صورتک سیاه و سفید نشان می‌دهد که چطور یک شبکه از صفر و یک‌ها به تصویر تبدیل می‌شود (پیوند تصویر در `media.json`، فقط پیوند).

این همان ایده‌ای است که در هفتهٔ صفر دیدی: هر چیزی، از جمله تصویر، در نهایت با بیت نمایش داده می‌شود. فرقش این است که این هفته قرار است خودت با C این بیت‌ها را بخوانی و تغییر بدهی، مثلاً در پرابلم‌ست [Filter](/kb/d/w04-ps-filter-less).

## سخنرانی چه می‌گوید

- **از سخنرانی:** سخنرانی با یک اثر هنری شروع شد: دو نفر از دانشجوها، Avery و Marie، پیش از کلاس با کاغذهای یادداشت چسب‌دار (Post-it) سبز و بنفش تصویری ساخته بودند که از دور یک گربه بود؛ گربه‌ای که فقط با صفر و یک‌ها ساخته شده بود.
- **از سخنرانی:** David گفت اگر روی یک تصویر زوم کنی، جزئیات بیشتری می‌بینی، اما اگر باز هم زوم کنی می‌فهمی که جزئیات تصویر محدود است و از نقطه‌ها یعنی پیکسل‌ها ساخته شده است.

> [!TIP]
> **تألیفی: یک آزمایش کوچک**
> روی یک کاغذ شطرنجی ۸ در ۸، خانه‌های «۱» را سفید و «۰» را سیاه رنگ کن تا یک صورتک بسازی. حالا ۶۴ رقم را سطر به سطر بنویس. همین فهرست، یک bitmap یک بیتی است.

## اشتباه‌های رایج

- فکر کردن به اینکه تصویر چیزی «جدا» از عددهاست. تصویر هم فقط دنباله‌ای از بیت‌هاست که به روش قراردادی تفسیر می‌شود.
- قاطی کردن «یک بیت برای هر پیکسل» (سیاه و سفید) با تصویرهای رنگی که بیت‌های بیشتری برای هر پیکسل لازم دارند.

## جمع‌بندی

- تصویر شبکه‌ای از پیکسل‌هاست و در ساده‌ترین حالت هر پیکسل یک بیت است.
- این هفته چرخ‌های کمکی برداشته می‌شوند و به خود حافظه نگاه می‌کنیم.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w04-fa)
- بعدی: [مبنای شانزده (هگزادسیمال)](/kb/d/w04-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
