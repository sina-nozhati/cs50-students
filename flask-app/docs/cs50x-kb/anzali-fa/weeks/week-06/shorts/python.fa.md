---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-sh-python
type: short-summary
title: 'ویدئوی کوتاه: پایتون (Python)'
title_fa: پایتون
title_en: Python
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/python/
source_refs:
- src-short-python
- src-python-docs
- src-anzali-inference-6
concept_ids:
- w06-c-python3-version
- w06-c-interpreted
- w06-c-no-declaration
- w06-c-logical-words
- w06-c-elif
- w06-c-bool-capitalized
- w06-c-augmented-assignment
- w06-c-for-range
- w06-c-list
- w06-c-append
- w06-c-tuple
- w06-c-dict
- w06-c-dict-iteration
- w06-c-def-function
- w06-c-main-convention
- w06-c-object-method
- w06-c-class-init
- w06-c-import
prev: w06-sec
next: w06-ps-hello
order: 18
video:
  youtube_id: mgBpcQRDtl0
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: معرفی پایتون
    evidence_en: null
  - start: '1:30'
    start_seconds: 90
    title_fa: تفسیری، نه کامپایلی
    evidence_en: not a compiled language
  - start: '1:59'
    start_seconds: 119
    title_fa: پایتون ۳
    evidence_en: we teach Python 3
  - start: '2:36'
    start_seconds: 156
    title_fa: متغیرها و رشته‌ها
    evidence_en: variables have two
  - start: '4:09'
    start_seconds: 249
    title_fa: شرط‌ها و elif
    evidence_en: conditional statements
  - start: '6:32'
    start_seconds: 392
    title_fa: عملگر سه‌تایی و True/False
    evidence_en: ternary
  - start: '7:17'
    start_seconds: 437
    title_fa: input و حلقه‌ها
    evidence_en: function called input
  - start: '9:19'
    start_seconds: 559
    title_fa: range
    evidence_en: For x in range
  - start: '10:11'
    start_seconds: 611
    title_fa: فهرست‌ها
    evidence_en: arrays are really
  - start: '14:39'
    start_seconds: 879
    title_fa: tuple
    evidence_en: So what a tuple is
  - start: '18:39'
    start_seconds: 1119
    title_fa: واژه‌نامه
    evidence_en: is the concept of a dictionary
  - start: '21:26'
    start_seconds: 1286
    title_fa: پیمایش واژه‌نامه
    evidence_en: for pie in pizzas
  - start: '25:00'
    start_seconds: 1500
    title_fa: شیوه‌های قالب‌بندی رشته
    evidence_en: deprecated in Python 3
  - start: '25:20'
    start_seconds: 1520
    title_fa: تابع‌ها و main
    evidence_en: explicitly force it
  - start: '27:31'
    start_seconds: 1651
    title_fa: شیء، کلاس و متد
    evidence_en: Let's talk about objects
  - start: '35:06'
    start_seconds: 2106
    title_fa: سبک و تورفتگی
    evidence_en: good style
  - start: '37:58'
    start_seconds: 2278
    title_fa: import و اجرای برنامه
    evidence_en: very top of our Python file
  - start: '38:48'
    start_seconds: 2328
    title_fa: پایان
    evidence_en: I'm Doug Lloyd
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: پایتون (Python)

