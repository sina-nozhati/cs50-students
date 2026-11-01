---
id: w03-n03
type: note
title: جست‌وجوی دودویی (Binary Search)
title_fa: جست‌وجوی دودویی
title_en: Binary Search
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Binary Search
official_anchor: binary-search
source_url: https://cs50.harvard.edu/x/2026/notes/3/#binary-search
source_refs:
- src-notes-3#binary-search
- src-transcript-3
- src-short-binary-search
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-binary-search
- w03-c-sorted-precondition
prev: w03-n02
next: w03-n04
order: 3
video:
  youtube_id: 6Svu_ae5ebk
  start: '14:49'
  start_seconds: 889
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=889s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'Caitlin'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جست‌وجوی دودویی

> **منبع رسمی:** بخش «Binary Search» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#binary-search). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۴:۴۹ تا حدود ۲۷:۰۱](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=889s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اگر از قبل بدانی قفسه‌ها **مرتب** هستند، لازم نیست همه را باز کنی. **جست‌وجوی دودویی** (`binary search`) همان ترفند پاره کردن دفترچهٔ تلفن در هفتهٔ صفر است، این بار روی آرایه.

## شرط لازم: مرتب بودن

- جست‌وجوی دودویی یک **الگوریتم جست‌وجو** (`search algorithm`) دیگر برای پیدا کردن `50` است.
- با این فرض که مقدارهای داخل قفسه‌ها **از کوچک به بزرگ** چیده شده‌اند، شبه‌کدش این است:

```text
If no doors left
    Return false
If 50 is behind middle door
    Return true
Else if 50 < middle door
    Search left half
Else if 50 > middle door
    Search right half
```

- با واژگان کد، الگوریتم را این‌طور دقیق‌تر می‌کنیم:

```text
If no doors left
    Return false
If 50 is behind doors[middle]
    Return true
Else if 50 < doors[middle]
    Search doors[0] through doors[middle - 1]
Else if 50 > doors[middle]
    Search doors[middle + 1] through doors[n - 1]
```

- درس‌نامه می‌گوید با دیدن این تقریب تقریباً می‌توانی کد واقعی را تصور کنی.

> [!IMPORTANT]
> **مهم**
> جست‌وجوی دودویی روی آرایهٔ **نامرتب** کار نمی‌کند. اگر داده مرتب نباشد، نمی‌دانی نیمه‌ای که دور می‌اندازی چه چیزی را از دست می‌دهد.

## گام‌به‌گام

- `If no doors left` حالتی است که دیگر جایی برای گشتن نمانده؛ یعنی `50` نیست.
- اگر `50` از قفسهٔ وسط کوچک‌تر بود، فقط **نیمهٔ چپ** (`doors[0]` تا `doors[middle - 1]`) را می‌گردیم و اگر بزرگ‌تر بود، **نیمهٔ راست** (`doors[middle + 1]` تا `doors[n - 1]`).
- خودِ قفسهٔ وسط را دیگر نگاه نمی‌کنیم؛ برای همین `- 1` و `+ 1` آمده است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** Kelly اسکناس‌ها را از کوچک به بزرگ چید و داوطلب دوم، Caitlin، از وسط شروع کرد. ۲۰ را دید، پس ۵۰ باید سمت راست باشد؛ وسطِ سه قفسهٔ باقی‌مانده ۱۰۰ بود و ۵۰ درست کنارش پیدا شد. David گفت این همان ایدهٔ دفترچهٔ تلفن است: وسط، بعد وسطِ وسط، و همین‌طور.
- **از ویدئوی کوتاه Binary Search:** Doug Lloyd سه متغیر را دنبال می‌کند: شروع (`start`)، پایان (`end`) و وسط (`midpoint`). اگر `start` از `end` بزرگ‌تر شود، زیرآرایه اندازهٔ صفر دارد و عدد در آرایه نیست.

> [!TIP]
> **راهنما**
> یک آزمایش ذهنی: در آرایه‌ای مرتب با ۱۰۲۴ عضو، جست‌وجوی دودویی حداکثر حدود ۱۰ بار نصف می‌کند (۲ به توان ۱۰ برابر ۱۰۲۴ است). جست‌وجوی خطی ممکن است ۱۰۲۴ قفسه باز کند.

## اشتباه‌های رایج

- اجرای جست‌وجوی دودویی روی دادهٔ نامرتب.
- فراموش کردن شرط «هیچ دری نمانده» و گیر افتادن در جست‌وجوی بی‌پایان.
- نگه داشتن قفسهٔ وسط در نیمهٔ بعدی به‌جای `middle - 1` یا `middle + 1`.

## جمع‌بندی

- جست‌وجوی دودویی در هر گام نیمی از مسئله را حذف می‌کند.
- پیش‌شرطش مرتب بودن داده است.

## پیوندها

- قبلی: [جست‌وجوی خطی و قفسه‌ها](/kb/d/w03-n02)
- بعدی: [زمان اجرا و نماد O بزرگ](/kb/d/w03-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
