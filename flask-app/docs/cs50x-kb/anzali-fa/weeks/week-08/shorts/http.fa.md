---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-http
type: short-summary
title: 'ویدئوی کوتاه: HTTP (HTTP)'
title_fa: HTTP
title_en: HTTP
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/http/
source_refs:
- src-short-http
- src-anzali-inference-8
concept_ids:
- w08-c-http
- w08-c-get-post
- w08-c-headers
- w08-c-status-codes
- w08-c-devtools-network
- w08-c-url
prev: w08-sh-tcp
next: w08-sh-html
order: 21
video:
  youtube_id: 4axL8Gfw2nI
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: پروتکل لایهٔ کاربرد'
    evidence_en: null
  - start: '2:47'
    start_seconds: 167
    title_fa: درخواست و پاسخ ساده
    evidence_en: GET/HTTP/1.1
  - start: '5:17'
    start_seconds: 317
    title_fa: 404 Not Found
    evidence_en: 404 Not Found
  - start: '6:10'
    start_seconds: 370
    title_fa: خط درخواست
    evidence_en: request line
  - start: '8:36'
    start_seconds: 516
    title_fa: کدهای موفقیت و تغییر مسیر
    evidence_en: 301 Moved Permanently
  - start: '9:37'
    start_seconds: 577
    title_fa: خطاهای کاربر
    evidence_en: 401 Unauthorized
  - start: '10:40'
    start_seconds: 640
    title_fa: خطاهای سرور
    evidence_en: 500 Internal Server Error
  - start: '11:32'
    start_seconds: 692
    title_fa: ابزار توسعه‌دهنده
    evidence_en: Developer Tools
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: HTTP (HTTP)

> **منبع رسمی:** [صفحهٔ Short «HTTP» در CS50x](https://cs50.harvard.edu/x/shorts/http/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

IP و TCP داده را به دستگاه و برنامهٔ درست می‌رسانند، اما برنامهٔ گیرنده هم باید بداند با داده چه کند. HTTP (Hypertext Transfer Protocol) یک پروتکل **لایهٔ کاربرد** است: قاعدهٔ اینکه درخواست صفحهٔ وب چه شکلی باشد و سرور چطور پاسخ بدهد، مثل قالب نامهٔ اداری. نمونه‌های دیگر این لایه FTP، SMTP و RDP هستند.

درخواست با یک **خط درخواست** شروع می‌شود: روش، هدف و نسخه، مثل `GET / HTTP/1.1`، و خط بعد `Host: www.cats.com`. هدف و میزبان روی هم منبع را مشخص می‌کنند. پاسخ موفق `HTTP/1.1 200 OK` است، همراه نوع محتوا و خود HTML. اگر `cats.html` نباشد، پاسخ `404 Not Found` است.

ویدئو کدهای وضعیت رایج را مرور می‌کند: `200 OK`؛ تغییر مسیر `301 Moved Permanently` و `302 Found` که مرورگر خودکار دنبالشان می‌کند؛ خطای کاربر `401 Unauthorized` (باید وارد شوی)، `403 Forbidden` (اجازه نداری، چه وارد شده باشی چه نه) و `404 Not Found`؛ و خطای سرور `500 Internal Server Error`، `503 Service Unavailable` و `504 Gateway Timeout`. در پایان با زبانهٔ Network در ابزار توسعه‌دهندهٔ کروم (F12) کدهای `200` و `302` درخواست به گوگل و `301` درخواست به `thefacebook.com` را نشان می‌دهد.

## نکته‌های کلیدی

- HTTP پروتکل لایهٔ کاربرد است: قالب درخواست و پاسخ وب.
- خط درخواست: روش، هدف و نسخه، مثل `GET /cats.html HTTP/1.1`؛ سپس `Host`.
- ۲xx موفقیت، ۳xx تغییر مسیر، ۴xx خطای درخواست، ۵xx خطای سرور.
- `401` یعنی باید وارد شوی؛ `403` یعنی در هر حال اجازه نداری.
- کدهای پنهان را در زبانهٔ Network ابزار توسعه‌دهنده می‌بینی.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`http.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: پروتکل لایهٔ کاربرد](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=0s)
- [۲:۴۷ — درخواست و پاسخ ساده](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=167s)
- [۵:۱۷ — 404 Not Found](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=317s)
- [۶:۱۰ — خط درخواست](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=370s)
- [۸:۳۶ — کدهای موفقیت و تغییر مسیر](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=516s)
- [۹:۳۷ — خطاهای کاربر](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=577s)
- [۱۰:۴۰ — خطاهای سرور](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=640s)
- [۱۱:۳۲ — ابزار توسعه‌دهنده](https://www.youtube.com/watch?v=4axL8Gfw2nI&t=692s)

> [!NOTE]
> **یادداشت (d135، d153)**
> ویدئو می‌گوید نسخهٔ HTTP «احتمالاً همیشه» 1.1 است؛ در سخنرانی ۲۰۲۵ پاسخ‌ها `HTTP/2` هستند. همچنین ویدئو خطای ۵۰۰ را کوتاهی سرور می‌نامد، در حالی که درس‌نامه می‌گوید وقتی برنامه مال خودت است، ۵۰۰ معمولاً تقصیر خود توسعه‌دهنده است.

## مفاهیم مرتبط

- HTTP: پروتکل سطح کاربرد برای انتقال صفحه‌ها — [یادداشت](/kb/d/w08-n06) · درس کوتاه `w08-l02` (واحد `w08-l02-u01`)
- درخواست‌های GET و POST — [یادداشت](/kb/d/w08-n06) · درس کوتاه `w08-l02` (واحد `w08-l02-u01`)
- سرآیندهای درخواست و پاسخ (Host، Content-Type) — [یادداشت](/kb/d/w08-n06) · درس کوتاه `w08-l02` (واحد `w08-l02-u01`)
- کدهای وضعیت: 200، 301، 404، 500 و دیگران — [یادداشت](/kb/d/w08-n06) · درس کوتاه `w08-l02` (واحد `w08-l02-u02`)
- ابزار توسعه‌دهندهٔ مرورگر: زبانهٔ Network — [یادداشت](/kb/d/w08-n06) · درس کوتاه `w08-l02` (واحد `w08-l02-u02`)
- اجزای نشانی: پروتکل، دامنه، دامنهٔ سطح بالا و مسیر — [یادداشت](/kb/d/w08-n06) · درس کوتاه `w08-l02` (واحد `w08-l02-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/4axL8Gfw2nI) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/http/http.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/http/lang/en/http.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/http/lang/en/http.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
