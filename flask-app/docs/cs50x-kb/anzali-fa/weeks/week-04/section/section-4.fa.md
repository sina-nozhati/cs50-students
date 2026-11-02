---
week: 4
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:28+03:30'
verified_at: '2026-10-28T17:26:17+03:30'
generated_at: '2026-10-28T18:00:00+03:30'
review_status: draft-needs-human-review
id: w04-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۴ (Section 4)
title_fa: جلسهٔ حل تمرین هفتهٔ ۴
title_en: Section 4
parent: w04-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly, read in full); chapter times from section4.srt (inference for boundaries); concatenate.c and create.c verbatim (not pset solutions); pdf.c link-only (signature check close to Recover, D29)
source_url: https://cs50.harvard.edu/x/sections/4/
source_refs:
- src-section-4#week-4-memory
- src-section-4-transcript
- src-section-4-video
- src-section-4-code
- src-anzali-inference-4
- src-anzali-authored-4
concept_ids:
- w04-c-hexadecimal
- w04-c-0x-prefix
- w04-c-rgb-hex-color
- w04-c-pointer
- w04-c-address-of
- w04-c-dereference
- w04-c-malloc
- w04-c-malloc-null-check
- w04-c-free
- w04-c-bracket-as-pointer
- w04-c-nul-byte-room
- w04-c-valgrind
- w04-c-memory-leak
- w04-c-buffer-overflow-write
- w04-c-file-pointer
- w04-c-fopen-null-check
- w04-c-fread-fwrite
- w04-c-fprintf-fclose
- w04-c-file-signature
prev: w04-summary
next: w04-sh-hexadecimal
order: 17
video:
  youtube_id: Gjf0L3mkVtY
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: خوش‌آمد و نقشهٔ جلسه
    evidence_en: null
  - start: 0:59
    start_seconds: 59
    title_fa: مرور مبنای شانزده
    evidence_en: hexadecimal
  - start: '3:17'
    start_seconds: 197
    title_fa: 'پرسش: چرا مبنای ۳۷ نه؟'
    evidence_en: '37'
  - start: '4:52'
    start_seconds: 292
    title_fa: اشاره‌گرها با نمودار حافظه
    evidence_en: pointers
  - start: '10:09'
    start_seconds: 609
    title_fa: 'تمرین: a، b و اشاره‌گر c'
    evidence_en: practice
  - start: '19:14'
    start_seconds: 1154
    title_fa: پرسش و پاسخ دربارهٔ اشاره‌گرها
    evidence_en: point to two
  - start: '20:17'
    start_seconds: 1217
    title_fa: malloc برای یک عدد و یک آرایه
    evidence_en: malloc
  - start: '22:43'
    start_seconds: 1363
    title_fa: نماد کروشه و حساب اشاره‌گر
    evidence_en: array plus 1
  - start: '24:16'
    start_seconds: 1456
    title_fa: سه خطای رایج حافظه
    evidence_en: common
  - start: '25:29'
    start_seconds: 1529
    title_fa: 'تمرین: تابع concat'
    evidence_en: concatenate
  - start: '39:50'
    start_seconds: 2390
    title_fa: خطای prototype و اجرای نهایی
    evidence_en: prototype
  - start: '40:32'
    start_seconds: 2432
    title_fa: چرا اصلاً اشاره‌گر؟
    evidence_en: why are we even
  - start: '41:04'
    start_seconds: 2464
    title_fa: اشکال‌زدایی create.c
    evidence_en: debug
  - start: '43:42'
    start_seconds: 2622
    title_fa: valgrind و رفع سه خطا
    evidence_en: valgrind
  - start: '48:25'
    start_seconds: 2905
    title_fa: 'ورودی و خروجی فایل: fopen'
    evidence_en: file io
  - start: '52:26'
    start_seconds: 3146
    title_fa: fread و fwrite
    evidence_en: read it
  - start: '58:53'
    start_seconds: 3533
    title_fa: 'تمرین: pdf.c'
    evidence_en: pdf
  - start: '1:07:20'
    start_seconds: 4040
    title_fa: پایان جلسه
    evidence_en: end of cs 50
  chapters_origin: inference
code_files:
- file: concatenate.c
  policy: verbatim
- file: create.c
  policy: verbatim
- file: pdf.c
  policy: link-only
  reason: file-signature check pattern used by Recover (D29)
---

# جلسهٔ حل تمرین هفتهٔ ۴ (Section)

