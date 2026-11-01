---
id: w08-n05
type: note
title: 'DHCP: نشانی IP دستگاه خودت (DHCP)'
title_fa: 'DHCP: نشانی IP دستگاه خودت'
title_en: DHCP
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: DHCP
official_anchor: dhcp
source_url: https://cs50.harvard.edu/x/2026/notes/8/#dhcp
source_refs:
- src-notes-8#dhcp
- src-transcript-8
- src-short-internet-primer
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-dhcp
- w08-c-gateway-nameserver
prev: w08-n04
next: w08-n06
order: 5
video:
  youtube_id: yYst7puZXjw
  start: '20:39'
  start_seconds: 1239
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=1239s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'yet another acronym DHCP'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# DHCP: نشانی IP دستگاه خودت

> **منبع رسمی:** بخش «DHCP» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#dhcp). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۰:۳۹ تا حدود ۲۲:۵۲](https://www.youtube.com/watch?v=yYst7puZXjw&t=1239s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

وقتی لپ‌تاپت را به وای‌فای کافه وصل می‌کنی، هیچ‌وقت نشانی IP تایپ نمی‌کنی. پس دستگاه از کجا می‌داند نشانی‌اش چیست، بسته‌ها را به کدام مسیریاب بدهد و از کدام سرور DNS بپرسد؟ پاسخ **DHCP** است.

## DHCP

- **DHCP** (`dynamic host configuration protocol`) پروتکلی است که نشانی IP دستگاه تو را تعیین می‌کند.
- این پروتکل همچنین **دروازهٔ پیش‌فرض** (`default gateway`) و **سرورهای نام** (`nameserver`) را که دستگاهت به کار می‌برد مشخص می‌کند.
- و حالا دیگر از بیرونِ پاکت استعاری‌مان حرف نمی‌زنیم: بیایید درون پاکت را ببینیم.

> [!NOTE]
> **از سخنرانی: سؤال دستگاه تازه‌وارد**
> دیوید DHCP را این‌طور توضیح می‌دهد: وقتی مک، رایانهٔ شخصی یا گوشی‌ات را برای اولین بار روشن می‌کنی، عملاً پیامی همگانی می‌فرستد شبیه «Hello world، نشانی IP من چیست؟» و سرور DHCP شبکهٔ محلی، بنا به پیکربندی دانشگاه یا شرکت اینترنتی یا خانه، نشانی دستگاه، نشانی مسیریاب محلی و نشانی سرورهای DNS را به آن می‌گوید. به گفتهٔ دیوید، در گذشته همهٔ این‌ها را باید دستی تایپ می‌کردند.

> [!TIP]
> **از ویدئوی کوتاه: پیش از DHCP**
> داگ لوید در [مقدمه‌ای بر اینترنت](/kb/d/w08-sh-internet-primer) یادآوری می‌کند که پیش از DHCP مدیران شبکه باید نشانی هر دستگاه را دستی تنظیم می‌کردند. DHCP این کار را خودکار کرد و برای همین نشانی دستگاهت ممکن است در شبکه‌های مختلف یا حتی روزهای مختلف فرق کند.

> [!IMPORTANT]
> **استنتاجی: سه پاسخ، سه یادداشت**
> سه چیزی که DHCP می‌دهد هر کدام به یک یادداشت قبلی وصل‌اند: نشانی IP (یادداشت ۲)، دروازهٔ پیش‌فرض، یعنی نخستین مسیریاب (یادداشت ۲)، و سرور نام (یادداشت ۴). بدون این سه، دستگاه نه نشانی دارد، نه می‌داند بسته‌ها را به کجا بدهد، نه می‌تواند نام‌ها را ترجمه کند.

## اشتباه‌های رایج

- فکر کردن به اینکه نشانی IP دستگاه همیشه ثابت است.
- یکی دانستن DHCP و DNS؛ DHCP به دستگاه نشانی می‌دهد و DNS نام‌ها را ترجمه می‌کند.

## جمع‌بندی

- DHCP به دستگاه نشانی IP، دروازهٔ پیش‌فرض و سرورهای نام می‌دهد.
- با DHCP بحث «بیرون پاکت» تمام می‌شود؛ از یادداشت بعد به درون پاکت می‌رویم.

## پیوندها

- قبلی: [DNS: از نام دامنه تا نشانی IP](/kb/d/w08-n04)
- بعدی: [HTTP و HTTPS: نشانی، درخواست و کد وضعیت](/kb/d/w08-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
