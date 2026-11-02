---
id: manual-strtok
type: reference
title: strtok(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/strtok
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:46:09+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- manual
- strtok
checksum: sha256:e2916378bdf2c988c01d6cca573f7612eb4fe66a167b2ff389f15944662b9d3c
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# strtok(3) — CS50 manual page

## 1. Source metadata
- **Title:** strtok(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/strtok>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:46:09+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/strtok> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/strtok#name)

strtok, strtok_r - extract tokens from strings

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/strtok#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/strtok#synopsis)

```
#include <string.h>
char *strtok(char *restrict str, const char *restrict delim);
char *strtok_r(char *restrict str, const char *restrict delim,
 char **restrict saveptr);
```

> Feature Test Macro Requirements for glibc (see
> [feature_test_macros](https://manual.cs50.io/7/feature_test_macros)(7)):

[strtok_r](https://manual.cs50.io/3/strtok_r)():

```
    _POSIX_C_SOURCE
        || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/strtok#description)

The [strtok](https://manual.cs50.io/3/strtok)() function breaks a string into a
sequence of zero or more nonempty tokens. On the first call to
[strtok](https://manual.cs50.io/3/strtok)(), the string to be parsed should be specified
in `str`. In each subsequent call that should parse the same
string, `str` must be NULL.

The `delim` argument specifies a set of bytes that delimit the
tokens in the parsed string. The caller may specify different strings in
`delim` in successive calls that parse the same string.

Each call to [strtok](https://manual.cs50.io/3/strtok)() returns a pointer to a
null-terminated string containing the next token. This string does not
include the delimiting byte. If no more tokens are found,
[strtok](https://manual.cs50.io/3/strtok)() returns NULL.

A sequence of calls to [strtok](https://manual.cs50.io/3/strtok)() that operate on the
same string maintains a pointer that determines the point from which to
start searching for the next token. The first call to
[strtok](https://manual.cs50.io/3/strtok)() sets this pointer to point to the first byte
of the string. The start of the next token is determined by scanning
forward for the next nondelimiter byte in `str`. If such a byte
is found, it is taken as the start of the next token. If no such byte is
found, then there are no more tokens, and [strtok](https://manual.cs50.io/3/strtok)()
returns NULL. (A string that is empty or that contains only delimiters
will thus cause [strtok](https://manual.cs50.io/3/strtok)() to return NULL on the first
call.)

The end of each token is found by scanning forward until either the
next delimiter byte is found or until the terminating null byte ('\0')
is encountered. If a delimiter byte is found, it is overwritten with a
null byte to terminate the current token, and [strtok](https://manual.cs50.io/3/strtok)()
saves a pointer to the following byte; that pointer will be used as the
starting point when searching for the next token. In this case,
[strtok](https://manual.cs50.io/3/strtok)() returns a pointer to the start of the found
token.

From the above description, it follows that a sequence of two or more
contiguous delimiter bytes in the parsed string is considered to be a
single delimiter, and that delimiter bytes at the start or end of the
string are ignored. Put another way: the tokens returned by
[strtok](https://manual.cs50.io/3/strtok)() are always nonempty strings. Thus, for
example, given the string "`aaa;;bbb,`", successive calls to
[strtok](https://manual.cs50.io/3/strtok)() that specify the delimiter string
"`;,`" would return the strings "`aaa`" and
"`bbb`", and then a null pointer.

The [strtok_r](https://manual.cs50.io/3/strtok_r)() function is a reentrant version of
[strtok](https://manual.cs50.io/3/strtok)(). The `saveptr` argument is a pointer to
a `char *` variable that is used internally by
[strtok_r](https://manual.cs50.io/3/strtok_r)() in order to maintain context between
successive calls that parse the same string.

On the first call to [strtok_r](https://manual.cs50.io/3/strtok_r)(), `str` should
point to the string to be parsed, and the value of `*saveptr` is
ignored (but see NOTES). In subsequent calls, `str` should be
NULL, and `saveptr` (and the buffer that it points to) should be
unchanged since the previous call.

Different strings may be parsed concurrently using sequences of calls
to [strtok_r](https://manual.cs50.io/3/strtok_r)() that specify different `saveptr`
arguments.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/strtok#return-value)

The [strtok](https://manual.cs50.io/3/strtok)() and [strtok_r](https://manual.cs50.io/3/strtok_r)()
functions return a pointer to the next token, or NULL if there are no
more tokens.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/strtok#examples)

The program below uses nested loops that employ
[strtok_r](https://manual.cs50.io/3/strtok_r)() to break a string into a two-level hierarchy
of tokens. The first command-line argument specifies the string to be
parsed. The second argument specifies the delimiter byte(s) to be used
to separate that string into "major" tokens. The third argument
specifies the delimiter byte(s) to be used to separate the "major"
tokens into subtokens.

An example of the output produced by this program is the
following:

```
$ ./a.out 'a/bbb///cc;xxx:yyy:' ':;' '/'
1: a/bbb///cc
         --> a
         --> bbb
         --> cc
2: xxx
         --> xxx
3: yyy
         --> yyy
```

<a id="program-source"></a>

#### Program source

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int
main(int argc, char *argv[])
{
    char *str1, *str2, *token, *subtoken;
    char *saveptr1, *saveptr2;
    int j;
    if (argc != 4) {
        fprintf(stderr, "Usage: %s string delim subdelim\n",
                argv[0]);
        exit(EXIT_FAILURE);
    }
    for (j = 1, str1 = argv[1]; ; j++, str1 = NULL) {
        token = strtok_r(str1, argv[2], &saveptr1);
        if (token == NULL)
            break;
        printf("%d: %s\n", j, token);
        for (str2 = token; ; str2 = NULL) {
            subtoken = strtok_r(str2, argv[3], &saveptr2);
            if (subtoken == NULL)
                break;
            printf("\t --> %s\n", subtoken);
        }
    }
    exit(EXIT_SUCCESS);
}
```

Another example program using [strtok](https://manual.cs50.io/3/strtok)() can be found
in [getaddrinfo_a](https://manual.cs50.io/3/getaddrinfo_a)(3).

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/strtok#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [strtok](https://manual.cs50.io/3/strtok)() | Thread safety | MT-Unsafe race:strtok |
| [strtok_r](https://manual.cs50.io/3/strtok_r)() | Thread safety | MT-Safe |

<a id="versions"></a>

### [VERSIONS](https://manual.cs50.io/3/strtok#versions)

On some implementations, `*saveptr` is required to be NULL on
the first call to [strtok_r](https://manual.cs50.io/3/strtok_r)() that is being used to
parse `str`.

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/strtok#standards)

[strtok](https://manual.cs50.io/3/strtok)()
:   C11, POSIX.1-2008.

[strtok_r](https://manual.cs50.io/3/strtok_r)()
:   POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/strtok#history)

[strtok](https://manual.cs50.io/3/strtok)()
:   POSIX.1-2001, C89, SVr4, 4.3BSD.

[strtok_r](https://manual.cs50.io/3/strtok_r)()
:   POSIX.1-2001.

<a id="bugs"></a>

### [BUGS](https://manual.cs50.io/3/strtok#bugs)

Be cautious when using these functions. If you do use them, note
that:

* These functions modify their first argument.
* These functions cannot be used on constant strings.
* The identity of the delimiting byte is lost.
* The [strtok](https://manual.cs50.io/3/strtok)() function uses a static buffer while
  parsing, so it's not thread safe. Use [strtok_r](https://manual.cs50.io/3/strtok_r)() if
  this matters to you.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/strtok#see-also)

[memchr](https://manual.cs50.io/3/memchr)(3), [strchr](https://manual.cs50.io/3/strchr)(3),
[string](https://manual.cs50.io/3/string)(3), [strpbrk](https://manual.cs50.io/3/strpbrk)(3),
[strsep](https://manual.cs50.io/3/strsep)(3), [strspn](https://manual.cs50.io/3/strspn)(3),
[strstr](https://manual.cs50.io/3/strstr)(3), [wcstok](https://manual.cs50.io/3/wcstok)(3)

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
- https://manual.cs50.io/3/strtok — retrieved 2026-10-18T05:46:09+03:30, sha256 `e2916378bdf2c988…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
