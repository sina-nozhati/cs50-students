---
id: w03-n01
type: note
title: 'خوش آمدید: الگوریتم‌ها و رشد زمان اجرا (Welcome!)'
title_fa: 'خوش آمدید: الگوریتم‌ها و رشد زمان اجرا'
title_en: Welcome!
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Welcome!
official_anchor: welcome
source_url: https://cs50.harvard.edu/x/2026/notes/3/#welcome
source_refs:
- src-notes-3#welcome
- src-transcript-3
- src-anzali-authored-3
- src-srt-3
concept_ids:
- w03-c-algorithm-black-box
- w03-c-growth-graph
prev: w03-fa
next: w03-n02
order: 1
video:
  youtube_id: 6Svu_ae5ebk
  start: 0:00
  start_seconds: 0
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=0s
  origin: inference
  basis: start of lecture
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# خوش آمدید: الگوریتم‌ها و رشد زمان اجرا

> **منبع رسمی:** بخش «Welcome!» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#welcome). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۰:۰۰ تا حدود ۱۲:۵۲](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=0s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تا اینجا یاد گرفتی برنامه‌ای بنویسی که **درست** کار کند. از این هفته سؤال تازه‌ای می‌پرسیم: برنامه‌ات **چقدر سریع** کار می‌کند، و وقتی داده ده برابر شد، چه اتفاقی برایش می‌افتد؟ این هفته دربارهٔ **طراحی** (`design`) الگوریتم‌هاست، نه فقط درستی‌شان.

## الگوریتم: جعبهٔ سیاه

- در هفتهٔ صفر **الگوریتم** (`algorithm`) را معرفی کردیم: جعبه‌ای سیاه که ممکن است ورودی بگیرد و خروجی بسازد.
- این هفته درک‌مان از الگوریتم‌ها را از **شبه‌کد** (`pseudocode`) تا خودِ کد گسترش می‌دهیم.
- همچنین به **کارایی** (`efficiency`) این الگوریتم‌ها فکر می‌کنیم و روی مفهوم‌های هفتهٔ پیش، به‌خصوص آرایه‌ها، بنا می‌کنیم.

## سه منحنی که باید بشناسی

درس‌نامه نموداری نشان می‌دهد: محور افقی «اندازهٔ مسئله» (`size of problem`) و محور عمودی «زمان حل» (`time to solve`)، با سه منحنی `n`، `n/2` و `log₂ n`. این نمودار در صفحهٔ رسمی به‌صورت SVG درون‌خطی رسم شده و فایل تصویری جدا ندارد؛ آن را در [درس‌نامهٔ رسمی](https://cs50.harvard.edu/x/2026/notes/3/#welcome) ببین.

- `n`: هر عضو تازه یک گام بیشتر. یک خط راست.
- `n/2`: باز هم خط راست، فقط با شیب کمتر؛ دو برابر سریع‌تر، ولی همان شکل.
- `log₂ n`: منحنی‌ای که تقریباً صاف می‌شود؛ دو برابر شدن داده فقط **یک** گام اضافه می‌خواهد.

> [!NOTE]
> **نکته**
> الگوریتم‌ها می‌توانند کُند باشند، با هزینهٔ زمانی و پردازشی بالا، یا تند، با هزینهٔ پایین. درس‌نامه می‌گوید شیوهٔ برخورد یک الگوریتم با مسئله می‌تواند زمان حل را تعیین کند و الگوریتم‌ها را می‌توان تا یک حد، کاراتر و کاراتر طراحی کرد.

## سخنرانی چه می‌گوید: حضور و غیاب الگوریتمی

- **از سخنرانی:** David اول پیشنهاد کرد حاضران را یکی‌یکی بشمارد (`1, 2, 3, ...`) و بعد دوتا‌دوتا (`2, 4, 6, ...`). هر دو روش خط راست‌اند؛ دومی فقط سریع‌تر است.
- **از سخنرانی:** بعد از همه خواست بایستند و عدد ۱ را در ذهن نگه دارند. هر کس با یک نفرِ ایستادهٔ دیگر جفت شود، دو عدد را جمع کند، یکی بنشیند و آن که ایستاده مانده دوباره از گام ۲ تکرار کند. با هر دور نیمی از جمعیت می‌نشینند.
- **از سخنرانی:** حاصل این الگوریتم ۱۴۱ نفر شد و شمارش دستی Kelly حدود ۱۶۰. David گفت این اختلاف احتمالاً از «باگ‌های اجرا» و حساب ذهنی بوده، نه از خود الگوریتم.
- **از سخنرانی:** اگر جمعیت دو برابر شود، الگوریتم سوم فقط **یک** دور بیشتر لازم دارد؛ همان ایدهٔ پاره کردن دفترچهٔ تلفن در هفتهٔ صفر.

> [!TIP]
> **راهنما**
> هر وقت الگوریتمی دیدی که در هر گام **نیمی** از مسئله را کنار می‌گذارد، به `log n` فکر کن. هر وقت دیدی هر عضو را یک بار نگاه می‌کند، به `n`.

## اشتباه‌های رایج

- «سریع‌تر» را با «بهتر رشد می‌کند» یکی دانستن. شمارش دوتا‌دوتا سریع‌تر است، اما هنوز خطی رشد می‌کند.
- فکر کردن به اینکه کارایی فقط دربارهٔ زمان است. David گفت هزینه می‌تواند زمان، پول یا فضای ذخیره‌سازی باشد؛ هر منبع محدودی.

## جمع‌بندی

- الگوریتم جعبه‌ای است که ورودی را به خروجی تبدیل می‌کند؛ این هفته کارایی‌اش را می‌سنجیم.
- سه شکل رشد را به خاطر بسپار: `n`، `n/2` و `log₂ n`.

## پیوندها

- قبلی: [نمای کلی هفته](/kb/d/w03-fa)
- بعدی: [جست‌وجوی خطی و قفسه‌ها](/kb/d/w03-n02)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
