---
id: w05-n02
type: note
title: ساختمان داده و نوع دادهٔ انتزاعی (Data Structures)
title_fa: ساختمان داده و نوع دادهٔ انتزاعی
title_en: Data Structures
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Data Structures
official_anchor: data-structures
source_url: https://cs50.harvard.edu/x/2026/notes/5/#data-structures
source_refs:
- src-notes-5#data-structures
- src-transcript-5
- src-anzali-authored-5
- src-srt-5
concept_ids:
- w05-c-data-structure
- w05-c-abstract-data-type
- w05-c-dictionary-adt
prev: w05-n01
next: w05-n03
order: 2
video:
  youtube_id: PmAI76OGE_E
  start: '3:33'
  start_seconds: 213
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=213s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'known as abstract data types'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ساختمان داده و نوع دادهٔ انتزاعی

> **منبع رسمی:** بخش «Data Structures» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#data-structures). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳:۳۳ تا حدود ۳:۵۸](https://www.youtube.com/watch?v=PmAI76OGE_E&t=213s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پیش از نوشتن هر کدی باید بدانی ساختاری که می‌خواهی **چه رفتاری** دارد. این یادداشت دو اصطلاح پایه را جدا می‌کند: ساختمان داده و نوع دادهٔ انتزاعی.

## ساختمان‌های داده

- **ساختمان‌های داده** (data structures) در اصل شکل‌هایی از سازمان‌دهی در حافظه‌اند.
- راه‌های زیادی برای سازمان‌دهی داده در حافظه وجود دارد.
- **نوع‌های دادهٔ انتزاعی** (abstract data types) آن‌هایی‌اند که می‌توانیم به‌صورت مفهومی تصورشان کنیم. در یادگیری علوم کامپیوتر معمولاً مفید است از همین ساختارهای مفهومی شروع کنیم؛ یاد گرفتن آن‌ها فهم پیاده‌سازی ساختارهای مشخص‌تر را بعداً آسان‌تر می‌کند.

> [!TIP]
> **تألیفی: نوع انتزاعی یا ساختمان داده؟**
> یک راه ساده برای جدا کردن این دو: نوع دادهٔ انتزاعی می‌گوید **چه کاری** می‌شود کرد (مثلاً «به صف اضافه کن» و «از سر صف بردار»)، و ساختمان داده می‌گوید داده **چطور** در حافظه چیده می‌شود (مثلاً آرایه یا فهرست پیوندی). یک نوع انتزاعی را می‌شود با چند ساختمان دادهٔ مختلف پیاده کرد.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David توضیح داد که آنچه در ویدئوی Jack دیدیم نوع‌های دادهٔ انتزاعی بودند: مهم ویژگی‌ها و کارکردی است که ساختار ارائه می‌دهد، مستقل از اینکه در سطح پایین چطور پیاده شده باشد.
- **از سخنرانی:** او **دیکشنری** را نوع انتزاعی دیگری معرفی کرد: جدولی دوستونی که در یک ستون «کلید» و در ستون دیگر «مقدار» است، مثل واژه و معنی در فرهنگ لغت یا نام و شماره در دفترچهٔ تلفن. هر جا بخواهی دادهای را به دادهٔ دیگری نسبت بدهی (جفت کلید-مقدار)، دیکشنری ابزار اصلی است.
- **از سخنرانی:** او گفت دیکشنری را هم می‌شود به چند شکل پیاده کرد؛ یکی سریع و دیگری کند. مثلاً اگر برنامهٔ مخاطبین گوشی با یک آرایهٔ ثابت پیاده شده بود و فقط ۵۰ دوست را جا می‌داد، محدودیت آزاردهنده‌ای بود.

> [!NOTE]
> **یادداشت**
> بخش «Data Structures» درس‌نامه دیکشنری را نام نمی‌برد؛ این مطلب فقط **از سخنرانی** است. بعدها در همین هفته جدول درهم‌سازی را می‌بینی که David آن را راه رایج پیاده‌سازی دیکشنری خواند.

## اشتباه‌های رایج

- یکی گرفتن «صف» با «آرایه»: صف یک رفتار است و آرایه فقط یکی از راه‌های پیاده‌سازی آن.
- فکر کردن به اینکه هر محدودیت یک پیاده‌سازی (مثلاً ظرفیت ثابت) محدودیت خود نوع انتزاعی است.

## جمع‌بندی

- ساختمان داده: شکل سازمان‌دهی داده در حافظه.
- نوع دادهٔ انتزاعی: رفتار و عملیات، مستقل از پیاده‌سازی.
- صف، پشته و دیکشنری نوع‌های انتزاعی‌اند که هر کدام چند پیاده‌سازی ممکن دارند.

## پیوندها

- قبلی: [خوش آمدید: Jack Learns the Facts](/kb/d/w05-n01)
- بعدی: [صف: اول وارد، اول خارج (FIFO)](/kb/d/w05-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
