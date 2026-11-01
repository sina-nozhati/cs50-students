---
id: w07-n12
type: note
title: حملهٔ تزریق SQL و جای‌نگهدار ? (SQL Injection Attacks)
title_fa: حملهٔ تزریق SQL و جای‌نگهدار ?
title_en: SQL Injection Attacks
week: 7
parent: w07-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: SQL Injection Attacks
official_anchor: sql-injection-attacks
source_url: https://cs50.harvard.edu/x/2026/notes/7/#sql-injection-attacks
source_refs:
- src-notes-7#sql-injection-attacks
- src-transcript-7
- src-sql-box-7
- src-anzali-authored-7
- src-srt-7
concept_ids:
- w07-c-sql-injection
- w07-c-sql-comment
- w07-c-never-trust-input
- w07-c-fstring-sql-danger
prev: w07-n11
next: w07-summary
order: 12
video:
  youtube_id: oqRU2So6Z2Y
  start: '1:59:22'
  start_seconds: 7162
  url: https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=7162s
  origin: inference
  basis: first lecture7.srt cue containing the phrase 'SQL injection attack'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:37+03:30'
verified_at: '2026-10-29T05:22:43+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; SQL and Python code copied exactly from the official notes (fence language sql or python; text for reference listings); results marked «اجراشده روی جعبهٔ ساخت» were run on authored fixture databases (fixtures/*.sql), never on songs.db, movies.db or fiftyville.db; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# حملهٔ تزریق SQL و جای‌نگهدار ?

