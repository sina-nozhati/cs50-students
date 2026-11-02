---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-fa
type: week-overview
title: هفتهٔ ۸ — HTML، CSS و جاوااسکریپت (پایگاه دانش فارسی)
title_fa: هفتهٔ ۸ — HTML، CSS و جاوااسکریپت
title_en: Week 8 — HTML, CSS, JavaScript
parent: week-8
source_type: translated-rewritten
origin: mixed
origin_detail: Official week summary/topic list rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/8/
source_refs:
- src-week-8#week-8-html-css-javascript
- src-notes-8#lecture-8
- src-pset-8
- src-short-internet-primer
- src-short-javascript
- src-anzali-authored-8
- src-anzali-inference-8
children:
- w08-n01
- w08-n02
- w08-n03
- w08-n04
- w08-n05
- w08-n06
- w08-n07
- w08-n08
- w08-n09
- w08-n10
- w08-n11
- w08-n12
- w08-n13
- w08-n14
- w08-n15
- w08-summary
- w08-sec
- w08-sh-internet-primer
- w08-sh-ip
- w08-sh-tcp
- w08-sh-http
- w08-sh-html
- w08-sh-css
- w08-sh-javascript
- w08-sh-dom
- w08-ps-trivia
- w08-ps-homepage
- w08-pr-redo
objective_ids:
- w08-o01
- w08-o02
- w08-o03
- w08-o04
- w08-o05
- w08-o06
- w08-o07
- w08-o08
- w08-o09
- w08-o10
---

# هفتهٔ ۸ — HTML، CSS و جاوااسکریپت

