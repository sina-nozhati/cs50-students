---
id: w03-n04
type: note
title: 'زمان اجرا و نماد O بزرگ (Running Time: big O)'
title_fa: زمان اجرا و نماد O بزرگ
title_en: 'Running Time: big O'
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Running Time
official_anchor: running-time
source_url: https://cs50.harvard.edu/x/2026/notes/3/#running-time
source_refs:
- src-notes-3#running-time
- src-transcript-3
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-big-o
- w03-c-common-running-times
- w03-c-drop-constants
- w03-c-time-command
prev: w03-n03
next: w03-n05
order: 4
video:
  youtube_id: 6Svu_ae5ebk
  start: '27:01'
  start_seconds: 1621
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=1621s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'running time'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# زمان اجرا و نماد O بزرگ

> **منبع رسمی:** بخش «Running Time» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#running-time). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۷:۰۱ تا حدود ۳۵:۵۳](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=1621s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

«برنامهٔ من در ۲ ثانیه اجرا شد» جملهٔ مفیدی نیست؛ روی کامپیوتر دیگر شاید ۲۰ ثانیه طول بکشد. دانشمندان کامپیوتر به‌جای ثانیه، **شکل رشد** را می‌سنجند. ابزارش **نماد O بزرگ** (`big O notation`) است و از این هفته تا آخر دوره همراه‌مان است.

## زمان اجرا

- می‌توانی بسنجی یک الگوریتم برای حل مسئله چقدر زمان می‌برد.
- **زمان اجرا** (`running time`) با تحلیلی به نام **نماد O بزرگ** بیان می‌شود. همان نمودار سه منحنی این بار با برچسب‌های `O(n)`، `O(n/2)` و `O(log₂ n)` رسم شده است (SVG درون‌خطی در [درس‌نامهٔ رسمی](https://cs50.harvard.edu/x/2026/notes/3/#running-time)).
- دانشمندان کامپیوتر به‌جای دقت فوق‌العادهٔ ریاضی، کارایی را بر حسب **مرتبهٔ** (`the order of`) زمان‌های اجرا بیان می‌کنند.

## ثابت‌ها حذف می‌شوند

- الگوریتم اول `O(n)` است، یعنی «از مرتبهٔ n».
- دومی **هم** `O(n)` است، چون در O بزرگ **ثابت‌ها حذف می‌شوند**.
- سومی `O(log n)` است.

> [!IMPORTANT]
> **مهم**
> این **شکل منحنی** است که کارایی الگوریتم را نشان می‌دهد، نه عدد دقیق گام‌ها. `n/2` گام برای `n` بزرگ همان شکلِ `n` را دارد.

## زمان‌های اجرای رایج

از کندترین به سریع‌ترین، همان‌طور که درس‌نامه فهرست می‌کند:

| زمان اجرا | خوانش فارسی (تألیفی) | نمونه از این هفته |
| --- | --- | --- |
| `O(n²)` | مربعی | مرتب‌سازی انتخابی و حبابی |
| `O(n log n)` | n در لگاریتم n | مرتب‌سازی ادغامی |
| `O(n)` | خطی | جست‌وجوی خطی |
| `O(log n)` | لگاریتمی | جست‌وجوی دودویی |
| `O(1)` | ثابت | یک گام، مستقل از اندازهٔ ورودی |

- از میان این‌ها `O(n²)` کندترین و `O(1)` سریع‌ترین است.
- جست‌وجوی خطی `O(n)` بود، چون در **بدترین حالت** ممکن است `n` گام لازم داشته باشد.
- جست‌وجوی دودویی `O(log n)` بود، چون حتی در بدترین حالت گام‌های کمتر و کمتری لازم دارد.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David گفت O بزرگ در اصل فقط یک **کران بالا** است، اما فکر کردن به آن در قالب **بدترین حالت** مفید است؛ مثل Jose که ۵۰ را در آخرین قفسه پیدا کرد.
- **از سخنرانی:** آیا گاهی جست‌وجوی خطی بهتر است؟ بله. اگر فقط **یک بار** قرار است بگردی، شاید مرتب کردن داده ارزشش را نداشته باشد. اما گوگل بارها و بارها جست‌وجو می‌کند، پس هزینهٔ مرتب‌سازی میان جست‌وجوهای زیاد سرشکن می‌شود.
- **از سخنرانی:** David تعریف کرد در دورهٔ تحصیلات تکمیلی گاهی کد بد اما درست می‌نوشت، هفت ساعت می‌خوابید و صبح جواب را می‌گرفت؛ مگر اینکه باگی داشت و کل شب هدر می‌رفت. تصمیم گرانِ آگاهانه گاهی عاقلانه است، اما ناآگاهانه هرگز.

> [!TIP]
> **راهنما**
> وقتی دنبال O بزرگ یک الگوریتم هستی، از خودت بپرس: «اگر ورودی دو برابر شود، کار چند برابر می‌شود؟» دو برابر یعنی `O(n)`؛ چهار برابر یعنی `O(n²)`؛ فقط یک گام بیشتر یعنی `O(log n)`.

## اشتباه‌های رایج

- نوشتن `O(n/2)` یا `O(2n)` به‌عنوان جواب نهایی؛ ثابت‌ها حذف می‌شوند و هر دو `O(n)` هستند.
- یکی دانستن «سریع روی دادهٔ کوچک» با «کارا».
- فراموش کردن اینکه `O(log n)` جست‌وجوی دودویی فقط روی دادهٔ مرتب صادق است.

## جمع‌بندی

- O بزرگ شکل رشد زمان اجرا را بیان می‌کند و ثابت‌ها را کنار می‌گذارد.
- ترتیب را حفظ کن: `O(n²)`، `O(n log n)`، `O(n)`، `O(log n)`، `O(1)`.

## پیوندها

- قبلی: [جست‌وجوی دودویی](/kb/d/w03-n03)
- بعدی: [امگا و تتا: کران پایین و کران دقیق](/kb/d/w03-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
