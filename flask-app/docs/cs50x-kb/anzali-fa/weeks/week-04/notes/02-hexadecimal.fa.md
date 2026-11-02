---
id: w04-n02
type: note
title: مبنای شانزده (هگزادسیمال) (Hexadecimal)
title_fa: مبنای شانزده (هگزادسیمال)
title_en: Hexadecimal
week: 4
parent: w04-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Hexadecimal
official_anchor: hexadecimal
source_url: https://cs50.harvard.edu/x/2026/notes/4/#hexadecimal
source_refs:
- src-notes-4#hexadecimal
- src-transcript-4
- src-short-hexadecimal
- src-anzali-authored-4
- src-srt-4
concept_ids:
- w04-c-rgb-hex-color
- w04-c-hexadecimal
- w04-c-hex-place-values
- w04-c-hex-byte
prev: w04-n01
next: w04-n03
order: 2
video:
  youtube_id: db0H0U13YsA
  start: '4:22'
  start_seconds: 262
  url: https://www.youtube.com/watch?v=db0H0U13YsA&t=262s
  origin: inference
  basis: first lecture4.srt cue containing the phrase 'Photoshop or similar editing'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مبنای شانزده (هگزادسیمال)

> **منبع رسمی:** بخش «Hexadecimal» از [درس‌نامهٔ هفتهٔ ۴ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/4/#hexadecimal). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۴:۲۲ تا حدود ۱۱:۴۴](https://www.youtube.com/watch?v=db0H0U13YsA&t=262s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

نشانی‌های حافظه، رنگ‌ها و بایت‌های فایل‌ها را معمولاً در **مبنای شانزده** (hexadecimal) می‌نویسند. اگر این مبنا را بشناسی، `0x7ffc...` در خروجی برنامه یا `FF0000` در یک ویرایشگر تصویر دیگر عجیب به نظر نمی‌رسد.

## RGB و یک عدد عجیب

- **RGB** یعنی قرمز، سبز و آبی: سه عدد که مقدار هر یک از این رنگ‌ها را نشان می‌دهند.
- درس‌نامه پنجرهٔ انتخاب رنگ Adobe Photoshop را نشان می‌دهد: با تغییر مقدار قرمز، سبز و آبی، رنگ انتخاب‌شده عوض می‌شود.
- پایین همان پنجره مقداری هست که از رقم و حرف ساخته شده است. مثلاً `255` آنجا به‌صورت `FF` نوشته می‌شود. چرا؟

## مبنای شانزده

هگزادسیمال سیستم شمارشی با ۱۶ رقم است:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

- `F` یعنی `15`. به این سیستم **مبنای ۱۶** (base-16) هم می‌گویند.
- در هگزادسیمال هر ستون توانی از ۱۶ است.
- چند نمونه از درس‌نامه:

| دهدهی | هگزادسیمال |
|---|---|
| 0 | `00` |
| 1 | `01` |
| 9 | `09` |
| 10 | `0A` |
| 15 | `0F` |
| 16 | `10` |
| 255 | `FF` |

- چرا `FF` برابر 255 است؟ ستون چپ ۱۶تایی‌ها را می‌شمارد: ۱۶ × ۱۵ (یعنی `F`) می‌شود 240 و با 15 ستون راست می‌شود 255. این بزرگ‌ترین عددی است که با دو رقم هگزادسیمال می‌شود نوشت.
- فایدهٔ هگزادسیمال این است که اطلاعات را با رقم‌های **کمتر** و خلاصه‌تر نشان می‌دهد.

> [!IMPORTANT]
> **مهم**
> هر رقم هگزادسیمال دقیقاً ۴ بیت است (۱۶ = ۲ به توان ۴)، پس دو رقم دقیقاً یک بایت (۸ بیت) است. برای همین `FF` یعنی بایتی که هر هشت بیتش ۱ است. این را ویدئوی کوتاه [Hexadecimal](/kb/d/w04-sh-hexadecimal) مفصل نشان می‌دهد.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David توضیح داد که در Photoshop رنگ سفید را می‌شود با `FF FF FF` نشان داد، یعنی بیشترین مقدار قرمز، سبز و آبی، و سیاه را با `00 00 00`.
- **از سخنرانی:** او گفت امروز `0x`های زیادی و عددهای دو، چهار یا هشت رقمی هگزادسیمال می‌بینیم، اما معمولاً برایمان مهم نیست این عددها به دهدهی چه می‌شوند و لازم نیست حساب زیادی بکنیم؛ فقط باید به دیدن این شکل نوشتن عادت کنیم.

> [!TIP]
> **تألیفی: تبدیل دستی**
> برای تبدیل `0x2A` به دهدهی: 2 × 16 + 10 = 42. برای تبدیل 200 به هگزادسیمال: 200 ÷ 16 = 12 با باقی‌ماندهٔ 8، پس `C8`.

## اشتباه‌های رایج

- خواندن `10` هگزادسیمال به‌جای ده؛ `0x10` یعنی شانزده.
- فراموش کردن اینکه حرف‌های `A` تا `F` رقم‌اند و مقدارشان ۱۰ تا ۱۵ است.
- فکر کردن به اینکه هگزادسیمال «نوع دادهٔ» جدیدی است؛ فقط روش دیگری برای **نوشتن** همان عدد است.

## جمع‌بندی

- هگزادسیمال ۱۶ رقم دارد و هر ستونش توانی از ۱۶ است.
- دو رقم هگزادسیمال یک بایت است و `FF` برابر 255.
- رنگ‌های RGB معمولاً با سه جفت رقم هگزادسیمال نوشته می‌شوند.

## پیوندها

- قبلی: [خوش آمدید: هنر پیکسلی](/kb/d/w04-n01)
- بعدی: [حافظه و نشانی‌ها](/kb/d/w04-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-04/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
