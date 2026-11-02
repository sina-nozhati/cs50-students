---
id: w71-n04
type: note
title: هوش مصنوعی در بازی‌ها و درخت تصمیم (AI and Decision Trees)
title_fa: هوش مصنوعی در بازی‌ها و درخت تصمیم
title_en: AI and Decision Trees
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Decision Trees
official_anchor: decision-trees
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#decision-trees
source_refs:
- src-notes-71#decision-trees
- src-transcript-71
- src-anzali-authored-71
- src-srt-71
concept_ids:
- w71-c-classic-ai
- w71-c-decision-tree
- w71-c-breakout-pseudocode
prev: w71-n03
next: w71-n05
order: 4
video:
  youtube_id: -9bo8HlSxwQ
  start: '17:50'
  start_seconds: 1070
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=1070s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'So spam'
official_blocks:
- breakout
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# هوش مصنوعی در بازی‌ها و درخت تصمیم

> **منبع رسمی:** بخش «Decision Trees» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#decision-trees). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱۷:۵۰ تا حدود ۲۳:۵۶](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=1070s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

هوش مصنوعی پدیدهٔ تازه‌ای نیست. پیش از مدل‌های زبانی، الگوریتم‌هایی سال‌ها همان کاری را می‌کردند که تو از هفتهٔ ۰ می‌نویسی: شرط، حلقه و تصمیم. این بخش نشان می‌دهد ساده‌ترین «هوش» یک بازی چیزی جز چند `if` نیست.

## هوش مصنوعی از دهه‌ها پیش

- هوش مصنوعی **دهه‌هاست** همراه ماست. نرم‌افزار مدت‌هاست خودش را با کاربر تطبیق می‌دهد.
- الگوریتم‌ها در **ایمیل‌های ناخواسته** (`spam`)، در **تشخیص دست‌خط**، در پیشنهاد فیلم و ویدئو و در **بازی کردن** به دنبال الگو می‌گردند.
- از سخنرانی: مالان از پیشنهادهای Netflix و دستیارهای صوتی هم نام برد، و از بازی‌های قدیمی مثل Pong و Breakout، که در آن‌ها حریف کامپیوتری باید تصمیم بگیرد پاروی خودش را کجا ببرد.
- در بازی‌ها، **دستورهای گام‌به‌گام** می‌توانند به یک حریف کامپیوتری اجازه دهند Breakout بازی کند.

## درخت تصمیم

- **درخت تصمیم** (`decision tree`) ابزاری است که یک الگوریتم با آن تصمیم می‌گیرد چه کاری بکند.
- برای نمونه، در Breakout الگوریتم می‌تواند بر اساس این دستورها انتخاب کند:

```text
While game is ongoing:
  If ball is left of paddle:
    Move paddle left
  Else if ball is right of paddle:
    Move paddle right
  Else:
    Don't move paddle
```

- این همان **شبه‌کد** (`pseudocode`) هفتهٔ ۰ است: یک حلقه و یک زنجیرهٔ `if`/`else if`/`else`.
- از سخنرانی: مالان همین را به‌صورت درخت کشید: «آیا توپ سمت چپ پارو است؟» اگر بله، به چپ برو. اگر نه، «آیا سمت راست است؟» اگر بله، به راست برو؛ وگرنه حرکت نکن.
- بیشتر بازی‌ها سعی می‌کنند **تعداد محاسباتی** را که برای رقابت با بازیکن لازم است کم کنند.

**نمونهٔ تألیفی (پایتون):** همان شبه‌کد برای یک لحظه از بازی. مکان توپ و پارو فقط دو عدد روی محور افقی‌اند:

```python
def move(ball, paddle):
    if ball < paddle:
        return "left"
    elif ball > paddle:
        return "right"
    else:
        return "stay"


print(move(3, 5))
print(move(5, 5))
```

خروجی این برنامه `left` و سپس `stay` است.

> [!NOTE]
> **تألیفی: چرا این «هوش» است؟**
> این برنامه چیزی یاد نمی‌گیرد؛ هر رفتارش را برنامه‌نویس از پیش نوشته است. برای بازی ساده‌ای مثل Breakout کافی است، اما برای بازی‌هایی با حالت‌های بسیار زیاد، نوشتن همهٔ شرط‌ها با دست ممکن نیست. بخش‌های بعدی همین مشکل را دنبال می‌کنند.

## پیوندها

- قبلی: [مهندسی پرامپت، کد chat3.py و Copilot](/kb/d/w71-n03)
- بعدی: [مینی‌ماکس](/kb/d/w71-n05)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