> **منبع رسمی:** [صفحهٔ Short «Python» در CS50x](https://cs50.harvard.edu/x/shorts/python/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

ویدئو پایتون را زبانی پرکاربرد و همه‌منظوره معرفی می‌کند که کارهای دشوار C، مثل کار با رشته‌ها، را ساده‌تر می‌کند و از C الهام گرفته است. پایتون لزوماً کامپایل نمی‌شود؛ برنامه را مفسر خط‌به‌خط اجرا می‌کند. هشدار مهم ویدئو این است که CS50 **پایتون ۳** را درس می‌دهد و هنگام جست‌وجوی مستندات باید «Python 3» را بنویسی تا نتیجه‌های پایتون ۲ نیاید.

سپس ویدئو نحو C را کنار نحو پایتون می‌گذارد: متغیر فقط با مقداردهی ساخته می‌شود و نوع نمی‌خواهد؛ نقطه‌ویرگول لازم نیست؛ رشته نوع داخلی است و با کوتیشن یک‌تایی یا دوتایی نوشته می‌شود؛ شرط‌ها با `or`، `and`، `not`، `elif` و دونقطه نوشته می‌شوند و تورفتگی مهم است؛ `True` و `False` با حرف بزرگ‌اند؛ `input` ورودی می‌گیرد؛ و فقط دو حلقه هست، `while` و `for`، چون `do-while` و `++` وجود ندارند.

بخش میانی دربارهٔ ساختارهای داده است: `range` با شروع، پایان و گام؛ فهرست به جای آرایه، با اندازهٔ متغیر، `append`، `insert`، `len` و اشاره‌ای به list comprehension؛ **tuple** به عنوان مجموعه‌ای مرتب و تغییرناپذیر، با نمونهٔ فهرست رئیس‌جمهورها و سال آغاز کارشان؛ و **واژه‌نامه** که از نظر ایده به جدول درهم‌سازی نزدیک است، با نمونهٔ قیمت پیتزاها و پیمایش با `for pie in pizzas` و `pizzas.items()`.

بخش پایانی تابع‌ها (`def`، بدون نوع برگشتی و نوع پارامتر، عملگر توان `**`)، قرارداد `if __name__ == "__main__":`، **شیء‌ها** (ویژگی و متد، کلیدواژهٔ `class`، تابع `__init__` و پارامتر `self`)، اهمیت سبک و تورفتگی، `import cs50` و اجرای برنامه با `python file.py` را مرور می‌کند.

## نکته‌های کلیدی

- CS50 پایتون ۳ درس می‌دهد؛ در جست‌وجوی مستندات «Python 3» بنویس.
- متغیر فقط با مقداردهی ساخته می‌شود: `x = 54`؛ نوع و نقطه‌ویرگول لازم نیست.
- شرط‌ها با واژه‌های `or`، `and` و `not` نوشته می‌شوند؛ به جای `else if` از `elif` استفاده کن و پس از شرط دونقطه بگذار.
- `True` و `False` در پایتون با حرف بزرگ نوشته می‌شوند.
- پایتون `do-while` و `++` ندارد؛ بنویس `counter += 1`.
- `print` به‌طور پیش‌فرض در پایان سطر تازه می‌گذارد؛ `\n` لازم نیست.
- `range(0, 100, 2)` عددهای زوج از `0` تا `98` را می‌دهد؛ پایان ناشامل است.
- فهرست اندازهٔ ثابت ندارد و می‌تواند نوع‌های مختلف را نگه دارد؛ `nums.append(5)` به انتها می‌افزاید.
- tuple مرتب و تغییرناپذیر است و با پرانتز نوشته می‌شود، مثل `("George Washington", 1789)`.
- واژه‌نامه کلید را به مقدار نگاشت می‌کند؛ `for pie in pizzas` روی کلیدها و `for pie, price in pizzas.items()` روی جفت‌ها می‌چرخد.
- تابع با `def` تعریف می‌شود و نوع برگشتی یا نوع پارامتر نمی‌خواهد.
- متد تابعی است که به یک شیء تعلق دارد؛ کلاس با `class` تعریف می‌شود و هر متد پارامتر اول `self` دارد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`python.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — معرفی پایتون](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=0s)
- [۱:۳۰ — تفسیری، نه کامپایلی](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=90s)
- [۱:۵۹ — پایتون ۳](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=119s)
- [۲:۳۶ — متغیرها و رشته‌ها](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=156s)
- [۴:۰۹ — شرط‌ها و elif](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=249s)
- [۶:۳۲ — عملگر سه‌تایی و True/False](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=392s)
- [۷:۱۷ — input و حلقه‌ها](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=437s)
- [۹:۱۹ — range](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=559s)
- [۱۰:۱۱ — فهرست‌ها](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=611s)
- [۱۴:۳۹ — tuple](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=879s)
- [۱۸:۳۹ — واژه‌نامه](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=1119s)
- [۲۱:۲۶ — پیمایش واژه‌نامه](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=1286s)
- [۲۵:۰۰ — شیوه‌های قالب‌بندی رشته](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=1500s)
- [۲۵:۲۰ — تابع‌ها و main](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=1520s)
- [۲۷:۳۱ — شیء، کلاس و متد](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=1651s)
- [۳۵:۰۶ — سبک و تورفتگی](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=2106s)
- [۳۷:۵۸ — import و اجرای برنامه](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=2278s)
- [۳۸:۴۸ — پایان](https://www.youtube.com/watch?v=mgBpcQRDtl0&t=2328s)

> **ناهمخوانی (d113):** ویدئو (۲۰۱۷) می‌گوید ترتیب پیمایش واژه‌نامه تضمین‌شده نیست. **استنتاج:** از پایتون ۳٫۷ به بعد، زبان ترتیب افزودن کلیدها را حفظ می‌کند؛ با این حال اگر ترتیب برایت معنا دارد، فهرست روشن‌تر است.

> **ناهمخوانی (d114):** ویدئو قالب‌بندی رشته با `%` را «منسوخ» می‌نامد. مستندات پایتون ۳ آن را حذف نکرده‌اند، ولی برای کد تازه f-string یا `str.format` را توصیه می‌کنند؛ سخنرانی هم f-string را به کار می‌برد.

> **توجه (d108):** ویدئو در محیط CS50 IDE ضبط شده است؛ امروز در cs50.dev (VS Code) کار می‌کنی. همچنین در ویدئو یک بار گفته می‌شود `range 1000` ولی منظور `range(100)` است (عددهای ۰ تا ۹۹).

## مفاهیم مرتبط

- پایتون ۳ (نه پایتون ۲) — [یادداشت](/kb/d/w06-sh-python) · درس کوتاه `w06-l04` (واحد `w06-l04-u04`)
- زبان تفسیری: اجرای مستقیم با مفسر، بدون کامپایل جدا — [یادداشت](/kb/d/w06-n01) · درس کوتاه `w06-l01` (واحد `w06-l01-u01`)
- متغیر بدون اعلان نوع: counter = 0 — [یادداشت](/kb/d/w06-n05) · درس کوتاه `w06-l02` (واحد `w06-l02-u03`)
- or و and به جای || و && — [یادداشت](/kb/d/w06-n07) · درس کوتاه `w06-l03` (واحد `w06-l03-u02`)
- if، elif، else — [یادداشت](/kb/d/w06-n07) · درس کوتاه `w06-l03` (واحد `w06-l03-u01`)
- True و False با حرف بزرگ — [یادداشت](/kb/d/w06-sh-python) · درس کوتاه `w06-l04` (واحد `w06-l04-u04`)
- += به جای ++ (پایتون ++ ندارد) — [یادداشت](/kb/d/w06-n05) · درس کوتاه `w06-l02` (واحد `w06-l02-u03`)
- for i in range(n) — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u01`)
- فهرست (list): دنباله‌ای تغییرپذیر — [یادداشت](/kb/d/w06-n12) · درس کوتاه `w06-l06` (واحد `w06-l06-u03`)
- متد append برای افزودن به انتهای فهرست — [یادداشت](/kb/d/w06-n12) · درس کوتاه `w06-l06` (واحد `w06-l06-u03`)
- tuple: دنبالهٔ تغییرناپذیر — [یادداشت](/kb/d/w06-sh-python) · درس کوتاه `w06-l04` (واحد `w06-l04-u04`)
- دیکشنری (dict): جفت‌های کلید و مقدار — [یادداشت](/kb/d/w06-n13) · درس کوتاه `w06-l07` (واحد `w06-l07-u02`)
- پیمایش دیکشنری: کلیدها و items() — [یادداشت](/kb/d/w06-sh-python) · درس کوتاه `w06-l04` (واحد `w06-l04-u04`)
- تعریف تابع با def و پارامترها — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u03`)
- قرارداد main و فراخوانی main() در پایان فایل — [یادداشت](/kb/d/w06-n09) · درس کوتاه `w06-l04` (واحد `w06-l04-u03`)
- شیء و متد: تابعی که به یک مقدار تعلق دارد — [یادداشت](/kb/d/w06-n08) · درس کوتاه `w06-l03` (واحد `w06-l03-u03`)
- class، __init__ و self — [یادداشت](/kb/d/w06-sh-python) · درس کوتاه `w06-l04` (واحد `w06-l04-u04`)
- import و from ... import — [یادداشت](/kb/d/w06-n03) · درس کوتاه `w06-l01` (واحد `w06-l01-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/mgBpcQRDtl0) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/python/python.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/python/lang/en/python.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/python/lang/en/python.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
