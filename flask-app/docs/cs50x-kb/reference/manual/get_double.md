---
id: manual-get_double
type: reference
title: get_double(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/get_double
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:03+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- cs50-h
- get-double
- manual
checksum: sha256:90e79dfed52db43cf9837e34fbcc881fc610fdf9393893ccfb33b86dad54cf5a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# get_double(3) — CS50 manual page

## 1. Source metadata
- **Title:** get_double(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/get_double>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:03+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/get_double> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/get_double#name)

get_double - prompt a user for a `double`

get_double - prompts user for a line of text from stdin and returns
the equivalent double

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/get_double#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <cs50.h>
```

<a id="prototype"></a>

#### Prototype

```c
double get_double(string prompt, ...);
```

**#include <cs50.h>**

**double get_double(const char *format, ...);**

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/get_double#description)

This function prompts the user for a `double`. If the user inputs anything other than a `double` (or a value that cannot fit in a `double`), the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](https://manual.cs50.io/3/printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the
equivalent double as precisely as possible; if text does not represent a
double or would cause underflow or overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/get_double#return-value)

This function returns the user’s input as precisely as possible as a `double`.

Returns the double equivalent to the line read from stdin in
[**DBL_MIN**, **DBL_MAX**), as precisely as
possible. If line can’t be read, returns **DBL_MAX**.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/get_double#example)

```c
#include <cs50.h>  
#include <stdio.h>  

int main(void)
{
    double d = get_double("Input:  ");
    printf("Output: %f\n", d);
}
```

> ```
> /**
>  * Returns the quotient of two doubles, or DBL_MAX on error.
>  */
> double divide_doubles(void)
> {
>     // read double from stdin
>     double d = get_double("Enter a double: ");
>
>     // make sure we read one successfully
>     if (d == DBL_MAX)
>     {
>         return DBL_MAX;
>     }
>
>     double e = get_double("What do you want to divide %lf by? ", d);
>
>     // make sure we don't divide by zero
>     if (e == DBL_MAX || e == 0.0)
>     {
>         return DBL_MAX;
>     }
>
>     return i / j;
> }
> ```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/get_double#see-also)

> ```
> get_char(3), get_float(3), get_int(3), get_long(3),
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
- https://manual.cs50.io/3/get_double — retrieved 2026-10-18T05:45:03+03:30, sha256 `90e79dfed52db43c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
