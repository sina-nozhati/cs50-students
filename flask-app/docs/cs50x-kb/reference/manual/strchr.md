---
id: manual-strchr
type: reference
title: strchr(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strchr
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:10+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strchr
checksum: sha256:877f13d7c9c22824922674642ea1571417224aba4490ca41e4433f6225fbe0c5
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strchr(3) — CS50 manual page

## 1. Source metadata
- **Title:** strchr(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strchr>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:10+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strchr> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strchr#name)

strchr, strrchr, strchrnul - locate character in string

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strchr#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strchr#synopsis)

```
#include <string.h>
char *strchr(const char *s, int c);
char *strrchr(const char *s, int c);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include <string.h>
char *strchrnul(const char *s, int c);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strchr#description)

The [strchr](https://manual.cs50.io/3/strchr)() function returns a pointer to the first
occurrence of the character `c` in the string `s`.

The [strrchr](https://manual.cs50.io/3/strrchr)() function returns a pointer to the last
occurrence of the character `c` in the string `s`.

The [strchrnul](https://manual.cs50.io/3/strchrnul)() function is like
[strchr](https://manual.cs50.io/3/strchr)() except that if `c` is not found in
`s`, then it returns a pointer to the null byte at the end of
`s`, rather than NULL.

Here "character" means "byte"; these functions do not work with wide
or multibyte characters.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strchr#return-value)

The [strchr](https://manual.cs50.io/3/strchr)() and [strrchr](https://manual.cs50.io/3/strrchr)()
functions return a pointer to the matched character or NULL if the
character is not found. The terminating null byte is considered part of
the string, so that if `c` is specified as '\0', these functions
return a pointer to the terminator.

The [strchrnul](https://manual.cs50.io/3/strchrnul)() function returns a pointer to the
matched character, or a pointer to the null byte at the end of
`s` (i.e., `s+strlen(s)`) if the character is not
found.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strchr#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strchr](https://manual.cs50.io/3/strchr)(), [strrchr](https://manual.cs50.io/3/strrchr)(), [strchrnul](https://manual.cs50.io/3/strchrnul)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strchr#standards)

[strchr](https://manual.cs50.io/3/strchr)() [strrchr](https://manual.cs50.io/3/strrchr)()
:   C11, POSIX.1-2008.

[strchrnul](https://manual.cs50.io/3/strchrnul)()
:   GNU.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strchr#history)

[strchr](https://manual.cs50.io/3/strchr)() [strrchr](https://manual.cs50.io/3/strrchr)()
:   POSIX.1-2001, C89, SVr4, 4.3BSD.

[strchrnul](https://manual.cs50.io/3/strchrnul)()
:   glibc 2.1.1.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strchr#see-also)

[memchr](https://manual.cs50.io/3/memchr)(3), [string](https://manual.cs50.io/3/string)(3),
[strlen](https://manual.cs50.io/3/strlen)(3), [strpbrk](https://manual.cs50.io/3/strpbrk)(3),
[strsep](https://manual.cs50.io/3/strsep)(3), [strspn](https://manual.cs50.io/3/strspn)(3),
[strstr](https://manual.cs50.io/3/strstr)(3), [strtok](https://manual.cs50.io/3/strtok)(3),
[wcschr](https://manual.cs50.io/3/wcschr)(3), [wcsrchr](https://manual.cs50.io/3/wcsrchr)(3)

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
- https://manual.cs50.io/3/strchr — retrieved 2026-10-18T05:46:10+03:30, sha256 `877f13d7c9c22824…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
