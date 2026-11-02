---
week: 1
lang: fa
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:18+03:30'
verified_at: '2026-10-27T06:27:31+03:30'
generated_at: '2026-10-27T09:00:00+03:30'
review_status: draft-needs-human-review
id: w01-sh-conditional-statements
type: short-summary
title: 'ویدئوی کوتاه: دستورهای شرطی (Conditional Statements)'
title_fa: دستورهای شرطی
title_en: Conditional Statements
parent: w01-fa
source_type: translated-rewritten
origin: mixed
origin_detail: 'Persian summary of the official short (2017 transcript read in full); chapter times from the official .srt (boundaries: inference)'
source_url: https://cs50.harvard.edu/x/shorts/conditional_statements/
source_refs:
- src-short-conditional-statements
- src-anzali-inference-1
concept_ids:
- w01-c-if-else
- w01-c-else-if-chain
- w01-c-switch
- w01-c-ternary
prev: w01-sh-operators
next: w01-sh-loops
order: 24
video:
  youtube_id: 1wsaV5nVC7g
  chapters:
  - start: 0:00
    start_seconds: 0
    title_fa: مقدمه
    evidence_en: null
  - start: 0:26
    start_seconds: 26
    title_fa: یادآوری از Scratch
    evidence_en: from scratch
  - start: '2:00'
    start_seconds: 120
    title_fa: if و else
    evidence_en: Otherwise
  - start: '2:52'
    start_seconds: 172
    title_fa: زنجیرهٔ else if
    evidence_en: mutually exclusive
  - start: '4:14'
    start_seconds: 254
    title_fa: switch
    evidence_en: switch
  - start: '5:16'
    start_seconds: 316
    title_fa: سرریز case
    evidence_en: fall through
  - start: '7:20'
    start_seconds: 440
    title_fa: عملگر سه‌تایی
    evidence_en: ternary operator
  - start: '8:39'
    start_seconds: 519
    title_fa: جمع‌بندی
    evidence_en: If and if-else
  chapters_origin: inference
recorded: '2017'
---

# ویدئوی کوتاه: دستورهای شرطی (Conditional Statements)

> **منبع رسمی:** [صفحهٔ Short «Conditional Statements» در CS50x](https://cs50.harvard.edu/x/shorts/conditional_statements/)، با ارائهٔ Doug Lloyd، ضبط‌شده در ۲۰۱۷ با محیط CS50 IDE. این صفحه خلاصهٔ فارسی ویدئو است، نه ترجمهٔ کامل. همهٔ نکته‌ها **از ویدئوی کوتاه** هستند.

## خلاصه

این ویدئو سه ساختار شرطی C را مقایسه می‌کند: `if` و زنجیره‌های آن، `switch` و عملگر سه‌تایی `?:`.

تمرکز آن بر این است که کدام شاخه‌ها ناسازگارند و کی چند شاخه ممکن است با هم اجرا شوند.

## نکته‌های کلیدی

- بدنهٔ `if` فقط وقتی اجرا می‌شود که عبارت بولی درست باشد؛ `else` برای حالت نادرست است.
- در زنجیرهٔ `if`، `else if`، `else` شاخه‌ها ناسازگارند و فقط یکی اجرا می‌شود.
- اگر چند `if` جدا بنویسی، چند شاخه ممکن است اجرا شوند. `else` همیشه به نزدیک‌ترین `if` تعلق دارد.
- `switch` روی مقدارهای مشخص (`case`) تصمیم می‌گیرد. بعد از هر `case` باید `break` بگذاری؛ وگرنه اجرا به `case` بعدی «سرریز» (fall through) می‌کند.
- گاهی این سرریز عمدی است؛ ویدئو با آن یک شمارش معکوس می‌سازد.
- عملگر سه‌تایی `?:` یک `if`/`else` ساده را در یک خط می‌نویسد: اگر شرط درست بود مقدار اول، وگرنه مقدار دوم.

## فصل‌های ویدئو

> **استنتاج:** زمان شروع فصل‌ها از زیرنویس رسمی (`conditional_statements.srt`) استخراج شده و عنوان فصل‌ها تألیفی است.

- [۰:۰۰ — مقدمه](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=0s)
- [۰:۲۶ — یادآوری از Scratch](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=26s)
- [۲:۰۰ — if و else](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=120s)
- [۲:۵۲ — زنجیرهٔ else if](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=172s)
- [۴:۱۴ — switch](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=254s)
- [۵:۱۶ — سرریز case](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=316s)
- [۷:۲۰ — عملگر سه‌تایی](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=440s)
- [۸:۳۹ — جمع‌بندی](https://www.youtube.com/watch?v=1wsaV5nVC7g&t=519s)

## مفاهیم مرتبط

- if و else در C — [یادداشت](/kb/d/w01-n09) · درس کوتاه `w01-l07` (واحد `w01-l07-u01`)
- زنجیرهٔ else if و شاخه‌های ناسازگار — [یادداشت](/kb/d/w01-n09) · درس کوتاه `w01-l07` (واحد `w01-l07-u02`)
- دستور switch — [یادداشت](/kb/d/w01-sh-conditional-statements) · درس کوتاه `w01-l07` (واحد `w01-l07-u04`)
- عملگر سه‌تایی ?: — [یادداشت](/kb/d/w01-sh-conditional-statements) · درس کوتاه `w01-l07` (واحد `w01-l07-u04`)

## منابع

- [ویدئو در YouTube](https://youtu.be/1wsaV5nVC7g) · [اسلایدها (PDF)](https://cdn.cs50.net/2017/fall/shorts/conditional_statements/conditional_statements.pdf)
- [زیرنویس](https://cdn.cs50.net/2017/fall/shorts/conditional_statements/lang/en/conditional_statements.srt) · [متن گفتار](https://cdn.cs50.net/2017/fall/shorts/conditional_statements/lang/en/conditional_statements.txt)

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
