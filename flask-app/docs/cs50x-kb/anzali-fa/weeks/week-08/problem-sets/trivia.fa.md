---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-ps-trivia
type: problem-set-guide
title: راهنمای پرسش‌های سرگرمی (Trivia)
title_fa: پرسش‌های سرگرمی (Trivia)
title_en: Trivia
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/psets/8/trivia/
source_refs:
- src-pset-8-trivia#implementation-details
- src-pset-8-trivia#testing
- src-anzali-authored-8
- src-pset-8
concept_ids:
- w08-c-http-server
- w08-c-headings
- w08-c-input-attrs
- w08-c-queryselector
- w08-c-queryselectorall
- w08-c-event-listener
- w08-c-domcontentloaded
- w08-c-click-event
- w08-c-style-property
- w08-c-innerhtml
- w08-c-value-property
- w08-c-equality-operators
- w08-c-js-loops
problem_set_ref: weeks/week-08/problem-sets/trivia.json
prev: w08-sh-dom
next: w08-ps-homepage
order: 26
choice_group: null
submission: required
deadline_utc: '2027-06-30T23:59:00+00:00'
deadline_tehran: '2027-07-01T03:29:00+03:30'
---

# راهنمای پرسش‌های سرگرمی (Trivia)

> **منبع رسمی:** [Trivia](https://cs50.harvard.edu/x/2026/psets/8/trivia/) از پرابلم‌ست ۸ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تحویل لازم است. مهلت رسمی `2027-06-30T23:59:00+00:00` (به وقت تهران: ۱ ژوئیهٔ ۲۰۲۷، ساعت ۳:۲۹ بامداد).

## خلاصهٔ مسئله

صفحه‌ای می‌سازی که کاربر در آن به پرسش‌های سرگرمی پاسخ بدهد. فایل آغازین `index.html` دو بخش خالی دارد: «Part 1» برای یک پرسش چندگزینه‌ای و «Part 2» برای یک پرسش با پاسخ متنی. پرسش‌ها را خودت انتخاب می‌کنی.

در هر دو بخش، جاوااسکریپت باید به پاسخ کاربر واکنش نشان بدهد: دکمه یا جعبهٔ متن سبز یا قرمز می‌شود و زیر پرسش «Correct!» یا «Incorrect» ظاهر می‌شود. این راهنما کد هیچ بخشی از راه‌حل را ندارد: نه HTML پرسش‌ها، نه جاوااسکریپت گوش‌دهنده‌ها. همهٔ ابزارهای لازم در یادداشت‌ها و درس‌های کوتاه این هفته روی نمونه‌های دیگر تمرین شده‌اند.

> **از سخنرانی و جلسه:** `querySelector`، `addEventListener` و `DOMContentLoaded` در [یادداشت رویدادها](/kb/d/w08-n13)؛ `style` و `innerHTML` در [یادداشت DOM پویا](/kb/d/w08-n14)؛ `querySelectorAll` و حلقه در [یادداشت تکمیل خودکار](/kb/d/w08-n15). [جلسهٔ حل تمرین](/kb/d/w08-sec) یک صفحهٔ امتیاز با دکمه و `innerHTML` می‌سازد.

## خواسته‌های رسمی

1. صفحه را با HTML، CSS و جاوااسکریپت طراحی کن تا کاربر به پرسش‌های سرگرمی پاسخ بدهد.
2. در `index.html`، زیر «Part 1» یک پرسش چندگزینه‌ای به انتخاب خودت با HTML بگذار.
3. متن پرسش را با سرعنوان `h3` بنویس.
4. برای هر گزینه یک `button` بگذار؛ دست‌کم سه گزینه، که دقیقاً یکی درست است.
5. با جاوااسکریپت کاری کن که رنگ دکمه‌ها با کلیک کاربر عوض شود.
6. کلیک روی گزینهٔ نادرست: دکمه قرمز شود و زیر پرسش «Incorrect» ظاهر شود.
7. کلیک روی گزینهٔ درست: دکمه سبز شود و زیر پرسش «Correct!» ظاهر شود.
8. در `index.html`، زیر «Part 2» یک پرسش با پاسخ متنی به انتخاب خودت با HTML بگذار.
9. برای نوشتن پاسخ یک `input` و برای تأیید آن یک `button` بگذار (متن پرسش باز هم با `h3`).
10. با جاوااسکریپت کاری کن که رنگ جعبهٔ متن با تأیید پاسخ عوض شود.
11. پاسخ نادرست و زدن دکمهٔ تأیید: جعبهٔ متن قرمز شود و «Incorrect» ظاهر شود.
12. پاسخ درست و زدن دکمهٔ تأیید: جعبهٔ متن سبز شود و «Correct!» ظاهر شود.
13. check50 ندارد؛ برای هر پرسش هم پاسخ درست و هم نادرست را آزمایش کن.

## شروع کار

اول `cd` را تنها اجرا کن، بعد فایل‌ها را دانلود کن. صفحهٔ رسمی می‌گوید پس از `ls` باید `index.html` و `styles.css` را ببینی. فایل آغازین از نشانی پاییز ۲۰۲۵ دانلود می‌شود (d147). برای دیدن صفحه، در پوشهٔ `trivia` فرمان `http-server` را اجرا کن.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2025/fall/psets/8/trivia.zip
unzip trivia.zip
rm trivia.zip
```

بعد وارد پوشه شو و فایل‌ها را ببین:

```bash
cd trivia
ls
```

## راهنمایی‌های رسمی

> **رسمی:** بازنویسی فارسی بخش Hints صفحهٔ رسمی.

- برای پیدا کردن **یک** عنصر HTML از `document.querySelector` استفاده کن.
- برای پیدا کردن **همهٔ** عنصرهایی که با یک پرس‌وجو جورند از `document.querySelectorAll` استفاده کن؛ همهٔ عنصرهای جور را برمی‌گرداند.

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- اجرای http-server و درگاه 8080 — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u01`)
- سرعنوان‌ها از h1 تا h6 — [یادداشت](/kb/d/w08-n07) · درس کوتاه `w08-l03` (واحد `w08-l03-u02`)
- autocomplete، autofocus و placeholder — [یادداشت](/kb/d/w08-n09) · درس کوتاه `w08-l04` (واحد `w08-l04-u01`)
- document.querySelector با انتخابگر CSS — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)
- querySelectorAll برای چند عنصر — [یادداشت](/kb/d/w08-ps-trivia) · درس کوتاه `w08-l07` (واحد `w08-l07-u03`)
- addEventListener: گوش دادن به رویداد — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)
- DOMContentLoaded: صبر تا بارگیری کامل صفحه — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)
- رویداد click روی دکمه — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l07` (واحد `w08-l07-u02`)
- element.style.backgroundColor: نام camelCase — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l07` (واحد `w08-l07-u02`)
- innerHTML برای تغییر محتوای یک عنصر — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l07` (واحد `w08-l07-u01`)
- خاصیت value برای متن تایپ‌شده در input — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)
- == در برابر === در جاوااسکریپت — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l06` (واحد `w08-l06-u02`)
- حلقهٔ for...of روی آرایه — [یادداشت](/kb/d/w08-n15) · درس کوتاه `w08-l06` (واحد `w08-l06-u01`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. اول فقط HTML را بنویس و در مرورگر ببین: سرعنوان، دکمه‌ها، جعبهٔ متن و جایی خالی برای متن بازخورد. هنوز هیچ جاوااسکریپتی ننوشته‌ای.
2. از خودت بپرس جاوااسکریپت چطور دکمهٔ درست را از نادرست تشخیص می‌دهد. می‌توانی به عنصرها `id` یا `class` بدهی؛ کدام برای «یک عنصر» و کدام برای «چند عنصر» مناسب است؟
3. کدت باید پس از بارگذاری صفحه اجرا شود. در یادداشت رویدادها دیدی کدام رویداد برای این کار است، و اینکه `<script>` در `<head>` بدون آن عنصرها را پیدا نمی‌کند.
4. برای چند دکمهٔ نادرست، `querySelectorAll` چیزی شبیه آرایه برمی‌گرداند. در یادداشت تکمیل خودکار دیدی چطور روی چنین مجموعه‌ای حلقه بزنی.
5. رنگ را با ویژگی `style` عنصر عوض می‌کنی و متن بازخورد را با `innerHTML` عنصری دیگر. نام ویژگی‌های CSS در جاوااسکریپت camelCase می‌شوند.
6. برای پرسش متنی، مقدار تایپ‌شده در ویژگی `value` جعبه است. مقایسه را با `===` انجام بده و دربارهٔ حروف بزرگ و کوچک یا فاصلهٔ اضافه تصمیم بگیر.

## اشتباه‌های رایج

- گذاشتن `<script>` در `<head>` بدون `DOMContentLoaded`؛ `querySelector` مقدار `null` برمی‌گرداند
- نوشتن `background-color` به جای `backgroundColor` در جاوااسکریپت
- بستن رویداد فقط به اولین دکمه با `querySelector` وقتی چند دکمهٔ نادرست هست
- مقایسه با `=` به جای `===`
- نوشتن «correct» بدون علامت تعجب یا با حروف متفاوت
- آزمودن فقط پاسخ درست و فراموش کردن پاسخ نادرست

## چک‌لیست خودآزمایی

1. زیر «Part 1» یک پرسش با `h3` و دست‌کم سه دکمه هست و دقیقاً یکی درست است.
2. کلیک روی هر گزینهٔ نادرست آن را قرمز می‌کند و «Incorrect» را زیر پرسش نشان می‌دهد.
3. کلیک روی گزینهٔ درست آن را سبز می‌کند و «Correct!» را نشان می‌دهد.
4. زیر «Part 2» یک پرسش با `h3`، یک `input` و یک دکمهٔ تأیید هست.
5. پاسخ نادرست جعبه را قرمز و پاسخ درست آن را سبز می‌کند، با متن بازخورد زیر پرسش.
6. متن بازخورد دقیقاً `Correct!` و `Incorrect` است (با علامت تعجب فقط در اولی).
7. هر دو حالت درست و نادرست هر پرسش را در مرورگر با `http-server` آزموده‌ام.
8. کنسول مرورگر هیچ خطای جاوااسکریپت نشان نمی‌دهد.

## آزمون و تحویل

صفحهٔ رسمی برای این مسئله check50 ندارد؛ با `http-server` و چک‌لیست بالا خودت آزمایش کن.

صفحهٔ رسمی برای این مسئله style50 را نام نمی‌برد.

تحویل با submit50:

```bash
submit50 cs50/problems/2026/x/trivia
```

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راه‌حل‌های کارکنان در صفحهٔ رسمی Trivia](https://cs50.harvard.edu/x/psets/8/trivia/#how-to-submit): صفحهٔ رسمی زیر «How to Submit» دو راه‌حل کامل کارکنان را در بلوک‌های تاشو نشان می‌دهد (d139، D64)؛ در این بسته بازتولید نشده است. پیش از تحویل کار خودت به آن نگاه نکن.
- [ویدئوی راهنمای گام‌به‌گام](https://video.cs50.io/WGd0Jx7rxUo): ویدئوی رسمی؛ در زمان CS50 IDE ضبط شده است. فقط پیوند.

## ویدئو و نمایش

- [راهنمای گام‌به‌گام (walkthrough)](https://youtu.be/WGd0Jx7rxUo)

## پیوند رسمی

- [Trivia](https://cs50.harvard.edu/x/2026/psets/8/trivia/)
- [پرابلم‌ست ۸](https://cs50.harvard.edu/x/psets/8/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
