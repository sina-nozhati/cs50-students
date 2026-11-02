---
week: 71
week_slug: week-ai
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
generated_at: '2026-10-31T20:00:00+03:30'
review_status: draft-needs-human-review
id: w71-fa
type: week-overview
title: جلسهٔ هوش مصنوعی (پایگاه دانش فارسی)
title_fa: جلسهٔ هوش مصنوعی
title_en: Artificial Intelligence
parent: week-ai
source_type: translated-rewritten
origin: mixed
origin_detail: Official week topic line and notes structure rewritten in Persian; objectives, concept map, order and mastery criteria authored by CS50x Anzali
source_url: https://cs50.harvard.edu/x/weeks/ai/
source_refs:
- src-week-71
- src-notes-71#artificial-intelligence
- src-honesty-71
- src-code-71
- src-anzali-authored-71
children:
- w71-n01
- w71-n02
- w71-n03
- w71-n04
- w71-n05
- w71-n06
- w71-n07
- w71-n08
- w71-summary
objective_ids:
- w71-o01
- w71-o02
- w71-o03
- w71-o04
- w71-o05
- w71-o06
---

# جلسهٔ هوش مصنوعی (Artificial Intelligence)

> **منبع رسمی:** [صفحهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/weeks/ai/) و [درس‌نامهٔ آن](https://cs50.harvard.edu/x/2026/notes/ai/). خلاصه و فهرست مباحث بازنویسی فارسی منبع رسمی است. هدف‌ها، نقشهٔ یادگیری، ترتیب درس‌ها، نمونه‌های پایتون و معیار تسلط **تألیف CS50x Anzali** هستند.

## این جلسه دربارهٔ چیست؟

این سخنرانی ویژه، در ترتیب رسمی درس، بعد از هفتهٔ ۷ و پیش از هفتهٔ ۸ آمده است. از اردکی شروع می‌کند که در طول درس کنارت بوده، **اردک CS50**، و لایه‌به‌لایه نشان می‌دهد پشت آن چیست: **هوش مصنوعی مولد** (`generative AI`) و **پرامپت‌ها**، سپس ایده‌های قدیمی‌تر مثل **درخت تصمیم** و **مینی‌ماکس** در بازی‌ها، بعد **یادگیری ماشین** و **یادگیری تقویتی**، و در آخر **شبکه‌های عصبی** و **مدل‌های زبانی بزرگ**.

## مباحث رسمی جلسه

صفحهٔ رسمی این مباحث را فهرست می‌کند:

Prompt Engineering. System Prompt. User Prompt. Generative Artificial Intelligence. Artificial Intelligence. Decision Trees. Minimax. Machine Learning. Reinforcement Learning. Explore vs. Exploit. Deep Learning. Neural Networks. Large Language Models. Transformer Architecture. Hallucinations.

> **توجه:** این جلسه پرابلم‌ست، آزمایشگاه، جلسهٔ حل تمرین و ویدئوی کوتاه ندارد. کد منبع سخنرانی `chat3.py` و پوشهٔ `speller/` است؛ `chat3.py` در یادداشت ۳ آمده و Speller (کد توزیعی پرابلم‌ست ۵) در این بسته بازتولید نشده است (D82، D84، d193).

## قاعدهٔ CS50 دربارهٔ هوش مصنوعی

درس‌نامه: در CS50 استفاده از هوش مصنوعی مولد **بیرون از ابزارهای خود درس** مجاز نیست. طبق [سیاست صداقت تحصیلی](https://cs50.harvard.edu/x/honesty/)، استفاده از نرم‌افزارهای هوش مصنوعی خود CS50، از جمله اردک CS50 در cs50.ai و cs50.dev، معقول است؛ استفاده از نرم‌افزارهای هوش مصنوعی دیگر (مثل ChatGPT، Claude، Copilot، Gemini) که پاسخ پرسش‌ها یا سطرهای کد را پیشنهاد یا کامل می‌کند، نامعقول است. جزئیات در [یادداشت ۳](/kb/d/w71-n03).

## هدف‌های یادگیری

> **تألیفی:** این هدف‌ها را CS50x Anzali از درس‌نامه و سخنرانی استخراج کرده است.

- **w71-o01** — بگویی اردک CS50 چیست، چرا عمداً پاسخ را لو نمی‌دهد و قاعدهٔ رسمی CS50 دربارهٔ ابزارهای هوش مصنوعی چیست.
- **w71-o02** — هوش مصنوعی مولد، پرامپت سیستمی و پرامپت کاربر را توضیح بدهی و نقش `input`، `instructions` و `model` را در `chat3.py` بگویی.
- **w71-o03** — شبه‌کد درخت تصمیم Breakout را بخوانی و به پایتون ترجمه کنی.
- **w71-o04** — مینی‌ماکس را با امتیاز ۱، ۰ و ۱- توضیح بدهی و بگویی چرا برای بازی‌های بزرگ کافی نیست.
- **w71-o05** — یادگیری تقویتی و کاوش در برابر بهره‌برداری را با `epsilon` توضیح بدهی.
- **w71-o06** — یادگیری با نظارت و بدون نظارت، شبکهٔ عصبی و پارامترها، و ایدهٔ مدل‌های زبانی بزرگ و توهم را توضیح بدهی.

## پیش‌نیازها

- هفتهٔ ۰ (شبه‌کد و شرط‌ها) و هفتهٔ ۳ (بازگشت). ([نمای کلی هفتهٔ ۰](/kb/d/w00-fa))
- هفتهٔ ۶ (پایتون): همهٔ نمونه‌ها و تمرین‌های این جلسه پایتون‌اند. ([نمای کلی هفتهٔ ۶](/kb/d/w06-fa))

## نقشهٔ یادگیری

> **تألیفی:** نقشهٔ مفهومی زیر استنتاج آموزشی است. نسخهٔ کامل در `curriculum.json` است.

```text
مرحلهٔ ۱: اردک و پرامپت
  اردک‌گویی -> اردک CS50 -> هوش مصنوعی مولد -> پرامپت سیستمی و کاربر -> قاعدهٔ CS50

مرحلهٔ ۲: بازی‌ها
  درخت تصمیم (Breakout) -> امتیاز نتیجه‌ها -> مینی‌ماکس -> اندازهٔ درخت بازی

مرحلهٔ ۳: یادگیری ماشین
  پاداش و جریمه -> یادگیری تقویتی -> کاوش در برابر بهره‌برداری (epsilon)

مرحلهٔ ۴: یادگیری عمیق
  با نظارت و بدون نظارت -> شبکهٔ عصبی و پارامترها -> مدل زبانی بزرگ -> توهم
```

## ترتیب پیشنهادی

1. یادداشت‌های سخنرانی را به ترتیب بخوان (۸ بخش). هر یادداشت پیوند زمانی ویدئو دارد.
2. هم‌زمان درس‌های کوتاه (micro-lesson) هر بخش را بگذران.
3. چالش‌های اختیاری را حل کن و آزمون تسلط جلسه را بده.

## معیار تسلط بر جلسه

> **تألیفی:** پیشنهاد CS50x Anzali و قابل تنظیم (پیش‌فرض موقت).

- همهٔ درس‌های کوتاه جلسه «مسلط» شده باشند.
- نمرهٔ آزمون تسلط جلسه دست‌کم ۸۰٪ باشد.
- نرخ یادآوری فلش‌کارت‌ها در ۲۰ مرور آخر دست‌کم ۸۰٪ باشد.

## پیوندهای رسمی

- [صفحهٔ جلسه](https://cs50.harvard.edu/x/weeks/ai/) · [درس‌نامه](https://cs50.harvard.edu/x/2026/notes/ai/) · [ویدئوی سخنرانی](https://video.cs50.io/-9bo8HlSxwQ) · [کد منبع](https://cdn.cs50.net/2025/fall/lectures/ai/src/) · [CS50.ai](https://cs50.ai) · [صداقت تحصیلی](https://cs50.harvard.edu/x/honesty/)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
