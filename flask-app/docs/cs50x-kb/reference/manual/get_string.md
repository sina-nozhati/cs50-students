---
id: manual-get_string
type: reference
title: get_string(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/get_string
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:08+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- cs50-h
- get-string
- manual
checksum: sha256:5b0e09784cb3a627eb131babfdb4a38cd3e38451a1fea60bbcd51bafffd20831
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# get_string(3) — CS50 manual page

## 1. Source metadata
- **Title:** get_string(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/get_string>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:08+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/get_string> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/get_string#name)

get_string - prompt a user for a `string`

get_string - prompts user for a line of text from stdin and returns
it as a string

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/get_string#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <cs50.h>
```

<a id="prototype"></a>

#### Prototype

```c
string get_string(string prompt, ...);
```

**#include <cs50.h>**

**char *get_string(const char *format, ...);**

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/get_string#description)

This function prompts the user for a `string`.

This function expects at least one argument, `prompt`. If `prompt` contains any format codes, a la [printf](https://manual.cs50.io/3/printf), this function accepts additional arguments as well, one per format code.

Prompts user for a line of text from standard input and returns it as
a string (char *), sans trailing line ending. Supports CR (\r), LF (\n),
and CRLF (\r\n) as line endings. Stores string on heap, but library’s
destructor frees memory on program’s exit.

The prompt is formatted like **printf(3)**.

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/get_string#return-value)

This function returns the user’s input as a `string`.

Returns the read line as a string. If user inputs only a line ending,
returns "", not NULL. Returns NULL upon error or no input whatsoever
(i.e., just EOF).

<a id="example"></a>

### [EXAMPLE](https://manual.cs50.io/3/get_string#example)

```c
#include <cs50.h>  
#include <stdio.h>  

int main(void)
{
    string s = get_string("Input:  ");
    printf("Output: %s\n", s);
}
```

> ```
> int main(void)
> {
>     string s = get_string("Enter string: ");
>
>     // ensure string was read
>     if (s == NULL)
>     {
>         return 1;
>     }
>
>     string next = get_string("You just entered %s. Enter a new string: ", s);
>
>     if (next == NULL)
>     {
>         return 1;
>     }
>
>     printf("Your last string was %s\n", s);
> }
> ```

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/get_string#see-also)

> ```
> get_char(3), get_double(3), get_float(3), get_int(3),
> get_long(3), printf(3)
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
- https://manual.cs50.io/3/get_string — retrieved 2026-10-18T05:45:08+03:30, sha256 `5b0e09784cb3a627…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
