---
id: manual-fabs
type: reference
title: fabs(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/fabs
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:35+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- fabs
- manual
checksum: sha256:9c7e342a290e5b8d2cc1e05db4ffdccb20f3301348a725ca289035afc79deb4e
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# fabs(3) — CS50 manual page

## 1. Source metadata
- **Title:** fabs(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/fabs>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:35+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/fabs> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/fabs#name)

fabs, fabsf, fabsl - absolute value of floating-point number

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/fabs#library)

Math library (`libm`, `-lm`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/fabs#synopsis)

```
#include <math.h>
double fabs(double x);
float fabsf(float x);
long double fabsl(long double x);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[fabsf](https://manual.cs50.io/3/fabsf)(), [fabsl](https://manual.cs50.io/3/fabsl)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
        || /* Since glibc 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/fabs#description)

These functions return the absolute value of the floating-point
number `x`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/fabs#return-value)

These functions return the absolute value of `x`.

If `x` is a NaN, a NaN is returned.

If `x` is -0, +0 is returned.

If `x` is negative infinity or positive infinity, positive
infinity is returned.

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/fabs#errors)

No errors occur.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/fabs#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [fabs](https://manual.cs50.io/3/fabs)(), [fabsf](https://manual.cs50.io/3/fabsf)(), [fabsl](https://manual.cs50.io/3/fabsl)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/fabs#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/fabs#history)

C99, POSIX.1-2001.

The variant returning `double` also conforms to SVr4, 4.3BSD,
C89.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/fabs#see-also)

[abs](https://manual.cs50.io/3/abs)(3), [cabs](https://manual.cs50.io/3/cabs)(3),
[ceil](https://manual.cs50.io/3/ceil)(3), [floor](https://manual.cs50.io/3/floor)(3),
[labs](https://manual.cs50.io/3/labs)(3), [rint](https://manual.cs50.io/3/rint)(3)

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
- https://manual.cs50.io/3/fabs — retrieved 2026-10-18T05:45:35+03:30, sha256 `9c7e342a290e5b8d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
