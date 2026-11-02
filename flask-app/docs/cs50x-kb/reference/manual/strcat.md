---
id: manual-strcat
type: reference
title: strcat(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strcat
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:15+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strcat
checksum: sha256:99f9732b6f55c54d4f278044f4a7724f5b74664d43e5cd5e628fe2f83c864193
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strcat(3) — CS50 manual page

## 1. Source metadata
- **Title:** strcat(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strcat>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:15+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strcat> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strcat#name)

stpcpy, strcpy, strcat - copy or catenate a string

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strcat#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strcat#synopsis)

```
#include <string.h>
char *stpcpy(char *restrict dst, const char *restrict src);
char *strcpy(char *restrict dst, const char *restrict src);
char *strcat(char *restrict dst, const char *restrict src);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[stpcpy](https://manual.cs50.io/3/stpcpy)():

```
    Since glibc 2.10:
        _POSIX_C_SOURCE >= 200809L
    Before glibc 2.10:
        _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strcat#description)

[stpcpy](https://manual.cs50.io/3/stpcpy)() [strcpy](https://manual.cs50.io/3/strcpy)()
:   These functions copy the string pointed to by `src`, into a
    string at the buffer pointed to by `dst`. The programmer is
    responsible for allocating a destination buffer large enough, that is,
    `strlen(src) + 1`. For the difference between the two functions,
    see RETURN VALUE.

[strcat](https://manual.cs50.io/3/strcat)()
:   This function catenates the string pointed to by `src`, after
    the string pointed to by `dst` (overwriting its terminating null
    byte). The programmer is responsible for allocating a destination buffer
    large enough, that is, `strlen(dst) + strlen(src) + 1`.

An implementation of these functions might be:

```
char *
stpcpy(char *restrict dst, const char *restrict src)
{
    char  *p;
    p = mempcpy(dst, src, strlen(src));
    *p = '\0';
    return p;
}
char *
strcpy(char *restrict dst, const char *restrict src)
{
    stpcpy(dst, src);
    return dst;
}
char *
strcat(char *restrict dst, const char *restrict src)
{
    stpcpy(dst + strlen(dst), src);
    return dst;
}
```

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strcat#return-value)

[stpcpy](https://manual.cs50.io/3/stpcpy)()
:   This function returns a pointer to the terminating null byte of the
    copied string.

[strcpy](https://manual.cs50.io/3/strcpy)() [strcat](https://manual.cs50.io/3/strcat)()
:   These functions return `dst`.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/strcat#examples)

```
#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int
main(void)
{
    char    *p;
    char    *buf1;
    char    *buf2;
    size_t  len, maxsize;
    maxsize = strlen("Hello ") + strlen("world") + strlen("!") + 1;
    buf1 = malloc(sizeof(*buf1) * maxsize);
    if (buf1 == NULL)
        err(EXIT_FAILURE, "malloc()");
    buf2 = malloc(sizeof(*buf2) * maxsize);
    if (buf2 == NULL)
        err(EXIT_FAILURE, "malloc()");
    p = buf1;
    p = stpcpy(p, "Hello ");
    p = stpcpy(p, "world");
    p = stpcpy(p, "!");
    len = p - buf1;
    printf("[len = %zu]: ", len);
    puts(buf1);  // "Hello world!"
    free(buf1);
    strcpy(buf2, "Hello ");
    strcat(buf2, "world");
    strcat(buf2, "!");
    len = strlen(buf2);
    printf("[len = %zu]: ", len);
    puts(buf2);  // "Hello world!"
    free(buf2);
    exit(EXIT_SUCCESS);
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strcat#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [stpcpy](https://manual.cs50.io/3/stpcpy)(), [strcpy](https://manual.cs50.io/3/strcpy)(), [strcat](https://manual.cs50.io/3/strcat)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strcat#standards)

[stpcpy](https://manual.cs50.io/3/stpcpy)()
:   POSIX.1-2008.

[strcpy](https://manual.cs50.io/3/strcpy)() [strcat](https://manual.cs50.io/3/strcat)()
:   POSIX.1-2001, C89, SVr4, 4.3BSD.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/strcat#caveats)

The strings `src` and `dst` may not overlap.

If the destination buffer is not large enough, the behavior is
undefined. See **_FORTIFY_SOURCE** in
[feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7).

[strcat](https://manual.cs50.io/3/strcat)() can be very inefficient. Read about [https://www.joelonsoftware.com/2001/12/11/back-to-basics/](https://manual.cs50.io/3/<a href=)">Shlemiel
the painter.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strcat#see-also)

[strdup](https://manual.cs50.io/3/strdup)(3), [string](https://manual.cs50.io/3/string)(3),
[wcscpy](https://manual.cs50.io/3/wcscpy)(3), [string_copying](https://manual.cs50.io/7/string_copying)(7)

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
- https://manual.cs50.io/3/strcat — retrieved 2026-10-18T05:45:15+03:30, sha256 `99f9732b6f55c54d…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
