---
week: 6
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
generated_at: '2026-10-29T05:00:00+03:30'
review_status: draft-needs-human-review
id: w06-summary
type: week-summary
title: خلاصهٔ هفتهٔ ۶ (Summing Up)
title_fa: خلاصهٔ هفتهٔ ۶
title_en: Summing Up
parent: w06-fa
source_type: translated-rewritten
origin: mixed
origin_detail: First section is a faithful rewrite of 'Summing Up'; quick-review table is authored. Designed to replace the English official summary on /kb/week/6 (see integration/week-summary-overrides).
official_section: Summing Up
official_anchor: summing-up
source_url: https://cs50.harvard.edu/x/notes/6/#summing-up
source_refs:
- src-notes-6#summing-up
- src-week-6#week-6-python
- src-anzali-authored-6
prev: w06-n15
next: w06-sec
order: 16
replaces_official_summary_for: week-6
---

# خلاصهٔ هفتهٔ ۶: پایتون

> **منبع رسمی:** این خلاصه بازنویسی فارسی بخش «Summing Up» از [درس‌نامهٔ هفتهٔ ۶](https://cs50.harvard.edu/x/notes/6/#summing-up) است. جدول «مرور سریع» **تألیفی** است.

## در این هفته چه یاد گرفتی؟

درس‌نامه می‌گوید در این درس یاد گرفتی بلوک‌های سازندهٔ برنامه‌نویسی از درس‌های قبل چطور در پایتون پیاده می‌شوند، پایتون چطور کد ساده‌تری را ممکن می‌کند و چطور از کتابخانه‌های گوناگون پایتون استفاده کنی. در پایان یاد گرفتی که مهارت‌هایت به عنوان برنامه‌نویس به یک زبان محدود نیست؛ و داری راه تازه‌ای برای یادگیری کشف می‌کنی که در هر زبان برنامه‌نویسی، و شاید تقریباً در هر زمینهٔ یادگیری، به کارت می‌آید. به‌طور مشخص این‌ها را دیدی:

- پایتون.
- متغیرها.
- شرط‌ها.
- حلقه‌ها.
- نوع‌ها.
- برنامه‌نویسی شیءگرا.
- بریدن و عدم دقت ممیز شناور.
- استثناها.
- واژه‌نامه‌ها.
- آرگومان‌های خط فرمان.
- کتابخانه‌های شخص ثالث.

## مرور سریع

> **تألیفی:** خلاصهٔ یک‌خطی هر مفهوم، با پیوند به یادداشت کامل.

| مفهوم | یک جمله | یادداشت |
| --- | --- | --- |
| زبان تفسیری | با `python file.py` اجرا می‌شود؛ کامپایل جداگانه ندارد. | [سلام پایتون](/kb/d/w06-n01) |
| بهای سطح بالا | کد کوتاه‌تر، اما احتمالاً کندتر و با کنترل کمتر بر حافظه. | [Speller و Filter](/kb/d/w06-n02) |
| import | `import cs50` و `cs50.get_int`، یا `from cs50 import get_int`. | [تابع‌ها و کتابخانه‌ها](/kb/d/w06-n03) |
| f-string | `f"hello, {answer}"` مقدار را درون رشته می‌گذارد. | [رشته‌ها](/kb/d/w06-n04) |
| sep و end | پارامترهای نام‌دار `print`؛ پیش‌فرض فاصله و سطر تازه. | [رشته‌ها](/kb/d/w06-n04) |
| نوع‌ها | بدون اعلان؛ `int` سرریز نمی‌کند؛ `long` و `double` نیست. | [متغیرها و نوع‌ها](/kb/d/w06-n05) |
| input | همیشه `str` برمی‌گرداند؛ برای عدد `int(...)`. | [ماشین‌حساب](/kb/d/w06-n06) |
| شرط | تورفتگی، دونقطه، `elif`، `or` و `and`، `in`. | [شرط‌ها](/kb/d/w06-n07) |
| متد | تابع درون شیء؛ متد رشته رشتهٔ تازه برمی‌گرداند. | [شیءگرایی](/kb/d/w06-n08) |
| حلقه و main | `for i in range(n)`؛ `def`؛ `main()` در پایان فایل. | [حلقه‌ها و انتزاع](/kb/d/w06-n09) |
| / و // | `/` همیشه `float`؛ `//` تقسیم کف؛ عدم دقت هنوز هست. | [تقسیم و استثنا](/kb/d/w06-n10) |
| استثنا | `try` و `except ValueError` خطای تبدیل را می‌گیرد. | [تقسیم و استثنا](/kb/d/w06-n10) |
| while True | جای `do-while`؛ با `break` بیرون می‌آیی. | [Mario](/kb/d/w06-n11) |
| list | `append`، `len`، `sum`، نمایه و برش. | [فهرست‌ها](/kb/d/w06-n12) |
| dict | کلید و مقدار؛ `in` فقط کلیدها را می‌گردد. | [جست‌وجو و واژه‌نامه](/kb/d/w06-n13) |
| sys | `sys.argv` فهرست رشته‌ها؛ `sys.exit(n)` وضعیت خروج. | [خط فرمان](/kb/d/w06-n14) |
| csv | `csv.writer`، `csv.DictWriter` و `with open`. | [CSV و کتابخانه‌ها](/kb/d/w06-n15) |

## گام بعدی

- اگر هنوز نگذرانده‌ای، [آزمون تسلط هفته](/kb/d/w06-fa) را بده.
- سپس به [پرابلم‌ست ۶](https://cs50.harvard.edu/x/psets/6/) برو. راهنماهای فارسی از [نمای کلی هفته](/kb/d/w06-fa) در دسترس‌اند.

> **پیوند رسمی:** متن کامل انگلیسی در [cs50.harvard.edu/x/notes/6](https://cs50.harvard.edu/x/notes/6/) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
