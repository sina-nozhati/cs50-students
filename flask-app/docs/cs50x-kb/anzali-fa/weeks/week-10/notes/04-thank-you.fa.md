---
id: w10-n04
type: note
title: سپاس و جمع‌بندی (Thank You! and Summing Up)
title_fa: سپاس و جمع‌بندی
title_en: Thank You! and Summing Up
week: 10
parent: w10-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Thank You!
official_anchor: thank-you
source_url: https://cs50.harvard.edu/x/2026/notes/10/#thank-you
source_refs:
- src-notes-10#thank-you
- src-notes-10#summing-up
- src-transcript-10
- src-anzali-authored-10
- src-anzali-inference-10
- src-srt-10
concept_ids:
- w10-c-summing-up
- w10-c-review-quiz
prev: w10-n03
next: w10-summary
order: 4
video:
  youtube_id: ApQTgFkf8TU
  start: '38:40'
  start_seconds: 2320
  url: https://www.youtube.com/watch?v=ApQTgFkf8TU&t=2320s
  origin: inference
  basis: first lecture10.srt cue (after the previous note's cue) containing the phrase 'So a few thanks before'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:40:25+03:30'
verified_at: '2026-10-29T19:40:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official notes (which contain no code); transcript-only facts are marked «از سخنرانی»; authored material is marked تألیفی. All third-party links are copied from the official notes. Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# سپاس و جمع‌بندی

> **منبع رسمی:** بخش «Thank You!» از [درس‌نامهٔ هفتهٔ ۱۰ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/10/#thank-you). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۸:۴۰](https://www.youtube.com/watch?v=ApQTgFkf8TU&t=2320s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

پایان درس است: سپاس از کسانی که درس را ممکن کردند و سه توصیهٔ پایانی. سخنرانی با یک مسابقهٔ مرور تمام شد که پرسش‌هایش را خود دانشجویان نوشته بودند؛ مرور خوبی برای کل درس است.

## سپاس

- سپاس که در این درس شرکت کردی!
- افراد زیادی این درس را ممکن کردند؛ از همهٔ آن‌ها برای ممکن کردن درس و پشتیبانی خوبشان سپاسگزاریم.
- از سخنرانی: از تیم CS50، دستیاران آموزشی (TF و CA) و سازندگان **اردک CS50** هم نام برده شد.

## جمع‌بندی

در این درس به سفرت در طول درس فکر کردیم. به‌طور مشخص تشویقت می‌کنیم که…

- مهارت‌های برنامه‌نویسی‌ای را که در این درس آموختی برای حل مسئله‌های دنیا به کار ببری.
- مهارت‌های تازه‌ات را برداری و **یادگیری را ادامه بدهی**!
- قوی تمام کنی و پروژهٔ نهایی‌ات را ارسال کنی.
- [کواک!](https://youtu.be/DLzxrzFCyOs?si=PC0oK7Pv_NkO4FmX)

این CS50 بود!

## مسابقهٔ پایانی (مرور کل درس)

از سخنرانی: پرسش‌ها را دانشجویان برای مرور نوشته بودند. پاسخ درست و توضیح آن همان است که در سخنرانی گفته شد:

- **بزرگ‌ترین عدد ۸ بیتی بدون علامت:** ۲۵۵، نه ۲۵۶؛ چون شمارش از ۰ شروع می‌شود و ۰ یکی از ۲۵۶ حالت را می‌گیرد (هفتهٔ ۰).
- **مسئلهٔ سال ۲۰۳۸:** سرریز عدد صحیح؛ چون زمان با عدد صحیح ۳۲ بیتی از مبدأ ۱ ژانویهٔ ۱۹۷۰ شمرده می‌شود. بیشتر سخت‌افزارهای امروزی شمارندهٔ ۶۴ بیتی دارند (هفتهٔ ۱).
- **کدام گام کامپایل نیست؟** تفسیر (interpreting). گام‌ها: پیش‌پردازش (`#include` و مانند آن)، کامپایل به اسمبلی، اسمبل به کد ماشین، و پیوند (linking) با کتابخانه‌ها (هفتهٔ ۲).
- **اشاره‌گر چه چیزی نگه می‌دارد؟** نشانی یک مقدار در حافظه (هفتهٔ ۴).
- **زمان اجرای جست‌وجوی خطی:** O(n)؛ ممکن است Ω(1) باشد، اما بدترین حالت رسیدن به انتهای فهرست است (هفتهٔ ۳).
- **کدام ساختمان‌داده «اول وارد، اول خارج» (FIFO) است؟** صف؛ در مقابل، پشته LIFO است (هفتهٔ ۵).
- **کدام عملگر نشانی متغیر را برمی‌گرداند؟** `&`؛ و `*` در بیشتر جاها برعکس آن است: رفتن به یک نشانی (هفتهٔ ۴).
- **کدام فرمان SQL ردیف‌های تکراری نتیجه را حذف می‌کند؟** `DISTINCT`؛ `UNIQUE` هم کلیدواژهٔ SQL است اما برای تعریف یکتایی یک ستون در طرح‌واره (هفتهٔ ۷).
- **کد HTTP ‏418 یعنی چه؟** «I'm a teapot»، که از یک شوخی روز اول آوریل آمده است (هفتهٔ ۸).
- **malloc حافظه را از کجا می‌گیرد؟** از heap؛ stack برای قاب‌های فراخوانی توابع است (هفتهٔ ۴).
- **malloc بدون free چه مشکلی می‌سازد؟** نشت حافظه (memory leak) (هفتهٔ ۴).
- **safetyschool.org به کجا می‌رود؟** با پاسخ HTTP ‏301 به yale.edu (هفتهٔ ۸).
- **کار DNS چیست؟** ترجمهٔ نام دامنه به نشانی IP (هفتهٔ ۸).
- **کدام ابزار داخلی SQL برای شرایط رقابتی نیست؟** `ENROLL`؛ `BEGIN TRANSACTION`، `COMMIT` و `ROLLBACK` واقعاً ابزار SQL‌اند (هفتهٔ ۷).
- **مالان سخنرانی را با چه جمله‌ای شروع می‌کند؟** «All right, this is CS50».

> [!NOTE]
> **تألیفی: دربارهٔ «هفته»ها**
> شمارهٔ هفته‌ای که کنار هر پرسش آمده، برچسب تألیفی این بسته است تا بدانی برای مرور به کجا برگردی؛ در خود سخنرانی نیامده است.

## پیوندها

- قبلی: [نگاه به آینده: ابزارهای بعد از CS50](/kb/d/w10-n03)
- بعدی: [خلاصهٔ هفته](/kb/d/w10-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-10/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
