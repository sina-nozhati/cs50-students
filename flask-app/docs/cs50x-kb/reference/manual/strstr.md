---
id: manual-strstr
type: reference
title: strstr(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strstr
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:11+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strstr
checksum: sha256:4714b459417171d0471fe5ff04f3e7a79396b3b08f8e32cf9c5f41c1763b0bee
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strstr(3) — CS50 manual page

## 1. Source metadata
- **Title:** strstr(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strstr>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:11+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strstr> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strstr#name)

strstr - locate a substring

strstr, strcasestr - locate a substring

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strstr#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strstr#synopsis)

<a id="header-files"></a>

#### Header Files

```c
#include <cs50.h>  
#include <string.h>
```

<a id="prototype"></a>

#### Prototype

```c
string strstr(string haystack, string needle);
```

```
#include <string.h>
char *strstr(const char *haystack, const char *needle);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include <string.h>
char *strcasestr(const char *haystack, const char *needle);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strstr#description)

This function searches `haystack` for (the first occurrence of) `needle`. In other words, it determines whether (and where) `needle` is a substring of `haystack`.

The [strstr](https://manual.cs50.io/3/strstr)() function finds the first occurrence of
the substring `needle` in the string `haystack`. The
terminating null bytes ('\0') are not compared.

The [strcasestr](https://manual.cs50.io/3/strcasestr)() function is like
[strstr](https://manual.cs50.io/3/strstr)(), but ignores the case of both arguments.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strstr#return-value)

If `needle` is found in `haystack`, this function returns the substring of `haystack` that begins with `needle`. (For instance, if `haystack` is `"foo bar bar baz"` and `needle` is `"bar"`, this function returns `"bar bar baz"`.) If `needle` is not found in `haystack`, this function returns `NULL`.

These functions return a pointer to the beginning of the located
substring, or NULL if the substring is not found.

If `needle` is the empty string, the return value is always
`haystack` itself.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/strstr#example)

```c
#include <cs50.h>  
#include <string.h>  
#include <stdio.h>  

int main(void)
{
    string haystack = "foo bar bar baz";
    string needle = "bar";

    string match = strstr(haystack, needle);
    if (match)
    {
        printf("%s\n", match);
    }
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strstr#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strstr](https://manual.cs50.io/3/strstr)() | Thread safety | MT-Safe |
| [strcasestr](https://manual.cs50.io/3/strcasestr)() | Thread safety | MT-Safe locale |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strstr#standards)

[strstr](https://manual.cs50.io/3/strstr)()
:   C11, POSIX.1-2008.

[strcasestr](https://manual.cs50.io/3/strcasestr)()
:   GNU.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strstr#history)

[strstr](https://manual.cs50.io/3/strstr)()
:   POSIX.1-2001, C89.

[strcasestr](https://manual.cs50.io/3/strcasestr)()
:   GNU.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strstr#see-also)

[memchr](https://manual.cs50.io/3/memchr)(3), [memmem](https://manual.cs50.io/3/memmem)(3),
[strcasecmp](https://manual.cs50.io/3/strcasecmp)(3), [strchr](https://manual.cs50.io/3/strchr)(3),
[string](https://manual.cs50.io/3/string)(3), [strpbrk](https://manual.cs50.io/3/strpbrk)(3),
[strsep](https://manual.cs50.io/3/strsep)(3), [strspn](https://manual.cs50.io/3/strspn)(3),
[strtok](https://manual.cs50.io/3/strtok)(3), [wcsstr](https://manual.cs50.io/3/wcsstr)(3)

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
- https://manual.cs50.io/3/strstr — retrieved 2026-10-18T05:46:11+03:30, sha256 `4714b459417171d0…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
