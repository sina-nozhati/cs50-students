---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-pr-license
type: practice-guide
title: راهنمای پلاک‌خوان (License)
title_fa: پلاک‌خوان (License)
title_en: License
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Summary and requirements: Persian rewrite of the official page; hints, checklist and common mistakes authored; official sample I/O and commands verbatim; NO solution'
source_url: https://cs50.harvard.edu/x/2026/practice/license/
source_refs:
- src-practice-license#implementation-details
- src-practice-license#checking-for-memory-leaks
- src-anzali-authored-4
concept_ids:
- w04-c-string-char-star
- w04-c-pointer-copy
- w04-c-strcpy
- w04-c-malloc
- w04-c-free
- w04-c-valgrind
- w04-c-memory-leak
- w04-c-file-pointer
- w04-c-fprintf-fclose
- w04-c-fread-fwrite
problem_set_ref: weeks/week-04/problem-sets/license.json
prev: w04-pr-bottomup
next: null
order: 28
submission: optional-practice
deadline_utc: null
deadline_tehran: null
---

# راهنمای پلاک‌خوان (License)

> **منبع رسمی:** [License](https://cs50.harvard.edu/x/2026/practice/license/) از مسئله‌های تمرینی هفتهٔ ۴ CS50x 2026. بخش‌های «خلاصه» و «خواسته‌ها» بازنویسی فارسی صفحهٔ رسمی‌اند. راهنمایی، چک‌لیست و اشتباه‌های رایج **تألیفی** هستند. **این راهنما راه‌حل ارائه نمی‌دهد.**

> **وضعیت تحویل:** تمرین اختیاری است؛ تحویل ندارد.

## خلاصهٔ مسئله

در شرکتی کار می‌کنی که فناوری تشخیص پلاک خودرو می‌سازد. فایل متنی `plates.txt` هشت شمارهٔ پلاک دارد و برنامه‌ای که باید آن‌ها را بخواند و چاپ کند، فقط آخرین پلاک را هشت بار چاپ می‌کند.

کد آغازین `license.c` چند خطا دارد: هم خطای منطقی (چه چیزی واقعاً در آرایه ذخیره می‌شود؟) و هم دو خطای حافظه که `valgrind` نشان می‌دهد. باید با `debug50` و `valgrind` آن‌ها را پیدا و اصلاح کنی.

> **از سخنرانی:** تفاوت کپی نشانی و کپی محتوا در [یادداشت کپی کردن](/kb/d/w04-n08) و [malloc و free](/kb/d/w04-n09)، و خواندن گزارش `valgrind` در [یادداشت Valgrind](/kb/d/w04-n10) آمده است.

## خواسته‌های رسمی

1. خطاهای کد آغازین را اصلاح کن تا هر هشت پلاک درست چاپ شوند.
2. وقتی برنامه درست کار کرد، با `valgrind` مطمئن شو نشت حافظه ندارد.
3. دو نوع خطای حافظه در گزارش هست که باید اصلاح شوند.

## شروع کار

در ترمینال cs50.dev اول `cd` را تنها اجرا کن، بعد فایل‌ها را با فرمان رسمی دانلود کن (نشانی دانلود قدیمی‌تر است؛ ناهمخوانی d63). در پوشه `license.c` و `plates.txt` هست. اول برنامه را همان‌طور که هست اجرا کن تا خطا را ببینی.

فایل آغازین رسمی را دانلود کن (پیش از آن `cd` را تنها اجرا کن):

```bash
wget https://cdn.cs50.net/2022/fall/labs/4/license.zip
unzip license.zip
rm license.zip
```

## نمونه‌های رسمی ورودی و خروجی

خروجی درست:

```text
license/ $ ./license plates.txt
11ZT00
1KAD21
78ZZ01
99ZZ11
72ZZ21
98ZZ31
44ZW41
34ZZ51
```

## مفاهیم لازم

پیش از شروع، این مفاهیم را مرور کن:

- رشته همان char * است: نشانی اولین نویسه — [یادداشت](/kb/d/w04-n05) · درس کوتاه `w04-l03` (واحد `w04-l03-u01`)
- t = s فقط نشانی را کپی می‌کند: دو نام برای یک رشته — [یادداشت](/kb/d/w04-n08) · درس کوتاه `w04-l04` (واحد `w04-l04-u01`)
- strcpy برای کپی کردن محتوای رشته — [یادداشت](/kb/d/w04-n09) · درس کوتاه `w04-l04` (واحد `w04-l04-u03`)
- malloc: گرفتن چند بایت حافظه از سیستم عامل — [یادداشت](/kb/d/w04-n09) · درس کوتاه `w04-l04` (واحد `w04-l04-u02`)
- free: پس دادن حافظه‌ای که malloc داده است — [یادداشت](/kb/d/w04-n09) · درس کوتاه `w04-l04` (واحد `w04-l04-u02`)
- valgrind: ابزار یافتن خطاهای حافظه — [یادداشت](/kb/d/w04-n10) · درس کوتاه `w04-l05` (واحد `w04-l05-u01`)
- نشت حافظه: malloc بدون free — [یادداشت](/kb/d/w04-n10) · درس کوتاه `w04-l05` (واحد `w04-l05-u01`)
- FILE * و fopen با حالت r، w، a — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- fprintf برای نوشتن در فایل و fclose برای بستن — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u01`)
- fread و fwrite: خواندن و نوشتن بایت‌ها — [یادداشت](/kb/d/w04-n15) · درس کوتاه `w04-l07` (واحد `w04-l07-u02`)

## راهنمایی مرحله‌ای

> **تألیفی:** این راهنمایی‌ها فقط جهت فکر کردن را نشان می‌دهند و کد نمی‌دهند. یکی‌یکی باز کن.

1. با `debug50` یک نقطهٔ توقف داخل حلقهٔ خواندن بگذار و بعد از هر دور، نشانی‌ای را که در هر خانهٔ آرایه ذخیره شده ببین. چند نشانی متفاوت می‌بینی؟
2. یادداشت «کپی کردن» را به یاد بیاور: وقتی یک آرایهٔ `char` را به یک `char *` نسبت می‌دهی، چه چیزی کپی می‌شود، محتوا یا نشانی؟
3. اگر هر پلاک باید جای خودش را در حافظه داشته باشد، آن جا از کجا می‌آید؟ و بعد از آن، محتوا چطور به آن‌جا می‌رسد؟
4. گزارش `valgrind` دو جا را نشان می‌دهد: یکی کنار `malloc` و یکی کنار `fopen`. هر کدام به کدام قانون «هر چیزی که گرفتی پس بده» مربوط است؟

## اشتباه‌های رایج

- کپی نشانی به‌جای کپی محتوا
- گرفتن حافظه بدون آزاد کردن همهٔ آن
- فراموش کردن بستن فایل
- جا نگذاشتن برای `\0`

## چک‌لیست خودآزمایی

1. هر هشت پلاک، هر کدام یک بار و به ترتیب، چاپ می‌شوند.
2. با `debug50` دیده‌ام هر خانهٔ آرایه به کجا اشاره می‌کند.
3. `valgrind` «definitely lost» نشان نمی‌دهد.
4. هر فایلی که باز شده، بسته شده است.
5. check50 همه را سبز نشان می‌دهد.
6. style50 تغییری پیشنهاد نمی‌کند.

## بررسی نشت حافظه با valgrind

صفحهٔ رسمی این را پیشنهاد می‌کند:

فرمان رسمی:

```bash
valgrind ./license plates.txt
```

نمونهٔ گزارش رسمی پیش از اصلاح (شماره‌خط‌های تو ممکن است فرق کند):

```bash
==24478== HEAP SUMMARY:
==24478==     in use at exit: 528 bytes in 9 blocks
==24478==   total heap usage: 10 allocs, 1 frees, 4,624 bytes allocated
==24478== 
==24478== 56 bytes in 8 blocks are definitely lost in loss record 1 of 2
==24478==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==24478==    by 0x109207: main (license.c:30)
==24478== 
==24478== 472 bytes in 1 blocks are still reachable in loss record 2 of 2
==24478==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==24478==    by 0x4A086CD: __fopen_internal (iofopen.c:65)
==24478==    by 0x4A086CD: fopen@@GLIBC_2.2.5 (iofopen.c:86)
==24478==    by 0x1091CD: main (license.c:20)
==24478== 
==24478== LEAK SUMMARY:
==24478==    definitely lost: 56 bytes in 8 blocks
==24478==    indirectly lost: 0 bytes in 0 blocks
==24478==      possibly lost: 0 bytes in 0 blocks
==24478==    still reachable: 472 bytes in 1 blocks
==24478==         suppressed: 0 bytes in 0 blocks
==24478== 
==24478== For lists of detected and suppressed errors, rerun with: -s
==24478== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

## آزمون و تحویل

درستی با check50:

```bash
check50 cs50/labs/2023/x/license
```

سبک با style50:

```bash
style50 license.c
```

این مسئله تحویل ندارد.

## فقط پیوند

> **سیاست بدون راه‌حل:** موارد زیر در صفحهٔ رسمی هست ولی در این بسته بازتولید نشده است.

- [راهنمایی‌های رسمی «More Hints»](https://cs50.harvard.edu/x/2026/practice/license/#debugging): پرسش‌های رسمی که تقریباً راه اصلاح را نام می‌برند؛ فقط پیوند.

## ویدئو و نمایش

- [نمایش ترمینال (asciinema)](https://asciinema.org/a/ITMqFWOktPyhwPuK8l6z2poZm)

## پیوند رسمی

- [License](https://cs50.harvard.edu/x/2026/practice/license/)
- [سیاست صداقت علمی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
