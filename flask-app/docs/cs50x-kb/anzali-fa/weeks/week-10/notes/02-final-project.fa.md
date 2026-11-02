---
id: w10-n02
type: note
title: پروژهٔ نهایی، هکاتون و نمایشگاه CS50 (Final Project)
title_fa: پروژهٔ نهایی، هکاتون و نمایشگاه CS50
title_en: Final Project
week: 10
parent: w10-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Final Project
official_anchor: final-project
source_url: https://cs50.harvard.edu/x/2026/notes/10/#final-project
source_refs:
- src-notes-10#final-project
- src-transcript-10
- src-project-10
- src-hackathon-10
- src-anzali-authored-10
- src-srt-10
concept_ids:
- w10-c-final-project
- w10-c-final-project-ai
- w10-c-good-better-best
- w10-c-hackathon-fair
prev: w10-n01
next: w10-n03
order: 2
video:
  youtube_id: ApQTgFkf8TU
  start: '18:31'
  start_seconds: 1111
  url: https://www.youtube.com/watch?v=ApQTgFkf8TU&t=1111s
  origin: inference
  basis: first lecture10.srt cue (after the previous note's cue) containing the phrase 'So with your final project'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:40:25+03:30'
verified_at: '2026-10-29T19:40:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official notes (which contain no code); transcript-only facts are marked «از سخنرانی»; authored material is marked تألیفی. All third-party links are copied from the official notes. Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# پروژهٔ نهایی، هکاتون و نمایشگاه CS50

> **منبع رسمی:** بخش «Final Project» از [درس‌نامهٔ هفتهٔ ۱۰ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/10/#final-project). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۸:۳۱ تا حدود ۳۰:۱۳](https://www.youtube.com/watch?v=ApQTgFkf8TU&t=1111s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا هر مسئله را تیم درس طراحی کرده بود. **پروژهٔ نهایی** نخستین پروژه‌ای است که مشخصات و طراحی‌اش با خود توست. این صفحه فقط آنچه درس‌نامه و سخنرانی دربارهٔ آن گفته‌اند را مرور می‌کند؛ مشخصات کامل در صفحهٔ رسمی پروژهٔ نهایی است.

## پروژهٔ نهایی

- پروژهٔ نهایی فرصتی است تا با همین مهارت‌ها پروژه‌ای بسازی که **مشخصات و طراحی آن با خودت** است.
- در [مشخصات پروژهٔ نهایی](https://cs50.harvard.edu/x/2026/project/) فرصت استفاده از **ابزارهای مبتنی بر هوش مصنوعی بیرون از ابزارهای خود درس** را می‌بینی؛ کاری که در هیچ مسئلهٔ دیگری مجاز نبود.
- از سخنرانی: تا حالا همهٔ مسئله‌ها را تیم درس نوشته بود و تو گام‌به‌گام دستورها را دنبال می‌کردی؛ پروژهٔ نهایی «چرخ‌های کمکی» را برمی‌دارد. می‌توانی از کد مسئله‌های قبلی (مثلاً مسئلهٔ ۹ برای کار وب) شروع کنی، یا از یک پنجرهٔ خالی، اما در نهایت باید کار **خودت** باشد.
- از سخنرانی: مشخصات از تو می‌خواهد سه هدف بگذاری: هدف **خوب** که در هر حال به آن می‌رسی، هدف **بهتر** که کمی بلندپروازانه است، و هدف **بهترین** که به گفتهٔ او در نرم‌افزار به‌ندرت پیش می‌آید؛ چون حتی برنامه‌نویسان باتجربه هم زمان لازم را کم تخمین می‌زنند.
- از سخنرانی: با هوش مصنوعی حالا انگار یک «همکار تازه‌کار» کنار توست که در رفع باگ، راهنمایی و حتی پیاده‌سازی بخشی از امکانات کمک می‌کند؛ کار تو این است که چیزی بسازی که برایت جالب است و مسئله‌ای واقعی را حل کند.

## هکاتون و نمایشگاه CS50

- امید است در [هکاتون CS50](https://cs50.harvard.edu/college/2025/fall/hackathon/) شرکت کنی؛ یک شب‌زنده‌داری حماسی که در آن همه با هم روی پروژه‌های نهایی کار می‌کنند.
- برای دانشجویان حاضر در دانشگاه، امید است در **نمایشگاه CS50** (CS50 Fair) شرکت کنند و پروژهٔ نهایی‌شان را به نمایش بگذارند.
- از سخنرانی: در هکاتون، دستیاران آموزشی بیشتر برای این حاضرند که کمک کنند *خودت* مسئله را حل کنی (نشان دادن مستندات و منابع)، نه اینکه به همهٔ پرسش‌ها جواب بدهند.
- از سخنرانی: در نمایشگاه، پروژه را روی تلفن یا لپ‌تاپ به رهگذران (استادان، دانشجویان، کارکنان و بازدیدکنندگان) نشان می‌دهی.

> [!NOTE]
> **تألیفی: برای دانشجوی CS50x**
> هکاتون و نمایشگاه رویدادهای حضوری دانشگاه هاروارد برای دانشجویان همان دوره‌اند. مشخصات، شیوهٔ ارسال و موعد پروژهٔ نهایی را فقط از [صفحهٔ رسمی پروژهٔ نهایی](https://cs50.harvard.edu/x/2026/project/) بخوان؛ این بسته هنوز راهنمای فارسی آن را ندارد.

## مرور با بازی: «پانتومیم CS50»

- از سخنرانی: دو تیم سه‌نفره واژه‌هایی از درس را که از پرسش‌های مرور خود دانشجویان برداشته شده بود، بی‌صدا و فقط با حرکت نشان دادند؛ از جمله **بازگشت** (recursion)، **پایتون**، **اردک**، **دودویی**، **آرایه**، **حلقه**، **الگوریتم**، **زمان اجرا** و **جست‌وجوی دودویی**.

## پیوندها

- قبلی: [مرور: از ورودی تا خروجی، دقت و انتزاع](/kb/d/w10-n01)
- بعدی: [نگاه به آینده: ابزارهای بعد از CS50](/kb/d/w10-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-10/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
