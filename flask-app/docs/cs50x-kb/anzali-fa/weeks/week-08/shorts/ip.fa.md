---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-ip
type: short-summary
title: 'ویدئوی کوتاه: IP (IP)'
title_fa: IP
title_en: IP
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/ip/
source_refs:
- src-short-ip
- src-anzali-inference-8
concept_ids:
- w08-c-router
- w08-c-packet
- w08-c-protocol
- w08-c-ip-address
- w08-c-fragmentation
prev: w08-sh-internet-primer
next: w08-sh-tcp
order: 19
video:
  youtube_id: A1g9SokDJSU
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: پروتکل اینترنت'
    evidence_en: null
  - start: '1:18'
    start_seconds: 78
    title_fa: هزینهٔ سیم‌کشی همه به همه
    evidence_en: physical wired connection
  - start: '3:25'
    start_seconds: 205
    title_fa: مسیریاب و جدول مسیریابی
    evidence_en: routing table
  - start: '8:15'
    start_seconds: 495
    title_fa: یک پیام از شبکهٔ ۱ تا ۵
    evidence_en: send a message to you
  - start: '11:11'
    start_seconds: 671
    title_fa: شکستن داده به بسته‌ها
    evidence_en: split this data into packets
  - start: '12:54'
    start_seconds: 774
    title_fa: پروتکل بی‌اتصال
    evidence_en: connection, less protocol
  - start: '15:14'
    start_seconds: 914
    title_fa: رسیدن تضمین‌نشده
    evidence_en: doesn't guarantee delivery
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: IP (IP)

> **منبع رسمی:** [صفحهٔ Short «IP» در CS50x](https://cs50.harvard.edu/x/shorts/ip/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

IP (Internet Protocol) نخستین پروتکلی است که اینترنت را می‌سازد: قاعدهٔ جابه‌جا کردن اطلاعات از نقطهٔ A به B، و پذیرفتنش شرط پیوستن به اینترنت است. داگ لوید نشان می‌دهد وصل کردن مستقیم همهٔ شبکه‌ها به هم با سیم ممکن نیست: با شش شبکه هم سیم‌کشی زیاد است، چه رسد به شبکه‌هایی آن سوی اقیانوس.

راه‌حل **مسیریاب** است. هر مسیریاب یک **جدول مسیریابی** دارد: «اگر نشانی با ۴ شروع شد، از این طرف بفرست». مسیریاب بسته را به مقصد نمی‌رساند؛ فقط یک گام نزدیک‌ترش می‌کند و بقیه را به مسیریاب بعدی می‌سپارد، شبیه بازگشت (recursion) در C. ویدئو یک پیام را از شبکهٔ ۱ تا شبکهٔ ۵ گام‌به‌گام دنبال می‌کند.

IP داده را به **بسته‌ها** می‌شکند، چون یک تکهٔ بزرگ مثل کامیونی است که همهٔ ترافیک پشتش گیر می‌کند، و اگر گم شود باید همه‌اش دوباره فرستاده شود. IP **بی‌اتصال** است: مسیر ثابتی وجود ندارد و اگر جدول‌ها چند گزینه داشته باشند، بسته‌های یک پیام ممکن است از راه‌های مختلف بروند، مثل GPS که از ترافیک دوری می‌کند. اما IP رسیدن بسته را تضمین نمی‌کند؛ این کار TCP است.

## نکته‌های کلیدی

- وصل کردن مستقیم همهٔ شبکه‌ها به هم ممکن نیست؛ مسیریاب‌ها واسطه‌اند.
- هر مسیریاب با جدول مسیریابی بسته را یک گام به مقصد نزدیک‌تر می‌کند.
- IP داده را به بسته‌های کوچک می‌شکند تا شبکه بند نیاید و گم شدن یک بسته ارزان باشد.
- IP بی‌اتصال است: بسته‌های یک پیام ممکن است از مسیرهای متفاوت بروند.
- IP رسیدن بسته را تضمین نمی‌کند؛ TCP این کار را می‌کند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`ip.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: پروتکل اینترنت](https://www.youtube.com/watch?v=A1g9SokDJSU&t=0s)
- [۱:۱۸ — هزینهٔ سیم‌کشی همه به همه](https://www.youtube.com/watch?v=A1g9SokDJSU&t=78s)
- [۳:۲۵ — مسیریاب و جدول مسیریابی](https://www.youtube.com/watch?v=A1g9SokDJSU&t=205s)
- [۸:۱۵ — یک پیام از شبکهٔ ۱ تا ۵](https://www.youtube.com/watch?v=A1g9SokDJSU&t=495s)
- [۱۱:۱۱ — شکستن داده به بسته‌ها](https://www.youtube.com/watch?v=A1g9SokDJSU&t=671s)
- [۱۲:۵۴ — پروتکل بی‌اتصال](https://www.youtube.com/watch?v=A1g9SokDJSU&t=774s)
- [۱۵:۱۴ — رسیدن تضمین‌نشده](https://www.youtube.com/watch?v=A1g9SokDJSU&t=914s)

> [!NOTE]
> **یادداشت (d144)**
> متن گفتار ویدئوی TCP می‌گوید IP «پروتکل با اتصال» است؛ همین ویدئو روشن می‌گوید IP بی‌اتصال (connectionless) است و درستش همین است.

## مفاهیم مرتبط

- مسیریاب (router) و تصمیم مسیریابی — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- بستهٔ داده (packet) که از مسیریابی به مسیریاب دیگر می‌رود — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- پروتکل: قراردادی برای تبادل داده — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- نشانی IP به شکل #.#.#.# با عددهای ۰ تا ۲۵۵ — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- تکه‌تکه کردن فایل بزرگ به چند بسته — [یادداشت](/kb/d/w08-n03) · درس کوتاه `w08-l01` (واحد `w08-l01-u02`)

## منابع

- [ویدئو در YouTube](https://youtu.be/A1g9SokDJSU) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/ip/ip.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/ip/lang/en/ip.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/ip/lang/en/ip.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
