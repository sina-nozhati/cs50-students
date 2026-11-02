---
id: tool-check50-json-specification
type: tool
title: JSON specification ¶
week: null
parent: tool-check50
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/projects/check50/en/latest/json_specification/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:38+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- check50-json-specification
- tool
checksum: sha256:ce161a123da26944894fc76ad01166ed6703f7a9c203767964574f3103d72e76
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# JSON specification ¶

## 1. Source metadata
- **Title:** JSON specification ¶
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/projects/check50/en/latest/json_specification/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:38+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/projects/check50/en/latest/json_specification/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### JSON specification

Check50 can create a machine readable output in the form of json. For instance, running check50 with -o json on a non compiling implementation of one of our problems called caesar:

```
check50 cs50/problems/2018/x/caesar -o json
```

Produces the following:

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
        }
    ],
    "version": "3.0.0"
}
```

#### Top level

Assuming check50 is able to run successfully, you will find three keys at the top level of the json output: slug, results and version.

* **slug** (string) is the slug with which check50 was run, cs50/problems/2018/x/caesar in the above example.
* **results** ([object]) is a list containing the results of each run check. More on this key below.
* **version** (string) is the version of check50 used to run the checks.

If check50 encounters an error while running, e.g. due to an invalid slug, the results key will be replaced by an error key containing information about the error encountered.

#### results

If the results key exists (that is, check50 was able to run the checks successfully), it will contain a list of objects each corresponding to a check. The order of these objects corresponds to the order the checks appear in the file in which they were written. Each object will contain the following fields:

* **name** (string) is the unique name of the check (the literal name of the Python function specifying the check).
* **description** (string) is a description of the check.
* **passed** (bool, nullable) is true if the check passed, false if the check failed, or null if the check was skipped (either because the check’s dependency did not pass or because the check threw some unexpected error).
* **log** ([string]) contains the log accrewed during the execution of the check. Each element of the list is a line from the log.
* **cause** (object, nullable) contains the reason that a check did not pass. If passed is true, cause will be null and cause will never be null if passed is not true. More detail about keys that may appear within cause below.
* **data** (object) contains arbitrary data communicated by the check via the check50.data API call. Checks could use this to add additional information such as memory usage to the results, but check50 itself does not add anything to data by default.
* **dependency** (string, nullable) is the name of the check upon which this check depends, or null if the check has no dependency.

##### cause

The cause key is null if the check passed and non-null. This key is by design an open-ended object. Everything in the .payload attribute of a check50.Failure will be put in the cause key. Through this mechanism you can communicate any information you want from a failing check to the results. Depending on what occurred, check50 adds the following keys to cause:

* **rationale** (string) is a stduent-facing explanation of why the check did not pass (e.g. the student’s program did not output what was expected).
* **help** (string) is an additional help message that may appear alongside the rationale giving additional context.
* **expected** (string) and **actual** (string) are keys that always appear in a pair. In case you are expecting X as output, but Y was found instead, you will find these keys containing X and Y in the cause field. These appear when a check raises a check50.Mismatch exception.
* **error** (object) appears in cause when an unexpected error occurred during a check. It will contain the keys type, value, traceback and data with the same properties as in the top-level error key described below.

#### error

If check50 encounters an unexpected error, the error key will replace the results key in the JSON output. It will contain the following keys:

* **type** (string) contains the type name of the thrown exception.
* **value** (string) contains the result of converting the exception to a string.
* **traceback** ([string]) contains the stack trace of the thrown exception.
* **data** (object) contains any additional data the exception may carry in its payload attribute.

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
- https://cs50.readthedocs.io/projects/check50/en/latest/json_specification/ — retrieved 2026-10-18T05:42:38+03:30, sha256 `ce161a123da26944…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
