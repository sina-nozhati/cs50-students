---
id: w99-n07
type: note
title: ارسال با submit50، کارنامه و گواهی (submit50, Gradebook and Certificate)
title_fa: ارسال با submit50، کارنامه و گواهی
title_en: submit50, Gradebook and Certificate
week: 99
week_slug: final-project
parent: w99-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Step 3 of 3
official_anchor: step-3-of-3
source_url: https://cs50.harvard.edu/x/2026/project/#step-3-of-3
source_refs:
- src-project-99#step-3-of-3
- src-certificate-99
- src-faqs-99
- src-gradebook-99
- src-anzali-authored-99
concept_ids:
- w99-c-fp-submit50
- w99-c-fp-too-large
- w99-c-fp-gradebook
- w99-c-fp-deadline
prev: w99-n06
next: w99-summary
order: 7
official_blocks:
- submit50
official_quotes:
- too_large
- gradebook
- green_banner
- resubmit
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:09+03:30'
verified_at: '2026-10-31T16:15:00+03:30'
review_status: draft-needs-human-review
content_policy: 'Guidance only: faithful Persian rewrite of the official Final Project specification, with requirement sentences quoted in English verbatim (official99.REQ, checked against the live page). No project idea is prescribed and no project code or solution is given (D88). Authored planning tips are marked تألیفی. Callouts use GitHub-style markers followed by a bold Persian label line.'
---

# ارسال با submit50، کارنامه و گواهی

> **منبع رسمی:** بخش «Step 3 of 3» از [صفحهٔ پروژهٔ نهایی CS50x 2026](https://cs50.harvard.edu/x/2026/project/#step-3-of-3). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. الزام‌های رسمی به انگلیسی و کلمه‌به‌کلمه نقل شده‌اند و مطالب **تألیفی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

پروژه‌ای که ساخته شده ولی درست ارسال نشده، از نظر درس هنوز ارسال نشده است. و درس تا وقتی کارنامه‌ات را باز نکنی و بنر سبز را نبینی، کامل حساب نمی‌شود.

## ارسال با submit50 (پایان گام ۲)

- فرمان `submit50` را از **درون پوشهٔ** `project` اجرا کن (یا از هر پوشه‌ای که `README.md` و کد پروژه در آن است؛ کد هم باید ارسال شود).
- با نام کاربری و گذرواژهٔ GitHub وارد شو. برای امنیت، به‌جای حرف‌های گذرواژه ستاره می‌بینی.

```text
submit50 cs50/problems/2026/x/project
```

## اگر ارسال نشد چون پروژه بزرگ است

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> try to ZIP all of the contents of that directory (except for README.md) and then submit that instead.

- همهٔ محتوای پوشه را **به‌جز** `README.md` در یک ZIP بگذار و آن را ارسال کن.
- اگر باز هم بزرگ بود: برخی فایل‌های پیکربندی را حذف کن، حجم ارسال را به **زیر ۱۰۰ مگابایت** برسان، یا مستقیم با رابط وب GitHub در `github.com/me50/USERNAME` بارگذاری کن و مطمئن شو در شاخهٔ `cs50/problems/2026/x/project` هستی؛ وگرنه سامانه نمی‌تواند آن را بررسی کند.

## گام ۳: کارنامه و گواهی

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> Be sure to visit your gradebook at cs50.me/cs50x a few minutes after you submit.

- فقط با باز کردن کارنامه است که سامانه بررسی می‌کند درس را تمام کرده‌ای یا نه.
- همین کار ساخت **گواهی رایگان CS50** (فوری) و **گواهی Verified از edX** (ظرف ۳۰ روز) را راه می‌اندازد، اگر بقیهٔ تکلیف‌ها را هم کامل کرده باشی.
- گواهی رایگانت را، با پیوند بالای کارنامه، **پیش از مهلت** دریافت کن.

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> The course is not considered complete until you do the above and see the green banner saying you’ve completed the course.

- اگر این کار را پیش از مهلت نکنی، وضعیتت تابع [قواعد انتقال](https://cs50.harvard.edu/x/faqs/#deadlines) در FAQ است و کادر درس پس از آن تاریخ اصلاح دستی انجام نمی‌دهد.

## اگر نتیجه‌ای ندیدی

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> If you don’t see any results in your gradebook, best to resubmit (running the above submit50 command) with only your README.md file this time. No need to resubmit your form.

- پروژه معمولاً ظرف چند دقیقه نمره می‌گیرد. اگر نتیجه‌ای ندیدی، `submit50` را دوباره فقط با `README.md` اجرا کن. لازم نیست فرم را دوباره بفرستی.

> [!NOTE]
> **گواهی و آستانهٔ ۷۰٪**
> صفحهٔ گواهی می‌گوید برای گواهی رایگان باید در هر پرابلم‌ست و در پروژهٔ نهایی دست‌کم ۷۰٪ بگیری (d200). معیار جزئی نمره‌دهی پروژه در صفحه‌های رسمی نیامده است.

> [!TIP]
> **تألیفی: ترتیب کارهای روز تحویل**
> ویدئو (گام ۱) → فرم → README.md با نشانی ویدئو (گام ۲) → `submit50` → چند دقیقه بعد، کارنامه (گام ۳) → دریافت گواهی و دیدن بنر سبز. همهٔ این ترتیب در چالش «چیدن گام‌های تحویل» تمرین می‌شود.

صفحهٔ رسمی با این جمله تمام می‌شود: «This was CS50x!»

## پیوندها

- قبلی: [گام ۲: فایل README.md](/kb/d/w99-n06)
- بعدی: [خلاصه و فهرست وارسی](/kb/d/w99-summary)
- فهرست وارسی: `weeks/final-project/checklist.json` · واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/final-project/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
