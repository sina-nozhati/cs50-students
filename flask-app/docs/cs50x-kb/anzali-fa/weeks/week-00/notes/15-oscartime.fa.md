---
id: w00-n15
type: note
title: 'Oscartime: چند اسپرایت، چند اسکریپت و امتیاز (Oscartime)'
title_fa: 'Oscartime: چند اسپرایت، چند اسکریپت و امتیاز'
title_en: Oscartime
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Oscartime
official_anchor: oscartime
source_url: https://cs50.harvard.edu/x/notes/0/#oscartime
source_refs:
- src-notes-0#oscartime
- src-transcript-0
- src-studio-lecture
- src-scratch-oscartime
- src-scratch-trash-fall
- src-scratch-trash-drag
- src-scratch-go-to-top
concept_ids:
- w00-c-costume
- w00-c-thread
- w00-c-incremental-development
- w00-c-variable
- w00-c-custom-block
- w00-c-sprite
prev: w00-n14
next: w00-n16
order: 15
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# Oscartime: چند اسپرایت، چند اسکریپت و امتیاز

> **منبع رسمی:** بخش «Oscartime» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#oscartime). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

Oscartime نشان می‌دهد یک بازی کامل چطور از **قطعه‌های کوچک** ساخته می‌شود: چند **اسپرایت** (sprite)، **لباس‌ها** (costumes)، چند **اسکریپت** که هم‌زمان اجرا می‌شوند، **بلوک سفارشی** و **متغیر** امتیاز. این همان چیزی است که در پرابلم‌ست ۰ از تو خواسته می‌شود.

## معرفی (طبق درس‌نامه)

