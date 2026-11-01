---
id: w08-n06
type: note
title: 'HTTP و HTTPS: نشانی، درخواست و کد وضعیت (HTTPS)'
title_fa: 'HTTP و HTTPS: نشانی، درخواست و کد وضعیت'
title_en: HTTPS
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: HTTPS
official_anchor: https
source_url: https://cs50.harvard.edu/x/2026/notes/8/#https
source_refs:
- src-notes-8#https
- src-transcript-8
- src-short-http
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-http
- w08-c-https
- w08-c-url
- w08-c-get-post
- w08-c-headers
- w08-c-status-codes
- w08-c-curl
- w08-c-devtools-network
prev: w08-n05
next: w08-n07
order: 6
video:
  youtube_id: yYst7puZXjw
  start: '22:52'
  start_seconds: 1372
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=1372s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'or HTTPS,'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# HTTP و HTTPS: نشانی، درخواست و کد وضعیت

> **منبع رسمی:** بخش «HTTPS» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#https). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۲:۵۲ تا حدود ۳۹:۵۰](https://www.youtube.com/watch?v=yYst7puZXjw&t=1372s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

حالا که بسته به رایانهٔ درست و درگاه درست رسید، درونش چه نوشته شده است؟ درون پاکت درخواستی به زبان **HTTP** است: «لطفاً این صفحه را بده». و پاسخ سرور هم، پیش از خود صفحه، با یک کد وضعیت شروع می‌شود. اگر روزی سایتت `404` یا `500` داد، باید بدانی یعنی چه.

## HTTP و HTTPS

- **HTTP** یا **پروتکل انتقال ابرمتن** (`hypertext transfer protocol`) پروتکلی در سطح کاربرد است که توسعه‌دهنده‌ها با آن، از راه انتقال داده از جایی به جای دیگر، چیزهای قدرتمند و مفید می‌سازند. **HTTPS** نسخهٔ امن این پروتکل است.
- وقتی نشانی‌ای مثل `https://www.example.com` می‌بینی، در واقع به‌طور ضمنی همان نشانی را با یک `/` در انتها باز می‌کنی.
- **مسیر** (`path`) چیزی است که بعد از آن اسلش می‌آید. مثلاً `https://www.example.com/folder/file.html` به `example.com` می‌رود، وارد پوشهٔ `folder` می‌شود و فایل `file.html` را باز می‌کند.
- `.com` **دامنهٔ سطح بالا** (`top-level domain`) نام دارد و نوع یا مکان سازمانِ مربوط به نشانی را نشان می‌دهد.
- `https` در این نشانی پروتکلی است که برای وصل شدن به آن نشانی به کار می‌رود. منظور از پروتکل این است که HTTP با **درخواست‌های** (`request`) `GET` یا `POST` از سرور اطلاعات می‌خواهد. مثلاً در Google Chrome راست‌کلیک کن، `inspect` را بزن، در `developer tools` به `Network` برو و `Preserve log` را انتخاب کن؛ `Request Headers` را می‌بینی که در آن `GET` آمده است. در مرورگرهای دیگر هم با روش‌های کمی متفاوت شدنی است.

## درخواست و پاسخ

- مثلاً هنگام فرستادن یک درخواست GET، رایانه‌ات ممکن است این را به سرور بفرستد:

```text
GET / HTTP/2
Host: www.harvard.edu
```

- این درخواست از راه HTTP محتوایی را می‌خواهد که روی `www.harvard.edu` ارائه می‌شود.
- معمولاً بعد از درخواست، در `Response Headers` چنین چیزی می‌گیری:

```text
HTTP/2 200
Content-Type: text/html
```

> [!TIP]
> **از ویدئوی کوتاه: سطر درخواست**
> داگ لوید در [ویدئوی HTTP](/kb/d/w08-sh-http) نسخهٔ 1.1 را نشان می‌دهد (`GET / HTTP/1.1`): روش (method)، مسیر و نسخهٔ پروتکل، و در سطر بعد `Host`. درس‌نامهٔ ۲۰۲۶ همان ساختار را با `HTTP/2` نشان می‌دهد؛ ایده یکی است.

## دیدن سرآیندها با curl

