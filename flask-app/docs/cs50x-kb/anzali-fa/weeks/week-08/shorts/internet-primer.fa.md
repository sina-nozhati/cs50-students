---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-internet-primer
type: short-summary
title: 'ویدئوی کوتاه: مقدمه‌ای بر اینترنت (Internet Primer)'
title_fa: مقدمه‌ای بر اینترنت
title_en: Internet Primer
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/internet_primer/
source_refs:
- src-short-internet-primer
- src-anzali-inference-8
concept_ids:
- w08-c-internet
- w08-c-ip-address
- w08-c-ipv4-ipv6
- w08-c-dhcp
- w08-c-dns
- w08-c-router
prev: w08-sec
next: w08-sh-ip
order: 18
video:
  youtube_id: 04GztBlVo_s
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: از خط فرمان به وب'
    evidence_en: null
  - start: '2:16'
    start_seconds: 136
    title_fa: نشانی IP
    evidence_en: IP address
  - start: '6:11'
    start_seconds: 371
    title_fa: کمبود نشانی و IPv6
    evidence_en: IPv6
  - start: '8:58'
    start_seconds: 538
    title_fa: DHCP
    evidence_en: DHCP
  - start: '10:22'
    start_seconds: 622
    title_fa: DNS
    evidence_en: Domain Name System
  - start: '14:13'
    start_seconds: 853
    title_fa: نقطهٔ دسترسی و مسیریاب
    evidence_en: access points
  - start: '17:43'
    start_seconds: 1063
    title_fa: اینترنت چیست؟
    evidence_en: interconnected network
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: مقدمه‌ای بر اینترنت (Internet Primer)

