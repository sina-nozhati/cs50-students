---
id: manual-exit
type: reference
title: exit(2) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/2/exit
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:44+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- exit
- manual
checksum: sha256:100c4713394a0b89859727201fbbf853dd1213cd4e4809e5fa1ab403c977b03c
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# exit(2) — CS50 manual page

## 1. Source metadata
- **Title:** exit(2) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/2/exit>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:44+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/2/exit> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/2/exit#name)

_exit, _Exit - terminate the calling process

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/2/exit#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/2/exit#synopsis)

```
#include <unistd.h>
[[noreturn]] void _exit(int status);
#include <stdlib.h>
[[noreturn]] void _Exit(int status);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[_Exit](https://manual.cs50.io/2/_Exit)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/2/exit#description)

[_exit](https://manual.cs50.io/2/_exit)() terminates the calling process
"immediately". Any open file descriptors belonging to the process are
closed. Any children of the process are inherited by
[init](https://manual.cs50.io/1/init)(1) (or by the nearest "subreaper" process as
defined through the use of the [prctl](https://manual.cs50.io/2/prctl)(2)
**PR_SET_CHILD_SUBREAPER** operation). The process's parent
is sent a **SIGCHLD** signal.

The value `status & 0xFF` is returned to the parent
process as the process's exit status, and can be collected by the parent
using one of the [wait](https://manual.cs50.io/2/wait)(2) family of calls.

The function [_Exit](https://manual.cs50.io/2/_Exit)() is equivalent to
[_exit](https://manual.cs50.io/2/_exit)().

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/2/exit#return-value)

These functions do not return.

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/2/exit#standards)

[_exit](https://manual.cs50.io/2/_exit)()
:   POSIX.1-2008.

[_Exit](https://manual.cs50.io/2/_Exit)()
:   C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/2/exit#history)

POSIX.1-2001, SVr4, 4.3BSD.

[_Exit](https://manual.cs50.io/2/_Exit)() was introduced by C99.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/2/exit#notes)

For a discussion on the effects of an exit, the transmission of exit
status, zombie processes, signals sent, and so on, see
[exit](https://manual.cs50.io/3/exit)(3).

The function [_exit](https://manual.cs50.io/2/_exit)() is like
[exit](https://manual.cs50.io/3/exit)(3), but does not call any functions registered
with [atexit](https://manual.cs50.io/3/atexit)(3) or [on_exit](https://manual.cs50.io/3/on_exit)(3). Open
[stdio](https://manual.cs50.io/3/stdio)(3) streams are not flushed. On the other hand,
[_exit](https://manual.cs50.io/2/_exit)() does close open file descriptors, and this may
cause an unknown delay, waiting for pending output to finish. If the
delay is undesired, it may be useful to call functions like
[tcflush](https://manual.cs50.io/3/tcflush)(3) before calling [_exit](https://manual.cs50.io/2/_exit)().
Whether any pending I/O is canceled, and which pending I/O may be
canceled upon [_exit](https://manual.cs50.io/2/_exit)(), is implementation-dependent.

<a id="c-librarykernel-differences"></a>

#### C library/kernel differences

The text above in DESCRIPTION describes the traditional effect of
[_exit](https://manual.cs50.io/2/_exit)(), which is to terminate a process, and these are
the semantics specified by POSIX.1 and implemented by the C library
wrapper function. On modern systems, this means termination of all
threads in the process.

By contrast with the C library wrapper function, the raw Linux
[_exit](https://manual.cs50.io/2/_exit)() system call terminates only the calling thread,
and actions such as reparenting child processes or sending
**SIGCHLD** to the parent process are performed only if
this is the last thread in the thread group.

Up to glibc 2.3, the [_exit](https://manual.cs50.io/2/_exit)() wrapper function
invoked the kernel system call of the same name. Since glibc 2.3, the
wrapper function invokes [exit_group](https://manual.cs50.io/2/exit_group)(2), in order to
terminate all of the threads in a process.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/2/exit#see-also)

[execve](https://manual.cs50.io/2/execve)(2), [exit_group](https://manual.cs50.io/2/exit_group)(2),
[fork](https://manual.cs50.io/2/fork)(2), [kill](https://manual.cs50.io/2/kill)(2),
[wait](https://manual.cs50.io/2/wait)(2), [wait4](https://manual.cs50.io/2/wait4)(2),
[waitpid](https://manual.cs50.io/2/waitpid)(2), [atexit](https://manual.cs50.io/3/atexit)(3),
[exit](https://manual.cs50.io/3/exit)(3), [on_exit](https://manual.cs50.io/3/on_exit)(3),
[termios](https://manual.cs50.io/3/termios)(3)

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
- https://manual.cs50.io/2/exit — retrieved 2026-10-18T05:45:44+03:30, sha256 `100c4713394a0b89…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
