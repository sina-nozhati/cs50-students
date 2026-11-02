---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sh-variables-and-scope
type: short-summary
title: 'ویدئوی کوتاه: متغیرها و حوزه (Variables and Scope)'
title_fa: متغیرها و حوزه
title_en: Variables and Scope
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/variables_and_scope/
source_refs:
- src-short-variables-and-scope
- src-anzali-inference-2
concept_ids:
- w02-c-local-global
- w02-c-pass-by-value
prev: w02-sh-functions
next: w02-sh-debugging-step-through
order: 23
video:
  youtube_id: GiFbdVGjF9I
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: متغیرهای محلی
    evidence_en: null
  - start: '1:26'
    start_seconds: 86
    title_fa: متغیرهای سراسری
    evidence_en: global variables do exist
  - start: '2:44'
    start_seconds: 164
    title_fa: فراخوانی با مقدار
    evidence_en: passed by value
  - start: '3:40'
    start_seconds: 220
    title_fa: تغییر ندادن و بازنویسی foo
    evidence_en: foo is not changed
  - start: '4:48'
    start_seconds: 288
    title_fa: نام‌های تکراری و حوزه
    evidence_en: same variable name
  - start: '5:20'
    start_seconds: 320
    title_fa: 'تمرین: دو x هم‌نام'
    evidence_en: what would be printed
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: متغیرها و حوزه (Variables and Scope)

> **منبع رسمی:** [صفحهٔ Short «Variables and Scope» در CS50x](https://cs50.harvard.edu/x/shorts/variables_and_scope/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو تفاوت متغیر محلی (local) و سراسری (global) را توضیح می‌دهد و نشان می‌دهد چرا این تفاوت مهم است: متغیرهای محلی هنگام فراخوانی تابع «با مقدار» (by value) فرستاده می‌شوند، یعنی تابع گیرنده یک کپی می‌گیرد.

در پایان یک برنامهٔ نمونه با دو متغیر هم‌نام `x` (یکی در `main` و یکی در `increment`) را دنبال می‌کنی.

## نکته‌های کلیدی

- متغیر محلی فقط درون تابعی که در آن اعلان شده شناخته می‌شود؛ تابع‌های دیگر نمی‌توانند به آن اشاره کنند.
- متغیر سراسری بیرون از همهٔ تابع‌ها اعلان می‌شود و همهٔ تابع‌ها به آن دسترسی دارند. انعطاف دارد اما خطرناک است، چون یک تابع ممکن است مقدارش را زودتر از انتظار تغییر دهد.
- در فراخوانی با مقدار، تابع گیرنده (callee) کپی خودش را می‌گیرد؛ متغیر در تابع فراخواننده (caller) تغییر نمی‌کند مگر اینکه مقدار بازگشتی را دوباره در آن بریزی.
- مثال ویدئو: `triple(foo)` به‌تنهایی `foo` را تغییر نمی‌دهد، اما `foo = triple(foo)` آن را به ۱۲ تبدیل می‌کند.
- وقتی یک نام در چند تابع تکرار می‌شود (که در کار تیمی زیاد پیش می‌آید)، باید با دقت دنبال کنی هر نمونه متعلق به کدام تابع است.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`variables_and_scope.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — متغیرهای محلی](https://www.youtube.com/watch?v=GiFbdVGjF9I&t=0s)
- [۱:۲۶ — متغیرهای سراسری](https://www.youtube.com/watch?v=GiFbdVGjF9I&t=86s)
- [۲:۴۴ — فراخوانی با مقدار](https://www.youtube.com/watch?v=GiFbdVGjF9I&t=164s)
- [۳:۴۰ — تغییر ندادن و بازنویسی foo](https://www.youtube.com/watch?v=GiFbdVGjF9I&t=220s)
- [۴:۴۸ — نام‌های تکراری و حوزه](https://www.youtube.com/watch?v=GiFbdVGjF9I&t=288s)
- [۵:۲۰ — تمرین: دو x هم‌نام](https://www.youtube.com/watch?v=GiFbdVGjF9I&t=320s)

## مفاهیم مرتبط

- متغیر محلی و متغیر سراسری — [یادداشت](/kb/d/w02-sh-variables-and-scope) · درس کوتاه `w02-l05` (واحد `w02-l05-u04`)
- ارسال با مقدار: تابع کپی می‌گیرد — [یادداشت](/kb/d/w02-sh-variables-and-scope) · درس کوتاه `w02-l05` (واحد `w02-l05-u04`)

## منابع

- [ویدئو در YouTube](https://youtu.be/GiFbdVGjF9I) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/variables_and_scope/variables_and_scope.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/variables_and_scope/lang/en/variables_and_scope.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/variables_and_scope/lang/en/variables_and_scope.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
