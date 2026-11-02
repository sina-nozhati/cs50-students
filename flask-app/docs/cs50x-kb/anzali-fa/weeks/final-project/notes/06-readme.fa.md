---
id: w99-n06
type: note
title: 'گام ۲: فایل README.md (Step 2: README.md)'
title_fa: 'گام ۲: فایل README.md'
title_en: 'Step 2: README.md'
week: 99
week_slug: final-project
parent: w99-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Step 2 of 3
official_anchor: step-2-of-3
source_url: https://cs50.harvard.edu/x/2026/project/#step-2-of-3
source_refs:
- src-project-99#step-2-of-3
- src-faqs-99
- src-anzali-authored-99
concept_ids:
- w99-c-fp-readme-name
- w99-c-fp-readme-content
- w99-c-fp-readme-length
prev: w99-n05
next: w99-n07
order: 6
official_blocks:
- readme_template
official_quotes:
- readme_name
- readme_include
- readme_words
- readme_paragraphs
- readme_750
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:09+03:30'
verified_at: '2026-10-31T16:15:00+03:30'
review_status: draft-needs-human-review
content_policy: 'Guidance only: faithful Persian rewrite of the official Final Project specification, with requirement sentences quoted in English verbatim (official99.REQ, checked against the live page). No project idea is prescribed and no project code or solution is given (D88). Authored planning tips are marked تألیفی. Callouts use GitHub-style markers followed by a bold Persian label line.'
---

# گام ۲: فایل README.md

> **منبع رسمی:** بخش «Step 2 of 3» از [صفحهٔ پروژهٔ نهایی CS50x 2026](https://cs50.harvard.edu/x/2026/project/#step-2-of-3). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. الزام‌های رسمی به انگلیسی و کلمه‌به‌کلمه نقل شده‌اند و مطالب **تألیفی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

طبق FAQ رسمی، دومین دلیل رایج قبول نشدن پروژهٔ نهایی، مستندات آن است. README.md جایی است که نشان می‌دهی پروژه چه می‌کند و چرا این‌طور طراحی شده است.

## نام و محل فایل

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> Create a README.md text file (named exactly that!) in your project folder that explains your project.

- نام فایل باید **دقیقاً** `README.md` باشد و در پوشهٔ `project` قرار بگیرد.

## چه چیزهایی باید در آن باشد

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> This file should include your Project Title, the URL of your video (created in step 1 above) and a description of your project.

- **عنوان پروژه**، **نشانی ویدئو** (از گام ۱) و **توضیح پروژه**.
- می‌توانی از این قالب رسمی استفاده کنی:

```markdown
# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
TODO
```

## طول و عمق

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> should at least be several hundred words that describe things in detail!

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> Your README.md file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them.

- دست‌کم **چند صد واژه**، و دست‌کم **چند پاراگراف**.
- باید بگوید پروژه **چیست**، هر **فایلی** که نوشتی **چه دارد و چه می‌کند**، و اگر میان چند **تصمیم طراحی** (`design choice`) مردد بودی، **چرا** آن را برگزیدی.

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> A README.md in the neighborhood of 750 words is likely to be sufficient for describing your project and all aspects of its functionality. If unable to reach that threshold, that probably means your project is insufficiently complex.

- حدود **۷۵۰ واژه** احتمالاً کافی است. اگر به آن نمی‌رسی، احتمالاً پروژه **به اندازهٔ کافی پیچیده نیست**.

> [!NOTE]
> **یادداشت دربارهٔ اعداد**
> «حدود ۷۵۰ واژه» در صفحهٔ رسمی راهنماست، نه حداقل سخت؛ صفحهٔ رسمی معیار نمره‌دهی جزئی‌تری منتشر نکرده است (d203). FAQ از «README یا DESIGN» نام می‌برد، اما مشخصات فعلی فقط `README.md` را می‌خواهد (d199).

> [!TIP]
> **تألیفی: یک ساختار پیشنهادی**
> بعد از سه سطر قالب رسمی، این بخش‌ها را به ترتیب بنویس: (۱) پروژه چیست و چه مسئله‌ای را حل می‌کند؛ (۲) چطور اجرا می‌شود؛ (۳) برای هر فایل، یک پاراگراف دربارهٔ این‌که چه دارد و چه می‌کند؛ (۴) تصمیم‌های طراحی و چرایی آن‌ها؛ (۵) ذکر منبع‌ها و ابزارهای هوش مصنوعی که استفاده کردی. این ساختار پیشنهاد CS50x Anzali است؛ الزام رسمی همان سه مورد و توضیح فایل‌ها و تصمیم‌هاست.

- اگر با Markdown آشنا نیستی، صفحهٔ رسمی به راهنمای «Basic Writing and Formatting Syntax» در GitHub و پیش‌نمایش Markdown در VS Code پیوند می‌دهد.

## پیوندها

- قبلی: [گام ۱: ویدئو و فرم](/kb/d/w99-n05)
- بعدی: [ارسال با submit50، کارنامه و گواهی](/kb/d/w99-n07)
- فهرست وارسی: `weeks/final-project/checklist.json` · واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/final-project/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
