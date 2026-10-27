---
id: w00-n12
type: note
title: 'سلام به تو: ورودی، متغیر و مقدار بازگشتی (Hello, You)'
title_fa: 'سلام به تو: ورودی، متغیر و مقدار بازگشتی'
title_en: Hello, You
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Hello, You
official_anchor: hello-you
source_url: https://cs50.harvard.edu/x/notes/0/#hello-you
source_refs:
- src-notes-0#hello-you
- src-transcript-0
- src-src0-zip
concept_ids:
- w00-c-variable
- w00-c-return-value
- w00-c-string-join
prev: w00-n11
next: w00-n13
order: 12
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# سلام به تو: ورودی، متغیر و مقدار بازگشتی

> **منبع رسمی:** بخش «Hello, You» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#hello-you). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

برنامه‌ای که همیشه یک چیز می‌گوید جالب نیست. این بخش برنامه را **تعاملی** می‌کند و سه ایدهٔ مهم را نشان می‌دهد: **متغیر** (variable)، **مقدار بازگشتی** (return value) و **تودرتو کردن تابع‌ها** (nesting).

## برنامه (عیناً مطابق درس‌نامه)

```text
when green flag clicked
ask [What's your name?] and wait
say (join [hello,] (answer))
```

## توضیح درس‌نامه به فارسی

- با کلیک روی پرچم سبز، تابع `ask` اجرا می‌شود. برنامه از تو، یعنی کاربر، می‌پرسد `What's your name?`.
- سپس نام را در **متغیری** به نام `answer` ذخیره می‌کند.
- بعد `answer` را به تابع ویژه‌ای به نام `join` می‌دهد که دو **رشته** (string) متن را به هم می‌چسباند: `hello,` و نامی که وارد شده است. مقدار `answer` به‌عنوان **آرگومان** به `join` داده می‌شود.
- حاصل این‌ها با هم به تابع `say` داده می‌شود. گربه «hello,» و نام را می‌گوید. برنامه حالا تعاملی است.

![scratch as algorithm](https://cs50.harvard.edu/x/notes/0/cs50Week0Slide169.png "hello and answer provided to join to get hello david")

طبق درس‌نامه، ورودی‌های `hello,` و `answer` به `join` داده می‌شوند و `join` مقدار `hello, David` را **برمی‌گرداند** (return). این مقدار بازگشتی به `say` داده می‌شود و `say` **اثر جانبی** سخن گفتن گربه را ایجاد می‌کند.

## نسخهٔ گویا با speak (عیناً مطابق درس‌نامه)

```text
when green flag clicked
ask [What's your name?] and wait
speak (join [hello,] (answer))
```

همان متغیر، همراه با `hello`، به تابعی به نام `speak` داده می‌شود. **از سخنرانی:** `speak` از افزونهٔ (extension) **Text to Speech** است و با بلوک «set voice to» می‌شود صدا را عوض کرد (مثلاً kitten یا giant).

## مقدار بازگشتی در برابر اثر جانبی (از سخنرانی)

| | اثر جانبی (side effect) | مقدار بازگشتی (return value) |
| --- | --- | --- |
| چه کسی می‌بیند؟ | انسان (روی صفحه یا از بلندگو) | فقط کد |
| مثال | حباب `say` | `answer` از `ask`؛ حاصل `join` |
| کاربرد | نمایش نتیجه | ورودیِ تابعی دیگر |

## اشکال‌زدایی در سخنرانی (درس مهم)

در سخنرانی، نسخهٔ اول برنامه دو بلوک `say` جدا داشت: یکی «hello,» و دیگری `answer`. نتیجه این بود که فقط نام دیده می‌شد. علت: هر دو بلوک اجرا می‌شدند، اما آن‌قدر سریع که «hello,» دیده نمی‌شد. اول با `wait` حل شد، بعد بهتر با **`join`**. بعد از آن، یک اشکال ظاهری هم پیدا شد: **فاصله** بعد از ویرگول جا افتاده بود (`hello,David`). با افزودن فاصله در رشتهٔ `hello, ` درست شد.

## خروجی مورد انتظار

اگر کاربر `David` تایپ کند، گربه می‌گوید `hello, David`. اگر فاصلهٔ بعد از ویرگول در رشته نباشد، خروجی `hello,David` می‌شود.

## مثال تألیفی

```text
when green flag clicked
ask [Which city are you from?] and wait
say (join [I love ] (answer)) for (3) seconds
```

اگر پاسخ `Anzali` باشد، خروجی `I love Anzali` است. دقت کن فاصلهٔ بعد از `love` جزء رشته است.

## اشتباه‌های رایج

- استفاده از دو بلوک `say` پشت سر هم و انتظار دیدن هر دو پیام.
- فراموش کردن فاصله در رشته هنگام `join`.
- اینکه فکر کنی `answer` را خودت باید بسازی. در Scratch، `ask` آن را خودکار پر می‌کند. متغیرهای دلخواه را بعداً خودت می‌سازی (Oscartime را ببین).

## محدودیت‌ها

`answer` همیشه آخرین پاسخ را نگه می‌دارد. اگر دوباره `ask` کنی، مقدار قبلی جایگزین می‌شود. این رفتار پیش‌فرض Scratch است و درس‌نامه جزئیاتش را بیشتر از این باز نمی‌کند.

## جمع‌بندی

- `ask` پاسخ کاربر را در متغیر `answer` می‌گذارد؛ این **مقدار بازگشتی** است.
- `join` دو رشته را می‌چسباند و حاصل را برمی‌گرداند.
- خروجیِ یک تابع می‌تواند ورودیِ تابع دیگر باشد (تودرتو).

## سؤال‌های خودآزمایی

1. `answer` از کجا مقدار می‌گیرد؟
2. خروجی `join` اثر جانبی است یا مقدار بازگشتی؟
3. چرا دو بلوک `say` پشت سر هم مشکل ایجاد کرد؟
4. اگر رشتهٔ اول `hello,` (بدون فاصله) باشد و کاربر `Sara` وارد کند، گربه چه می‌گوید؟

**پاسخ کوتاه:** ۱) از تابع `ask`. ۲) مقدار بازگشتی. ۳) اولی آن‌قدر سریع جایش را به دومی داد که دیده نشد. ۴) `hello,Sara`.

## پیوندها

- قبلی: [سلام دنیا: رویداد، تابع، آرگومان و اثر جانبی](/kb/d/w00-n11)
- بعدی: [میو: حلقه، بلوک سفارشی و انتزاع](/kb/d/w00-n13)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
