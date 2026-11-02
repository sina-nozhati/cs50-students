---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sh-functions
type: short-summary
title: 'ویدئوی کوتاه: توابع (Functions)'
title_fa: توابع
title_en: Functions
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/functions/
source_refs:
- src-short-functions
- src-anzali-inference-2
concept_ids:
- w02-c-function-anatomy
- w02-c-function-benefits
prev: w02-sec
next: w02-sh-variables-and-scope
order: 22
video:
  youtube_id: n1glFqt3g38
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: تابع به‌عنوان جعبهٔ سیاه
    evidence_en: null
  - start: '1:22'
    start_seconds: 82
    title_fa: چرا جعبهٔ سیاه؟
    evidence_en: black box
  - start: '4:04'
    start_seconds: 244
    title_fa: چرا از تابع استفاده کنیم
    evidence_en: So why do we use functions
  - start: '5:08'
    start_seconds: 308
    title_fa: اعلان تابع
    evidence_en: declare the function
  - start: '5:53'
    start_seconds: 353
    title_fa: سه بخش اعلان
    evidence_en: three parts
  - start: '8:36'
    start_seconds: 516
    title_fa: 'تمرین: ضرب دو عدد اعشاری'
    evidence_en: multiplies two floating point
  - start: '10:15'
    start_seconds: 615
    title_fa: تعریف تابع
    evidence_en: definition
  - start: '13:58'
    start_seconds: 838
    title_fa: فراخوانی تابع
    evidence_en: To call a function
  - start: '17:16'
    start_seconds: 1036
    title_fa: ورودی و خروجی void
    evidence_en: void argument list
  - start: '17:37'
    start_seconds: 1057
    title_fa: تمرین valid triangle
    evidence_en: valid triangle
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: توابع (Functions)

> **منبع رسمی:** [صفحهٔ Short «Functions» در CS50x](https://cs50.harvard.edu/x/shorts/functions/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو تابع را یک «جعبهٔ سیاه» معرفی می‌کند: صفر یا چند ورودی می‌گیرد و یک خروجی می‌دهد. وقتی تابع را خودمان ننوشته‌ایم، لازم نیست بدانیم درونش چطور پیاده‌سازی شده؛ فقط باید رفتارش قابل‌پیش‌بینی باشد. برای همین نام روشن و مستندسازی مهم است.

بعد سه کار اصلی را می‌بینی: اعلان تابع (declaration)، تعریف آن (definition) و فراخوانی آن (call). در پایان یک تمرین تابع `valid_triangle` حل می‌شود.

## نکته‌های کلیدی

- یک تابع مثل `mult` را می‌شود به چند شکل پیاده کرد (ضرب مستقیم یا جمع تکراری)؛ تا وقتی خروجی درست است، پیاده‌سازی درون جعبهٔ سیاه برای کاربر مهم نیست.
- سه دلیل برای نوشتن تابع: سازمان‌دهی (شکستن مسئلهٔ بزرگ به بخش‌های کوچک)، ساده‌سازی (اشکال‌زدایی تابع ۱۰خطی آسان‌تر از ۱۰۰۰خطی است) و استفادهٔ دوباره.
- اعلان تابع به کامپایلر خبر می‌دهد که تابعی بعداً می‌آید. معمولاً همهٔ اعلان‌ها را بالای کد، پیش از `main`، می‌گذاریم.
- اعلان سه بخش دارد: نوع بازگشتی، نام و فهرست آرگومان‌ها (هر کدام با نوع و نام، جداشده با ویرگول). اعلان با `;` تمام می‌شود.
- سرآغاز تعریف همان اعلان است، بدون `;` و با `{`. با `return` خروجی جعبهٔ سیاه را برمی‌گردانیم.
- برای فراخوانی، آرگومان‌هایی از نوع مورد انتظار بده و مقدار بازگشتی را در متغیری از نوع درست ذخیره کن.
- تابعی که ورودی ندارد فهرست آرگومان `void` دارد (مثل `main` تا اینجا) و تابعی که خروجی ندارد نوع بازگشتی `void` دارد.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`functions.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — تابع به‌عنوان جعبهٔ سیاه](https://www.youtube.com/watch?v=n1glFqt3g38&t=0s)
- [۱:۲۲ — چرا جعبهٔ سیاه؟](https://www.youtube.com/watch?v=n1glFqt3g38&t=82s)
- [۴:۰۴ — چرا از تابع استفاده کنیم](https://www.youtube.com/watch?v=n1glFqt3g38&t=244s)
- [۵:۰۸ — اعلان تابع](https://www.youtube.com/watch?v=n1glFqt3g38&t=308s)
- [۵:۵۳ — سه بخش اعلان](https://www.youtube.com/watch?v=n1glFqt3g38&t=353s)
- [۸:۳۶ — تمرین: ضرب دو عدد اعشاری](https://www.youtube.com/watch?v=n1glFqt3g38&t=516s)
- [۱۰:۱۵ — تعریف تابع](https://www.youtube.com/watch?v=n1glFqt3g38&t=615s)
- [۱۳:۵۸ — فراخوانی تابع](https://www.youtube.com/watch?v=n1glFqt3g38&t=838s)
- [۱۷:۱۶ — ورودی و خروجی void](https://www.youtube.com/watch?v=n1glFqt3g38&t=1036s)
- [۱۷:۳۷ — تمرین valid triangle](https://www.youtube.com/watch?v=n1glFqt3g38&t=1057s)

## مفاهیم مرتبط

- اجزای اعلان تابع: نوع بازگشتی، نام، فهرست آرگومان‌ها — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)
- چرا تابع: سازمان‌دهی، ساده‌سازی، استفادهٔ دوباره — [یادداشت](/kb/d/w02-sh-functions) · درس کوتاه `w02-l05` (واحد `w02-l05-u03`)

## منابع

- [ویدئو در YouTube](https://youtu.be/n1glFqt3g38) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/functions/functions.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
