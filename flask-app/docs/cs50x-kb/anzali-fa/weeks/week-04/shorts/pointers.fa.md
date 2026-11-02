---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-sh-pointers
type: short-summary
title: 'ویدئوی کوتاه: اشاره‌گرها (Pointers)'
title_fa: اشاره‌گرها
title_en: Pointers
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/pointers/
source_refs:
- src-short-pointers
- src-anzali-inference-4
concept_ids:
- w04-c-pointer
- w04-c-null-pointer
- w04-c-address-of
- w04-c-dereference
- w04-c-pointer-size
- w04-c-string-char-star
- w04-c-swap-by-pointer
- w04-c-memory-addresses
prev: w04-sh-hexadecimal
next: w04-sh-defining-custom-types
order: 19
video:
  youtube_id: XISnO2YhnsY
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: چرا اشاره‌گر
    evidence_en: null
  - start: 0:50
    start_seconds: 50
    title_fa: ارسال با مقدار
    evidence_en: passed by value
  - start: '3:22'
    start_seconds: 202
    title_fa: 'حافظه: RAM'
    evidence_en: we have to move it to RAM
  - start: '5:09'
    start_seconds: 309
    title_fa: حافظه مثل آرایه‌ای از بایت‌ها
    evidence_en: memory as a big array of byte-sized cells
  - start: '9:32'
    start_seconds: 572
    title_fa: اشاره‌گر فقط یک نشانی است
    evidence_en: A pointer is nothing more than an address
  - start: '14:54'
    start_seconds: 894
    title_fa: اشاره‌گر NULL
    evidence_en: called the null pointer
  - start: '17:31'
    start_seconds: 1051
    title_fa: عملگر & و نام آرایه
    evidence_en: an array's name is actually itself a pointer
  - start: '19:19'
    start_seconds: 1159
    title_fa: dereference
    evidence_en: This is called dereferencing
  - start: '21:21'
    start_seconds: 1281
    title_fa: dereference کردن NULL
    evidence_en: dereference a pointer whose value is null
  - start: '24:14'
    start_seconds: 1454
    title_fa: چند اشاره‌گر در یک خط
    evidence_en: declare multiple variables of the same type
  - start: '25:52'
    start_seconds: 1552
    title_fa: اندازهٔ یک رشته
    evidence_en: how large is a string
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: اشاره‌گرها (Pointers)