Oscartime یکی از برنامه‌های Scratch خود استاد (David) است. درس‌نامه به شوخی می‌گوید موسیقی بازی شاید هنوز آزارش بدهد، چون هنگام ساختن برنامه ساعت‌ها به آن گوش داده است. چند دقیقه [Oscartime](https://scratch.mit.edu/projects/277537196) را بازی کن.

**از سخنرانی:** هدف بازی این است که پیش از تمام شدن آهنگ، هر چه بیشتر زباله‌ای را که از آسمان می‌افتد به سطل زبالهٔ اسکار بکشی. استاد می‌گوید ساختش حدود ۸ تا ۱۲ ساعت طول کشید و این بازی نتیجهٔ اولین تکلیف خودش در همین کلاس بود.

## گام ۰: پس‌زمینه

درس‌نامه: برای ساختن Oscartime، اول تیر چراغ برق (lamp post) را اضافه می‌کنیم. **از سخنرانی:** نسخهٔ ۰ هیچ کدی نداشت؛ فقط پس‌زمینهٔ صحنه و اسپرایت سطل زباله بود.

![oscartime interface](https://cs50.harvard.edu/x/notes/0/cs50Week0Scratch10.png "oscartime interface")

## گام ۱: لباس اسکار (عیناً مطابق درس‌نامه)

```text
when green flag clicked
switch costume to (oscar1 v)
forever
if <touching (mouse-pointer v)?> then
switch costume to (oscar2 v)
else
switch costume to (oscar1 v)
```

وقتی ماوس را روی اسکار می‌بری، لباسش عوض می‌شود. یعنی درِ سطل باز می‌شود. منبع: [این بلوک‌ها را ببین](https://scratch.mit.edu/studios/50827060/).

**از سخنرانی:** انیمیشن یعنی چند **لباس** (costume) برای یک اسپرایت، مثلاً سطل بسته، درِ باز و اسکارِ بیرون‌آمده، که پشت سر هم عوض می‌شوند.

## گام ۲: زبالهٔ در حال سقوط (عیناً مطابق درس‌نامه)

```text
when green flag clicked
set drag mode [draggable v]
go to x: (pick random (0) to (240)) y: (180)
forever
  change y by (-1)
end
```

مختصات y زباله همیشه از ۱۸۰ (بالای صحنه) شروع می‌شود و x تصادفی است. تا وقتی زباله بالای زمین است، هر بار ۱ پیکسل پایین می‌رود. [بلوک‌ها](https://scratch.mit.edu/projects/726782167)

**از سخنرانی:** Scratch خودش جلوی خارج شدن اسپرایت از صحنه را می‌گیرد، پس زباله پایین صحنه می‌ایستد.

## گام ۳: انداختن زباله در سطل (عیناً مطابق درس‌نامه)

```text
when green flag clicked
forever
  if <touching [Oscar v] ?> then
    go to x: (pick random (0) to (240)) y: (180)
  end
end
```

[بلوک‌ها](https://scratch.mit.edu/projects/726780064)

**از سخنرانی:** زباله واقعاً «داخل سطل» نمی‌رود. همان اسپرایت **دوباره به بالای صحنه منتقل می‌شود**، طوری که انگار زبالهٔ تازه‌ای در حال افتادن است.

## اسکریپت‌های هم‌زمان (threads)، از سخنرانی

اسپرایت زباله در این مرحله **دو اسکریپت** دارد که هر دو با «when green flag clicked» شروع می‌شوند. سخنرانی می‌گوید زباله «دو کار را هم‌زمان، در اصل به‌صورت موازی» انجام می‌دهد: یکی سقوط، دیگری بررسی تماس با اسکار. صفحهٔ هفته این مفهوم را **Threads** (ریسه‌ها) نامیده است.

## گام ۴: بلوک سفارشی go to top (عیناً مطابق درس‌نامه)

درس‌نامه این مرحله را «پیاده‌سازی متغیرهای امتیاز» می‌نامد، اما کدِ نشان‌داده‌شده در درس‌نامه بلوک سفارشی `go to top` است:

```text
when green flag clicked
set drag mode [draggable v]
go to top
forever
  change y by (-1)
end
```

```text
when green flag clicked
forever
  if <touching [Oscar v] ?> then
    go to top
  end
end
```

```text
define go to top
  go to x: (pick random (0) to (240)) y: (180)
```

[بلوک‌ها](https://scratch.mit.edu/projects/726779570)

**از سخنرانی:** در نسخهٔ قبل، همان بلوک «go to x … y: 180» در دو اسکریپت کپی شده بود. با بلوک سفارشی، تغییرِ آینده فقط در یک جا لازم است.

## متغیر امتیاز (score)، فقط از سخنرانی

> **ثبت شکاف:** کدِ متغیر امتیاز در درس‌نامه نیامده است. آنچه در ادامه می‌آید از توضیح شفاهی سخنرانی (نسخهٔ ۴) است، نه از کد رسمی درس‌نامه.

در نسخهٔ ۴، متغیری به نام `score` ساخته شد (از دستهٔ Variables). اول به ۰ تنظیم می‌شود، و هر بار که زباله با اسکار تماس پیدا کند، پیش از رفتن به بالا، `score` یکی زیاد می‌شود. Scratch مقدار متغیر را خودکار روی صحنه نشان می‌دهد. سخنرانی توصیه می‌کند متغیر را با **نام کامل و معنادار** (مثل `score`) نام‌گذاری کنی، نه `x` یا `y`.

## درس اصلی برای پروژهٔ خودت

طبق سخنرانی، یک برنامهٔ پیچیده را به بلوک‌های سازندهٔ پایه بشکن. از مسئله‌های ساده شروع کن و **گام‌به‌گام** (baby steps) پیش برو. صفحهٔ پرابلم‌ست هم همین را می‌گوید.

بازی کامل را امتحان کن: [Oscartime](https://scratch.mit.edu/projects/277537196).

## مثال تألیفی: اسکلت امتیاز

```text
when green flag clicked
set [score v] to (0)

when green flag clicked
forever
  if <touching [Basket v] ?> then
    change [score v] by (1)
    go to top
  end
end
```

این اسکلت فرضی یک اسپرایت «Basket» دارد. برای پروژه‌ات باید نام‌ها و منطق را خودت طراحی کنی.

## اشتباه‌های رایج

- قرار دادن `change [score] by (1)` **بیرون** از بلوک `if`. امتیاز در هر دور حلقه زیاد می‌شود، نه فقط هنگام تماس. سخنرانی می‌گوید افزایش امتیاز هنگام تماس و پیش از رفتن به بالا انجام می‌شود.
- فراموش کردن تنظیم دوبارهٔ امتیاز به ۰ در شروع بازی. امتیاز از بازی قبل باقی می‌ماند.
- ساختن چند اسپرایت زبالهٔ کپی‌شده، در حالی که یک اسپرایت با «رفتن به بالا» کافی است.

## محدودیت‌ها

فایل‌های `Oscartime*.sb3` در این بسته بازرسی نشده‌اند. کد امتیاز فقط از توضیح شفاهی سخنرانی است. برای دیدن جزئیات دقیق، استودیوی رسمی را باز کن و **See inside** را بزن.

## جمع‌بندی

- لباس‌ها انیمیشن می‌سازند.
- چند اسکریپت با پرچم سبز هم‌زمان اجرا می‌شوند (threads).
- بلوک سفارشی تکرار را حذف می‌کند؛ متغیر امتیاز وضعیت بازی را نگه می‌دارد.

## سؤال‌های خودآزمایی

1. چرا زبالهٔ «انداخته‌شده» دوباره از بالا می‌افتد؟
2. اسپرایت زباله در گام ۳ چند اسکریپت دارد و آن‌ها چطور اجرا می‌شوند؟
3. بلوک `go to top` چه مشکلی را حل کرد؟
4. کد متغیر امتیاز از کدام منبع آمده است؟

**پاسخ کوتاه:** ۱) همان اسپرایت به `y = 180` و x تصادفی منتقل می‌شود. ۲) دو اسکریپت؛ هم‌زمان (موازی). ۳) تکرار همان بلوک‌ها در دو اسکریپت. ۴) فقط از توضیح سخنرانی؛ درس‌نامه کدش را نیاورده است.

## پیوندها

- قبلی: [شرط‌ها و حلقهٔ همیشگی](/kb/d/w00-n14)
- بعدی: [Ivy’s Hardest Game: حرکت، دیوار و دشمن](/kb/d/w00-n16)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
