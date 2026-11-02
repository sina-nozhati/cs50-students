---
id: manual-fopen
type: reference
title: fopen(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/fopen
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:49+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- fopen
- manual
checksum: sha256:de0f1fa578835381859f4ff99f80f24d1f03b56ff08aecf473bd7ae75e36e0f7
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# fopen(3) — CS50 manual page

## 1. Source metadata
- **Title:** fopen(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/fopen>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:49+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/fopen> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/fopen#name)

fopen - open a file

fopen, fdopen, freopen - stream open functions

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/fopen#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/fopen#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdio.h>
```

<a id="prototype"></a>

#### Prototype

```c
FILE *fopen(const char *pathname, const char *mode);
```

```
#include <stdio.h>
FILE *fopen(const char *restrict pathname, const char *restrict mode);
FILE *fdopen(int fd, const char *mode);
FILE *freopen(const char *restrict pathname, const char *restrict mode,
 FILE *restrict stream);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[fdopen](https://manual.cs50.io/3/fdopen)():

```
    _POSIX_C_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/fopen#description)

This function opens a file, `pathname`. Supported values for `mode` include

* `"r"`, if opening the file in order to read from it,
* `"w"`, if opening the file in order to write to it, and
* `"a"`, if opening the file in order to append to it.

The [fopen](https://manual.cs50.io/3/fopen)() function opens the file whose name is
the string pointed to by `pathname` and associates a stream with
it.

The argument `mode` points to a string beginning with one of
the following sequences (possibly followed by additional characters, as
described below):

**r**
:   Open text file for reading. The stream is positioned at the beginning
    of the file.

**r+**
:   Open for reading and writing. The stream is positioned at the
    beginning of the file.

**w**
:   Truncate file to zero length or create text file for writing. The
    stream is positioned at the beginning of the file.

**w+**
:   Open for reading and writing. The file is created if it does not
    exist, otherwise it is truncated. The stream is positioned at the
    beginning of the file.

**a**
:   Open for appending (writing at end of file). The file is created if
    it does not exist. The stream is positioned at the end of the file.

**a+**
:   Open for reading and appending (writing at end of file). The file is
    created if it does not exist. Output is always appended to the end of
    the file. POSIX is silent on what the initial read position is when
    using this mode. For glibc, the initial file position for reading is at
    the beginning of the file, but for Android/BSD/MacOS, the initial file
    position for reading is at the end of the file.

The `mode` string can also include the letter 'b' either as a
last character or as a character between the characters in any of the
two-character strings described above. This is strictly for
compatibility with ISO C and has no effect; the 'b' is ignored on all
POSIX conforming systems, including Linux. (Other systems may treat text
files and binary files differently, and adding the 'b' may be a good
idea if you do I/O to a binary file and expect that your program may be
ported to non-UNIX environments.)

See [NOTES](https://manual.cs50.io/3/fopen#notes) below for details of glibc extensions for
`mode`.

Any created file will have the mode **S_IRUSR** |
**S_IWUSR** | **S_IRGRP** |
**S_IWGRP** | **S_IROTH** |
**S_IWOTH** (0666), as modified by the process's umask
value (see [umask](https://manual.cs50.io/2/umask)(2)).

Reads and writes may be intermixed on read/write streams in any
order. Note that ANSI C requires that a file positioning function
intervene between output and input, unless an input operation encounters
end-of-file. (If this condition is not met, then a read is allowed to
return the result of writes other than the most recent.) Therefore it is
good practice (and indeed sometimes necessary under Linux) to put an
[fseek](https://manual.cs50.io/3/fseek)(3) or [fsetpos](https://manual.cs50.io/3/fsetpos)(3) operation
between write and read operations on such a stream. This operation may
be an apparent no-op (as in `fseek(..., 0L, SEEK_CUR)` called for
its synchronizing side effect).

Opening a file in append mode (**a** as the first
character of `mode`) causes all subsequent write operations to
this stream to occur at end-of-file, as if preceded by the call:

```
fseek(stream, 0, SEEK_END);
```

The file descriptor associated with the stream is opened as if by a
call to [open](https://manual.cs50.io/2/open)(2) with the following flags:

> |  |  |
> | --- | --- |
> | fopen() mode | open() flags |
> | fIrfP | O_RDONLY |
> | fIwfP | O_WRONLY | O_CREAT | O_TRUNC |
> | fIafP | O_WRONLY | O_CREAT | O_APPEND |
> | fIr+fP | O_RDWR |
> | fIw+fP | O_RDWR | O_CREAT | O_TRUNC |
> | fIa+fP | O_RDWR | O_CREAT | O_APPEND |

<a id="fdopen"></a>

#### fdopen()

The [fdopen](https://manual.cs50.io/3/fdopen)() function associates a stream with the
existing file descriptor, `fd`. The `mode` of the stream
(one of the values "r", "r+", "w", "w+", "a", "a+") must be compatible
with the mode of the file descriptor. The file position indicator of the
new stream is set to that belonging to `fd`, and the error and
end-of-file indicators are cleared. Modes "w" or "w+" do not cause
truncation of the file. The file descriptor is not dup'ed, and will be
closed when the stream created by [fdopen](https://manual.cs50.io/3/fdopen)() is closed.
The result of applying [fdopen](https://manual.cs50.io/3/fdopen)() to a shared memory
object is undefined.

<a id="freopen"></a>

#### freopen()

The [freopen](https://manual.cs50.io/3/freopen)() function opens the file whose name is
the string pointed to by `pathname` and associates the stream
pointed to by `stream` with it. The original stream (if it
exists) is closed. The `mode` argument is used just as in the
[fopen](https://manual.cs50.io/3/fopen)() function.

If the `pathname` argument is a null pointer,
[freopen](https://manual.cs50.io/3/freopen)() changes the mode of the stream to that
specified in `mode`; that is, [freopen](https://manual.cs50.io/3/freopen)() reopens
the pathname that is associated with the stream. The specification for
this behavior was added in the C99 standard, which says:

> In this case, the file descriptor associated with the stream need not
> be closed if the call to [freopen](https://manual.cs50.io/3/freopen)() succeeds. It is
> implementation-defined which changes of mode are permitted (if any), and
> under what circumstances.

The primary use of the [freopen](https://manual.cs50.io/3/freopen)() function is to
change the file associated with a standard text stream (`stderr`,
`stdin`, or `stdout`).

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/fopen#return-value)

This function returns a pointer to a `FILE` representing the opened file or, in cases of error (as when `pathname` doesn’t exist), `NULL`.

Upon successful completion [fopen](https://manual.cs50.io/3/fopen)(),
[fdopen](https://manual.cs50.io/3/fdopen)(), and [freopen](https://manual.cs50.io/3/freopen)() return a
`FILE` pointer. Otherwise, NULL is returned and `errno` is
set to indicate the error.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/fopen#examples)

```c
#include <stdio.h>  

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

### [ERRORS](https://manual.cs50.io/3/fopen#errors)

**EINVAL**
:   The `mode` provided to [fopen](https://manual.cs50.io/3/fopen)(),
    [fdopen](https://manual.cs50.io/3/fdopen)(), or [freopen](https://manual.cs50.io/3/freopen)() was
    invalid.

The [fopen](https://manual.cs50.io/3/fopen)(), [fdopen](https://manual.cs50.io/3/fdopen)(), and
[freopen](https://manual.cs50.io/3/freopen)() functions may also fail and set
`errno` for any of the errors specified for the routine
[malloc](https://manual.cs50.io/3/malloc)(3).

The [fopen](https://manual.cs50.io/3/fopen)() function may also fail and set
`errno` for any of the errors specified for the routine
[open](https://manual.cs50.io/2/open)(2).

The [fdopen](https://manual.cs50.io/3/fdopen)() function may also fail and set
`errno` for any of the errors specified for the routine
[fcntl](https://manual.cs50.io/2/fcntl)(2).

The [freopen](https://manual.cs50.io/3/freopen)() function may also fail and set
`errno` for any of the errors specified for the routines
[open](https://manual.cs50.io/2/open)(2), [fclose](https://manual.cs50.io/3/fclose)(3), and
[fflush](https://manual.cs50.io/3/fflush)(3).

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/fopen#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [fopen](https://manual.cs50.io/3/fopen)(), [fdopen](https://manual.cs50.io/3/fdopen)(), [freopen](https://manual.cs50.io/3/freopen)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/fopen#standards)

[fopen](https://manual.cs50.io/3/fopen)() [freopen](https://manual.cs50.io/3/freopen)()
:   C11, POSIX.1-2008.

[fdopen](https://manual.cs50.io/3/fdopen)()
:   POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/fopen#history)

[fopen](https://manual.cs50.io/3/fopen)() [freopen](https://manual.cs50.io/3/freopen)()
:   POSIX.1-2001, C89.

[fdopen](https://manual.cs50.io/3/fdopen)()
:   POSIX.1-2001.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/fopen#notes)

<a id="glibc-notes"></a>

#### glibc notes

The GNU C library allows the following extensions for the string
specified in `mode`:

**c** (since glibc 2.3.3)
:   Do not make the open operation, or subsequent read and write
    operations, thread cancelation points. This flag is ignored for
    [fdopen](https://manual.cs50.io/3/fdopen)().

**e** (since glibc 2.7)
:   Open the file with the **O_CLOEXEC** flag. See
    [open](https://manual.cs50.io/2/open)(2) for more information. This flag is ignored for
    [fdopen](https://manual.cs50.io/3/fdopen)().

**m** (since glibc 2.3)
:   Attempt to access the file using [mmap](https://manual.cs50.io/2/mmap)(2), rather
    than I/O system calls ([read](https://manual.cs50.io/2/read)(2),
    [write](https://manual.cs50.io/2/write)(2)). Currently, use of [mmap](https://manual.cs50.io/2/mmap)(2)
    is attempted only for a file opened for reading.

**x**
:   Open the file exclusively (like the **O_EXCL** flag of
    [open](https://manual.cs50.io/2/open)(2)). If the file already exists,
    [fopen](https://manual.cs50.io/3/fopen)() fails, and sets `errno` to
    **EEXIST**. This flag is ignored for
    [fdopen](https://manual.cs50.io/3/fdopen)().

In addition to the above characters, [fopen](https://manual.cs50.io/3/fopen)() and
[freopen](https://manual.cs50.io/3/freopen)() support the following syntax in
`mode`:

**,ccs=**`string`

The given `string` is taken as the name of a coded character
set and the stream is marked as wide-oriented. Thereafter, internal
conversion functions convert I/O to and from the character set
`string`. If the **,ccs=**`string` syntax is
not specified, then the wide-orientation of the stream is determined by
the first file operation. If that operation is a wide-character
operation, the stream is marked wide-oriented, and functions to convert
to the coded character set are loaded.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/fopen#bugs)

When parsing for individual flag characters in `mode` (i.e.,
the characters preceding the "ccs" specification), the glibc
implementation of [fopen](https://manual.cs50.io/3/fopen)() and
[freopen](https://manual.cs50.io/3/freopen)() limits the number of characters examined in
`mode` to 7 (or, before glibc 2.14, to 6, which was not enough to
include possible specifications such as "rb+cmxe"). The current
implementation of [fdopen](https://manual.cs50.io/3/fdopen)() parses at most 5 characters
in `mode`.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/fopen#see-also)

[open](https://manual.cs50.io/2/open)(2), [fclose](https://manual.cs50.io/3/fclose)(3),
[fileno](https://manual.cs50.io/3/fileno)(3), [fmemopen](https://manual.cs50.io/3/fmemopen)(3),
[fopencookie](https://manual.cs50.io/3/fopencookie)(3), [open_memstream](https://manual.cs50.io/3/open_memstream)(3)

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
- https://manual.cs50.io/3/fopen — retrieved 2026-10-18T05:45:49+03:30, sha256 `de0f1fa578835381…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
