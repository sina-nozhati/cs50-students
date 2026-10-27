---
id: manual-floor
type: reference
title: floor(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/floor
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:36+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- floor
- manual
checksum: sha256:5f9f9ad678050b4824a2c5d1781b01f756d04f7f458995f91f0405cc92abae25
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# floor(3) — CS50 manual page

## 1. Source metadata
- **Title:** floor(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/floor>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:36+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/floor> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/floor#name)

floor - calculate the floor of a number

floor, floorf, floorl - largest integral value not greater than
argument

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/floor#library)

Math library (`libm`, `-lm`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/floor#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <math.h>
```

<a id="prototype"></a>

#### Prototype

```c
double floor(double x);
```

```
#include <math.h>
double floor(double x);
float floorf(float x);
long double floorl(long double x);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[floorf](https://manual.cs50.io/3/floorf)(), [floorl](https://manual.cs50.io/3/floorl)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
        || /* Since glibc 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/floor#description)

This function returns the floor of `x`.

These functions return the largest integral value that is not greater
than `x`.

For example, `floor(0.5)` is 0.0, and `floor(-0.5)` is
-1.0.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/floor#return-value)

This function returns, as a `double`, the largest integer that is not greater than `x`. You may safely cast that value to a `long` (or an `int` if it fits).

These functions return the floor of `x`.

If `x` is integral, +0, -0, NaN, or an infinity, `x`
itself is returned.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/floor#example)

```c
#include <math.h>  
#include <stdio.h>  

int main(void)
{
    printf("This is CS%i\n", (int) floor(50.1));
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/floor#errors)

No errors occur. POSIX.1-2001 documents a range error for overflows,
but see NOTES.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/floor#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [floor](https://manual.cs50.io/3/floor)(), [floorf](https://manual.cs50.io/3/floorf)(), [floorl](https://manual.cs50.io/3/floorl)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/floor#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/floor#history)

C99, POSIX.1-2001.

The variant returning `double` also conforms to SVr4, 4.3BSD,
C89.

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

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/floor#see-also)

[ceil](https://manual.cs50.io/3/ceil)(3), [lrint](https://manual.cs50.io/3/lrint)(3),
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
- https://manual.cs50.io/3/floor — retrieved 2026-10-18T05:45:36+03:30, sha256 `5f9f9ad678050b48…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
