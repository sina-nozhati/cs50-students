---
id: manual-srand
type: reference
title: srand(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/srand
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:40+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- srand
checksum: sha256:64844977d6000dbb72aa557ded77feb3da0379a0fa3b0b901d52ea28ab02f475
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# srand(3) — CS50 manual page

## 1. Source metadata
- **Title:** srand(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/srand>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:40+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/srand> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/srand#name)

rand, rand_r, srand - pseudo-random number generator

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/srand#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/srand#synopsis)

```
#include <stdlib.h>
int rand(void);
void srand(unsigned int seed);
[[deprecated]] int rand_r(unsigned int *seedp);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[rand_r](https://manual.cs50.io/3/rand_r)():

```
    Since glibc 2.24:
        _POSIX_C_SOURCE >= 199506L
    glibc 2.23 and earlier
        _POSIX_C_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/srand#description)

The [rand](https://manual.cs50.io/3/rand)() function returns a pseudo-random integer
in the range 0 to **RAND_MAX** inclusive (i.e., the
mathematical range [0, **RAND_MAX**]).

The [srand](https://manual.cs50.io/3/srand)() function sets its argument as the seed
for a new sequence of pseudo-random integers to be returned by
[rand](https://manual.cs50.io/3/rand)(). These sequences are repeatable by calling
[srand](https://manual.cs50.io/3/srand)() with the same seed value.

If no seed value is provided, the [rand](https://manual.cs50.io/3/rand)() function is
automatically seeded with a value of 1.

The function [rand](https://manual.cs50.io/3/rand)() is not reentrant, since it uses
hidden state that is modified on each call. This might just be the seed
value to be used by the next call, or it might be something more
elaborate. In order to get reproducible behavior in a threaded
application, this state must be made explicit; this can be done using
the reentrant function [rand_r](https://manual.cs50.io/3/rand_r)().

Like [rand](https://manual.cs50.io/3/rand)(), [rand_r](https://manual.cs50.io/3/rand_r)() returns a
pseudo-random integer in the range [0, **RAND_MAX**]. The
`seedp` argument is a pointer to an `unsigned int` that is
used to store state between calls. If [rand_r](https://manual.cs50.io/3/rand_r)() is
called with the same initial value for the integer pointed to by
`seedp`, and that value is not modified between calls, then the
same pseudo-random sequence will result.

The value pointed to by the `seedp` argument of
[rand_r](https://manual.cs50.io/3/rand_r)() provides only a very small amount of state, so
this function will be a weak pseudo-random generator. Try
[drand48_r](https://manual.cs50.io/3/drand48_r)(3) instead.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/srand#return-value)

The [rand](https://manual.cs50.io/3/rand)() and [rand_r](https://manual.cs50.io/3/rand_r)() functions
return a value between 0 and **RAND_MAX** (inclusive). The
[srand](https://manual.cs50.io/3/srand)() function returns no value.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/srand#examples)

POSIX.1-2001 gives the following example of an implementation of
[rand](https://manual.cs50.io/3/rand)() and [srand](https://manual.cs50.io/3/srand)(), possibly useful
when one needs the same sequence on two different machines.

```
static unsigned long next = 1;
/* RAND_MAX assumed to be 32767 */
int myrand(void) {
    next = next * 1103515245 + 12345;
    return((unsigned)(next/65536) % 32768);
}
void mysrand(unsigned int seed) {
    next = seed;
}
```

The following program can be used to display the pseudo-random
sequence produced by [rand](https://manual.cs50.io/3/rand)() when given a particular
seed. When the seed is `-1`, the program uses a random seed.

```
#include <stdio.h>
#include <stdlib.h>
int
main(int argc, char *argv[])
{
    int           r;
    unsigned int  seed, nloops;
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <seed> <nloops>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    seed = atoi(argv[1]);
    nloops = atoi(argv[2]);
    if (seed == -1) {
        seed = arc4random();
        printf("seed: %u\n", seed);
    }
    srand(seed);
    for (unsigned int j = 0; j < nloops; j++) {
        r =  rand();
        printf("%d\n", r);
    }
    exit(EXIT_SUCCESS);
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/srand#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [rand](https://manual.cs50.io/3/rand)(), [rand_r](https://manual.cs50.io/3/rand_r)(), [srand](https://manual.cs50.io/3/srand)() | Thread safety | MT-Safe |

<a id="versions"></a>

### [VERSIONS](https://manual.cs50.io/3/srand#versions)

The versions of [rand](https://manual.cs50.io/3/rand)() and [srand](https://manual.cs50.io/3/srand)()
in the Linux C Library use the same random number generator as
[random](https://manual.cs50.io/3/random)(3) and [srandom](https://manual.cs50.io/3/srandom)(3), so the
lower-order bits should be as random as the higher-order bits. However,
on older [rand](https://manual.cs50.io/3/rand)() implementations, and on current
implementations on different systems, the lower-order bits are much less
random than the higher-order bits. Do not use this function in
applications intended to be portable when good randomness is needed.
(Use [random](https://manual.cs50.io/3/random)(3) instead.)

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/srand#standards)

[rand](https://manual.cs50.io/3/rand)() [srand](https://manual.cs50.io/3/srand)()
:   C11, POSIX.1-2008.

[rand_r](https://manual.cs50.io/3/rand_r)()
:   POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/srand#history)

[rand](https://manual.cs50.io/3/rand)() [srand](https://manual.cs50.io/3/srand)()
:   SVr4, 4.3BSD, C89, POSIX.1-2001.

[rand_r](https://manual.cs50.io/3/rand_r)()
:   POSIX.1-2001. Obsolete in POSIX.1-2008.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/srand#see-also)

[drand48](https://manual.cs50.io/3/drand48)(3), [random](https://manual.cs50.io/3/random)(3)

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
- https://manual.cs50.io/3/srand — retrieved 2026-10-18T05:45:40+03:30, sha256 `64844977d6000dbb…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
