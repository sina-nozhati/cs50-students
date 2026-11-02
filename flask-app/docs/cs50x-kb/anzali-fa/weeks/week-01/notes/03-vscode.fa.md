---
id: w01-n03
type: note
title: 'VS Code برای CS50: فایل‌ها، ویرایشگر و ترمینال (Visual Studio Code for CS50)'
title_fa: 'VS Code برای CS50: فایل‌ها، ویرایشگر و ترمینال'
title_en: Visual Studio Code for CS50
week: 1
parent: w01-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Visual Studio Code for CS50
official_anchor: visual-studio-code-for-cs50
source_url: https://cs50.harvard.edu/x/notes/1/#visual-studio-code-for-cs50
source_refs:
- src-notes-1#visual-studio-code-for-cs50
- src-transcript-1
- src-srt-1
concept_ids:
- w01-c-ide-regions
- w01-c-gui-cli
prev: w01-n02
next: w01-n04
order: 3
video:
  youtube_id: SlqjA04_dpk
  start: '5:14'
  start_seconds: 314
  url: https://www.youtube.com/watch?v=SlqjA04_dpk&t=314s
  origin: inference
  basis: first lecture1.srt cue containing the phrase 'Visual Studio Code'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# VS Code برای CS50: فایل‌ها، ویرایشگر و ترمینال

> **منبع رسمی:** بخش «Visual Studio Code for CS50» از [درس‌نامهٔ هفتهٔ ۱ CS50x 2026](https://cs50.harvard.edu/x/notes/1/#visual-studio-code-for-cs50). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵:۱۴ تا حدود ۹:۴۲](https://www.youtube.com/watch?v=SlqjA04_dpk&t=314s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

همهٔ کارهای این هفته در یک محیط انجام می‌شود: **Visual Studio Code** که CS50 آن را در cs50.dev برایت آماده کرده است. شناخت سه بخش آن، کار با بقیهٔ هفته را ساده می‌کند.

## محیط CS50

- **ویرایشگر متن** (text editor) مورد استفادهٔ این دوره، Visual Studio Code یا همان VS Code است.
- نسخه‌ای که CS50 برایت آماده کرده در [cs50.dev](https://cs50.dev) در دسترس است.
- مهم‌ترین دلیل استفاده از آن: همهٔ نرم‌افزارهای لازم دوره از قبل رویش نصب است و دستورهای دوره بر پایهٔ همین محیط نوشته شده‌اند.
- نصب دستی این نرم‌افزارها روی کامپیوتر خودت دردسر زیادی دارد. درس‌نامه توصیه می‌کند همهٔ تکلیف‌ها را در همین محیط انجام بدهی.

![IDE with file explorer, text editor, and terminal](https://cs50.harvard.edu/x/notes/1/cs50Week1Slide017.png "IDE with file explorer, text editor, and terminal")

*تصویر رسمی: محیط VS Code با کاوشگر فایل، ویرایشگر و ترمینال.*

## سه بخش اصلی

| بخش | کار |
| --- | --- |
| **کاوشگر فایل** (file explorer) | سمت چپ؛ فایل‌هایت را نشان می‌دهد |
| **ویرایشگر متن** (text editor) | وسط؛ جایی که کد را می‌نویسی |
| **ترمینال** (terminal) یا **رابط خط فرمان** (command line interface، CLI) | پایین؛ جایی که فرمان می‌دهی |

## GUI و CLI

- بخش‌هایی که با ماوس با آن‌ها کار می‌کنی **رابط کاربری گرافیکی** (graphical user interface، GUI) هستند.
- ترمینال CLI است: با تایپ فرمان به **کامپیوتری در فضای ابری** (cloud) دستور می‌دهی.
- طبق بخش لینوکس درس‌نامه، CLI برای اجرای فرمان و کار با فایل‌ها اغلب از GUI مفیدتر است. فرمان‌ها را در [لینوکس و فرمان‌های ترمینال](/kb/d/w01-n08) می‌بینی.

## سخنرانی چه می‌گوید

**از سخنرانی:** فقط یک مرورگر وب روی هر Mac یا PC لازم داری؛ همه‌چیز از پیش نصب و پیکربندی شده است. برنامه‌ای که می‌سازی در پوشهٔ جاری تو روی همان کامپیوتر ابری قرار می‌گیرد.

## جمع‌بندی

- VS Code در cs50.dev سه بخش دارد: کاوشگر فایل، ویرایشگر و ترمینال.
- این هفته بیشتر با ترمینال کار می‌کنی.

## پیوندها

- قبلی: [کد منبع، کد ماشین و کامپایلر](/kb/d/w01-n02)
- بعدی: [سلام دنیا در C: نوشتن، کامپایل و اجرا](/kb/d/w01-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-01/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
