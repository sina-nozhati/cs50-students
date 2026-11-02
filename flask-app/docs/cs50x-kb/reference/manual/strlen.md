---
id: manual-strlen
type: reference
title: strlen(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strlen
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:10+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strlen
checksum: sha256:a7ee04f553fadf636987249b1ca5b55180a1b714322da74ec8c0d14b94b033ab
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strlen(3) — CS50 manual page

## 1. Source metadata
- **Title:** strlen(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strlen>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:10+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strlen> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strlen#name)

strlen - calculate the length of a string

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strlen#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strlen#synopsis)

strlen - calculate the length of a string

<a id="header-files"></a>

#### Header Files

```c
#include <cs50.h>  
#include <string.h>
```

<a id="prototype"></a>

#### Prototype

```c
int strlen(string s);
```

```
#include <string.h>
size_t strlen(const char *s);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strlen#description)

This function calculates the length of `s`.

The [strlen](https://manual.cs50.io/3/strlen)() function calculates the length of the
string pointed to by `s`, excluding the terminating null byte
('\0').

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strlen#return-value)

This function returns the number of characters in `s`, excluding the terminating NUL byte (i.e., `'\0'`).

The [strlen](https://manual.cs50.io/3/strlen)() function returns the number of bytes in
the string pointed to by `s`.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/strlen#example)

```c
#include <cs50.h>  
#include <stdio.h>  
#include <string.h>  

int main(void)
{
    string s = get_string("Input:  ");
    printf("Output: ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strlen#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strlen](https://manual.cs50.io/3/strlen)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strlen#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strlen#history)

POSIX.1-2001, C89, SVr4, 4.3BSD.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/strlen#notes)

In cases where the input buffer may not contain a terminating null
byte, [strnlen](https://manual.cs50.io/3/strnlen)(3) should be used instead.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strlen#see-also)

[string](https://manual.cs50.io/3/string)(3), [strnlen](https://manual.cs50.io/3/strnlen)(3),
[wcslen](https://manual.cs50.io/3/wcslen)(3), [wcsnlen](https://manual.cs50.io/3/wcsnlen)(3)

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
- https://manual.cs50.io/3/strlen — retrieved 2026-10-18T05:45:10+03:30, sha256 `a7ee04f553fadf63…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