> **منبع رسمی:** [صفحهٔ Short «Internet Primer» در CS50x](https://cs50.harvard.edu/x/shorts/internet_primer/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو با یک «تغییر فرهنگ» شروع می‌شود: تا اینجا کاربر فقط از راه خط فرمان با برنامه‌هایت کار می‌کرد و از این به بعد با وب‌سایت‌هایت کار می‌کند. داگ لوید یادآوری می‌کند CS50 درس شبکه نیست و این ویدئو فقط یک راهنمای سطح بالاست.

اولین چیزی که برای وصل شدن لازم است **نشانی IP** است: شناسهٔ یکتای دستگاه در شبکه، مثل نشانی پستی خانه. در IPv4 نشانی ۳۲ بیتی است و به شکل `w.x.y.z` نوشته می‌شود، هر عدد از ۰ تا ۲۵۵؛ یعنی کمی بیش از ۴ میلیارد نشانی. چون دستگاه‌ها بیشترند، **نشانی خصوصی** به‌عنوان راه‌حل موقت به کار می‌رود و راه‌حل بلندمدت **IPv6** با ۱۲۸ بیت است که به شکل هشت دستهٔ شانزده‌شانزدهی نوشته می‌شود و دسته‌های صفر را می‌شود با `::` خلاصه کرد (d140).

نشانی را خودت انتخاب نمی‌کنی: **سرور DHCP** از فهرستی که دارد یکی به تو می‌دهد؛ پیش از DHCP این کار دستی بود. **DNS** نام‌های خوانا مثل `cs50.harvard.edu` را به نشانی IP ترجمه می‌کند. ویدئو آن را «دفترچهٔ تلفن وب» می‌نامد، اما دفترچه‌ای محلی: هیچ فهرست کاملی از همهٔ اینترنت در یک جا نیست و DNS میان سرورهای بسیار پخش است.

در خانه، مسیریاب (همراه سوئیچ و نقطهٔ دسترسی، گاهی مودم) تنها دستگاهی است که نشانی عمومی دارد و مثل پلیس راهنمایی‌ورانندگی ترافیک دستگاه‌های خانه را جابه‌جا می‌کند. در پایان، خود **اینترنت** را تعریف می‌کند: یک ابر جدا نیست، بلکه مجموعهٔ قاعده‌هایی است که شبکه‌های کوچک را به هم وصل می‌کند.

## نکته‌های کلیدی

- نشانی IPv4 چهار عدد ۰ تا ۲۵۵ است، روی هم ۳۲ بیت و حدود ۴ میلیارد نشانی.
- IPv6 ۱۲۸ بیت است و به شکل شانزده‌شانزدهی نوشته می‌شود؛ `::` جای دسته‌های صفر را می‌گیرد.
- DHCP نشانی می‌دهد؛ DNS نام را به نشانی ترجمه می‌کند.
- DNS متمرکز نیست؛ میان سرورهای زیادی پخش است.
- مسیریاب خانه با یک نشانی عمومی، ترافیک نشانی‌های خصوصی را جابه‌جا می‌کند.
- اینترنت یعنی شبکه‌های به‌هم‌پیوسته و قاعده‌هایی که گفت‌وگویشان را ممکن می‌کند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`internet_primer.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: از خط فرمان به وب](https://www.youtube.com/watch?v=04GztBlVo_s&t=0s)
- [۲:۱۶ — نشانی IP](https://www.youtube.com/watch?v=04GztBlVo_s&t=136s)
- [۶:۱۱ — کمبود نشانی و IPv6](https://www.youtube.com/watch?v=04GztBlVo_s&t=371s)
- [۸:۵۸ — DHCP](https://www.youtube.com/watch?v=04GztBlVo_s&t=538s)
- [۱۰:۲۲ — DNS](https://www.youtube.com/watch?v=04GztBlVo_s&t=622s)
- [۱۴:۱۳ — نقطهٔ دسترسی و مسیریاب](https://www.youtube.com/watch?v=04GztBlVo_s&t=853s)
- [۱۷:۴۳ — اینترنت چیست؟](https://www.youtube.com/watch?v=04GztBlVo_s&t=1063s)

> [!NOTE]
> **یادداشت (d140، d141)**
> این ویدئو در ۲۰۱۷ ضبط شده و از نوشتن وب‌سایت با PHP حرف می‌زند؛ CS50x 2026 به جای آن پایتون و Flask را در هفتهٔ ۹ درس می‌دهد. همچنین می‌گوید IPv6 «هشت دستهٔ ۱۶ بایتی» است؛ درستش هشت دستهٔ ۱۶ **بیتی** است که روی هم ۱۲۸ بیت می‌شود.

> [!TIP]
> **نکته (d145)**
> درس‌نامه می‌گوید هر رایانه نشانی یکتایی دارد؛ این ویدئو دقیق‌ترش می‌کند: پشت یک مسیریاب خانگی، دستگاه‌ها نشانی خصوصی دارند و با یک نشانی عمومی مشترک بیرون می‌روند.

## مفاهیم مرتبط

- اینترنت: شبکه‌ای که رایانه‌های سراسر جهان را به هم وصل می‌کند — [یادداشت](/kb/d/w08-n01) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- نشانی IP به شکل #.#.#.# با عددهای ۰ تا ۲۵۵ — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- IPv4 با ۳۲ بیت و IPv6 با ۱۲۸ بیت — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)
- DHCP: گرفتن نشانی IP دستگاه به‌طور خودکار — [یادداشت](/kb/d/w08-n05) · درس کوتاه `w08-l01` (واحد `w08-l01-u03`)
- DNS: تبدیل نام دامنه به نشانی IP — [یادداشت](/kb/d/w08-n04) · درس کوتاه `w08-l01` (واحد `w08-l01-u03`)
- مسیریاب (router) و تصمیم مسیریابی — [یادداشت](/kb/d/w08-n02) · درس کوتاه `w08-l01` (واحد `w08-l01-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/04GztBlVo_s) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/internet_primer/internet_primer.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/internet_primer/lang/en/internet_primer.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/internet_primer/lang/en/internet_primer.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
