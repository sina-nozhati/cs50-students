---
id: manual-pow
type: reference
title: pow(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/pow
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:33+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- pow
checksum: sha256:da58dd81323ae9e199d94768cb7d7f959d413c689344a2bb54f2bc1ae4c12729
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# pow(3) — CS50 manual page

## 1. Source metadata
- **Title:** pow(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/pow>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:33+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/pow> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/pow#name)

pow - raise a number to a power

pow, powf, powl - power functions

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/pow#library)

Math library (`libm`, `-lm`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/pow#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <math.h>
```

<a id="prototype"></a>

#### Prototype

```c
double pow(double x, double y);
```

```
#include <math.h>
double pow(double x, double y);
float powf(float x, float y);
long double powl(long double x, long double y);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[powf](https://manual.cs50.io/3/powf)(), [powl](https://manual.cs50.io/3/powl)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
        || /* Since glibc 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/pow#description)

This function raises `x` to the power of `y`.

These functions return the value of `x` raised to the power of
`y`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/pow#return-value)

This function returns, as a `double`, `x` raised to the power of `y`.

On success, these functions return the value of `x` to the
power of `y`.

If the result overflows, a range error occurs, and the functions
return **HUGE_VAL**, **HUGE_VALF**, or
**HUGE_VALL**, respectively, with the mathematically
correct sign.

If result underflows, and is not representable, a range error occurs,
and 0.0 with the appropriate sign is returned.

If `x` is +0 or -0, and `y` is an odd integer less than
0, a pole error occurs and **HUGE_VAL**,
**HUGE_VALF**, or **HUGE_VALL**, is returned,
with the same sign as `x`.

If `x` is +0 or -0, and `y` is less than 0 and not an
odd integer, a pole error occurs and +**HUGE_VAL**,
+**HUGE_VALF**, or +**HUGE_VALL**, is
returned.

If `x` is +0 (-0), and `y` is an odd integer greater
than 0, the result is +0 (-0).

If `x` is 0, and `y` greater than 0 and not an odd
integer, the result is +0.

If `x` is -1, and `y` is positive infinity or negative
infinity, the result is 1.0.

If `x` is +1, the result is 1.0 (even if `y` is a
NaN).

If `y` is 0, the result is 1.0 (even if `x` is a
NaN).

If `x` is a finite value less than 0, and `y` is a
finite noninteger, a domain error occurs, and a NaN is returned.

If the absolute value of `x` is less than 1, and `y` is
negative infinity, the result is positive infinity.

If the absolute value of `x` is greater than 1, and `y`
is negative infinity, the result is +0.

If the absolute value of `x` is less than 1, and `y` is
positive infinity, the result is +0.

If the absolute value of `x` is greater than 1, and `y`
is positive infinity, the result is positive infinity.

If `x` is negative infinity, and `y` is an odd integer
less than 0, the result is -0.

If `x` is negative infinity, and `y` less than 0 and
not an odd integer, the result is +0.

If `x` is negative infinity, and `y` is an odd integer
greater than 0, the result is negative infinity.

If `x` is negative infinity, and `y` greater than 0 and
not an odd integer, the result is positive infinity.

If `x` is positive infinity, and `y` less than 0, the
result is +0.

If `x` is positive infinity, and `y` greater than 0,
the result is positive infinity.

Except as specified above, if `x` or `y` is a NaN, the
result is a NaN.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/pow#example)

```c
#include <math.h>  
#include <stdio.h>  

int main(void)
{
    printf("A 32-bit integer can store %li possible values.\n", (long) pow(2, 32));
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/pow#errors)

See [math_error](https://manual.cs50.io/7/math_error)(7) for information on how to
determine whether an error has occurred when calling these
functions.

The following errors can occur:

Domain error: `x` is negative, and `y` is a finite noninteger
:   `errno` is set to **EDOM**. An invalid
    floating-point exception (**FE_INVALID**) is raised.

Pole error: `x` is zero, and `y` is negative
:   `errno` is set to **ERANGE** (but see BUGS). A
    divide-by-zero floating-point exception (**FE_DIVBYZERO**)
    is raised.

Range error: the result overflows
:   `errno` is set to **ERANGE**. An overflow
    floating-point exception (**FE_OVERFLOW**) is raised.

Range error: the result underflows
:   `errno` is set to **ERANGE**. An underflow
    floating-point exception (**FE_UNDERFLOW**) is raised.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/pow#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [pow](https://manual.cs50.io/3/pow)(), [powf](https://manual.cs50.io/3/powf)(), [powl](https://manual.cs50.io/3/powl)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/pow#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/pow#history)

C99, POSIX.1-2001.

The variant returning `double` also conforms to SVr4, 4.3BSD,
C89.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/pow#bugs)

<a id="historical-bugs-now-fixed"></a>

#### Historical bugs (now fixed)

Before glibc 2.28, on some architectures (e.g., x86-64)
[pow](https://manual.cs50.io/3/pow)() may be more than 10,000 times slower for some
inputs than for other nearby inputs. This affects only
[pow](https://manual.cs50.io/3/pow)(), and not [powf](https://manual.cs50.io/3/powf)() nor
[powl](https://manual.cs50.io/3/powl)(). This problem was fixed in glibc 2.28.

A number of bugs in the glibc implementation of
[pow](https://manual.cs50.io/3/pow)() were fixed in glibc 2.16.

In glibc 2.9 and earlier, when a pole error occurs, `errno` is
set to **EDOM** instead of the POSIX-mandated
**ERANGE**. Since glibc 2.10, glibc does the right
thing.

In glibc 2.3.2 and earlier, when an overflow or underflow error
occurs, glibc's [pow](https://manual.cs50.io/3/pow)() generates a bogus invalid
floating-point exception (**FE_INVALID**) in addition to
the overflow or underflow exception.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/pow#see-also)

[cbrt](https://manual.cs50.io/3/cbrt)(3), [cpow](https://manual.cs50.io/3/cpow)(3),
[sqrt](https://manual.cs50.io/3/sqrt)(3)

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
- https://manual.cs50.io/3/pow — retrieved 2026-10-18T05:45:33+03:30, sha256 `da58dd81323ae9e1…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
