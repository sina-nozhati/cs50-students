---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sh-debugging-step-through
type: short-summary
title: 'ویدئوی کوتاه: اشکال‌زدایی: اجرای گام‌به‌گام (Debugging step through)'
title_fa: 'اشکال‌زدایی: اجرای گام‌به‌گام'
title_en: Debugging step through
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2021 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/debugging_step_through/
source_refs:
- src-short-debugging-step-through
- src-anzali-inference-2
concept_ids:
- w02-c-debugger
- w02-c-breakpoint
- w02-c-step-over-into
- w02-c-logical-error
prev: w02-sh-variables-and-scope
next: w02-sh-debugging-step-into
order: 24
video:
  youtube_id: '---HbbANxDQ'
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: معرفی بازی guess
    evidence_en: null
  - start: 0:44
    start_seconds: 44
    title_fa: گذاشتن نقطهٔ توقف
    evidence_en: break point
  - start: '1:04'
    start_seconds: 64
    title_fa: اجرا با debug50
    evidence_en: debug50 of guess
  - start: '1:25'
    start_seconds: 85
    title_fa: Step Over و دیدن مقدارها
    evidence_en: Step Over button
  - start: '2:18'
    start_seconds: 138
    title_fa: پیدا کردن اشکال حلقه
    evidence_en: while loop
  - start: '2:47'
    start_seconds: 167
    title_fa: باگ دوم برای تو
    evidence_en: leave this one up to you
  chapters_origin: inference
recorded: '2021'
presenter: Carter
---

# ویدئوی کوتاه: اشکال‌زدایی: اجرای گام‌به‌گام (Debugging step through)

> **منبع رسمی:** [صفحهٔ Short «Debugging step through» در CS50x](https://cs50.harvard.edu/x/shorts/debugging_step_through/)، با ارائهٔ Carter، ضبط‌شده در ۲۰۲۱ با محیط VS Code. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

Carter یک بازی حدس عدد به نام `guess` دارد که با هر حدس نادرست، صفحه را پر از پیام می‌کند. او با `debug50`، یک نقطهٔ توقف و دکمهٔ Step Over خط‌به‌خط جلو می‌رود و مقدار متغیرها را تماشا می‌کند.

اشکال این بود که به‌جای `if` از `while` استفاده شده بود. بعد از اصلاح، باگ دیگری می‌ماند که پیدا کردنش به خود بیننده سپرده می‌شود.

## نکته‌های کلیدی

- نقطهٔ توقف (breakpoint) را با کلیک روی دایرهٔ کم‌رنگ کنار شمارهٔ خط می‌گذاری تا قرمز پررنگ شود.
- پیش از اجرای خط مقداردهی، متغیرها ممکن است مقدار عجیبی داشته باشند (در ویدئو، `guess` مقدار 32,764 دارد).
- Step Over خط بعدی را اجرا می‌کند؛ خط برجسته‌شدهٔ زرد نشان می‌دهد برنامه کجاست.
- دیدن اینکه اجرای برنامه دوباره به خط حلقه برمی‌گردد، نشانهٔ این بود که حلقه جای شرط نشسته است.
- بعد از هر اصلاح، دوباره `make` کن و برنامه را امتحان کن.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`guess.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — معرفی بازی guess](https://www.youtube.com/watch?v=---HbbANxDQ&t=0s)
- [۰:۴۴ — گذاشتن نقطهٔ توقف](https://www.youtube.com/watch?v=---HbbANxDQ&t=44s)
- [۱:۰۴ — اجرا با debug50](https://www.youtube.com/watch?v=---HbbANxDQ&t=64s)
- [۱:۲۵ — Step Over و دیدن مقدارها](https://www.youtube.com/watch?v=---HbbANxDQ&t=85s)
- [۲:۱۸ — پیدا کردن اشکال حلقه](https://www.youtube.com/watch?v=---HbbANxDQ&t=138s)
- [۲:۴۷ — باگ دوم برای تو](https://www.youtube.com/watch?v=---HbbANxDQ&t=167s)

## مفاهیم مرتبط

- دیباگر و debug50 — [یادداشت](/kb/d/w02-n05) · درس کوتاه `w02-l02` (واحد `w02-l02-u01`)
- نقطهٔ توقف (breakpoint) — [یادداشت](/kb/d/w02-n05) · درس کوتاه `w02-l02` (واحد `w02-l02-u01`)
- Step Over و Step Into — [یادداشت](/kb/d/w02-n05) · درس کوتاه `w02-l02` (واحد `w02-l02-u02`)
- خطای منطقی — [یادداشت](/kb/d/w02-n03) · درس کوتاه `w02-l01` (واحد `w02-l01-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/---HbbANxDQ)
- [زیرنویس](https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.srt) · [متن گفتار](https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
