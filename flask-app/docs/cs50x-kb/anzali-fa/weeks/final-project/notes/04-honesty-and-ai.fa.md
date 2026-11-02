---
id: w99-n04
type: note
title: صداقت تحصیلی و استفادهٔ مجاز از هوش مصنوعی (Academic Honesty and Acceptable AI Use)
title_fa: صداقت تحصیلی و استفادهٔ مجاز از هوش مصنوعی
title_en: Academic Honesty and Acceptable AI Use
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
- src-honesty-99
- src-anzali-authored-99
concept_ids:
- w99-c-fp-ai-allowed
- w99-c-fp-ai-cite
- w99-c-fp-honesty-cite
prev: w99-n03
next: w99-n05
order: 4
official_blocks: []
official_quotes:
- ai
- ai_amplify
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:09+03:30'
verified_at: '2026-10-31T16:15:00+03:30'
review_status: draft-needs-human-review
content_policy: 'Guidance only: faithful Persian rewrite of the official Final Project specification, with requirement sentences quoted in English verbatim (official99.REQ, checked against the live page). No project idea is prescribed and no project code or solution is given (D88). Authored planning tips are marked تألیفی. Callouts use GitHub-style markers followed by a bold Persian label line.'
---

# صداقت تحصیلی و استفادهٔ مجاز از هوش مصنوعی

> **منبع رسمی:** بخش «Getting Started» از [صفحهٔ پروژهٔ نهایی CS50x 2026](https://cs50.harvard.edu/x/2026/project/#getting-started). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. الزام‌های رسمی به انگلیسی و کلمه‌به‌کلمه نقل شده‌اند و مطالب **تألیفی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

قاعدهٔ هوش مصنوعی در پروژهٔ نهایی با بقیهٔ درس **فرق دارد**. اگر این تفاوت را دقیق ندانی، ممکن است یا بی‌جهت از ابزاری مجاز دوری کنی، یا بدتر، فکر کنی همان آزادی در پرابلم‌ست‌ها هم هست.

## قاعدهٔ رسمی پروژهٔ نهایی

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> For your final project (and your final project only!) it is reasonable to use AI-based software other than CS50’s own (e.g., ChatGPT, GitHub Copilot, Bing Chat, et al.), but the essence of the work must still be your own.

> **متن رسمی (انگلیسی، کلمه‌به‌کلمه):**
>
> Treat such tools as amplifying, not supplanting, your productivity. But you still must cite any use of such tools in the comments of your code.

- **فقط** در پروژهٔ نهایی، استفاده از نرم‌افزار هوش مصنوعی غیر از ابزارهای خود CS50 معقول است. نمونه‌های صفحهٔ پروژه: ChatGPT، GitHub Copilot و Bing Chat.
- **جوهر کار** باید همچنان مال خودت باشد.
- این ابزارها باید بهره‌وری‌ات را **تقویت** کنند، نه این‌که **جای تو** را بگیرند.
- هر استفاده از این ابزارها را باید در **توضیحات کد** (`comments`) ذکر کنی.

> [!WARNING]
> **این استثنا فقط برای پروژهٔ نهایی است**
> سیاست [صداقت تحصیلی](https://cs50.harvard.edu/x/honesty/) برای بقیهٔ درس می‌گوید: استفاده از نرم‌افزارهای هوش مصنوعی خود CS50، از جمله اردک CS50 در cs50.ai و cs50.dev، معقول است؛ استفاده از نرم‌افزارهای هوش مصنوعی دیگر (مثل ChatGPT، Claude، Copilot، Gemini) که پاسخ پرسش‌ها یا سطرهای کد را پیشنهاد یا کامل می‌کند، نامعقول است. صفحهٔ صداقت تحصیلی خودش از استثنای پروژهٔ نهایی نام نمی‌برد؛ این استثنا از صفحهٔ پروژه است (d196، d197).

## صداقت تحصیلی در پروژه

صفحهٔ صداقت تحصیلی، از جمله، این‌ها را **معقول** می‌داند:

- آوردن **چند سطر** کدی که در وب یا جای دیگر پیدا کردی، به شرط آن‌که خودشان راه‌حل کار تعیین‌شده نباشند و **منشأ** آن سطرها را ذکر کنی.
- رفتن به وب برای آموزش، مرجع و حل مشکل‌های فنی، ولی نه برای راه‌حل آماده.

و این‌ها را **نامعقول**:

- ذکر نکردن منشأ کد یا تکنیکی که بیرون از درس پیدا کردی و در کارت به کار بردی.
- ارسال کار کس دیگر (حتی با تغییر)، بیش از همان چند سطر مجاز.
- ارسال کار یکسان یا مشابه به این درس و درسی دیگر، مگر صریحاً مجاز باشد.

> [!NOTE]
> **کار گروهی**
> صفحهٔ صداقت تحصیلی «تقسیم کار با فرد دیگر و ترکیب کارها» را نامعقول می‌داند؛ پروژهٔ نهایی صریحاً گروه دو یا سه نفره را با سهم برابر مجاز می‌کند (d198). این اجازه فقط برای پروژهٔ نهایی است.

> [!TIP]
> **تألیفی: چطور ذکر منبع کنم؟**
> بالای هر فایل یا کنار هر بخشی که با کمک ابزار هوش مصنوعی یا از منبعی بیرونی نوشتی، در یک توضیح کوتاه بنویس از چه ابزار یا منبعی و برای چه کاری کمک گرفتی. قاعدهٔ رسمی فقط می‌گوید «در توضیحات کد»؛ قالب دقیق را صفحهٔ رسمی تعیین نکرده است. یک آزمون ساده: آیا می‌توانی هر سطر پروژه را برای کسی توضیح بدهی؟ اگر نه، آن بخش هنوز «کار خودت» نیست.

## پیوندها

- قبلی: [دامنه، نقطه‌های عطف و نسخه‌بندی](/kb/d/w99-n03)
- بعدی: [گام ۱: ویدئو و فرم](/kb/d/w99-n05)
- فهرست وارسی: `weeks/final-project/checklist.json` · واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/final-project/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
