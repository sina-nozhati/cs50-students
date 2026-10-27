---
id: w01-n17
type: note
title: درستی، طراحی و سبک (Correctness, Design, Style)
title_fa: درستی، طراحی و سبک
title_en: Correctness, Design, Style
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Correctness, Design, Style
official_anchor: correctness-design-style
source_url: https://cs50.harvard.edu/x/notes/1/#correctness-design-style
source_refs:
- src-notes-1#correctness-design-style
- src-transcript-1
- src-section-1
- src-pset-1
- src-style-guide-c
- src-srt-1
concept_ids:
- w01-c-correctness-design-style
prev: w01-n16
next: w01-n18
order: 17
video:
  youtube_id: SlqjA04_dpk
  start: '1:58:34'
  start_seconds: 7114
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=7114s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'style 50'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# درستی، طراحی و سبک

> **منبع رسمی:** بخش «Correctness, Design, Style» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#correctness-design-style). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۸:۳۴ تا حدود ۲:۰۲:۴۹](https://www.youtube.com/watch?v=SlqjA04_dpk&t=7114s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

کدی که اجرا می‌شود لزوماً کد خوب نیست. CS50 کد را روی **سه محور** می‌سنجد و برای هر محور ابزاری دارد.

## سه محور

| محور | پرسش | ابزار |
| --- | --- | --- |
| **درستی** (correctness) | آیا کد همان‌طور که می‌خواهیم اجرا می‌شود؟ | `check50` |
| **طراحی** (design) | کد چقدر خوب طراحی شده است؟ | `design50` |
| **سبک** (style) | کد چقدر زیبا و یکدست است؟ | `style50` |

## در عمل

- `check50` را با شناسهٔ مسئله اجرا می‌کنی، مثلاً `check50 cs50/problems/2026/x/me`. دستور دقیق هر مسئله در صفحهٔ رسمی همان مسئله آمده است.
- `style50` را با نام فایل اجرا می‌کنی، مثلاً `style50 hello.c`.
- **از جلسهٔ حل تمرین (Section 1):** در cs50.dev دکمه‌های style50 و design50 هم در محیط هست. design50 بازخورد طراحی می‌دهد.

> **توجه:** برخی صفحه‌های پرابلم‌ست فقط `check50` و `style50` را نام می‌برند. design50 در درس‌نامه و جلسهٔ حل تمرین آمده است.

## سخنرانی چه می‌گوید

**از سخنرانی:** سبک «اولین مانع» برای تحویل کد خوب است، اما طراحی بسیار ذهنی‌تر است. برای مثال، تکرار یک خط به‌جای حلقه کار می‌کند اما طراحی ضعیفی دارد.

## چرا مهم است؟

- **درستی** بدون طراحی خوب، کد را سخت‌خوان و پرخطا می‌کند.
- **سبک** یکدست باعث می‌شود دیگران (و خودت در آینده) کد را راحت بخوانند. راهنمای رسمی سبک C در [cs50.readthedocs.io/style/c](https://cs50.readthedocs.io/style/c/) است.

## اشتباه‌های رایج

- اکتفا به این‌که «کد کامپایل شد».
- نادیده گرفتن پیشنهادهای `style50` دربارهٔ تورفتگی و فاصله.

## جمع‌بندی

- درستی با `check50`، طراحی با `design50`، سبک با `style50`.

## پیوندها

- قبلی: [توابع: انتزاع، پارامتر، حوزه و مقدار بازگشتی](/kb/d/w01-n16)
- بعدی: [Mario: حلقه‌های تودرتو، ثابت و تابع کمکی](/kb/d/w01-n18)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