> **منبع رسمی:** [صفحهٔ Section 4 CS50x](https://cs50.harvard.edu/x/sections/4/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/4/lang/en/section4.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، از مدرسان CS50 در هاروارد، اداره می‌کند و چهار موضوع را دنبال می‌کند: مبنای شانزده، اشاره‌گرها، تخصیص پویای حافظه و ورودی و خروجی فایل.

بخش اول مرور **هگزادسیمال** است: رقم‌های 0 تا 9 و A تا F، پیشوند `0x` برای این‌که معلوم باشد عدد در مبنای شانزده است، و این‌که بیشترین مقدار یک رنگ در RGB یعنی ۲۵۵ با `FF` نوشته می‌شود. در پاسخ به پرسشی که «چرا با A تا Z تا مبنای ۳۷ نرویم؟» می‌گوید مسئله کارآمدی نمایش در حافظه است: مبنای شانزده با تعداد بیت‌هایی که معمولاً ذخیره می‌کنیم جور است. (این‌که هر رقم هگزادسیمال دقیقاً ۴ بیت است در درس‌نامه آمده است.)

بخش دوم **اشاره‌گرها** است. Kelly حافظه را مثل ردیفی از خانه‌های نشانی‌دار می‌کشد: متغیر `n` در یک نشانی، و اشاره‌گر `p` که آن نشانی را نگه می‌دارد. با `*p = 9` مقدار `n` عوض می‌شود. بعد یک تمرین قدم‌به‌قدم می‌دهد: `a = 28`، `b = 50`، اشاره‌گر `c` به `a`، سپس `*c = 14`، بعد `c` به `b` و `*c = 25`؛ و می‌پرسد در هر گام مقدار هر متغیر چیست. در پرسش و پاسخ تأکید می‌کند وقتی `c` به `b` اشاره می‌کند دیگر به `a` کاری ندارد، یک اشاره‌گر در هر لحظه فقط یک نشانی نگه می‌دارد (اما آرایه‌ای از اشاره‌گرها ممکن است)، و یکی از دلیل‌های اشاره‌گر همان `swap` سخنرانی است.

بخش سوم **تخصیص پویای حافظه** است: `malloc` برای یک `int` و برای آرایه‌ای از پنج `int`، دسترسی با `*array` و `*(array + 1)` یا همان کروشه، بررسی `NULL` و `return 1`، و `free` در پایان. Kelly سه خطای رایج حافظه را نام می‌برد: آزاد نکردن حافظه، نبستن فایل، و استفاده از حافظه‌ای بیش از آن‌چه گرفته‌ای. سپس تابع `concat` را با شرکت‌کننده‌ها می‌نویسد: طول دو رشته را با `strlen` می‌گیرد، `len1 + len2 + 1` بایت می‌گیرد (یکی برای `\0`)، با دو حلقه کپی می‌کند (حلقهٔ دوم از اندیس `len1 + i`)، `\0` را در `len1 + len2` می‌گذارد و رشته را برمی‌گرداند. `free` در `main` و **بعد** از `printf` می‌آید، چون رشته تا آن‌جا لازم است. بار اول کامپایل به خاطر نبودن prototype شکست می‌خورد.

بخش چهارم اشکال‌زدایی `create.c` با `valgrind` و بعد **فایل‌ها** است. نسخهٔ معیوب `create.c` سه خطا دارد و `valgrind` «invalid write of size 1» در خط ۱۶ و «6 bytes definitely lost» گزارش می‌کند. رفع خطاها: `free(filename)`، `fclose(new_file)` و `+ 1` برای `\0` در `malloc`. بعد Kelly `fopen` را با صفحهٔ راهنما (manual) توضیح می‌دهد: حالت‌های `r`، `w` و `a`، و `NULL` در صورت خطا. `fread` و `fwrite` را با چهار ورودی‌شان (نشانی، اندازهٔ هر قلم، تعداد قلم‌ها، فایل) باز می‌کند و یک حلقهٔ کپی نویسه‌به‌نویسه از `in.txt` به `out.txt` نشان می‌دهد. در پایان برنامهٔ `pdf.c` را می‌نویسد که با خواندن چهار بایت اول فایل تشخیص می‌دهد احتمالاً PDF است یا نه.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section4.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — خوش‌آمد و نقشهٔ جلسه](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=0s)
- [۰:۵۹ — مرور مبنای شانزده](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=59s)
- [۳:۱۷ — پرسش: چرا مبنای ۳۷ نه؟](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=197s)
- [۴:۵۲ — اشاره‌گرها با نمودار حافظه](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=292s)
- [۱۰:۰۹ — تمرین: a، b و اشاره‌گر c](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=609s)
- [۱۹:۱۴ — پرسش و پاسخ دربارهٔ اشاره‌گرها](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=1154s)
- [۲۰:۱۷ — malloc برای یک عدد و یک آرایه](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=1217s)
- [۲۲:۴۳ — نماد کروشه و حساب اشاره‌گر](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=1363s)
- [۲۴:۱۶ — سه خطای رایج حافظه](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=1456s)
- [۲۵:۲۹ — تمرین: تابع concat](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=1529s)
- [۳۹:۵۰ — خطای prototype و اجرای نهایی](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=2390s)
- [۴۰:۳۲ — چرا اصلاً اشاره‌گر؟](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=2432s)
- [۴۱:۰۴ — اشکال‌زدایی create.c](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=2464s)
- [۴۳:۴۲ — valgrind و رفع سه خطا](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=2622s)
- [۴۸:۲۵ — ورودی و خروجی فایل: fopen](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=2905s)
- [۵۲:۲۶ — fread و fwrite](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=3146s)
- [۵۸:۵۳ — تمرین: pdf.c](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=3533s)
- [۱:۰۷:۲۰ — پایان جلسه](https://www.youtube.com/watch?v=Gjf0L3mkVtY&t=4040s)

## کد رسمی جلسه

سه فایل کد منبع جلسه در [src4.zip](https://cdn.cs50.net/2025/fall/sections/4/src4.zip) هست. دو فایل اول به پرابلم‌ست‌ها جواب نمی‌دهند، برای همین متن کاملشان این‌جا آمده است (تصمیم D29).

`concatenate.c`: چسباندن دو رشته در حافظه‌ای که با `malloc` گرفته شده:

```c
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *concat(char *s1, char *s2);

int main(void)
{
    char *s1 = get_string("String 1: ");
    char *s2 = get_string("String 2: ");

    char *s3 = concat(s1, s2);
    printf("%s\n", s3);
    free(s3);
}

char *concat(char *s1, char *s2)
{
    // Get memory for s3
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    char *s3 = malloc(len1 + len2 + 1);

    // Copy over the values from s1 and s2
    for (int i = 0; i < len1; i++)
    {
        s3[i] = s1[i];
    }
    for (int i = 0; i < len2; i++)
    {
        s3[len1 + i] = s2[i];
    }

    s3[len1 + len2] = '\0';
    return s3;
}
```

> **توجه:** در این فایل پس از `malloc` بررسی `NULL` نیامده است، هرچند خود جلسه چند دقیقه پیش‌تر بر آن تأکید کرده بود. در کد خودت همیشه بررسی کن (ناهمخوانی d64).

`create.c`: نسخهٔ **اصلاح‌شده** برنامه‌ای که یک فایل تازه با نامی از خط فرمان می‌سازد (نسخهٔ معیوب فقط در ویدئو نشان داده شده):

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for improper usage, otherwise, get filename length
    if (argc != 2)
    {
        printf("Wrong usage: Try ./create [filename]\n");
        return 1;
    }
    int filename_length = strlen(argv[1]);

    // Create a new block of memory to store filename
    char *filename = malloc(sizeof(char) * (filename_length + 1));

    // Check if malloc failed
    if (filename == NULL)
    {
        printf("Malloc failed.");
        return 1;
    }

    // Copy argv[1] into block of memory for filename
    sprintf(filename, "%s", argv[1]);

    // Open new file under the name stored at filename
    FILE *new_file = fopen(filename, "w");

    // Check if fopen failed
    if (new_file == NULL)
    {
        printf("Could not create file.");
        return 1;
    }

    free(filename);
    fclose(new_file);
}
```

> **توجه:** دو پیام خطای این فایل `\n` ندارند، و اگر `fopen` شکست بخورد برنامه پیش از `free(filename)` برمی‌گردد و همان چند بایت نشت می‌کند. این‌ها خطای جزئی کد جلسه‌اند و در این بسته اصلاح نشده‌اند (ناهمخوانی d64).

`pdf.c`: **فقط پیوند.** این برنامه با خواندن چند بایت اول فایل و مقایسه با یک امضا کار می‌کند؛ همان الگویی که قلب Recover است. برای همین متنش این‌جا بازتولید نشده است: [فهرست src4](https://cdn.cs50.net/2025/fall/sections/4/src4/).

## نکته‌های کلیدی

- دو رقم هگزادسیمال یک بایت است؛ پیشوند `0x` فقط می‌گوید عدد در مبنای شانزده نوشته شده.
- `int *c = &a;` یعنی «`c` اشاره‌گری به `int` است با مقدار نشانی `a`»؛ `c = &b;` بعدها فقط نشانی نگه‌داشته‌شده را عوض می‌کند و `*c = 25` مقدار `b` را.
- `*(array + 1)` و `array[1]` یک چیزند.
- هر `malloc` یک `free` لازم دارد و هر `fopen` یک `fclose`.
- برای رشته‌ای به طول n، `n + 1` بایت بگیر؛ کم گرفتن آن یک بایت همان «invalid write of size 1» در `valgrind` است.
- `fread` و `fwrite` تعداد قلم‌های خوانده یا نوشته‌شده را برمی‌گردانند؛ `0` یعنی چیزی برای خواندن نماند.
- بسیاری از قالب‌های فایل با چند بایت ثابت (امضا) شروع می‌شوند.

## کاربرد در پرابلم‌ست

> **تألیفی:** پیوند جلسه با مسئله‌های این هفته.

- الگوی `fopen`، بررسی `NULL`، `fread` و `fwrite` و `fclose` در [Volume](/kb/d/w04-ps-volume) و [Recover](/kb/d/w04-ps-recover) لازم می‌شود؛ اما کد جلسه بخشی از راه‌حل آن‌ها نیست.
- ایدهٔ «امضای فایل» که `pdf.c` با آن کار می‌کند، پایهٔ تشخیص شروع هر عکس در Recover است. صفحهٔ رسمی Recover امضای JPEG را توضیح می‌دهد.
- اشکال‌زدایی `create.c` با `valgrind` تمرین خوبی پیش از [پلاک‌خوان (License)](/kb/d/w04-pr-license) است.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
