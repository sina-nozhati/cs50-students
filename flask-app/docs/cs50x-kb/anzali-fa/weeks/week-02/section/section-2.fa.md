---
week: 2
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
generated_at: '2026-10-28T09:00:00+03:30'
review_status: draft-needs-human-review
id: w02-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۲ (Section 2)
title_fa: جلسهٔ حل تمرین هفتهٔ ۲
title_en: Section 2
parent: w02-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly); chapter times from section2.srt (inference for boundaries); print.c verbatim; reverse.c, alphabetical.c and initials.c link-only
source_url: https://cs50.harvard.edu/x/sections/2/
source_refs:
- src-section-2#week-2-arrays
- src-section-2-transcript
- src-section-2-video
- src-section-2-code
- src-anzali-inference-2
concept_ids:
- w02-c-design-efficiency
- w02-c-early-return
- w02-c-array
- w02-c-nul
- w02-c-argc-argv
- w02-c-exit-status
prev: w02-summary
next: w02-sh-functions
order: 21
video:
  youtube_id: ZlJuiMNrzBQ
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: خوش‌آمد و پرسش‌های هفته
    evidence_en: null
  - start: '1:21'
    start_seconds: 81
    title_fa: طراحی خوب چیست
    evidence_en: good design
  - start: '2:30'
    start_seconds: 150
    title_fa: کار تکراری و عدد جادویی
    evidence_en: redundant operations
  - start: '5:19'
    start_seconds: 319
    title_fa: 'بازی: strlen در شرط حلقه'
    evidence_en: second option
  - start: '6:45'
    start_seconds: 405
    title_fa: 'بازی: ثابت به‌جای عدد جادویی'
    evidence_en: months in a year
  - start: '8:02'
    start_seconds: 482
    title_fa: 'بازی: else زائد'
    evidence_en: redundant to ask else
  - start: '9:35'
    start_seconds: 575
    title_fa: 'بازی: خروج زودهنگام'
    evidence_en: exit immediately
  - start: '11:37'
    start_seconds: 697
    title_fa: 'آرایه: جدول امتیاز Pac-Man'
    evidence_en: Pac-Man
  - start: '13:42'
    start_seconds: 822
    title_fa: اعلان و پر کردن آرایه
    evidence_en: 0 indexed
  - start: '14:48'
    start_seconds: 888
    title_fa: چاپ آرایه با حلقه
    evidence_en: 4 loop like so
  - start: '16:46'
    start_seconds: 1006
    title_fa: 'پرسش‌ها: طول ثابت آرایه'
    evidence_en: dynamic
  - start: '18:57'
    start_seconds: 1137
    title_fa: 'رشته: Emma و NUL'
    evidence_en: name Emma
  - start: '21:16'
    start_seconds: 1276
    title_fa: تمرین print.c
    evidence_en: character by character
  - start: '26:59'
    start_seconds: 1619
    title_fa: بهبود طراحی print.c
    evidence_en: design improvements
  - start: '28:31'
    start_seconds: 1711
    title_fa: تمرین reverse.c
    evidence_en: reverse.c that takes
  - start: '32:18'
    start_seconds: 1938
    title_fa: ASCII و تمرین alphabetical.c
    evidence_en: program called Alphabetical
  - start: '38:01'
    start_seconds: 2281
    title_fa: باگ مقایسه با NUL
    evidence_en: null character at the end
  - start: '38:38'
    start_seconds: 2318
    title_fa: آرگومان‌های خط فرمان
    evidence_en: talking about command line arguments
  - start: '40:24'
    start_seconds: 2424
    title_fa: argc و argv
    evidence_en: count of the arguments
  - start: '44:04'
    start_seconds: 2644
    title_fa: تمرین initials.c
    evidence_en: Write a program initials.c
  - start: '49:42'
    start_seconds: 2982
    title_fa: پیام راهنما و return 1
    evidence_en: correct usage
  chapters_origin: inference
---

# جلسهٔ حل تمرین هفتهٔ ۲ (Section)

