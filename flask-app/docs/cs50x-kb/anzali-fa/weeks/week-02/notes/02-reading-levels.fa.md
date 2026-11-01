---
id: w02-n02
type: note
title: 'سطح خوانایی متن و رمزنگاری: دو مسئلهٔ این هفته (Reading Levels)'
title_fa: 'سطح خوانایی متن و رمزنگاری: دو مسئلهٔ این هفته'
title_en: Reading Levels
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Reading Levels
official_anchor: reading-levels
source_url: https://cs50.harvard.edu/x/2026/notes/2/#reading-levels
source_refs:
- src-notes-2#reading-levels
- src-transcript-2
- src-pset-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-reading-level
prev: w02-n01
next: w02-n03
order: 2
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:56'
  start_seconds: 116
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=116s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'reading level'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# سطح خوانایی متن و رمزنگاری: دو مسئلهٔ این هفته

> **منبع رسمی:** بخش «Reading Levels» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#reading-levels). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۶ تا حدود ۹:۲۲](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=116s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

می‌شود به یک کامپیوتر یاد داد که «سخت بودن» یک متن را بسنجد؟ این یکی از مسئله‌های واقعی همین هفته است و تمرین **Readability** پرابلم‌ست ۲ دقیقاً همین را می‌خواهد.

## حرف اصلی درس‌نامه

- یکی از مسئله‌های واقعی این درس، فهمیدن **سطح خوانایی** (`reading level`) متن است.
- در کلاس، با کمک چند دانشجو، متن‌هایی با سطح‌های خوانایی متفاوت خوانده شد.
- این هفته سطح خوانایی را **کمّی** می‌کنیم؛ یعنی آن را به عدد تبدیل می‌کنیم. این یکی از چالش‌های برنامه‌نویسی‌ات است.

## سخنرانی چه می‌گوید

**از سخنرانی:** سه داوطلب سه متن خواندند و David گفت با سنجه‌ای که در پرابلم‌ست می‌بینی:

| داوطلب | ویژگی متن | سطح طبق همان سنجه |
| --- | --- | --- |
| Lea | عبارت‌های خیلی کوتاه و ساده | پیش از کلاس اول (Before Grade 1) |
| Maria | جمله‌هایی از Dr. Seuss با قافیه | کلاس سوم (Grade 3) |
| Omar | یک پاراگراف کامل با جمله‌ها و واژه‌های پیچیده‌تر | کلاس دهم (Grade 10) |

- **از سخنرانی:** برای سنجیدن، باید متن را ریزتر از «یک رشتهٔ کامل» ببینیم: حرف‌به‌حرف و واژه‌به‌واژه. ابزار این کار آرایه است، که در همین هفته یاد می‌گیری.
- **از سخنرانی:** مسئلهٔ دوم هفته **رمزنگاری** (`cryptography`) است: هنر به‌هم‌ریختن اطلاعات تا بتوان پیام امن فرستاد. پایان سخنرانی دوباره به آن برمی‌گردد؛ یادداشت [رمزنگاری](/kb/d/w02-n18) را ببین.

## پیوند با پرابلم‌ست

> **تألیفی:** راهنمای فارسی [Readability](/kb/d/w02-ps-readability) فقط الزامات رسمی و سرنخ‌های مفهومی را می‌آورد. فرمول رسمی در همان راهنما با پیوند به صفحهٔ رسمی آمده است.

## جمع‌بندی

- سطح خوانایی را می‌شود با شمردن حرف‌ها، واژه‌ها و جمله‌ها به عدد تبدیل کرد.
- برای چنین شمارشی باید درون رشته را ببینیم؛ آرایه همین امکان را می‌دهد.

## پیوندها

- قبلی: [خوش آمدید: نگاهی زیر کاپوت](/kb/d/w02-n01)
- بعدی: [باگ و خطاهای کامپایل](/kb/d/w02-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