> **منبع رسمی:** بخش «SQL Injection Attacks» از [درس‌نامهٔ هفتهٔ ۷ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/7/#sql-injection-attacks). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۵۹:۲۲ تا حدود ۲:۰۶:۵۷](https://www.youtube.com/watch?v=oqRU2So6Z2Y&t=7162s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

تزریق SQL یکی از قدیمی‌ترین و پرهزینه‌ترین آسیب‌پذیری‌های نرم‌افزار است و دلیلش فقط یک عادت بد است: چسباندن ورودی کاربر به متن پرس‌وجو. این یادداشت نشان می‌دهد چرا `?` در `favorites.py` آنجاست و از هفتهٔ ۹ در هر پرس‌وجوی وب‌سایتت لازم است.

## حمله‌های تزریق SQL

- حالا، با همان کد بالا، شاید بپرسی علامت‌های `?` چه می‌کنند. یکی از مشکل‌هایی که در کاربردهای واقعی SQL پیش می‌آید **حملهٔ تزریق** (injection attack) نام دارد: حمله‌ای که در آن یک بازیگر بدخواه کد SQL بدخواهانه وارد می‌کند.
- برای نمونه، یک صفحهٔ ورود را در نظر بگیر (درس‌نامه تصویر صفحه‌ای با دو فیلد نام کاربری و گذرواژه نشان می‌دهد؛ پیوند در `media.json`).
- بدون محافظت درست در کد خودمان، بازیگر بدخواه می‌تواند کد بدخواهانه اجرا کند. این را در نظر بگیر:

```python
rows = db.execute("SELECT COUNT(*) FROM users WHERE username = ? AND password = ?", username, password)
```

- دقت کن که چون `?` سر جایش است، پیش از آنکه `username` و `password` کورکورانه در پرس‌وجو پذیرفته شوند، می‌شود روی آن‌ها اعتبارسنجی انجام داد.
- هرگز کورکورانه به ورودی کاربر اعتماد نکن.
- با استفاده از کتابخانهٔ CS50، کتابخانه نویسه‌های احتمالاً بدخواهانه را «پاک‌سازی» (sanitize) و حذف می‌کند.

> [!NOTE]
> **یادداشت**
> درس‌نامه فقط نسخهٔ **امن** (با `?`) را نشان می‌دهد و نسخهٔ ناامن را نمی‌آورد؛ در سخنرانی نسخهٔ ناامن روی اسلاید است (d115). همچنین درس‌نامه می‌گوید کتابخانه نویسه‌های خطرناک را «حذف» می‌کند؛ سخنرانی دقیق‌تر می‌گوید «هر نویسهٔ خطرناکی برایت **گریز** (escape) داده می‌شود». روی جعبهٔ ساخت، کتابخانهٔ cs50 نسخهٔ 9.5.0 ورودی `Hello, It's Me` را بی‌تغییر جست‌وجو کرد و سطر درست را پیدا کرد؛ پس نقل‌قول حذف نشد، بلکه به شکل بخشی از مقدار رفتار شد (d116).

> [!NOTE]
> **از سخنرانی: نقل‌قول و دو خط تیره**
> دیوید صفحهٔ ورود GitHub را مثال می‌زند: اگر کسی نام کاربری‌اش را با یک نقل‌قول تکی و بعد `--` تمام کند، نقل‌قول، رشتهٔ برنامه‌نویس را زودتر می‌بندد و `--` بقیهٔ پرس‌وجو (از جمله بررسی گذرواژه) را به توضیح تبدیل می‌کند. او یادآوری می‌کند که `--` در SQL نشانهٔ توضیح است، مثل `#` در پایتون و `//` در C. سخنرانی با کمیک معروف XKCD دربارهٔ «Bobby Tables کوچولو» تمام می‌شود.

> [!TIP]
> **تألیفی: نمایش امن حمله روی پایگاه دادهٔ نمونه**
> این کد تألیفی و **ناامن** فقط برای فهم حمله است و نباید در برنامه‌ای واقعی نوشته شود:
> ```python
> rows = db.execute(f"SELECT COUNT(*) AS n FROM users WHERE username = '{username}' AND password = '{password}'")
> ```
>
> روی `fixtures/users.sql`، با نام کاربری `malan'--` و هر گذرواژهٔ دلخواه، متن پرس‌وجو به `... WHERE username = 'malan'--' AND password = '...'` تبدیل می‌شود، بررسی گذرواژه به توضیح بدل می‌شود و `n` برابر `1` می‌شود؛ یعنی ورود بدون گذرواژه. همان ورودی در نسخهٔ `?` (کد رسمی بالا) `0` می‌دهد، چون کاربری با نام دقیق `malan'--` وجود ندارد (هر دو اجراشده روی جعبهٔ ساخت با پایگاه دادهٔ ساختگی). گذرواژه‌ها در این پایگاه دادهٔ نمونه فقط برای سادگی متن ساده‌اند؛ برنامهٔ واقعی درهم‌سازی (hash) گذرواژه را ذخیره می‌کند (هفتهٔ ۹).

## اشتباه‌های رایج

- ساختن پرس‌وجو با f-string، `+` یا `%` و ورودی کاربر.
- گذاشتن `?` داخل نقل‌قول (`'?'`)؛ آن وقت `?` یک رشتهٔ معمولی است، نه جای‌نگهدار.
- تلاش برای «پاک کردن» دستی ورودی (مثلاً حذف نقل‌قول‌ها) به جای استفاده از جای‌نگهدار؛ نام‌هایی مثل O'Brien را خراب می‌کند و همهٔ حالت‌ها را نمی‌پوشاند.

## جمع‌بندی

- تزریق SQL یعنی ورودی کاربر بخشی از **کد** SQL شود، نه فقط **داده**.
- `'` رشته را زودتر می‌بندد و `--` بقیهٔ پرس‌وجو را به توضیح تبدیل می‌کند.
- همیشه با `?` و آرگومان جدا پرس‌وجو بساز؛ هرگز به ورودی کاربر کورکورانه اعتماد نکن.

## پیوندها

- قبلی: [شرایط مسابقه و تراکنش](/kb/d/w07-n11)
- بعدی: [خلاصهٔ هفته](/kb/d/w07-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-07/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
