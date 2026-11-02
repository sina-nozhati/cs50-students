---
id: tool-check50-extension-writer
type: tool
title: Writing check50 extensions ¶
week: null
parent: tool-check50
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/projects/check50/en/latest/extension_writer/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:40+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- check50-extension-writer
- tool
checksum: sha256:44f792c20022de6ccf4a8fe8326f5a094d7e0fb9541b8695c8f81bded6a22fed
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Writing check50 extensions ¶

## 1. Source metadata
- **Title:** Writing check50 extensions ¶
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/projects/check50/en/latest/extension_writer/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:40+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/projects/check50/en/latest/extension_writer/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Writing check50 extensions

Core to check50’s design is extensibility. Not only in checks, but also in the tool itself. We designed `check50.c`, `check50.py` and `check50.flask` to be extensions of check50 that ship with check50. By design these three modules are all standalone and only depend on the core of check50, and no other part of check50 depends on them. In other words, you can remove or add any of these modules and check50 would still function as expected.

We ship check50 with three extensions because these extensions are core to the material cs50 teaches. But different courses have different needs, and we realize we cannot predict and cater for every usecase. This is why check50 comes with the ability to pip install other Python packages. You can configure this via the `dependencies` key in `.cs50.yaml`. Through this mechanism you can write your own extension and then have check50 install it for you whenever check50 runs. Host your extension anywhere pip can install from, for instance GitHub or PyPi. And all you have to do then is to fill in the `dependencies` key of `.cs50.yaml` with the location of your extension. check50 will make sure your extension is always there when the checks are run.

#### check50.internal

In addition to all the functionality check50 exposes, we expose an extra API for extensions in `check50.internal`. You can find the documentation in [API docs](https://cs50.readthedocs.io/projects/check50/en/latest/api/#api).

#### Example: a JavaScript extension

Out of the box check50 does not ship with any JavaScript specific functionality. You can use check50’s generic API and run a `.js` file through an interpreter such as `node`: `check50.run('node <student_file.js>')`. But we realize most JavaScript classes are not about writing command-line scripts, and we do need a way to call functions. This is why we wrote a small javascript extension for check50 dubbed check50_js at
<https://github.com/cs50/check50/tree/sample-extension>.

##### check50_js

The challenge in writing this extension is that check50 itself is written in Python, so we need an interface between the two languages. This could be as simple as an intermediate JavaScript script that runs the students function and then outputs the results to stdout for check50 to read. But this approach does create indirection and creates quite some clutter in the checks codebase. Luckily, in case of Python and JavaScript (and PHP and Perl) we have access to a Python package called `python-bond`. This package lets us “bond” two languages together, and lets you evaluate code in another language’s interpreter. Effectively creating a channel through which you can evaluate code and call functions from the other language. This is what we ended up doing for our JavaScript extension.

You can find example checks using check50_js and their solutions at:

* **hello.js**: [checks](https://github.com/cs50/check50/tree/examples/js/hello) [solution](https://github.com/cs50/check50/tree/examples/solutions/hello_js/hello.js)
* **line.js**: [checks](https://github.com/cs50/check50/tree/examples/js/line) [solution](https://github.com/cs50/check50/tree/examples/solutions/line_js/line.js)
* **addition.js**: [checks](https://github.com/cs50/check50/tree/examples/js/addition) [solution](https://github.com/cs50/check50/tree/examples/solutions/addition_js/addition.js)

To try any of these examples for yourself, simply run:

* **hello.js**:

```
wget https://raw.githubusercontent.com/cs50/check50/examples/solutions/hello_js/hello.js
check50 cs50/check50/examples/js/hello
```

* **line.js**:

```
wget https://raw.githubusercontent.com/cs50/check50/examples/solutions/line_js/line.js
check50 cs50/check50/examples/js/line
```

* **addition.js**:

```
wget https://raw.githubusercontent.com/cs50/check50/examples/solutions/addition_js/addition.js
check50 cs50/check50/examples/js/addition
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
- https://cs50.readthedocs.io/projects/check50/en/latest/extension_writer/ — retrieved 2026-10-18T05:42:40+03:30, sha256 `44f792c20022de6c…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
