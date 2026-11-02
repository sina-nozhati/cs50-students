---
id: tool-cs50-library-c
type: tool
title: CS50 Library for C
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/libraries/cs50/c/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:36+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- cs50-library-c
- tool
checksum: sha256:2fa6ddbe1dccc24f85fa2e25a4cd2b420f92c8f9c5b8b487eda098523001b069
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# CS50 Library for C

## 1. Source metadata
- **Title:** CS50 Library for C
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/libraries/cs50/c/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:36+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/libraries/cs50/c/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="cs50-library-for-c"></a>

### CS50 Library for C

<a id="installation"></a>

#### Installation

<a id="ubuntu"></a>

##### Ubuntu

```
$ curl -s https://packagecloud.io/install/repositories/cs50/repo/script.deb.sh | sudo bash
$ sudo apt install libcs50
```

<a id="fedora"></a>

##### Fedora

```
$ curl -s https://packagecloud.io/install/repositories/cs50/repo/script.rpm.sh | sudo bash
$ dnf install libcs50
```

<a id="from-source-linux-and-mac"></a>

##### From Source (Linux and Mac)

> 1. Download the latest release from <https://github.com/cs50/libcs50/releases>
> 2. Extract `libcs50-*.*`
> 3. `cd libcs50-*`
> 4. `sudo make install`

By default, we install to `/usr/local`. If you’d like to change the installation location, run `sudo DESTDIR=/path/to/install make install` instead.

<a id="environment-variables"></a>

#### Environment Variables

