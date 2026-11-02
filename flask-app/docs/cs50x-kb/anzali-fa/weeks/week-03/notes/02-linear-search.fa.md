---
id: w03-n02
type: note
title: جست‌وجوی خطی و قفسه‌ها (Linear Search)
title_fa: جست‌وجوی خطی و قفسه‌ها
title_en: Linear Search
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Linear Search
official_anchor: linear-search
source_url: https://cs50.harvard.edu/x/2026/notes/3/#linear-search
source_refs:
- src-notes-3#linear-search
- src-transcript-3
- src-srt-3
concept_ids:
- w03-c-array-memory-lockers
- w03-c-linear-search
- w03-c-pseudocode-precision
prev: w03-n01
next: w03-n03
order: 2
video:
  youtube_id: 6Svu_ae5ebk
  start: '12:52'
  start_seconds: 772
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=772s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'lockers'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# جست‌وجوی خطی و قفسه‌ها

> **منبع رسمی:** بخش «Linear Search» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#linear-search). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۲:۵۲ تا حدود ۱۴:۴۹](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=772s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

جست‌وجو (`searching`) یکی از پرتکرارترین کارهای هر برنامه است: آیا این کاربر وجود دارد؟ این کلمه در فرهنگ لغت هست؟ ساده‌ترین راه را **جست‌وجوی خطی** (`linear search`) می‌نامیم و پایهٔ مقایسهٔ همهٔ الگوریتم‌های بعدی است.

## آرایه مثل ردیفی از قفسه‌ها

- یادت هست که هفتهٔ پیش **آرایه** (`array`) را دیدیم: بلوک‌هایی از حافظه که پشت‌سرهم و کنار هم قرار دارند.
- درس‌نامه آرایه را مثل **هفت قفسهٔ قرمز** تصور می‌کند که از `[0]` تا `[6]` شماره خورده‌اند. این جدول در صفحهٔ رسمی به‌صورت جدول HTML آمده است ([درس‌نامهٔ رسمی](https://cs50.harvard.edu/x/2026/notes/3/#linear-search)).
- خانهٔ سمت چپ **مکان ۰** (`location 0`) یا **ابتدای آرایه** است و خانهٔ سمت راست **مکان ۶** یا **انتهای آرایه**.

> [!IMPORTANT]
> **مهم**
> کامپیوتر دید پرنده ندارد. برای دانستن محتوای یک قفسه باید **به آن برود و درش را باز کند**. پس هر بار فقط یک مقدار را می‌بیند.

## مسئله: آیا ۵۰ در آرایه هست؟

- مسئلهٔ اصلی این است: «آیا عدد `50` داخل آرایه هست؟» کامپیوتر باید قفسه‌ها را یکی‌یکی نگاه کند. به فرایند پیدا کردن یک عدد، نویسه، رشته یا هر چیز دیگر **جست‌وجو** می‌گوییم.
- آرایه را به الگوریتم می‌دهیم و الگوریتم مقدار `true` یا `false` برمی‌گرداند.

دستورهایی که می‌توانیم به الگوریتم بدهیم، به زبان **شبه‌کد** (`pseudocode`)، یعنی نسخه‌ای خوانا برای انسان:

```text
For each door from left to right
    If 50 is behind door
        Return true
Return false
```

یک دانشمند کامپیوتر همین شبه‌کد را این‌طور ترجمه می‌کند:

```text
For i from 0 to n-1
    If 50 is behind doors[i]
        Return true
Return false
```

- این هنوز کد نیست، اما تقریب خیلی نزدیکی است به اینکه کد نهایی چه شکلی خواهد داشت.
- `doors[i]` همان اندیس‌گذاری هفتهٔ ۲ است و `n` تعداد قفسه‌هاست؛ پس آخرین اندیس `n-1` است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** داوطلبی به نام Jose قفسه‌های پر از پول Monopoly را از چپ به راست یکی‌یکی باز کرد و اسکناس ۵۰ دلاری در آخرین قفسه بود. David با خنده گفت او از اول «برای شکست چیده شده بود».
- **از سخنرانی:** اگر از راست شروع می‌کرد، شاید در یک گام پیدا می‌کرد، اما این تغییری بنیادی در الگوریتم نیست؛ وقتی هیچ چیز از ترتیب داده‌ها نمی‌دانی، بهترین کار رفتن خطی و پیوسته است.
- **از سخنرانی:** پریدن تصادفی بین قفسه‌ها هم کمکی نمی‌کند و تازه باید به خاطر بسپاری کدام درها را باز کرده‌ای.

> [!WARNING]
> **هشدار**
> `Return false` **بیرون** از حلقه است. **از سخنرانی:** David نسخه‌ای غلط با `Else` نشان داد که بلافاصله بعد از اولین در `Return false` می‌کرد؛ با هر `return` کار تابع تمام می‌شود، پس شش قفسهٔ دیگر هرگز دیده نمی‌شدند. تورفتگی در شبه‌کد عمدی است. این باگ را در چالش‌های این هفته شکار می‌کنیم.

## اشتباه‌های رایج

- شمردن قفسه‌ها از ۱ به‌جای ۰؛ قفسهٔ «مکان ۶» یعنی دست‌کم هفت قفسه وجود دارد.
- برگرداندن `false` پیش از دیدن همهٔ قفسه‌ها.

## جمع‌بندی

- جست‌وجوی خطی همه‌چیز را از ابتدا تا انتها یکی‌یکی نگاه می‌کند.
- روی هر آرایه‌ای کار می‌کند، چه مرتب باشد چه نه.

## پیوندها

- قبلی: [خوش آمدید: الگوریتم‌ها و رشد زمان اجرا](/kb/d/w03-n01)
- بعدی: [جست‌وجوی دودویی](/kb/d/w03-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
