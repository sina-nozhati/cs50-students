---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۱ (Section 1)
title_fa: جلسهٔ حل تمرین هفتهٔ ۱
title_en: Section 1
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript; chapter times from section1.srt (inference for boundaries); contacts.c verbatim; hello.c and mario.c link-only
source_url: https://cs50.harvard.edu/x/sections/1/
source_refs:
- src-section-1#week-1-c
- src-section-1-transcript
- src-section-1-video
- src-section-1-code
- src-anzali-inference-1
prev: w01-summary
next: w01-sh-data-types
order: 21
video:
  youtube_id: 8N5ZpIh9gzM
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: خوش‌آمد و برنامهٔ جلسه
    evidence_en: null
  - start: '1:15'
    start_seconds: 75
    title_fa: محیط cs50.dev
    evidence_en: CS50.dev
  - start: '2:29'
    start_seconds: 149
    title_fa: دکمهٔ style50
    evidence_en: Style 50 button
  - start: '3:43'
    start_seconds: 223
    title_fa: design50 و توضیح کد
    evidence_en: Design 50
  - start: '5:10'
    start_seconds: 310
    title_fa: 'از Scratch به C: main'
    evidence_en: transitioning
  - start: '6:14'
    start_seconds: 374
    title_fa: stdio.h و صفحه‌های راهنما
    evidence_en: is a library in C
  - start: '8:51'
    start_seconds: 531
    title_fa: چرا نوع داده مهم است
    evidence_en: data types
  - start: '10:17'
    start_seconds: 617
    title_fa: متغیر balance و انتساب
    evidence_en: balance
  - start: '13:51'
    start_seconds: 831
    title_fa: ضرب، تقسیم و شکل‌های کوتاه
    evidence_en: multiplication
  - start: '15:06'
    start_seconds: 906
    title_fa: تقسیم صحیح
    evidence_en: floor division
  - start: '15:30'
    start_seconds: 930
    title_fa: باقی‌مانده (%)
    evidence_en: modulo
  - start: '16:40'
    start_seconds: 1000
    title_fa: گرفتن ورودی با get_int
    evidence_en: get in
  - start: '18:22'
    start_seconds: 1102
    title_fa: کد قالب %i
    evidence_en: format code
  - start: '20:04'
    start_seconds: 1204
    title_fa: 'نمایش زنده: خطای include و \n'
    evidence_en: make hello
  - start: '24:16'
    start_seconds: 1456
    title_fa: تمرین Contacts
    evidence_en: Contacts
  - start: '30:19'
    start_seconds: 1819
    title_fa: شرط‌ها و عبارت بولی
    evidence_en: conditional
  - start: '33:29'
    start_seconds: 2009
    title_fa: حلقهٔ for
    evidence_en: for loop
  - start: '35:35'
    start_seconds: 2135
    title_fa: while و do while
    evidence_en: while loop
  - start: '37:17'
    start_seconds: 2237
    title_fa: هرم Mario (چپ‌چین)
    evidence_en: pyramid
  - start: '42:29'
    start_seconds: 2549
    title_fa: انتزاع با تابع کمکی
    evidence_en: abstract
  - start: '48:44'
    start_seconds: 2924
    title_fa: رد کردن ورودی نامعتبر با do while
    evidence_en: '-5'
  chapters_origin: inference
---

# جلسهٔ حل تمرین هفتهٔ ۱ (Section)

