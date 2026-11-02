---
id: manual-assert
type: reference
title: assert(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/assert
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:13+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- assert
- c
- manual
checksum: sha256:8fb29bdc50a37ef15f3f9e0e850225daac02e544958ad4802b513584b8e4b2c2
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# assert(3) — CS50 manual page

## 1. Source metadata
- **Title:** assert(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/assert>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:13+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/assert> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/assert#name)

assert - abort the program if assertion is false

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/assert#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/assert#synopsis)

```
#include <assert.h>
void assert(scalar expression);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/assert#description)

This macro can help programmers find bugs in their programs, or
handle exceptional cases via a crash that will produce limited debugging
output.

If `expression` is false (i.e., compares equal to zero),
[assert](https://manual.cs50.io/3/assert)() prints an error message to standard error and
terminates the program by calling [abort](https://manual.cs50.io/3/abort)(3). The error
message includes the name of the file and function containing the
[assert](https://manual.cs50.io/3/assert)() call, the source code line number of the call,
and the text of the argument; something like:

```
prog: some_file.c:16: some_func: Assertion `val == 0' failed.
```

If the macro **NDEBUG** is defined at the moment
`<assert.h>` was last included, the macro
[assert](https://manual.cs50.io/3/assert)() generates no code, and hence does nothing at
all. It is not recommended to define **NDEBUG** if using
[assert](https://manual.cs50.io/3/assert)() to detect error conditions since the software
may behave non-deterministically.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/assert#return-value)

No value is returned.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/assert#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [assert](https://manual.cs50.io/3/assert)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/assert#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/assert#history)

C89, C99, POSIX.1-2001.

In C89, `expression` is required to be of type `int`
and undefined behavior results if it is not, but in C99 it may have any
scalar type.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/assert#bugs)

[assert](https://manual.cs50.io/3/assert)() is implemented as a macro; if the
expression tested has side-effects, program behavior will be different
depending on whether **NDEBUG** is defined. This may create
Heisenbugs which go away when debugging is turned on.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/assert#see-also)

[abort](https://manual.cs50.io/3/abort)(3), [assert_perror](https://manual.cs50.io/3/assert_perror)(3),
[exit](https://manual.cs50.io/3/exit)(3)

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
- https://manual.cs50.io/3/assert — retrieved 2026-10-18T05:46:13+03:30, sha256 `8fb29bdc50a37ef1…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
