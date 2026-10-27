---
id: manual-get_long
type: reference
title: get_long(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/get_long
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:06+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- cs50-h
- get-long
- manual
checksum: sha256:180ac746ed3fb692b26348c4388e61c7b0bf4a6852a8b961f68d7ede5977c16e
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# get_long(3) — CS50 manual page

## 1. Source metadata
- **Title:** get_long(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/get_long>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:06+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/get_long> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/get_long#name)

get_long - prompt a user for an `long`

get_long - prompts user for a line of text from stdin and returns the
equivalent long

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/get_long#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <cs50.h>
```

<a id="prototype"></a>

#### Prototype

```c
long get_long(string prompt, ...);
```

**#include <cs50.h>**

**long get_long(const char *format, ...);**

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/get_long#description)

This function prompts the user for a `long`. If the user inputs anything other than an `long` (or a value that cannot fit in an `long`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](https://manual.cs50.io/3/printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the
equivalent long; if the text does not represent a long or would cause
overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/get_long#return-value)

This function returns the user’s input as a `long`.

Returns the long equivalent to the line read from stdin in
[**LONG_MIN**, **LONG_MAX**). If line can’t be
read, returns **LONG_MAX**.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/get_long#example)

```c
#include <cs50.h>  
#include <stdio.h>  

int main(void)
{
    long l = get_long("Input:  ");
    printf("Output: %li\n", l);
}
```

> ```
> /**
>  * Returns the difference of two longs read from stdin, or LONG_MAX if there was an error.
>  */
> long subtract_longs(void)
> {
>     // read long from stdin
>     long i = get_long("Enter a long: ");
>
>     // make sure we read one successfully
>     if (i == LONG_MAX)
>     {
>         return LONG_MAX;
>     }
>
>     long j = get_long("What do you want to subtract from %ld? ", i);
>
>     if (j == LONG_MAX)
>     {
>         return LONG_MAX;
>     }
>
>     return i - j;
> }
> ```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/get_long#see-also)

> ```
> get_char(3), get_double(3), get_float(3), get_int(3), get_string(3),
> printf(3)
> ```

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
- https://manual.cs50.io/3/get_long — retrieved 2026-10-18T05:45:06+03:30, sha256 `180ac746ed3fb692…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
