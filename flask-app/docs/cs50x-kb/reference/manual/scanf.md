---
id: manual-scanf
type: reference
title: scanf(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/scanf
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:03+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- scanf
checksum: sha256:3b0bd8bcb617e9b9d5b9c713f1d9a6f5f3a874290d2ed690135061e02563ecee
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# scanf(3) — CS50 manual page

## 1. Source metadata
- **Title:** scanf(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/scanf>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:03+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/scanf> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/scanf#name)

scanf - get input from a user

scanf, fscanf, vscanf, vfscanf - input FILE format conversion

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/scanf#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/scanf#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdio.h>
```

<a id="prototype"></a>

#### Prototype

```c
int scanf(const char *format, ...);
```

Note that `...` represents zero or more additional arguments.

```
#include <stdio.h>
int scanf(const char *restrict format, ...);
int fscanf(FILE *restrict stream,
 const char *restrict format, ...);
#include <stdarg.h>
int vscanf(const char *restrict format, va_list ap);
int vfscanf(FILE *restrict stream,
 const char *restrict format, va_list ap);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[vscanf](https://manual.cs50.io/3/vscanf)(), [vfscanf](https://manual.cs50.io/3/vfscanf)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/scanf#description)

This function “scans” input from a user’s keyboard for values of specified types. It expects as input a “format string” that specifies what to expect and zero or more subsequent arguments, each of which should be a location in memory. The format string should typically contain “conversion specifications,” placeholders that begin with `%` that specify what types of values to expect. Subsequent arguments will be assigned those values. For instance, if `n` is a `int`, this function can get an `int` from a user using `%i`:

```c
scanf("%i", &n);
```

Among this function’s supported conversion specifications are:

| Conversion Specification | Type |
| --- | --- |
| `%c` | `char` |
| `%lf` | `double` |
| `%f` | `float` |
| `%i` | `int` |
| `%li` | `long` |

It is not safe to use this function to get a string from a user using `%s`, as the user’s input might exceed the capacity of the argument that would be assigned that value.

The [scanf](https://manual.cs50.io/3/scanf)() family of functions scans formatted
input like [sscanf](https://manual.cs50.io/3/sscanf)(3), but read from a `FILE`. It
is very difficult to use these functions correctly, and it is preferable
to read entire lines with [fgets](https://manual.cs50.io/3/fgets)(3) or
[getline](https://manual.cs50.io/3/getline)(3) and parse them later with
[sscanf](https://manual.cs50.io/3/sscanf)(3) or more specialized functions such as
[strtol](https://manual.cs50.io/3/strtol)(3).

The [scanf](https://manual.cs50.io/3/scanf)() function reads input from the standard
input stream `stdin` and [fscanf](https://manual.cs50.io/3/fscanf)() reads input
from the stream pointer `stream`.

The [vfscanf](https://manual.cs50.io/3/vfscanf)() function is analogous to
[vfprintf](https://manual.cs50.io/3/vfprintf)(3) and reads input from the stream pointer
`stream` using a variable argument list of pointers (see
[stdarg](https://manual.cs50.io/3/stdarg)(3). The [vscanf](https://manual.cs50.io/3/vscanf)() function is
analogous to [vprintf](https://manual.cs50.io/3/vprintf)(3) and reads from the standard
input.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/scanf#return-value)

This function returns the number of arguments that were assigned values or `EOF`, a constant defined in `stdio.h`, in cases of error.

On success, these functions return the number of input items
successfully matched and assigned; this can be fewer than provided for,
or even zero, in the event of an early matching failure.

The value **EOF** is returned if the end of input is
reached before either the first successful conversion or a matching
failure occurs. **EOF** is also returned if a read error
occurs, in which case the error indicator for the stream (see
[ferror](https://manual.cs50.io/3/ferror)(3)) is set, and `errno` is set to
indicate the error.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/scanf#examples)

```c
#include <stdio.h>  

int main(void)
{
    int i;
    printf("Input: ");
    scanf("%i", &i);
    printf("Output: %i\n", i);
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/scanf#errors)

**EAGAIN**
:   The file descriptor underlying `stream` is marked nonblocking,
    and the read operation would block.

**EBADF**
:   The file descriptor underlying `stream` is invalid, or not
    open for reading.

**EILSEQ**
:   Input byte sequence does not form a valid character.

**EINTR**
:   The read operation was interrupted by a signal; see
    [signal](https://manual.cs50.io/7/signal)(7).

**EINVAL**
:   Not enough arguments; or `format` is NULL.

**ENOMEM**
:   Out of memory.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/scanf#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [scanf](https://manual.cs50.io/3/scanf)(), [fscanf](https://manual.cs50.io/3/fscanf)(), [vscanf](https://manual.cs50.io/3/vscanf)(), [vfscanf](https://manual.cs50.io/3/vfscanf)() | Thread safety | MT-Safe locale |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/scanf#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/scanf#history)

C99, POSIX.1-2001.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/scanf#caveats)

These functions make it difficult to distinguish newlines from other
white space, This is especially problematic with line-buffered input,
like the standard input stream.

These functions can't report errors after the last non-suppressed
conversion specification.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/scanf#bugs)

It is impossible to accurately know how many characters these
functions have consumed from the input stream, since they only report
the number of successful conversions. For example, if the input is
"123\n a", `scanf("%d %d", &a, &b)` will consume the
digits, the newline, and the space, but not the letter a. This makes it
difficult to recover from invalid input.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/scanf#see-also)

[fgets](https://manual.cs50.io/3/fgets)(3), [getline](https://manual.cs50.io/3/getline)(3),
[sscanf](https://manual.cs50.io/3/sscanf)(3)

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
- https://manual.cs50.io/3/scanf — retrieved 2026-10-18T05:46:03+03:30, sha256 `3b0bd8bcb617e9b9…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
