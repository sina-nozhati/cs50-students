---
id: tool-help50
type: tool
title: help50
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/help50/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:28+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- help50
- tool
checksum: sha256:7e4e94524e0c5ca24ec3ed24ae95aba46494538157de4438e3bbe6ec9ea0dcfb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# help50

## 1. Source metadata
- **Title:** help50
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/help50/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:28+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/help50/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="help50"></a>

### `help50`

`help50` is a command-line tool with which you can get help understanding error messages in your terminal window. Rather than something you run yourself, it runs automatically: whenever a command fails, `help50` looks at the command’s output. If it recognizes the error, it offers a hint in yellow right below it. If it doesn’t, and you’re in [CS50 Codespace](https://cs50.dev/), it offers a **help50** button atop your terminal window instead, which you can click to ask the [CS50 Duck](https://cs50.readthedocs.io/cs50.ai/) to explain the error.

For instance, were you to mistype `ls` as `1s`, you would see

```
$ 1s
bash: 1s: command not found
Did you mean to run `ls` (which starts with a lowercase L)?
```

wherein the last line is `help50`’s hint. Or were you to try to compile `hello.c` with `make hello.c` instead of `make hello`, you would see

```
$ make hello.c
make: Nothing to be done for 'hello.c'.
Did you mean to run `make hello` instead?
```

And were you to run a command whose error `help50` doesn’t recognize, you would see

```
$ cat nothere
cat: nothere: No such file or directory
🦆 Click `help50` above for help with that error.
```

along with a **help50** button atop your terminal window. Click it, and the duck will be asked to explain what you ran and what happened. The button disappears once you’ve clicked it or run another command.

Among the errors that `help50` recognizes are misspelled or miscapitalized commands, running a file instead of compiling it (e.g., `./hello.c`), running a program that you haven’t recompiled since editing it, a `cd` or `make` or `python` that refers to a file or directory that’s in some other directory, `check 50` instead of `check50`, and a Python file of your own (e.g., `cs50.py`) that “shadows” a module of the same name.

<a id="usage"></a>

#### Usage

Nothing to run! Simply run commands as usual, and help appears when a command fails. `help50` ignores commands that fail without any output (e.g., `grep` that finds no matches) and commands that you interrupt with control-c.

If you’re accustomed to running

```
help50 make hello
```

from earlier versions of `help50`, that still works: it simply runs `make hello` for you, and help appears as it would have anyway.

`help50` also supports a few commands of its own:

| Command | Effect |
| --- | --- |
| `help50 status` | Reports whether `help50` is `started` or `stopped` in the current terminal window. |
| `help50 stop` | Stops `help50` in the current terminal window. |
| `help50 start` | Starts `help50` again in the current terminal window. |
| `help50 disable` | Keeps `help50` from starting in new terminal windows. |
| `help50 enable` | Undoes `help50 disable`. |
| `help50 is-enabled` | Reports whether `help50` is `enabled` or `disabled`. |

<a id="installation"></a>

#### Installation

`help50` is already installed for you in [CS50 Codespace](https://cs50.dev/), so no need to install it yourself; simply use it as directed!

`help50` is part of [`cs50/cli`](https://cs50.readthedocs.io/cs50/cli/), CS50’s Docker image, so it’s also available via [`cli50`](https://cs50.readthedocs.io/cli50/), though without the **help50** button (and thus the duck), which is a feature of CS50 Codespace.

<a id="source-code"></a>

#### Source Code

* <https://github.com/cs50/cli>, for `help50` itself and its helpers
* <https://github.com/cs50/help50.vsix>, for the **help50** button in CS50 Codespace

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
- https://cs50.readthedocs.io/help50/ — retrieved 2026-10-18T05:42:28+03:30, sha256 `7e4e94524e0c5ca2…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
