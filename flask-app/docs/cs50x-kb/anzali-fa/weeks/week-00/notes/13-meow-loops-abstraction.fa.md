---
id: w00-n13
type: note
title: 'میو: حلقه، بلوک سفارشی و انتزاع (Meow, Loops, and Abstraction)'
title_fa: 'میو: حلقه، بلوک سفارشی و انتزاع'
title_en: Meow, Loops, and Abstraction
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Meow, Loops, and Abstraction
official_anchor: meow-loops-and-abstraction
source_url: https://cs50.harvard.edu/x/notes/0/#meow-loops-and-abstraction
source_refs:
- src-notes-0#meow-loops-and-abstraction
- src-transcript-0
- src-src0-zip
- src-pset-0-scratch#starting-from-scratch
concept_ids:
- w00-c-custom-block
- w00-c-parameter-input
- w00-c-loop
- w00-c-correctness-vs-design
prev: w00-n12
next: w00-n14
order: 13
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# میو: حلقه، بلوک سفارشی و انتزاع

> **منبع رسمی:** بخش «Meow, Loops, and Abstraction» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#meow-loops-and-abstraction). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

کدی که «درست» کار می‌کند همیشه «خوب طراحی‌شده» نیست. این بخش با یک گربهٔ میو‌میوکن نشان می‌دهد چطور تکرار را با **حلقه** (loop) کم کنیم و با **بلوک سفارشی** (custom block) جزئیات را پنهان کنیم. این همان **انتزاع** (abstraction) است، که پرابلم‌ست ۰ صریحاً می‌خواهد.

## انتزاع طبق درس‌نامه

- انتزاع، در کنار شبه‌کدنویسی، یک مهارت و مفهوم اساسی در برنامه‌نویسی است.
- انتزاع یعنی ساده کردن یک مسئله به مسئله‌های کوچک‌تر و کوچک‌تر.
- مثال درس‌نامه: اگر میزبان مهمانی شام بزرگی برای دوستانت باشی، «پختن کل غذا» می‌تواند خیلی سنگین باشد. اما اگر آن را به کارهای کوچک‌تر بشکنی، کار بزرگ آسان‌تر به نظر می‌رسد.

## گام ۱: تکرار دستی (عیناً مطابق درس‌نامه)

```text
when green flag clicked
play sound (Meow v) until done
wait (1) seconds
play sound (Meow v) until done
wait (1) seconds
play sound (Meow v) until done
```

درس‌نامه می‌گوید اینجا یک کار را بارها تکرار می‌کنی. اگر ببینی مدام همان دستورها را می‌نویسی، احتمالاً می‌توانی هنرمندانه‌تر برنامه بنویسی و این تکرار را پنهان کنی.

## گام ۲: حلقه با repeat (عیناً مطابق درس‌نامه)

```text
when green flag clicked
repeat (3)
play sound (Meow v) until done
wait (1) seconds
```

این حلقه دقیقاً همان کار برنامهٔ قبلی را می‌کند، اما مسئله ساده‌تر شده، چون تکرار به بلوکی سپرده شده که کد را برای ما **تکرار** می‌کند. (در Scratch، دو بلوک آخر **داخل** دهانهٔ `repeat` قرار می‌گیرند.)

## گام ۳: بلوک سفارشی meow (عیناً مطابق درس‌نامه)

```text
define meow
play sound (Meow v) until done
wait (1) seconds

when green flag clicked
repeat (3)
meow
```

با بلوک `define`، بلوک (تابع) خودمان به نام `meow` را تعریف کرده‌ایم. این تابع صدای میو را پخش می‌کند و یک ثانیه صبر می‌کند. وقتی پرچم سبز کلیک شود، `meow` سه بار تکرار می‌شود.

## گام ۴: بلوک سفارشی با ورودی (عیناً مطابق درس‌نامه)

```text
define meow n times
repeat (n)
 play sound [meow v] until done
 wait (1) seconds
```

`n` از عبارت «meow n times» گرفته می‌شود و از طریق بلوک `define` به تابع meow داده می‌شود.

**از سخنرانی:** بلوک با **Make a Block** (در دستهٔ صورتی My Blocks) ساخته می‌شود. ورودی با گزینهٔ «Add an input» اضافه می‌شود. «label» (مثل `times`) اثر عملکردی ندارد و فقط خوانایی را بیشتر می‌کند. سرانجام زیر پرچم سبز فقط یک بلوک `meow (3) times` می‌ماند و حلقهٔ بیرونی هم لازم نیست.

