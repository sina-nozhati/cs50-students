---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-tcp
type: short-summary
title: 'ویدئوی کوتاه: TCP (TCP)'
title_fa: TCP
title_en: TCP
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/tcp/
source_refs:
- src-short-tcp
- src-anzali-inference-8
concept_ids:
- w08-c-tcp
- w08-c-port
- w08-c-retransmission
- w08-c-packet-header
prev: w08-sh-ip
next: w08-sh-http
order: 20
video:
  youtube_id: GP7uvI_6uas
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: کار TCP'
    evidence_en: null
  - start: '1:14'
    start_seconds: 74
    title_fa: TCP/IP و تضمین رسیدن
    evidence_en: TCP/IP
  - start: '1:51'
    start_seconds: 111
    title_fa: شمارهٔ درگاه
    evidence_en: port number
  - start: '3:01'
    start_seconds: 181
    title_fa: درگاه‌های استاندارد
    evidence_en: port 21
  - start: '4:06'
    start_seconds: 246
    title_fa: لایه‌ها مثل عروسک تودرتو
    evidence_en: nesting dolls
  - start: '5:14'
    start_seconds: 314
    title_fa: مثال ایمیل چهاربسته‌ای
    evidence_en: send an email
  - start: '7:46'
    start_seconds: 466
    title_fa: بستهٔ گم‌شده
    evidence_en: packet number two is missing
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: TCP (TCP)

> **منبع رسمی:** [صفحهٔ Short «TCP» در CS50x](https://cs50.harvard.edu/x/shorts/tcp/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

IP بسته را به **دستگاه** درست می‌رساند، اما روی یک دستگاه برنامه‌ها و خدمات زیادی اجرا می‌شوند. TCP (Transmission Control Protocol) بسته را به **برنامهٔ** درست می‌رساند و چیزی را تضمین می‌کند که IP تضمین نمی‌کند: رسیدن همهٔ داده. چون این دو همیشه با هم کار می‌کنند، معمولاً TCP/IP خوانده می‌شوند.

نشانی IP به‌علاوهٔ **شمارهٔ درگاه** (port) یک خدمت خاص روی یک دستگاه خاص را مشخص می‌کند. چند درگاه استاندارد: FTP ۲۱، ایمیل (SMTP) ۲۵، DNS ۵۳، وب ۸۰ و وب امن ۴۴۳. TCP روی هر تکهٔ داده درگاه و شمارهٔ بسته (مثلاً «۸ از ۱۵») را می‌نویسد و IP دور آن نشانی مقصد و فرستنده را می‌پیچد، مثل عروسک‌های تودرتو. گیرنده لایه‌ها را یکی‌یکی باز می‌کند.

مثال ویدئو یک ایمیل چهاربسته‌ای (A تا D) است. بسته‌ها ممکن است نامرتب برسند، چون IP بی‌اتصال است؛ TCP آن‌ها را سر جایشان می‌گذارد. اگر بستهٔ ۲ نرسد، TCP از روی نشانی برگشت، فقط همان بسته را دوباره درخواست می‌کند، نه کل ایمیل را، و وقتی هر چهار بسته رسیدند داده را به درگاه ۲۵ تحویل می‌دهد.

## نکته‌های کلیدی

- IP دستگاه را پیدا می‌کند؛ TCP برنامه یا خدمت درست را.
- IP + شمارهٔ درگاه یک خدمت یکتا را مشخص می‌کند.
- درگاه‌های رایج: ۲۱ FTP، ۲۵ SMTP، ۵۳ DNS، ۸۰ HTTP، ۴۴۳ HTTPS.
- TCP بسته‌ها را شماره می‌زند تا گیرنده آن‌ها را به ترتیب بچیند.
- بستهٔ گم‌شده دوباره درخواست می‌شود، فقط همان یکی.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`tcp.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: کار TCP](https://www.youtube.com/watch?v=GP7uvI_6uas&t=0s)
- [۱:۱۴ — TCP/IP و تضمین رسیدن](https://www.youtube.com/watch?v=GP7uvI_6uas&t=74s)
- [۱:۵۱ — شمارهٔ درگاه](https://www.youtube.com/watch?v=GP7uvI_6uas&t=111s)
- [۳:۰۱ — درگاه‌های استاندارد](https://www.youtube.com/watch?v=GP7uvI_6uas&t=181s)
- [۴:۰۶ — لایه‌ها مثل عروسک تودرتو](https://www.youtube.com/watch?v=GP7uvI_6uas&t=246s)
- [۵:۱۴ — مثال ایمیل چهاربسته‌ای](https://www.youtube.com/watch?v=GP7uvI_6uas&t=314s)
- [۷:۴۶ — بستهٔ گم‌شده](https://www.youtube.com/watch?v=GP7uvI_6uas&t=466s)

> [!NOTE]
> **یادداشت (d144)**
> در متن گفتار آمده IP «پروتکل با اتصال» است و برای همین بسته‌ها از مسیرهای مختلف می‌روند. منظور «بی‌اتصال» (connectionless) است، همان که ویدئوی IP می‌گوید.

## مفاهیم مرتبط

- TCP: پی‌گیری ترتیب بسته‌ها و تحویل مطمئن — [یادداشت](/kb/d/w08-n03) · درس کوتاه `w08-l01` (واحد `w08-l01-u02`)
- شمارهٔ درگاه (port): ۸۰ برای HTTP و ۴۴۳ برای HTTPS — [یادداشت](/kb/d/w08-n03) · درس کوتاه `w08-l01` (واحد `w08-l01-u02`)
- درخواست دوبارهٔ بستهٔ گم‌شده و تأیید دریافت — [یادداشت](/kb/d/w08-n03) · درس کوتاه `w08-l01` (واحد `w08-l01-u02`)
- سرآیند بسته: نشانی مبدأ و مقصد درون هر بسته — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/GP7uvI_6uas) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/tcp/tcp.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