> **منبع رسمی:** [صفحهٔ Section 2 CS50x](https://cs50.harvard.edu/x/sections/2/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/2/lang/en/section2.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، از مدرسان CS50 در هاروارد، اداره می‌کند. او با چند پرسش شروع می‌کند: کامپایل چه مرحله‌هایی دارد؟ کی از آرایه استفاده کنیم؟ رشته چیست؟ آرگومان خط فرمان به چه درد می‌خورد؟ و مهم‌تر از همه، **طراحی خوب** یعنی چه؟ چون طراحی یکی از محورهای ارزیابی کد است.

بخش طراحی با یک بازی پیش می‌رود: دو قطعه کد کنار هم، و شرکت‌کننده‌ها می‌گویند کدام بهتر است. چهار درس از این بازی بیرون می‌آید. اول، کار تکراری نکن: اگر `strlen` را در شرط حلقه بنویسی، در هر دور دوباره حساب می‌شود، در حالی که طول رشته عوض نمی‌شود؛ بهتر است یک بار حسابش کنی و در متغیر نگه داری. دوم، از **عدد جادویی** بپرهیز: به‌جای ۱۲ بنویس `const int MONTHS_IN_YEAR = 12`؛ این هفته هم ۲۶ حرف الفبا نامزد خوبی برای ثابت است. سوم، `else` زائد را حذف کن: اگر شاخهٔ `if` با `return` تمام می‌شود، `else` بعدش لازم نیست. چهارم، حالت خطا را اول بررسی کن و زود خارج شو، تا بقیهٔ کد بدون تودرتویی اضافه خوانا بماند. Kelly همچنین یادآوری می‌کند پیش‌نمونهٔ تابع‌های کمکی را بالای `main` بگذاری.

بعد سراغ آرایه می‌رود، با مثال جدول امتیاز Pac-Man. به‌جای پنج متغیر جدا `score1` تا `score5`، یک آرایهٔ `int scores[5]` می‌سازد، خانه‌ها را با اندیس از صفر پر می‌کند و نشان می‌دهد می‌شود هنگام اعلان هم با آکولاد مقدار داد. در پاسخ به پرسش‌ها توضیح می‌دهد همهٔ عنصرهای آرایه باید هم‌نوع باشند و طول آرایه در C پس از اعلان عوض نمی‌شود (برخلاف list در Python؛ ساختار پویا در هفته‌های بعد می‌آید).

در بخش رشته، نام «Emma» را آرایه‌ای از پنج نویسه نشان می‌دهد: چهار حرف و `\0` در پایان. `name[0]` حرف اول را می‌دهد. بعد سه برنامهٔ کوچک را زنده می‌نویسد: `print.c` که رشته را نویسه‌به‌نویسه چاپ می‌کند، `reverse.c` که آن را وارونه چاپ می‌کند و `alphabetical.c` که می‌سنجد حروف یک رشتهٔ کوچک به ترتیب الفبا هستند یا نه. در دو برنامهٔ آخر، دو باگ آموزنده پیش می‌آید: شروع از اندیسی که روی `\0` می‌افتد، و مقایسهٔ آخرین حرف با `\0`. Kelly برای پیدا کردن باگ دوم موقتاً مقدار عددی نویسه‌ها را با `printf` چاپ می‌کند.

در پایان آرگومان‌های خط فرمان را با مثال `make mario` و `./caesar 13` توضیح می‌دهد و برنامهٔ `initials.c` را می‌نویسد که حرف اول هر بخش از نام را چاپ می‌کند. اگر کاربر نامی ندهد، برنامه پیام راهنما چاپ می‌کند و `1` برمی‌گرداند.

## نکته‌های کلیدی

- طراحی خوب یعنی کارآمد، خوانا و قابل نگه‌داری: کار تکراری نکن، عدد جادویی را ثابت کن، `else` زائد نگذار.
- محاسبه‌ای را که در حلقه تغییر نمی‌کند (مثل طول رشته) یک بار انجام بده و در متغیر نگه دار.
- آرایه برای نگه‌داشتن چند مقدار هم‌نوع زیر یک نام است؛ اندیس از ۰ شروع می‌شود.
- رشته آرایه‌ای از نویسه‌هاست که با `\0` تمام می‌شود؛ آخرین حرف در اندیس طول منهای ۱ است.
- چون نویسه‌ها عدد ASCII‌اند، می‌توان آن‌ها را با `<` و `>` مقایسه کرد.
- `argc` تعداد آرگومان‌هاست و نام برنامه را هم می‌شمارد؛ `argv` آرایه‌ای از رشته‌هاست.
- اگر ورودی خط فرمان کافی نیست، پیام راهنما چاپ کن و `return 1`.

> **تألیفی:** اگر می‌خواهی این نکته‌ها را تمرین کنی، بعد از دیدن جلسه، درس‌های کوتاه ۶ تا ۸ این بسته را بگذران.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع هر فصل از زیرنویس رسمی (`section2.srt`) استخراج شده است. عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — خوش‌آمد و پرسش‌های هفته](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=0s)
- [۱:۲۱ — طراحی خوب چیست](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=81s)
- [۲:۳۰ — کار تکراری و عدد جادویی](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=150s)
- [۵:۱۹ — بازی: strlen در شرط حلقه](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=319s)
- [۶:۴۵ — بازی: ثابت به‌جای عدد جادویی](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=405s)
- [۸:۰۲ — بازی: else زائد](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=482s)
- [۹:۳۵ — بازی: خروج زودهنگام](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=575s)
- [۱۱:۳۷ — آرایه: جدول امتیاز Pac-Man](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=697s)
- [۱۳:۴۲ — اعلان و پر کردن آرایه](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=822s)
- [۱۴:۴۸ — چاپ آرایه با حلقه](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=888s)
- [۱۶:۴۶ — پرسش‌ها: طول ثابت آرایه](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=1006s)
- [۱۸:۵۷ — رشته: Emma و NUL](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=1137s)
- [۲۱:۱۶ — تمرین print.c](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=1276s)
- [۲۶:۵۹ — بهبود طراحی print.c](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=1619s)
- [۲۸:۳۱ — تمرین reverse.c](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=1711s)
- [۳۲:۱۸ — ASCII و تمرین alphabetical.c](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=1938s)
- [۳۸:۰۱ — باگ مقایسه با NUL](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=2281s)
- [۳۸:۳۸ — آرگومان‌های خط فرمان](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=2318s)
- [۴۰:۲۴ — argc و argv](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=2424s)
- [۴۴:۰۴ — تمرین initials.c](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=2644s)
- [۴۹:۴۲ — پیام راهنما و return 1](https://www.youtube.com/watch?v=ZlJuiMNrzBQ&t=2982s)

## کد print.c از جلسه

این کد رسمی جلسه، عیناً از `src2` است. به طول رشته که یک بار در `len` ذخیره می‌شود دقت کن:

```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Input: ");

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        printf("%c", text[i]);
    }
    printf("\n");
}
```

> **فقط پیوند:** `reverse.c`، `alphabetical.c` و `initials.c` پاسخ کامل تمرین‌های خود جلسه‌اند و `initials.c` شیوهٔ کار با `argv` را دقیقاً همان‌طور نشان می‌دهد که در No Vowels و Caesar لازم است. طبق سیاست «بدون راه‌حل» این سه فایل در این بسته بازتولید نشده‌اند و فقط از [فهرست کد منبع جلسه](https://cdn.cs50.net/2025/fall/sections/2/src2/) در دسترس‌اند. پیشنهاد: اول خودت بنویس، بعد مقایسه کن.

## منابع جلسه

- [ویدئو در CS50 Video Player](https://video.cs50.io/ZlJuiMNrzBQ) · [YouTube](https://youtu.be/ZlJuiMNrzBQ)
- [صوت](https://cdn.cs50.net/2025/fall/sections/2/section2.mp3) · [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/sections/2/section2.pdf)
- کد منبع: [فهرست](https://cdn.cs50.net/2025/fall/sections/2/src2/) · [PDF](https://cdn.cs50.net/2025/fall/sections/2/src2.pdf) · [zip](https://cdn.cs50.net/2025/fall/sections/2/src2.zip)
- [زیرنویس](https://cdn.cs50.net/2025/fall/sections/2/lang/en/section2.srt) · [متن گفتار](https://cdn.cs50.net/2025/fall/sections/2/lang/en/section2.txt)
- MP4: [360p](https://cdn.cs50.net/2025/fall/sections/2/section2-360p.mp4) · [720p](https://cdn.cs50.net/2025/fall/sections/2/section2-720p.mp4) · [1080p](https://cdn.cs50.net/2025/fall/sections/2/section2-1080p.mp4)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
