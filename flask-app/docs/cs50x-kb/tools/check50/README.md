---
id: tool-check50
type: tool
title: check50 ¶
week: null
parent: tools
children:
- tool-check50-user
- tool-check50-check-writer
- tool-check50-extension-writer
- tool-check50-json-specification
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/projects/check50/en/latest/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:38+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- check50
- tool
checksum: sha256:98d3de995226cb6bb233d38976510176c295d1d2850aa32b775f769663dce7e1
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# check50 ¶

## 1. Source metadata
- **Title:** check50 ¶
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/projects/check50/en/latest/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:38+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/projects/check50/en/latest/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### `check50`

check50 is a tool for checking student code. As a student you can use check50 to check your CS50 problem sets or any other Problem sets for which check50 checks exist. check50 allows teachers to automatically grade code on correctness and to provide automatic feedback while students are coding.

#### Installation

First make sure you have Python 3.6 or higher installed. You can download Python [here](https://www.python.org/downloads/).

check50 has a dependency on git, please make sure to [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if git is not already installed.

To install check50 under Linux / OS X:

```
pip install check50
```

Under Windows, please [install the Linux subsystem](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Then install check50 within the subsystem.

#### Usage

To use check50 to check a problem, execute check50 like so:

```
check50 <owner>/<repo>/<branch>/<check>
```

For instance, if you want to check [CS50's Caesar problem from edX 2018](https://github.com/cs50/problems/tree/2018/x/caesar) you call:

```
check50 cs50/problems/2018/x/caesar
```

You can choose to run checks locally by passing the `--local` flag like so:

```
check50 --local <owner>/<repo>/<branch>/<check>
```

For an overview of all flags run:

```
check50 --help
```

#### Design

* **Write checks for code in code** check50 uses pure Python for checks and exposes a small Python api for common functionality.
* **Extensibility in checks** Anyone can add checks to check50 without asking for permission. In fact, here is a tutorial to get you started: [Writing check50 checks](https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/#check-writer)
* **Extensibility in the tool itself** We cannot predict everything you need, nor can we cater for every use-case out of the box. This is why check50 provides you with a mechanism for adding your own code to the tool, once more without asking for permission. This lets you support different programming languages and add new functionality. Jump to [Writing check50 extensions](https://cs50.readthedocs.io/projects/check50/en/latest/extension_writer/#extension-writer) to learn more.
* **PaaS** check50 can run online. This guarantees a consistent environment and lets you check code for correctness without introducing your own hardware.

#### Checks

In check50 the checks are decoupled from the tool. You can find CS50’s set of checks for CS50 problem sets at [/cs50/problems](https://github.com/cs50/problems). If you would like to develop your own set of checks such that you can use check50 in your own course jump to [Writing check50 checks](https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/#check-writer).

Under the hood, checks are naked Python functions decorated with the `@check50.check` decorator. check50 exposes several functions, see [API docs](https://cs50.readthedocs.io/projects/check50/en/latest/api/#api), that allow you to easily write checks for input/output testing. check50 comes with three builtin extensions: `c`, `py` and `flask`. These extensions add extra functionality for C, Python and Python’s Flask framework to check50’s core.

By design check50 is extensible. If you want to add support for other programming languages / frameworks and you are comfortable with Python please check out [Writing check50 extensions](https://cs50.readthedocs.io/projects/check50/en/latest/extension_writer/#extension-writer).

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 tools (index)](../README.md) (`tools`)
- **Children:**
  - [Running check50 ¶](check50-user.md) (`tool-check50-user`)
  - [Writing check50 checks ¶](check-writer.md) (`tool-check50-check-writer`)
  - [Writing check50 extensions ¶](extension-writer.md) (`tool-check50-extension-writer`)
  - [JSON specification ¶](json-specification.md) (`tool-check50-json-specification`)

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
- https://cs50.readthedocs.io/projects/check50/en/latest/ — retrieved 2026-10-18T05:40:38+03:30, sha256 `98d3de995226cb6b…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
