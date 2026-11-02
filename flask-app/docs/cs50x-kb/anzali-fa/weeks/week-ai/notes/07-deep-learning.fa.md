---
id: w71-n07
type: note
title: یادگیری عمیق و شبکه‌های عصبی (Deep Learning)
title_fa: یادگیری عمیق و شبکه‌های عصبی
title_en: Deep Learning
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Deep Learning
official_anchor: deep-learning
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#deep-learning
source_refs:
- src-notes-71#deep-learning
- src-transcript-71
- src-slide-images-71
- src-anzali-authored-71
- src-srt-71
concept_ids:
- w71-c-supervised-learning
- w71-c-unsupervised-learning
- w71-c-neural-network
- w71-c-parameters
prev: w71-n06
next: w71-n08
order: 7
video:
  youtube_id: -9bo8HlSxwQ
  start: '37:31'
  start_seconds: 2251
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=2251s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'supervised'
official_blocks: []
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# یادگیری عمیق و شبکه‌های عصبی

> **منبع رسمی:** بخش «Deep Learning» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#deep-learning). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۳۷:۳۱ تا حدود ۴۲:۵۲](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=2251s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

یادگیری تقویتی به پاداش نیاز دارد و یادگیری با کمک انسان به برچسب. برای مسئله‌های بزرگ هیچ‌کدام کافی نیست. این بخش نشان می‌دهد **شبکهٔ عصبی** (`neural network`) چطور از روی داده **پارامترهایی** پیدا می‌کند که هیچ انسانی تک‌تک ننوشته است.

## یادگیری با نظارت و بدون نظارت

- **یادگیری با نظارت** (`supervised learning`) شکلی از یادگیری است که در آن انسان با هوش مصنوعی همکاری می‌کند. برای نمونه، وقتی در برنامهٔ ایمیلت دکمهٔ «spam» را می‌زنی، به هوش مصنوعی یاد می‌دهی کدام ایمیل‌ها را ناخواسته بداند.
- اما یادگیری با نظارت برای مسئله‌های بزرگ‌تر خوب **مقیاس‌پذیر** نیست. به همین دلیل **یادگیری بدون نظارت** (`unsupervised learning`) راهی است که هوش مصنوعی با کمترین دخالت انسان یاد بگیرد.
- از سخنرانی: برچسب زدن میلیون‌ها یا میلیاردها داده برای انسان واقع‌بینانه نیست.

## یادگیری عمیق و شبکهٔ عصبی

- **یادگیری عمیق** (`deep learning`) از شبکه‌های عصبی استفاده می‌کند تا مسئله‌ها و راه‌حل‌ها را بکاود.
- برای نمونه، یادگیری عمیق می‌تواند پیش‌بینی کند که در نقطه‌ای از یک نمودار، نقطهٔ **آبی** ظاهر می‌شود یا **قرمز**: [اسلاید ۲۰۸](https://cs50.harvard.edu/x/notes/ai/cs50AiLectureSlide208.png).
- از دادهٔ آموزشی موجود برای پیش‌بینی نتیجه استفاده می‌شود. هوش مصنوعی ممکن است دادهٔ آموزشی بیشتری هم بسازد تا الگوهای بیشتری کشف کند.
- یادگیری عمیق **گره‌هایی** می‌سازد که ورودی‌ها را به خروجی‌ها مرتبط می‌کنند: [اسلاید ۲۱۰](https://cs50.harvard.edu/x/notes/ai/cs50AiLectureSlide210.png).
- از سخنرانی: نورون‌های مغز در این تصویر به دایره و یال تبدیل می‌شوند، یعنی همان **گراف**. برای جدا کردن نقطه‌های آبی و قرمز، شبکه دنبال خطی می‌گردد: اگر `ax + by + c > 0` باشد آبی، وگرنه قرمز. اعداد `a`، `b` و `c` همان **پارامترهای** شبکه‌اند و از داده به دست می‌آیند. شبکه‌های واقعی میلیاردها از این‌ها دارند.

**نمونهٔ تألیفی (پایتون):** یک «نورون» با پارامترهای آماده. در یک شبکهٔ واقعی این اعداد آموخته می‌شوند، نه نوشته:

```python
a, b, c = 1, -1, 0


def color(x, y):
    if a * x + b * y + c > 0:
        return "blue"
    return "red"


print(color(3, 1))
print(color(1, 3))
```

خروجی `blue` و سپس `red` است.

## پیوندها

- قبلی: [یادگیری ماشین، یادگیری تقویتی و کاوش در برابر بهره‌برداری](/kb/d/w71-n06)
- بعدی: [مدل‌های زبانی بزرگ، توجه و توهم](/kb/d/w71-n08)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
