---
week: 9
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:45+03:30'
verified_at: '2026-10-29T17:05:00+03:30'
generated_at: '2026-10-29T18:00:00+03:30'
review_status: draft-needs-human-review
id: w09-sh-ajax
type: short-summary
title: 'ویدئوی کوتاه: Ajax (AJAX)'
title_fa: Ajax
title_en: AJAX
parent: w09-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/ajax/
source_refs:
- src-short-ajax
- src-anzali-inference-9
concept_ids:
- w09-c-ajax
- w09-c-xmlhttprequest
- w09-c-json
- w09-c-partial-template
- w09-c-api
prev: w09-sh-flask
next: w09-ps-birthdays
order: 19
video:
  youtube_id: dQcBs4S-wEQ
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: از کار سمت کاربر به گفت‌وگو با سرور
    evidence_en: null
  - start: 0:10
    start_seconds: 10
    title_fa: Ajax چیست؟
    evidence_en: Ajax
  - start: '1:11'
    start_seconds: 71
    title_fa: 'نمونه‌ها: امتیاز زنده و ایمیل'
    evidence_en: sports
  - start: '2:22'
    start_seconds: 142
    title_fa: شیء XMLHttpRequest
    evidence_en: XMLHttpRequest
  - start: '3:00'
    start_seconds: 180
    title_fa: onreadystatechange
    evidence_en: onreadystatechange
  - start: '4:29'
    start_seconds: 269
    title_fa: readyState ۴ و status ۲۰۰
    evidence_en: '200'
  - start: '5:45'
    start_seconds: 345
    title_fa: یک تابع کامل Ajax
    evidence_en: preparing
  - start: '7:30'
    start_seconds: 450
    title_fa: 'نمونهٔ عملی: Ajax test'
    evidence_en: Ajax test
  - start: '8:02'
    start_seconds: 482
    title_fa: ajax.js و infodiv
    evidence_en: infodiv
  - start: '11:31'
    start_seconds: 691
    title_fa: اجرا و جمع‌بندی
    evidence_en: Zamyla
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: Ajax (AJAX)

> **منبع رسمی:** [صفحهٔ Short «AJAX» در CS50x](https://cs50.harvard.edu/x/shorts/ajax/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

تا اینجا هر کار جاوااسکریپت سمت کاربر بود: کلیک روی دکمه و تغییر رنگ یا متن، بی‌آنکه با جهان بیرون حرف بزنیم. **Ajax** اجازه می‌دهد از درون صفحه با سرور حرف بزنیم و فقط بخشی از صفحه را به‌روز کنیم، نه کل آن را؛ مثل امتیازهای زندهٔ یک سایت ورزشی یا ایمیل تازه‌ای که بالای صندوق ظاهر می‌شود. نامش زمانی کوتاه‌شدهٔ Asynchronous JavaScript and XML بود، اما امروز به جای XML بیشتر JSON به کار می‌رود.

ویدئو روش «خالص» جاوااسکریپتِ آن زمان را نشان می‌دهد: ساختن یک شیء `XMLHttpRequest`، تعریف یک تابع بی‌نام برای `onreadystatechange`، و منتظر ماندن تا `readyState` به ۴ (پایان) و `status` به ۲۰۰ (OK) برسد؛ سپس `open` با روش GET و یک نشانی، و `send`. یادآوری می‌کند که همین کار را اغلب با jQuery می‌نویسند.

در نمونهٔ عملی، یک منوی کشویی با رویداد `onchange` تابع `cs50info(this.value)` را صدا می‌زند؛ تابع فایل `name + ".html"` را می‌خواهد (یک تکه HTML بدون `<html>` و `<body>`) و با jQuery آن را درون `div` با شناسهٔ `infodiv` می‌گذارد. با انتخاب نام‌های دیگر فقط همان بخش عوض می‌شود و بقیهٔ صفحه سر جایش می‌ماند.

## نکته‌های کلیدی

- Ajax یعنی درخواست به سرور از درون صفحه، بدون بارگذاری دوبارهٔ کل صفحه.
- امروز بیشتر JSON منتقل می‌شود تا XML.
- `readyState` از ۰ تا ۴ است؛ ۴ یعنی پاسخ کامل رسیده.
- `status` برابر ۲۰۰ یعنی OK.
- پاسخ می‌تواند یک تکه HTML باشد که درون یک عنصر گذاشته می‌شود.
- درخواست‌ها می‌توانند به سرور خودت یا سرورهای دیگر بروند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`ajax.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — از کار سمت کاربر به گفت‌وگو با سرور](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=0s)
- [۰:۱۰ — Ajax چیست؟](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=10s)
- [۱:۱۱ — نمونه‌ها: امتیاز زنده و ایمیل](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=71s)
- [۲:۲۲ — شیء XMLHttpRequest](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=142s)
- [۳:۰۰ — onreadystatechange](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=180s)
- [۴:۲۹ — readyState ۴ و status ۲۰۰](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=269s)
- [۵:۴۵ — یک تابع کامل Ajax](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=345s)
- [۷:۳۰ — نمونهٔ عملی: Ajax test](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=450s)
- [۸:۰۲ — ajax.js و infodiv](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=482s)
- [۱۱:۳۱ — اجرا و جمع‌بندی](https://www.youtube.com/watch?v=dQcBs4S-wEQ&t=691s)

> [!NOTE]
> **یادداشت (d169)**
> این ویدئو در ۲۰۱۷ ضبط شده و Ajax را با `XMLHttpRequest` و jQuery نشان می‌دهد. سخنرانی CS50x 2026 همین ایده را با `fetch` و `await` پیاده می‌کند ([یادداشت shows](/kb/d/w09-n14)) که کوتاه‌تر است و jQuery لازم ندارد.

> [!TIP]
> **نکته (تألیفی)**
> قالب `search.html` در shows2 دقیقاً همان «تکه HTML»ی است که این ویدئو با `name + ".html"` می‌گیرد؛ و shows3 به جای HTML، JSON برمی‌گرداند تا مرورگر خودش HTML را بسازد.

## مفاهیم مرتبط

- Ajax: درخواست از جاوااسکریپت بدون بارگذاری دوبارهٔ صفحه — [یادداشت](/kb/d/w09-n14) · درس کوتاه `w09-l07` (واحد `w09-l07-u02`)
- XMLHttpRequest، readyState 4 و status 200 (روش قدیمی Ajax) — [یادداشت](/kb/d/w09-sh-ajax)
- JSON: نمایش متنی کلید و مقدار برای داده — [یادداشت](/kb/d/w09-n15) · درس کوتاه `w09-l07` (واحد `w09-l07-u02`)
- قالب تکه‌ای (فقط چند li) که درون صفحهٔ موجود نشانده می‌شود — [یادداشت](/kb/d/w09-n14) · درس کوتاه `w09-l07` (واحد `w09-l07-u01`)
- API: مشخصاتی برای کار با یک خدمت دیگر — [یادداشت](/kb/d/w09-n14) · درس کوتاه `w09-l07` (واحد `w09-l07-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/dQcBs4S-wEQ) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/ajax/ajax.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/ajax/lang/en/ajax.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/ajax/lang/en/ajax.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
