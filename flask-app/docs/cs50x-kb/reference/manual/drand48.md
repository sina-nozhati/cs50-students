---
id: manual-drand48
type: reference
title: drand48(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/drand48
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:41+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- drand48
- manual
checksum: sha256:e93fa70769613120911eeca2d63eacf2a9589cf519ec75210a84b8555eb301c4
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# drand48(3) — CS50 manual page

## 1. Source metadata
- **Title:** drand48(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/drand48>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:41+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/drand48> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/drand48#name)

drand48, erand48, lrand48, nrand48, mrand48, jrand48, srand48,
seed48, lcong48 - generate uniformly distributed pseudo-random
numbers

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/drand48#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/drand48#synopsis)

```
#include <stdlib.h>
double drand48(void);
double erand48(unsigned short xsubi[3]);
long lrand48(void);
long nrand48(unsigned short xsubi[3]);
long mrand48(void);
long jrand48(unsigned short xsubi[3]);
void srand48(long seedval);
unsigned short *seed48(unsigned short seed16v[3]);
void lcong48(unsigned short param[7]);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

All functions shown above:

```
    _XOPEN_SOURCE
        || /* glibc >= 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/drand48#description)

These functions generate pseudo-random numbers using the linear
congruential algorithm and 48-bit integer arithmetic.

The [drand48](https://manual.cs50.io/3/drand48)() and [erand48](https://manual.cs50.io/3/erand48)()
functions return nonnegative double-precision floating-point values
uniformly distributed over the interval [0.0, 1.0).

The [lrand48](https://manual.cs50.io/3/lrand48)() and [nrand48](https://manual.cs50.io/3/nrand48)()
functions return nonnegative long integers uniformly distributed over
the interval [0, 2^31).

The [mrand48](https://manual.cs50.io/3/mrand48)() and [jrand48](https://manual.cs50.io/3/jrand48)()
functions return signed long integers uniformly distributed over the
interval [-2^31, 2^31).

The [srand48](https://manual.cs50.io/3/srand48)(), [seed48](https://manual.cs50.io/3/seed48)(), and
[lcong48](https://manual.cs50.io/3/lcong48)() functions are initialization functions, one
of which should be called before using [drand48](https://manual.cs50.io/3/drand48)(),
[lrand48](https://manual.cs50.io/3/lrand48)(), or [mrand48](https://manual.cs50.io/3/mrand48)(). The functions
[erand48](https://manual.cs50.io/3/erand48)(), [nrand48](https://manual.cs50.io/3/nrand48)(), and
[jrand48](https://manual.cs50.io/3/jrand48)() do not require an initialization function to
be called first.

All the functions work by generating a sequence of 48-bit integers,
`Xi`, according to the linear congruential formula:

```
Xn+1 = (aXn + c) mod m, where n >= 0
```

The parameter `m` = 2^48, hence 48-bit integer arithmetic is
performed. Unless [lcong48](https://manual.cs50.io/3/lcong48)() is called, `a` and
`c` are given by:

```
a = 0x5DEECE66D
c = 0xB
```

The value returned by any of the functions
[drand48](https://manual.cs50.io/3/drand48)(), [erand48](https://manual.cs50.io/3/erand48)(),
[lrand48](https://manual.cs50.io/3/lrand48)(), [nrand48](https://manual.cs50.io/3/nrand48)(),
[mrand48](https://manual.cs50.io/3/mrand48)(), or [jrand48](https://manual.cs50.io/3/jrand48)() is computed by
first generating the next 48-bit `Xi` in the sequence. Then the
appropriate number of bits, according to the type of data item to be
returned, is copied from the high-order bits of `Xi` and
transformed into the returned value.

The functions [drand48](https://manual.cs50.io/3/drand48)(), [lrand48](https://manual.cs50.io/3/lrand48)(),
and [mrand48](https://manual.cs50.io/3/mrand48)() store the last 48-bit `Xi`
generated in an internal buffer. The functions
[erand48](https://manual.cs50.io/3/erand48)(), [nrand48](https://manual.cs50.io/3/nrand48)(), and
[jrand48](https://manual.cs50.io/3/jrand48)() require the calling program to provide
storage for the successive `Xi` values in the array argument
`xsubi`. The functions are initialized by placing the initial
value of `Xi` into the array before calling the function for the
first time.

The initializer function [srand48](https://manual.cs50.io/3/srand48)() sets the high
order 32-bits of `Xi` to the argument `seedval`. The low
order 16-bits are set to the arbitrary value 0x330E.

The initializer function [seed48](https://manual.cs50.io/3/seed48)() sets the value of
`Xi` to the 48-bit value specified in the array argument
`seed16v`. The previous value of `Xi` is copied into an
internal buffer and a pointer to this buffer is returned by
[seed48](https://manual.cs50.io/3/seed48)().

The initialization function [lcong48](https://manual.cs50.io/3/lcong48)() allows the
user to specify initial values for `Xi`, `a`, and
`c`. Array argument elements `param[0-2]` specify
`Xi`, `param[3-5]` specify `a`, and
`param[6]` specifies `c`. After [lcong48](https://manual.cs50.io/3/lcong48)()
has been called, a subsequent call to either [srand48](https://manual.cs50.io/3/srand48)()
or [seed48](https://manual.cs50.io/3/seed48)() will restore the standard values of
`a` and `c`.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/drand48#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [drand48](https://manual.cs50.io/3/drand48)(), [erand48](https://manual.cs50.io/3/erand48)(), [lrand48](https://manual.cs50.io/3/lrand48)(), [nrand48](https://manual.cs50.io/3/nrand48)(), [mrand48](https://manual.cs50.io/3/mrand48)(), [jrand48](https://manual.cs50.io/3/jrand48)(), [srand48](https://manual.cs50.io/3/srand48)(), [seed48](https://manual.cs50.io/3/seed48)(), [lcong48](https://manual.cs50.io/3/lcong48)() | Thread safety | MT-Unsafe race:drand48 |

The above functions record global state information for the random
number generator, so they are not thread-safe.

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/drand48#standards)

POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/drand48#history)

POSIX.1-2001, SVr4.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/drand48#see-also)

[rand](https://manual.cs50.io/3/rand)(3), [random](https://manual.cs50.io/3/random)(3)

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
- https://manual.cs50.io/3/drand48 — retrieved 2026-10-18T05:45:41+03:30, sha256 `e93fa70769613120…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
