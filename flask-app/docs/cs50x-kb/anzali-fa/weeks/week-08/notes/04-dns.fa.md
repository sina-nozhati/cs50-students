---
id: w08-n04
type: note
title: 'DNS: از نام دامنه تا نشانی IP (DNS)'
title_fa: 'DNS: از نام دامنه تا نشانی IP'
title_en: DNS
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: DNS
official_anchor: dns
source_url: https://cs50.harvard.edu/x/2026/notes/8/#dns
source_refs:
- src-notes-8#dns
- src-short-internet-primer
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-dns
- w08-c-fqdn
prev: w08-n03
next: w08-n05
order: 4
video:
  youtube_id: yYst7puZXjw
  start: '17:06'
  start_seconds: 1026
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=1026s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase 'namely DNS for domain name system'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# DNS: از نام دامنه تا نشانی IP

> **منبع رسمی:** بخش «DNS» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#dns). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۷:۰۶ تا حدود ۲۰:۳۹](https://www.youtube.com/watch?v=yYst7puZXjw&t=1026s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هیچ‌کس `23.185.0.1` یا عددی مثل آن را برای باز کردن یک سایت حفظ نمی‌کند. ما نام‌ها را به خاطر می‌سپاریم، مثل `harvard.edu`. کسی باید نام را به نشانی IP ترجمه کند؛ این کار **DNS** است.

## DNS

- اگر برای دیدن هر وب‌سایت باید نشانی IP آن را به خاطر می‌سپردی، کار بسیار خسته‌کننده می‌شد.
- **DNS** یا **سامانهٔ نام دامنه** (`domain name system`) مجموعه‌ای از سرورها روی اینترنت است که نشانی‌های وب‌سایت مثل `harvard.edu` را به یک نشانی IP مشخص می‌رسانند.
- DNS در اصل یک جدول یا پایگاه داده است که **نام‌های دامنهٔ کامل** (`fully qualified domain name`) را به نشانی‌های IP مشخص پیوند می‌دهد.

> [!TIP]
> **تألیفی: DNS مثل یک دیکشنری پایتون**
> از هفتهٔ ۶ یادت هست که دیکشنری کلید را به مقدار نگاشت می‌کرد. DNS را می‌شود مثل یک دیکشنری عظیم و پخش‌شده تصور کرد که کلیدش نام دامنه و مقدارش نشانی IP است؛ با این تفاوت که هیچ رایانه‌ای کل آن را نگه نمی‌دارد.

> [!NOTE]
> **از ویدئوی کوتاه: هیچ سرور DNS همه‌چیز را نمی‌داند**
> داگ لوید در [مقدمه‌ای بر اینترنت](/kb/d/w08-sh-internet-primer) توضیح می‌دهد که DNS **غیرمتمرکز** است. سرورهای بزرگ (مثلاً متعلق به شرکت‌های اینترنتی) نشانی‌های پرکاربرد را نگه می‌دارند و سرورهای کوچک‌تر، مثلاً در یک دانشگاه، فقط نام‌های محلی را. اگر سروری نامی را نشناسد، پرسش را به سرور دیگری می‌سپارد؛ پاسخ‌ها هم برای مدتی ذخیره (cache) می‌شوند.

> [!IMPORTANT]
> **استنتاجی: DNS فقط ترجمه می‌کند**
> DNS صفحه را به تو نمی‌دهد؛ فقط می‌گوید صفحه کجاست. بعد از آنکه مرورگر نشانی IP را گرفت، با TCP/IP و HTTP خود صفحه را درخواست می‌کند. اگر DNS خراب باشد، اینترنت «قطع» به نظر می‌رسد، در حالی که بسته‌ها هنوز به نشانی‌های IP می‌رسند.

## اشتباه‌های رایج

- فکر کردن به اینکه یک سرور مرکزی همهٔ نام‌ها را می‌داند.
- یکی دانستن نام دامنه و نشانی IP؛ یک نام ممکن است به نشانی‌های مختلفی برسد و نشانی‌ها ممکن است عوض شوند.

## جمع‌بندی

- DNS نام‌های دامنه را به نشانی‌های IP ترجمه می‌کند.
- DNS مجموعه‌ای از سرورهاست و مثل جدولی پخش‌شده کار می‌کند.

## پیوندها

- قبلی: [TCP، شمارهٔ درگاه و بسته‌های گم‌شده](/kb/d/w08-n03)
- بعدی: [DHCP: نشانی IP دستگاه خودت](/kb/d/w08-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
