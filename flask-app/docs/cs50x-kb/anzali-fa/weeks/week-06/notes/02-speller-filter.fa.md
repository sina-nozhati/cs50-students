---
id: w06-n02
type: note
title: 'Speller و Filter در پایتون: چرا زبان سطح بالا (Speller and Filter)'
title_fa: 'Speller و Filter در پایتون: چرا زبان سطح بالا'
title_en: Speller and Filter
week: 6
parent: w06-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Speller
official_anchor: speller
source_url: https://cs50.harvard.edu/x/2026/notes/6/#speller
source_refs:
- src-notes-6#speller
- src-notes-6#filter
- src-transcript-6
- src-pset-6
- src-anzali-authored-6
- src-srt-6
concept_ids:
- w06-c-high-level-tradeoff
- w06-c-set
prev: w06-n01
next: w06-n03
order: 2
video:
  youtube_id: Rl0ludWTLxs
  start: '7:02'
  start_seconds: 422
  url: https://www.youtube.com/watch?v=Rl0ludWTLxs&t=422s
  origin: inference
  basis: first lecture6.srt cue containing the phrase 'implemented in advance a speller'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:34+03:30'
verified_at: '2026-10-29T04:00:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Python and C code copied exactly from the official notes (fence language python or c; text for reference listings); authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# Speller و Filter در پایتون: چرا زبان سطح بالا

> **منبع رسمی:** بخش «Speller» از [درس‌نامهٔ هفتهٔ ۶ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/6/#speller). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۷:۰۲ تا حدود ۱۷:۵۱](https://www.youtube.com/watch?v=Rl0ludWTLxs&t=422s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

دو برنامه‌ای که در هفته‌های ۴ و ۵ با زحمت در C نوشتی (Speller و Filter) در پایتون چند سطر بیشتر نیستند. این یادداشت نشان می‌دهد زبان‌های سطح بالا **چرا** وجود دارند و چه بهایی دارند.

## Speller

- برای نشان دادن این سادگی، فایلی به نام `dictionary.py` بساز و کد زیر را بنویس:

```python
# Words in dictionary
words = set()

def check(word):
    """Return true if word is in dictionary else false"""
    return word.lower() in words

def load(dictionary):
    """Load dictionary into memory, returning true if successful else false"""
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    """Returns number of words in dictionary if loaded else 0 if not yet loaded"""
    return len(words)

def unload():
    """Unloads dictionary from memory, returning true if successful else false"""
    return True
```

- چهار تابع داریم. در `check` اگر `word` (با حروف کوچک) در `words` باشد، `True` برمی‌گردد. در `load` فایل واژه‌نامه باز می‌شود و همهٔ سطرهایش به مجموعهٔ `words` اضافه می‌شوند. `size` فقط طول (`len`) مجموعه را برمی‌گرداند. `unload` فقط باید `True` برگرداند، چون پایتون مدیریت حافظه را خودش انجام می‌دهد.
- `words` یک **مجموعه** (`set`) است: مجموعه‌ای از مقدارهای یکتا که می‌شود به‌سرعت پرسید آیا مقداری در آن هست یا نه.

> [!NOTE]
> **یادداشت**
> متن درس‌نامه می‌گوید «برای هر سطر فایل، آن سطر را به `words` اضافه می‌کنیم و با `rstrip` سطر تازهٔ انتهایی را حذف می‌کنیم»، اما کدِ همان بخش حلقه و `rstrip` ندارد و از `file.read().splitlines()` استفاده می‌کند؛ `splitlines` خودش نویسه‌های سطر تازه را کنار می‌گذارد (d99). این صفحه کد را همان‌طور که هست توضیح می‌دهد.

- این کد نشان می‌دهد چرا زبان‌های سطح بالا وجود دارند: ساده‌تر کردن کار و نوشتن آسان‌تر کد.
- اما **سرعت** بهای این سادگی است. چون C به تو اجازه می‌دهد دربارهٔ مدیریت حافظه تصمیم بگیری، ممکن است (بسته به کدت) سریع‌تر از پایتون اجرا شود. C فقط سطرهای کد تو را اجرا می‌کند، اما پایتون وقتی تابع‌های داخلی‌اش را صدا می‌زنی، همهٔ کدی را هم که زیر پوسته همراه آن‌هاست اجرا می‌کند.

> [!TIP]
> **از سخنرانی: پیوند با هفتهٔ ۵**
> David گفت مجموعه‌ای که پایتون فراهم می‌کند در عمل همان کاری را می‌کند که در Problem Set 5 خودت با یک جدول درهم‌سازی پیاده کردی. یعنی ساختمان داده هنوز هست؛ فقط کس دیگری آن را برایت نوشته است.

## Filter

- برای نشان دادن بیشتر این سادگی، فایل `blur.py` را بساز:

```python
# Blurs an image

from PIL import Image, ImageFilter

# Blur image
before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")
```

- این برنامه `Image` و `ImageFilter` را از کتابخانه‌ای به نام `PIL` وارد (import) می‌کند. یک فایل ورودی می‌گیرد و یک فایل خروجی می‌سازد.
- با تغییری کوچک، برنامهٔ `edges.py` نتیجه‌ای کاملاً متفاوت (پیدا کردن لبه‌ها) می‌دهد:

```python
# Blurs an image

from PIL import Image, ImageFilter

# Find edges
before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")
```

> [!NOTE]
> **یادداشت**
> توضیح ابتدای فایل رسمی `edges.py` هنوز `# Blurs an image` است، در حالی که برنامه لبه‌ها را پیدا می‌کند (`ImageFilter.FIND_EDGES`). کد عیناً آمده و این ناهمخوانی ثبت شده است (d100).

- پایتون به تو اجازه می‌دهد کارهایی را که در C و زبان‌های **سطح پایین‌تر** بسیار پیچیده‌تر بود، پشت انتزاع پنهان کنی.
- یکی از بهاهای استفاده از پایتون این است که زبانی تفسیری است، نه کامپایلی؛ برای همین معمولاً کمی (اغلب بسیار کم) کندتر از برنامهٔ کامپایل‌شده است.

## اشتباه‌های رایج

- این برداشت که «پایتون همیشه کند است»؛ درس‌نامه می‌گوید C **ممکن است** سریع‌تر باشد، بسته به کد.
- اجرای `blur.py` بدون فایل `bridge.bmp` یا بدون نصب بودن `PIL`؛ این برنامه‌ها فایل و کتابخانه لازم دارند.

## جمع‌بندی

- Speller در پایتون با یک `set` و چند سطر نوشته می‌شود؛ حافظه را پایتون مدیریت می‌کند.
- Filter با کتابخانهٔ `PIL` چند سطر است.
- بها: سرعت اجرای احتمالاً کمتر و کنترل کمتر روی حافظه.

## پیوندها

- قبلی: [سلام پایتون: زبان تفسیری](/kb/d/w06-n01)
- بعدی: [تابع، کتابخانه، ماژول و بسته](/kb/d/w06-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-06/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