> **منبع رسمی:** [صفحهٔ Short «Pointers» در CS50x](https://cs50.harvard.edu/x/shorts/pointers/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو اشاره‌گرها را شاید سخت‌ترین موضوع CS50 می‌نامد، ولی ابزاری که اجازه می‌دهد داده را واقعاً بین تابع‌ها جابه‌جا کنیم، نه فقط کپی آن را. ابتدا حافظه (RAM) را یک آرایهٔ بزرگ از خانه‌های یک‌بایتی معرفی می‌کند که هر خانه نشانی دارد.

بعد مهم‌ترین جمله را تکرار می‌کند: «اشاره‌گر چیزی جز یک نشانی نیست». سپس NULL، عملگر &، نام آرایه به‌عنوان اشاره‌گر، dereference با *، دام تعریف چند اشاره‌گر در یک خط و اندازهٔ اشاره‌گر را می‌بیند.

## نکته‌های کلیدی

- در C داده‌ها با مقدار (کپی) به تابع فرستاده می‌شوند؛ به همین دلیل swap معمولی مقدارهای فراخواننده را عوض نمی‌کند، ولی با اشاره‌گر تغییرها در تابع دیگر هم اثر می‌کنند.
- هر نوع داده فضای مشخصی می‌گیرد: int چهار بایت، char یک بایت، float چهار بایت، double و long long هشت بایت.
- اشاره‌گر داده‌ای است که مقدارش یک نشانی حافظه است؛ نوع اشاره‌گر می‌گوید در آن نشانی چه نوع داده‌ای پیدا می‌شود.
- اگر اشاره‌گر را بلافاصله مقدار معنادار نمی‌دهی، آن را NULL بگذار؛ dereference کردن NULL باعث segmentation fault می‌شود و ویدئو می‌گوید این خراب شدن از دست زدن بی‌صدا به حافظهٔ دیگران بهتر است.
- &x نشانی x است؛ نام یک آرایه در واقع اشاره‌گری به اولین عضو آن است، به همین دلیل تغییر آرایه در تابع، در فراخواننده هم دیده می‌شد.
- *pc یعنی داده‌ای که در نشانی pc پیدا می‌شود. ویدئو آن را به رفتن به خانهٔ همسایه تشبیه می‌کند: دانستن نشانی کافی نیست، باید به آنجا بروی.
- در `int *px, py, pz;` فقط px اشاره‌گر است و py و pz عدد صحیح‌اند.
- رشته در واقع char * است؛ اندازهٔ هر اشاره‌گر، بسته به سیستم، ۴ یا ۸ بایت است (در محیط ۶۴ بیتی CS50 IDE هشت بایت).

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`pointers.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — چرا اشاره‌گر](https://www.youtube.com/watch?v=XISnO2YhnsY&t=0s)
- [۰:۵۰ — ارسال با مقدار](https://www.youtube.com/watch?v=XISnO2YhnsY&t=50s)
- [۳:۲۲ — حافظه: RAM](https://www.youtube.com/watch?v=XISnO2YhnsY&t=202s)
- [۵:۰۹ — حافظه مثل آرایه‌ای از بایت‌ها](https://www.youtube.com/watch?v=XISnO2YhnsY&t=309s)
- [۹:۳۲ — اشاره‌گر فقط یک نشانی است](https://www.youtube.com/watch?v=XISnO2YhnsY&t=572s)
- [۱۴:۵۴ — اشاره‌گر NULL](https://www.youtube.com/watch?v=XISnO2YhnsY&t=894s)
- [۱۷:۳۱ — عملگر & و نام آرایه](https://www.youtube.com/watch?v=XISnO2YhnsY&t=1051s)
- [۱۹:۱۹ — dereference](https://www.youtube.com/watch?v=XISnO2YhnsY&t=1159s)
- [۲۱:۲۱ — dereference کردن NULL](https://www.youtube.com/watch?v=XISnO2YhnsY&t=1281s)
- [۲۴:۱۴ — چند اشاره‌گر در یک خط](https://www.youtube.com/watch?v=XISnO2YhnsY&t=1454s)
- [۲۵:۵۲ — اندازهٔ یک رشته](https://www.youtube.com/watch?v=XISnO2YhnsY&t=1552s)

## مفاهیم مرتبط

- اشاره‌گر: متغیری که نشانی نگه می‌دارد (int *p) — [یادداشت](/kb/d/w04-n04) · درس کوتاه `w04-l02` (واحد `w04-l02-u02`)
- اشاره‌گر NULL: نشانی‌ای که به هیچ‌جا اشاره نمی‌کند — [یادداشت](/kb/d/w04-sh-pointers) · درس کوتاه `w04-l02` (واحد `w04-l02-u03`)
- عملگر & : نشانی یک متغیر — [یادداشت](/kb/d/w04-n04) · درس کوتاه `w04-l02` (واحد `w04-l02-u01`)
- عملگر * : رفتن به نشانی (dereference) — [یادداشت](/kb/d/w04-n04) · درس کوتاه `w04-l02` (واحد `w04-l02-u02`)
- اندازهٔ اشاره‌گر: ۸ بایت در سیستم ۶۴ بیتی — [یادداشت](/kb/d/w04-n04) · درس کوتاه `w04-l02` (واحد `w04-l02-u02`)
- رشته همان char * است: نشانی اولین نویسه — [یادداشت](/kb/d/w04-n05) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)
- جابه‌جایی واقعی با فرستادن نشانی‌ها به تابع — [یادداشت](/kb/d/w04-n12) · درس کوتاه `w04-l06` (واحد `w04-l06-u01`)
- هر بایت حافظه نشانی (address) دارد — [یادداشت](/kb/d/w04-n03) · درس کوتاه `w04-l01` (واحد `w04-l01-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/XISnO2YhnsY) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/pointers/pointers.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/pointers/lang/en/pointers.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/pointers/lang/en/pointers.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
