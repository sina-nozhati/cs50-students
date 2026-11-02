---
id: w03-n11
type: note
title: مرتب‌سازی حبابی (Bubble Sort)
title_fa: مرتب‌سازی حبابی
title_en: Bubble Sort
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Bubble Sort
official_anchor: bubble-sort
source_url: https://cs50.harvard.edu/x/2026/notes/3/#bubble-sort
source_refs:
- src-notes-3#bubble-sort
- src-transcript-3
- src-short-bubble-sort
- src-section-3
- src-section-3-transcript
- src-visualizations-3
- src-srt-3
concept_ids:
- w03-c-bubble-sort
- w03-c-early-exit-no-swaps
prev: w03-n10
next: w03-n12
order: 11
video:
  youtube_id: 6Svu_ae5ebk
  start: '1:10:49'
  start_seconds: 4249
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=4249s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'called bubble sort'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مرتب‌سازی حبابی

> **منبع رسمی:** بخش «Bubble Sort» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#bubble-sort). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۱۰:۴۹ تا حدود ۱:۲۹:۲۱](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=4249s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

مرتب‌سازی انتخابی مدام جلو و عقب می‌رفت. شاید بهتر باشد فقط به **همسایه‌ها** نگاه کنیم. **مرتب‌سازی حبابی** (`bubble sort`) همین کار را می‌کند و یک ترفند کوچک دارد که بهترین حالتش را خیلی بهتر می‌کند.

## مرتب‌سازی حبابی

- مرتب‌سازی حبابی با جابه‌جایی پیاپی عضوها کار می‌کند تا عضوهای بزرگ‌تر مثل حباب به انتها «بالا بیایند».
- شبه‌کد مرتب‌سازی حبابی:

```text
Repeat n-1 times
    For i from 0 to n–2
        If numbers[i] and numbers[i+1] out of order
            Swap them
    If no swaps
        Quit
```

- هرچه آرایه را بیشتر مرتب می‌کنیم، بخش بیشتری از آن مرتب می‌شود؛ پس فقط لازم است جفت‌هایی را نگاه کنیم که هنوز مرتب نشده‌اند.

> [!NOTE]
> **نکته**
> حلقهٔ درونی تا `n–2` می‌رود چون هر بار `numbers[i]` را با `numbers[i+1]` مقایسه می‌کند. اگر `i` تا `n-1` برود، `numbers[i+1]` بیرون از آرایه است. **از جلسهٔ حل تمرین:** Kelly همین را گفت: اگر تا `n - 1` بروی، با مقداری مقایسه می‌کنی که وجود ندارد.

## تحلیل

درس‌نامه حبابی را این‌طور تحلیل می‌کند:

- `(n - 1) × (n - 1)`
- `n² - n - n + 1`
- `n² - 2n + 1`
- یا ساده‌تر، `O(n²)`.

- در بدترین حالت یا کران بالا، مرتب‌سازی حبابی از مرتبهٔ `O(n²)` است. در بهترین حالت یا کران پایین از مرتبهٔ `Ω(n)`.
- می‌توانی مقایسهٔ این الگوریتم‌ها را [تصویرسازی‌شده](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html) ببینی.

> [!IMPORTANT]
> **مهم**
> `Ω(n)` فقط به لطف خط `If no swaps / Quit` به دست می‌آید. اگر آرایه از قبل مرتب باشد، در اولین گذر هیچ جابه‌جایی رخ نمی‌دهد و الگوریتم بعد از حدود `n` مقایسه می‌ایستد. بدون این خط، حبابی هم مثل انتخابی همیشه `n²` کار می‌کرد.

## سخنرانی و ویدئوی کوتاه چه می‌گویند

- **از سخنرانی:** با همان هشت داوطلب، David ۷ و ۲ را مقایسه و جابه‌جا کرد، بعد ۷ و ۵ و همین‌طور تا آخر. Precious، صاحب عدد ۷، «حباب‌وار» تا انتهای صف رفت و یکی از هشت مسئله حل شد.
- **از ویدئوی کوتاه Bubble Sort:** Doug Lloyd یک **شمارندهٔ جابه‌جایی** (`swap counter`) نگه می‌دارد و تا وقتی صفر نشده، تکرار می‌کند؛ همان ایدهٔ «اگر جابه‌جایی نبود، تمام».

## اشتباه‌های رایج

- حلقهٔ درونی تا `n-1` و خواندن `numbers[n]` که بیرون از آرایه است.
- حذف شرط توقف و از دست دادن `Ω(n)`.
- جابه‌جایی بدون متغیر موقت: `a = b; b = a;` هر دو را برابر می‌کند.

## جمع‌بندی

- حبابی جفت‌های کنار هم را مقایسه و در صورت لزوم جابه‌جا می‌کند.
- `O(n²)` در بدترین حالت، اما `Ω(n)` در بهترین حالت.

## پیوندها

- قبلی: [مرتب‌سازی و مرتب‌سازی انتخابی](/kb/d/w03-n10)
- بعدی: [بازگشت: حالت پایه و حالت بازگشتی](/kb/d/w03-n12)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
