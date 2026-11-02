---
id: w00-n16
type: note
title: 'Ivy’s Hardest Game: حرکت، دیوار و دشمن (Ivy’s Hardest Game)'
title_fa: 'Ivy’s Hardest Game: حرکت، دیوار و دشمن'
title_en: Ivy’s Hardest Game
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Ivy’s Hardest Game
official_anchor: ivys-hardest-game
source_url: https://cs50.harvard.edu/x/notes/0/#ivys-hardest-game
source_refs:
- src-notes-0#ivys-hardest-game
- src-transcript-0
- src-scratch-ivy-1
- src-scratch-ivy-2
- src-scratch-ivy-3
- src-scratch-ivy-full-notes
- src-scratch-ivy-full-pset
concept_ids:
- w00-c-movement-collision
- w00-c-boolean-operators
- w00-c-custom-block
- w00-c-sprite
prev: w00-n15
next: w00-summary
order: 16
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# Ivy’s Hardest Game: حرکت، دیوار و دشمن

> **منبع رسمی:** بخش «Ivy’s Hardest Game» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#ivys-hardest-game). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

این بازی نشان می‌دهد چطور با **صفحه‌کلید** حرکت بسازیم، جلوی خروج از صحنه را بگیریم و **دشمن**‌هایی بسازیم که خودکار حرکت می‌کنند یا ما را دنبال می‌کنند. همه با همان بلوک‌های پایه، به‌علاوهٔ **بلوک‌های سفارشی** برای خوانایی.

## سه جزء اصلی (طبق درس‌نامه)

درس‌نامه می‌گوید حالا می‌توانیم حرکت را در برنامه پیاده کنیم و برنامهٔ ما سه جزء اصلی دارد.

**جزء ۱: حلقهٔ اصلی** (عیناً مطابق درس‌نامه)

```text
when green flag clicked
go to x: (0) y: (0)
forever
listen for keyboard
feel for walls
```

با کلیک روی پرچم سبز، اسپرایت به مرکز صحنه `(0,0)` می‌رود و سپس برای همیشه به صفحه‌کلید گوش می‌دهد و دیوارها را بررسی می‌کند.

**جزء ۲: گوش دادن به صفحه‌کلید** (عیناً مطابق درس‌نامه)

```text
define listen for keyboard
if <key (up arrow v) pressed?> then
change y by (1)
end
if <key (down arrow v) pressed?> then
change y by (-1)
end
if <key (right arrow v) pressed?> then
change x by (1)
end
if <key (left arrow v) pressed?> then
change x by (-1)
end
```

برای هر کلید جهت‌نما، اسپرایت در صفحه جابه‌جا می‌شود.

**جزء ۳: حس کردن دیوارها** (عیناً مطابق درس‌نامه)

```text
define feel for walls
if <touching (left wall v) ?> then
change x by (1)
end
if <touching (right wall v) ?> then
change x by (-1)
end
```

