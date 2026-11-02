---
id: manual-sleep
type: reference
title: sleep(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/sleep
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:14+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- sleep
checksum: sha256:4e45e6a3d93bc7b344f3ff07cc29a37abfb1ce21a659a60b720153ef01cb856f
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# sleep(3) — CS50 manual page

## 1. Source metadata
- **Title:** sleep(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/sleep>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:14+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/sleep> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/sleep#name)

sleep - sleep for a specified number of seconds

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/sleep#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/sleep#synopsis)

```
#include <unistd.h>
unsigned int sleep(unsigned int seconds);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/sleep#description)

[sleep](https://manual.cs50.io/3/sleep)() causes the calling thread to sleep either
until the number of real-time seconds specified in `seconds` have
elapsed or until a signal arrives which is not ignored.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/sleep#return-value)

Zero if the requested time has elapsed, or the number of seconds left
to sleep, if the call was interrupted by a signal handler.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/sleep#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [sleep](https://manual.cs50.io/3/sleep)() | Thread safety | MT-Unsafe sig:SIGCHLD/linux |

<a id="versions"></a>

### [VERSIONS](https://manual.cs50.io/3/sleep#versions)

On Linux, [sleep](https://manual.cs50.io/3/sleep)() is implemented via
[nanosleep](https://manual.cs50.io/2/nanosleep)(2). See the [nanosleep](https://manual.cs50.io/2/nanosleep)(2) man
page for a discussion of the clock used.

On some systems, [sleep](https://manual.cs50.io/3/sleep)() may be implemented using
[alarm](https://manual.cs50.io/2/alarm)(2) and **SIGALRM** (POSIX.1 permits
this); mixing calls to [alarm](https://manual.cs50.io/2/alarm)(2) and
[sleep](https://manual.cs50.io/3/sleep)() is a bad idea.

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/sleep#standards)

POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/sleep#history)

POSIX.1-2001.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/sleep#caveats)

Using [longjmp](https://manual.cs50.io/3/longjmp)(3) from a signal handler or modifying
the handling of **SIGALRM** while sleeping will cause
undefined results.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/sleep#see-also)

[sleep](https://manual.cs50.io/1/sleep)(1), [alarm](https://manual.cs50.io/2/alarm)(2),
[nanosleep](https://manual.cs50.io/2/nanosleep)(2), [signal](https://manual.cs50.io/2/signal)(2),
[signal](https://manual.cs50.io/7/signal)(7)

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
- https://manual.cs50.io/3/sleep — retrieved 2026-10-18T05:46:14+03:30, sha256 `4e45e6a3d93bc7b3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
