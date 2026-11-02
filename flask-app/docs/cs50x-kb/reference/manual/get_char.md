---
id: manual-get_char
type: reference
title: get_char(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/get_char
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:02+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- cs50-h
- get-char
- manual
checksum: sha256:766c9eaaef594d2911622fa0c6185aa8f4805e8af26be959fc31207e24d3b50a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# get_char(3) — CS50 manual page

## 1. Source metadata
- **Title:** get_char(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/get_char>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:02+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/get_char> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/get_char#name)

get_char - prompt a user for a `char`

get_char - prompts user for a line of text from stdin and returns the
equivalent char

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/get_char#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <cs50.h>
```

<a id="prototype"></a>

#### Prototype

```c
char get_char(string prompt, ...);
```

**#include <cs50.h>**

**char get_char(const char *format, ...);**

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/get_char#description)

This function prompts the user for a `char`. If the user inputs more or less than one `char`, the function prompts the user again.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](https://manual.cs50.io/3/printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns the
equivalent char; if text is not a single char, user is reprompted.

The prompt is formatted like **printf(3)**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/get_char#return-value)

This function returns the user’s input as a `char`.

Returns char equivalent to the line read from stdin. If line can’t be
read, returns **CHAR_MAX**.

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/get_char#example)

```c
#include <cs50.h>  
#include <stdio.h>  

int main(void)
{
    char c = get_char("Input:  ");
    printf("Output: %c.\n", c);
}
```

> ```
> int main(void)
> {
>     // attempt to read character from stdin
>     char c = get_char("Enter char: ");
>
>     // ensure character was read successfully
>     if (c == CHAR_MAX)
>     {
>         return 1;
>     }
>
>     char next = get_char("You just entered %c. Enter another char: ", c);
>
>     if (next == CHAR_MAX)
>     {
>         return 1;
>     }
>
>     printf("The last char you entered was %c\n", next);
> }
> ```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/get_char#see-also)

> ```
> get_double(3), get_float(3), get_int(3), get_long(3),
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
- https://manual.cs50.io/3/get_char — retrieved 2026-10-18T05:45:02+03:30, sha256 `766c9eaaef594d29…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
