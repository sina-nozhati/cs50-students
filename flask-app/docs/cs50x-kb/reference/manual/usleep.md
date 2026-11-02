---
id: manual-usleep
type: reference
title: usleep(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/usleep
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:15+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- usleep
checksum: sha256:1ce683cbd0665c356f4d47a5c0bebfd58585496ce8543f003c47cdcc910d92e0
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# usleep(3) — CS50 manual page

## 1. Source metadata
- **Title:** usleep(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/usleep>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:15+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/usleep> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/usleep#name)

usleep - suspend execution for microsecond intervals

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/usleep#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/usleep#synopsis)

```
#include <unistd.h>
int usleep(useconds_t usec);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[usleep](https://manual.cs50.io/3/usleep)():

```
    Since glibc 2.12:
        (_XOPEN_SOURCE >= 500) && ! (_POSIX_C_SOURCE >= 200809L)
            || /* glibc >= 2.19: */ _DEFAULT_SOURCE
            || /* glibc <= 2.19: */ _BSD_SOURCE
    Before glibc 2.12:
        _BSD_SOURCE || _XOPEN_SOURCE >= 500
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/usleep#description)

The [usleep](https://manual.cs50.io/3/usleep)() function suspends execution of the
calling thread for (at least) `usec` microseconds. The sleep may
be lengthened slightly by any system activity or by the time spent
processing the call or by the granularity of system timers.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/usleep#return-value)

The [usleep](https://manual.cs50.io/3/usleep)() function returns 0 on success. On
error, -1 is returned, with `errno` set to indicate the
error.

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/usleep#errors)

**EINTR**
:   Interrupted by a signal; see [signal](https://manual.cs50.io/7/signal)(7).

**EINVAL**
:   `usec` is greater than or equal to 1000000. (On systems where
    that is considered an error.)

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/usleep#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [usleep](https://manual.cs50.io/3/usleep)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/usleep#standards)

None.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/usleep#history)

4.3BSD, POSIX.1-2001. POSIX.1-2001 declares it obsolete, suggesting
[nanosleep](https://manual.cs50.io/2/nanosleep)(2) instead. Removed in POSIX.1-2008.

On the original BSD implementation, and before glibc 2.2.2, the
return type of this function is `void`. The POSIX version returns
`int`, and this is also the prototype used since glibc 2.2.2.

Only the **EINVAL** error return is documented by SUSv2
and POSIX.1-2001.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/usleep#caveats)

The interaction of this function with the **SIGALRM**
signal, and with other timer functions such as
[alarm](https://manual.cs50.io/2/alarm)(2), [sleep](https://manual.cs50.io/3/sleep)(3),
[nanosleep](https://manual.cs50.io/2/nanosleep)(2), [setitimer](https://manual.cs50.io/2/setitimer)(2),
[timer_create](https://manual.cs50.io/2/timer_create)(2), [timer_delete](https://manual.cs50.io/2/timer_delete)(2),
[timer_getoverrun](https://manual.cs50.io/2/timer_getoverrun)(2), [timer_gettime](https://manual.cs50.io/2/timer_gettime)(2),
[timer_settime](https://manual.cs50.io/2/timer_settime)(2), [ualarm](https://manual.cs50.io/3/ualarm)(3) is
unspecified.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/usleep#see-also)

[alarm](https://manual.cs50.io/2/alarm)(2), [getitimer](https://manual.cs50.io/2/getitimer)(2),
[nanosleep](https://manual.cs50.io/2/nanosleep)(2), [select](https://manual.cs50.io/2/select)(2),
[setitimer](https://manual.cs50.io/2/setitimer)(2), [sleep](https://manual.cs50.io/3/sleep)(3),
[ualarm](https://manual.cs50.io/3/ualarm)(3), **useconds_t**(3type),
[time](https://manual.cs50.io/7/time)(7)

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
- https://manual.cs50.io/3/usleep — retrieved 2026-10-18T05:46:15+03:30, sha256 `1ce683cbd0665c35…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