> **منبع رسمی:** [صفحهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/weeks/8/) و [درس‌نامهٔ هفتهٔ ۸](https://cs50.harvard.edu/x/2026/notes/8/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها و معیار تسلط **تألیف CS50x Anzali** هستند و قاعدهٔ رسمی CS50 نیستند.

## این هفته دربارهٔ چیست؟

تا اینجا برنامه‌هایت در ترمینال اجرا می‌شدند. این هفته به **وب** می‌روی. هفته از «بیرون پاکت» شروع می‌شود: اینترنت چطور بسته‌ها را با **مسیریاب‌ها** جابه‌جا می‌کند، **IP** و **TCP** چه نقشی دارند، **DNS** نام‌ها را به نشانی ترجمه می‌کند و **DHCP** به دستگاهت نشانی می‌دهد. بعد درون پاکت را باز می‌کنی: **HTTP** و **HTTPS**، درخواست `GET` و کدهای وضعیت مثل `200`، `301` و `404`.

سپس سه زبان وب را یاد می‌گیری. **HTML** ساختار صفحه است: تگ‌ها، ویژگی‌ها، فهرست، جدول، تصویر، پیوند و فرم، به‌علاوهٔ **عبارت باقاعده** برای اعتبارسنجی ورودی. **CSS** ظاهر صفحه است: ویژگی‌ها، انتخابگرها و آبشار، و چارچوبی مثل **Bootstrap**. **جاوااسکریپت** صفحه را پویا می‌کند: رویدادها، `querySelector`، تغییر `innerHTML` و سبک، زمان‌سنج و در آخر یک تکمیل خودکار.

## مباحث رسمی هفته

صفحهٔ رسمی هفته این مباحث را فهرست می‌کند:

اینترنت: مسیریاب‌ها؛ TCP/IP؛ DNS. HTTP: نشانی‌ها، GET و POST. HTML: تگ‌ها؛ ویژگی‌ها. سرورها. عبارت‌های باقاعده. CSS: ویژگی‌ها؛ انتخابگرها. چارچوب‌ها. جاوااسکریپت: متغیرها؛ شرط‌ها؛ حلقه‌ها. رویدادها. (Internet: Routers; TCP/IP; DNS. HTTP: URLs, GET, POST. HTML: Tags; Attributes. Servers. Regular Expressions. CSS: Properties; Selectors. Frameworks. JavaScript: Variables; Conditionals; Loops. Events.)

> **توجه:** هشت ویدئوی کوتاه این هفته (Doug Lloyd) در سال ۲۰۱۷ ضبط شده‌اند. بخشی از نمونه‌هایشان مال CS50 قدیم است، مثل PHP، `var`، jQuery و `getElementById` (d141). خلاصهٔ فارسی هر ویدئو این تفاوت‌ها را نشان می‌دهد.

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه، سخنرانی، جلسهٔ حل تمرین و پرابلم‌ست ۸ استخراج کرده است.

- **w08-o01** — نقش مسیریاب، بسته، نشانی IP (IPv4 و IPv6)، TCP و شمارهٔ درگاه را توضیح بدهی.
- **w08-o02** — کار DNS و DHCP را از هم جدا کنی و بگویی DHCP چه چیزهایی به دستگاه می‌دهد.
- **w08-o03** — بخش‌های یک نشانی وب، درخواست `GET`، سرآیندها و کدهای وضعیت رایج را بخوانی و با `curl -I` یا ابزار توسعه‌دهندهٔ مرورگر ببینی.
- **w08-o04** — یک سند HTML درست با `<!DOCTYPE html>`، `<head>` و `<body>` بنویسی و درخت آن را تصور کنی.
- **w08-o05** — سرعنوان، فهرست، جدول، تصویر با `alt`، ویدئو و پیوند بسازی.
- **w08-o06** — فرم با `action`، `method` و `name` بسازی، رشتهٔ پرس‌وجو را بخوانی و با `type="email"` و `pattern` ورودی را اعتبارسنجی کنی و مرز این اعتبارسنجی را بدانی.
- **w08-o07** — CSS را با ویژگی `style`، تگ `<style>` و فایل بیرونی به کار ببری و انتخابگر نوع، کلاس و شناسه را بشناسی.
- **w08-o08** — از چارچوبی مثل Bootstrap با کلاس‌های آماده استفاده کنی.
- **w08-o09** — نحو پایهٔ جاوااسکریپت (متغیر، شرط، حلقه، تابع، `==` و `===`) و گوش دادن به رویدادها با `addEventListener` و `DOMContentLoaded` را به کار ببری.
- **w08-o10** — DOM را با `querySelector`، `innerHTML` و `style` تغییر بدهی و با `keyup`، `click` و `setInterval` صفحه را پویا کنی.

## پیش‌نیازها

- هفتهٔ ۱: نحو C (متغیر، شرط، حلقه)؛ نحو جاوااسکریپت به آن نزدیک است. ([نمای کلی هفتهٔ ۱](/kb/d/w01-fa))
- هفتهٔ ۵: درخت؛ سند HTML در حافظه یک درخت است. ([نمای کلی هفتهٔ ۵](/kb/d/w05-fa))
- هفتهٔ ۶: پایتون و عبارت باقاعده با `re`. ([نمای کلی هفتهٔ ۶](/kb/d/w06-fa))

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: بیرون پاکت
  مسیریاب و بسته -> IP و IPv4/IPv6 -> TCP و درگاه -> DNS -> DHCP

مرحلهٔ ۲: درون پاکت
  HTTP و HTTPS -> نشانی و GET -> سرآیندها -> کد وضعیت -> curl و ابزار توسعه‌دهنده

مرحلهٔ ۳: HTML
  تگ و ویژگی -> DOCTYPE، head، body -> درخت سند -> فهرست، جدول، تصویر، پیوند

مرحلهٔ ۴: فرم
  form و input -> name و رشتهٔ پرس‌وجو -> type="email" و pattern -> مرز اعتبارسنجی

مرحلهٔ ۵: CSS
  ویژگی و مقدار -> style -> انتخابگر نوع، کلاس، شناسه -> فایل بیرونی -> Bootstrap

مرحلهٔ ۶: جاوااسکریپت
  متغیر و نوع -> == و === -> تابع و رویداد -> DOMContentLoaded

مرحلهٔ ۷: DOM پویا
  keyup و template literal -> innerHTML -> style و click -> setInterval -> autocomplete
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۱۵ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران (۷ درس).
3. ویدئوهای کوتاه را کنار یادداشت‌ها ببین: [مقدمه‌ای بر اینترنت](/kb/d/w08-sh-internet-primer)، [IP](/kb/d/w08-sh-ip) و [TCP](/kb/d/w08-sh-tcp) پس از یادداشت ۳، [HTTP](/kb/d/w08-sh-http) پس از یادداشت ۶، [HTML](/kb/d/w08-sh-html) پس از یادداشت ۸، [CSS](/kb/d/w08-sh-css) پس از یادداشت ۱۱، و [جاوااسکریپت](/kb/d/w08-sh-javascript) و [DOM](/kb/d/w08-sh-dom) پس از یادداشت ۱۴.
4. [جلسهٔ حل تمرین (Section)](/kb/d/w08-sec) را پیش از پرابلم‌ست ببین؛ یک صفحهٔ امتیاز (scoreboard) را از HTML تا جاوااسکریپت می‌سازد.
5. چالش‌های کوتاه هفته را امتحان کن، آزمون تسلط را بده و بعد سراغ پرابلم‌ست برو.

## پرابلم‌ست ۸

طبق صفحهٔ رسمی پرابلم‌ست ۸:

- [Trivia](/kb/d/w08-ps-trivia) را **تحویل بده**.
- [Homepage](/kb/d/w08-ps-homepage) را **تحویل بده**.
- پیش از شروع، `update50` را در codespace اجرا کن و وقتی پرسیده شد، **Rebuild now** را بزن.
- مهلت رسمی: `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

مسئلهٔ تمرینی اختیاری: [Radio Shack Redo](/kb/d/w08-pr-redo). صفحهٔ آن می‌گوید check50 ندارد و تحویل لازم نیست.

> **سیاست این بسته:** هیچ راه‌حلی برای پرابلم‌ست‌ها ارائه نمی‌شود. بخش «Hints» صفحهٔ رسمی Trivia دو راه‌حل کامل کارکنان را نشان می‌دهد (پاسخ درست هر دو پرسش و کد گوش‌دهنده‌ها)؛ این بسته آن‌ها را بازتولید نمی‌کند و فقط پیوند می‌دهد (D64، d139). راهنمای Homepage فقط مفهوم‌ها و چک‌لیست می‌دهد، نه کد یک سایت (D65). همهٔ نمونه‌های جاوااسکریپت این بسته با node و نمونه‌های HTML با jsdom روی جعبهٔ ساخت اجرا شده‌اند (D66، D67).

## معیار تسلط بر هفته

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه هفته «مسلط» شده باشند.
- نمرهٔ آزمون تسلط هفته دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.
- چک‌لیست خودآزمایی هر دو پرابلم‌ست کامل شده باشد.

## پیوندهای رسمی

- [صفحهٔ هفتهٔ ۸](https://cs50.harvard.edu/x/weeks/8/) · [درس‌نامه](https://cs50.harvard.edu/x/2026/notes/8/) · [ویدئوی سخنرانی](https://video.cs50.io/yYst7puZXjw)
- [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/lectures/8/lecture8.pdf) · [کد منبع (zip)](https://cdn.cs50.net/2025/fall/lectures/8/src8.zip) · [زیرنویس](https://cdn.cs50.net/2025/fall/lectures/8/lang/en/lecture8.srt)
- [نمایش زندهٔ «بسته‌ای که دست‌به‌دست می‌شود»](https://youtu.be/cUJlRNRguAM) · [جلسهٔ حل تمرین](https://cs50.harvard.edu/x/sections/8/) · [پرابلم‌ست ۸](https://cs50.harvard.edu/x/2026/psets/8/)
- [سرویس اعتبارسنجی W3C](https://validator.w3.org/#validate_by_input) · [مرجع وب در w3schools](https://www.w3schools.com/html/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
