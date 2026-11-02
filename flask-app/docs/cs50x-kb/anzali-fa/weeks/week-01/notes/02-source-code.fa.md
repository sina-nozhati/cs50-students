---
id: w01-n02
type: note
title: کد منبع، کد ماشین و کامپایلر (Source Code)
title_fa: کد منبع، کد ماشین و کامپایلر
title_en: Source Code
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Source Code
official_anchor: source-code
source_url: https://cs50.harvard.edu/x/notes/1/#source-code
source_refs:
- src-notes-1#source-code
- src-transcript-1
- src-srt-1
concept_ids:
- w01-c-source-code
- w01-c-machine-code
- w01-c-compiler
prev: w01-n01
next: w01-n03
order: 2
video:
  youtube_id: SlqjA04_dpk
  start: '3:15'
  start_seconds: 195
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=195s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'source code'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# کد منبع، کد ماشین و کامپایلر

> **منبع رسمی:** بخش «Source Code» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#source-code). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳:۱۵ تا حدود ۵:۱۴](https://www.youtube.com/watch?v=SlqjA04_dpk&t=195s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

برنامه‌ای که ما می‌نویسیم با چیزی که کامپیوتر اجرا می‌کند فرق دارد. این بخش توضیح می‌دهد پل میان این دو چیست.

## کد منبع و کد ماشین

- برنامه‌ای که انسان می‌نویسد **کد منبع** (source code) نام دارد.
- کامپیوتر فقط صفر و یک می‌فهمد. به این صفر و یک‌ها **کد ماشین** (machine code) می‌گوییم.
- **کامپایلر** (compiler) نرم‌افزار ویژه‌ای است که کد منبع را به کد ماشین تبدیل می‌کند.

درس‌نامه این فرایند را با نمودار زیر نشان می‌دهد (در درس‌نامهٔ رسمی نمودار Mermaid است؛ اینجا متن آن عیناً آمده است):

```text
flowchart LR
    in["source code"] --> BOX[" compiler "]
    BOX --> out["machine code"]
```

خوانش فارسی نمودار: کد منبع ← کامپایلر ← کد ماشین.

## سه معیار کد خوب

درس‌نامه می‌گوید امروز سه چیز را بررسی می‌کنیم:

1. **درستی** (correctness): آیا کد همان‌طور که می‌خواهیم اجرا می‌شود؟
2. **طراحی** (design): کد چقدر خوب طراحی شده است؟
3. **سبک** (style): کد چقدر زیبا و یکدست است؟

این سه معیار را در [درستی، طراحی و سبک](/kb/d/w01-n17) دوباره می‌بینیم.

## پیوند با هفتهٔ ۰

در هفتهٔ ۰، **از سخنرانی**، کامپایلر «برنامه‌ای که یک زبان را به زبان دیگر ترجمه می‌کند» معرفی شد. در Scratch این کار پشت صحنه انجام می‌شد؛ در C خودت با فرمان `make` کامپایلر را اجرا می‌کنی.

## اشتباه‌های رایج

- یکی گرفتن «فایل `.c`» با «برنامهٔ قابل اجرا». فایل `.c` کد منبع است؛ برنامهٔ اجرایی بعد از کامپایل ساخته می‌شود.
- فکر کردن به این‌که «کد درست اجرا می‌شود، پس خوب است». درستی فقط یکی از سه معیار است.

## جمع‌بندی

- کد منبع برای انسان است، کد ماشین برای کامپیوتر.
- کامپایلر این دو را به هم وصل می‌کند.

## پیوندها

- قبلی: [خوش آمدید: از Scratch به C](/kb/d/w01-n01)
- بعدی: [VS Code برای CS50: فایل‌ها، ویرایشگر و ترمینال](/kb/d/w01-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
