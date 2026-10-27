---
id: manual-malloc
type: reference
title: malloc(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/malloc
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:45+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- malloc
- manual
checksum: sha256:41c7cdf94422e4e5b2ca0dab679fc6bce3ef6f7d0a90beedc6f5ca1ff245f48a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# malloc(3) — CS50 manual page

## 1. Source metadata
- **Title:** malloc(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/malloc>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:45+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/malloc> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/malloc#name)

malloc - allocate memory dynamically

malloc, free, calloc, realloc, reallocarray - allocate and free
dynamic memory

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/malloc#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/malloc#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdlib.h>
```

<a id="prototype"></a>

#### Prototype

```c
void *malloc(size_t size);
```

Think of `void *` as meaning the address of any type of value in memory. Think of `size_t` as a `long`.

```
#include <stdlib.h>
void *malloc(size_t size);
void free(void *_Nullable ptr);
void *calloc(size_t nmemb, size_t size);
void *realloc(void *_Nullable ptr, size_t size);
void *reallocarray(void *_Nullable ptr, size_t nmemb, size_t size);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[reallocarray](https://manual.cs50.io/3/reallocarray)():

```
    Since glibc 2.29:
        _DEFAULT_SOURCE
    glibc 2.28 and earlier:
        _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/malloc#description)

This function dynamically allocates `size` contiguous bytes of memory (on the heap) that can be used to store any type of values.

<a id="malloc"></a>

#### malloc()

The [malloc](https://manual.cs50.io/3/malloc)() function allocates `size` bytes
and returns a pointer to the allocated memory. *The memory is not
initialized*. If `size` is 0, then [malloc](https://manual.cs50.io/3/malloc)()
returns a unique pointer value that can later be successfully passed to
[free](https://manual.cs50.io/3/free)(). (See "Nonportable behavior" for portability
issues.)

<a id="free"></a>

#### free()

The [free](https://manual.cs50.io/3/free)() function frees the memory space pointed
to by `ptr`, which must have been returned by a previous call to
[malloc](https://manual.cs50.io/3/malloc)() or related functions. Otherwise, or if
`ptr` has already been freed, undefined behavior occurs. If
`ptr` is NULL, no operation is performed.

<a id="calloc"></a>

#### calloc()

The [calloc](https://manual.cs50.io/3/calloc)() function allocates memory for an array
of `nmemb` elements of `size` bytes each and returns a
pointer to the allocated memory. The memory is set to zero. If
`nmemb` or `size` is 0, then [calloc](https://manual.cs50.io/3/calloc)()
returns a unique pointer value that can later be successfully passed to
[free](https://manual.cs50.io/3/free)().

If the multiplication of `nmemb` and `size` would
result in integer overflow, then [calloc](https://manual.cs50.io/3/calloc)() returns an
error. By contrast, an integer overflow would not be detected in the
following call to [malloc](https://manual.cs50.io/3/malloc)(), with the result that an
incorrectly sized block of memory would be allocated:

```
malloc(nmemb * size);
```

<a id="realloc"></a>

#### realloc()

The [realloc](https://manual.cs50.io/3/realloc)() function changes the size of the
memory block pointed to by `ptr` to `size` bytes. The
contents of the memory will be unchanged in the range from the start of
the region up to the minimum of the old and new sizes. If the new size
is larger than the old size, the added memory will `not` be
initialized.

If `ptr` is NULL, then the call is equivalent to
`malloc(size)`, for all values of `size`.

If `size` is equal to zero, and `ptr` is not NULL, then
the call is equivalent to `free(ptr)` (but see "Nonportable
behavior" for portability issues).

Unless `ptr` is NULL, it must have been returned by an earlier
call to **malloc** or related functions. If the area
pointed to was moved, a `free(ptr)` is done.

<a id="reallocarray"></a>

#### reallocarray()

The [reallocarray](https://manual.cs50.io/3/reallocarray)() function changes the size of (and
possibly moves) the memory block pointed to by `ptr` to be large
enough for an array of `nmemb` elements, each of which is
`size` bytes. It is equivalent to the call

```
realloc(ptr, nmemb * size);
```

However, unlike that [realloc](https://manual.cs50.io/3/realloc)() call,
[reallocarray](https://manual.cs50.io/3/reallocarray)() fails safely in the case where the
multiplication would overflow. If such an overflow occurs,
[reallocarray](https://manual.cs50.io/3/reallocarray)() returns an error.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/malloc#return-value)

This function returns the address of the first byte of memory allocated or `NULL` in cases of error (as when insufficient memory is available).

The [malloc](https://manual.cs50.io/3/malloc)(), [calloc](https://manual.cs50.io/3/calloc)(),
[realloc](https://manual.cs50.io/3/realloc)(), and [reallocarray](https://manual.cs50.io/3/reallocarray)()
functions return a pointer to the allocated memory, which is suitably
aligned for any type that fits into the requested size or less. On
error, these functions return NULL and set `errno`. Attempting to
allocate more than **PTRDIFF_MAX** bytes is considered an
error, as an object that large could cause later pointer subtraction to
overflow.

The [free](https://manual.cs50.io/3/free)() function returns no value, and preserves
`errno`.

The [realloc](https://manual.cs50.io/3/realloc)() and [reallocarray](https://manual.cs50.io/3/reallocarray)()
functions return NULL if `ptr` is not NULL and the requested size
is zero; this is not considered an error. (See "Nonportable behavior"
for portability issues.) Otherwise, the returned pointer may be the same
as `ptr` if the allocation was not moved (e.g., there was room to
expand the allocation in-place), or different from `ptr` if the
allocation was moved to a new address. If these functions fail, the
original block is left untouched; it is not freed or moved.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/malloc#examples)

```
#include <err.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MALLOCARRAY(n, type)  ((type *) my_mallocarray(n, sizeof(type)))
#define MALLOC(type)          MALLOCARRAY(1, type)
static inline void *my_mallocarray(size_t nmemb, size_t size);
int
main(void)
{
    char  *p;
    p = MALLOCARRAY(32, char);
    if (p == NULL)
        err(EXIT_FAILURE, "malloc");
    strlcpy(p, "foo", 32);
    puts(p);
}
static inline void *
my_mallocarray(size_t nmemb, size_t size)
{
    return reallocarray(NULL, nmemb, size);
}
```

<a id="errors"></a>

### [ERRORS](https://manual.cs50.io/3/malloc#errors)

[calloc](https://manual.cs50.io/3/calloc)(), [malloc](https://manual.cs50.io/3/malloc)(),
[realloc](https://manual.cs50.io/3/realloc)(), and [reallocarray](https://manual.cs50.io/3/reallocarray)() can fail
with the following error:

**ENOMEM**
:   Out of memory. Possibly, the application hit the
    **RLIMIT_AS** or **RLIMIT_DATA** limit
    described in [getrlimit](https://manual.cs50.io/2/getrlimit)(2). Another reason could be that
    the number of mappings created by the caller process exceeded the limit
    specified by `/proc/sys/vm/max_map_count`.

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/malloc#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [malloc](https://manual.cs50.io/3/malloc)(), [free](https://manual.cs50.io/3/free)(), [calloc](https://manual.cs50.io/3/calloc)(), [realloc](https://manual.cs50.io/3/realloc)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/malloc#standards)

[malloc](https://manual.cs50.io/3/malloc)() [free](https://manual.cs50.io/3/free)() [calloc](https://manual.cs50.io/3/calloc)() [realloc](https://manual.cs50.io/3/realloc)()
:   C11, POSIX.1-2008.

[reallocarray](https://manual.cs50.io/3/reallocarray)()
:   None.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/malloc#history)

[malloc](https://manual.cs50.io/3/malloc)() [free](https://manual.cs50.io/3/free)() [calloc](https://manual.cs50.io/3/calloc)() [realloc](https://manual.cs50.io/3/realloc)()
:   POSIX.1-2001, C89.

[reallocarray](https://manual.cs50.io/3/reallocarray)()
:   glibc 2.26. OpenBSD 5.6, FreeBSD 11.0.

[malloc](https://manual.cs50.io/3/malloc)() and related functions rejected sizes
greater than **PTRDIFF_MAX** starting in glibc 2.30.

[free](https://manual.cs50.io/3/free)() preserved `errno` starting in glibc
2.33.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/malloc#notes)

By default, Linux follows an optimistic memory allocation strategy.
This means that when [malloc](https://manual.cs50.io/3/malloc)() returns non-NULL there is
no guarantee that the memory really is available. In case it turns out
that the system is out of memory, one or more processes will be killed
by the OOM killer. For more information, see the description of
`/proc/sys/vm/overcommit_memory` and
`/proc/sys/vm/oom_adj` in [proc](https://manual.cs50.io/5/proc)(5), and the Linux
kernel source file
`Documentation/vm/overcommit-accounting.rst`.

Normally, [malloc](https://manual.cs50.io/3/malloc)() allocates memory from the heap,
and adjusts the size of the heap as required, using
[sbrk](https://manual.cs50.io/2/sbrk)(2). When allocating blocks of memory larger than
**MMAP_THRESHOLD** bytes, the glibc
[malloc](https://manual.cs50.io/3/malloc)() implementation allocates the memory as a
private anonymous mapping using [mmap](https://manual.cs50.io/2/mmap)(2).
**MMAP_THRESHOLD** is 128 kB by default, but is adjustable
using [mallopt](https://manual.cs50.io/3/mallopt)(3). Prior to Linux 4.7 allocations
performed using [mmap](https://manual.cs50.io/2/mmap)(2) were unaffected by the
**RLIMIT_DATA** resource limit; since Linux 4.7, this limit
is also enforced for allocations performed using
[mmap](https://manual.cs50.io/2/mmap)(2).

To avoid corruption in multithreaded applications, mutexes are used
internally to protect the memory-management data structures employed by
these functions. In a multithreaded application in which threads
simultaneously allocate and free memory, there could be contention for
these mutexes. To scalably handle memory allocation in multithreaded
applications, glibc creates additional `memory allocation arenas`
if mutex contention is detected. Each arena is a large region of memory
that is internally allocated by the system (using
[brk](https://manual.cs50.io/2/brk)(2) or [mmap](https://manual.cs50.io/2/mmap)(2)), and managed with
its own mutexes.

If your program uses a private memory allocator, it should do so by
replacing [malloc](https://manual.cs50.io/3/malloc)(), [free](https://manual.cs50.io/3/free)(),
[calloc](https://manual.cs50.io/3/calloc)(), and [realloc](https://manual.cs50.io/3/realloc)(). The
replacement functions must implement the documented glibc behaviors,
including `errno` handling, size-zero allocations, and overflow
checking; otherwise, other library routines may crash or operate
incorrectly. For example, if the replacement `free`() does not
preserve `errno`, then seemingly unrelated library routines may
fail without having a valid reason in `errno`. Private memory
allocators may also need to replace other glibc functions; see
"Replacing malloc" in the glibc manual for details.

Crashes in memory allocators are almost always related to heap
corruption, such as overflowing an allocated chunk or freeing the same
pointer twice.

The [malloc](https://manual.cs50.io/3/malloc)() implementation is tunable via
environment variables; see [mallopt](https://manual.cs50.io/3/mallopt)(3) for details.

<a id="nonportable-behavior"></a>

#### Nonportable behavior

The behavior of these functions when the requested size is zero is
glibc specific; other implementations may return NULL without setting
`errno`, and portable POSIX programs should tolerate such
behavior. See **realloc**(3p).

POSIX requires memory allocators to set `errno` upon failure.
However, the C standard does not require this, and applications portable
to non-POSIX platforms should not assume this.

Portable programs should not use private memory allocators, as POSIX
and the C standard do not allow replacement of
[malloc](https://manual.cs50.io/3/malloc)(), [free](https://manual.cs50.io/3/free)(),
[calloc](https://manual.cs50.io/3/calloc)(), and [realloc](https://manual.cs50.io/3/realloc)().

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/malloc#see-also)

[valgrind](https://manual.cs50.io/1/valgrind)(1), [brk](https://manual.cs50.io/2/brk)(2),
[mmap](https://manual.cs50.io/2/mmap)(2), [alloca](https://manual.cs50.io/3/alloca)(3),
[malloc_get_state](https://manual.cs50.io/3/malloc_get_state)(3), [malloc_info](https://manual.cs50.io/3/malloc_info)(3),
[malloc_trim](https://manual.cs50.io/3/malloc_trim)(3), [malloc_usable_size](https://manual.cs50.io/3/malloc_usable_size)(3),
[mallopt](https://manual.cs50.io/3/mallopt)(3), [mcheck](https://manual.cs50.io/3/mcheck)(3),
[mtrace](https://manual.cs50.io/3/mtrace)(3), [posix_memalign](https://manual.cs50.io/3/posix_memalign)(3)

For details of the GNU C library implementation, see [https://sourceware.org/glibc/wiki/MallocInternals](https://manual.cs50.io/3/<a href=)">.

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
- https://manual.cs50.io/3/malloc — retrieved 2026-10-18T05:45:45+03:30, sha256 `41c7cdf94422e4e5…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