- این روش دیدن سرآیندها شاید پیچیده‌تر از لازم باشد. می‌توانی کار HTTP را در [cs50.dev](https://cs50.dev) بررسی کنی. مثلاً این را در ترمینال بنویس:

```bash
curl -I https://www.harvard.edu/
```

- خروجی این فرمان همهٔ سرآیندهای پاسخ سرور را برمی‌گرداند.
- حالا این فرمان را اجرا کن:

```bash
curl -I https://harvard.edu
```

- پاسخ `301` می‌بینی که به مرورگر اشاره می‌کند وب‌سایت درست را کجا پیدا کند.
- به همین ترتیب:

```bash
curl -I http://www.harvard.edu/
```

- اینجا `s` از `https` حذف شده است. پاسخ سرور `301` است، یعنی وب‌سایت برای همیشه جابه‌جا شده است.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: دو فرمان نخست**
> در ۲۹ اکتبر ۲۰۲۶ ساعت ۰۷:۵۰ به وقت تهران، `curl -I https://www.harvard.edu/` پاسخ `HTTP/2 200` با `content-type: text/html` داد و `curl -I https://harvard.edu` پاسخ `HTTP/2 301` با `location: https://www.harvard.edu/`. فرمان سوم (HTTP ساده، بدون s) روی جعبهٔ ساخت قابل آزمودن نبود، چون شبکهٔ جعبه درخواست‌های HTTP ساده را مسدود می‌کند؛ پس آن ادعا فقط از درس‌نامه است.

## کدهای وضعیت

- شبیه `301`، کد `404` یعنی نشانی خواسته‌شده پیدا نشد. کدهای پاسخ بسیار دیگری هم هست:

```text
200 OK
301 Moved Permanently
302 Found
304 Not Modified
307 Temporary Redirect
401 Unauthorized
403 Forbidden
404 Not Found
418 I'm a Teapot
500 Internal Server Error
503 Service Unavailable
```

- خطاهای `500` وقتی به محصول یا برنامه‌ای مربوط باشند که خودت ساخته‌ای، معمولاً تقصیر خود توسعه‌دهنده‌اند. این برای مجموعه‌تمرین هفتهٔ بعد و شاید پروژهٔ نهایی‌ات مهم است. با این حال خطای `500` ممکن است از مشکلات زیرساخت یا خدمات شخص ثالث هم باشد.

> [!WARNING]
> **از ویدئوی کوتاه: چه کسی مقصر است؟ (d135)**
> ویدئوی HTTP دسته‌ها را این‌طور جمع‌بندی می‌کند: کدهای ۲۰۰ یعنی موفق، ۳۰۰ یعنی هدایت به جای دیگر، ۴۰۰ یعنی مشکل از سمت درخواست‌کننده، و ۵۰۰ یعنی مشکل از سمت سرور. این با جملهٔ درس‌نامه تناقض ندارد: اگر سرور مال توست، «سمت سرور» یعنی کد تو.

> [!TIP]
> **تألیفی: رقم اول را بخوان**
> برای حدس زدن معنای کدی که نمی‌شناسی، به رقم اولش نگاه کن: `2` موفقیت، `3` هدایت، `4` خطای درخواست، `5` خطای سرور. دربارهٔ `418 I'm a Teapot` هم دیوید در سخنرانی می‌گوید کد واقعی کاربردی نیست، بلکه شوخی روز اول آوریل بوده که حالا بخشی از فرهنگ اینترنت شده است.

## اشتباه‌های رایج

- فکر کردن به اینکه `301` خطاست؛ یعنی «برو به نشانی دیگر» و مرورگر خودش آن را دنبال می‌کند.
- یکی دانستن `401` و `403`: اولی یعنی احراز هویت نشده‌ای، دومی یعنی اجازه نداری.
- انداختن تقصیر `500` همیشه به گردن کاربر.

## جمع‌بندی

- HTTP پروتکل سطح کاربرد وب است و HTTPS نسخهٔ امن آن.
- نشانی وب از پروتکل، نام دامنه (با دامنهٔ سطح بالا) و مسیر تشکیل می‌شود.
- مرورگر درخواست `GET` یا `POST` می‌فرستد و سرور با کد وضعیت و سرآیندها پاسخ می‌دهد.
- `curl -I` سرآیندهای پاسخ را در ترمینال نشان می‌دهد.

## پیوندها

- قبلی: [DHCP: نشانی IP دستگاه خودت](/kb/d/w08-n05)
- بعدی: [HTML: تگ، ویژگی و درخت سند](/kb/d/w08-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
