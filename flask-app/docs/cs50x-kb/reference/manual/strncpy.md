---
id: manual-strncpy
type: reference
title: strncpy(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strncpy
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:14+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strncpy
checksum: sha256:5a137f3ce9ea40956fc1a490eb06ff9fd9346fd5526427ced53689233c775e72
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strncpy(3) — CS50 manual page

## 1. Source metadata
- **Title:** strncpy(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strncpy>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:14+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strncpy> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strncpy#name)

stpncpy, strncpy - fill a fixed-size buffer with non-null bytes from
a string, padding with null bytes as needed

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strncpy#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strncpy#synopsis)

```
#include <string.h>
char *strncpy(char dst[restrict .dsize], const char *restrict src,
 size_t dsize);
char *stpncpy(char dst[restrict .dsize], const char *restrict src,
 size_t dsize);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[stpncpy](https://manual.cs50.io/3/stpncpy)():

```
    Since glibc 2.10:
        _POSIX_C_SOURCE >= 200809L
    Before glibc 2.10:
        _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strncpy#description)

These functions copy non-null bytes from the string pointed to by
`src` into the array pointed to by `dst`. If the source
has too few non-null bytes to fill the destination, the functions pad
the destination with trailing null bytes. If the destination buffer,
limited by its size, isn't large enough to hold the copy, the resulting
character sequence is truncated. For the difference between the two
functions, see RETURN VALUE.

An implementation of these functions might be:

```
char *
strncpy(char *restrict dst, const char *restrict src, size_t dsize)
{
    stpncpy(dst, src, dsize);
    return dst;
}
char *
stpncpy(char *restrict dst, const char *restrict src, size_t dsize)
{
    size_t  dlen;
    dlen = strnlen(src, dsize);
    return memset(mempcpy(dst, src, dlen), 0, dsize - dlen);
}
```

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strncpy#return-value)

[strncpy](https://manual.cs50.io/3/strncpy)()
:   returns `dst`.

[stpncpy](https://manual.cs50.io/3/stpncpy)()
:   returns a pointer to one after the last character in the destination
    character sequence.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/strncpy#examples)

```
#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int
main(void)
{
    char    *p;
    char    buf1[20];
    char    buf2[20];
    size_t  len;
    if (sizeof(buf2) < strlen("Hello world!"))
        errx("strncpy: truncating character sequence");
    strncpy(buf2, "Hello world!", sizeof(buf2));
    len = strnlen(buf2, sizeof(buf2));
    printf("[len = %zu]: ", len);
    fwrite(buf2, 1, len, stdout);
    putchar('\n');
    if (sizeof(buf1) < strlen("Hello world!"))
        errx("stpncpy: truncating character sequence");
    p = stpncpy(buf1, "Hello world!", sizeof(buf1));
    len = p - buf1;
    printf("[len = %zu]: ", len);
    fwrite(buf1, 1, len, stdout);
    putchar('\n');
    exit(EXIT_SUCCESS);
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strncpy#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [stpncpy](https://manual.cs50.io/3/stpncpy)(), [strncpy](https://manual.cs50.io/3/strncpy)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strncpy#standards)

[strncpy](https://manual.cs50.io/3/strncpy)()
:   C11, POSIX.1-2008.

[stpncpy](https://manual.cs50.io/3/stpncpy)()
:   POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strncpy#history)

[strncpy](https://manual.cs50.io/3/strncpy)()
:   C89, POSIX.1-2001, SVr4, 4.3BSD.

[stpncpy](https://manual.cs50.io/3/stpncpy)()
:   glibc 1.07. POSIX.1-2008.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/strncpy#caveats)

The name of these functions is confusing. These functions produce a
null-padded character sequence, not a string (see
[string_copying](https://manual.cs50.io/7/string_copying)(7)). For example:

```
strncpy(buf, "1", 5);       // { '1',   0,   0,   0,   0 }
strncpy(buf, "1234", 5);    // { '1', '2', '3', '4',   0 }
strncpy(buf, "12345", 5);   // { '1', '2', '3', '4', '5' }
strncpy(buf, "123456", 5);  // { '1', '2', '3', '4', '5' }
```

It's impossible to distinguish truncation by the result of the call,
from a character sequence that just fits the destination buffer;
truncation should be detected by comparing the length of the input
string with the size of the destination buffer.

If you're going to use this function in chained calls, it would be
useful to develop a similar function that accepts a pointer to the end
(one after the last element) of the destination buffer instead of its
size.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strncpy#see-also)

[wcpncpy](https://manual.cs50.io/3/wcpncpy)(3), [string_copying](https://manual.cs50.io/7/string_copying)(7)

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
- https://manual.cs50.io/3/strncpy — retrieved 2026-10-18T05:45:14+03:30, sha256 `5a137f3ce9ea4095…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
