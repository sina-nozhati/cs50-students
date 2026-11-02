---
week: 8
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
generated_at: '2026-10-29T08:00:00+03:30'
review_status: draft-needs-human-review
id: w08-sh-javascript
type: short-summary
title: 'ویدئوی کوتاه: جاوااسکریپت (JavaScript) (JavaScript)'
title_fa: جاوااسکریپت (JavaScript)
title_en: JavaScript
parent: w08-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/javascript/
source_refs:
- src-short-javascript
- src-anzali-inference-8
concept_ids:
- w08-c-javascript
- w08-c-script-src
- w08-c-js-variables
- w08-c-js-conditionals
- w08-c-js-loops
- w08-c-js-function
- w08-c-anonymous-function
- w08-c-js-array
- w08-c-js-objects
- w08-c-console-log
- w08-c-event-listener
prev: w08-sh-css
next: w08-sh-dom
order: 24
video:
  youtube_id: Z93IaNfavZw
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'مقدمه: زبانی از تبار C'
    evidence_en: null
  - start: '2:02'
    start_seconds: 122
    title_fa: script و فایل .js
    evidence_en: script tags
  - start: '2:51'
    start_seconds: 171
    title_fa: متغیر، شرط و حلقه
    evidence_en: variables
  - start: '3:58'
    start_seconds: 238
    title_fa: تابع و تابع بی‌نام
    evidence_en: anonymous
  - start: '4:31'
    start_seconds: 271
    title_fa: آرایه
    evidence_en: arrays
  - start: '5:10'
    start_seconds: 310
    title_fa: شیء و روش
    evidence_en: object-oriented
  - start: '9:04'
    start_seconds: 544
    title_fa: for ... in و for ... of
    evidence_en: for var key in
  - start: '10:33'
    start_seconds: 633
    title_fa: الحاق و parseInt
    evidence_en: concatenate
  - start: '12:42'
    start_seconds: 762
    title_fa: map با تابع بی‌نام
    evidence_en: map
  - start: '14:55'
    start_seconds: 895
    title_fa: رویدادها و گرداننده
    evidence_en: event handler
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: جاوااسکریپت (JavaScript) (JavaScript)

