---
id: manual-atof
type: reference
title: atof(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/atof
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:28+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- atof
- c
- manual
checksum: sha256:c61a340017333602f349091991e2ebaeaa98437727758c83eb70b605b8edf9bb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# atof(3) — CS50 manual page

## 1. Source metadata
- **Title:** atof(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/atof>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/atof> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/atof#name)

atof - convert a `string` to a `float`

atof - convert a string to a double

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/atof#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/atof#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdlib.h>
```

<a id="prototype"></a>

#### Prototype

```c
float atof(string s);
```

```
#include <stdlib.h>
double atof(const char *nptr);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/atof#description)

This function converts a (positive or negative) floating-point value from a `string` (e.g., `"50.0"`) to a `float` (e.g., `50.0`).

The [atof](https://manual.cs50.io/3/atof)() function converts the initial portion of
the string pointed to by `nptr` to `double`. The behavior
is the same as

```
strtod(nptr, NULL);
```

except that [atof](https://manual.cs50.io/3/atof)() does not detect errors.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/atof#return-value)

This function returns its input, `s`, as a `float`.

The converted value.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/atof#example)

```c
#include <stdio.h>  
#include <stdlib.h>  

int main(void)
{
    printf("This is CS%.0f\n", atof("50.0"));
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/atof#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [atof](https://manual.cs50.io/3/atof)() | Thread safety | MT-Safe locale |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/atof#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/atof#history)

POSIX.1-2001, C89, C99, SVr4, 4.3BSD.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/atof#see-also)

[atoi](https://manual.cs50.io/3/atoi)(3), [atol](https://manual.cs50.io/3/atol)(3),
[strfromd](https://manual.cs50.io/3/strfromd)(3), [strtod](https://manual.cs50.io/3/strtod)(3),
[strtol](https://manual.cs50.io/3/strtol)(3), [strtoul](https://manual.cs50.io/3/strtoul)(3)

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
- https://manual.cs50.io/3/atof — retrieved 2026-10-18T05:45:28+03:30, sha256 `c61a340017333602…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
