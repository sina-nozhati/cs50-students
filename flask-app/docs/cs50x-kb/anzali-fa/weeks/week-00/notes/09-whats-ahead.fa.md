---
id: w00-n09
type: note
title: 'در ادامهٔ دوره: از Scratch تا C و انتزاع (What’s Ahead)'
title_fa: 'در ادامهٔ دوره: از Scratch تا C و انتزاع'
title_en: What’s Ahead
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: What’s Ahead
official_anchor: whats-ahead
source_url: https://cs50.harvard.edu/x/notes/0/#whats-ahead
source_refs:
- src-notes-0#whats-ahead
- src-transcript-0
concept_ids:
- w00-c-abstraction
- w00-c-compiler
prev: w00-n08
next: w00-n10
order: 9
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# در ادامهٔ دوره: از Scratch تا C و انتزاع

> **منبع رسمی:** بخش «What’s Ahead» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#whats-ahead). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

این بخش نقشهٔ راه دوره را نشان می‌دهد: Scratch در این هفته، C در هفته‌های بعد، و سپس Python. ایدهٔ مهم **انتزاع** (abstraction) هم اینجا معرفی می‌شود: هر نسل از برنامه‌نویس‌ها روی کار نسل قبل می‌ایستد.

## بازنویسی درس‌نامه

- این هفته **Scratch** را یاد می‌گیری؛ یک زبان برنامه‌نویسی بصری (visual programming language).
- در هفته‌های بعد زبان **C** را یاد می‌گیری که چیزی شبیه این است:

```c
#include <stdio.h>

int main(void)
{
  printf("hello, world\n");
}
```

- یادگرفتن C تو را برای یادگیری زبان‌های دیگر، مثل **Python**، خیلی آماده‌تر می‌کند.
- برنامه‌نویس‌ها با **انتزاع** روی کار برنامه‌نویس‌های دیگر ساخته‌اند. به‌جای برنامه‌نویسی با صفر و یک، زبان‌هایی ساخته شد تا کار بسیار سختِ برنامه‌نویسی دودویی را **پنهان کنند** (abstract away) و زبان‌هایی ساده‌تر و ساده‌تر بسازند. «ما می‌توانیم روی شانهٔ دیگران بایستیم.»

## نکته‌های تکمیلی از سخنرانی

- در سخنرانی صفحه‌ای پر از صفر و یک نشان داده شد که در واقع برنامهٔ «hello, world» بود. شرکت‌هایی مثل Intel، AMD و Nvidia تعیین می‌کنند کدام الگوی صفر و یک یعنی «جمع کن»، «ذخیره کن» یا «چاپ کن». یعنی **دستورها** هم مثل داده استاندارد شده‌اند.
- در روزهای اول، انسان‌ها مستقیماً با صفر و یک (مثلاً کارت‌های پانچ) کد می‌نوشتند. بعد کسی **کامپایلر** (compiler) را ساخت: برنامه‌ای که یک زبان را به زبان دیگر ترجمه می‌کند. در هفتهٔ بعد بیشتر دربارهٔ کامپایلر یاد می‌گیری.
- سخنرانی می‌گوید (و خودش آن را «دروغ مصلحتی» یا white lie می‌نامد) که برنامه‌ای نوشته‌شده به C می‌تواند Python را به C تبدیل کند، و C به صفر و یک. این سلسله‌مراتب نمونه‌ای از انتزاع است. همین ایده دربارهٔ `chat.py` هم صدق می‌کند: OpenAI جزئیات سطح پایین را پنهان کرده است.

## تعریف‌ها

- **زبان برنامه‌نویسی بصری:** زبانی که در آن به‌جای تایپ متن، بلوک‌ها را کنار هم می‌چینی (Scratch).
- **انتزاع (abstraction):** پنهان کردن جزئیات پیچیده پشت یک مفهوم یا ابزار ساده‌تر.
- **کامپایلر (compiler)**، از سخنرانی: برنامه‌ای که یک زبان را به زبان دیگر ترجمه می‌کند.

## خروجی مورد انتظار

برنامهٔ C بالا، پس از کامپایل و اجرا، متن `hello, world` را چاپ می‌کند و به خط بعد می‌رود (`\n`). اجرای آن موضوع هفتهٔ ۱ است. در این هفته فقط شکلش را ببین.

## اشتباه‌های رایج

- اینکه فکر کنی Scratch «اسباب‌بازی» است و ربطی به برنامه‌نویسی واقعی ندارد. طبق درس‌نامه، Scratch همان بلوک‌های سازندهٔ اساسی را دارد.
- نگرانی از نحو (syntax) C در این هفته. این هفته فقط Scratch لازم است.

## محدودیت‌ها

جزئیات C (`#include`، `main`، `printf`) در هفتهٔ ۱ توضیح داده می‌شود. اینجا فقط نمونه‌ای از ظاهر آن است.

## جمع‌بندی

- مسیر دوره: Scratch ← C ← Python و زبان‌های دیگر.
- انتزاع یعنی ساختن ابزار ساده روی کار پیچیدهٔ دیگران.

## سؤال‌های خودآزمایی

1. چرا زبان‌های برنامه‌نویسی سطح بالا ساخته شدند؟
2. برنامهٔ C نمونه چه چیزی چاپ می‌کند؟
3. در یک جمله، انتزاع را تعریف کن.

**پاسخ کوتاه:** ۱) تا کار بسیار سختِ برنامه‌نویسی با صفر و یک را پنهان کنند. ۲) `hello, world`. ۳) پنهان کردن جزئیات پیچیده پشت مفهومی ساده‌تر تا بتوان روی آن ساخت.

## پیوندها

- قبلی: [شبه‌کد و بلوک‌های سازندهٔ برنامه‌نویسی](/kb/d/w00-n08)
- بعدی: [آشنایی با Scratch: محیط و دستگاه مختصات](/kb/d/w00-n10)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
