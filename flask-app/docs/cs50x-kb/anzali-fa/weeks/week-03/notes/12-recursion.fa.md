---
id: w03-n12
type: note
title: 'بازگشت: حالت پایه و حالت بازگشتی (Recursion: the idea)'
title_fa: 'بازگشت: حالت پایه و حالت بازگشتی'
title_en: 'Recursion: the idea'
week: 3
parent: w03-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Recursion
official_anchor: recursion
source_url: https://cs50.harvard.edu/x/2026/notes/3/#recursion
source_refs:
- src-notes-3#recursion
- src-transcript-3
- src-short-call-stacks
- src-short-recursion
- src-section-3
- src-section-3-transcript
- src-anzali-inference-3
- src-srt-3
concept_ids:
- w03-c-recursion
- w03-c-base-case
- w03-c-recursive-case
prev: w03-n11
next: w03-n13
order: 12
video:
  youtube_id: 6Svu_ae5ebk
  start: '1:29:21'
  start_seconds: 5361
  url: https://www.youtube.com/watch?v=6Svu_ae5ebk&t=5361s
  origin: inference
  basis: first lecture3.srt cue containing the phrase 'Recursion'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# بازگشت: حالت پایه و حالت بازگشتی

> **منبع رسمی:** بخش «Recursion» از [درس‌نامهٔ هفتهٔ ۳ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/3/#recursion). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۹:۲۱ تا حدود ۱:۳۶:۰۵](https://www.youtube.com/watch?v=6Svu_ae5ebk&t=5361s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

انتخابی و حبابی هر دو `O(n²)` بودند. آیا می‌شود بهتر مرتب کرد؟ کلید جواب ایده‌ای است که اول کمی جادویی به نظر می‌رسد: تابعی که **خودش را صدا می‌زند**. اسمش **بازگشت** (`recursion`) است.

## بازگشت چیست

- درس‌نامه می‌پرسد: چطور می‌توانیم کارایی مرتب‌سازی‌مان را بهتر کنیم؟
- **بازگشت** مفهومی در برنامه‌نویسی است که در آن یک تابع **خودش را فراخوانی می‌کند**. این را قبلاً هم دیده‌ایم:

```text
If no doors left
    Return false
If number behind middle door
    Return true
Else if number < middle door
    Search left half
Else if number > middle door
    Search right half
```

- دقت کن که `search` را روی نسخه‌های کوچک‌تر و کوچک‌تری از همین مسئله صدا می‌زنیم.

## دفترچهٔ تلفن هفتهٔ صفر

در شبه‌کد هفتهٔ صفر هم می‌توانی ببینی بازگشت کجا به کار رفته بود:

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

این کد می‌توانست برای برجسته کردن ویژگی بازگشتی‌اش این‌طور ساده شود:

```text
1  Pick up phone book
2  Open to middle of phone book
3  Look at page
4  If person is on page
5      Call person
6  Else if person is earlier in book
7      Search left half of book
9  Else if person is later in book
10     Search right half of book
12 Else
13     Quit
```

- خط‌های «برو به خط ۳» جای خود را به «نیمهٔ چپ کتاب را جست‌وجو کن» داده‌اند: همان الگوریتم، روی کتابی کوچک‌تر.

> [!NOTE]
> **نکته**
> در نسخهٔ رسمی شمارهٔ خط‌ها از ۷ به ۹ و از ۱۰ به ۱۲ می‌پرد. به نظر می‌رسد عمدی باشد: خط‌های ۸ و ۱۱ (همان «برو به خط ۳») حذف شده‌اند و بقیهٔ شماره‌ها ثابت مانده‌اند تا مقایسه با نسخهٔ قبلی آسان باشد (استنتاج ویراستاری).

## حالت پایه و حالت بازگشتی

- **حالت پایه** (`base case`) شرطی است که جلوی ادامهٔ بی‌پایان بازگشت را می‌گیرد و از حلقه‌های بی‌نهایت جلوگیری می‌کند.
- **حالت بازگشتی** (`recursive case`) بخشی از تابع بازگشتی است که خودش را با ورودی تغییریافته صدا می‌زند و به سمت حالت پایه حرکت می‌کند.

> [!WARNING]
> **هشدار**
> بازگشت بدون حالت پایه، یا با حالت بازگشتی‌ای که به حالت پایه نزدیک نمی‌شود، تا ابد ادامه می‌یابد. **از ویدئوی کوتاه Recursion:** Doug Lloyd می‌گوید چنین برنامه‌ای سرانجام به‌خاطر تمام شدن حافظه از کار می‌افتد.

## سخنرانی، جلسهٔ حل تمرین و ویدئوهای کوتاه

- **از سخنرانی:** اگر در گوگل «recursion» را جست‌وجو کنی، گوگل می‌پرسد «منظورت recursion بود؟» و با کلیک روی آن دوباره به همان صفحه می‌رسی. David اعتراف کرد شوخی در کلاس چندان نگرفت.
- **از جلسهٔ حل تمرین:** Kelly فاکتوریل را بازگشتی نوشت: حالت پایه «اگر `n` صفر بود، ۱ برگردان» و حالت بازگشتی «`n` ضرب در فاکتوریل `n - 1`». بعد دنبالهٔ فیبوناچی را با **دو** حالت پایه (۰ و ۱) نوشت. هر دو کد در [صفحهٔ جلسهٔ حل تمرین](/kb/d/w03-sec) آمده‌اند.
- **از ویدئوی کوتاه Call Stacks:** هر فراخوانی تابع یک **قاب** (`frame`) روی **پشتهٔ فراخوانی** (`call stack`) می‌سازد. فقط قاب بالایی فعال است و بقیه منتظر می‌مانند. برای همین بازگشت کار می‌کند.

## اشتباه‌های رایج

- فراموش کردن حالت پایه.
- صدا زدن تابع با همان ورودی (`f(n)` به‌جای `f(n - 1)`) و نزدیک نشدن به حالت پایه.
- حالت پایه‌ای که هرگز رخ نمی‌دهد، مثلاً `n == 0` وقتی `n` منفی شروع شده است.

## جمع‌بندی

- تابع بازگشتی مسئله را با حل نسخهٔ کوچک‌تری از **همان** مسئله حل می‌کند.
- همیشه دو بخش دارد: حالت پایه و حالت بازگشتی.

## پیوندها

- قبلی: [مرتب‌سازی حبابی](/kb/d/w03-n11)
- بعدی: [هرم ماریو: تکرار در برابر بازگشت](/kb/d/w03-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-03/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
