---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-call-stacks
type: short-summary
title: 'ویدئوی کوتاه: پشتهٔ فراخوانی (Call Stacks)'
title_fa: پشتهٔ فراخوانی
title_en: Call Stacks
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/call_stacks/
source_refs:
- src-short-call-stacks
- src-anzali-inference-3
concept_ids:
- w03-c-call-stack
- w03-c-recursion
prev: w03-sh-selection-sort
next: w03-sh-recursion
order: 26
video:
  youtube_id: aCPkszeKRa4
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: قاب پشته
    evidence_en: null
  - start: '1:39'
    start_seconds: 99
    title_fa: قاب فعال
    evidence_en: that is called the active frame
  - start: '2:05'
    start_seconds: 125
    title_fa: push و pop
    evidence_en: pushed onto the top of the stack
  - start: '3:12'
    start_seconds: 192
    title_fa: نمونهٔ فاکتوریل
    evidence_en: an example using the factorial function
  - start: '3:38'
    start_seconds: 218
    title_fa: printf منتظر می‌ماند
    evidence_en: It calls printf()
  - start: '5:26'
    start_seconds: 326
    title_fa: حالت پایه برمی‌گردد
    evidence_en: It's going to return 1
  - start: '6:30'
    start_seconds: 390
    title_fa: بازگشت جواب‌ها
    evidence_en: It got its answer back of 6
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: پشتهٔ فراخوانی (Call Stacks)

> **منبع رسمی:** [صفحهٔ Short «Call Stacks» در CS50x](https://cs50.harvard.edu/x/shorts/call_stacks/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

وقتی تابعی صدا زده می‌شود، سیستم برایش جایی در حافظه کنار می‌گذارد: یک **قاب پشته** (`stack frame`). اگر چند تابع صدا زده شوند، قاب‌ها روی هم چیده می‌شوند و فقط قاب بالایی **فعال** است.

ویدئو با `main` که `move` و آن `direction` را صدا می‌زند شروع می‌کند و بعد فراخوانی بازگشتی `fact(5)` را قاب‌به‌قاب دنبال می‌کند تا ۱۲۰ چاپ شود.

## نکته‌های کلیدی

- تابعی که تازه صدا زده می‌شود روی پشته «push» می‌شود و قاب فعال است؛ بقیه منتظرند.
- وقتی تابع کارش تمام شد و مقدارش را برگرداند، قابش «pop» می‌شود و تابع زیرین دوباره فعال می‌شود.
- در نمونهٔ فاکتوریل، `main` تابع `printf` را صدا می‌زند که منتظر `fact(5)` است، و `fact(5)` منتظر `fact(4)` و همین‌طور تا `fact(1)`؛ در آن لحظه هفت قاب روی پشته است.
- `fact(1)` حالت پایه است و ۱ برمی‌گرداند؛ بعد جواب‌ها یکی‌یکی پایین می‌آیند تا `printf` عدد ۱۲۰ را چاپ کند.
- **توجه:** ویدئو در پایان می‌گوید `printf` «چیزی برنمی‌گرداند»؛ در واقع `printf` یک int (تعداد نویسه‌های چاپ‌شده) برمی‌گرداند که این‌جا استفاده نمی‌شود (ناهمخوانی d51).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`call_stacks.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — قاب پشته](https://www.youtube.com/watch?v=aCPkszeKRa4&t=0s)
- [۱:۳۹ — قاب فعال](https://www.youtube.com/watch?v=aCPkszeKRa4&t=99s)
- [۲:۰۵ — push و pop](https://www.youtube.com/watch?v=aCPkszeKRa4&t=125s)
- [۳:۱۲ — نمونهٔ فاکتوریل](https://www.youtube.com/watch?v=aCPkszeKRa4&t=192s)
- [۳:۳۸ — printf منتظر می‌ماند](https://www.youtube.com/watch?v=aCPkszeKRa4&t=218s)
- [۵:۲۶ — حالت پایه برمی‌گردد](https://www.youtube.com/watch?v=aCPkszeKRa4&t=326s)
- [۶:۳۰ — بازگشت جواب‌ها](https://www.youtube.com/watch?v=aCPkszeKRa4&t=390s)

## مفاهیم مرتبط

- پشتهٔ فراخوانی و قاب‌های تابع — [یادداشت](/kb/d/w03-sh-call-stacks) · درس کوتاه `w03-l06` (واحد `w03-l06-u02`)
- بازگشت: تابعی که خودش را صدا می‌زند — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/aCPkszeKRa4) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/call_stacks/call_stacks.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/call_stacks/lang/en/call_stacks.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/call_stacks/lang/en/call_stacks.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
