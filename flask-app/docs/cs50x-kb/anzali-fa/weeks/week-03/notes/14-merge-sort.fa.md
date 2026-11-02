---
id: w03-n14
type: note
title: مرتب‌سازی ادغامی (Merge Sort)
title_fa: مرتب‌سازی ادغامی
title_en: Merge Sort
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Merge Sort
official_anchor: merge-sort
source_url: https://cs50.harvard.edu/x/2026/notes/3/#merge-sort
source_refs:
- src-notes-3#merge-sort
- src-short-merge-sort
- src-section-3
- src-section-3-transcript
- src-visualizations-3
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-merge-sort
- w03-c-merging
- w03-c-n-log-n
prev: w03-n13
next: w03-summary
order: 14
video:
  youtube_id: 6Svu_ae5ebk
  start: '1:46:09'
  start_seconds: 6369
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=6369s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'pseudo code for merge sort'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مرتب‌سازی ادغامی

> **منبع رسمی:** بخش «Merge Sort» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#merge-sort). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۶:۰۹](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=6369s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حالا که بازگشت را بلدی، می‌توانی الگوریتمی بفهمی که از `O(n²)` بهتر است: **مرتب‌سازی ادغامی** (`merge sort`). شبه‌کدش فقط چند خط است، اما هر خطش یک دنیا کار انجام می‌دهد.

## شبه‌کد

- اکنون می‌توانیم در جست‌وجوی مرتب‌سازی کاراتر از بازگشت بهره بگیریم و الگوریتمی به نام **مرتب‌سازی ادغامی** پیاده کنیم، یک الگوریتم مرتب‌سازی بسیار کارا.
- شبه‌کد مرتب‌سازی ادغامی خیلی کوتاه است:

```text
If only one number
    Quit
Else
    Sort left half of numbers
    Sort right half of numbers
    Merge sorted halves
```

## گام‌به‌گام با ۶۳۴۱

این فهرست عددها را در نظر بگیر:

```text
6341
```

- **اول**، مرتب‌سازی ادغامی می‌پرسد: «آیا این یک عدد است؟» جواب «نه» است، پس ادامه می‌دهد.

```text
6341
```

- **دوم**، عددها را از وسط (یا تا جای ممکن نزدیک به وسط) نصف می‌کند و نیمهٔ چپ را مرتب می‌کند.

```text
63|41
```

- **سوم**، به عددهای سمت چپ نگاه می‌کند و می‌پرسد: «آیا این یک عدد است؟» چون نه، عددهای سمت چپ را از وسط نصف می‌کند.

```text
6|3
```

- **چهارم**، باز می‌پرسد: «آیا این یک عدد است؟» این بار جواب بله است! پس این کار را تمام می‌کند و به آخرین کاری که در حال اجرایش بود برمی‌گردد:

```text
63|41
```

- **پنجم**، عددهای سمت چپ را مرتب (ادغام) می‌کند.

```text
36|41
```

- حالا به همان جای شبه‌کد برمی‌گردیم که نیمهٔ چپ مرتب شده است. فرایندی مشابه گام‌های ۳ تا ۵ برای عددهای سمت راست رخ می‌دهد و نتیجه می‌شود:

```text
36|14
```

- هر دو نیمه مرتب‌اند. در پایان، الگوریتم دو طرف را **ادغام** می‌کند: به اولین عدد سمت چپ و اولین عدد سمت راست نگاه می‌کند، کوچک‌تر را اول می‌گذارد، بعد دومین کوچک‌تر را، و همین را برای همهٔ عددها تکرار می‌کند تا به این برسد:

```text
1346
```

- مرتب‌سازی ادغامی تمام شد و برنامه پایان می‌یابد.

> [!NOTE]
> **نکته**
> در صفحهٔ رسمی بلوک «6341» و «63|41» هر کدام دو بار آمده‌اند: یک بار پیش و یک بار پس از پرسش «آیا این یک عدد است؟». این تکرار در منبع است و این‌جا عیناً حفظ شده است.

## زمان اجرا

- مرتب‌سازی ادغامی الگوریتمی بسیار کاراست با بدترین حالت `O(n log n)`.
- بهترین حالت هم `Ω(n log n)` است، چون الگوریتم باز هم باید به هر جای فهرست سر بزند.
- بنابراین مرتب‌سازی ادغامی `Θ(n log n)` هم هست، چون بهترین و بدترین حالتش یکی است.
- یک [تصویرسازی نهایی](https://www.youtube.com/watch?v=ZZuD6iUe3Pc) هم در کلاس نشان داده شد.

> [!TIP]
> **راهنما**
> **از جلسهٔ حل تمرین:** یک راه فهمیدن `n log n`: فهرست را آن‌قدر نصف می‌کنی تا به فهرست‌های تک‌عضوی برسی؛ تعداد این نصف کردن‌ها `log n` است (برای ۸ عضو، ۳ بار). در هر سطح، ادغام کردن حدود `n` کار می‌برد. پس `n` ضرب در `log n`.

> [!WARNING]
> **هشدار**
> **از ویدئوی کوتاه Merge Sort:** سرعت ادغامی رایگان نیست. Doug Lloyd یادآوری می‌کند که برای ساختن زیرآرایه‌های ادغام‌شده احتمالاً **حافظهٔ بیشتری** لازم است. روی آرایهٔ از قبل مرتب، حبابی با `Ω(n)` حتی ممکن است سریع‌تر باشد.

## اشتباه‌های رایج

- فکر کردن به اینکه ادغامی در بهترین حالت `Ω(n)` است. نه؛ همیشه نصف و ادغام می‌کند.
- فراموش کردن حالت پایه «اگر فقط یک عدد بود، تمام».
- در ادغام، فراموش کردن عضوهای باقی‌ماندهٔ یک نیمه وقتی نیمهٔ دیگر خالی شده است.

## جمع‌بندی

- ادغامی: نیمهٔ چپ را مرتب کن، نیمهٔ راست را مرتب کن، دو نیمه را ادغام کن.
- `O(n log n)`، `Ω(n log n)` و در نتیجه `Θ(n log n)`؛ سریع‌تر از `O(n²)` برای ورودی‌های بزرگ.

## پیوندها

- قبلی: [هرم ماریو: تکرار در برابر بازگشت](/kb/d/w03-n13)
- بعدی: [خلاصهٔ هفته](/kb/d/w03-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
