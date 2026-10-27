---
id: tool-style50
type: tool
title: style50
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/style50/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:57+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- style50
- tool
checksum: sha256:596744e6b1c5f7a4e4769871473297e494d88e0f4bb568faab79870635691e1c
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# style50

## 1. Source metadata
- **Title:** style50
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/style50/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:57+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/style50/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="style50"></a>

### `style50`

`style50` is a command-line tool with which you can check your code for consistency with [CS50’s style guide](https://cs50.readthedocs.io/style/c/) (for C). If your code isn’t styled consistently, `style50` will summarize the changes you should make to your code, as by highlighting in green characters you should add and highlighting in red characters you should delete.

For instance, consider the code below, wherein the call to `printf` isn’t properly indented.

```
#include <stdio.h>

int main(void)
{
printf("hello, world\n");
}
```

Given that code as input, `style50` will output

```
#include <stdio.h>
  
int main(void)
{
    printf("hello, world\n");
}
```

wherein highlighted are four spaces that should be added for style’s sake.

On the other hand, consider the code below, wherein the curly braces are unnecessarily indented.

```
#include <stdio.h>

int main(void)
    {
    printf("hello, world\n");
    }
```

Given that code as input, `style50` will output

```
#include <stdio.h>
  
int main(void)
    {
    printf("hello, world\n");
    }
```

wherein highlighted are four spaces that should be deleted for style’s sake.

<a id="usage"></a>

#### Usage

To check your code’s style, execute

```
style50 file
```

where `file` is the (path to some) file whose style you’d like to check.

<a id="modes"></a>

##### Modes

By default, `style50` operates in [`character`](https://cs50.readthedocs.io/style50/#character) mode, but you can specify other modes with `-o` or `--output`.

Consider the (poorly styled) file below, `hello.c`, for a look at these modes.

```
#include <stdio.h>

int main(void)
    {
printf("hello, world\n");
    }
```

<a id="character"></a>

###### `character`

In `character` mode, `style50` compares its input against CS50’s style guide character by character. Were you to run

```
style50 --output character hello.c
```

or just

```
style50 -o character hello.c
```

or even just

```
style50 hello.c
```

you would see the below.

```
#include <stdio.h>
  
int main(void)
{\n
    {\n
    printf("hello, world\n");
    }
```

<a id="split"></a>

###### `split`

In `split` mode, `style50` displays its input and output side by side. Were you to run

```
style50 --output split hello.c
```

or just

```
style50 -o split hello.c
```

you would see the below.

```
#include <stdio.h>               #include <stdio.h>
  
int main(void)                   int main(void)
    {                            {
printf("hello, world\n");            printf("hello, world\n");
    }                            }
```

<a id="unified"></a>

###### `unified`

In `unified` mode, `style50` displays its output line by line, akin to [`git-diff`](https://git-scm.com/docs/git-diff). Were you to run

```
style50 --output unified hello.c
```

or just

```
style50 -o unified hello.c
```

you would see the below.

```
  #include <stdio.h>
  
  int main(void)
-     {
+ {
- printf("hello, world\n");
+     printf("hello, world\n");
-     }
+ }
```

<a id="installation"></a>

#### Installation

`style50` is already installed for you in [CS50 Codespace](https://cs50.dev/), so no need to install it yourself; simply use it as directed!

If you’d like to install `style50` on your own Mac or PC, so that you can check your code’s style without using CS50 Codespace, you’ll need a command-line environment:

* If running Linux or the like, you already have one! Open a terminal window in your usual way.
* If running Mac OS, you already have one! Open **Applications > Utilities > Terminal**.
* If running Windows, you’ll need to install the [Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about), which is only supported on Windows 10. Once installed, [run `bash`](https://blogs.windows.com/buildingapps/2016/03/30/run-bash-on-ubuntu-on-windows/).

To install `style50` within that command-line environment:

1. [Install Python](https://www.python.org/downloads/) 2.7 or higher, if not already installed.
2. Install `pip`, as via

   ```
   sudo easy_install pip
   ```

   if not already installed.
3. Execute

   ```
   sudo pip3 install style50
   ```

   to install `style50` itself.
4. Install [Artistic Style 3.0](http://astyle.sourceforge.net/). If running a Debian-based operating system (e.g., Ubuntu Linux), simply run

   ```
   apt-get update
   apt-get install astyle
   ```

   to install CS50’s own compiled version of `astyle`.

<a id="upgrading"></a>

#### Upgrading

Execute

```
sudo pip install --upgrade style50
```

to upgrade `style50`, once installed.

<a id="source-code"></a>

#### Source Code

<https://github.com/cs50/style50>

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 tools (index)](README.md) (`tools`)

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
- https://cs50.readthedocs.io/style50/ — retrieved 2026-10-18T05:40:57+03:30, sha256 `596744e6b1c5f7a4…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
