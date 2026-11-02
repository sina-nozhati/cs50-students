---
id: w02-n18
type: note
title: 'رمزنگاری: متن ساده، کلید و متن رمز (از سخنرانی) (Cryptography (lecture transcript))'
title_fa: 'رمزنگاری: متن ساده، کلید و متن رمز (از سخنرانی)'
title_en: Cryptography (lecture transcript)
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Cryptography (week page topic; lecture transcript)
official_anchor: lecture-2
source_url: https://cdn.cs50.net/2025/fall/lectures/2/lang/en/lecture2.txt
source_refs:
- src-transcript-2
- src-week-2
- src-pset-2
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-cryptography
- w02-c-cipher-key
- w02-c-rotation-cipher
prev: w02-n17
next: w02-summary
order: 18
video:
  youtube_id: h5Gc1n8ZuU8
  start: '2:20:23'
  start_seconds: 8423
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=8423s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'cryptography'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# رمزنگاری: متن ساده، کلید و متن رمز (از سخنرانی)

> **منبع رسمی:** [رونوشت رسمی سخنرانی ۲](https://cdn.cs50.net/2025/fall/lectures/2/lang/en/lecture2.txt) و فهرست موضوع‌های [صفحهٔ هفتهٔ ۲](https://cs50.harvard.edu/x/2026/weeks/2/). درس‌نامه این بخش را ندارد. این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۲:۲۰:۲۳](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=8423s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

فهرست موضوع‌های صفحهٔ هفتهٔ ۲ با **رمزنگاری** (`cryptography`) تمام می‌شود و سخنرانی هم با آن به پایان می‌رسد. پرابلم‌ست ۲ از تو می‌خواهد یکی از دو رمز Caesar یا Substitution را پیاده کنی. این یادداشت پایهٔ مفهومی آن‌هاست.

> **توجه:** درس‌نامهٔ رسمی ۲۰۲۶ بخشی به نام Cryptography **ندارد**. همهٔ مطالب این یادداشت از رونوشت رسمی سخنرانی (`lecture2.txt`) گرفته شده‌اند و برچسب **از سخنرانی** دارند (ناهمخوانی d24).

## مدل ذهنی

**از سخنرانی:**

- رمزنگاری هنر به‌هم‌ریختن اطلاعات برای ارتباط امن است: گذرواژه‌ها، شمارهٔ کارت اعتباری، پیام‌های شخصی.
- ورودی **متن ساده** (`plaintext`) است، نسخهٔ قابل خواندن برای انسان. خروجی **متن رمز** (`ciphertext`) است.
- درون «جعبهٔ سیاه» یک **رمز** (`cipher`) هست: الگوریتمی که اطلاعات را رمز می‌کند.
- اما الگوریتم به‌تنهایی کافی نیست. فرستنده و گیرنده باید از پیش یک راز مشترک داشته باشند: **کلید** (`key`).

> **تألیفی:** نمودار ساده‌شدهٔ این بسته از گفته‌های سخنرانی.

```text
plaintext  +  key  ->  [ cipher ]  ->  ciphertext
```

## رمز چرخشی

**از سخنرانی:**

- اگر کلید `1` باشد، هر حرف یک جا جلو می‌رود: A به B، B به C و Z دوباره به A برمی‌گردد.
- با کلید `1`، متن `HI!` به `IJ!` تبدیل می‌شود. در این رمز ساده نشانه‌گذاری (مثل `!`) دست نمی‌خورد.
- **رمزگشایی** یعنی همان کلید، اما با **کم کردن**: B به A و A به Z.
- **ROT13** با کلید ۱۳ سال‌ها در اینترنت برای پنهان کردن «اسپویل» به کار رفته است؛ با آن `HI` به `UV` تبدیل می‌شود.
- **ROT26** امن‌تر نیست: ۲۶ جا چرخیدن یعنی هر حرف به خودش برمی‌گردد.

## چرا این رمز امن نیست

**از سخنرانی:**

- مهاجم (مثل معلمی که یادداشت دو دانش‌آموز را می‌گیرد) کافی است همهٔ کلیدها را بیازماید: ۱، ۲، ۳ تا ۲۵. این روش را **آزمودن همهٔ حالت‌ها** (`brute force`) می‌نامند.
- این رمز در تاریخ به نام **رمز سزار** شناخته می‌شود، چون سزار با آن با سردارانش پیام ردوبدل می‌کرد. اگر هیچ‌کس دیگری روش را نشناسد، همین کافی بود؛ امروز چند خط کد کافی است تا آن را بشکنی.
- الگوریتم‌های امروزی بسیار پیچیده‌ترند.
- David سخنرانی را با یک پیام رمزشده تمام کرد که با چرخش معکوس یک‌جایی خوانده می‌شود: «this was CS50».

## پیوند با این هفته

> **تألیفی:** برای پیاده کردن چنین رمزی، همهٔ ابزارهای این هفته لازم است: رشته به‌عنوان آرایه (`s[i]`)، حساب ASCII، `isupper` و `islower` از `ctype.h`، آرگومان خط فرمان برای گرفتن کلید، و `return 1` برای ورودی نادرست. راه‌حل در این بسته نیست؛ [راهنمای Caesar](/kb/d/w02-ps-caesar) و [راهنمای Substitution](/kb/d/w02-ps-substitution) فقط الزامات و سرنخ‌های مفهومی دارند.

## اشتباه‌های رایج

- فراموش کردن «دور زدن» از Z به A.
- تغییر دادن نشانه‌گذاری و فاصله‌ها.
- تصور این‌که کلید بزرگ‌تر یعنی امنیت بیشتر؛ ROT26 هیچ تغییری نمی‌دهد.

## جمع‌بندی

- متن ساده + کلید، از راه یک رمز، متن رمز می‌شود.
- رمز سزار با ۲۵ کلید ممکن، با آزمودن همه به‌سادگی شکسته می‌شود.

## پیوندها

- قبلی: [وضعیت خروج](/kb/d/w02-n17)
- بعدی: [خلاصهٔ هفته](/kb/d/w02-summary)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
