---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۶ (Section 6)
title_fa: جلسهٔ حل تمرین هفتهٔ ۶
title_en: Section 6
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly, read in full); chapter times from section6.srt (inference for boundaries); str_prediction.py verbatim (syntax drill, not a pset solution); playlist.py and 2018_top100.csv link-only (completed DictReader filter, D47)
source_url: https://cs50.harvard.edu/x/sections/6/
source_refs:
- src-section-6#week-6-python
- src-section-6-transcript
- src-section-6-video
- src-section-6-code
- src-anzali-inference-6
- src-anzali-authored-6
concept_ids:
- w06-c-python-language
- w06-c-no-declaration
- w06-c-indentation-blocks
- w06-c-f-string
- w06-c-list
- w06-c-append
- w06-c-for-range
- w06-c-while-py
- w06-c-augmented-assignment
- w06-c-string-slicing
- w06-c-iterate-string
- w06-c-print-end
- w06-c-import
- w06-c-def-function
- w06-c-sys-argv
- w06-c-dict
- w06-c-list-of-dicts
- w06-c-with-open
- w06-c-csv-dictreader
- w06-c-input-returns-str
- w06-c-try-except
prev: w06-summary
next: w06-sh-python
order: 17
video:
  youtube_id: SHbahshnkAs
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: 'خوش‌آمد: از C به پایتون'
    evidence_en: null
  - start: '1:00'
    start_seconds: 60
    title_fa: سطح پایین و سطح بالا
    evidence_en: low level
  - start: '2:27'
    start_seconds: 147
    title_fa: چرا CS50 با C شروع می‌کند
    evidence_en: why might you think
  - start: '5:00'
    start_seconds: 300
    title_fa: input، == و f-string
    evidence_en: string compare
  - start: '8:35'
    start_seconds: 515
    title_fa: فهرست‌ها
    evidence_en: So moving to lists
  - start: '10:40'
    start_seconds: 640
    title_fa: حلقهٔ for و range
    evidence_en: moving out the loops
  - start: '15:10'
    start_seconds: 910
    title_fa: تمرین پیش‌بینی range
    evidence_en: imagine what each of these
  - start: '18:11'
    start_seconds: 1091
    title_fa: حلقهٔ while و +=
    evidence_en: And so while loops
  - start: '19:06'
    start_seconds: 1146
    title_fa: برش رشته
    evidence_en: string splicing as we call it
  - start: '21:21'
    start_seconds: 1281
    title_fa: import
    evidence_en: a few more functionalities
  - start: '22:22'
    start_seconds: 1342
    title_fa: def
    evidence_en: creating our own functions
  - start: '23:04'
    start_seconds: 1384
    title_fa: sys.argv
    evidence_en: functionality with comma
  - start: '24:18'
    start_seconds: 1458
    title_fa: 'str_prediction: دور ۱'
    evidence_en: string prediction
  - start: '27:13'
    start_seconds: 1633
    title_fa: دور ۲
    evidence_en: Round 2.
  - start: '29:10'
    start_seconds: 1750
    title_fa: دور ۳
    evidence_en: move on to round 3
  - start: '30:32'
    start_seconds: 1832
    title_fa: دور ۴
    evidence_en: move on to round 4
  - start: '31:50'
    start_seconds: 1910
    title_fa: دور ۵
    evidence_en: Round 5.
  - start: '33:07'
    start_seconds: 1987
    title_fa: 'دور ۶: برعکس کردن رشته'
    evidence_en: So now for around 6
  - start: '34:35'
    start_seconds: 2075
    title_fa: خطای string index out of range
    evidence_en: String index out of range
  - start: '36:58'
    start_seconds: 2218
    title_fa: واژه‌نامه‌ها
    evidence_en: a thing called dictionaries
  - start: '40:00'
    start_seconds: 2400
    title_fa: فهرستی از واژه‌نامه‌ها
    evidence_en: list of dictionaries.
  - start: '43:55'
    start_seconds: 2635
    title_fa: with open و csv.DictReader
    evidence_en: library called Dict Reader
  - start: '47:34'
    start_seconds: 2854
    title_fa: تمرین playlist.py
    evidence_en: Playlist at Pie
  - start: '54:40'
    start_seconds: 3280
    title_fa: خطای مقایسهٔ str و int و تبدیل با float
    evidence_en: comparison is not supported
  chapters_origin: inference
