---
id: manual-get_int
type: reference
title: get_int(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/get_int
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:05+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- cs50-h
- get-int
- manual
checksum: sha256:f14c587d489d75c9292674c9a3ed3d202fb8e93a751200a570098092eb4734d1
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# get_int(3) — CS50 manual page

## 1. Source metadata
- **Title:** get_int(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/get_int>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:05+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/get_int> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/get_int#name)

get_int - prompt a user for an `int`

get_int - prompts user for a line of text from stdin and returns the
equivalent int

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/get_int#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <cs50.h>
```

<a id="prototype"></a>

#### Prototype

```c
int get_int(string prompt, ...);
```

**#include <cs50.h>**

**int get_int(const char *format, ...);**

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/get_int#description)

This function prompts the user for an `int`. If the user inputs anything other than an `int` (or a value that cannot fit in an `int`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](https://manual.cs50.io/3/printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the
equivalent int; if text does not represent an int or would cause
overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/get_int#return-value)

This function returns the user’s input as a `int`.

Returns the int equivalent to the line read from stdin in
[**INT_MIN**, **INT_MAX**). If line can’t be
read, returns **INT_MAX**.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/get_int#example)

```c
#include <cs50.h>  
#include <stdio.h>  

int main(void)
{
    int i = get_int("Input:  ");
    printf("Output: %i\n", i);
}
```

> ```
> /**
>  * Returns the sum of two ints read from stdin, or INT_MAX if there was an error.
>  */
> int add_ints(void)
> {
>     // read int from stdin
>     int i = get_int("Enter an int: ");
>
>     // make sure we read one successfully
>     if (i == INT_MAX)
>     {
>         return INT_MAX;
>     }
>
>     int j = get_int("What do you want to add %d to? ", i);
>
>     if (j == INT_MAX)
>     {
>         return INT_MAX;
>     }
>
>     return i + j;
> }
> ```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/get_int#see-also)

> ```
> get_char(3), get_double(3), get_float(3), get_long(3),
> get_string(3), printf(3)
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
- https://manual.cs50.io/3/get_int — retrieved 2026-10-18T05:45:05+03:30, sha256 `f14c587d489d75c9…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
