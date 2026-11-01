---
id: w02-n05
type: note
title: 'debug50، نقطهٔ توقف و اردک پلاستیکی (Debugging: debug50 and the duck)'
title_fa: debug50، نقطهٔ توقف و اردک پلاستیکی
title_en: 'Debugging: debug50 and the duck'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Debugging
official_anchor: debugging
source_url: https://cs50.harvard.edu/x/2026/notes/2/#debugging
source_refs:
- src-notes-2#debugging
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-debugger
- w02-c-breakpoint
- w02-c-step-over-into
- w02-c-rubber-duck
prev: w02-n04
next: w02-n06
order: 5
video:
  youtube_id: h5Gc1n8ZuU8
  start: '26:08'
  start_seconds: 1568
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=1568s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'debug 50'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# debug50، نقطهٔ توقف و اردک پلاستیکی

> **منبع رسمی:** بخش «Debugging» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#debugging). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۶:۰۸ تا حدود ۴۱:۵۷](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=1568s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

`printf` خوب است، اما وقتی کد بزرگ می‌شود، باید جای‌جای آن چاپ بگذاری و دوباره کامپایل کنی. **دیباگر** (`debugger`) ابزاری است که برنامه‌نویسان ساخته‌اند تا باگ را ردیابی کنند: برنامه را وسط کار نگه می‌دارد تا خط‌به‌خط ببینی چه می‌گذرد.

## debug50 در VS Code

- در VS Code یک دیباگر از پیش پیکربندی‌شده به نام `debug50` در اختیارت است.
- **گام ۱: نقطهٔ توقف** (`breakpoint`). کنار شمارهٔ یک خط، سمت چپ، کلیک کن. نقطهٔ قرمزی ظاهر می‌شود. درس‌نامه آن را مثل **تابلوی ایست** می‌داند که از دیباگر می‌خواهد همان‌جا مکث کند.
- **گام ۲:** `debug50 ./buggy` را اجرا کن. دیباگر بالا می‌آید و یک خط کد با رنگ طلایی روشن می‌شود؛ برنامه همان‌جا **متوقف** است.
- بالا سمت چپ همهٔ **متغیرهای محلی** نمایش داده می‌شوند، از جمله `h` که هنوز مقداری ندارد.
- دکمهٔ **Step Over** بالای پنجره اجرا را خط‌به‌خط جلو می‌برد. می‌بینی مقدار `i` با هر دور حلقه زیاد می‌شود.
- دیباگر به تو **نمی‌گوید** باگ کجاست؛ کمک می‌کند آرام شوی و اجرای کد را گام‌به‌گام ببینی.
- با **Step Into** می‌توانی وارد جزئیات یک تابع، مثلاً `print_column`، شوی.

> **منبع رسمی:** تصویر نقطهٔ توقف در درس‌نامه: [cs50Week2Debugging.png](https://cs50.harvard.edu/x/notes/2/cs50Week2Debugging.png) (فقط پیوند).

## اردک پلاستیکی و CS50 Duck

- روش سوم: مشکل و گام‌هایی را که برای حلش برداشته‌ای **بلند** برای یک **اردک پلاستیکی** (`rubber duck`)، یک شیء بی‌جان یا یک آدم توضیح بده. اغلب وسط توضیح خودت اشتباه را پیدا می‌کنی.
- و در پایان، **CS50 Duck** (روی [CS50.ai](https://cs50.ai) و داخل VS Code) هم در اشکال‌زدایی کمکت می‌کند.

> **توجه:** در متن رسمی درس‌نامه جملهٔ «Finally, , also known as the CS50 Duck» یک نام پیوند جاافتاده دارد. بخش‌های پیشین همان درس‌نامه CS50 Duck و CS50.ai را با هم نام می‌برند (ناهمخوانی d21).

## چهار روش

> **تألیفی:** جمع‌بندی درس‌نامه از «چهار روش» اشکال‌زدایی نام می‌برد. فهرست زیر برداشت ما از متن همین بخش است.

| روش | کی به کار می‌آید |
| --- | --- |
| خواندن پیام خطای کامپایلر | کد کامپایل نمی‌شود |
| `printf` | می‌خواهی مقدار یک متغیر را سریع ببینی |
| `debug50` | می‌خواهی اجرای کد را خط‌به‌خط و درون تابع‌ها دنبال کنی |
| اردک پلاستیکی و CS50 Duck | نمی‌دانی از کجا شروع کنی |

## اشتباه‌های رایج

- اجرای `debug50` بدون گذاشتن نقطهٔ توقف؛ برنامه بی‌توقف تا پایان می‌رود.
- زدن Step Over روی تابعی که باگ داخل آن است. برای دیدن درون تابع، Step Into بزن.
- اجرای `debug50 buggy` بدون `./`.

## جمع‌بندی

- نقطهٔ توقف بگذار، `debug50 ./program` بزن، با Step Over و Step Into جلو برو و متغیرها را تماشا کن.
- اردک را دست‌کم نگیر: توضیح بلند مسئله خودش روش اشکال‌زدایی است.

## پیوندها

- قبلی: [اشکال‌زدایی با printf](/kb/d/w02-n04)
- بعدی: [کامپایل: make و clang](/kb/d/w02-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