code_files:
- file: str_prediction.py
  policy: verbatim
- file: playlist.py
  policy: link-only
  reason: completed CSV DictReader filtering exercise; students should write it along with the section (D47)
- file: 2018_top100.csv
  policy: link-only
  reason: data file for playlist.py
---

# جلسهٔ حل تمرین هفتهٔ ۶ (Section)

> **منبع رسمی:** [صفحهٔ Section 6 CS50x](https://cs50.harvard.edu/x/sections/6/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/6/lang/en/section6.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، مدرس (preceptor) CS50 در هاروارد، اداره می‌کند و سه بخش دارد: نحو تازهٔ پایتون در مقایسه با C، تمرین پیش‌بینی خروجی با رشته‌ها، و کار با واژه‌نامه و فایل CSV.

بخش اول **مقایسهٔ C و پایتون** است. C زبانی **سطح پایین** و پایتون زبانی **سطح بالا** است که روی C ساخته شده و مدیریت حافظه را خودکار کرده است؛ دیگر `malloc` و `free` نمی‌نویسی. نوع متغیرها را مفسر تشخیص می‌دهد. Kelly می‌پرسد چرا CS50 با C شروع می‌کند و پاسخ شرکت‌کننده‌ها این است که C بنیادها را بهتر یاد می‌دهد، چون باید بفهمی رایانه واقعاً چه می‌کند. بعد مقایسه‌ها می‌آیند: `name = input(...)` به جای `get_string` با نوع صریح، نبودن نقطه‌ویرگول، مقایسهٔ مستقیم رشته‌ها با `==` (در C چون رشته نشانی است باید از `strcmp` استفاده می‌کردی)، نبودن آکولاد و اهمیت **تورفتگی**، و f-string به جای `%s`.

سپس **فهرست‌ها** می‌آیند: شبیه آرایه‌اند، ولی نوع اعلان نمی‌شود، می‌توانند نوع‌های گوناگون را نگه دارند و طولشان ثابت نیست (`append` و حذف). حلقهٔ `for` روی عضوهای یک فهرست می‌چرخد و `range` با سه پارامتر شروع (پیش‌فرض `0`، شامل)، پایان (ناشامل) و گام (پیش‌فرض `1`) کار را ساده می‌کند. شرکت‌کننده‌ها خروجی چند `range` را پیش‌بینی می‌کنند، مثلاً `range(1, 3, 2)` فقط `1` است و `range(5, 0, -1)` عددهای `5` تا `1` است. حلقهٔ `while` تقریباً همان است، ولی `n++` در پایتون نیست و باید `n += 1` بنویسی. Kelly **برش رشته** را با `"wahoo"` نشان می‌دهد: `phrase[0]` نویسهٔ `w` است و `phrase[1:3]` نویسه‌های `a` و `h` را می‌دهد. در پایان این بخش `import cs50` و `cs50.get_int` در برابر `from cs50 import get_int`، تعریف تابع با `def` و `sys.argv` را مرور می‌کند؛ پایتون معادل مستقیم `argc` ندارد و به جایش `len(sys.argv)` را به کار می‌بری.

بخش دوم تمرین **`str_prediction.py`** است: شش «دور» که در هر کدام رشته‌ای از کاربر گرفته و بخشی از آن نویسه‌به‌نویسه با `end=""` چاپ می‌شود. دور ۱ با گام `2` یک نویسه در میان چاپ می‌کند؛ دور ۲ نویسهٔ اول و آخر را نمی‌آورد؛ دور ۳ و ۵ همهٔ رشته را چاپ می‌کنند (یکی با `for` روی رشته و دیگری با `while`)؛ دور ۴ با `phrase[1:]` نویسهٔ اول را حذف می‌کند. دور ۶ چالش است: رشته را فقط با تغییر آرگومان‌های `range` برعکس کن. تلاش اول با شروع از `len(phrase)` خطای **`string index out of range`** می‌دهد، چون آخرین نمایه `len(phrase) - 1` است؛ تلاش دوم با پایان `0` نویسهٔ اول را جا می‌اندازد، چون پایان ناشامل است؛ با پایان `-1` درست کار می‌کند.

بخش سوم **واژه‌نامه** است: جفت‌های کلید و مقدار، مثلاً آهنگی با کلید `name` و `tempo`. با `song["name"]` مقدار را می‌خوانی، با انتساب آن را عوض می‌کنی یا کلید تازه می‌افزایی، و متدهای `keys()` و `values()` کلیدها و مقدارها را می‌دهند. فهرستی از واژه‌نامه‌ها هم ممکن است: `songs[2]["tempo"]`. بعد فایل CSV صد آهنگ برتر سال ۲۰۱۸ می‌آید: `with open(...) as file` فایل را فقط درون بلوک باز نگه می‌دارد و `csv.DictReader` هر سطر را واژه‌نامه‌ای با کلیدهای سطر سرآیند می‌کند (`fieldnames` نام ستون‌ها را می‌دهد).

در پایان Kelly برنامهٔ **`playlist.py`** را با شرکت‌کننده‌ها کامل می‌کند: کمینه و بیشینهٔ tempo از کاربر گرفته می‌شود و آهنگ‌هایی که در این بازه‌اند به فهرست افزوده و نامشان چاپ می‌شود. در میانه خطای مقایسه‌ای با پیام `not supported between instances of 'str' and 'int'` پیدا می‌شود، چون هر مقداری که از CSV خوانده می‌شود **رشته** است و باید با `float` تبدیل شود. یکی از شرکت‌کننده‌ها پیشنهاد `try` و `except` را برای تبدیل می‌دهد و Kelly آن را «فکر درستی برای پرابلم‌ست» می‌داند. جلسه با اشاره به هفتهٔ ۷ و SQL تمام می‌شود.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section6.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — خوش‌آمد: از C به پایتون](https://www.youtube.com/watch?v=SHbahshnkAs&t=0s)
- [۱:۰۰ — سطح پایین و سطح بالا](https://www.youtube.com/watch?v=SHbahshnkAs&t=60s)
- [۲:۲۷ — چرا CS50 با C شروع می‌کند](https://www.youtube.com/watch?v=SHbahshnkAs&t=147s)
- [۵:۰۰ — input، == و f-string](https://www.youtube.com/watch?v=SHbahshnkAs&t=300s)
- [۸:۳۵ — فهرست‌ها](https://www.youtube.com/watch?v=SHbahshnkAs&t=515s)
- [۱۰:۴۰ — حلقهٔ for و range](https://www.youtube.com/watch?v=SHbahshnkAs&t=640s)
- [۱۵:۱۰ — تمرین پیش‌بینی range](https://www.youtube.com/watch?v=SHbahshnkAs&t=910s)
- [۱۸:۱۱ — حلقهٔ while و +=](https://www.youtube.com/watch?v=SHbahshnkAs&t=1091s)
- [۱۹:۰۶ — برش رشته](https://www.youtube.com/watch?v=SHbahshnkAs&t=1146s)
- [۲۱:۲۱ — import](https://www.youtube.com/watch?v=SHbahshnkAs&t=1281s)
- [۲۲:۲۲ — def](https://www.youtube.com/watch?v=SHbahshnkAs&t=1342s)
- [۲۳:۰۴ — sys.argv](https://www.youtube.com/watch?v=SHbahshnkAs&t=1384s)
- [۲۴:۱۸ — str_prediction: دور ۱](https://www.youtube.com/watch?v=SHbahshnkAs&t=1458s)
- [۲۷:۱۳ — دور ۲](https://www.youtube.com/watch?v=SHbahshnkAs&t=1633s)
- [۲۹:۱۰ — دور ۳](https://www.youtube.com/watch?v=SHbahshnkAs&t=1750s)
- [۳۰:۳۲ — دور ۴](https://www.youtube.com/watch?v=SHbahshnkAs&t=1832s)
- [۳۱:۵۰ — دور ۵](https://www.youtube.com/watch?v=SHbahshnkAs&t=1910s)
- [۳۳:۰۷ — دور ۶: برعکس کردن رشته](https://www.youtube.com/watch?v=SHbahshnkAs&t=1987s)
- [۳۴:۳۵ — خطای string index out of range](https://www.youtube.com/watch?v=SHbahshnkAs&t=2075s)
- [۳۶:۵۸ — واژه‌نامه‌ها](https://www.youtube.com/watch?v=SHbahshnkAs&t=2218s)
- [۴۰:۰۰ — فهرستی از واژه‌نامه‌ها](https://www.youtube.com/watch?v=SHbahshnkAs&t=2400s)
- [۴۳:۵۵ — with open و csv.DictReader](https://www.youtube.com/watch?v=SHbahshnkAs&t=2635s)
- [۴۷:۳۴ — تمرین playlist.py](https://www.youtube.com/watch?v=SHbahshnkAs&t=2854s)
- [۵۴:۴۰ — خطای مقایسهٔ str و int و تبدیل با float](https://www.youtube.com/watch?v=SHbahshnkAs&t=3280s)

## کد رسمی جلسه

دو فایل کد و یک فایل داده در [src6.zip](https://cdn.cs50.net/2025/fall/sections/6/src6.zip) هست.

`str_prediction.py`: شش دور پیش‌بینی خروجی با `range`، برش و `while`. این فایل بخشی از راه‌حل هیچ پرابلم‌ستی نیست و فقط نحو حلقه و رشته را تمرین می‌دهد، برای همین متن کاملش اینجا آمده است:

```python
# Round 1
phrase = input("Give me a string: ")

for i in range(0, len(phrase), 2):
    print(phrase[i], end="")
print("")


# Round 2
phrase = input("Give me a string: ")

for i in range(1, len(phrase) - 1):
    print(phrase[i], end="")
print("")


# Round 3
phrase = input("Give me a string: ")

for character in phrase:
    print(character, end="")
print("")


# Round 4
phrase = input("Give me a string: ")

for character in phrase[1:]:
    print(character, end="")
print("")


# Round 5
phrase = input("Give me a string: ")

i = 0
while i < len(phrase):
    print(phrase[i], end="")
    i += 1
print("")


# Round 6: Reverse phrase, only by changing the range function's arguments
phrase = input("Give me a string: ")

for i in range(len(phrase) - 1, -1, -1):
    print(phrase[i], end="")
print("")
```

> **تألیفی:** پیش از اجرای هر دور، خروجی را برای رشته‌ای مثل `elephant` روی کاغذ پیش‌بینی کن. درس کوتاه این هفته یک تمرین پیش‌بینی خروجی بر پایهٔ همین فایل دارد.

`playlist.py` و `2018_top100.csv`: **فقط پیوند** (تصمیم D47). نسخهٔ موجود در zip کامل‌شده است و الگوی خواندن CSV با `DictReader`، تبدیل با `float` و پالایش سطرها را یکجا نشان می‌دهد؛ بهتر است خودت آن را در جلسه همراه Kelly بنویسی: [فهرست src6](https://cdn.cs50.net/2025/fall/sections/6/src6/).

## نکته‌های کلیدی

- پایتون سطح بالاست: مدیریت حافظه خودکار است، نوع اعلان نمی‌شود و رشته‌ها با `==` مقایسه می‌شوند.
- تورفتگی جای آکولاد را می‌گیرد و بخشی از معنای برنامه است.
- در `range(start, stop, step)` و در برش `s[start:stop:step]` شروع شامل و پایان ناشامل است.
- `n++` در پایتون نیست؛ `n += 1` بنویس.
- آخرین نمایهٔ رشته `len(s) - 1` است؛ نمایهٔ `len(s)` خطای `IndexError` می‌دهد.
- هر مقداری که از `input` یا از فایل CSV می‌خوانی رشته است؛ برای مقایسهٔ عددی تبدیلش کن.
- `csv.DictReader` هر سطر را به واژه‌نامه‌ای با کلیدهای سطر سرآیند تبدیل می‌کند.

> **تألیفی:** برای DNA این جلسه مهم است، چون آن مسئله هم CSV می‌خواند و عددهای درون آن رشته‌اند. ولی کد شمردن STRها را خودت باید بنویسی؛ این بسته آن را ارائه نمی‌دهد.

## پیوندها

- [صفحهٔ Section 6](https://cs50.harvard.edu/x/sections/6/) · [ویدئو](https://video.cs50.io/SHbahshnkAs) · [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/sections/6/section6.pdf)
- [کد منبع (zip)](https://cdn.cs50.net/2025/fall/sections/6/src6.zip) · [متن گفتار](https://cdn.cs50.net/2025/fall/sections/6/lang/en/section6.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
