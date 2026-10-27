---
id: w00-n08
type: note
title: شبه‌کد و بلوک‌های سازندهٔ برنامه‌نویسی (Pseudocode)
title_fa: شبه‌کد و بلوک‌های سازندهٔ برنامه‌نویسی
title_en: Pseudocode
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Pseudocode
official_anchor: pseudocode
source_url: https://cs50.harvard.edu/x/notes/0/#pseudocode
source_refs:
- src-notes-0#pseudocode
- src-transcript-0
concept_ids:
- w00-c-pseudocode
- w00-c-function
- w00-c-conditional
- w00-c-boolean-expression
- w00-c-loop
- w00-c-corner-case
- w00-c-abstraction
prev: w00-n07
next: w00-n09
order: 8
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# شبه‌کد و بلوک‌های سازندهٔ برنامه‌نویسی

> **منبع رسمی:** بخش «Pseudocode» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#pseudocode). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

قبل از نوشتن کد، باید منطق را روشن کنی. **شبه‌کد** (pseudocode) همین کار را می‌کند. درس‌نامه آن را برای موفقیت در این دوره و در برنامه‌نویسی «محوری» می‌داند. شبه‌کدِ دفترچهٔ تلفن چهار بلوک سازندهٔ اصلی برنامه‌نویسی را هم معرفی می‌کند: تابع، شرط، عبارت بولی و حلقه.

## شبه‌کد طبق درس‌نامه

- شبه‌کد دستورهایی خوانا برای انسان است که معمولاً گام‌های یک الگوریتم را توصیف می‌کند.
- توانایی نوشتن شبه‌کد برای موفقیت در این کلاس و در برنامه‌نویسی محوری است.
- مثلاً برای الگوریتم سوم (نصف کردن دفترچه) می‌توان این شبه‌کد را نوشت. متن عیناً مطابق درس‌نامه است:

```text
1  Pick up phone book
2  Open to middle of phone book
3  Look at page
4  If person is on page
5      Call person
6  Else if person is earlier in book
7      Open to middle of left half of book
8      Go back to line 3
9  Else if person is later in book
10     Open to middle of right half of book
11     Go back to line 3
12 Else
13     Quit
```

**ترجمهٔ فارسی خط‌به‌خط (برای فهم، نه جایگزین متن بالا):** ۱) دفترچه را بردار. ۲) وسط آن را باز کن. ۳) به صفحه نگاه کن. ۴) اگر شخص در صفحه است، ۵) به او زنگ بزن. ۶) وگرنه اگر شخص در بخش‌های قبلی دفترچه است، ۷) وسط نیمهٔ چپ را باز کن، ۸) به خط ۳ برگرد. ۹) وگرنه اگر شخص در بخش‌های بعدی است، ۱۰) وسط نیمهٔ راست را باز کن، ۱۱) به خط ۳ برگرد. ۱۲) وگرنه ۱۳) خارج شو.

## چرا شبه‌کد مهم است (دو دلیل درس‌نامه)

1. وقتی قبل از نوشتن کدِ رسمی شبه‌کد می‌نویسی، منطق مسئله را از پیش مرور می‌کنی.
2. بعداً می‌توانی آن را به دیگرانی بدهی که می‌خواهند تصمیم‌های کدنویسی تو و طرز کار کدت را بفهمند.

## چهار بلوک سازنده در این شبه‌کد

| مفهوم | نمونه در شبه‌کد | توضیح درس‌نامه |
| --- | --- | --- |
| **تابع** (function) | Pick up، Open to، Look at، Call | خط‌هایی که با فعل شروع می‌شوند |
| **شرط** (conditional) | If، Else if، Else | انتخاب مسیر |
| **عبارت بولی** (boolean expression) | person is earlier in book | عبارتی که درست (true) یا نادرست (false) است |
| **حلقه** (loop) | Go back to line 3 | تکرار |

این بلوک‌ها اصول بنیادین برنامه‌نویسی‌اند. در Scratch هم از همهٔ آن‌ها استفاده می‌کنیم.

## نکته‌های تکمیلی از سخنرانی

- شبه‌کد شکل رسمی واحدی ندارد؛ هر کس می‌تواند شیوهٔ خودش را داشته باشد. فقط باید **کوتاه و دقیق** باشد.
- چرا «برگرد به خط ۳» حلقهٔ بی‌پایان نمی‌سازد؟ چون هر بار مسئله نصف می‌شود و سرانجام به یک صفحه می‌رسد.
- **حالت مرزی (corner case):** اگر شخص اصلاً در دفترچه نباشد چه؟ خط‌های `Else` / `Quit` برای همین است. سخنرانی می‌گوید وقتی برنامه‌ای هنگ می‌کند یا گوشی خودبه‌خود ری‌استارت می‌شود، اغلب برنامه‌نویس چنین حالتی را پیش‌بینی نکرده و رفتار برنامه «تعریف‌نشده» مانده است.
- واژهٔ «بولی» (Boolean) از نام ریاضی‌دانی به نام **بول** (Boole) آمده است. عبارت بولی پرسشی است با پاسخ بله/خیر، درست/نادرست یا ۱/۰.

## مثال تألیفی: شبه‌کد صبحانه

```text
1  Open fridge
2  If there is milk
3      Pour milk
4  Else
5      Pour water
6  Close fridge
```

در این مثال، `Open`، `Pour` و `Close` تابع‌اند، `If` / `Else` شرط است و «there is milk» عبارت بولی است. حلقه ندارد.

## اشتباه‌های رایج

- نوشتن شبه‌کد خیلی مبهم («دنبالش بگرد»). شبه‌کد باید آن‌قدر دقیق باشد که کس دیگری هم بتواند اجرایش کند.
- فراموش کردن حالت مرزی (`Else` / `Quit`).
- یکی گرفتن «شرط» با «عبارت بولی». عبارت بولی **پرسش** است؛ شرط **تصمیم** بر اساس آن پرسش.

## محدودیت‌ها

شبه‌کد اجرا نمی‌شود و کامپیوتر آن را نمی‌فهمد. باید به یک زبان برنامه‌نویسی (Scratch، C و…) ترجمه شود.

## جمع‌بندی

- شبه‌کد = گام‌های الگوریتم به زبان انسانی و دقیق.
- چهار بلوک سازنده: تابع، شرط، عبارت بولی، حلقه.
- همیشه حالت مرزی را در نظر بگیر.

## سؤال‌های خودآزمایی

1. در شبه‌کد دفترچه، کدام خط‌ها حلقه می‌سازند؟
2. «person is on page» تابع است، شرط است یا عبارت بولی؟
3. خط‌های ۱۲ و ۱۳ چه حالتی را پوشش می‌دهند؟
4. دو دلیل درس‌نامه برای نوشتن شبه‌کد چیست؟

**پاسخ کوتاه:** ۱) خط‌های ۸ و ۱۱ (برگشت به خط ۳). ۲) عبارت بولی. ۳) حالتی که شخص در دفترچه نیست. ۴) مرور منطق پیش از کدنویسی، و توضیح تصمیم‌ها به دیگران.

## پیوندها

- قبلی: [الگوریتم و زمان اجرا](/kb/d/w00-n07)
- بعدی: [در ادامهٔ دوره: از Scratch تا C و انتزاع](/kb/d/w00-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
