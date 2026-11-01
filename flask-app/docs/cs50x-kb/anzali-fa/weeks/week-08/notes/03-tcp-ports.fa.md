---
id: w08-n03
type: note
title: 'TCP، شمارهٔ درگاه و بسته‌های گم‌شده (Routers: TCP and Ports)'
title_fa: TCP، شمارهٔ درگاه و بسته‌های گم‌شده
title_en: 'Routers: TCP and Ports'
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Routers
official_anchor: routers
source_url: https://cs50.harvard.edu/x/2026/notes/8/#routers
source_refs:
- src-notes-8#routers
- src-transcript-8
- src-short-tcp
- src-packet-video-8
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-tcp
- w08-c-port
- w08-c-fragmentation
- w08-c-retransmission
prev: w08-n02
next: w08-n04
order: 3
video:
  youtube_id: yYst7puZXjw
  start: '11:13'
  start_seconds: 673
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=673s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase "there's another protocol in TCP IP"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# TCP، شمارهٔ درگاه و بسته‌های گم‌شده

> **منبع رسمی:** بخش «Routers» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#routers). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۱:۱۳ تا حدود ۱۷:۰۶](https://www.youtube.com/watch?v=yYst7puZXjw&t=673s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

یک رایانه هم‌زمان چند خدمت دارد: وب، ایمیل، تماس تصویری. نشانی IP فقط می‌گوید بسته به کدام رایانه برود؛ هنوز معلوم نیست به کدام برنامه. از طرف دیگر بسته‌ها ممکن است گم شوند یا نامرتب برسند. **TCP** هر دو مشکل را حل می‌کند.

## TCP

- **TCP** یا **پروتکل کنترل انتقال** (`transmission control protocol`) کمک می‌کند ترتیب بسته‌هایی که فرستاده می‌شوند پی‌گیری شود.
- TCP همچنین خدمات وب را از هم جدا می‌کند. برای نمونه، `80` برای HTTP و `443` برای HTTPS به کار می‌رود. این عددها **شمارهٔ درگاه** (`port`) پیش‌فرض این خدمات‌اند.
- وقتی اطلاعات از جایی به جای دیگر فرستاده می‌شود، نشانی IP مبدأ، نشانی IP مقصد و یک شمارهٔ درگاه TCP فرستاده می‌شود.

> [!NOTE]
> **از ویدئوی کوتاه: درگاه‌های رایج دیگر**
> داگ لوید در [ویدئوی TCP](/kb/d/w08-sh-tcp) چند درگاه استاندارد دیگر را هم نام می‌برد: FTP روی ۲۱، ایمیل (SMTP) روی ۲۵ و DNS روی ۵۳. نشانی IP به‌علاوهٔ شمارهٔ درگاه، یک خدمت مشخص روی یک رایانهٔ مشخص را یکتا می‌کند.

## تکه‌تکه کردن و بسته‌های گم‌شده

- این پروتکل‌ها برای تقسیم فایل‌های بزرگ به چند بخش یا بسته هم به کار می‌روند. مثلاً عکس بزرگ یک گربه را می‌توان در چند بسته فرستاد. اگر بسته‌ای گم شود، TCP/IP می‌تواند بسته‌های گم‌شده را دوباره از سرور مبدأ درخواست کند.
- TCP وقتی همهٔ داده فرستاده و دریافت شد، این را **تأیید** (acknowledge) می‌کند.

> [!TIP]
> **از ویدئوی کوتاه: پاکت درون پاکت**
> داگ لوید فرستادن ایمیلی چهاربسته‌ای را دنبال می‌کند. TCP روی هر تکه می‌نویسد «درگاه ۲۵، بستهٔ ۱ از ۴»، و IP دور آن نشانی رایانهٔ مقصد را می‌پیچد. گیرنده لایهٔ IP را برمی‌دارد، لایهٔ TCP را می‌خواند و تکه را سر جایش می‌گذارد، حتی اگر بستهٔ ۳ پیش از ۲ برسد. اگر ۱، ۳ و ۴ برسند و ۲ نه، TCP فقط همان بستهٔ ۲ را دوباره می‌خواهد، نه کل ایمیل را.

> [!NOTE]
> **از سخنرانی: نمایش رد کردن بسته**
> در کلاس، چند داوطلب تکه‌های یک تصویر را مثل بسته از دست‌به‌دست به مقصد رساندند. صفحهٔ هفته ویدئوی جداگانه‌ای با نام [Passing TCP/IP Packet](https://youtu.be/cUJlRNRguAM) هم دارد.

> [!IMPORTANT]
> **استنتاجی: IP بدون اتصال است (d144)**
> هر بسته جداگانه مسیر خودش را می‌رود و ممکن است بسته‌ها با ترتیبی متفاوت برسند. به همین دلیل شماره‌گذاری بسته‌ها کار TCP است، نه IP. در متن رسمی ویدئوی TCP عبارت «connection with protocol» آمده که از بافت پیداست منظور «connectionless» بوده است.

## اشتباه‌های رایج

- فکر کردن به اینکه شمارهٔ درگاه رایانه را مشخص می‌کند؛ رایانه را IP مشخص می‌کند و درگاه، خدمت روی آن را.
- جابه‌جا گفتن درگاه‌ها: HTTP روی ۸۰ و HTTPS روی ۴۴۳.
- فکر کردن به اینکه با گم شدن یک بسته کل فایل دوباره فرستاده می‌شود.

## جمع‌بندی

- TCP ترتیب بسته‌ها را نگه می‌دارد، بستهٔ گم‌شده را دوباره می‌خواهد و دریافت را تأیید می‌کند.
- شمارهٔ درگاه خدمت را مشخص می‌کند: ۸۰ برای HTTP و ۴۴۳ برای HTTPS.
- هر بسته نشانی IP مبدأ، نشانی IP مقصد و شمارهٔ درگاه را دارد.

## پیوندها

- قبلی: [مسیریاب، بسته و نشانی IP](/kb/d/w08-n02)
- بعدی: [DNS: از نام دامنه تا نشانی IP](/kb/d/w08-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
