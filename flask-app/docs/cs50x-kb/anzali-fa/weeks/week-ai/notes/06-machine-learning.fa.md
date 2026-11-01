---
id: w71-n06
type: note
title: یادگیری ماشین، یادگیری تقویتی و کاوش در برابر بهره‌برداری (Machine Learning)
title_fa: یادگیری ماشین، یادگیری تقویتی و کاوش در برابر بهره‌برداری
title_en: Machine Learning
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Machine Learning
official_anchor: machine-learning
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#machine-learning
source_refs:
- src-notes-71#machine-learning
- src-transcript-71
- src-anzali-authored-71
- src-srt-71
concept_ids:
- w71-c-machine-learning
- w71-c-reinforcement-learning
- w71-c-explore-exploit
prev: w71-n05
next: w71-n07
order: 6
video:
  youtube_id: -9bo8HlSxwQ
  start: '29:33'
  start_seconds: 1773
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=1773s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'machine learning, writing code'
official_blocks:
- epsilon
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# یادگیری ماشین، یادگیری تقویتی و کاوش در برابر بهره‌برداری

> **منبع رسمی:** بخش «Machine Learning» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#machine-learning). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۹:۳۳ تا حدود ۳۷:۳۱](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=1773s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

مینی‌ماکس فقط وقتی کار می‌کند که بتوانی همهٔ حالت‌ها را بشماری. وقتی نمی‌توانی، کامپیوتر باید از **تجربه** یاد بگیرد. این بخش **یادگیری ماشین** (`machine learning`) را از راه **یادگیری تقویتی** (`reinforcement learning`) معرفی می‌کند و یک ایدهٔ مهم را با یک متغیر ساده نشان می‌دهد.

## یاد گرفتن با پاداش

- درس‌نامه: یادگیری ماشین راهی است که کامپیوتر با آن از راه **تقویت** یاد می‌گیرد. از سخنرانی: مالان یادگیری تقویتی را «یک نوع» یادگیری ماشین نامید که خود ما انسان‌ها هم مدام به کار می‌بریم (d190).
- کامپیوتر می‌تواند یاد بگیرد **پنکیک** را برگرداند.
- کامپیوتر می‌تواند بازی **The Floor is Lava** را یاد بگیرد.
- کامپیوتر آزمایش پشت آزمایش تکرار می‌کند تا بفهمد کدام رفتارها را تکرار کند و کدام را نه.
- از سخنرانی: در ویدئوی پنکیک، پژوهشگر چند بار به ربات نشان داد چطور پنکیک را برگرداند و بعد ربات خودش تلاش کرد. کلید ماجرا این است که پشت صحنه نوعی **پاداش** و **جریمه** وجود دارد: نتیجهٔ خوب تشویق می‌شود و نتیجهٔ بد نه.
- از سخنرانی: در نسخهٔ «زمین گدازه است»، کامپیوتر خانه‌هایی را که به گدازه رسیدند به خاطر می‌سپارد و از آن‌ها پرهیز می‌کند و مسیری را که به خروجی رسید تکرار می‌کند. اما یک دانش‌آموز کلاس هفتم در جلسه دید که این مسیر **کوتاه‌ترین** مسیر نبود.

## کاوش در برابر بهره‌برداری

- در بسیاری از الگوریتم‌های هوش مصنوعی مفهوم **کاوش در برابر بهره‌برداری** (`explore vs. exploit`) وجود دارد: هوش مصنوعی گاهی به‌طور تصادفی کاری را امتحان می‌کند که شاید بهینه به نظر نرسد. **تصادف** می‌تواند به نتیجهٔ بهتری برسد.
- از سخنرانی: مالان گفت وقتی برای بار اول به رستورانی می‌رود و غذایی را دوست دارد، دیگر هیچ غذای دیگری از منو سفارش نمی‌دهد؛ شاید غذای بهتری آنجا باشد که هرگز کشفش نمی‌کند. اگر فقط ۱۰٪ مواقع چیز دیگری سفارش بدهد، شاید غذای فوق‌العاده‌ای پیدا کند.
- درس‌نامه این ایده را این‌طور نشان می‌دهد:

```text
epsilon = 0.10

If random() < epsilon:
    Make a random move
Else: 
    Make the move with the highest value
```

- دقت کن که `epsilon` **نرخ تصادف** را نشان می‌دهد. از سخنرانی: کامپیوتر عددی تصادفی بین ۰ و ۱ می‌سازد؛ اگر کمتر از `epsilon` باشد، که ۱۰٪ مواقع رخ می‌دهد، حرکتی تصادفی انجام می‌دهد.
- از سخنرانی: در Breakout، پارو اول کارهای تصادفی می‌کند، اما بعد از ۲۰۰ دور (`episode`) می‌فهمد که با زدن توپ امتیازش بالا می‌رود؛ و با بازی کافی، یاد می‌گیرد اگر از ردیف بالا راهی باز کند، بازی تقریباً خودش امتیاز جمع می‌کند.

**نمونهٔ تألیفی (پایتون):** برای اینکه خروجی قابل پیش‌بینی باشد، به جای `random()` از یک لیست عدد آماده استفاده می‌کنیم:

```python
epsilon = 0.10
values = {"up": 3, "right": 7, "down": 1}

for r in [0.50, 0.05, 0.90]:
    if r < epsilon:
        print("random move")
    else:
        best = "up"
        for move in values:
            if values[move] > values[best]:
                best = move
        print(best)
```

خروجی سه سطر است: `right`، `random move` و `right`. فقط عدد `0.05` از `epsilon` کمتر است.

## پیوندها

- قبلی: [مینی‌ماکس](/kb/d/w71-n05)
- بعدی: [یادگیری عمیق و شبکه‌های عصبی](/kb/d/w71-n07)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
