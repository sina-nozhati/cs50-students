---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sh-debugging-step-into
type: short-summary
title: 'ویدئوی کوتاه: اشکال‌زدایی: ورود به تابع (Step Into) (Debugging step into)'
title_fa: 'اشکال‌زدایی: ورود به تابع (Step Into)'
title_en: Debugging step into
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2021 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/debugging_step_into/
source_refs:
- src-short-debugging-step-into
- src-anzali-inference-2
concept_ids:
- w02-c-step-over-into
- w02-c-debugger
- w02-c-strcmp
prev: w02-sh-debugging-step-through
next: w02-sh-arrays
order: 25
video:
  youtube_id: tk3cl8hyfqM
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: معرفی برنامهٔ secret
    evidence_en: null
  - start: 0:38
    start_seconds: 38
    title_fa: نگاه به کد
    evidence_en: code secret.c
  - start: 0:50
    start_seconds: 50
    title_fa: نقطهٔ توقف و Step Over
    evidence_en: breakpoint
  - start: '1:51'
    start_seconds: 111
    title_fa: Step Into
    evidence_en: step into
  - start: '2:50'
    start_seconds: 170
    title_fa: مقایسهٔ رشته‌ها با strcmp
    evidence_en: string compare
  - start: '3:39'
    start_seconds: 219
    title_fa: اجرای دوباره
    evidence_en: come on in
  chapters_origin: inference
recorded: '2021'
presenter: Carter
---

# ویدئوی کوتاه: اشکال‌زدایی: ورود به تابع (Step Into) (Debugging step into)

> **منبع رسمی:** [صفحهٔ Short «Debugging step into» در CS50x](https://cs50.harvard.edu/x/shorts/debugging_step_into/)، با ارائهٔ Carter، ضبط‌شده در ۲۰۲۱ با محیط VS Code. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

Carter برنامه‌ای به نام `secret` دارد که اگر عبارت رمز درست (please) وارد شود، باید «come on in» چاپ کند؛ اما نمی‌کند. Step Over از روی تابع `check_phrase` علت را نشان نمی‌دهد.

با Step Into وارد خود تابع می‌شود و می‌بیند اشکال در مقایسهٔ دو رشته با `==` است. در C برای مقایسهٔ رشته‌ها از `strcmp` استفاده می‌شود که اگر دو رشته یکسان باشند 0 برمی‌گرداند.

## نکته‌های کلیدی

- گاهی Step Over کافی نیست: کل برنامه را رد می‌کنی و اشکال را نمی‌بینی، چون اشکال درون یک تابع است.
- Step Into به درون تابع فراخوانی‌شده می‌رود تا خط‌های خود آن را گام‌به‌گام ببینی.
- در C دو رشته را نمی‌توان با `==` مقایسه کرد؛ ویدئو `strcmp` را معرفی می‌کند. چرایی آن در هفته‌های بعد روشن می‌شود.
- `strcmp` وقتی دو رشته دقیقاً برابر باشند 0 برمی‌گرداند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`secret.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — معرفی برنامهٔ secret](https://www.youtube.com/watch?v=tk3cl8hyfqM&t=0s)
- [۰:۳۸ — نگاه به کد](https://www.youtube.com/watch?v=tk3cl8hyfqM&t=38s)
- [۰:۵۰ — نقطهٔ توقف و Step Over](https://www.youtube.com/watch?v=tk3cl8hyfqM&t=50s)
- [۱:۵۱ — Step Into](https://www.youtube.com/watch?v=tk3cl8hyfqM&t=111s)
- [۲:۵۰ — مقایسهٔ رشته‌ها با strcmp](https://www.youtube.com/watch?v=tk3cl8hyfqM&t=170s)
- [۳:۳۹ — اجرای دوباره](https://www.youtube.com/watch?v=tk3cl8hyfqM&t=219s)

## مفاهیم مرتبط

- Step Over و Step Into — [یادداشت](/kb/d/w02-n05) · درس کوتاه `w02-l02` (واحد `w02-l02-u02`)
- دیباگر و debug50 — [یادداشت](/kb/d/w02-n05) · درس کوتاه `w02-l02` (واحد `w02-l02-u01`)
- مقایسهٔ رشته‌ها با strcmp، نه == — [یادداشت](/kb/d/w02-sh-debugging-step-into) · درس کوتاه `w02-l02` (واحد `w02-l02-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/tk3cl8hyfqM)
- [زیرنویس](https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.srt) · [متن گفتار](https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
