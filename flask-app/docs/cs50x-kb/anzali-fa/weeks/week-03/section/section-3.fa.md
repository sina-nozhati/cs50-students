---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sec
type: section-summary
title: جلسهٔ حل تمرین هفتهٔ ۳ (Section 3)
title_fa: جلسهٔ حل تمرین هفتهٔ ۳
title_en: Section 3
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: Persian summary of the official section video/transcript (Kelly); chapter times from section3.srt (inference for boundaries); struct.c, factorial.c and fib.c verbatim (not pset solutions)
source_url: https://cs50.harvard.edu/x/sections/3/
source_refs:
- src-section-3#week-3-algorithms
- src-section-3-transcript
- src-section-3-video
- src-section-3-code
- src-anzali-inference-3
concept_ids:
- w03-c-struct
- w03-c-dot-notation
- w03-c-array-of-structs
- w03-c-recursion
- w03-c-base-case
- w03-c-factorial-fib
- w03-c-linear-search
- w03-c-big-o
- w03-c-selection-sort
- w03-c-bubble-sort
- w03-c-merge-sort
prev: w03-summary
next: w03-sh-linear-search
order: 21
video:
  youtube_id: r383B4M1EgE
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: خوش‌آمد و نقشهٔ جلسه
    evidence_en: null
  - start: '1:17'
    start_seconds: 77
    title_fa: 'struct: گروه کردن دادهٔ مرتبط'
    evidence_en: how can we group
  - start: '3:54'
    start_seconds: 234
    title_fa: 'تمرین: struct نامزد'
    evidence_en: start out with a little exercise
  - start: '9:19'
    start_seconds: 559
    title_fa: تابع get_candidate
    evidence_en: create your own get candidate
  - start: '20:50'
    start_seconds: 1250
    title_fa: آرایه‌ای از نامزدها
    evidence_en: use our get candidate function to create an array
  - start: '28:42'
    start_seconds: 1722
    title_fa: بازگشت چیست
    evidence_en: move on to recursion
  - start: '30:37'
    start_seconds: 1837
    title_fa: فاکتوریل
    evidence_en: heard of factorials before
  - start: '33:25'
    start_seconds: 2005
    title_fa: حالت پایه و حالت بازگشتی
    evidence_en: what is our base case
  - start: '42:41'
    start_seconds: 2561
    title_fa: فیبوناچی
    evidence_en: the Fibonacci sequence is a sequence
  - start: '49:38'
    start_seconds: 2978
    title_fa: جست‌وجوی خطی
    evidence_en: If you had like this array of
  - start: '50:34'
    start_seconds: 3034
    title_fa: تحلیل زمان اجرا
    evidence_en: runtime analysis
  - start: '54:43'
    start_seconds: 3283
    title_fa: مرتب‌سازی انتخابی
    evidence_en: let's look at selection sort
  - start: '1:00:19'
    start_seconds: 3619
    title_fa: مرتب‌سازی حبابی
    evidence_en: move on now to bubble sort
  - start: '1:05:15'
    start_seconds: 3915
    title_fa: مرتب‌سازی ادغامی
    evidence_en: finally we're going to get to merge sort
  - start: '1:10:36'
    start_seconds: 4236
    title_fa: جدول زمان اجرای سه الگوریتم
    evidence_en: this is a chart
  chapters_origin: inference
---

# جلسهٔ حل تمرین هفتهٔ ۳ (Section)