## جمع‌بندی درس‌نامه دربارهٔ طراحی

درس‌نامه می‌گوید این فرایند پالایش (refinement) به کدی با طراحی بهتر و بهتر رسید. ما الگوریتم خودمان را برای حل یک مسئله ساختیم. هر دوی این مهارت‌ها را در سراسر دوره تمرین خواهی کرد.

## چرا تکرار بد است؟ (از سخنرانی)

در سخنرانی، مدت `wait` از ۱ به ۲ ثانیه تغییر کرد و لازم شد **در دو جا** عوض شود. با ۶۰، ۶۰۰ یا ۶۰۰۰ بلوک، دیر یا زود جایی را فراموش می‌کنی. حلقه و بلوک سفارشی تغییر را **در یک جا** متمرکز می‌کنند. کپی‌پیست کردن کد معمولاً نشانهٔ طراحی ضعیف است.

> **ناهمخوانی ثبت‌شده:** فایل `meow1.sb3` در کد منبع رسمی به‌جای سه بار میو، سه بار `say [cough] for (1) seconds` دارد. درس‌نامه نسخهٔ میو را نشان می‌دهد و ما از درس‌نامه پیروی کرده‌ایم (sources.json، d02 و d03).

## خروجی مورد انتظار

در هر چهار نسخه، گربه سه بار میو می‌کند و بین آن‌ها یک ثانیه مکث می‌کند. نسخهٔ آخر با `meow (5) times` پنج بار میو می‌کند.

## مثال تألیفی

```text
define jump (h)
change y by (h)
wait (0.2) seconds
change y by ((0) - (h))

when [space v] key pressed
jump (40)
```

این بلوک سفارشی یک ورودی (`h`، ارتفاع پرش) دارد و اسپرایت را بالا و دوباره پایین می‌برد. این دقیقاً از همان نوع بلوکی است که پرابلم‌ست می‌خواهد (بلوک سفارشی **با حداقل یک ورودی**)، اما خودت باید بلوکی متناسب با ایدهٔ پروژه‌ات بسازی.

## اشتباه‌های رایج

- گذاشتن بلوک‌ها **زیر** `repeat` به‌جای **داخل** آن. فقط یک بار اجرا می‌شوند.
- ساختن بلوک سفارشی و استفاده نکردن از ورودی آن داخل تعریف (مثلاً `repeat (3)` به‌جای `repeat (n)`).
- فراموش کردن `wait`. میوها پشت سر هم پخش می‌شوند، یا پیام‌های `say` سریع جای هم را می‌گیرند.

## محدودیت‌ها

بلوک‌های سفارشی در Scratch فقط داخل همان اسپرایت در دسترس‌اند. این نکته از رفتار Scratch است و درس‌نامه آن را ذکر نمی‌کند. برای پروژه‌ات بررسی کن کدام اسپرایت به بلوک نیاز دارد.

## جمع‌بندی

- تکرار ← `repeat`.
- دنبالهٔ بلوک با نام معنادار ← بلوک سفارشی (`define`).
- بلوک سفارشی با ورودی ← انعطاف بیشتر (`meow n times`).

## سؤال‌های خودآزمایی

1. چرا نسخهٔ ۱ «درست» اما «بد طراحی‌شده» است؟
2. در `define meow n times`، `n` چه نقشی دارد؟
3. طبق درس‌نامه، انتزاع را تعریف کن.
4. «label» در بلوک سفارشی چه اثری دارد؟

**پاسخ کوتاه:** ۱) کار را درست انجام می‌دهد، اما تکرار دارد و تغییرش باید در چند جا انجام شود. ۲) ورودیِ تعداد تکرار. ۳) ساده کردن مسئله به مسئله‌های کوچک‌تر و کوچک‌تر. ۴) اثر عملکردی ندارد؛ فقط خوانایی را بیشتر می‌کند.

## پیوندها

- قبلی: [سلام به تو: ورودی، متغیر و مقدار بازگشتی](/kb/d/w00-n12)
- بعدی: [شرط‌ها و حلقهٔ همیشگی](/kb/d/w00-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
