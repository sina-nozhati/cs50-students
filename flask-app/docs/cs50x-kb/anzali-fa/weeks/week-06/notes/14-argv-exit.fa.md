---
id: w06-n14
type: note
title: آرگومان خط فرمان و وضعیت خروج (Command-Line Arguments and Exit Status)
title_fa: آرگومان خط فرمان و وضعیت خروج
title_en: Command-Line Arguments and Exit Status
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Command-Line Arguments
official_anchor: command-line-arguments
source_url: https://cs50.harvard.edu/x/2026/notes/6/#command-line-arguments
source_refs:
- src-notes-6#command-line-arguments
- src-notes-6#exit-status
- src-transcript-6
- src-python-docs
- src-anzali-authored-6
- src-srt-6
concept_ids:
- w06-c-sys-argv
- w06-c-sys-exit
prev: w06-n13
next: w06-n15
order: 14
video:
  youtube_id: Rl0ludWTLxs
  start: '2:08:51'
  start_seconds: 7731
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=7731s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'ability to give you access to command line'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# آرگومان خط فرمان و وضعیت خروج

> **منبع رسمی:** بخش «Command-Line Arguments» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#command-line-arguments). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۰۸:۵۱ تا حدود ۲:۱۴:۲۷](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=7731s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در C آرگومان‌های خط فرمان از پارامترهای `main` (`argc` و `argv`) می‌آمدند و وضعیت خروج با `return` از `main` برمی‌گشت. در پایتون `main` الزامی نیست؛ پس این دو از کتابخانهٔ `sys` می‌آیند. `check50` وضعیت خروج برنامه‌ات را بررسی می‌کند.

## آرگومان‌های خط فرمان

- مثل C می‌توانی از آرگومان‌های خط فرمان استفاده کنی. این کد را در نظر بگیر:

```python
# Prints a command-line argument

from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")
```

- `argv[1]` با یک **رشتهٔ قالب‌بندی‌شده** (f-string) چاپ شده است؛ همان `f` که در دستور `print` آمده.
- `argv` فهرستی از رشته‌هاست. `argv[0]` نام فایل برنامه است (اینجا `greet.py`)، نه `python`. پس با `python greet.py David` مقدار `len(argv)` برابر `2` است و خروجی `hello, David` (اجراشده روی جعبهٔ ساخت).
- دربارهٔ کتابخانهٔ `sys` در [مستندات پایتون](https://docs.python.org/3/library/sys.html) بیشتر بخوان.

> [!TIP]
> **تألیفی: argc کجاست؟**
> پایتون `argc` ندارد؛ `len(argv)` همان کار را می‌کند. و چون هر عضو `argv` رشته است، اگر آرگومان عددی می‌خواهی باید با `int(argv[1])` تبدیلش کنی.

## وضعیت خروج

- کتابخانهٔ `sys` متدهای داخلی هم دارد. با `sys.exit(i)` می‌شود برنامه را با کد خروج مشخصی تمام کرد:

```python
# Exits with explicit value, importing sys

import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)
```

- برای استفاده از تابع‌های داخلی `sys` از **نمادگذاری نقطه** استفاده شده است (`sys.argv` و `sys.exit`).
- اگر آرگومانی ندهی، برنامه `Missing command-line argument` چاپ می‌کند و با وضعیت `1` تمام می‌شود؛ سطرهای بعد از `sys.exit(1)` اجرا نمی‌شوند. می‌توانی وضعیت را با `echo $?` پس از اجرا ببینی (اجراشده روی جعبهٔ ساخت).

> [!IMPORTANT]
> **دو شکل import، دو شکل نام**
> `greet.py` نوشته `from sys import argv` و برای همین مستقیم `argv` را به کار می‌برد. `exit.py` نوشته `import sys` و باید `sys.argv` و `sys.exit` بنویسد. ترکیب نادرست این دو (مثلاً `import sys` و بعد `argv` بدون پیشوند) خطای `NameError` می‌دهد.

> [!NOTE]
> **از سخنرانی: from sys import argv**
> David گفت می‌توانست به جای `import sys` بنویسد `from sys import argv`؛ هر دو شکل درست‌اند و فقط نحوهٔ نام بردن را عوض می‌کنند.

## اشتباه‌های رایج

- انتظار اینکه `argv[0]` اولین آرگومان کاربر باشد؛ اولین آرگومان کاربر `argv[1]` است.
- `return 1` در سطح بالای فایل (بیرون از تابع)؛ خطای نحوی است. برای خروج با وضعیت از `sys.exit(1)` استفاده کن.
- مقایسهٔ `argv[1]` با عدد بدون تبدیل.

## جمع‌بندی

- `sys.argv` فهرست رشته‌هاست؛ `argv[0]` نام فایل برنامه.
- `len(sys.argv)` جای `argc` را می‌گیرد.
- `sys.exit(n)` برنامه را با وضعیت `n` تمام می‌کند.

## پیوندها

- قبلی: [جست‌وجو، in و دیکشنری](/kb/d/w06-n13)
- بعدی: [فایل CSV و کتابخانه‌های شخص ثالث](/kb/d/w06-n15)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
