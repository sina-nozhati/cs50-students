---
id: w05-n10
type: note
title: درخت‌ها و درخت جست‌وجوی دودویی (Trees)
title_fa: درخت‌ها و درخت جست‌وجوی دودویی
title_en: Trees
week: 5
parent: w05-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Trees
official_anchor: trees
source_url: https://cs50.harvard.edu/x/2026/notes/5/#trees
source_refs:
- src-notes-5#trees
- src-transcript-5
- src-anzali-inference-5
- src-srt-5
concept_ids:
- w05-c-tree
- w05-c-bst
- w05-c-bst-search
- w05-c-balanced-tree
prev: w05-n09
next: w05-n11
order: 10
video:
  youtube_id: PmAI76OGE_E
  start: '1:22:17'
  start_seconds: 4937
  url: https://www.youtube.com/watch?v=PmAI76OGE_E&t=4937s
  origin: inference
  basis: first lecture5.srt cue containing the phrase 'And so I give you trees'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:31+03:30'
verified_at: '2026-10-28T18:42:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code and pseudocode copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# درخت‌ها و درخت جست‌وجوی دودویی

> **منبع رسمی:** بخش «Trees» از [درس‌نامهٔ هفتهٔ ۵ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/5/#trees). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۲۲:۱۷ تا حدود ۱:۳۷:۰۳](https://www.youtube.com/watch?v=PmAI76OGE_E&t=4937s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

درخت جست‌وجوی دودویی ترکیبی از سرعت آرایه و پویایی فهرست پیوندی است. اینجا دوباره به جست‌وجوی دودویی و بازگشت برمی‌گردی، این بار روی ساختاری دوبعدی.

## درخت‌ها

- آرایه‌ها حافظهٔ پیوسته‌ای دارند که می‌شود سریع جست‌وجویش کرد، و امکان جست‌وجوی دودویی را می‌دهند.
- آیا می‌شود بهترین ویژگی‌های آرایه و فهرست پیوندی را با هم داشت؟
- **درخت‌های جست‌وجوی دودویی** (binary search trees) ساختمان دادهٔ دیگری‌اند که می‌شود با آن‌ها داده را کارآمدتر نگه داشت تا جست‌وجو و بازیابی شود.
- یک دنبالهٔ مرتب از عددها را تصور کن، مثلاً `1` تا `7`.
- حالا تصور کن مقدار وسط بالای یک درخت قرار بگیرد. مقدارهای کوچک‌تر از آن به چپ و مقدارهای بزرگ‌تر به راست می‌روند.
- سپس با اشاره‌گرها هر ناحیهٔ حافظه را به جای درستش وصل می‌کنیم تا همهٔ گره‌ها به هم متصل شوند.

> [!WARNING]
> **هشدار**
> متن جایگزین (alt) تصویرهای این بخش در درس‌نامه می‌گوید زیر `4` عددهای `3` و `5` هستند. در خود چیدمان، و در سخنرانی، فرزندان `4` عددهای `2` و `6`اند و برگ‌ها `1`، `3`، `5` و `7`. این تفاوت در `sources.json` ثبت شده است.

- در کد، جست‌وجوی چنین درختی را می‌شود این‌طور پیاده کرد:

```c
bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        return search(tree->right, number);
    }
    else if (number == tree->number)
    {
        return true;
    }
}
```

- این تابع درخت را **بازگشتی** جست‌وجو می‌کند. اگر عدد مورد نظر از عدد گرهٔ فعلی کوچک‌تر باشد، زیردرخت چپ را می‌گردد؛ اگر بزرگ‌تر باشد، زیردرخت راست را. این رویکرد بازگشتی، وقتی درخت **متوازن** است، جست‌وجویی با پیچیدگی O(log n) می‌دهد.
- درخت پویایی‌ای دارد که آرایه ندارد: می‌تواند هر طور بخواهیم بزرگ و کوچک شود.
- همچنین این ساختار، وقتی درخت متوازن است، زمان جست‌وجوی O(log n) می‌دهد.

> [!NOTE]
> **یادداشت**
> این کد یک قطعه است: باید پیش از آن `stdbool.h` آمده باشد و `node`ی با فیلدهای `number`، `left` و `right` تعریف شده باشد. ما برای آزمودن، آن را درون چنین تعریفی کامپایل کردیم. با `-Wall -Werror`، کامپایلر خطای `control reaches end of non-void function` می‌دهد، چون پس از آخرین `else if` هیچ `return`ی نیست. منطقاً یکی از چهار شاخه همیشه اجرا می‌شود، اما کامپایلر این را نمی‌داند. سخنرانی خودش پیشنهاد کرد شرط آخر را به `else` ساده تبدیل کنی. این مورد در `sources.json` ثبت شده است.

## سخنرانی چه می‌گوید

- **از سخنرانی:** David درخت را با شجره‌نامهٔ خانوادگی مقایسه کرد: بالای آن **ریشه** (root) است و گره‌های بی‌فرزند **برگ** (leaf) نام دارند. درخت اولین ساختار **دوبعدی** این هفته است.
- **از سخنرانی:** ویژگی کلیدی: هر گره از فرزند چپش بزرگ‌تر و از فرزند راستش کوچک‌تر است (اگر مقدار تکراری نداشته باشیم)، و این ویژگی **بازگشتی** است: برای هر زیردرخت هم برقرار است.
- **از سخنرانی:** برای یافتن `5` از ریشهٔ `4` به راست و از `6` به چپ می‌رویم؛ هر قدم مثل نصف کردن دفترچهٔ تلفن است. ارتفاع درخت حدود log₂ n است.
- **از سخنرانی:** هزینه: هر گره یک عدد و **دو** اشاره‌گر دارد؛ David گفت این تقریباً سه برابر حافظهٔ آرایه است، «حدود ۱۶ یا ۲۰ بایت» به‌جای ۴ بایت.
- **از سخنرانی:** اگر عددها به ترتیب بد وارد شوند، مثلاً `1`، `2`، `3`، درخت به یک فهرست پیوندی بلند و باریک تبدیل می‌شود و جست‌وجو دوباره O(n) می‌شود. الگوریتم‌هایی هستند که با هر درج یا حذف درخت را دوباره **متوازن** می‌کنند (مثلاً `2` را ریشه می‌کنند)، اما این هفته آن‌ها را در کد نمی‌نویسیم.

> [!NOTE]
> **یادداشت**
> روی سامانه‌های ۶۴ بیتی رایج، گره‌ای با یک `int` و دو اشاره‌گر به‌خاطر پُرکننده معمولاً ۲۴ بایت است، نه ۱۶ یا ۲۰. این برداشت تحریریهٔ CS50x انزلی است (استنتاجی).

## اشتباه‌های رایج

- فکر کردن به اینکه هر درخت دودویی خودبه‌خود O(log n) است؛ فقط درخت **متوازن** چنین است.
- فراموش کردن حالت پایه `tree == NULL` در تابع بازگشتی.
- انتظار اینکه کامپایلر بفهمد زنجیرهٔ `else if` همهٔ حالت‌ها را پوشش می‌دهد.

## جمع‌بندی

- درخت جست‌وجوی دودویی: چپ کوچک‌تر، راست بزرگ‌تر، به‌صورت بازگشتی.
- جست‌وجو در درخت متوازن O(log n) است؛ در بدترین حالتِ نامتوازن O(n).
- بهای این سرعت و پویایی، دو اشاره‌گر برای هر گره است.

## پیوندها

- قبلی: [افزودن به انتها، درج مرتب و آزادسازی](/kb/d/w05-n09)
- بعدی: [درهم‌سازی و جدول درهم‌سازی](/kb/d/w05-n11)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-05/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
