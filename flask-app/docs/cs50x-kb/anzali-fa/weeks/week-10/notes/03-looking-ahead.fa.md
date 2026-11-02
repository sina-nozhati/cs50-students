---
id: w10-n03
type: note
title: 'نگاه به آینده: ابزارهای بعد از CS50 (Looking Ahead)'
title_fa: 'نگاه به آینده: ابزارهای بعد از CS50'
title_en: Looking Ahead
week: 10
parent: w10-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Looking Ahead
official_anchor: looking-ahead
source_url: https://cs50.harvard.edu/x/2026/notes/10/#looking-ahead
source_refs:
- src-notes-10#looking-ahead
- src-transcript-10
- src-looking-ahead-links-10
- src-cs50-dev
- src-communities
- src-anzali-authored-10
- src-srt-10
concept_ids:
- w10-c-editors
- w10-c-command-line-tools
- w10-c-git
- w10-c-static-hosting
- w10-c-web-app-hosting
- w10-c-ai-tools-ahead
- w10-c-more-cs50
prev: w10-n02
next: w10-n04
order: 3
video:
  youtube_id: ApQTgFkf8TU
  start: '30:13'
  start_seconds: 1813
  url: https://www.youtube.com/watch?v=ApQTgFkf8TU&t=1813s
  origin: inference
  basis: first lecture10.srt cue (after the previous note's cue) containing the phrase 'using Visual Studio Code for CS'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:40:25+03:30'
verified_at: '2026-10-29T19:40:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official notes (which contain no code); transcript-only facts are marked «از سخنرانی»; authored material is marked تألیفی. All third-party links are copied from the official notes. Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# نگاه به آینده: ابزارهای بعد از CS50

> **منبع رسمی:** بخش «Looking Ahead» از [درس‌نامهٔ هفتهٔ ۱۰ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/10/#looking-ahead). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۰:۱۳ تا حدود ۳۸:۴۰](https://www.youtube.com/watch?v=ApQTgFkf8TU&t=1813s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

در CS50 همه‌چیز در cs50.dev آماده بود. بیرون از درس، خودت ابزارها را نصب و پیکربندی می‌کنی. این بخش نقشهٔ راه همین گذار است؛ همهٔ پیوندها از درس‌نامهٔ رسمی‌اند و فهرست‌ها، به گفتهٔ خود سخنرانی، پیشنهادهای سلیقه‌ای تیم درس‌اند، نه فهرست کامل.

## ویرایشگر و خط فرمان

- با رفتن از کار این درس به دنیای بیرون از CS50، شاید بخواهی چند گام برای آماده شدن برداری.
- [VS Code را بارگیری کن](https://code.visualstudio.com/) و [درباره‌اش بیاموز](https://code.visualstudio.com/docs). [Cursor](https://cursor.com) و [Windsurf](https://windsurf.com) ویرایشگرهای متنی محبوب دیگری‌اند.
- برای اجرای فرمان در ترمینال، همان‌طور که در [CS50.dev](https://cs50.dev) کار می‌کردی، ابزارهای خط فرمان را روی [مک](https://developer.apple.com/xcode/) یا [رایانهٔ ویندوزی](https://learn.microsoft.com/en-us/windows/wsl/about) نصب کن.
- از سخنرانی: cs50.dev نسخهٔ سازگارشده‌ای از GitHub Codespaces است، یعنی VS Code در فضای ابری؛ پس تو همین حالا با ابزاری کار کرده‌ای که در صنعت رایج است. اگر بخواهی همان نرم‌افزارهای ازپیش‌نصب CS50 را روی رایانهٔ خودت داشته باشی، مستندات CS50 شیوهٔ کار با **Docker** (کانتینرسازی) را توضیح می‌دهد.
- از سخنرانی: نصب روی رایانهٔ خودت ممکن است دردسرهای فنی داشته باشد (مثلاً جداگانه نصب کردن پایتون)؛ این عادی است و دلیلش همین است که درس از روز اول این کار را از تو نخواست.

## Git و میزبانی

- [دربارهٔ Git بیشتر بیاموز](https://youtu.be/MJUJ4wbFm_A).
- یک وب‌سایت را با [GitHub](https://pages.github.com/) میزبانی کن.
- اگر لازم شد، یک برنامهٔ وب را روی [AWS](https://aws.amazon.com/education/awseducate/)، [Azure](https://azure.microsoft.com/en-us/free/students/)، [Google Cloud](https://cloud.google.com/edu/students)، [Cloudflare](https://www.cloudflare.com/students)، [Heroku](https://heroku.com) یا [Vercel](https://vercel.com) میزبانی کن.
- از سخنرانی: Git استاندارد رایج امروز برای همکاری و نگه‌داشتن نسخه‌های کد است؛ CS50 آن را پنهان کرده بود و مثلاً «تاریخچه» در cs50.dev در پشت صحنه با Git کار می‌کند. پیوند بالا آموزش Git از Brian Yu از تیم CS50 است.
- از سخنرانی: برای کار گروهی روی پروژهٔ نهایی، Live Share در VS Code اجازه می‌دهد هم‌زمان در یک فضای کد کار کنید.
- از سخنرانی: برای سایت **ایستا** (فقط HTML و CSS و جاوااسکریپت، بدون پایتون و Flask) GitHub Pages یا Netlify گزینه‌های رایگان رایج‌اند؛ برای **برنامهٔ وب** که سمت سرور یا پایگاه داده دارد، سراغ فهرست دوم می‌روی که بسیاری‌شان حساب دانشجویی دارند.

## پرسیدن و ادامهٔ یادگیری

- پرسش‌هایت را در جامعه‌های آنلاین مرتبط بپرس.
- با ابزارهای مبتنی بر هوش مصنوعی مثل [ChatGPT](https://chat.openai.com/)، [Claude](https://claude.ai)، [Gemini](https://gemini.google.com)، [GitHub Copilot](https://github.com/features/copilot)، [Codex](https://openai.com/codex) یا [v0](https://v0.app) پرسش کن.
- هر یک از [درس‌های دیگر CS50](https://edX.org/cs50) را بگذران.
- به یکی از [جامعه‌های](https://cs50.harvard.edu/communities) فراوان CS50 بپیوند.
- از سخنرانی: اردک CS50 عمداً محدود بود تا معلم خوبی باشد؛ برای پروژهٔ نهایی می‌توانی از این ابزارها برای **بالا بردن بهره‌وری خودت** استفاده کنی، «نه اینکه کار را به‌جای تو انجام دهند». ساده‌ترین شروع، به گفتهٔ او، روشن کردن GitHub Copilot در فضای کد CS50 طبق مستندات CS50 است.
- از سخنرانی: برای پاسخ انسانی هنوز Reddit، Stack Overflow و Server Fault جای خوبی‌اند؛ برای خبرهای فناوری TechCrunch و Hacker News را نام برد. درس‌های دیگر CS50 (مثلاً پایتون، SQL، R، امنیت سایبری و ساخت بازی) در edX رایگان در دسترس‌اند.

> [!IMPORTANT]
> **تألیفی: قانون استفاده از هوش مصنوعی**
> این اجازه فقط برای **پروژهٔ نهایی** است. در مسئله‌های هفته‌های ۰ تا ۹ همان قانون همیشگی درس برقرار است: فقط ابزارهای هوش مصنوعی خود CS50 مثل اردک.

## پیوندها

- قبلی: [پروژهٔ نهایی، هکاتون و نمایشگاه CS50](/kb/d/w10-n02)
- بعدی: [سپاس و جمع‌بندی](/kb/d/w10-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-10/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
