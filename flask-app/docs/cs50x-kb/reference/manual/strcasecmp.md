---
id: manual-strcasecmp
type: reference
title: strcasecmp(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strcasecmp
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:12+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strcasecmp
checksum: sha256:6a9fe199f015eabd124a9a60613b00b782e672ee00cc0bf846411e7169b4c4d0
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strcasecmp(3) — CS50 manual page

## 1. Source metadata
- **Title:** strcasecmp(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strcasecmp>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:12+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strcasecmp> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strcasecmp#name)

strcasecmp - compare two strings ignoring case

strcasecmp, strncasecmp - compare two strings ignoring case

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strcasecmp#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strcasecmp#synopsis)

<a id="header-files"></a>

#### Header Files

```c
#include <cs50.h>  
#include <strings.h>
```

<a id="prototype"></a>

#### Prototype

```c
int strcasecmp(string s1, string s2);
```

```
#include <strings.h>
int strcasecmp(const char *s1, const char *s2);
int strncasecmp(const char s1[.n], const char s2[.n], size_t n);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strcasecmp#description)

This function compares two strings case-insensitively.

The [strcasecmp](https://manual.cs50.io/3/strcasecmp)() function performs a byte-by-byte
comparison of the strings `s1` and `s2`, ignoring the case
of the characters. It returns an integer less than, equal to, or greater
than zero if `s1` is found, respectively, to be less than, to
match, or be greater than `s2`.

The [strncasecmp](https://manual.cs50.io/3/strncasecmp)() function is similar, except that
it compares no more than `n` bytes of `s1` and
`s2`.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strcasecmp#return-value)

This function returns

* an `int` less than `0` if `s1` comes before `s2`, ignoring case,
* `0` if `s1` is the same as `s2`, ignoring case, or
* an `int` greater than `0` if `s1` comes after `s2`, ignoring case.

The strings are compared using “ASCIIbetical” order, based on the ASCII values of their characters. For instance, `"AAA"` would come before `"BBB"`.

The [strcasecmp](https://manual.cs50.io/3/strcasecmp)() and [strncasecmp](https://manual.cs50.io/3/strncasecmp)()
functions return an integer less than, equal to, or greater than zero if
`s1` is, after ignoring case, found to be less than, to match, or
be greater than `s2`, respectively.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/strcasecmp#example)

```c
#include <cs50.h>  
#include <stdio.h>  
#include <strings.h>  

int main(void)
{
    string s1 = get_string("s1: ");
    string s2 = get_string("s2: ");
    if (strcasecmp(s1, s2) == 0)
    {
        printf("Those are the same, ignoring case.\n");
    }
    else
    {
        printf("Those are different, even ignoring case.\n");
    }
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strcasecmp#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strcasecmp](https://manual.cs50.io/3/strcasecmp)(), [strncasecmp](https://manual.cs50.io/3/strncasecmp)() | Thread safety | MT-Safe locale |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strcasecmp#standards)

POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strcasecmp#history)

4.4BSD, POSIX.1-2001.

The [strcasecmp](https://manual.cs50.io/3/strcasecmp)() and [strncasecmp](https://manual.cs50.io/3/strncasecmp)()
functions first appeared in 4.4BSD, where they were declared in
`<string.h>`. Thus, for reasons of historical
compatibility, the glibc `<string.h>` header file also
declares these functions, if the **_DEFAULT_SOURCE** (or,
in glibc 2.19 and earlier, **_BSD_SOURCE**) feature test
macro is defined.

The POSIX.1-2008 standard says of these functions:

> When the **LC_CTYPE** category of the locale being used
> is from the POSIX locale, these functions shall behave as if the strings
> had been converted to lowercase and then a byte comparison performed.
> Otherwise, the results are unspecified.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strcasecmp#see-also)

[memcmp](https://manual.cs50.io/3/memcmp)(3), [strcmp](https://manual.cs50.io/3/strcmp)(3),
[strcoll](https://manual.cs50.io/3/strcoll)(3), [string](https://manual.cs50.io/3/string)(3),
[strncmp](https://manual.cs50.io/3/strncmp)(3), [wcscasecmp](https://manual.cs50.io/3/wcscasecmp)(3),
[wcsncasecmp](https://manual.cs50.io/3/wcsncasecmp)(3)

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
- https://manual.cs50.io/3/strcasecmp — retrieved 2026-10-18T05:45:12+03:30, sha256 `6a9fe199f015eabd…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
