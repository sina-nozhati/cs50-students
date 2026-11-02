---
id: manual-memcpy
type: reference
title: memcpy(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/memcpy
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:07+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- memcpy
checksum: sha256:cb270dac70dd433e4515f11e2feb138c73a02b360e3df90380813af1e62c1d31
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# memcpy(3) — CS50 manual page

## 1. Source metadata
- **Title:** memcpy(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/memcpy>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:07+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/memcpy> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/memcpy#name)

memcpy - copy memory area

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/memcpy#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/memcpy#synopsis)

```
#include <string.h>
void *memcpy(void dest[restrict .n], const void src[restrict .n],
 size_t n);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/memcpy#description)

The [memcpy](https://manual.cs50.io/3/memcpy)() function copies `n` bytes from
memory area `src` to memory area `dest`. The memory areas
must not overlap. Use [memmove](https://manual.cs50.io/3/memmove)(3) if the memory areas do
overlap.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/memcpy#return-value)

The [memcpy](https://manual.cs50.io/3/memcpy)() function returns a pointer to
`dest`.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/memcpy#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [memcpy](https://manual.cs50.io/3/memcpy)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/memcpy#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/memcpy#history)

POSIX.1-2001, C89, SVr4, 4.3BSD.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/memcpy#caveats)

Failure to observe the requirement that the memory areas do not
overlap has been the source of significant bugs. (POSIX and the C
standards are explicit that employing [memcpy](https://manual.cs50.io/3/memcpy)() with
overlapping areas produces undefined behavior.) Most notably, in glibc
2.13 a performance optimization of [memcpy](https://manual.cs50.io/3/memcpy)() on some
platforms (including x86-64) included changing the order in which bytes
were copied from `src` to `dest`.

This change revealed breakages in a number of applications that
performed copying with overlapping areas. Under the previous
implementation, the order in which the bytes were copied had
fortuitously hidden the bug, which was revealed when the copying order
was reversed. In glibc 2.14, a versioned symbol was added so that old
binaries (i.e., those linked against glibc versions earlier than 2.14)
employed a [memcpy](https://manual.cs50.io/3/memcpy)() implementation that safely handles
the overlapping buffers case (by providing an "older"
[memcpy](https://manual.cs50.io/3/memcpy)() implementation that was aliased to
[memmove](https://manual.cs50.io/3/memmove)(3)).

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/memcpy#see-also)

[bcopy](https://manual.cs50.io/3/bcopy)(3), [bstring](https://manual.cs50.io/3/bstring)(3),
[memccpy](https://manual.cs50.io/3/memccpy)(3), [memmove](https://manual.cs50.io/3/memmove)(3),
[mempcpy](https://manual.cs50.io/3/mempcpy)(3), [strcpy](https://manual.cs50.io/3/strcpy)(3),
[strncpy](https://manual.cs50.io/3/strncpy)(3), [wmemcpy](https://manual.cs50.io/3/wmemcpy)(3)

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
- https://manual.cs50.io/3/memcpy — retrieved 2026-10-18T05:46:07+03:30, sha256 `cb270dac70dd433e…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
