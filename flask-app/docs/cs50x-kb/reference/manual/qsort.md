---
id: manual-qsort
type: reference
title: qsort(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/qsort
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:12+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- qsort
checksum: sha256:ef95515a4ef33d16d7337971e2873148fc845787820f4f6f9cdcf09b31c98ba8
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# qsort(3) — CS50 manual page

## 1. Source metadata
- **Title:** qsort(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/qsort>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:12+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/qsort> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/qsort#name)

qsort, qsort_r - sort an array

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/qsort#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/qsort#synopsis)

```
#include <stdlib.h>
void qsort(void base[.size * .nmemb], size_t nmemb, size_t size,
 int (*compar)(const void [.size], const void [.size]));
void qsort_r(void base[.size * .nmemb], size_t nmemb, size_t size,
 int (*compar)(const void [.size], const void [.size], void *),
 void *arg);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[qsort_r](https://manual.cs50.io/3/qsort_r)():

```
    _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/qsort#description)

The [qsort](https://manual.cs50.io/3/qsort)() function sorts an array with
`nmemb` elements of size `size`. The `base`
argument points to the start of the array.

The contents of the array are sorted in ascending order according to
a comparison function pointed to by `compar`, which is called
with two arguments that point to the objects being compared.

The comparison function must return an integer less than, equal to,
or greater than zero if the first argument is considered to be
respectively less than, equal to, or greater than the second. If two
members compare as equal, their order in the sorted array is
undefined.

The [qsort_r](https://manual.cs50.io/3/qsort_r)() function is identical to
[qsort](https://manual.cs50.io/3/qsort)() except that the comparison function
`compar` takes a third argument. A pointer is passed to the
comparison function via `arg`. In this way, the comparison
function does not need to use global variables to pass through arbitrary
arguments, and is therefore reentrant and safe to use in threads.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/qsort#return-value)

The [qsort](https://manual.cs50.io/3/qsort)() and [qsort_r](https://manual.cs50.io/3/qsort_r)() functions
return no value.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/qsort#examples)

For one example of use, see the example under
[bsearch](https://manual.cs50.io/3/bsearch)(3).

Another example is the following program, which sorts the strings
given in its command-line arguments:

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int
cmpstringp(const void *p1, const void *p2)
{
    /* The actual arguments to this function are "pointers to
       pointers to char", but strcmp(3) arguments are "pointers
       to char", hence the following cast plus dereference. */
    return strcmp(*(const char **) p1, *(const char **) p2);
}
int
main(int argc, char *argv[])
{
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <string>...\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    qsort(&argv[1], argc - 1, sizeof(char *), cmpstringp);
    for (size_t j = 1; j < argc; j++)
        puts(argv[j]);
    exit(EXIT_SUCCESS);
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/qsort#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [qsort](https://manual.cs50.io/3/qsort)(), [qsort_r](https://manual.cs50.io/3/qsort_r)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/qsort#standards)

[qsort](https://manual.cs50.io/3/qsort)()
:   C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/qsort#history)

[qsort](https://manual.cs50.io/3/qsort)()
:   POSIX.1-2001, C89, SVr4, 4.3BSD.

[qsort_r](https://manual.cs50.io/3/qsort_r)()
:   glibc 2.8.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/qsort#notes)

To compare C strings, the comparison function can call
[strcmp](https://manual.cs50.io/3/strcmp)(3), as shown in the example below.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/qsort#see-also)

[sort](https://manual.cs50.io/1/sort)(1), [alphasort](https://manual.cs50.io/3/alphasort)(3),
[strcmp](https://manual.cs50.io/3/strcmp)(3), [versionsort](https://manual.cs50.io/3/versionsort)(3)

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
- https://manual.cs50.io/3/qsort — retrieved 2026-10-18T05:46:12+03:30, sha256 `ef95515a4ef33d16…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