> **منبع رسمی:** [صفحهٔ Short «JavaScript» در CS50x](https://cs50.harvard.edu/x/shorts/javascript/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

جاوااسکریپت، مثل زبان‌های دیگر پایان درس، از نحو C گرفته شده و از میانهٔ دههٔ ۱۹۹۰ وجود دارد. همراه HTML و CSS، تجربهٔ کاربری وب را می‌سازد. برخلاف پایتون که در این ویدئو سمت سرور است، جاوااسکریپت **سمت کاربر**، در مرورگر خودت، اجرا می‌شود. می‌شود آن را بین تگ‌های `<script>` نوشت، یا بهتر، در فایل `.js` که با ویژگی `src` وصل می‌شود.

متغیرها نوع ندارند. شرط‌ها (`if`، `switch`، `?:`) و حلقه‌ها همان C هستند. تابع با کلیدواژهٔ `function` تعریف می‌شود و می‌تواند **بی‌نام** باشد. آرایه با `[]` ساخته می‌شود و نوع‌های مختلف را کنار هم نگه می‌دارد. **شیء** شبیه ساختار C است، با این تفاوت که **روش** (method) هم دارد، و نحوش با آکولاد شبیه واژه‌نامهٔ پایتون است: `{year: 1963, model: 'Beetle'}`.

دو حلقهٔ تازه: `for ... in` روی کلیدها (برای آرایه، اندیس‌ها) و `for ... of` روی مقدارها. ویدئو هشدار می‌دهد `+` هم جمع است هم الحاق، و با `parseInt` می‌شود اشتباه را رفع کرد. سپس `map` با یک تابع بی‌نام هر عنصر آرایه را دو برابر می‌کند. در پایان **رویدادها**: کلیک یا بارگذاری صفحه، و **گرداننده‌ای** (event handler) که در ویژگی `onclick` دکمه وصل می‌شود و با `innerHTML` دکمهٔ کلیک‌شده می‌فهمد کدام دکمه زده شده.

## نکته‌های کلیدی

- جاوااسکریپت در مرورگر کاربر اجرا می‌شود؛ بهتر است در فایل `.js` با `src` باشد.
- شرط‌ها و حلقه‌ها همان C هستند؛ تابع با `function` و می‌تواند بی‌نام باشد.
- شیء = ویژگی‌ها + روش‌ها؛ نحوش شبیه واژه‌نامهٔ پایتون است.
- `for ... in` کلید یا اندیس می‌دهد؛ `for ... of` مقدار.
- `+` روی رشته الحاق می‌کند؛ `parseInt` رشته را عدد می‌کند.
- `map` تابعی را روی همهٔ عنصرهای آرایه اجرا می‌کند.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`javascript.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه: زبانی از تبار C](https://www.youtube.com/watch?v=Z93IaNfavZw&t=0s)
- [۲:۰۲ — script و فایل .js](https://www.youtube.com/watch?v=Z93IaNfavZw&t=122s)
- [۲:۵۱ — متغیر، شرط و حلقه](https://www.youtube.com/watch?v=Z93IaNfavZw&t=171s)
- [۳:۵۸ — تابع و تابع بی‌نام](https://www.youtube.com/watch?v=Z93IaNfavZw&t=238s)
- [۴:۳۱ — آرایه](https://www.youtube.com/watch?v=Z93IaNfavZw&t=271s)
- [۵:۱۰ — شیء و روش](https://www.youtube.com/watch?v=Z93IaNfavZw&t=310s)
- [۹:۰۴ — for ... in و for ... of](https://www.youtube.com/watch?v=Z93IaNfavZw&t=544s)
- [۱۰:۳۳ — الحاق و parseInt](https://www.youtube.com/watch?v=Z93IaNfavZw&t=633s)
- [۱۲:۴۲ — map با تابع بی‌نام](https://www.youtube.com/watch?v=Z93IaNfavZw&t=762s)
- [۱۴:۵۵ — رویدادها و گرداننده](https://www.youtube.com/watch?v=Z93IaNfavZw&t=895s)

> [!NOTE]
> **یادداشت (d141، d142)**
> ویدئو برای متغیر محلی `var` را پیشنهاد می‌کند؛ درس‌نامهٔ ۲۰۲۶ و این بسته `let` و `const` را به کار می‌برند. آرایه روش `size` ندارد؛ طول آرایه ویژگی `length` است (روی جعبهٔ ساخت، `typeof [].size` مقدار `undefined` داد). ویژگی منبع رویداد امروز `event.target` است.

> [!TIP]
> **نکته (اجراشده روی جعبهٔ ساخت)**
> هشدار ویدئو دربارهٔ `+` واقعی است: در `for (var day in week)`، متغیر `day` رشته است (`'0'`، `'1'`، ...)، پس `day + 1` مقدار `01` و `11` را چاپ می‌کند، ولی `parseInt(day) + 1` مقدار `1` و `2` را.

## مفاهیم مرتبط

- جاوااسکریپت: زبان برنامه‌نویسی تعامل در صفحه — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u01`)
- <script src> برای بارگیری فایل جاوااسکریپت جدا — [یادداشت](/kb/d/w08-n15) · درس کوتاه `w08-l07` (واحد `w08-l07-u03`)
- متغیر با let در جاوااسکریپت — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l06` (واحد `w08-l06-u01`)
- if و else در جاوااسکریپت با آکولاد — [یادداشت](/kb/d/w08-n14) · درس کوتاه `w08-l06` (واحد `w08-l06-u02`)
- حلقهٔ for...of روی آرایه — [یادداشت](/kb/d/w08-n15) · درس کوتاه `w08-l06` (واحد `w08-l06-u01`)
- تعریف تابع در جاوااسکریپت — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u02`)
- تابع بی‌نام به‌عنوان آرگومان — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)
- آرایه در جاوااسکریپت و length — [یادداشت](/kb/d/w08-n15) · درس کوتاه `w08-l07` (واحد `w08-l07-u03`)
- شیء در جاوااسکریپت: خاصیت و متد — [یادداشت](/kb/d/w08-sh-javascript) · درس کوتاه `w08-l07` (واحد `w08-l07-u03`)
- console.log و کنسول مرورگر — [یادداشت](/kb/d/w08-sh-javascript) · درس کوتاه `w08-l06` (واحد `w08-l06-u01`)
- addEventListener: گوش دادن به رویداد — [یادداشت](/kb/d/w08-n13) · درس کوتاه `w08-l06` (واحد `w08-l06-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/Z93IaNfavZw) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/javascript/javascript.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/javascript/lang/en/javascript.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/javascript/lang/en/javascript.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