> **منبع رسمی:** [صفحهٔ Section 3 CS50x](https://cs50.harvard.edu/x/sections/3/) و [متن گفتار جلسه](https://cdn.cs50.net/2025/fall/sections/3/lang/en/section3.txt). این صفحه خلاصهٔ فارسی جلسه است، نه ترجمهٔ کامل. همهٔ مطالب این صفحه **از جلسهٔ حل تمرین** هستند مگر جایی که **تألیفی** برچسب خورده باشد.

## خلاصه

جلسه را Kelly، از مدرسان CS50 در هاروارد، اداره می‌کند و سه سؤال را دنبال می‌کند: چطور داده‌های مرتبط از نوع‌های مختلف را در یک واحد گروه کنیم؟ بازگشت چطور کار می‌کند؟ و چطور کارآمد جست‌وجو و مرتب کنیم و این کارآمدی را بسنجیم؟

بخش اول دربارهٔ **struct** است. Kelly با مثال نامزد انتخابات شروع می‌کند: نوع `candidate` با یک `string` به نام `name` و یک `int` به نام `votes`. بعد یک نمونه به نام `president` می‌سازد و با نماد نقطه فیلدهایش را پر می‌کند. تمرین در سه گام پیش می‌رود: اول یک struct نامزد با مقدارهای ثابت، بعد تابع `get_candidate` که نام و رأی را از کاربر می‌گیرد و یک `candidate` **برمی‌گرداند**، و در پایان آرایه‌ای از سه نامزد که با حلقه پر و با حلقه چاپ می‌شود. در پاسخ به یک پرسش توضیح می‌دهد حلقهٔ تودرتو این‌جا لازم نیست، چون دو حلقهٔ جدا هر کدام سه بار اجرا می‌شوند، نه نه بار.

بخش دوم **بازگشت** است: حل یک مسئله با حل نسخهٔ کوچک‌تر همان مسئله. Kelly فاکتوریل را با دست باز می‌کند (فاکتوریل ۳ یعنی ۳ ضرب در فاکتوریل ۲) و می‌پرسد حالت پایه چیست؛ پاسخ: فاکتوریل ۰ برابر ۱ (و اضافه می‌کند ۱ هم می‌توانست حالت پایه باشد). برنامه را می‌نویسد و با ۰، ۱ و ۵ امتحان می‌کند. در پاسخ به «چرا حلقه نه؟» می‌گوید هر تابع بازگشتی را می‌شود با حلقه هم نوشت. بعد فیبوناچی را می‌نویسد که **دو** حالت پایه دارد، تا تابع هرگز سراغ عدد منفی نرود.

بخش سوم **جست‌وجو و مرتب‌سازی** است. Kelly با جست‌وجوی خطی برای عدد ۶ در آرایه‌ای از کمدهای بسته شروع می‌کند و «تحلیل زمان اجرا» را توضیح می‌دهد: O(n) یعنی برای ورودی n تا حدود n گام لازم است و دو برابر شدن ورودی، زمان را دو برابر می‌کند. بعد با انیمیشن انتخابی، حبابی و ادغامی را مرور می‌کند، شبه‌کد هر کدام را می‌گوید و در پایان جدول O و Ω سه الگوریتم را نشان می‌دهد که برای مسئلهٔ Sort به کار می‌آید.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`section3.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — خوش‌آمد و نقشهٔ جلسه](https://www.youtube.com/watch?v=r383B4M1EgE&t=0s)
- [۱:۱۷ — struct: گروه کردن دادهٔ مرتبط](https://www.youtube.com/watch?v=r383B4M1EgE&t=77s)
- [۳:۵۴ — تمرین: struct نامزد](https://www.youtube.com/watch?v=r383B4M1EgE&t=234s)
- [۹:۱۹ — تابع get_candidate](https://www.youtube.com/watch?v=r383B4M1EgE&t=559s)
- [۲۰:۵۰ — آرایه‌ای از نامزدها](https://www.youtube.com/watch?v=r383B4M1EgE&t=1250s)
- [۲۸:۴۲ — بازگشت چیست](https://www.youtube.com/watch?v=r383B4M1EgE&t=1722s)
- [۳۰:۳۷ — فاکتوریل](https://www.youtube.com/watch?v=r383B4M1EgE&t=1837s)
- [۳۳:۲۵ — حالت پایه و حالت بازگشتی](https://www.youtube.com/watch?v=r383B4M1EgE&t=2005s)
- [۴۲:۴۱ — فیبوناچی](https://www.youtube.com/watch?v=r383B4M1EgE&t=2561s)
- [۴۹:۳۸ — جست‌وجوی خطی](https://www.youtube.com/watch?v=r383B4M1EgE&t=2978s)
- [۵۰:۳۴ — تحلیل زمان اجرا](https://www.youtube.com/watch?v=r383B4M1EgE&t=3034s)
- [۵۴:۴۳ — مرتب‌سازی انتخابی](https://www.youtube.com/watch?v=r383B4M1EgE&t=3283s)
- [۱:۰۰:۱۹ — مرتب‌سازی حبابی](https://www.youtube.com/watch?v=r383B4M1EgE&t=3619s)
- [۱:۰۵:۱۵ — مرتب‌سازی ادغامی](https://www.youtube.com/watch?v=r383B4M1EgE&t=3915s)
- [۱:۱۰:۳۶ — جدول زمان اجرای سه الگوریتم](https://www.youtube.com/watch?v=r383B4M1EgE&t=4236s)

## کد رسمی جلسه

سه فایل کد منبع جلسه در [src3.zip](https://cdn.cs50.net/2025/fall/sections/3/src3.zip) هست. این سه به پرابلم‌ست‌ها جواب نمی‌دهند، برای همین متن کاملشان این‌جا آمده است.

`struct.c`: آرایه‌ای از سه نامزد که با تابع `get_candidate` پر می‌شود:

```c
#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    int votes;

} candidate;

