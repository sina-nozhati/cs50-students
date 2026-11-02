---
id: w05-n01
type: note
title: 'خوش آمدید: Jack Learns the Facts (Welcome! and Jack Learns the Facts)'
title_fa: 'خوش آمدید: Jack Learns the Facts'
title_en: Welcome! and Jack Learns the Facts
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Welcome!
official_anchor: welcome
source_url: https://cs50.harvard.edu/x/2026/notes/5/#welcome
source_refs:
- src-notes-5#welcome
- src-transcript-5
- src-notes-5#jack-learns-the-facts
- src-jack-learns-the-facts
- src-srt-5
concept_ids:
- w05-c-organizing-memory
prev: w05-fa
next: w05-n02
order: 1
video:
  youtube_id: PmAI76OGE_E
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# خوش آمدید: Jack Learns the Facts

> **منبع رسمی:** بخش «Welcome!» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#welcome). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۳:۳۳](https://www.youtube.com/watch?v=PmAI76OGE_E&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هفته‌های قبل بلوک‌های پایهٔ برنامه‌نویسی را به تو دادند: متغیر، حلقه، تابع، آرایه، `struct` و در هفتهٔ ۴ اشاره‌گر و `malloc`. این هفته از همین ابزارها برای **سازمان‌دهی داده در حافظه** استفاده می‌کنی و می‌بینی هر شیوهٔ سازمان‌دهی چه امکان‌های طراحی‌ای باز می‌کند و چه هزینه‌ای دارد.

## خوش آمدید

- هفته‌های پیشین بلوک‌های بنیادی برنامه‌نویسی را معرفی کردند.
- هر آنچه در C یاد گرفته‌ای کمکت می‌کند همین بلوک‌ها را در زبان‌های سطح بالاتر مثل Python هم پیاده کنی.
- هر هفته مفاهیم سخت‌تر شده‌اند، مثل تپه‌ای که شیبش مدام تندتر می‌شود. این هفته، با بررسی **ساختمان‌های داده**، شیب کمی هموار می‌شود.
- تا اینجا دیده‌ای که یک آرایه چطور داده را در حافظه مرتب می‌کند.
- امروز دربارهٔ سازمان‌دهی داده در حافظه و امکان‌های طراحی‌ای صحبت می‌کنیم که از دانش رو به رشد تو بیرون می‌آیند.

## Jack Learns the Facts

درس‌نامه می‌گوید در کلاس ویدئویی به نام [Jack Learns the Facts](https://www.youtube.com/watch?v=ItAG3s6KIEI) ساختهٔ پروفسور Shannon Duvall از دانشگاه Elon پخش شد. این ویدئو بیرون از CS50 است و در این بسته فقط پیوند داده می‌شود.

> [!NOTE]
> **یادداشت**
> داستان ویدئو: Jack لباس‌ها، CDها و کتاب‌هایش را روی هم در یک جعبه می‌گذارد و هر روز همان بالایی را برمی‌دارد، پس همیشه چند لباس محدود را می‌پوشد. دوستش Lou پیشنهاد می‌کند لباس‌ها را در کمد به صف کند: از یک سر بگذارد و از سر دیگر بردارد تا «همه چیز را یک بار بپوشد پیش از آنکه چیزی را دو بار بپوشد». این دو رفتار همان **پشته** و **صف**اند که در یادداشت‌های بعدی می‌بینی.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت این آخرین هفتهٔ C است و هفتهٔ بعد به Python می‌رویم؛ زبانی سطح بالاتر که حل همین مسئله‌ها را برای انسان سریع‌تر می‌کند، هرچند اجرای کد لزوماً به همان سرعت C نیست.
- **از سخنرانی:** او گفت موضوع مشترک این هفته و هفتهٔ بعد **بده‌بستان** (trade-off) است؛ همان مضمونی که از هفته‌های قبل دیده‌ای.

## اشتباه‌های رایج

- فکر کردن به اینکه این هفته ابزار تازه‌ای جز عملگر `->` لازم داری؛ بیشتر کار ترکیب `struct`، اشاره‌گر و `malloc` از هفته‌های ۳ و ۴ است.
- نادیده گرفتن بده‌بستان‌ها: هر ساختمان داده‌ای در ازای مزیتی هزینه‌ای دارد.

## جمع‌بندی

- این هفته دربارهٔ سازمان‌دهی داده در حافظه است، با ابزارهایی که از قبل داری: `struct`، اشاره‌گر و `malloc`.
- پشته و صف را با یک داستان روزمره دیدی؛ تعریف دقیقشان در یادداشت‌های ۳ و ۴ می‌آید.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w05-fa)
- بعدی: [ساختمان داده و نوع دادهٔ انتزاعی](/kb/d/w05-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
