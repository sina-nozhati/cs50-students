---
id: manual-strtol
type: reference
title: strtol(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strtol
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:30+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strtol
checksum: sha256:ec2fc1950b0becdd345550e40fc15287b1f0ff471f585984a582319fbe1eef8d
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strtol(3) — CS50 manual page

## 1. Source metadata
- **Title:** strtol(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strtol>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:30+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strtol> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strtol#name)

strtol, strtoll, strtoq - convert a string to a long integer

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strtol#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strtol#synopsis)

```
#include <stdlib.h>
long strtol(const char *restrict nptr,
 char **restrict endptr, int base);
long long strtoll(const char *restrict nptr,
 char **restrict endptr, int base);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[strtoll](https://manual.cs50.io/3/strtoll)():

```
    _ISOC99_SOURCE
        || /* glibc <= 2.19: */ _SVID_SOURCE || _BSD_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strtol#description)

The [strtol](https://manual.cs50.io/3/strtol)() function converts the initial part of
the string in `nptr` to a long integer value according to the
given `base`, which must be between 2 and 36 inclusive, or be the
special value 0.

The string may begin with an arbitrary amount of white space (as
determined by [isspace](https://manual.cs50.io/3/isspace)(3)) followed by a single optional
'+' or '-' sign. If `base` is zero or 16, the string may then
include a "0x" or "0X" prefix, and the number will be read in base 16;
otherwise, a zero `base` is taken as 10 (decimal) unless the next
character is '0', in which case it is taken as 8 (octal).

The remainder of the string is converted to a `long` value in
the obvious manner, stopping at the first character which is not a valid
digit in the given base. (In bases above 10, the letter 'A' in either
uppercase or lowercase represents 10, 'B' represents 11, and so forth,
with 'Z' representing 35.)

If `endptr` is not NULL, and the `base` is supported,
[strtol](https://manual.cs50.io/3/strtol)() stores the address of the first invalid
character in `*endptr`. If there were no digits at all,
[strtol](https://manual.cs50.io/3/strtol)() stores the original value of `nptr` in
`*endptr` (and returns 0). In particular, if `*nptr` is
not '\0' but `**endptr` is '\0' on return, the entire string is
valid.

The [strtoll](https://manual.cs50.io/3/strtoll)() function works just like the
[strtol](https://manual.cs50.io/3/strtol)() function but returns a `long long`
integer value.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strtol#return-value)

The [strtol](https://manual.cs50.io/3/strtol)() function returns the result of the
conversion, unless the value would underflow or overflow. If an
underflow occurs, [strtol](https://manual.cs50.io/3/strtol)() returns
**LONG_MIN**. If an overflow occurs,
[strtol](https://manual.cs50.io/3/strtol)() returns **LONG_MAX**. In both
cases, `errno` is set to **ERANGE**. Precisely the
same holds for [strtoll](https://manual.cs50.io/3/strtoll)() (with
**LLONG_MIN** and **LLONG_MAX** instead of
**LONG_MIN** and **LONG_MAX**).

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/strtol#examples)

The program shown below demonstrates the use of
[strtol](https://manual.cs50.io/3/strtol)(). The first command-line argument specifies a
string from which [strtol](https://manual.cs50.io/3/strtol)() should parse a number. The
second (optional) argument specifies the base to be used for the
conversion. (This argument is converted to numeric form using
[atoi](https://manual.cs50.io/3/atoi)(3), a function that performs no error checking and
has a simpler interface than [strtol](https://manual.cs50.io/3/strtol)().) Some examples
of the results produced by this program are the following:

```
$ ./a.out 123
strtol() returned 123
$ ./a.out ' 123'
strtol() returned 123
$ ./a.out 123abc
strtol() returned 123
Further characters after number: "abc"
$ ./a.out 123abc 55
strtol: Invalid argument
$ ./a.out ''
No digits were found
$ ./a.out 4000000000
strtol: Numerical result out of range
```

<a id="program-source"></a>

#### Program source

```
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
int
main(int argc, char *argv[])
{
    int base;
    char *endptr, *str;
    long val;
    if (argc < 2) {
        fprintf(stderr, "Usage: %s str [base]\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    str = argv[1];
    base = (argc > 2) ? atoi(argv[2]) : 0;
    errno = 0;    /* To distinguish success/failure after call */
    strtol("0", NULL, base);
    if (errno == EINVAL) {
        perror("strtol");
        exit(EXIT_FAILURE);
    }
    errno = 0;    /* To distinguish success/failure after call */
    val = strtol(str, &endptr, base);
    /* Check for various possible errors. */
    if (errno == ERANGE) {
        perror("strtol");
        exit(EXIT_FAILURE);
    }
    if (endptr == str) {
        fprintf(stderr, "No digits were found\n");
        exit(EXIT_FAILURE);
    }
    /* If we got here, strtol() successfully parsed a number. */
    printf("strtol() returned %ld\n", val);
    if (*endptr != '\0')        /* Not necessarily an error... */
        printf("Further characters after number: \"%s\"\n", endptr);
    exit(EXIT_SUCCESS);
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/strtol#errors)

This function does not modify `errno` on success.

**EINVAL**
:   (not in C99) The given `base` contains an unsupported
    value.

**ERANGE**
:   The resulting value was out of range.

The implementation may also set `errno` to
**EINVAL** in case no conversion was performed (no digits
seen, and 0 returned).

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strtol#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strtol](https://manual.cs50.io/3/strtol)(), [strtoll](https://manual.cs50.io/3/strtoll)(), [strtoq](https://manual.cs50.io/3/strtoq)() | Thread safety | MT-Safe locale |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strtol#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strtol#history)

[strtol](https://manual.cs50.io/3/strtol)()
:   POSIX.1-2001, C89, SVr4, 4.3BSD.

[strtoll](https://manual.cs50.io/3/strtoll)()
:   POSIX.1-2001, C99.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/strtol#notes)

Since [strtol](https://manual.cs50.io/3/strtol)() can legitimately return 0,
**LONG_MAX**, or **LONG_MIN**
(**LLONG_MAX** or **LLONG_MIN** for
[strtoll](https://manual.cs50.io/3/strtoll)()) on both success and failure, the calling
program should set `errno` to 0 before the call, and then
determine if an error occurred by checking whether *errno ==
ERANGE* after the call.

According to POSIX.1, in locales other than "C" and "POSIX", these
functions may accept other, implementation-defined numeric strings.

BSD also has

```
quad_t strtoq(const char *nptr, char **endptr, int base);
```

with completely analogous definition. Depending on the wordsize of
the current architecture, this may be equivalent to
[strtoll](https://manual.cs50.io/3/strtoll)() or to [strtol](https://manual.cs50.io/3/strtol)().

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/strtol#caveats)

If the `base` needs to be tested, it should be tested in a
call where the string is known to succeed. Otherwise, it's impossible to
portably differentiate the errors.

```
errno = 0;
strtol("0", NULL, base);
if (errno == EINVAL)
    goto unsupported_base;
```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strtol#see-also)

[atof](https://manual.cs50.io/3/atof)(3), [atoi](https://manual.cs50.io/3/atoi)(3),
[atol](https://manual.cs50.io/3/atol)(3), [strtod](https://manual.cs50.io/3/strtod)(3),
[strtoimax](https://manual.cs50.io/3/strtoimax)(3), [strtoul](https://manual.cs50.io/3/strtoul)(3)

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
- https://manual.cs50.io/3/strtol — retrieved 2026-10-18T05:45:30+03:30, sha256 `ec2fc1950b0becdd…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
