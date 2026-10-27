---
id: manual-ceil
type: reference
title: ceil(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/ceil
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:37+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- ceil
- manual
checksum: sha256:b7a0f003af9962a12940312bc57ff1c4526adae34ca0bac31b32ae82cbc1614e
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# ceil(3) — CS50 manual page

## 1. Source metadata
- **Title:** ceil(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/ceil>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/ceil> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/ceil#name)

ceil - calculate the ceiling of a number

ceil, ceilf, ceill - ceiling function: smallest integral value not
less than argument

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/ceil#library)

Math library (`libm`, `-lm`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/ceil#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <math.h>
```

<a id="prototype"></a>

#### Prototype

```c
double ceil(double x);
```

```
#include <math.h>
double ceil(double x);
float ceilf(float x);
long double ceill(long double x);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[ceilf](https://manual.cs50.io/3/ceilf)(), [ceill](https://manual.cs50.io/3/ceill)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
        || /* Since glibc 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/ceil#description)

This function returns the ceiling of `x`.

These functions return the smallest integral value that is not less
than `x`.

For example, `ceil(0.5)` is 1.0, and `ceil(-0.5)` is
0.0.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/ceil#return-value)

This function returns, as a `double`, the smallest integer that is not less than `x`. You may safely cast that value to a `long` (or an `int` if it fits).

These functions return the ceiling of `x`.

If `x` is integral, +0, -0, NaN, or infinite, `x`
itself is returned.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/ceil#example)

```c
#include <math.h>  
#include <stdio.h>  

int main(void)
{
    printf("This is CS%i\n", (int) ceil(49.9));
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/ceil#errors)

No errors occur. POSIX.1-2001 documents a range error for overflows,
but see NOTES.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/ceil#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [ceil](https://manual.cs50.io/3/ceil)(), [ceilf](https://manual.cs50.io/3/ceilf)(), [ceill](https://manual.cs50.io/3/ceill)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/ceil#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/ceil#history)

C99, POSIX.1-2001.

The variant returning `double` also conforms to SVr4, 4.3BSD,
C89.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/ceil#notes)

SUSv2 and POSIX.1-2001 contain text about overflow (which might set
`errno` to **ERANGE**, or raise an
**FE_OVERFLOW** exception). In practice, the result cannot
overflow on any current machine, so this error-handling stuff is just
nonsense. (More precisely, overflow can happen only when the maximum
value of the exponent is smaller than the number of mantissa bits. For
the IEEE-754 standard 32-bit and 64-bit floating-point numbers the
maximum value of the exponent is 127 (respectively, 1023), and the
number of mantissa bits including the implicit bit is 24 (respectively,
53).)

The integral value returned by these functions may be too large to
store in an integer type (`int`, `long`, etc.). To avoid
an overflow, which will produce undefined results, an application should
perform a range check on the returned value before assigning it to an
integer type.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/ceil#see-also)

[floor](https://manual.cs50.io/3/floor)(3), [lrint](https://manual.cs50.io/3/lrint)(3),
[nearbyint](https://manual.cs50.io/3/nearbyint)(3), [rint](https://manual.cs50.io/3/rint)(3),
[round](https://manual.cs50.io/3/round)(3), [trunc](https://manual.cs50.io/3/trunc)(3)

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
- https://manual.cs50.io/3/ceil — retrieved 2026-10-18T05:45:37+03:30, sha256 `b7a0f003af9962a1…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
