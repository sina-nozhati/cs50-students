---
id: manual-fwrite
type: reference
title: fwrite(3) — CS50 manual page
week: null
parent: reference-manual
children: []
prerequisites: []
related: []
source_urls:
- https://manual.cs50.io/3/fwrite
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:45:52+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages:
- C
tags:
- c
- fwrite
- manual
checksum: sha256:1017347ab89d430b6193417fb3c8aceb844a551601df7bb35be36716ae8d2df6
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# fwrite(3) — CS50 manual page

## 1. Source metadata
- **Title:** fwrite(3) — CS50 manual page
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://manual.cs50.io/3/fwrite>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:45:52+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://manual.cs50.io/3/fwrite> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="name"></a>

### [NAME](https://manual.cs50.io/3/fwrite#name)

fwrite - write bytes to a file

fread, fwrite - binary stream input/output

<a id="library"></a>

### [LIBRARY](https://manual.cs50.io/3/fwrite#library)

Standard C library (`libc`, `-lc`)

<a id="synopsis"></a>

### [SYNOPSIS](https://manual.cs50.io/3/fwrite#synopsis)

<a id="header-file"></a>

#### Header File

```c
#include <stdio.h>
```

<a id="prototype"></a>

#### Prototype

```c
size_t fwrite(void *ptr, size_t size, size_t nmemb, FILE *stream);
```

Think of `void *` as representing the address of the first byte of any type of data. Think of `size_t` as a `long`.

```
#include <stdio.h>
size_t fread(void ptr[restrict .size * .nmemb],
 size_t size, size_t nmemb,
 FILE *restrict stream);
size_t fwrite(const void ptr[restrict .size * .nmemb],
 size_t size, size_t nmemb,
 FILE *restrict stream);
```

<a id="description"></a>

### [DESCRIPTION](https://manual.cs50.io/3/fwrite#description)

This function writes data to a file that has been opened via [fopen](https://manual.cs50.io/3/fopen). It expects as input:

* `ptr`, which is the address (of the first byte) of memory from which to read the data,
* `size`, which is the size (in bytes) of the type of data to write,
* `nmemb`, which is the number of those types to write at once, and
* `stream`, which is the pointer to a `FILE` returned by [fopen](https://manual.cs50.io/3/fopen).

For instance, if writing one `char` at a time, `size` would be `sizeof(char)` (i.e., `1`), and `nmemb` would be `1`.

The function [fread](https://manual.cs50.io/3/fread)() reads `nmemb` items of
data, each `size` bytes long, from the stream pointed to by
`stream`, storing them at the location given by `ptr`.

The function [fwrite](https://manual.cs50.io/3/fwrite)() writes `nmemb` items of
data, each `size` bytes long, to the stream pointed to by
`stream`, obtaining them from the location given by
`ptr`.

For nonlocking counterparts, see
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3).

<a id="return-value"></a>

### [RETURN VALUE](https://manual.cs50.io/3/fwrite#return-value)

This function returns the number of items written, which equals the number of bytes written when `size` is `1`.

If an error occurs, or the end of the file is reached, this function might return a value smaller than `nmemb` or even `0`.

On success, [fread](https://manual.cs50.io/3/fread)() and [fwrite](https://manual.cs50.io/3/fwrite)()
return the number of items read or written. This number equals the
number of bytes transferred only when `size` is 1. If an error
occurs, or the end of the file is reached, the return value is a short
item count (or zero).

The file position indicator for the stream is advanced by the number
of bytes successfully read or written.

[fread](https://manual.cs50.io/3/fread)() does not distinguish between end-of-file and
error, and callers must use [feof](https://manual.cs50.io/3/feof)(3) and
[ferror](https://manual.cs50.io/3/ferror)(3) to determine which occurred.

<a id="examples"></a>

### [EXAMPLES](https://manual.cs50.io/3/fwrite#examples)

```c
#include <stdio.h>  

int main(void)
{
    FILE *input = fopen("input.txt", "r");
    if (input == NULL)
    {
        return 1;
    }

    FILE *output = fopen("output.txt", "w");
    if (output == NULL)
    {
        fclose(input);
        return 1;
    }

    char c;
    while (fread(&c, sizeof(char), 1, input))
    {
        fwrite(&c, sizeof(char), 1, output);
    }

    fclose(input);
    fclose(output);
}
```

The program below demonstrates the use of [fread](https://manual.cs50.io/3/fread)() by
parsing /bin/sh ELF executable in binary mode and printing its magic and
class:

```
$ ./a.out
ELF magic: 0x7f454c46
Class: 0x02
```

<a id="program-source"></a>

#### Program source

```
#include <stdio.h>
#include <stdlib.h>
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
int
main(void)
{
    FILE           *fp;
    size_t         ret;
    unsigned char  buffer[4];
    fp = fopen("/bin/sh", "rb");
    if (!fp) {
        perror("fopen");
        return EXIT_FAILURE;
    }
    ret = fread(buffer, sizeof(*buffer), ARRAY_SIZE(buffer), fp);
    if (ret != ARRAY_SIZE(buffer)) {
        fprintf(stderr, "fread() failed: %zu\n", ret);
        exit(EXIT_FAILURE);
    }
    printf("ELF magic: %#04x%02x%02x%02x\n", buffer[0], buffer[1],
           buffer[2], buffer[3]);
    ret = fread(buffer, 1, 1, fp);
    if (ret != 1) {
        fprintf(stderr, "fread() failed: %zu\n", ret);
        exit(EXIT_FAILURE);
    }
    printf("Class: %#04x\n", buffer[0]);
    fclose(fp);
    exit(EXIT_SUCCESS);
}
```

<a id="attributes"></a>

### [ATTRIBUTES](https://manual.cs50.io/3/fwrite#attributes)

For an explanation of the terms used in this section, see
[attributes](https://manual.cs50.io/7/attributes)(7).

|  |  |  |
| --- | --- | --- |
| Interface | Attribute | Value |
| [fread](https://manual.cs50.io/3/fread)(), [fwrite](https://manual.cs50.io/3/fwrite)() | Thread safety | MT-Safe |

<a id="standards"></a>

### [STANDARDS](https://manual.cs50.io/3/fwrite#standards)

C11, POSIX.1-2008.

<a id="history"></a>

### [HISTORY](https://manual.cs50.io/3/fwrite#history)

POSIX.1-2001, C89.

<a id="see-also"></a>

### [SEE ALSO](https://manual.cs50.io/3/fwrite#see-also)

[read](https://manual.cs50.io/2/read)(2), [write](https://manual.cs50.io/2/write)(2),
[feof](https://manual.cs50.io/3/feof)(3), [ferror](https://manual.cs50.io/3/ferror)(3),
[unlocked_stdio](https://manual.cs50.io/3/unlocked_stdio)(3)

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
- https://manual.cs50.io/3/fwrite — retrieved 2026-10-18T05:45:52+03:30, sha256 `1017347ab89d430b…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
