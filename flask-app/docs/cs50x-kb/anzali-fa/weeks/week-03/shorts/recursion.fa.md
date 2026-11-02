---
week: 3
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:24+03:30'
verified_at: '2026-10-28T05:52:30+03:30'
generated_at: '2026-10-28T10:00:00+03:30'
review_status: draft-needs-human-review
id: w03-sh-recursion
type: short-summary
title: 'ویدئوی کوتاه: بازگشت (Recursion)'
title_fa: بازگشت
title_en: Recursion
parent: w03-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/recursion/
source_refs:
- src-short-recursion
- src-anzali-inference-3
concept_ids:
- w03-c-recursion
- w03-c-base-case
- w03-c-recursive-case
- w03-c-iteration-vs-recursion
- w03-c-factorial-fib
prev: w03-sh-call-stacks
next: w03-sh-merge-sort
order: 27
video:
  youtube_id: mz6tAJMVmfM
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: تابع بازگشتی
    evidence_en: null
  - start: '1:14'
    start_seconds: 74
    title_fa: فاکتوریل
    evidence_en: something called the factorial function
  - start: '3:15'
    start_seconds: 195
    title_fa: حالت پایه
    evidence_en: something called a base case
  - start: '5:57'
    start_seconds: 357
    title_fa: حذف آکولادها
    evidence_en: get rid of all of the curly braces
  - start: '7:38'
    start_seconds: 458
    title_fa: نسخهٔ تکراری کنار بازگشتی
    evidence_en: side by side, is the iterative version
  - start: '8:31'
    start_seconds: 511
    title_fa: 'چند حالت پایه: فیبوناچی'
    evidence_en: an example of something with multiple base cases
  - start: '9:27'
    start_seconds: 567
    title_fa: تمرین کولاتز
    evidence_en: something called the Collatz conjecture
  chapters_origin: inference
recorded: '2017'
presenter: Doug Lloyd
---

# ویدئوی کوتاه: بازگشت (Recursion)

> **منبع رسمی:** [صفحهٔ Short «Recursion» در CS50x](https://cs50.harvard.edu/x/shorts/recursion/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

تابع بازگشتی تابعی است که در اجرای خودش، خودش را صدا می‌زند. ویدئو با فاکتوریل شروع می‌کند: ۵ فاکتوریل یعنی ۵ ضرب در ۴ فاکتوریل، و همین‌طور تا ۱.

بعد نسخهٔ تکراری (با حلقه) و بازگشتی کنار هم مقایسه می‌شوند، فیبوناچی به‌عنوان نمونهٔ «چند حالت پایه» می‌آید و در پایان حدس کولاتز به‌عنوان تمرین پیشنهاد می‌شود.

## نکته‌های کلیدی

- هر تابع بازگشتی **حالت پایه** لازم دارد که فرایند بازگشتی را متوقف کند؛ وگرنه برنامه تا ابد ادامه می‌دهد و سرانجام به‌خاطر تمام شدن حافظه از کار می‌افتد.
- در فاکتوریل این ویدئو، حالت پایه «اگر n برابر ۱ بود، ۱ برگردان» است. (در جلسهٔ حل تمرین حالت پایه n برابر ۰ بود؛ هر دو برای ورودی مثبت درست‌اند.)
- ویدئو برای کوتاهی آکولادهای شاخه‌های تک‌خطی را حذف می‌کند؛ C این را می‌پذیرد، اما سبک CS50 (style50) آکولاد را پیشنهاد می‌کند (ناهمخوانی d53).
- فیبوناچی دو حالت پایه دارد. در این ویدئو شمارش از ۱ است: اولین عدد ۰ و دومین ۱. جلسهٔ حل تمرین شمارش را از ۰ شروع کرد (ناهمخوانی d52).
- هر تابع بازگشتی را می‌شود با حلقه هم نوشت و برعکس؛ اما بعضی مسئله‌ها به شکل بازگشتی زیباتر بیان می‌شوند.
- حدس کولاتز به‌عنوان تمرین آمده است: تعداد گام‌ها برای رسیدن از n به ۱. ویدئو پاسخ را نشان می‌دهد؛ ما آن را بازتولید نمی‌کنیم تا خودت امتحان کنی.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`recursion.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — تابع بازگشتی](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=0s)
- [۱:۱۴ — فاکتوریل](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=74s)
- [۳:۱۵ — حالت پایه](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=195s)
- [۵:۵۷ — حذف آکولادها](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=357s)
- [۷:۳۸ — نسخهٔ تکراری کنار بازگشتی](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=458s)
- [۸:۳۱ — چند حالت پایه: فیبوناچی](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=511s)
- [۹:۲۷ — تمرین کولاتز](https://www.youtube.com/watch?v=mz6tAJMVmfM&t=567s)

## مفاهیم مرتبط

- بازگشت: تابعی که خودش را صدا می‌زند — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- حالت پایه — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- حالت بازگشتی — [یادداشت](/kb/d/w03-n12) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)
- تکرار در برابر بازگشت: هرم با حلقه و با بازگشت — [یادداشت](/kb/d/w03-n13) · درس کوتاه `w03-l06` (واحد `w03-l06-u03`)
- فاکتوریل و فیبوناچی به‌صورت بازگشتی — [یادداشت](/kb/d/w03-sec) · درس کوتاه `w03-l06` (واحد `w03-l06-u01`)

## منابع

- [ویدئو در YouTube](https://youtu.be/mz6tAJMVmfM) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/recursion/recursion.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/recursion/lang/en/recursion.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/recursion/lang/en/recursion.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