> **منبع رسمی:** [صفحهٔ Section 1 CS50x](https://cs50.harvard.edu/x/sections/1/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/1/lang/en/section1.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، از مدرسان CS50، اداره می‌کند. او مباحث سخنرانی را مرور می‌کند و چند برنامهٔ کوچک را زنده می‌نویسد.

ابتدا محیط cs50.dev را معرفی می‌کند: ویرایشگر متن، کاوشگر فایل (File Explorer) و پنجرهٔ ترمینال. سپس دو دکمهٔ کمکی را نشان می‌دهد. **style50** نسخهٔ تو و نسخهٔ مرتب‌شده را کنار هم نشان می‌دهد و با «explain changes» علت تغییرها را از اردک هوش مصنوعی می‌پرسد. **design50** از CS50.ai دربارهٔ طراحی کد بازخورد می‌گیرد. قابلیت «explain highlighted code» هم بخشی از کد را که انتخاب کرده‌ای توضیح می‌دهد.

بعد، برنامهٔ «when green flag clicked» در Scratch را با `int main(void)` در C مقایسه می‌کند و توضیح می‌دهد `stdio.h` کتابخانه‌ای است که `printf` را دارد. برای دیدن توابع کتابخانه‌ها به manual.cs50.io ارجاع می‌دهد.

بخش متغیرها با مثال یک «برنامهٔ کیف پول» پیش می‌رود. متغیر `balance` از نوع `int` است و `=` عملگر **انتساب** است، نه برابری. سپس عملگرهای حسابی را مرور می‌کند: `+`، `-`، `*`، `/` و `%` و شکل‌های کوتاه مثل `*=`. تأکید می‌کند تقسیم دو عدد صحیح با `/` بخش اعشاری را دور می‌ریزد و این نکته در Cash به کار می‌آید.

با `get_int` ورودی می‌گیرد و با کد قالب `%i` آن را چاپ می‌کند. در محیط کد، خطای «call to undeclared library function printf» را نشان می‌دهد که با `#include <stdio.h>` رفع می‌شود. نشان می‌دهد بدون `\n` اعلان ترمینال روی همان خط خروجی می‌ماند.

تمرین Contacts نام، سن، شماره و مکان را می‌پرسد و چاپ می‌کند. بعد شرط‌ها با عبارت بولی (Boolean expression) و سه نوع حلقه را مرور می‌کند. `for` وقتی تعداد تکرار معلوم است، `while` وقتی شرط پایان معلوم است و `do while` وقتی کار باید دست‌کم یک بار انجام شود.

در پایان یک هرم **چپ‌چین** (ساده‌تر از خواستهٔ پرابلم‌ست) را گام‌به‌گام می‌سازد. چاپ هر ردیف را در یک تابع کمکی انتزاع می‌کند و با `do while` ورودی نامعتبر مثل `-5` را رد می‌کند.

## نکته‌های کلیدی

- سه محور ارزیابی کد: درستی (check50)، طراحی (design50) و سبک (style50).
- `int main(void)` معادل «when green flag clicked» است.
- اگر تابعی از کتابخانه را بدون `#include` صدا بزنی، کامپایلر خطا می‌دهد و پیام خطا معمولاً راه رفع را می‌گوید.
- `=` انتساب است: مقدار سمت راست در متغیر سمت چپ قرار می‌گیرد.
- `20 / 3` در اعداد صحیح برابر `6` است، و `20 % 6` باقی‌مانده یعنی `2` را می‌دهد.
- کد قالب جای‌نگهدار است و باید با نوع متغیر جور باشد (`%i` برای `int`، `%s` برای `string`).
- `do while` برای «بپرس تا ورودی معتبر شود» مناسب است.
- مسئلهٔ بزرگ را به مسئله‌های کوچک بشکن و هر کدام را در یک تابع انتزاع کن.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع هر فصل از زیرنویس رسمی (`section1.srt`) استخراج شده است. عنوان فصل‌ها تألیفی است. مرور `while` و `do while` در یک فصل ادغام شده، چون در زیرنویس از هم جدا نمی‌شوند.

- [۰:۰۰ — خوش‌آمد و برنامهٔ جلسه](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=0s)
- [۱:۱۵ — محیط cs50.dev](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=75s)
- [۲:۲۹ — دکمهٔ style50](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=149s)
- [۳:۴۳ — design50 و توضیح کد](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=223s)
- [۵:۱۰ — از Scratch به C: main](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=310s)
- [۶:۱۴ — stdio.h و صفحه‌های راهنما](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=374s)
- [۸:۵۱ — چرا نوع داده مهم است](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=531s)
- [۱۰:۱۷ — متغیر balance و انتساب](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=617s)
- [۱۳:۵۱ — ضرب، تقسیم و شکل‌های کوتاه](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=831s)
- [۱۵:۰۶ — تقسیم صحیح](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=906s)
- [۱۵:۳۰ — باقی‌مانده (%)](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=930s)
- [۱۶:۴۰ — گرفتن ورودی با get_int](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=1000s)
- [۱۸:۲۲ — کد قالب %i](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=1102s)
- [۲۰:۰۴ — نمایش زنده: خطای include و \n](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=1204s)
- [۲۴:۱۶ — تمرین Contacts](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=1456s)
- [۳۰:۱۹ — شرط‌ها و عبارت بولی](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=1819s)
- [۳۳:۲۹ — حلقهٔ for](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=2009s)
- [۳۵:۳۵ — while و do while](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=2135s)
- [۳۷:۱۷ — هرم Mario (چپ‌چین)](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=2237s)
- [۴۲:۲۹ — انتزاع با تابع کمکی](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=2549s)
- [۴۸:۴۴ — رد کردن ورودی نامعتبر با do while](https://www.youtube.com/watch?v=8N5ZpIh9gzM&t=2924s)

## کد Contacts از جلسه

این کد رسمی جلسه، عیناً از `src1` است:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Name, age, phone number, location
    string name = get_string("Name: ");
    int age = get_int("Age: ");
    string phone = get_string("Phone number: ");
    string location = get_string("Location: ");

    printf("New Contact: %s, %i, lives in %s, and can be reached at %s\n", name, age, location, phone);

}
```

> **فقط پیوند:** `hello.c` جلسه عملاً همان خواستهٔ پرابلم‌ست Me است و `mario.c` هرم چپ‌چین را کامل می‌سازد که بسیار نزدیک به راه‌حل Mario است. طبق سیاست «بدون راه‌حل» این دو فایل در این بسته بازتولید نشده‌اند و فقط از [فهرست کد منبع جلسه](https://cdn.cs50.net/2025/fall/sections/1/src1/) در دسترس‌اند. پیشنهاد: اول خودت پرابلم‌ست را حل کن.

## منابع جلسه

- [ویدئو در CS50 Video Player](https://video.cs50.io/8N5ZpIh9gzM) · [YouTube](https://youtu.be/8N5ZpIh9gzM)
- [صوت](https://cdn.cs50.net/2025/fall/sections/1/section1.mp3) · [اسلایدها (PDF)](https://cdn.cs50.net/2025/fall/sections/1/section1.pdf)
- کد منبع: [فهرست](https://cdn.cs50.net/2025/fall/sections/1/src1/) · [PDF](https://cdn.cs50.net/2025/fall/sections/1/src1.pdf) · [zip](https://cdn.cs50.net/2025/fall/sections/1/src1.zip)
- [زیرنویس](https://cdn.cs50.net/2025/fall/sections/1/lang/en/section1.srt) · [متن گفتار](https://cdn.cs50.net/2025/fall/sections/1/lang/en/section1.txt)
- MP4: [360p](https://cdn.cs50.net/2025/fall/sections/1/section1-360p.mp4) · [720p](https://cdn.cs50.net/2025/fall/sections/1/section1-720p.mp4) · [1080p](https://cdn.cs50.net/2025/fall/sections/1/section1-1080p.mp4)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
