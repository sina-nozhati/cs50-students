---
id: manual-atol
type: reference
title: atol(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/atol
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:29+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- atol
- c
- manual
checksum: sha256:883fc6594ac21e2006885832a7bf233ad67aa15c6da75b6805cbd6f92c730407
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# atol(3) — CS50 manual page

## 1. Source metadata
- **Title:** atol(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/atol>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:29+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/atol> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/atol#name)

atol - convert a `string` to a `long`

atoi, atol, atoll - convert a string to an integer

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/atol#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/atol#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdlib.h>
```

<a id="prototype"></a>

#### Prototype

```c
long atol(string s);
```

```
#include <stdlib.h>
int atoi(const char *nptr);
long atol(const char *nptr);
long long atoll(const char *nptr);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[atoll](https://manual.cs50.io/3/atoll)():

```
    _ISOC99_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/atol#description)

This function converts a (positive or negative) integer from a `string` (e.g., `"50"`) to a `long` (e.g., `50`).

The [atoi](https://manual.cs50.io/3/atoi)() function converts the initial portion of
the string pointed to by `nptr` to `int`. The behavior is
the same as

```
strtol(nptr, NULL, 10);
```

except that [atoi](https://manual.cs50.io/3/atoi)() does not detect errors.

The [atol](https://manual.cs50.io/3/atol)() and [atoll](https://manual.cs50.io/3/atoll)() functions
behave the same as [atoi](https://manual.cs50.io/3/atoi)(), except that they convert the
initial portion of the string to their return type of `long` or
`long long`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/atol#return-value)

This function returns its input, `s`, as a `long`.

The converted value or 0 on error.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/atol#example)

```c
#include <stdio.h>  
#include <stdlib.h>  

int main(void)
{
    printf("This is CS%li\n", atol("50"));
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/atol#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [atoi](https://manual.cs50.io/3/atoi)(), [atol](https://manual.cs50.io/3/atol)(), [atoll](https://manual.cs50.io/3/atoll)() | Thread safety | MT-Safe locale |

<a id="versions"></a>

### [VERSIONS](https://manual.cs50.io/3/atol#versions)

POSIX.1 leaves the return value of [atoi](https://manual.cs50.io/3/atoi)() on error
unspecified. On glibc, musl libc, and uClibc, 0 is returned on
error.

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/atol#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/atol#history)

C99, POSIX.1-2001, SVr4, 4.3BSD.

C89 and POSIX.1-1996 include the functions [atoi](https://manual.cs50.io/3/atoi)()
and [atol](https://manual.cs50.io/3/atol)() only.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/atol#bugs)

`errno` is not set on error so there is no way to distinguish
between 0 as an error and as the converted value. No checks for overflow
or underflow are done. Only base-10 input can be converted. It is
recommended to instead use the [strtol](https://manual.cs50.io/3/strtol)() and
[strtoul](https://manual.cs50.io/3/strtoul)() family of functions in new programs.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/atol#see-also)

[atof](https://manual.cs50.io/3/atof)(3), [strtod](https://manual.cs50.io/3/strtod)(3),
[strtol](https://manual.cs50.io/3/strtol)(3), [strtoul](https://manual.cs50.io/3/strtoul)(3)

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
- https://manual.cs50.io/3/atol — retrieved 2026-10-18T05:45:29+03:30, sha256 `883fc6594ac21e20…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
