---
id: w08-n02
type: note
title: 'مسیریاب، بسته و نشانی IP (Routers: IP and Packets)'
title_fa: مسیریاب، بسته و نشانی IP
title_en: 'Routers: IP and Packets'
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
- src-short-internet-primer
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-router
- w08-c-packet
- w08-c-protocol
- w08-c-ip-address
- w08-c-ipv4-ipv6
- w08-c-packet-header
prev: w08-n01
next: w08-n03
order: 2
video:
  youtube_id: yYst7puZXjw
  start: '5:28'
  start_seconds: 328
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=328s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'a protocol nowadays known as TCP IP'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# مسیریاب، بسته و نشانی IP

> **منبع رسمی:** بخش «Routers» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#routers). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵:۲۸ تا حدود ۱۱:۱۳](https://www.youtube.com/watch?v=yYst7puZXjw&t=328s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

وقتی در مرورگر نشانی‌ای را باز می‌کنی، درخواستت باید به رایانه‌ای مشخص در آن سوی دنیا برسد و جواب هم درست به تو برگردد. برای این کار هر رایانه نشانی لازم دارد و داده باید در بسته‌هایی با نشانی فرستنده و گیرنده سفر کند. این همان چیزی است که **IP** فراهم می‌کند.

## مسیریاب‌ها و بسته‌ها

- برای رساندن داده از جایی به جای دیگر باید **تصمیم مسیریابی** (routing decision) گرفت؛ یعنی کسی باید برنامه‌ریزی کند که داده چطور از نقطهٔ A به نقطهٔ B برود.
- داده می‌تواند از چند مسیر از A به B برود؛ اگر مسیریابی شلوغ باشد، داده از مسیر دیگری می‌رود. **بسته‌های** (`packet`) داده از مسیریابی به مسیریاب دیگر و از رایانه‌ای به رایانهٔ دیگر منتقل می‌شوند.
- **TCP/IP** دو **پروتکل** (`protocol`) هستند که به رایانه‌ها اجازه می‌دهند روی اینترنت با هم داده مبادله کنند.

> [!NOTE]
> **از سخنرانی: پروتکل مثل دست دادن**
> دیوید پروتکل را با یک قرارداد انسانی توضیح می‌دهد: وقتی کسی را برای اولین بار می‌بینی دستت را دراز می‌کنی و انتظار داری او هم دستش را دراز کند. پروتکل همین است: مجموعه‌ای از قراردادها که هر دو طرف از پیش می‌دانند.

## IP و نشانی‌ها

- **IP** یا **پروتکل اینترنت** (`internet protocol`) راهی است که رایانه‌ها با آن یکدیگر را روی اینترنت شناسایی می‌کنند. هر رایانه نشانی یکتایی در جهان دارد. نشانی‌ها به این شکل‌اند:

```text
#.#.#.#
```

- عددها از `0` تا `255` هستند. نشانی‌های IP (در IPv4) ۳۲ بیتی‌اند، یعنی بیش از ۴ میلیارد نشانی ممکن است. نسخه‌های تازه‌تر (مثل IPv6) با ۱۲۸ بیت جای رایانه‌های بسیار بیشتری دارند.
- در دنیای واقعی، سرورها کار زیادی برای ما انجام می‌دهند.

> [!TIP]
> **تألیفی: چرا از ۰ تا ۲۵۵؟**
> هر یک از چهار عدد در یک بایت (۸ بیت) جا می‌گیرد و ۸ بیت دقیقاً ۲۵۶ مقدار دارد: از ۰ تا ۲۵۵ (همان چیزی که در هفتهٔ ۰ دیدی). چهار بایت روی هم ۳۲ بیت می‌شود و ۲ به توان ۳۲ برابر ۴٬۲۹۴٬۹۶۷٬۲۹۶ است؛ «بیش از ۴ میلیارد». پس `192.168.1.300` نشانی IPv4 معتبری نیست.

> [!NOTE]
> **از ویدئوی کوتاه: «یکتا» در عمل (d145)**
> درس‌نامه می‌گوید هر رایانه نشانی یکتایی دارد. داگ لوید در [مقدمه‌ای بر اینترنت](/kb/d/w08-sh-internet-primer) توضیح می‌دهد که چون ۴ میلیارد نشانی برای همهٔ دستگاه‌ها کم است، دستگاه‌های یک خانه معمولاً **نشانی خصوصی** دارند و همه از راه مسیریاب خانه با یک نشانی عمومی مشترک بیرون می‌روند. IPv6 راه‌حل بلندمدت است.

## ساختار بسته

- بسته‌ها این ساختار را دارند:

```text
0                   1                   2                   3  
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

- بسته‌ها استاندارد شده‌اند. نشانی مبدأ (Source Address) و مقصد (Destination Address) درون هر بسته نگه داشته می‌شود.

> [!TIP]
> **استنتاجی: این شکل را حفظ نکن**
> نمودار بالا سرآیند (header) بستهٔ IPv4 است. لازم نیست فیلدهایش را حفظ کنی؛ نکتهٔ اصلی این است که هر بسته مثل یک پاکت نامه، نشانی فرستنده و گیرنده را روی خودش دارد و هر مسیریاب فقط با نگاه به همین نشانی تصمیم می‌گیرد آن را به کدام سو بفرستد.

## اشتباه‌های رایج

- نوشتن عددی بزرگ‌تر از ۲۵۵ در نشانی IPv4.
- فکر کردن به اینکه یک فایل بزرگ در یک بسته فرستاده می‌شود؛ یادداشت بعدی نشان می‌دهد فایل به چند بسته تقسیم می‌شود.
- یکی دانستن IP و TCP. IP رایانه را پیدا می‌کند؛ TCP (یادداشت بعدی) برنامه یا خدمت روی آن رایانه را.

## جمع‌بندی

- مسیریاب‌ها بسته‌ها را گام‌به‌گام به مقصد نزدیک می‌کنند و مسیر می‌تواند عوض شود.
- نشانی IPv4 به شکل `#.#.#.#` است، هر عدد از ۰ تا ۲۵۵، روی هم ۳۲ بیت. IPv6 ۱۲۸ بیت است.
- هر بسته نشانی مبدأ و مقصد را با خودش دارد.

## پیوندها

- قبلی: [اینترنت: از ARPANET تا صفحه‌های خودت](/kb/d/w08-n01)
- بعدی: [TCP، شمارهٔ درگاه و بسته‌های گم‌شده](/kb/d/w08-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
