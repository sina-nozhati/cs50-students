---
id: manual-isspace
type: reference
title: isspace(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/isspace
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:24+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- isspace
- manual
checksum: sha256:f3335c8f62364606c87f24cdae7a07fb9d25a88d0c815a742358385012c168fa
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# isspace(3) — CS50 manual page

## 1. Source metadata
- **Title:** isspace(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/isspace>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:24+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/isspace> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/isspace#name)

isspace - check whether a character is whitespace (e.g., a newline, space, or tab)

isalnum, isalpha, isascii, isblank, iscntrl, isdigit, isgraph,
islower, isprint, ispunct, isspace, isupper, isxdigit, isalnum_l,
isalpha_l, isascii_l, isblank_l, iscntrl_l, isdigit_l, isgraph_l,
islower_l, isprint_l, ispunct_l, isspace_l, isupper_l, isxdigit_l -
character classification functions

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/isspace#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/isspace#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <ctype.h>
```

<a id="prototype"></a>

#### Prototype

```c
int isspace(char c);
```

Think of this function as taking a `char` as input.

```
#include <ctype.h>
int isalnum(int c);
int isalpha(int c);
int iscntrl(int c);
int isdigit(int c);
int isgraph(int c);
int islower(int c);
int isprint(int c);
int ispunct(int c);
int isspace(int c);
int isupper(int c);
int isxdigit(int c);
int isascii(int c);
int isblank(int c);
int isalnum_l(int c, locale_t locale);
int isalpha_l(int c, locale_t locale);
int isblank_l(int c, locale_t locale);
int iscntrl_l(int c, locale_t locale);
int isdigit_l(int c, locale_t locale);
int isgraph_l(int c, locale_t locale);
int islower_l(int c, locale_t locale);
int isprint_l(int c, locale_t locale);
int ispunct_l(int c, locale_t locale);
int isspace_l(int c, locale_t locale);
int isupper_l(int c, locale_t locale);
int isxdigit_l(int c, locale_t locale);
int isascii_l(int c, locale_t locale);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[isascii](https://manual.cs50.io/3/isascii)():

```
    _XOPEN_SOURCE
        || /* glibc >= 2.19: */ _DEFAULT_SOURCE
        || /* glibc <= 2.19: */ _SVID_SOURCE
```

[isblank](https://manual.cs50.io/3/isblank)():

```
    _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
```

[salnum_l](https://manual.cs50.io/3/salnum_l)(), [salpha_l](https://manual.cs50.io/3/salpha_l)(),
[sblank_l](https://manual.cs50.io/3/sblank_l)(), [scntrl_l](https://manual.cs50.io/3/scntrl_l)(),
[sdigit_l](https://manual.cs50.io/3/sdigit_l)(), [sgraph_l](https://manual.cs50.io/3/sgraph_l)(),
[slower_l](https://manual.cs50.io/3/slower_l)(), [sprint_l](https://manual.cs50.io/3/sprint_l)(),
[spunct_l](https://manual.cs50.io/3/spunct_l)(), [sspace_l](https://manual.cs50.io/3/sspace_l)(),
[supper_l](https://manual.cs50.io/3/supper_l)(), [sxdigit_l](https://manual.cs50.io/3/sxdigit_l)():

```
    Since glibc 2.10:
        _XOPEN_SOURCE >= 700
    Before glibc 2.10:
        _GNU_SOURCE
```

[isascii_l](https://manual.cs50.io/3/isascii_l)():

```
    Since glibc 2.10:
        _XOPEN_SOURCE >= 700 && (_SVID_SOURCE || _BSD_SOURCE)
    Before glibc 2.10:
        _GNU_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/isspace#description)

This function checks whether `c` is whitespace (e.g., `\n`, `' '`, or `'\t'`) or not.

These functions check whether `c`, which must have the value
of an `unsigned char` or **EOF**, falls into a
certain character class according to the specified locale. The functions
without the "_l" suffix perform the check based on the current
locale.

The functions with the "_l" suffix perform the check based on the
locale specified by the locale object `locale`. The behavior of
these functions is undefined if `locale` is the special locale
object **LC_GLOBAL_LOCALE** (see
[duplocale](https://manual.cs50.io/3/duplocale)(3)) or is not a valid locale object
handle.

The list below explains the operation of the functions without the
"_l" suffix; the functions with the "_l" suffix differ only in using the
locale object `locale` instead of the current locale.

[isalnum](https://manual.cs50.io/3/isalnum)()
:   checks for an alphanumeric character; it is equivalent to
    **([isalpha](https://manual.cs50.io/3/isalpha)(**`c`**) ||
    [isdigit](https://manual.cs50.io/3/isdigit)(**`c`**))**`.`

[isalpha](https://manual.cs50.io/3/isalpha)()
:   checks for an alphabetic character; in the standard
    **"C"** locale, it is equivalent to
    **([isupper](https://manual.cs50.io/3/isupper)(**`c`**) ||
    [islower](https://manual.cs50.io/3/islower)(**`c`**))**`.` In some
    locales, there may be additional characters for which
    [isalpha](https://manual.cs50.io/3/isalpha)() is true—letters which are neither uppercase
    nor lowercase.

[isascii](https://manual.cs50.io/3/isascii)()
:   checks whether `c` is a 7-bit `unsigned char` value
    that fits into the ASCII character set.

[isblank](https://manual.cs50.io/3/isblank)()
:   checks for a blank character; that is, a space or a tab.

[iscntrl](https://manual.cs50.io/3/iscntrl)()
:   checks for a control character.

[isdigit](https://manual.cs50.io/3/isdigit)()
:   checks for a digit (0 through 9).

[isgraph](https://manual.cs50.io/3/isgraph)()
:   checks for any printable character except space.

[islower](https://manual.cs50.io/3/islower)()
:   checks for a lowercase character.

[isprint](https://manual.cs50.io/3/isprint)()
:   checks for any printable character including space.

[ispunct](https://manual.cs50.io/3/ispunct)()
:   checks for any printable character which is not a space or an
    alphanumeric character.

[isspace](https://manual.cs50.io/3/isspace)()
:   checks for white-space characters. In the **"C"** and
    **"POSIX"** locales, these are: space, form-feed
    (**'\f'**), newline (**'\n'**), carriage
    return (**'\r'**), horizontal tab (**'\t'**),
    and vertical tab (**'\v'**).

[isupper](https://manual.cs50.io/3/isupper)()
:   checks for an uppercase letter.

[isxdigit](https://manual.cs50.io/3/isxdigit)()
:   checks for hexadecimal digits, that is, one of  
    **0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/isspace#return-value)

This function returns a non-zero `int` if `c` is whitespace and `0` if `c` is not whitespace.

The values returned are nonzero if the character `c` falls
into the tested class, and zero if not.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/isspace#example)

```c
#include <cs50.h>  
#include <ctype.h>  
#include <stdio.h>  

int main(void)
{
    char c = get_char("Input: ");
    if (isspace(c))
    {
        printf("Your input is whitespace.\n");
    }
    else
    {
        printf("Your input is not whitespace.\n");
    }
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/isspace#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [isalnum](https://manual.cs50.io/3/isalnum)(), [isalpha](https://manual.cs50.io/3/isalpha)(), [isascii](https://manual.cs50.io/3/isascii)(), [isblank](https://manual.cs50.io/3/isblank)(), [iscntrl](https://manual.cs50.io/3/iscntrl)(), [isdigit](https://manual.cs50.io/3/isdigit)(), [isgraph](https://manual.cs50.io/3/isgraph)(), [islower](https://manual.cs50.io/3/islower)(), [isprint](https://manual.cs50.io/3/isprint)(), [ispunct](https://manual.cs50.io/3/ispunct)(), [isspace](https://manual.cs50.io/3/isspace)(), [isupper](https://manual.cs50.io/3/isupper)(), [isxdigit](https://manual.cs50.io/3/isxdigit)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/isspace#standards)

[isalnum](https://manual.cs50.io/3/isalnum)() [isalpha](https://manual.cs50.io/3/isalpha)() [iscntrl](https://manual.cs50.io/3/iscntrl)() [isdigit](https://manual.cs50.io/3/isdigit)() [isgraph](https://manual.cs50.io/3/isgraph)() [islower](https://manual.cs50.io/3/islower)() [isprint](https://manual.cs50.io/3/isprint)() [ispunct](https://manual.cs50.io/3/ispunct)() [isspace](https://manual.cs50.io/3/isspace)() [isupper](https://manual.cs50.io/3/isupper)() [isxdigit](https://manual.cs50.io/3/isxdigit)() [isblank](https://manual.cs50.io/3/isblank)()
:   C11, POSIX.1-2008.

[isascii](https://manual.cs50.io/3/isascii)() [isalnum_l](https://manual.cs50.io/3/isalnum_l)() [isalpha_l](https://manual.cs50.io/3/isalpha_l)() [isblank_l](https://manual.cs50.io/3/isblank_l)() [iscntrl_l](https://manual.cs50.io/3/iscntrl_l)() [isdigit_l](https://manual.cs50.io/3/isdigit_l)() [isgraph_l](https://manual.cs50.io/3/isgraph_l)() [islower_l](https://manual.cs50.io/3/islower_l)() [isprint_l](https://manual.cs50.io/3/isprint_l)() [ispunct_l](https://manual.cs50.io/3/ispunct_l)() [isspace_l](https://manual.cs50.io/3/isspace_l)() [isupper_l](https://manual.cs50.io/3/isupper_l)() [isxdigit_l](https://manual.cs50.io/3/isxdigit_l)()
:   POSIX.1-2008.

[isascii_l](https://manual.cs50.io/3/isascii_l)()
:   GNU.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/isspace#history)

[isalnum](https://manual.cs50.io/3/isalnum)() [isalpha](https://manual.cs50.io/3/isalpha)() [iscntrl](https://manual.cs50.io/3/iscntrl)() [isdigit](https://manual.cs50.io/3/isdigit)() [isgraph](https://manual.cs50.io/3/isgraph)() [islower](https://manual.cs50.io/3/islower)() [isprint](https://manual.cs50.io/3/isprint)() [ispunct](https://manual.cs50.io/3/ispunct)() [isspace](https://manual.cs50.io/3/isspace)() [isupper](https://manual.cs50.io/3/isupper)() [isxdigit](https://manual.cs50.io/3/isxdigit)()
:   C89, POSIX.1-2001.

[isblank](https://manual.cs50.io/3/isblank)()
:   C99, POSIX.1-2001.

[isascii](https://manual.cs50.io/3/isascii)()
:   POSIX.1-2001 (XSI).

    POSIX.1-2008 marks it as obsolete, noting that it cannot be used
    portably in a localized application.

[isalnum_l](https://manual.cs50.io/3/isalnum_l)() [isalpha_l](https://manual.cs50.io/3/isalpha_l)() [isblank_l](https://manual.cs50.io/3/isblank_l)() [iscntrl_l](https://manual.cs50.io/3/iscntrl_l)() [isdigit_l](https://manual.cs50.io/3/isdigit_l)() [isgraph_l](https://manual.cs50.io/3/isgraph_l)() [islower_l](https://manual.cs50.io/3/islower_l)() [isprint_l](https://manual.cs50.io/3/isprint_l)() [ispunct_l](https://manual.cs50.io/3/ispunct_l)() [isspace_l](https://manual.cs50.io/3/isspace_l)() [isupper_l](https://manual.cs50.io/3/isupper_l)() [isxdigit_l](https://manual.cs50.io/3/isxdigit_l)()
:   glibc 2.3. POSIX.1-2008.

[isascii_l](https://manual.cs50.io/3/isascii_l)()
:   glibc 2.3.

<a id="caveats"></a>

### [CAVEATS](https://manual.cs50.io/3/isspace#caveats)

The standards require that the argument `c` for these
functions is either **EOF** or a value that is
representable in the type `unsigned char`; otherwise, the
behavior is undefined. If the argument `c` is of type
`char`, it must be cast to `unsigned char`, as in the
following example:

```
char c;
...
res = toupper((unsigned char) c);
```

This is necessary because `char` may be the equivalent of
`signed char`, in which case a byte where the top bit is set
would be sign extended when converting to `int`, yielding a value
that is outside the range of `unsigned char`.

The details of what characters belong to which class depend on the
locale. For example, [isupper](https://manual.cs50.io/3/isupper)() will not recognize an
A-umlaut (Ä) as an uppercase letter in the default **C**
locale.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/isspace#see-also)

[iswalnum](https://manual.cs50.io/3/iswalnum)(3), [iswalpha](https://manual.cs50.io/3/iswalpha)(3),
[iswblank](https://manual.cs50.io/3/iswblank)(3), [iswcntrl](https://manual.cs50.io/3/iswcntrl)(3),
[iswdigit](https://manual.cs50.io/3/iswdigit)(3), [iswgraph](https://manual.cs50.io/3/iswgraph)(3),
[iswlower](https://manual.cs50.io/3/iswlower)(3), [iswprint](https://manual.cs50.io/3/iswprint)(3),
[iswpunct](https://manual.cs50.io/3/iswpunct)(3), [iswspace](https://manual.cs50.io/3/iswspace)(3),
[iswupper](https://manual.cs50.io/3/iswupper)(3), [iswxdigit](https://manual.cs50.io/3/iswxdigit)(3),
[newlocale](https://manual.cs50.io/3/newlocale)(3), [setlocale](https://manual.cs50.io/3/setlocale)(3),
[toascii](https://manual.cs50.io/3/toascii)(3), [tolower](https://manual.cs50.io/3/tolower)(3),
[toupper](https://manual.cs50.io/3/toupper)(3), [uselocale](https://manual.cs50.io/3/uselocale)(3),
[ascii](https://manual.cs50.io/7/ascii)(7), [locale](https://manual.cs50.io/7/locale)(7)

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
- https://manual.cs50.io/3/isspace — retrieved 2026-10-18T05:45:24+03:30, sha256 `f3335c8f62364606…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
