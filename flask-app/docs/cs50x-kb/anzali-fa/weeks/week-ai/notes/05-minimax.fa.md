---
id: w71-n05
type: note
title: مینی‌ماکس (Minimax)
title_fa: مینی‌ماکس
title_en: Minimax
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Minimax
official_anchor: minimax
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#minimax
source_refs:
- src-notes-71#minimax
- src-transcript-71
- src-slide-images-71
- src-anzali-authored-71
- src-anzali-inference-71
- src-srt-71
concept_ids:
- w71-c-score-outcomes
- w71-c-minimax
- w71-c-game-tree-size
prev: w71-n04
next: w71-n06
order: 5
video:
  youtube_id: -9bo8HlSxwQ
  start: '23:56'
  start_seconds: 1436
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=1436s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'called Mini Max'
official_blocks:
- minimax
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# مینی‌ماکس

> **منبع رسمی:** بخش «Minimax» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#minimax). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲۳:۵۶ تا حدود ۲۹:۳۳](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=1436s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

وقتی بازی پیچیده‌تر می‌شود، به جای نوشتن شرط برای هر وضعیت، می‌توان به هر نتیجه **عدد** داد و بهترین حرکت را حساب کرد. **مینی‌ماکس** (`minimax`) دقیقاً همین کار را می‌کند و همان **بازگشت** (`recursion`) هفتهٔ ۳ را دوباره به کار می‌گیرد.

## امتیاز دادن به نتیجه‌ها

- هوش مصنوعی اغلب در بازی خوب است، چون حرکت‌ها و نتیجه‌ها را به **مقدارهای ریاضی** تبدیل می‌کند.
- می‌توان تصور کرد الگوریتمی به نتیجه‌ها امتیاز **مثبت، منفی و خنثی** بدهد.
- در دوز (`tic-tac-toe`)، هوش مصنوعی می‌تواند صفحه‌ای را که کامپیوتر در آن می‌برد ۱ و صفحه‌ای را که می‌بازد ۱- در نظر بگیرد.
- از سخنرانی: مالان امتیازها را این‌طور تعریف کرد: اگر O ببرد ۱-، اگر X ببرد ۱ و اگر مساوی شود ۰. پس X می‌خواهد امتیاز را **بیشینه** کند و O می‌خواهد آن را **کمینه** کند (d189).
- کامپیوتر به درختی از نتیجه‌های ممکن نگاه می‌کند و به هر حرکت ممکن امتیاز می‌دهد. سپس با بیشینه کردن امتیاز خودش برای بردن تلاش می‌کند.

## شبه‌کد مینی‌ماکس

درس‌نامه این ایده را برای دوز این‌طور می‌نویسد (تورفتگی دو شاخه در متن رسمی یکسان نیست و همان‌طور حفظ شده است):

```text
If player is X:
  For each possible move:
    Calculate score for board
  Choose move with highest score

Else if player is O:
    For each possible move:
        Calculate score for board
    Choose move with lowest score
```

- تصویر این درخت در درس‌نامه: [اسلاید ۱۳۲](https://cs50.harvard.edu/x/notes/ai/cs50AiLectureSlide132.png).
- از سخنرانی: «همهٔ امکان‌ها را به‌صورت ریاضی امتحان کن و بعد تصمیم بگیر.» برای O همان کار انجام می‌شود، اما کمترین امتیاز انتخاب می‌شود.
- تألیفی: برای «امتیاز صفحه را حساب کن» باید فرض کنی حرکت انجام شده و همین پرسش را از دید **حریف** بپرسی؛ یعنی الگوریتم می‌تواند خودش را صدا بزند. نمونهٔ پایین همین برداشت است و متن رسمی آن را این‌طور بیان نکرده است.

**نمونهٔ تألیفی (پایتون):** درختی کوچک که برگ‌هایش امتیاز پایانی‌اند و هر لیست یعنی «نوبت کسی است که باید انتخاب کند»:

```python
def minimax(node, player):
    if type(node) == int:
        return node
    scores = []
    for child in node:
        if player == "X":
            scores.append(minimax(child, "O"))
        else:
            scores.append(minimax(child, "X"))
    if player == "X":
        return max(scores)
    else:
        return min(scores)


print(minimax([[1, 0], [-1, 1]], "X"))
```

خروجی `0` است: X می‌داند در هر شاخه O کوچک‌ترین امتیاز را برمی‌گزیند (۰ یا ۱-) و از میان آن‌ها بزرگ‌تر، یعنی ۰، را انتخاب می‌کند.

## چرا همیشه کافی نیست

- کامپیوترها قدرتمندند و می‌توانند نتیجه‌های بسیار زیادی را حساب کنند. اما کامپیوترهای جیبی و رومیزی ما شاید نتوانند **تریلیون‌ها** گزینه را برای درخت‌های پیچیده‌تر بازی حساب کنند. اینجاست که یادگیری ماشین کمک می‌کند.
- از سخنرانی: دوز ۲۵۵٬۱۶۸ بازی ممکن دارد؛ در شطرنج، با در نظر گرفتن فقط چهار جفت حرکت اول حدود ۸۵ میلیارد حالت می‌سازد، و در Go این عدد به حدود ۲۶۶ کوینتیلیون می‌رسد.

## پیوندها

- قبلی: [هوش مصنوعی در بازی‌ها و درخت تصمیم](/kb/d/w71-n04)
- بعدی: [یادگیری ماشین، یادگیری تقویتی و کاوش در برابر بهره‌برداری](/kb/d/w71-n06)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
