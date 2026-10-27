---
id: manual-fputc
type: reference
title: fputc(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/fputc
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:56+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- fputc
- manual
checksum: sha256:63e336e919faf5fa70ad00523f484c768859f953b0e469b6d5f3d49748116f45
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# fputc(3) — CS50 manual page

## 1. Source metadata
- **Title:** fputc(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/fputc>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:56+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/fputc> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/fputc#name)

fputc, fputs, putc, putchar, puts - output of characters and
strings

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/fputc#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/fputc#synopsis)

```
#include <stdio.h>
int fputc(int c, FILE *stream);
int putc(int c, FILE *stream);
int putchar(int c);
int fputs(const char *restrict s, FILE *restrict stream);
int puts(const char *s);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/fputc#description)

[fputc](https://manual.cs50.io/3/fputc)() writes the character `c`, cast to an
`unsigned char`, to `stream`.

[putc](https://manual.cs50.io/3/putc)() is equivalent to [fputc](https://manual.cs50.io/3/fputc)()
except that it may be implemented as a macro which evaluates
`stream` more than once.

**[putchar](https://manual.cs50.io/3/putchar)(**`c`**)** is equivalent
to **[putc](https://manual.cs50.io/3/putc)(**`c`**,**`stdout`**)**`.`

[fputs](https://manual.cs50.io/3/fputs)() writes the string `s` to
`stream`, without its terminating null byte ('\0').

[puts](https://manual.cs50.io/3/puts)() writes the string `s` and a trailing
newline to `stdout`.

Calls to the functions described here can be mixed with each other
and with calls to other output functions from the `stdio` library
for the same output stream.

For nonlocking counterparts, see
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3).

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/fputc#return-value)

[fputc](https://manual.cs50.io/3/fputc)(), [putc](https://manual.cs50.io/3/putc)(), and
[putchar](https://manual.cs50.io/3/putchar)() return the character written as an
`unsigned char` cast to an `int` or **EOF**
on error.

[puts](https://manual.cs50.io/3/puts)() and [fputs](https://manual.cs50.io/3/fputs)() return a
nonnegative number on success, or **EOF** on error.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/fputc#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [fputc](https://manual.cs50.io/3/fputc)(), [fputs](https://manual.cs50.io/3/fputs)(), [putc](https://manual.cs50.io/3/putc)(), [putchar](https://manual.cs50.io/3/putchar)(), [puts](https://manual.cs50.io/3/puts)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/fputc#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/fputc#history)

POSIX.1-2001, C89, C99.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/fputc#bugs)

It is not advisable to mix calls to output functions from the
`stdio` library with low-level calls to [write](https://manual.cs50.io/2/write)(2)
for the file descriptor associated with the same output stream; the
results will be undefined and very probably not what you want.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/fputc#see-also)

[write](https://manual.cs50.io/2/write)(2), [ferror](https://manual.cs50.io/3/ferror)(3),
[fgets](https://manual.cs50.io/3/fgets)(3), [fopen](https://manual.cs50.io/3/fopen)(3),
[fputwc](https://manual.cs50.io/3/fputwc)(3), [fputws](https://manual.cs50.io/3/fputws)(3),
[fseek](https://manual.cs50.io/3/fseek)(3), [fwrite](https://manual.cs50.io/3/fwrite)(3),
[putwchar](https://manual.cs50.io/3/putwchar)(3), [scanf](https://manual.cs50.io/3/scanf)(3),
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
- https://manual.cs50.io/3/fputc — retrieved 2026-10-18T05:45:56+03:30, sha256 `63e336e919faf5fa…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
