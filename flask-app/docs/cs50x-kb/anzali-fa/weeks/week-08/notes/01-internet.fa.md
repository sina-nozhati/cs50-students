---
id: w08-n01
type: note
title: 'اینترنت: از ARPANET تا صفحه‌های خودت (Welcome! and The Internet)'
title_fa: 'اینترنت: از ARPANET تا صفحه‌های خودت'
title_en: Welcome! and The Internet
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: The Internet
official_anchor: the-internet
source_url: https://cs50.harvard.edu/x/2026/notes/8/#the-internet
source_refs:
- src-notes-8#the-internet
- src-notes-8#welcome
- src-transcript-8
- src-short-internet-primer
- src-anzali-authored-8
- src-anzali-inference-8
- src-srt-8
concept_ids:
- w08-c-internet
- w08-c-arpanet
prev: w08-fa
next: w08-n02
order: 1
video:
  youtube_id: yYst7puZXjw
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# اینترنت: از ARPANET تا صفحه‌های خودت

> **منبع رسمی:** بخش «The Internet» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#the-internet). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۵:۲۸](https://www.youtube.com/watch?v=yYst7puZXjw&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا برنامه‌هایت در ترمینال اجرا می‌شدند: کاربر چیزی تایپ می‌کرد، برنامه جواب می‌داد و تمام. از این هفته برنامه‌ها به **مرورگر** (browser) می‌روند. پیش از نوشتن اولین صفحه، باید بدانیم داده چطور از یک رایانه به رایانهٔ دیگر می‌رسد؛ همهٔ چیزهایی که این هفته و هفتهٔ بعد می‌سازی روی همین لوله‌کشی سوار است.

## خوش آمدی

- در هفته‌های گذشته با پایتون آشنا شدیم: زبانی سطح بالا که همان قطعه‌های سازندهٔ C را به کار می‌برد. امروز همان قطعه‌ها را به سه زبان تازه می‌بریم: **HTML**، **CSS** و **جاوااسکریپت** (`JavaScript`).

## اینترنت

- **اینترنت** (`internet`) فناوری‌ای است که همهٔ ما هر روز از آن استفاده می‌کنیم و رایانه‌های سراسر جهان را به هم وصل می‌کند.
- با مهارت‌هایی که در هفته‌های قبل به دست آوردی، حالا می‌توانی صفحه‌ها و برنامه‌های وب خودت را بسازی.
- **ARPANET** نخستین نقطه‌های اینترنت را به هم وصل کرد.
- نقطه‌های میان دو نقطه را می‌توان **مسیریاب** (`router`) دانست.

> [!NOTE]
> **از سخنرانی: ARPANET از کجا آمد**
> دیوید توضیح می‌دهد که ARPANET پروژه‌ای از وزارت دفاع آمریکا (Advanced Research Projects Agency) بود تا ابررایانه‌های محدود آن زمان را، که برای بسیاری از پژوهشگران از نظر جغرافیایی دور از دسترس بودند، به هم وصل کند. نقشهٔ آن روزها فقط چند نقطه داشت؛ امروز میلیاردها دستگاه.

> [!TIP]
> **از ویدئوی کوتاه: اینترنت یک «چیز» نیست**
> داگ لوید در [مقدمه‌ای بر اینترنت](/kb/d/w08-sh-internet-primer) می‌گوید اینترنت ابری جدا نیست که همه به آن وصل شوند؛ شبکه‌های کوچک (خانه، مدرسه، محل کار) **به یکدیگر** وصل‌اند و اینترنت مجموعه‌ای از قواعد، یعنی **پروتکل‌ها**، است که می‌گوید این شبکه‌ها چطور با هم حرف بزنند. نامش هم از همین می‌آید: شبکهٔ میان‌شبکه‌ای (inter-net).

> [!IMPORTANT]
> **استنتاجی: نقشهٔ راه این هفته**
> یادداشت‌های ۲ تا ۶ «بیرون پاکت» را می‌بینند: نشانی‌دهی (IP)، رساندن مطمئن (TCP)، نام‌ها (DNS)، پیکربندی خودکار (DHCP) و درخواست صفحه (HTTP). یادداشت‌های ۷ تا ۱۵ «درون پاکت» را می‌بینند: خود صفحه با HTML، ظاهرش با CSS و رفتارش با جاوااسکریپت. این تقسیم‌بندی از جملهٔ خود درس‌نامه در بخش DHCP گرفته شده است.

## اشتباه‌های رایج

- یکی دانستن «اینترنت» و «وب». وب (صفحه‌ها و HTTP) فقط یکی از خدماتی است که روی اینترنت کار می‌کند؛ ایمیل و تماس تصویری هم روی همین شبکه‌اند.
- فکر کردن به اینکه داده همیشه از کوتاه‌ترین مسیر می‌رود. یادداشت بعدی نشان می‌دهد مسیر به تصمیم مسیریاب‌ها بستگی دارد.

## جمع‌بندی

- اینترنت رایانه‌های جهان را به هم وصل می‌کند و از ARPANET شروع شد.
- نقطه‌های میانی، مسیریاب‌ها هستند.
- این هفته سه زبان تازه داریم: HTML برای ساختار، CSS برای ظاهر و جاوااسکریپت برای تعامل.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w08-fa)
- بعدی: [مسیریاب، بسته و نشانی IP](/kb/d/w08-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
