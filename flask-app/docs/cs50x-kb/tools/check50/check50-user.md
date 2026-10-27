---
id: tool-check50-user
type: tool
title: Running check50 ¶
week: null
parent: tool-check50
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/projects/check50/en/latest/check50_user/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:37+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- check50-user
- tool
checksum: sha256:19b1fd76239d4624c5d9a08c404317f3b245073772f9d5a132257fd776935e1a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Running check50 ¶

## 1. Source metadata
- **Title:** Running check50 ¶
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/projects/check50/en/latest/check50_user/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/projects/check50/en/latest/check50_user/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Running check50

#### Slug

check50 requires one positional argument, a so called slug. Something like this:

```
check50 cs50/problems/2018/x/caesar
```

Why? Well, anyone can write checks for check50 without needing to ask for permission. To achieve this goal check50, the tool, is decoupled from any of its checks. The checks themselves are hosted anywhere on a popular hosting platform for code, GitHub. All you need to do to add your own checks is to put them on anywhere on GitHub. With this flexibility comes a price, as check50 does not know where your checks live on GitHub. In order to uniquely identify a collection of checks on GitHub check50 needs the following:

* org
* repository
* branch
* path to problem

These four pieces of information separated by a / is what check50 calls a slug, a string that uniquely identifies a set of checks. For instance the slug `cs50/problems/2018/x/caesar` uniquely identifies the org `cs50`, the repository `problems`, the branch `2018/x` and the path `caesar`.

#### Operation modes

Check50 can run in four mutually exclusive modes of operation.

##### online

By default check50 runs the checks remotely and then waits for the results to come back.

##### local

To run checks locally, pass the `--local` flag. The checks are still fetched remotely from GitHub.

##### offline

Running with `--offline` runs the checks locally and has check50 look for checks locally. check50 will not try to fetch checks remotely in this mode.

##### dev

The `--dev` flag signals check50 to run in developer mode. This implies `--offline`. More on this mode in [Writing check50 checks](https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/#check-writer).

#### Additional output

By default check50 will try to keep its output concise in its `ansi` output mode. For each check you will see at most its description and rationale/help on why the check failed. check50 will by default hide tracebacks and log output. You can show both by running check50 with the `--verbose` flag, or just the log with the `--log` flag.

##### verbose

Running with `--verbose` lets check50 output any tracebacks in the `ansi` output mode.

##### log-level

Running check50 with `--log-level INFO` will display any git commands run. `--log-level DEBUG` adds all output of any git commands run.

#### Targeting checks

Check50 lets you target specific checks by name with the `--target` flags. This will have check50 run just these checks and their dependencies.

##### target

With `--target` you can target checks from a larger body of checks by name. check50 will only run and show these checks and their dependencies.

#### Output modes

check50 supports three output modes: `ansi`, `html` and `json`. In short, the `ansi` output mode is text-based output meant to be displayed in a terminal. `html` is an extension of `ansi` showing the same results but in a webpage. This allows for visual comparisons and more information to be displayed in general. Finally, the `json` output mode provides a machine readable form of output, that can for instance be used for automatic grading.

The output modes can be mixed and matched through the `--output` or `-o` flag.

```
check50 <slug> -o ansi
check50 <slug> -o ansi html # equivalent to check50 <slug>
check50 <slug> -o json
```

By default check50 shows both `ansi` and `html` output.

##### ansi

The `ansi` output mode will have check50 print the results from the checks to stdout. This output mode keeps students in the terminal, the environment in which they are running check50 in the first place. Limited by its nature, check50’s `ansi` output mode is not suited for large pieces of text or visual comparisons. The output format is sufficient for showing which checks passed and failed, and offering short text based help or explanation on those checks.

![../_images/ansi_output.png](https://cs50.readthedocs.io/projects/check50/en/latest/_images/ansi_output.png)

##### html

In addition to `ansi`, check50 comes with a `html` output mode. This output mode allows check50 to show results side by side and to display more verbose information like the log by default. check50 creates a local self contained static html file in `/tmp` and will output the path to file in stdout.

![../_images/html_output.png](https://cs50.readthedocs.io/projects/check50/en/latest/_images/html_output.png)

##### json

check50 can provide machine readable output in the form of `json`. By default this output mode will print to stdout, but like any other form of output check50 can write to a file with the `--output-file` command line option. For a complete overview of the `json` output please refer to the [JSON specification](https://cs50.readthedocs.io/projects/check50/en/latest/json_specification/#json-specification).

```
{
    "slug": "cs50/problems/2018/x/caesar",
    "results": [
        {
            "name": "exists",
            "description": "caesar.c exists.",
            "passed": true,
            "log": [
                "checking that caesar.c exists..."
            ],
            "cause": null,
            "data": {},
            "dependency": null
        },
        {
            "name": "compiles",
            "description": "caesar.c compiles.",
            "passed": false,
            "log": [
                "running clang caesar.c -o caesar -std=c11 -ggdb -lm -lcs50...",
                "caesar.c:24:5: warning: implicit declaration of function 'f' is invalid in C99",
                "      [-Wimplicit-function-declaration]",
                "    f (argc != 2)",
                "    ^",
                "caesar.c:24:18: error: expected ';' after expression",
                "    f (argc != 2)",
                "                 ^",
                "                 ;",
                "1 warning and 1 error generated."
            ],
            "cause": {
                "rationale": "code failed to compile",
                "help": null
            },
            "data": {},
            "dependency": "exists"
        },
        {
            "name": "encrypts_a_as_b",
            "description": "encrypts \"a\" as \"b\" using 1 as key",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        },
        {
            "name": "encrypts_barfoo_as_yxocll",
            "description": "encrypts \"barfoo\" as \"yxocll\" using 23 as key",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        },
        {
            "name": "encrypts_BARFOO_as_EDUIRR",
            "description": "encrypts \"BARFOO\" as \"EDUIRR\" using 3 as key",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        },
        {
            "name": "encrypts_BaRFoo_FeVJss",
            "description": "encrypts \"BaRFoo\" as \"FeVJss\" using 4 as key",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        },
        {
            "name": "encrypts_barfoo_as_onesbb",
            "description": "encrypts \"barfoo\" as \"onesbb\" using 65 as key",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        },
        {
            "name": "checks_for_handling_non_alpha",
            "description": "encrypts \"world, say hello!\" as \"iadxp, emk tqxxa!\" using 12 as key",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        },
        {
            "name": "handles_no_argv",
            "description": "handles lack of argv[1]",
            "passed": null,
            "log": [],
            "cause": {
                "rationale": "can't check until a frown turns upside down"
            },
            "data": {},
            "dependency": "compiles"
        }
    ],
    "version": "3.0.0"
}
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [check50 ¶](README.md) (`tool-check50`)

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
- https://cs50.readthedocs.io/projects/check50/en/latest/check50_user/ — retrieved 2026-10-18T05:42:37+03:30, sha256 `19b1fd76239d4624…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
