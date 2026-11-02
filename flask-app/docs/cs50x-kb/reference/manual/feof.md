---
id: manual-feof
type: reference
title: feof(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/feof
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:59+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- feof
- manual
checksum: sha256:8ac0651e99b589610dfbe3dd48ba5ade79e3707dd50609d5278b413345026f8a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# feof(3) — CS50 manual page

## 1. Source metadata
- **Title:** feof(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/feof>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:59+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/feof> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/feof#name)

clearerr, feof, ferror - check and reset stream status

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/feof#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/feof#synopsis)

```
#include <stdio.h>
void clearerr(FILE *stream);
int feof(FILE *stream);
int ferror(FILE *stream);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/feof#description)

The function [clearerr](https://manual.cs50.io/3/clearerr)() clears the end-of-file and
error indicators for the stream pointed to by `stream`.

The function [feof](https://manual.cs50.io/3/feof)() tests the end-of-file indicator
for the stream pointed to by `stream`, returning nonzero if it is
set. The end-of-file indicator can be cleared only by the function
[clearerr](https://manual.cs50.io/3/clearerr)().

The function [ferror](https://manual.cs50.io/3/ferror)() tests the error indicator for
the stream pointed to by `stream`, returning nonzero if it is
set. The error indicator can be reset only by the
[clearerr](https://manual.cs50.io/3/clearerr)() function.

For nonlocking counterparts, see
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3).

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/feof#return-value)

The [feof](https://manual.cs50.io/3/feof)() function returns nonzero if the
end-of-file indicator is set for `stream`; otherwise, it returns
zero.

The [ferror](https://manual.cs50.io/3/ferror)() function returns nonzero if the error
indicator is set for `stream`; otherwise, it returns zero.

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/feof#errors)

These functions should not fail and do not set `errno`.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/feof#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [clearerr](https://manual.cs50.io/3/clearerr)(), [feof](https://manual.cs50.io/3/feof)(), [ferror](https://manual.cs50.io/3/ferror)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/feof#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/feof#history)

C89, POSIX.1-2001.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/feof#notes)

POSIX.1-2008 specifies that these functions shall not change the
value of `errno` if `stream` is valid.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/feof#caveats)

Normally, programs should read the return value of an input function,
such as [fgetc](https://manual.cs50.io/3/fgetc)(3), before using functions of the
[feof](https://manual.cs50.io/3/feof)(3) family. Only when the function returned the
sentinel value **EOF** it makes sense to distinguish
between the end of a file or an error with [feof](https://manual.cs50.io/3/feof)(3) or
[ferror](https://manual.cs50.io/3/ferror)(3).

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/feof#see-also)

[open](https://manual.cs50.io/2/open)(2), [fdopen](https://manual.cs50.io/3/fdopen)(3),
[fileno](https://manual.cs50.io/3/fileno)(3), [stdio](https://manual.cs50.io/3/stdio)(3),
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 Manual Pages (selected)](README.md) (`reference-manual`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
مرجع فنی رسمی؛ دستیار هوش مصنوعی باید برای توضیح توابع و قواعد سبک به این سند استناد کند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.


### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://manual.cs50.io/3/feof — retrieved 2026-10-18T05:45:59+03:30, sha256 `8ac0651e99b58961…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
