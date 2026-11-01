---
id: w71-n08
type: note
title: مدل‌های زبانی بزرگ، توجه و توهم (Large Language Models and Summing Up)
title_fa: مدل‌های زبانی بزرگ، توجه و توهم
title_en: Large Language Models and Summing Up
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Large Language Models
official_anchor: large-language-models
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#large-language-models
source_refs:
- src-notes-71#large-language-models
- src-transcript-71
- src-cs50-ai
- src-anzali-authored-71
- src-srt-71
concept_ids:
- w71-c-llm
- w71-c-attention-transformer
- w71-c-embeddings
- w71-c-hallucination
prev: w71-n07
next: w71-summary
order: 8
video:
  youtube_id: -9bo8HlSxwQ
  start: '42:52'
  start_seconds: 2572
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=2572s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'full circle to something like'
official_blocks: []
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# مدل‌های زبانی بزرگ، توجه و توهم

> **منبع رسمی:** بخش «Large Language Models» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#large-language-models). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴۲:۵۲](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=2572s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حالا به خود اردک برمی‌گردیم. **مدل زبانی بزرگ** (`large language model`) همان چیزی است که اردک و ChatGPT روی آن ساخته شده‌اند. این بخش نشان می‌دهد این مدل‌ها، در سطح ایده، چه کار می‌کنند و چرا گاهی اشتباه می‌کنند.

## مدل‌های زبانی بزرگ

- مدل‌های زبانی بزرگ (LLM) مدل‌هایی عظیم‌اند که بر اساس حجم بسیار زیادی آموزش **پیش‌بینی** می‌کنند.
- تا همین چند سال پیش، هوش مصنوعی در کامل کردن و ساختن جمله خوب نبود. Google در سال ۲۰۱۷ مقاله‌ای منتشر کرد دربارهٔ اینکه چطور **توجه** (`attention`) این مدل‌ها را می‌توان به رابطهٔ میان واژه‌های مختلف جلب کرد.
- **ترنسفورمر از پیش آموزش‌دیدهٔ مولد** (`Generative Pre-trained Transformer`)، یا به‌اختصار GPT، روی رابطهٔ میان واژه‌ها آموزش می‌بیند.
- هوش مصنوعی واژه‌ها را به **بردارهای تعبیه** (`embeddings`) تبدیل می‌کند تا رابطهٔ میان آن‌ها را پیدا کند. با آموزش بسیار زیاد، یک شبکهٔ عصبی عظیم می‌تواند ارتباط میان واژه‌ها را پیش‌بینی کند؛ و نتیجه، توانایی هوش مصنوعی مولد در ساختن محتوا و حتی گفت‌وگو با کاربر است.
- از سخنرانی: مالان پاراگرافی دربارهٔ ایالت Massachusetts نشان داد که با «The state's capital is» تمام می‌شد. مدل باید بفهمد «state» به Massachusetts برمی‌گردد تا Boston را پیش‌بینی کند. در یکی از مدل‌ها، هر واژه، مثلاً Massachusetts، با ۱٬۵۳۶ عدد اعشاری نمایش داده می‌شود؛ در تصویر توجه، خط ضخیم‌تر یعنی رابطهٔ قوی‌تر.
- از سخنرانی: در نهایت، این مدل‌ها مدل‌هایی آماری‌اند که محتمل‌ترین واژهٔ بعدی را پیشنهاد می‌کنند.

## توهم

- گاهی LLMها **توهم** (`hallucinate`) می‌زنند و اطلاعات نادرست می‌دهند.
- از سخنرانی: حتی اردک خود CS50 هم خطاپذیر است، با اینکه تیم درس کد زیادی نوشته تا این خطاها کمتر شوند. گاهی منشأ خطا انسانی است که در اینترنت چیزی ساخته و مدل آن را معتبر فرض کرده، و گاهی فقط بدشانسی، به خاطر همان کمی کاوش تصادفی.

> [!TIP]
> **تألیفی: با پاسخ اردک چه کنی**
> پاسخ را مثل راهنمایی یک هم‌کلاسی خوب ببین، نه حکم نهایی: آن را با درس‌نامه، مستندات و اجرای کد خودت بسنج.

## جمع‌بندی

در این درس با بخشی از فناوری پشت CS50.ai آشنا شدی. به‌طور مشخص دربارهٔ این‌ها حرف زدیم:

- هوش مصنوعی مولد
- مهندسی پرامپت
- هوش مصنوعی
- درخت تصمیم
- مینی‌ماکس
- یادگیری ماشین
- یادگیری عمیق
- مدل‌های زبانی بزرگ

- از سخنرانی: مالان جلسه را با شعر «ماشین مشق‌شب» (`The Homework Machine`) از Shel Silverstein تمام کرد؛ ماشینی که سال‌ها پیش، به شکلی طنزآمیز، وضعیت امروز ما با این ماشین‌ها را پیش‌بینی کرده بود.
- درس‌نامه با جملهٔ «This was CS50!» تمام می‌شود، هرچند این جلسه پیش از هفته‌های ۸ تا ۱۰ قرار دارد (d194).

## پیوندها

- قبلی: [یادگیری عمیق و شبکه‌های عصبی](/kb/d/w71-n07)
- بعدی: [خلاصهٔ جلسه](/kb/d/w71-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
