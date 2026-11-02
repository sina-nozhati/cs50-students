---
id: manual-strcmp
type: reference
title: strcmp(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strcmp
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:11+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strcmp
checksum: sha256:9feeb6e1765487bb40d60aed1348024b0c0a53a3de5cb26a29541a161cf037bd
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strcmp(3) — CS50 manual page

## 1. Source metadata
- **Title:** strcmp(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strcmp>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:11+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strcmp> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strcmp#name)

strcmp - compare two strings

strcmp, strncmp - compare two strings

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strcmp#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strcmp#synopsis)

<a id="header-files"></a>

#### Header Files

```c
#include <cs50.h>  
#include <string.h>
```

<a id="prototype"></a>

#### Prototype

```c
int strcmp(string s1, string s2);
```

```
#include <string.h>
int strcmp(const char *s1, const char *s2);
int strncmp(const char s1[.n], const char s2[.n], size_t n);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strcmp#description)

This function compares two strings case-sensitively.

The [strcmp](https://manual.cs50.io/3/strcmp)() function compares the two strings
`s1` and `s2`. The locale is not taken into account (for a
locale-aware comparison, see [strcoll](https://manual.cs50.io/3/strcoll)(3)). The
comparison is done using unsigned characters.

[strcmp](https://manual.cs50.io/3/strcmp)() returns an integer indicating the result of
the comparison, as follows:

* 0, if the `s1` and `s2` are equal;
* a negative value if `s1` is less than
  `s2`;
* a positive value if `s1` is greater than
  `s2`.

The [strncmp](https://manual.cs50.io/3/strncmp)() function is similar, except it
compares only the first (at most) `n` bytes of `s1` and
`s2`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strcmp#return-value)

This function returns

* an `int` less than `0` if `s1` comes before `s2`,
* `0` if `s1` is the same as `s2`,
* an `int` greater than `0` if `s1` comes after `s2`.

The strings are compared using “ASCIIbetical” order, based on the ASCII values of their characters. For instance, `"AAA"` would come before `"BBB"`, and `"AAA"` would also come before `"aaa"`.

The [strcmp](https://manual.cs50.io/3/strcmp)() and [strncmp](https://manual.cs50.io/3/strncmp)()
functions return an integer less than, equal to, or greater than zero if
`s1` (or the first `n` bytes thereof) is found,
respectively, to be less than, to match, or be greater than
`s2`.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/strcmp#examples)

```c
#include <cs50.h>  
#include <stdio.h>  
#include <string.h>  

int main(void)
{
    string s1 = get_string("s1: ");
    string s2 = get_string("s2: ");
    if (strcmp(s1, s2) == 0)
    {
        printf("Those are the same.\n");
    }
    else
    {
        printf("Those are different.\n");
    }
}
```

The program below can be used to demonstrate the operation of
[strcmp](https://manual.cs50.io/3/strcmp)() (when given two arguments) and
[strncmp](https://manual.cs50.io/3/strncmp)() (when given three arguments). First, some
examples using [strcmp](https://manual.cs50.io/3/strcmp)():

```
$ ./string_comp ABC ABC
<str1> and <str2> are equal
$ ./string_comp ABC AB      # 'C' is ASCII 67; 'C' - '\0' = 67
<str1> is greater than <str2> (67)
$ ./string_comp ABA ABZ     # 'A' is ASCII 65; 'Z' is ASCII 90
<str1> is less than <str2> (-25)
$ ./string_comp ABJ ABC
<str1> is greater than <str2> (7)
$ ./string_comp $'\201' A   # 0201 - 0101 = 0100 (or 64 decimal)
<str1> is greater than <str2> (64)
```

The last example uses [bash](https://manual.cs50.io/1/bash)(1)-specific syntax to
produce a string containing an 8-bit ASCII code; the result demonstrates
that the string comparison uses unsigned characters.

And then some examples using [strncmp](https://manual.cs50.io/3/strncmp)():

```
$ ./string_comp ABC AB 3
<str1> is greater than <str2> (67)
$ ./string_comp ABC AB 2
<str1> and <str2> are equal in the first 2 bytes
```

<a id="program-source"></a>

#### Program source

```
/* string_comp.c
   Licensed under GNU General Public License v2 or later.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int
main(int argc, char *argv[])
{
    int res;
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <str1> <str2> [<len>]\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    if (argc == 3)
        res = strcmp(argv[1], argv[2]);
    else
        res = strncmp(argv[1], argv[2], atoi(argv[3]));
    if (res == 0) {
        printf("<str1> and <str2> are equal");
        if (argc > 3)
            printf(" in the first %d bytes\n", atoi(argv[3]));
        printf("\n");
    } else if (res < 0) {
        printf("<str1> is less than <str2> (%d)\n", res);
    } else {
        printf("<str1> is greater than <str2> (%d)\n", res);
    }
    exit(EXIT_SUCCESS);
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strcmp#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strcmp](https://manual.cs50.io/3/strcmp)(), [strncmp](https://manual.cs50.io/3/strncmp)() | Thread safety | MT-Safe |

<a id="versions"></a>

### [VERSIONS](https://manual.cs50.io/3/strcmp#versions)

POSIX.1 specifies only that:

> The sign of a nonzero return value shall be determined by the sign of
> the difference between the values of the first pair of bytes (both
> interpreted as type `unsigned char`) that differ in the strings
> being compared.

In glibc, as in most other implementations, the return value is the
arithmetic result of subtracting the last compared byte in `s2`
from the last compared byte in `s1`. (If the two characters are
equal, this difference is 0.)

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strcmp#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strcmp#history)

POSIX.1-2001, C89, SVr4, 4.3BSD.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strcmp#see-also)

[memcmp](https://manual.cs50.io/3/memcmp)(3), [strcasecmp](https://manual.cs50.io/3/strcasecmp)(3),
[strcoll](https://manual.cs50.io/3/strcoll)(3), [string](https://manual.cs50.io/3/string)(3),
[strncasecmp](https://manual.cs50.io/3/strncasecmp)(3), [strverscmp](https://manual.cs50.io/3/strverscmp)(3),
[wcscmp](https://manual.cs50.io/3/wcscmp)(3), [wcsncmp](https://manual.cs50.io/3/wcsncmp)(3),
[ascii](https://manual.cs50.io/7/ascii)(7)

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
- https://manual.cs50.io/3/strcmp — retrieved 2026-10-18T05:45:11+03:30, sha256 `9feeb6e1765487bb…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