candidate get_candidate(void);

int main(void)
{
    candidate candidates[3];

    for (int i = 0; i < 3; i++)
    {
        candidates[i] = get_candidate();
    }

    for (int i = 0; i < 3; i++)
    {
        printf("Candidate %i is named %s and has %i votes.\n", i + 1, candidates[i].name,
               candidates[i].votes);
    }
}

// Function to get a new candidate
candidate get_candidate(void)
{
    candidate new_candidate;
    new_candidate.name = get_string("Name: ");
    new_candidate.votes = get_int("Votes: ");

    return new_candidate;
}
```

`factorial.c`: فاکتوریل بازگشتی با حالت پایهٔ ۰:

```c
#include <cs50.h>
#include <stdio.h>

int factorial(int n);

int main(void)
{
    int n = get_int("Factorial of: ");
    printf("Factorial of %i is %i\n", n, factorial(n));
}

int factorial(int n)
{
    // Base case
    if (n == 0)
    {
        return 1;
    }

    // Recursive case
    return n * factorial(n - 1);
}
```

`fib.c`: فیبوناچی بازگشتی با دو حالت پایه:

```c
#include <cs50.h>
#include <stdio.h>

int fib(int n);

int main(void)
{
    int n = get_int("Fibonacci number: ");
    printf("The %i Fibonacci number is %i\n", n, fib(n));
}

int fib(int n)
{
    // Base Case
    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }

    // Recursive Case
    return fib(n - 1) + fib(n - 2);
}
```

> **توجه:** در `fib.c` شمارش از صفر است (`fib(0)` برابر ۰ و `fib(1)` برابر ۱)، اما ویدئوی کوتاه Recursion از یک می‌شمارد (عنصر اول ۰، عنصر دوم ۱). هر دو یک دنباله‌اند با اندیس‌گذاری متفاوت (ناهمخوانی d52).

## نکته‌های کلیدی

- struct چند دادهٔ مرتبط با نوع‌های متفاوت را یک نوع تازه می‌کند؛ `typedef` نام آن نوع را تعریف می‌کند.
- تابع می‌تواند یک struct کامل برگرداند، مثل `get_candidate`.
- هر تابع بازگشتی حالت پایه لازم دارد؛ فیبوناچی دو حالت پایه دارد.
- هر کار بازگشتی را با حلقه هم می‌شود انجام داد؛ انتخاب بین این دو به خوانایی و مسئله بستگی دارد.
- انتخابی در بهترین حالت هم n² است، چون راهی برای توقف زودهنگام ندارد؛ حبابی با بررسی «جابه‌جایی رخ داد؟» می‌تواند در بهترین حالت n باشد.
- ادغامی log n بار نصف می‌کند و در هر سطح حدود n کار ادغام دارد، پس n log n؛ حتی اگر فهرست از قبل مرتب باشد.

> **توجه:** Kelly رشد n² را «نمایی» (exponential) می‌نامد. در اصطلاح دقیق، n² رشد **چندجمله‌ای** (درجه دو) است و «نمایی» برای رشدهایی مثل 2ⁿ به کار می‌رود (ناهمخوانی d55).

## کاربرد در پرابلم‌ست

> **تألیفی:** پیوند جلسه با مسئله‌های این هفته.

- struct `candidate` جلسه همان الگویی است که در کد آغازین [Plurality](/kb/d/w03-ps-plurality) و [Runoff](/kb/d/w03-ps-runoff) می‌بینی؛ اما کد جلسه بخشی از راه‌حل آن‌ها نیست.
- جدول O و Ω پایان جلسه ابزار اصلی تحلیل در [Sort](/kb/d/w03-ps-sort) است.
- فاکتوریل و فیبوناچی تمرین خوبی پیش از [atoi بازگشتی](/kb/d/w03-pr-atoi) هستند.

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
