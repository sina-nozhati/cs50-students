---
id: manual-memset
type: reference
title: memset(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/memset
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:08+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- memset
checksum: sha256:e90cba3c223ed18cfd265ebc7d393c9c1927f39789a261e6c359a3bcdc85d255
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# memset(3) — CS50 manual page

## 1. Source metadata
- **Title:** memset(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/memset>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:08+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/memset> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/memset#name)

memset - fill memory with a constant byte

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/memset#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/memset#synopsis)

```
#include <string.h>
void *memset(void s[.n], int c, size_t n);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/memset#description)

The [memset](https://manual.cs50.io/3/memset)() function fills the first `n`
bytes of the memory area pointed to by `s` with the constant byte
`c`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/memset#return-value)

The [memset](https://manual.cs50.io/3/memset)() function returns a pointer to the
memory area `s`.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/memset#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [memset](https://manual.cs50.io/3/memset)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/memset#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/memset#history)

POSIX.1-2001, C89, SVr4, 4.3BSD.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/memset#see-also)

[bstring](https://manual.cs50.io/3/bstring)(3), [bzero](https://manual.cs50.io/3/bzero)(3),
[swab](https://manual.cs50.io/3/swab)(3), [wmemset](https://manual.cs50.io/3/wmemset)(3)

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
- https://manual.cs50.io/3/memset — retrieved 2026-10-18T05:46:08+03:30, sha256 `e90cba3c223ed18c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
