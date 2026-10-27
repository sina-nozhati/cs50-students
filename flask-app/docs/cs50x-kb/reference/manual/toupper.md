---
id: manual-toupper
type: reference
title: toupper(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/toupper
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:17+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- toupper
checksum: sha256:4d45a3247d63644177870330e2eef4e2057d4ec199df3c2245a6b96f87a098c1
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# toupper(3) — CS50 manual page

## 1. Source metadata
- **Title:** toupper(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/toupper>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:17+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/toupper> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/toupper#name)

toupper - convert a `char` to uppercase

toupper, tolower, toupper_l, tolower_l - convert uppercase or
lowercase

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/toupper#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/toupper#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <ctype.h>
```

<a id="prototype"></a>

#### Prototype

```c
int toupper(char c);
```

Think of this function as taking a `char` as input.

```
#include <ctype.h>
int toupper(int c);
int tolower(int c);
int toupper_l(int c, locale_t locale);
int tolower_l(int c, locale_t locale);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[toupper_l](https://manual.cs50.io/3/toupper_l)(), [tolower_l](https://manual.cs50.io/3/tolower_l)():

```
    Since glibc 2.10:
        _XOPEN_SOURCE >= 700
    Before glibc 2.10:
        _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/toupper#description)

This function converts `c` to uppercase.

These functions convert lowercase letters to uppercase, and vice
versa.

If `c` is a lowercase letter, [toupper](https://manual.cs50.io/3/toupper)()
returns its uppercase equivalent, if an uppercase representation exists
in the current locale. Otherwise, it returns `c`. The
[toupper_l](https://manual.cs50.io/3/toupper_l)() function performs the same task, but uses
the locale referred to by the locale handle `locale`.

If `c` is an uppercase letter, [tolower](https://manual.cs50.io/3/tolower)()
returns its lowercase equivalent, if a lowercase representation exists
in the current locale. Otherwise, it returns `c`. The
[tolower_l](https://manual.cs50.io/3/tolower_l)() function performs the same task, but uses
the locale referred to by the locale handle `locale`.

If `c` is neither an `unsigned char` value nor
**EOF**, the behavior of these functions is undefined.

The behavior of [toupper_l](https://manual.cs50.io/3/toupper_l)() and
[tolower_l](https://manual.cs50.io/3/tolower_l)() is undefined if `locale` is the
special locale object **LC_GLOBAL_LOCALE** (see
[duplocale](https://manual.cs50.io/3/duplocale)(3)) or is not a valid locale object
handle.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/toupper#return-value)

If `c` is a lowercase letter (`a` through `z`), this function returns its uppercase equivalent (`A` through `Z`). If `c` is not a lowercase letter, this function returns `c` itself.

The value returned is that of the converted letter, or `c` if
the conversion was not possible.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/toupper#example)

```c
#include <cs50.h>  
#include <ctype.h>  
#include <stdio.h>  

int main(void)
{
    char c = get_char("Input:  ");
    printf("Output: %c\n", toupper(c));
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/toupper#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [toupper](https://manual.cs50.io/3/toupper)(), [tolower](https://manual.cs50.io/3/tolower)(), [toupper_l](https://manual.cs50.io/3/toupper_l)(), [tolower_l](https://manual.cs50.io/3/tolower_l)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/toupper#standards)

[toupper](https://manual.cs50.io/3/toupper)() [tolower](https://manual.cs50.io/3/tolower)()
:   C11, POSIX.1-2008.

[toupper_l](https://manual.cs50.io/3/toupper_l)() [tolower_l](https://manual.cs50.io/3/tolower_l)()
:   POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/toupper#history)

[toupper](https://manual.cs50.io/3/toupper)() [tolower](https://manual.cs50.io/3/tolower)()
:   C89, 4.3BSD, POSIX.1-2001.

[toupper_l](https://manual.cs50.io/3/toupper_l)() [tolower_l](https://manual.cs50.io/3/tolower_l)()
:   POSIX.1-2008.

<a id="notes"></a>

### [NOTES](https://manual.cs50.io/3/toupper#notes)

The standards require that the argument `c` for these
functions is either **EOF** or a value that is
representable in the type `unsigned char`. If the argument
`c` is of type `char`, it must be cast to *unsigned
char*, as in the following example:

```
char c;
...
res = toupper((unsigned char) c);
```

This is necessary because `char` may be the equivalent
`signed char`, in which case a byte where the top bit is set
would be sign extended when converting to `int`, yielding a value
that is outside the range of `unsigned char`.

The details of what constitutes an uppercase or lowercase letter
depend on the locale. For example, the default **"C"**
locale does not know about umlauts, so no conversion is done for
them.

In some non-English locales, there are lowercase letters with no
corresponding uppercase equivalent; the German sharp s is one
example.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/toupper#see-also)

[isalpha](https://manual.cs50.io/3/isalpha)(3), [newlocale](https://manual.cs50.io/3/newlocale)(3),
[setlocale](https://manual.cs50.io/3/setlocale)(3), [towlower](https://manual.cs50.io/3/towlower)(3),
[towupper](https://manual.cs50.io/3/towupper)(3), [uselocale](https://manual.cs50.io/3/uselocale)(3),
[locale](https://manual.cs50.io/7/locale)(7)

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
- https://manual.cs50.io/3/toupper — retrieved 2026-10-18T05:45:17+03:30, sha256 `4d45a3247d636441…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
