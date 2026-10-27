---
id: manual-strdup
type: reference
title: strdup(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strdup
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:16+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strdup
checksum: sha256:bc6f6694c53e2eb168d4bd1ec1bcda145aaab2ba2574d0d5b524a30f31884fba
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strdup(3) — CS50 manual page

## 1. Source metadata
- **Title:** strdup(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strdup>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:16+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strdup> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strdup#name)

strdup, strndup, strdupa, strndupa - duplicate a string

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strdup#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strdup#synopsis)

```
#include <string.h>
char *strdup(const char *s);
char *strndup(const char s[.n], size_t n);
char *strdupa(const char *s);
char *strndupa(const char s[.n], size_t n);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[strdup](https://manual.cs50.io/3/strdup)():

```
    _XOPEN_SOURCE >= 500
        || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

[strndup](https://manual.cs50.io/3/strndup)():

```
    Since glibc 2.10:
        _POSIX_C_SOURCE >= 200809L
    Before glibc 2.10:
        _GNU_SOURCE
```

[strdupa](https://manual.cs50.io/3/strdupa)(), [strndupa](https://manual.cs50.io/3/strndupa)():

```
    _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strdup#description)

The [strdup](https://manual.cs50.io/3/strdup)() function returns a pointer to a new
string which is a duplicate of the string `s`. Memory for the new
string is obtained with [malloc](https://manual.cs50.io/3/malloc)(3), and can be freed
with [free](https://manual.cs50.io/3/free)(3).

The [strndup](https://manual.cs50.io/3/strndup)() function is similar, but copies at
most `n` bytes. If `s` is longer than `n`, only
`n` bytes are copied, and a terminating null byte ('\0') is
added.

[strdupa](https://manual.cs50.io/3/strdupa)() and [strndupa](https://manual.cs50.io/3/strndupa)() are
similar, but use [alloca](https://manual.cs50.io/3/alloca)(3) to allocate the buffer.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strdup#return-value)

On success, the [strdup](https://manual.cs50.io/3/strdup)() function returns a pointer
to the duplicated string. It returns NULL if insufficient memory was
available, with `errno` set to indicate the error.

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/strdup#errors)

**ENOMEM**
:   Insufficient memory available to allocate duplicate string.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strdup#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strdup](https://manual.cs50.io/3/strdup)(), [strndup](https://manual.cs50.io/3/strndup)(), [strdupa](https://manual.cs50.io/3/strdupa)(), [strndupa](https://manual.cs50.io/3/strndupa)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strdup#standards)

[strdup](https://manual.cs50.io/3/strdup)() [strndup](https://manual.cs50.io/3/strndup)()
:   POSIX.1-2008.

[strdupa](https://manual.cs50.io/3/strdupa)() [strndupa](https://manual.cs50.io/3/strndupa)()
:   GNU.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strdup#history)

[strdup](https://manual.cs50.io/3/strdup)()
:   SVr4, 4.3BSD-Reno, POSIX.1-2001.

[strndup](https://manual.cs50.io/3/strndup)()
:   POSIX.1-2008.

[strdupa](https://manual.cs50.io/3/strdupa)() [strndupa](https://manual.cs50.io/3/strndupa)()
:   GNU.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strdup#see-also)

[alloca](https://manual.cs50.io/3/alloca)(3), [calloc](https://manual.cs50.io/3/calloc)(3),
[free](https://manual.cs50.io/3/free)(3), [malloc](https://manual.cs50.io/3/malloc)(3),
[realloc](https://manual.cs50.io/3/realloc)(3), [string](https://manual.cs50.io/3/string)(3),
[wcsdup](https://manual.cs50.io/3/wcsdup)(3)

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
- https://manual.cs50.io/3/strdup — retrieved 2026-10-18T05:45:16+03:30, sha256 `bc6f6694c53e2eb1…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
