---
id: manual-abs
type: reference
title: abs(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/abs
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:38+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- abs
- c
- manual
checksum: sha256:d230fcb37f0a121e400a3e8a4fc1459305198593369226f86d61cecf7d5c07f0
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# abs(3) — CS50 manual page

## 1. Source metadata
- **Title:** abs(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/abs>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:38+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/abs> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/abs#name)

abs, labs, llabs, imaxabs - compute the absolute value of an
integer

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/abs#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/abs#synopsis)

```
#include <stdlib.h>
int abs(int j);
long labs(long j);
long long llabs(long long j);
#include <inttypes.h>
intmax_t imaxabs(intmax_t j);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[llabs](https://manual.cs50.io/3/llabs)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/abs#description)

The [abs](https://manual.cs50.io/3/abs)() function computes the absolute value of
the integer argument `j`. The [labs](https://manual.cs50.io/3/labs)(),
[llabs](https://manual.cs50.io/3/llabs)(), and [imaxabs](https://manual.cs50.io/3/imaxabs)() functions
compute the absolute value of the argument `j` of the appropriate
integer type for the function.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/abs#return-value)

Returns the absolute value of the integer argument, of the
appropriate integer type for the function.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/abs#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [abs](https://manual.cs50.io/3/abs)(), [labs](https://manual.cs50.io/3/labs)(), [llabs](https://manual.cs50.io/3/llabs)(), [imaxabs](https://manual.cs50.io/3/imaxabs)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/abs#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/abs#history)

POSIX.1-2001, C99, SVr4, 4.3BSD.

C89 only includes the [abs](https://manual.cs50.io/3/abs)() and
[labs](https://manual.cs50.io/3/labs)() functions; the functions
[llabs](https://manual.cs50.io/3/llabs)() and [imaxabs](https://manual.cs50.io/3/imaxabs)() were added in
C99.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/abs#notes)

Trying to take the absolute value of the most negative integer is not
defined.

The [llabs](https://manual.cs50.io/3/llabs)() function is included since glibc 2.0.
The [imaxabs](https://manual.cs50.io/3/imaxabs)() function is included since glibc
2.1.1.

For [llabs](https://manual.cs50.io/3/llabs)() to be declared, it may be necessary to
define **_ISOC99_SOURCE** or
**_ISOC9X_SOURCE** (depending on the version of glibc)
before including any standard headers.

By default, GCC handles [abs](https://manual.cs50.io/3/abs)(),
[labs](https://manual.cs50.io/3/labs)(), and (since GCC 3.0) [llabs](https://manual.cs50.io/3/llabs)()
and [imaxabs](https://manual.cs50.io/3/imaxabs)() as built-in functions.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/abs#see-also)

[cabs](https://manual.cs50.io/3/cabs)(3), [ceil](https://manual.cs50.io/3/ceil)(3),
[fabs](https://manual.cs50.io/3/fabs)(3), [floor](https://manual.cs50.io/3/floor)(3),
[rint](https://manual.cs50.io/3/rint)(3)

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
- https://manual.cs50.io/3/abs — retrieved 2026-10-18T05:45:38+03:30, sha256 `d230fcb37f0a121e…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
