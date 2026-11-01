---
id: w05-n12
type: note
title: ترای (Trie) (Tries)
title_fa: ترای (Trie)
title_en: Tries
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Tries
official_anchor: tries
source_url: https://cs50.harvard.edu/x/2026/notes/5/#tries
source_refs:
- src-notes-5#tries
- src-transcript-5
- src-short-structures
- src-short-tries
- src-short-data-structures
- src-pset-5
- src-srt-5
concept_ids:
- w05-c-trie
- w05-c-trie-lookup
- w05-c-trie-memory
prev: w05-n11
next: w05-summary
order: 12
video:
  youtube_id: PmAI76OGE_E
  start: '1:53:48'
  start_seconds: 6828
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=6828s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'There are tries in the world'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# ترای (Trie)

> **منبع رسمی:** بخش «Tries» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#tries). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۳:۴۸](https://www.youtube.com/watch?v=PmAI76OGE_E&t=6828s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

ترای (trie) تنها ساختار این هفته است که جست‌وجوی آن به تعداد عضوها بستگی ندارد. اما بهایش را با حافظه می‌پردازی؛ و همین بده‌بستان پایان داستان این هفته است.

## ترای‌ها

- **ترای‌ها** (tries) شکل دیگری از ساختمان داده‌اند. ترای **درختی از آرایه‌ها**ست.
- درس‌نامه می‌گوید ترای‌ها همیشه در زمان ثابت جست‌وجوپذیرند.
- یکی از عیب‌های ترای این است که حافظهٔ زیادی می‌گیرد. درس‌نامه برای ذخیرهٔ *Toad* عدد «26 × 4 = 104 گره» را می‌آورد.
- *Toad* حرف به حرف ذخیره می‌شود: `T` در یک آرایه، `O` در آرایهٔ بعدی و همین‌طور تا آخر.
- *Tom* سپس به همین شکل ذخیره می‌شود و با *Toad* دو حرف مشترک `T` و `O` را شریک است.
- این ساختار زمان جست‌وجوی O(1) دارد.
- عیب این ساختار مقدار منابعی است که برای استفاده از آن لازم است.

> [!WARNING]
> **هشدار**
> «26 × 4 = 104» تعداد **اشاره‌گرها**ست، نه گره‌ها. در سخنرانی گفته شد ترای پس از درج *Toad* چهار گره دارد که هر کدام آرایه‌ای ۲۶تایی است؛ پس ۴ گره و ۱۰۴ اشاره‌گر. همچنین «همیشه زمان ثابت» به این معناست که زمان به تعداد واژه‌های ذخیره‌شده بستگی ندارد؛ زمان همچنان با **طول واژه** رشد می‌کند، که سقف دارد. هر دو مورد در `sources.json` ثبت شده‌اند.

> [!NOTE]
> **یادداشت**
> بخش «Summing Up» درس‌نامه درخت‌ها را در فهرست موضوع‌ها نیاورده، هرچند این هفته آن‌ها را دیدی. این مورد هم ثبت شده است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت نام trie از واژهٔ *retrieval* (بازیابی) آمده است.
- **از سخنرانی:** پایان یک نام با یک مقدار بولی نشانه‌گذاری می‌شود (در تصویر سبز). واژه صریحاً ذخیره نمی‌شود؛ وجودش از اشاره‌گرهای غیر `NULL` در مسیر و پرچم پایان معلوم است. برای همین *Toad* و *Toadette* که یکی پیشوند دیگری است، هر دو جا می‌شوند.
- **از سخنرانی:** برای جست‌وجوی *Toad* چهار گام لازم است، چه ترای سه نام داشته باشد چه سه میلیون؛ و چون طول نام‌ها سقف معقولی دارد، این عملاً زمان ثابت است.
- **از سخنرانی:** گره ترای را آرایه‌ای ۲۶تایی به اسم `children` از اشاره‌گرهای `struct node *` به همراه یک داده (مثلاً شمارهٔ تلفن) توصیف کرد.
- **از سخنرانی:** او گفت در پرابلم‌ست ۵ ترای پیاده **نمی‌کنی**، جدول درهم‌سازی پیاده می‌کنی، و دلیلش حافظه است: بیشتر اشاره‌گرهای آرایه‌های ترای `NULL` و بی‌استفاده می‌مانند.
- **از سخنرانی:** نمونهٔ جهان واقعی: رستوران Sweetgreen سالادهای سفارشی را در قفسه‌هایی با برچسب `A–E`، `F–J`، `K–N` و `O–Z` می‌گذارد؛ یک جدول درهم‌سازی واقعی. پیش‌تر برای هر حرف یک قفسه داشتند، اما قفسه‌های پرکاربرد سرریز می‌شدند و `Q` و `Z` خالی می‌ماندند.
- **از سخنرانی:** آخرین کار این هفته نوشتن یک غلط‌یاب املایی است: پرونده‌ای بزرگ با بیش از ۱۰۰ هزار واژهٔ انگلیسی را باید کارآمد در حافظه بارگذاری کنی و ابزارهایی سرعت و حافظهٔ کدت را می‌سنجند.

ویدئوی کوتاه [Tries](/kb/d/w05-sh-tries) ترای را با نمونه‌ای دیگر نشان می‌دهد و [Data Structures](/kb/d/w05-sh-data-structures) همهٔ ساختارهای این هفته را مقایسه می‌کند. تمرین اختیاری [Trie](/kb/d/w05-pr-trie) فرصتی برای کار با یک ترای واقعی است.

## اشتباه‌های رایج

- یکی گرفتن «گره» و «اشاره‌گر» در شمارش حافظهٔ ترای.
- فکر کردن به اینکه ترای واژه را به‌صورت رشته ذخیره می‌کند.
- فراموش کردن پرچم پایان واژه؛ بدون آن `Toad` و `Toadette` از هم جدا نمی‌شوند.

## جمع‌بندی

- ترای درختی از آرایه‌هاست؛ هر سطح یک حرف از واژه.
- جست‌وجو به تعداد واژه‌ها بستگی ندارد، فقط به طول واژه.
- بهایش حافظه است: بیشتر اشاره‌گرها `NULL`اند.
- این هفته: آرایه، فهرست پیوندی، درخت، جدول درهم‌سازی و ترای؛ هر کدام با بده‌بستان خودش میان زمان و فضا.

## پیوندها

- قبلی: [درهم‌سازی و جدول درهم‌سازی](/kb/d/w05-n11)
- بعدی: [خلاصهٔ هفته](/kb/d/w05-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