وقتی اسپرایت به دیوار می‌خورد، به جای امنی برگردانده می‌شود تا از صحنه بیرون نرود. [بلوک‌ها](https://scratch.mit.edu/projects/577647301)

**از سخنرانی:** چرا با دیوار راست، x را **کم** می‌کنیم؟ چون اسپرایت کمی روی دیوار رفته است. یک پیکسل عقب‌گرد مثل «برخورد و برگشت» عمل می‌کند. `left wall` و `right wall` نام اسپرایت‌های دیوار در این پروژه‌اند، نه بلوک‌های پیش‌فرض Scratch.

## دشمن رفت‌وبرگشتی: Yale (عیناً مطابق درس‌نامه)

```text
when green flag clicked
go to x: (0) y: (0)
point in direction (90)
forever
if <<touching (left wall v)?> or <touching (right wall v)?>> then
turn right (180) degrees
end
move (1) steps
end
```

اسپرایت Yale با رفت‌وبرگشت سر راه اسپرایت Harvard قرار می‌گیرد. وقتی به دیوار می‌خورد، می‌چرخد تا دوباره به دیوار دیگر بخورد. [بلوک‌ها](https://scratch.mit.edu/projects/577647503)

اینجا عملگر بولی **`or`** (یا) دو عبارت بولی را ترکیب می‌کند: اگر **یکی** از آن دو درست باشد، کل عبارت درست است.

**از سخنرانی:** برای سخت‌تر کردن بازی، `move (1) steps` را به `move (10) steps` تغییر بده.

## دشمن تعقیب‌کننده: MIT (عیناً مطابق درس‌نامه)

```text
when green flag clicked
go to (random position v)
forever
point towards (Harvard v)
move (1) steps
```

لوگوی MIT حالا لوگوی Harvard را دنبال می‌کند. [بلوک‌ها](https://scratch.mit.edu/projects/577647729)

**از سخنرانی:** با `move (10) steps`، MIT «لرزان» به نظر می‌رسد، چون از هدف جلو می‌زند و برمی‌گردد. این یک **اشکال بصری** است: کد دقیقاً همان کاری را می‌کند که گفته‌ایم، اما نتیجه مطلوب نیست. راه‌حل، گام‌های کوچک‌تر (۲، ۳ یا ۵) است.

Scratch اجازه می‌دهد اسپرایت‌های زیادی هم‌زمان روی صحنه باشند. بازی کامل: [Ivy’s Hardest Game](https://scratch.mit.edu/projects/565742837).

> **ناهمخوانی ثبت‌شده:** درس‌نامه برای بازی کامل پروژهٔ `565742837` را پیوند داده و صفحهٔ پرابلم‌ست پروژهٔ `326129433` را. هر دو را ثبت کرده‌ایم و یکی را بر دیگری ترجیح نداده‌ایم (sources.json، d01).

## مثال تألیفی: دیوار بالا و پایین

درس‌نامه فقط دیوار چپ و راست را دارد. اگر پروژه‌ات دیوار بالا و پایین هم دارد، الگو مشابه است:

```text
define feel for top and bottom
if <touching (top wall v) ?> then
change y by (-1)
end
if <touching (bottom wall v) ?> then
change y by (1)
end
```

## اشتباه‌های رایج

- علامت اشتباه در جبران دیوار (`change x by (1)` برای دیوار راست). اسپرایت داخل دیوار گیر می‌کند.
- استفاده از `and` به‌جای `or` برای دو دیوار. اسپرایت نمی‌تواند هم‌زمان با هر دو دیوار تماس داشته باشد، پس هرگز نمی‌چرخد.
- گام‌های خیلی بزرگ برای تعقیب‌کننده، که لرزش ایجاد می‌کند.
- فراموش کردن `point in direction (90)` در شروع. جهت اولیه از اجرای قبلی باقی می‌ماند.

## محدودیت‌ها

فایل‌های `.sb3` بازی Ivy’s Hardest Game در این بسته بازرسی نشده‌اند. مراحل بعدی بازی کامل (چند Yale، Princeton و…) فقط در سخنرانی دیده شده و کدشان در درس‌نامه نیست.

## جمع‌بندی

- بلوک‌های سفارشی (`listen for keyboard`، `feel for walls`) حلقهٔ اصلی را خوانا می‌کنند.
- `or` دو شرط را ترکیب می‌کند.
- چند اسپرایت با رفتارهای مستقل = بازی.

## سؤال‌های خودآزمایی

1. چرا با تماس با دیوار راست، `change x by (-1)` می‌زنیم؟
2. اگر `or` را با `and` عوض کنیم، Yale چه رفتاری خواهد داشت؟
3. چرا MIT با `move (10) steps` می‌لرزد؟

**پاسخ کوتاه:** ۱) تا اسپرایت یک پیکسل از دیوار عقب برود و بیرون نرود. ۲) هرگز نمی‌چرخد، چون هم‌زمان با هر دو دیوار تماس ندارد. ۳) از هدف جلو می‌زند و دوباره برمی‌گردد.

## پیوندها

- قبلی: [Oscartime: چند اسپرایت، چند اسکریپت و امتیاز](/kb/d/w00-n15)
- بعدی: [جمع‌بندی هفته](/kb/d/w00-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
