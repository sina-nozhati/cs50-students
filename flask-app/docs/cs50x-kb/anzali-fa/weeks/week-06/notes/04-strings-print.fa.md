---
id: w06-n04
type: note
title: رشته‌ها، f-string و پارامترهای نام‌دار print (Strings; Positional and Named Parameters)
title_fa: رشته‌ها، f-string و پارامترهای نام‌دار print
title_en: Strings; Positional and Named Parameters
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Strings
official_anchor: strings
source_url: https://cs50.harvard.edu/x/2026/notes/6/#strings
source_refs:
- src-notes-6#strings
- src-notes-6#positional-parameters-and-named-parameters
- src-anzali-authored-6
- src-anzali-inference-6
- src-srt-6
concept_ids:
- w06-c-string-concat
- w06-c-print-multiple
- w06-c-f-string
- w06-c-named-parameters
prev: w06-n03
next: w06-n05
order: 4
video:
  youtube_id: Rl0ludWTLxs
  start: '18:41'
  start_seconds: 1121
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=1121s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'we also have a function called get string'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# رشته‌ها، f-string و پارامترهای نام‌دار print

> **منبع رسمی:** بخش «Strings» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#strings). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۸:۴۱ تا حدود ۳۸:۱۶](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=1121s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

بیشتر خروجی برنامه‌هایت متن است. پایتون سه راه برای ساختن متن از چند تکه دارد و تابع `print` پارامترهایی دارد که رفتارش را عوض می‌کنند. دانستن تفاوت این راه‌ها جلوی فاصله‌های اضافه یا جاافتاده را در خروجی می‌گیرد؛ چیزی که `check50` به آن بسیار حساس است.

## رشته‌ها

- این کد C را به یاد داری:

```c
// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

- در پایتون به این تبدیل می‌شود:

```python
# get_string and print, with concatenation

from cs50 import get_string

answer = get_string("What's your name? ")
print("hello, " + answer)
```

- این کد را با `code hello.py` می‌نویسی و با `python hello.py` اجرا می‌کنی. علامت `+` رشتهٔ `"hello, "` و `answer` را به هم **الحاق** می‌کند (concatenation).
- همین کار را بدون الحاق هم می‌شود کرد:

```python
# get_string and print, without concatenation

from cs50 import get_string

answer = get_string("What's your name? ")
print("hello,", answer)
```

- اینجا `print` خودش میان `hello,` و `answer` یک فاصله می‌گذارد.
- راه سوم:

```python
# get_string and print, with format strings

from cs50 import get_string

answer  = get_string("What's your name? ")
print(f"hello, {answer}")
```

- آکولادها به `print` اجازه می‌دهند مقدار `answer` را درون رشته **جاگذاری** کند (interpolate). حرف `f` پیش از رشته لازم است؛ بدون آن، خودِ متن `{answer}` چاپ می‌شود.

> [!TIP]
> **تألیفی: کدام فاصله از کجا می‌آید؟**
> در `print("hello, " + answer)` فاصله را خودت درون رشته نوشته‌ای. در `print("hello,", answer)` فاصله را `print` میان دو آرگومان می‌گذارد. در `print(f"hello, {answer}")` فاصله بخشی از متن f-string است. اگر در شکل دوم هم درون رشته فاصله بگذاری (`"hello, "`)، دو فاصله چاپ می‌شود.

## پارامترهای موقعیتی و پارامترهای نام‌دار

- تابع‌هایی مثل `fread`، `fwrite` و `printf` در C **آرگومان موقعیتی** می‌گیرند: آرگومان‌ها را با ویرگول جدا می‌کنی و باید به یاد داشته باشی هر آرگومان در کدام جایگاه است.
- در پایتون، **پارامترهای نام‌دار** اجازه می‌دهند آرگومان را بدون توجه به جایگاهش بدهی.
- در مستندات تابع `print` این را می‌بینی:

```text
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

- می‌شود چند شیء به `print` داد. جداکنندهٔ پیش‌فرض (`sep`) یک فاصله است که وقتی بیش از یک شیء بدهی نمایش داده می‌شود. به همین ترتیب، در پایان هر `print` یک سطر تازه (`end`) چاپ می‌شود.

> [!IMPORTANT]
> **sep و end را با نام بده**
> `print("a", "b", sep="-")` خروجی `a-b` می‌دهد و `print("a", end="")` پس از `a` سطر تازه نمی‌گذارد. اگر این‌ها را بدون نام بدهی (`print("a", "-")`)، پایتون آن‌ها را شیء دیگری برای چاپ حساب می‌کند و `a -` چاپ می‌شود (استنتاجی، اجراشده روی جعبهٔ ساخت با پایتون ۳).

## اشتباه‌های رایج

- فراموش کردن `f` پیش از رشته: `print("hello, {answer}")` خودِ آکولادها را چاپ می‌کند.
- الحاق رشته با عدد: `"x: " + 3` خطای `TypeError` می‌دهد؛ از f-string یا ویرگول استفاده کن.
- فاصلهٔ اضافه با ترکیب ویرگول و فاصلهٔ درون رشته.

## جمع‌بندی

- سه راه: الحاق با `+`، چند آرگومان با ویرگول، و f-string.
- `print(*objects, sep=' ', end='\n', ...)`: پیش‌فرض‌ها فاصله و سطر تازه‌اند.
- `sep` و `end` پارامترهای نام‌دارند.

## پیوندها

- قبلی: [تابع، کتابخانه، ماژول و بسته](/kb/d/w06-n03)
- بعدی: [متغیرها و نوع‌ها](/kb/d/w06-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
