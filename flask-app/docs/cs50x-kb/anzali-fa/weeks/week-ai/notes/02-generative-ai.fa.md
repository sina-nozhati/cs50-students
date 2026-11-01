---
id: w71-n02
type: note
title: هوش مصنوعی مولد (Generative Artificial Intelligence)
title_fa: هوش مصنوعی مولد
title_en: Generative Artificial Intelligence
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Generative Artificial Intelligence
official_anchor: generative-artificial-intelligence
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#generative-artificial-intelligence
source_refs:
- src-notes-71#generative-artificial-intelligence
- src-transcript-71
- src-anzali-authored-71
- src-anzali-inference-71
- src-srt-71
concept_ids:
- w71-c-generative-ai
- w71-c-detecting-ai
prev: w71-n01
next: w71-n03
order: 2
video:
  youtube_id: -9bo8HlSxwQ
  start: '2:58'
  start_seconds: 178
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=178s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'generative artificial intelligence'
official_blocks: []
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# هوش مصنوعی مولد

> **منبع رسمی:** بخش «Generative Artificial Intelligence» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#generative-artificial-intelligence). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۵۸ تا حدود ۷:۵۹](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=178s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

ابزارهای امروز می‌توانند عکس، ویدئو، موسیقی و متنی بسازند که تشخیص آن از کار انسان سخت است. این بخش نشان می‌دهد **هوش مصنوعی مولد** (`generative AI`) به چه معناست و چرا «نگاه کردن» دیگر برای تشخیص کافی نیست.

## هوش مصنوعی مولد

- ابزارهای فراوانی امکان ورود تصویرهای ساخته‌شده با هوش مصنوعی به جهان را فراهم کرده‌اند.
- تا چند سال پیش، بیشتر این ابزارها **نشانه‌های** آشکاری داشتند که به بیننده می‌گفت تصویر ساختگی است.
- اما ابزارها در ساختن این تصویرها بسیار خوب شده‌اند. با پیشرفت فناوری، به‌زودی تشخیص چنین تصویرهایی با چشم غیرمسلح تقریباً، اگر نه کاملاً، ناممکن می‌شود.
- هوش مصنوعی مولد می‌تواند **عکس، ویدئو، موسیقی و متن** بسازد.

## بازی «کدام ساختگی است؟»

- از سخنرانی: حاضران با تلفن رأی دادند که کدام نمونه کار هوش مصنوعی است (نمونه‌ها از The New York Times بود).
- از سخنرانی: در دور اول، بیش از ۷۰٪ درست گفتند که عکس سمت راست ساختگی است. در دور دوم پاسخ **هر دو** بود: هیچ‌کدام از آن دو چهره در دنیای واقعی وجود نداشت و از روی دادهٔ آموزشی فراوان ساخته شده بود.
- از سخنرانی: در دور سوم، دو انشای کوتاه دربارهٔ ناهار مقایسه شد؛ متنی که هوش مصنوعی نوشته بود همانی بود که کمتر شبیه نوشتهٔ یک کودک کلاس چهارم یا پنجم بود. مالان گفت این بازی را در سال‌های آینده نمی‌شود انجام داد، چون تشخیص بیش از حد سخت می‌شود.

> [!NOTE]
> **تألیفی: برداشت برای دانشجو**
> اگر تشخیص با چشم ممکن نیست، دربارهٔ هر تصویر یا متن مهم بپرس از کجا آمده است. این همان مهارتی است که در هفتهٔ ۹ دربارهٔ «هرگز به ورودی کاربر اعتماد نکن» تمرین کردی، این بار برای محتوا.

## پیوندها

- قبلی: [اردک پلاستیکی و CS50.ai](/kb/d/w71-n01)
- بعدی: [مهندسی پرامپت، کد chat3.py و Copilot](/kb/d/w71-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
