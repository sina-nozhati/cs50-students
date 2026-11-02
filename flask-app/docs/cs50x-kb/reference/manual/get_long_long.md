---
id: manual-get_long_long
type: reference
title: get_long_long(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/get_long_long
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:07+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- cs50-h
- get-long-long
- manual
checksum: sha256:d3d34a8b3eb9053a45a027af4e43c6acf19c135c6e9fe0857478707d4aa2e542
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# get_long_long(3) — CS50 manual page

## 1. Source metadata
- **Title:** get_long_long(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/get_long_long>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:07+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/get_long_long> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/get_long_long#name)

get_long_long - prompts user for a line of text from stdin and
returns the equivalent long long

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/get_long_long#synopsis)

**#include <cs50.h>**

**long long get_long_long(const char *format,
...);**

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/get_long_long#description)

Prompts user for a line of text from standard input and returns the
equivalent long long; if the text does not represent a long long or
would cause overflow, user is reprompted.

The prompt is formatted like **printf(3)**.

This function will be deprecated in favor of
**get_long(3)**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/get_long_long#return-value)

Returns the long long equivalent to the line read from stdin in
[**LLONG_MIN**, **LLONG_MAX**). If line can’t
be read, returns **LLONG_MAX**.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/get_long_long#example)

> ```
> /**
>  * Returns the difference of two long longs read from stdin, or LLONG_MAX if there was an error.
>  */
> long long subtract_long_longs(void)
> {
>     // read long long from stdin
>     long long i = get_long_long("Enter a long long: ");
>
>     // make sure we read one successfully
>     if (i == LLONG_MAX)
>     {
>         return LLONG_MAX;
>     }
>
>     long long j = get_long_long("What do you want to subtract from %lld? ", i);
>
>     if (j == LLONG_MAX)
>     {
>         return LLONG_MAX;
>     }
>
>     return i - j;
> }
> ```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/get_long_long#see-also)

> ```
> get_char(3), get_double(3), get_float(3), get_int(3), get_long(3),
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
- https://manual.cs50.io/3/get_long_long — retrieved 2026-10-18T05:45:07+03:30, sha256 `d3d34a8b3eb9053a…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
