---
id: manual-sqrt
type: reference
title: sqrt(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/sqrt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:34+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- sqrt
checksum: sha256:e758dc630a6a015cf731bb1cd92e522e71bbe0370e4ed3ad33bd81f4d97b56ca
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# sqrt(3) — CS50 manual page

## 1. Source metadata
- **Title:** sqrt(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/sqrt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:34+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/sqrt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/sqrt#name)

sqrt - calculate the square root of a number

sqrt, sqrtf, sqrtl - square root function

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/sqrt#library)

Math library (`libm`, `-lm`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/sqrt#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <math.h>
```

<a id="prototype"></a>

#### Prototype

```c
double sqrt(double x);
```

```
#include <math.h>
double sqrt(double x);
float sqrtf(float x);
long double sqrtl(long double x);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[sqrtf](https://manual.cs50.io/3/sqrtf)(), [sqrtl](https://manual.cs50.io/3/sqrtl)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
        || /* Since glibc 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/sqrt#description)

This function calculates the square root of `x`.

These functions return the nonnegative square root of `x`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/sqrt#return-value)

This function returns, as a `double`, the square root of `x`.

On success, these functions return the square root of `x`.

If `x` is a NaN, a NaN is returned.

If `x` is +0 (-0), +0 (-0) is returned.

If `x` is positive infinity, positive infinity is
returned.

If `x` is less than -0, a domain error occurs, and a NaN is
returned.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/sqrt#example)

```c
#include <math.h>  
#include <stdio.h>  

int main(void)
{
    printf("This is CS%i\n", (int) sqrt(2500));
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/sqrt#errors)

See [math_error](https://manual.cs50.io/7/math_error)(7) for information on how to
determine whether an error has occurred when calling these
functions.

The following errors can occur:

Domain error: `x` less than -0
:   `errno` is set to **EDOM**. An invalid
    floating-point exception (**FE_INVALID**) is raised.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/sqrt#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [sqrt](https://manual.cs50.io/3/sqrt)(), [sqrtf](https://manual.cs50.io/3/sqrtf)(), [sqrtl](https://manual.cs50.io/3/sqrtl)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/sqrt#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/sqrt#history)

C99, POSIX.1-2001.

The variant returning `double` also conforms to SVr4, 4.3BSD,
C89.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/sqrt#see-also)

[cbrt](https://manual.cs50.io/3/cbrt)(3), [csqrt](https://manual.cs50.io/3/csqrt)(3),
[hypot](https://manual.cs50.io/3/hypot)(3)

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
- https://manual.cs50.io/3/sqrt — retrieved 2026-10-18T05:45:34+03:30, sha256 `e758dc630a6a015c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