For parity with [Visual Studio Code for CS50](https://cs50.readthedocs.io/code/) and [cli50](https://cs50.readthedocs.io/libraries/cs50/c/cli50/), you may want to set these environment variables:

```
CC="clang"
CFLAGS="-ferror-limit=1 -gdwarf-4 -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-but-set-variable -Wshadow"
LDLIBS="-lcrypt -lcs50 -lm"
```

<a id="makefile"></a>

##### Makefile

Alternatively, if using a `Makefile` to compile a program (e.g., `foo`) from multiple files (e.g., `foo.c` and `bar.c`), you could structure it as follows. But be sure the last line begins with an actual tab character (`\t`), not spaces.

```
CC= clang
CFLAGS = -ferror-limit=1 -gdwarf-4 -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-but-set-variable -Wshadow
LDLIBS = -lcrypt -lcs50 -lm

EXE = foo

SRCS = foo.c bar.c
OBJS = $(SRCS:.c=.o)

$(EXE): $(OBJS)
     $(CC) $(CFLAGS) -o $@ $(OBJS) $(LDLIBS)
```

<a id="usage"></a>

#### Usage

Note

To use these functions, make sure to include `#include <cs50.h>` atop your file and compile with the `-lcs50` flag.

type string
:   Type representing a C string. Aliased to `char *`.

    Example usage:

    ```
    string s = "hello, world!";
    ```

char get_char(const char *format, ...)
:   Parameters
    :   * **format** – the `printf()`-like format string used to display the prompt
        * **...** – values to be substituted into the format string a la `printf()`

    Returns
    :   the `char` equivalent to the line read from stdin, or `CHAR_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent `char`;
    if text does not represent a single char, user is reprompted.

    Example usage:

    ```
    #include <stdio.h>
    #include <cs50.h>

    int main(void)
    {
        // attempt to read character from stdin
        char c = get_char("Enter char: ");

        // ensure character was read successfully
        if (c == CHAR_MAX)
        {
            return 1;
        }

        char next = get_char("You just entered %c. Enter another char: ", c);

        if (next == CHAR_MAX)
        {
            return 1;
        }

        printf("The last char you entered was %c\n", next);
    }
    ```

double get_double(const char *format, ...)
:   Parameters
    :   * **format** – the `printf()`-like format string used to display the prompt
        * **...** – values to be substituted into the format string a la `printf()`

    Returns
    :   the `double` equivalent to the line read from stdin in [`DBL_MIN`, `DBL_MAX`), as precisely as possible, or `DBL_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent `double`;
    if text does not represent a double or would cause overflow or underflow, user is reprompted.

    Example usage:

    ```
    double divide_doubles(void)
    {
        // read double from stdin
        double d = get_double("Enter a double: ");

        // make sure we read one successfully
        if (d == DBL_MAX)
        {
            return DBL_MAX;
        }

        double e = get_double("What do you want to divide %lf by? ", d);

        // make sure we don't divide by zero
        if (e == DBL_MAX || e == 0.0)
        {
            return DBL_MAX;
        }

        return i / j;
    }
    ```

int get_int(const char *format, ...)
:   Parameters
    :   * **format** – the `printf()`-like format string used to display the prompt
        * **...** – values to be substituted into the format string a la `printf()`

    Returns
    :   the `int` equivalent to the line read from stdin in [`INT_MIN`, `INT_MAX`) or `INT_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent `int`;
    if text does not represent an int or would cause overflow, user is reprompted.

    Example usage:

    ```
    #include <cs50.h>

    ...

    // Returns the sum of two ints read from stdin, or INT_MAX if there was an error.
    int add_ints(void)
    {
        // read int from stdin
        int i = get_int("Enter an int: ");

        // make sure we read one successfully
        if (i == INT_MAX)
        {
            return INT_MAX;
        }

        int j = get_int("What do you want to add %d to? ", i);

        if (j == INT_MAX)
        {
            return INT_MAX;
        }

        return i + j;
    }
    ```

float get_float(const char *format, ...)
:   Parameters
    :   * **format** – the `printf()`-like format string used to display the prompt
        * **...** – values to be substituted into the format string a la `printf()`

    Returns
    :   the `float` equivalent to the line read from stdin in [`FLT_MIN`, `FLT_MAX`), as precisely as possible, or `FLT_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent float;
    if text does not represent a float or would cause overflow or underflow, user is reprompted.

    Example usage:

    ```
    // Returns the product of two floats, or FLT_MAX on error.
    float multiply_floats(void)
    {
        // read float from stdin
        float f = get_float("Enter a float: ");

        // make sure we read one successfully
        if (f == FLT_MAX)
        {
            return FLT_MAX;
        }

        float g = get_float("What do you want to multiply %f by? ", f);

        if (g == FLT_MAX)
        {
            return FLT_MAX;
        }

        return f * g;
    }
    ```

long get_long(const char *format, ...)
:   Parameters
    :   * **format** – the `printf()`-like format string used to display the prompt
        * **...** – values to be substituted into the format string a la `printf()`

    Returns
    :   the `long` equivalent to the line read from stdin in [`LONG_MIN`, `LONG_MAX`) or `LONG_MAX` on error

    Prompts user for a line of text from standard input and returns the equivalent `long`; if text does not represent an int or would cause overflow, user is reprompted.

    Example usage:

    ```
    #include <cs50.h>

    ...

    // Returns the difference of two longs read from stdin, or LONG_MAX if there was an error.
    long subtract_longs(void)
    {
        // read long from stdin
        long i = get_long("Enter a long: ");

        // make sure we read one successfully
        if (i == LONG_MAX)
        {
            return LONG_MAX;
        }

        long j = get_long("What do you want to subtract from %ld? ", i);

        if (j == LONG_MAX)
        {
            return LONG_MAX;
        }

        return i - j;
    }
    ```

char *get_string(const char *format, ...)
:   > param format
    > :   the `printf()`-like format string used to display the prompt
    >
    > param …
    > :   values to be substituted into the format string a la `printf()`
    >
    > returns
    > :   the read line as a string sans line endings, or `NULL` on `EOF`.

    Prompts user for a line of text from standard input and returns it as a string (`char *`),
    sans trailing line ending. Supports CR (`\r`), LF (`\n`), and CRLF (`\r\n`) as line
    endings. Stores string on heap, but library’s destructor frees memory on program’s
    exit.

    Example usage:

    ```
    int main(void)
    {
        string s = get_string("Enter string: ");

        // ensure string was read
        if (s == NULL)
        {
            return 1;
        }

        string next = get_string("You just entered %s. Enter a new string: ", s);

        if (next == NULL)
        {
            return 1;
        }

        printf("Your last string was %s\n", next);
    }
    ```

<a id="troubleshooting"></a>

#### Troubleshooting

If when compiling your program, you see:

> `/usr/bin/ld: cannot find -lcs50`:
> :   Add `export LIBRARY_PATH=/usr/local/lib` to your `.bashrc`.
>
> `fatal error: 'cs50.h' file not found`:
> :   Add `export C_INCLUDE_PATH=/usr/local/include` to your `.bashrc`.
>
> `cannot open shared object file: No such file or directory`:
> :   Add `export LD_LIBRARY_PATH=/usr/local/lib` to your `.bashrc`.

If when executing your program, you see something similar to the following (especially common on newer Macs):

```
dyld[.....]: Library not loaded: libcs50-X.Y.Z.dylib
  Referenced from: <.....> .....
  Reason: tried: 'libcs50-X.Y.Z.dylib' (no such file), .....
```

Add `export DYLD_LIBRARY_PATH=/usr/local/lib` to your `.bashrc`.

If you’re not using Bash, use whatever command sets the value of environment variables in your preferred shell. If you set `DESTDIR` to something other than `/usr/local`, substitute it in for `/usr/local` in the suggestions above.

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 tools (index)](../README.md) (`tools`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
مستند ابزار رسمی CS50؛ برای راهنمای فارسی نصب و استفاده و پاسخ‌گویی به سؤال‌های فنی دانشجویان.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.


### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.readthedocs.io/libraries/cs50/c/ — retrieved 2026-10-18T05:40:36+03:30, sha256 `2fa6ddbe1dccc24f…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
