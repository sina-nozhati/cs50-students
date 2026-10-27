---
id: manual-fclose
type: reference
title: fclose(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/fclose
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:50+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- fclose
- manual
checksum: sha256:f42e07844f414cd07c328781c4e488ac1ef66785702c1259437cf915f4fa7325
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# fclose(3) — CS50 manual page

## 1. Source metadata
- **Title:** fclose(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/fclose>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:50+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/fclose> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/fclose#name)

fclose - close a file

fclose - close a stream

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/fclose#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/fclose#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdio.h>
```

<a id="prototype"></a>

#### Prototype

```c
int fclose(FILE *stream);
```

```
#include <stdio.h>
int fclose(FILE *stream);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/fclose#description)

This function closes a file that has been opened via [fopen](https://manual.cs50.io/3/fopen). It expects as input the pointer to a `FILE` that was returned by [fopen](https://manual.cs50.io/3/fopen).

The [fclose](https://manual.cs50.io/3/fclose)() function flushes the stream pointed to
by `stream` (writing any buffered output data using
[fflush](https://manual.cs50.io/3/fflush)(3)) and closes the underlying file
descriptor.

The behaviour of [fclose](https://manual.cs50.io/3/fclose)() is undefined if the
`stream` parameter is an illegal pointer, or is a descriptor
already passed to a previous invocation of
[fclose](https://manual.cs50.io/3/fclose)().

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/fclose#return-value)

This function returns `0` if successful and `EOF`, a constant, in cases of error.

Upon successful completion, 0 is returned. Otherwise,
**EOF** is returned and `errno` is set to indicate
the error. In either case, any further access (including another call to
[fclose](https://manual.cs50.io/3/fclose)()) to the stream results in undefined
behavior.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/fclose#example)

```c
#inclue <stdio.h>  

int main(void)
{
    FILE *file = fopen("cs50.txt", "w");
    if (file != NULL)
    {
        fprintf(file, "This is CS50\n");
        fclose(file);
    }
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/fclose#errors)

**EBADF**
:   The file descriptor underlying `stream` is not valid.

The [fclose](https://manual.cs50.io/3/fclose)() function may also fail and set
`errno` for any of the errors specified for the routines
[close](https://manual.cs50.io/2/close)(2), [write](https://manual.cs50.io/2/write)(2), or
[fflush](https://manual.cs50.io/3/fflush)(3).

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/fclose#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [fclose](https://manual.cs50.io/3/fclose)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/fclose#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/fclose#history)

C89, POSIX.1-2001.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/fclose#notes)

Note that [fclose](https://manual.cs50.io/3/fclose)() flushes only the user-space
buffers provided by the C library. To ensure that the data is physically
stored on disk the kernel buffers must be flushed too, for example, with
[sync](https://manual.cs50.io/2/sync)(2) or [fsync](https://manual.cs50.io/2/fsync)(2).

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/fclose#see-also)

[close](https://manual.cs50.io/2/close)(2), [fcloseall](https://manual.cs50.io/3/fcloseall)(3),
[fflush](https://manual.cs50.io/3/fflush)(3), [fileno](https://manual.cs50.io/3/fileno)(3),
[fopen](https://manual.cs50.io/3/fopen)(3), [setbuf](https://manual.cs50.io/3/setbuf)(3)

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
- https://manual.cs50.io/3/fclose — retrieved 2026-10-18T05:45:50+03:30, sha256 `f42e07844f414cd0…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
