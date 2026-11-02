---
id: manual-fgetc
type: reference
title: fgetc(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/fgetc
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:55+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- fgetc
- manual
checksum: sha256:4c7eb4fc4a120c8f6d549eb720f3c2706dd0659ec416d4cacd5bf9c9a693022f
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# fgetc(3) — CS50 manual page

## 1. Source metadata
- **Title:** fgetc(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/fgetc>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:55+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/fgetc> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/fgetc#name)

fgetc, fgets, getc, getchar, ungetc - input of characters and
strings

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/fgetc#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/fgetc#synopsis)

```
#include <stdio.h>
int fgetc(FILE *stream);
int getc(FILE *stream);
int getchar(void);
char *fgets(char s[restrict .size], int size, FILE *restrict stream);
int ungetc(int c, FILE *stream);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/fgetc#description)

[fgetc](https://manual.cs50.io/3/fgetc)() reads the next character from
`stream` and returns it as an `unsigned char` cast to an
`int`, or **EOF** on end of file or error.

[getc](https://manual.cs50.io/3/getc)() is equivalent to [fgetc](https://manual.cs50.io/3/fgetc)()
except that it may be implemented as a macro which evaluates
`stream` more than once.

[getchar](https://manual.cs50.io/3/getchar)() is equivalent to
**[getc](https://manual.cs50.io/3/getc)(**`stdin`**)**`.`

[fgets](https://manual.cs50.io/3/fgets)() reads in at most one less than `size`
characters from `stream` and stores them into the buffer pointed
to by `s`. Reading stops after an **EOF** or a
newline. If a newline is read, it is stored into the buffer. A
terminating null byte ('\0') is stored after the last character in the
buffer.

[ungetc](https://manual.cs50.io/3/ungetc)() pushes `c` back to `stream`,
cast to `unsigned char`, where it is available for subsequent
read operations. Pushed-back characters will be returned in reverse
order; only one pushback is guaranteed.

Calls to the functions described here can be mixed with each other
and with calls to other input functions from the `stdio` library
for the same input stream.

For nonlocking counterparts, see
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3).

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/fgetc#return-value)

[fgetc](https://manual.cs50.io/3/fgetc)(), [getc](https://manual.cs50.io/3/getc)(), and
[getchar](https://manual.cs50.io/3/getchar)() return the character read as an *unsigned
char* cast to an `int` or **EOF** on end of file
or error.

[fgets](https://manual.cs50.io/3/fgets)() returns `s` on success, and NULL on
error or when end of file occurs while no characters have been read.

[ungetc](https://manual.cs50.io/3/ungetc)() returns `c` on success, or
**EOF** on error.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/fgetc#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [fgetc](https://manual.cs50.io/3/fgetc)(), [fgets](https://manual.cs50.io/3/fgets)(), [getc](https://manual.cs50.io/3/getc)(), [getchar](https://manual.cs50.io/3/getchar)(), [ungetc](https://manual.cs50.io/3/ungetc)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/fgetc#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/fgetc#history)

POSIX.1-2001, C89.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/fgetc#notes)

It is not advisable to mix calls to input functions from the
`stdio` library with low-level calls to [read](https://manual.cs50.io/2/read)(2)
for the file descriptor associated with the input stream; the results
will be undefined and very probably not what you want.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/fgetc#see-also)

[read](https://manual.cs50.io/2/read)(2), [write](https://manual.cs50.io/2/write)(2),
[ferror](https://manual.cs50.io/3/ferror)(3), [fgetwc](https://manual.cs50.io/3/fgetwc)(3),
[fgetws](https://manual.cs50.io/3/fgetws)(3), [fopen](https://manual.cs50.io/3/fopen)(3),
[fread](https://manual.cs50.io/3/fread)(3), [fseek](https://manual.cs50.io/3/fseek)(3),
[getline](https://manual.cs50.io/3/getline)(3), [gets](https://manual.cs50.io/3/gets)(3),
[getwchar](https://manual.cs50.io/3/getwchar)(3), [puts](https://manual.cs50.io/3/puts)(3),
[scanf](https://manual.cs50.io/3/scanf)(3), [ungetwc](https://manual.cs50.io/3/ungetwc)(3),
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3),
[feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)

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
- https://manual.cs50.io/3/fgetc — retrieved 2026-10-18T05:45:55+03:30, sha256 `4c7eb4fc4a120c8f…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
