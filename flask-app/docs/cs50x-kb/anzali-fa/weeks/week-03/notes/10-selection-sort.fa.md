---
id: w03-n10
type: note
title: مرتب‌سازی و مرتب‌سازی انتخابی (Sorting and Selection Sort)
title_fa: مرتب‌سازی و مرتب‌سازی انتخابی
title_en: Sorting and Selection Sort
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Sorting and Selection Sort
official_anchor: sorting-and-selection-sort
source_url: https://cs50.harvard.edu/x/2026/notes/3/#sorting-and-selection-sort
source_refs:
- src-notes-3#sorting-and-selection-sort
- src-transcript-3
- src-visualizations-3
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-sorting
- w03-c-selection-sort
- w03-c-swap
- w03-c-counting-steps
prev: w03-n09
next: w03-n11
order: 10
video:
  youtube_id: 6Svu_ae5ebk
  start: '1:03:20'
  start_seconds: 3800
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=3800s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'sorting numbers'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مرتب‌سازی و مرتب‌سازی انتخابی

> **منبع رسمی:** بخش «Sorting and Selection Sort» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#sorting-and-selection-sort). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۰۳:۲۰ تا حدود ۱:۱۰:۴۹](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=3800s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

جست‌وجوی دودویی سریع بود، به شرط آنکه داده **مرتب** باشد. اما مرتب کردن خودش هزینه دارد. این‌جا اولین الگوریتم مرتب‌سازی را می‌بینیم و یاد می‌گیریم هزینه‌اش را بشماریم.

## مرتب‌سازی

- **مرتب‌سازی** (`sorting`) یعنی گرفتن فهرستی نامرتب از مقدارها و تبدیل آن به فهرستی مرتب.
- وقتی فهرست مرتب است، جست‌وجو در آن برای کامپیوتر خیلی کم‌هزینه‌تر است. یادت باشد جست‌وجوی دودویی روی فهرست مرتب کار می‌کند، نه نامرتب.
- الگوریتم‌های مرتب‌سازی گوناگونی وجود دارد و **مرتب‌سازی انتخابی** (`selection sort`) یکی از آن‌هاست.

## مرتب‌سازی انتخابی

درس‌نامه آرایه را با خانه‌های `[0]`، `[1]`، `[2]`، `[...]` تا `[n-3]`، `[n-2]` و `[n-1]` نشان می‌دهد (جدول HTML در [درس‌نامهٔ رسمی](https://cs50.harvard.edu/x/2026/notes/3/#sorting-and-selection-sort)). شبه‌کد الگوریتم:

```text
For i from 0 to n–1
    Find smallest number between numbers[i] and numbers[n-1]
    Swap smallest number with numbers[i]
```

- در هر دور، **کوچک‌ترین** عدد را در بخش مرتب‌نشده «انتخاب» می‌کنیم و با خانهٔ `numbers[i]` جابه‌جا می‌کنیم. اسم الگوریتم از همین‌جا آمده است.

## شمردن گام‌ها

- دور اول پیمایش فهرست `n - 1` گام می‌برد. دور دوم `n - 2` گام. اگر همین منطق را ادامه دهیم، گام‌های لازم این‌طور نمایش داده می‌شوند:

```text
(n - 1) + (n - 2) + (n - 3) + ... + 1
```

- این مجموع به `n(n-1)/2` ساده می‌شود، یا ساده‌تر، `O(n²)`.
- در بدترین حالت یا کران بالا، مرتب‌سازی انتخابی از مرتبهٔ `O(n²)` است. در بهترین حالت یا کران پایین هم از مرتبهٔ `Ω(n²)`.

> [!IMPORTANT]
> **مهم**
> چرا بهترین حالت هم `n²` است؟ چون الگوریتم **هیچ راهی ندارد** بفهمد آرایه از قبل مرتب است. باید باز هم همهٔ خانه‌های باقی‌مانده را بگردد تا مطمئن شود کوچک‌ترین را پیدا کرده است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** هشت داوطلب با عددهای ۷، ۲، ۵، ۴، ۱، ۶، ۰ و ۳ روی صحنه ایستادند. وقتی David گفت خودتان مرتب شوید، همه **موازی** و «ارگانیک» جابه‌جا شدند؛ درست بود، اما الگوریتمی به نظر نمی‌رسید.
- **از سخنرانی:** بعد David یکی‌یکی جلوی آن‌ها رفت، کوچک‌ترین عدد را **به خاطر سپرد** (اول ۷، بعد ۲، بعد ۱ و در آخر ۰) و صاحب ۰ را با نفر اول جابه‌جا کرد. چون جایی خالی در آرایه نیست، باید **جابه‌جا** کرد؛ نمی‌شود کسی را کنار زد و به حافظه‌ای که مال ما نیست دست زد.

> [!TIP]
> **راهنما**
> برای دیدن مقایسهٔ این الگوریتم‌ها، [تصویرسازی رسمی](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html) را باز کن و یک آرایهٔ کوچک را قدم‌به‌قدم ببین.

## اشتباه‌های رایج

- فکر کردن به اینکه اگر آرایه مرتب باشد، انتخابی زودتر تمام می‌شود. نه؛ `Ω(n²)`.
- اشتباه در حد حلقهٔ درونی: جست‌وجوی کوچک‌ترین باید از `numbers[i]` تا `numbers[n-1]` باشد، نه از ابتدای آرایه.

## جمع‌بندی

- مرتب‌سازی انتخابی در هر دور کوچک‌ترین مقدار بخش مرتب‌نشده را به جای درستش می‌برد.
- `O(n²)` و `Ω(n²)`، پس `Θ(n²)`.

## پیوندها

- قبلی: [ساختارها (struct): نوع دادهٔ خودت را بساز](/kb/d/w03-n09)
- بعدی: [مرتب‌سازی حبابی](/kb/d/w03-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
