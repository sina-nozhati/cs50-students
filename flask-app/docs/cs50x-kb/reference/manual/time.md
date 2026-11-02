---
id: manual-time
type: reference
title: time(2) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/2/time
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:43+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- time
checksum: sha256:4834b1163833e1cff38f79f652edb25d175f0ece5e445a5e18cced14960d065c
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# time(2) — CS50 manual page

## 1. Source metadata
- **Title:** time(2) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/2/time>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:43+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/2/time> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/2/time#name)

time - get time in seconds

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/2/time#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/2/time#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <time.h>
```

<a id="prototype"></a>

#### Prototype

```c
long time(NULL);
```

Think of this function as returning a `long` as output and as taking only `NULL` as input.

```
#include <time.h>
time_t time(time_t *_Nullable tloc);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/2/time#description)

This function gets the current date and time as seconds since January 1, 1970, 00:00:00 UTC, otherwise known as the Epoch.

[time](https://manual.cs50.io/2/time)() returns the time as the number of seconds
since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).

If `tloc` is non-NULL, the return value is also stored in the
memory pointed to by `tloc`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/2/time#return-value)

This function returns the number of seconds since January 1, 1970, 00:00:00 UTC.

On success, the value of time in seconds since the Epoch is returned.
On error, `((time_t) -1)` is returned, and `errno` is set
to indicate the error.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/2/time#example)

```c
#include <stdio.h>  
#include <time.h>  

int main(void)
{
    printf("The time is now %li.\n", time(NULL));
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/2/time#errors)

**EOVERFLOW**
:   The time cannot be represented as a `time_t` value. This can
    happen if an executable with 32-bit `time_t` is run on a 64-bit
    kernel when the time is 2038-01-19 03:14:08 UTC or later. However, when
    the system time is out of `time_t` range in other situations, the
    behavior is undefined.

**EFAULT**
:   `tloc` points outside your accessible address space (but see
    BUGS).

    On systems where the C library [time](https://manual.cs50.io/2/time)() wrapper
    function invokes an implementation provided by the
    [vdso](https://manual.cs50.io/7/vdso)(7) (so that there is no trap into the kernel), an
    invalid address may instead trigger a **SIGSEGV**
    signal.

<a id="versions"></a>

### [VERSIONS](https://manual.cs50.io/2/time#versions)

POSIX.1 defines `seconds since the Epoch` using a formula that
approximates the number of seconds between a specified time and the
Epoch. This formula takes account of the facts that all years that are
evenly divisible by 4 are leap years, but years that are evenly
divisible by 100 are not leap years unless they are also evenly
divisible by 400, in which case they are leap years. This value is not
the same as the actual number of seconds between the time and the Epoch,
because of leap seconds and because system clocks are not required to be
synchronized to a standard reference. Linux systems normally follow the
POSIX requirement that this value ignore leap seconds, so that
conforming systems interpret it consistently; see POSIX.1-2018 Rationale
A.4.16.

Applications intended to run after 2038 should use ABIs with
`time_t` wider than 32 bits; see
**time_t**(3type).

<a id="c-librarykernel-differences"></a>

#### C library/kernel differences

On some architectures, an implementation of [time](https://manual.cs50.io/2/time)()
is provided in the [vdso](https://manual.cs50.io/7/vdso)(7).

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/2/time#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/2/time#history)

SVr4, 4.3BSD, C89, POSIX.1-2001.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/2/time#bugs)

Error returns from this system call are indistinguishable from
successful reports that the time is a few seconds `before` the
Epoch, so the C library wrapper function never sets `errno` as a
result of this call.

The `tloc` argument is obsolescent and should always be NULL
in new code. When `tloc` is NULL, the call cannot fail.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/2/time#see-also)

[date](https://manual.cs50.io/1/date)(1), [gettimeofday](https://manual.cs50.io/2/gettimeofday)(2),
[ctime](https://manual.cs50.io/3/ctime)(3), [ftime](https://manual.cs50.io/3/ftime)(3),
[time](https://manual.cs50.io/7/time)(7), [vdso](https://manual.cs50.io/7/vdso)(7)

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
- https://manual.cs50.io/2/time — retrieved 2026-10-18T05:45:43+03:30, sha256 `4834b1163833e1cf…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
