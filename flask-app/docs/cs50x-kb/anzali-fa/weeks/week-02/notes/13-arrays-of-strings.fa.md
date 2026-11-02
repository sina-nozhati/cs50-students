---
id: w02-n13
type: note
title: 'آرایه‌ای از رشته‌ها (Strings: arrays of strings)'
title_fa: آرایه‌ای از رشته‌ها
title_en: 'Strings: arrays of strings'
week: 2
parent: w02-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Strings
official_anchor: strings
source_url: https://cs50.harvard.edu/x/2026/notes/2/#strings
source_refs:
- src-notes-2#strings
- src-anzali-authored-2
- src-srt-2
concept_ids:
- w02-c-array-of-strings
prev: w02-n12
next: w02-n14
order: 13
video:
  youtube_id: h5Gc1n8ZuU8
  start: '1:42:22'
  start_seconds: 6142
  url: https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=6142s
  origin: inference
  basis: first lecture2.srt cue containing the phrase 'words'
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:21+03:30'
verified_at: '2026-10-28T01:38:59+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; C code copied exactly from the official notes; authored material is marked تألیفی; transcript-only facts are marked «از سخنرانی».
---

# آرایه‌ای از رشته‌ها

> **منبع رسمی:** بخش «Strings» از [درس‌نامهٔ هفتهٔ ۲ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/2/#strings). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۱:۴۲:۲۲ تا حدود ۱:۴۸:۱۵](https://www.youtube.com/watch?v=h5Gc1n8ZuU8&t=6142s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اگر رشته خودش آرایه است، آرایه‌ای از رشته‌ها چه؟ این همان ساختاری است که در پایان هفته در `argv` دوباره می‌بینی.

## دو رشته در یک آرایه

```c
// Array of strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string words[2];

    words[0] = "HI!";
    words[1] = "BYE!";

    printf("%s\n", words[0]);
    printf("%s\n", words[1]);
}
```

- هر دو رشته در **یک** آرایه از نوع `string` نگه داشته شده‌اند.
- آرایه‌ای به نام `words` ساخته شده است؛ آرایه‌ای از رشته‌ها. هر واژه در یکی از خانه‌های `words` است.

## اندیس روی اندیس

درس‌نامه دو رشته را در یک آرایه از رشته‌ها یکی می‌کند و بعد نشان می‌دهد که می‌شود به تک‌تک نویسه‌های هر واژه هم رسید:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string words[2];

    words[0] = "HI!";
    words[1] = "BYE!";

    printf("%c%c%c\n", words[0][0], words[0][1], words[0][2]);
    printf("%c%c%c%c\n", words[1][0], words[1][1], words[1][2], words[1][3]);
}
```

- `words[0]` رشتهٔ `"HI!"` است، پس `words[0][0]` نخستین نویسهٔ آن یعنی `'H'` است.
- `words[1][3]` چهارمین نویسهٔ `"BYE!"` است، یعنی `'!'`.
- **تألیفی:** دو جفت کروشه یعنی اول یک رشته را از آرایه برمی‌داری و بعد یک نویسه را از همان رشته.

## اشتباه‌های رایج

- جابه‌جا کردن ترتیب اندیس‌ها: اولی شمارهٔ رشته است، دومی شمارهٔ نویسه.
- خواندن `words[1][4]`: این خانه NUL رشتهٔ `"BYE!"` است، نه یک حرف.

## جمع‌بندی

- `string words[2]` آرایه‌ای از دو رشته است.
- `words[i][j]` یعنی نویسهٔ j از رشتهٔ i.

## پیوندها

- قبلی: [رشته، آرایه‌ای از نویسه‌ها و NUL](/kb/d/w02-n12)
- بعدی: [طول رشته و strlen](/kb/d/w02-n14)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-02/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
