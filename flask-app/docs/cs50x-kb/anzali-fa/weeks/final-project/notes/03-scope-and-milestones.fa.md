---
id: w99-n03
type: note
title: دامنه، نقطه‌های عطف و نسخه‌بندی (Scope, Milestones and Version Control)
title_fa: دامنه، نقطه‌های عطف و نسخه‌بندی
title_en: Scope, Milestones and Version Control
week: 99
week_slug: final-project
parent: w99-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Getting Started
official_anchor: getting-started
source_url: https://cs50.harvard.edu/x/2026/project/#getting-started
source_refs:
- src-project-99#getting-started
- src-notes-10#looking-ahead
- src-anzali-authored-99
concept_ids:
- w99-c-fp-questions
- w99-c-fp-outcomes
- w99-c-fp-milestones
- w99-c-fp-project-dir
- w99-c-fp-version-control
prev: w99-n02
next: w99-n04
order: 3
official_blocks: []
official_quotes:
- outcomes
- milestones
- project_dir
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:09+03:30'
verified_at: '2026-10-31T16:15:00+03:30'
review_status: draft-needs-human-review
content_policy: 'Guidance only: faithful Persian rewrite of the official Final Project specification, with requirement sentences quoted in English verbatim (official99.REQ, checked against the live page). No project idea is prescribed and no project code or solution is given (D88). Authored planning tips are marked تألیفی. Callouts use GitHub-style markers followed by a bold Persian label line.'
---

# دامنه، نقطه‌های عطف و نسخه‌بندی

> **منبع رسمی:** بخش «Getting Started» از [صفحهٔ پروژهٔ نهایی CS50x 2026](https://cs50.harvard.edu/x/2026/project/#getting-started). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. الزام‌های رسمی به انگلیسی و کلمه‌به‌کلمه نقل شده‌اند و مطالب **تألیفی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

صفحهٔ رسمی صادقانه می‌گوید: در دنیای نرم‌افزار تقریباً همه‌چیز بیش از آنچه فکر می‌کنی طول می‌کشد. پس پیش از شروع، باید بدانی «کافی» یعنی چه.

## پرسش‌های آغاز کار

صفحهٔ رسمی پیشنهاد می‌کند در شروع به این پرسش‌ها فکر کنی:

- نرم‌افزارت چه می‌کند؟ چه قابلیت‌هایی دارد؟ چطور اجرا می‌شود؟
- چه مهارت‌های تازه‌ای باید یاد بگیری؟ دربارهٔ چه موضوع‌هایی باید جست‌وجو کنی؟
- اگر با یک یا دو هم‌کلاسی کار می‌کنی، چه کسی چه می‌کند؟
- نتیجهٔ **خوب** برای پروژه‌ات چیست؟ نتیجهٔ **بهتر**؟ و **بهترین**؟

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> What might you consider to be a good outcome for your project? A better outcome? The best outcome?

## نقطه‌های عطف

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> Consider making goal milestones to keep you on track.

- **نقطهٔ عطف** (`milestone`) هدف میانی‌ای است که می‌توانی بگویی به آن رسیدی یا نه.

> [!TIP]
> **تألیفی: یک الگوی ساده برای نقطه‌های عطف**
> سه سطح «خوب، بهتر، بهترین» را به سه نقطهٔ عطف تبدیل کن. «خوب» باید کوچک‌ترین نسخه‌ای باشد که واقعاً کار می‌کند و می‌شود نشانش داد. هر نقطهٔ عطف را با یک جملهٔ قابل‌آزمون بنویس («کاربر می‌تواند …»)، نه با یک حس («تقریباً تمام شد»). یک تاریخ تقریبی هم کنارش بگذار و آن را دست‌کم چند هفته پیش از مهلت رسمی قرار بده، چون ویدئو و README هم وقت می‌خواهند.

## پوشهٔ project

- اگر از CS50 Codespace استفاده می‌کنی، پوشه‌ای به نام `project` بساز و کد و فایل‌های پروژه را در آن نگه دار.
- می‌توانی بیرون از Codespace هم پروژه را بسازی.

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> If using the CS50 Codespace, create a directory called project to store your project source code and other files.

## نسخه‌بندی (`version control`)

- صفحهٔ پروژه نسخه‌بندی را آموزش نمی‌دهد. فقط می‌گوید هنگام `submit50` با نام کاربری GitHub وارد می‌شوی و، اگر ارسال بزرگ بود، می‌توانی فایل‌ها را در شاخهٔ `cs50/problems/2026/x/project` از مخزن `github.com/me50/USERNAME` بارگذاری کنی (d202).
- در [هفتهٔ ۱۰](/kb/d/w10-n03) Git به‌عنوان ابزاری برای نسخه‌بندی معرفی شد.

> [!NOTE]
> **تألیفی: چرا نسخه‌بندی کمک می‌کند**
> پروژهٔ چندهفته‌ای یعنی روزهایی که چیزی را خراب می‌کنی و می‌خواهی به نسخهٔ دیروز برگردی. نسخه‌بندی همین را ممکن می‌کند و در کار گروهی نشان می‌دهد چه کسی چه چیزی را تغییر داده است. این پیشنهاد است، نه الزام رسمی.

## پیوندها

- قبلی: [انتخاب ایده و ابزار](/kb/d/w99-n02)
- بعدی: [صداقت تحصیلی و استفادهٔ مجاز از هوش مصنوعی](/kb/d/w99-n04)
- فهرست وارسی: `weeks/final-project/checklist.json` · واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/final-project/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
