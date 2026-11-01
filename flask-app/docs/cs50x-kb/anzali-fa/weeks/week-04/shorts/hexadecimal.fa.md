---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-sh-hexadecimal
type: short-summary
title: 'ویدئوی کوتاه: مبنای شانزده (Hexadecimal)'
title_fa: مبنای شانزده
title_en: Hexadecimal
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/hexadecimal/
source_refs:
- src-short-hexadecimal
- src-anzali-inference-4
concept_ids:
- w04-c-hexadecimal
- w04-c-hex-place-values
- w04-c-hex-byte
- w04-c-0x-prefix
- w04-c-memory-addresses
prev: w04-sec
next: w04-sh-pointers
order: 18
video:
  youtube_id: u_atXp-NF6w
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: چرا یک مبنای دیگر
    evidence_en: null
  - start: '1:23'
    start_seconds: 83
    title_fa: مبنای ۱۶ و رقم‌هایش
    evidence_en: the hexadecimal system, which is base 16
  - start: '2:42'
    start_seconds: 162
    title_fa: هر رقم = ۴ بیت
    evidence_en: each hexadecimal digit corresponds to a unique arrangement
  - start: '3:25'
    start_seconds: 205
    title_fa: پیشوند 0x
    evidence_en: prefix them with the prefix 0x
  - start: '4:15'
    start_seconds: 255
    title_fa: ارزش مکانی
    evidence_en: It also has place values
  - start: '7:11'
    start_seconds: 431
    title_fa: تبدیل دودویی به هگزادسیمال
    evidence_en: let's go to that conversion process
  - start: '8:55'
    start_seconds: 535
    title_fa: 'کاربرد: نشانی‌های حافظه'
    evidence_en: memory addresses in our system are represented in hexadecimal
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: مبنای شانزده (Hexadecimal)

> **منبع رسمی:** [صفحهٔ Short «Hexadecimal» در CS50x](https://cs50.harvard.edu/x/shorts/hexadecimal/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو توضیح می‌دهد چرا به یک مبنای دیگر نیاز داریم: رشته‌های بلند 0 و 1 برای انسان سخت خوانده می‌شوند، و هگزادسیمال (مبنای ۱۶) همان اطلاعات دودویی را کوتاه‌تر و خواناتر نشان می‌دهد.

ویدئو رقم‌ها و ارزش مکانی هگزادسیمال را مرور می‌کند، یک عدد دودویی ۳۲ رقمی را با گروه‌بندی چهارتایی به هشت رقم هگزادسیمال تبدیل می‌کند و در پایان می‌گوید کاربرد اصلی آن برای ما نشان دادن نشانی‌های حافظه است.

## نکته‌های کلیدی

- رقم‌های هگزادسیمال 0 تا 9 و a تا f هستند؛ a تا f یعنی 10 تا 15. حرف کوچک یا بزرگ فرقی ندارد.
- چون ۱۶ توانی از ۲ است، هر رقم هگزادسیمال دقیقاً با یک ترکیب ۴ بیتی متناظر است؛ مثلاً 0000 یعنی 0، 0110 یعنی 6 و 1111 یعنی f.
- پیشوند 0x به‌خودی‌خود معنایی ندارد؛ فقط به انسان می‌گوید عدد بعدی هگزادسیمال است و آن را از دهدهی جدا می‌کند.
- ارزش‌های مکانی توان‌های ۱۶اند: یکان، ۱۶تایی، ۲۵۶تایی و الی آخر؛ پس 0x397 همان 397 دهدهی نیست.
- برای تبدیل دودویی به هگزادسیمال، رقم‌ها را از راست به چپ چهارتا چهارتا گروه کن؛ نمونهٔ ویدئو به 0x46a2b93d می‌رسد.
- ویدئو می‌گوید احتمالاً با هگزادسیمال حساب نمی‌کنیم؛ بیشتر برای بیان و فهم نشانی‌های حافظه به کار می‌آید.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`hexadecimal.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — چرا یک مبنای دیگر](https://www.youtube.com/watch?v=u_atXp-NF6w&t=0s)
- [۱:۲۳ — مبنای ۱۶ و رقم‌هایش](https://www.youtube.com/watch?v=u_atXp-NF6w&t=83s)
- [۲:۴۲ — هر رقم = ۴ بیت](https://www.youtube.com/watch?v=u_atXp-NF6w&t=162s)
- [۳:۲۵ — پیشوند 0x](https://www.youtube.com/watch?v=u_atXp-NF6w&t=205s)
- [۴:۱۵ — ارزش مکانی](https://www.youtube.com/watch?v=u_atXp-NF6w&t=255s)
- [۷:۱۱ — تبدیل دودویی به هگزادسیمال](https://www.youtube.com/watch?v=u_atXp-NF6w&t=431s)
- [۸:۵۵ — کاربرد: نشانی‌های حافظه](https://www.youtube.com/watch?v=u_atXp-NF6w&t=535s)

## مفاهیم مرتبط

- مبنای شانزده: رقم‌های 0 تا 9 و A تا F — [یادداشت](/kb/d/w04-n02) · درس کوتاه `w04-l01` (واحد `w04-l01-u02`)
- ارزش مکانی در مبنای شانزده: 1، 16، 256 — [یادداشت](/kb/d/w04-n02) · درس کوتاه `w04-l01` (واحد `w04-l01-u02`)
- هر رقم هگزادسیمال ۴ بیت است و دو رقم یک بایت؛ FF یعنی 255 — [یادداشت](/kb/d/w04-n02) · درس کوتاه `w04-l01` (واحد `w04-l01-u02`)
- پیشوند 0x برای نوشتن عدد هگزادسیمال — [یادداشت](/kb/d/w04-n03) · درس کوتاه `w04-l01` (واحد `w04-l01-u03`)
- هر بایت حافظه نشانی (address) دارد — [یادداشت](/kb/d/w04-n03) · درس کوتاه `w04-l01` (واحد `w04-l01-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/u_atXp-NF6w) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/hexadecimal/hexadecimal.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
