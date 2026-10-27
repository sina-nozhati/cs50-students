---
id: tool-check50-check-writer
type: tool
title: Writing check50 checks ¶
week: null
parent: tool-check50
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:39+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- check50-check-writer
- tool
checksum: sha256:020ce549beb1daace4e4a0933ac8d4d385d1cd4bc0c1cbd09968f2a33dbf03a6
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Writing check50 checks ¶

## 1. Source metadata
- **Title:** Writing check50 checks ¶
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:39+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Writing check50 checks

check50 checks live in a git repo on Github. check50 finds the git repo based on the slug that is passed to check50. For instance, consider the following execution of check50:

```
check50 cs50/problems/2018/x/hello
```

check50 will look for an owner called cs50, a repo called problems, a branch called 2018 or 2018/x and a problem called x/hello or hello. The slug is thus parsed like so:

```
check50 <owner>/<repo>/<branch>/<problem>
```

#### Creating a git repo

To get you started, the first thing you need to do is [register with Github](https://github.com/join). Once you have done so, or if you already have an account with Github, [create a new git repo](https://github.com/new). Make sure to think of a good name for your repo, as this is what students will be typing. Also make sure your repo is set to public, it is initialised with a README, and finally add a Python .gitignore. Ultimately you should have something looking like this:

![../_images/repo.png](https://cs50.readthedocs.io/projects/check50/en/latest/_images/repo.png)

#### Creating a check and running it

Your new repo should live at `https://github.com/<user>/<repo>`, that is `https://github.com/cs50/example_checks` in our example. Once you have created your new repo, create a new file by clicking the Create new file button:

![../_images/new_file.png](https://cs50.readthedocs.io/projects/check50/en/latest/_images/new_file.png)

Then continue by creating the following .cs50.yaml file. All indentation is done by 2 spaces, as per YAML syntax.

![../_images/new_yaml.png](https://cs50.readthedocs.io/projects/check50/en/latest/_images/new_yaml.png)

Or in text, if you want to quickly copy-paste:

**.cs50.yaml**

```
1check50:
2  checks:
3    hello world:
4      - run: python3 hello.py
5        stdout: Hello, world!
6        exit: 0
```

Note that you should create a directory like in the example above by typing: example/.cs50.yaml. Once you have populated the file with the code above. Scroll down the page and hit the commit button:

![../_images/commit.png](https://cs50.readthedocs.io/projects/check50/en/latest/_images/commit.png)

That’s it! You know have a repo that check50 can use to check whether a python file called hello.py prints `Hello, world!` and exits with a `0` as exit code. To try it, simply execute:

```
check50 <owner>/<repo>/master/example --local
```

Where you substitute <owner> for your own username, <repo> for the repo you’ve just created. Given that a file called hello.py is in your current working directory, and it actually prints `Hello, world!` when run, you should now see the following:

```
:) hello world
```

#### Simple YAML checks

To get you started, and to cover the basics of input/output checking, check50 lets you write simple checks in YAML syntax. Under the hood, check50 compiles these YAML checks to Python checks that check50 then runs.

YAML checks in check50 all live in .cs50.yaml and start with a top-level key called `check50`, that specifies a `checks`. The `checks` record contains all checks, where the name of the check is the name of the YAML record. Like so:

**.cs50.yaml**

```
1check50:
2  checks:
3    hello world: # define a check named hello world
4      # check code
5    foo: # define a check named foo
6      # check code
7    bar: # define a check named bar
8      # check code
```

This code snippet defines three checks, named `hello world`, `foo` and `bar` respectively. These checks should contain a list of `run` records, that can each contain a combination of `stdin`, `stdout` and `exit`. See below:

**.cs50.yaml**

```
 1check50:
 2  checks:
 3    hello world:
 4      - run: python3 hello.py # run python3 hello.py
 5        stdout: Hello, world! # expect Hello, world! in stdout
 6        exit: 0 # expect program to exit with exitcode 0
 7    foo:
 8      - run: python3 foo.py # run python3 foo.py
 9        stdin: baz # insert baz into stdin
10        stdout: baz # expect baz in stdout
11        exit: 0 # expect program to exit with exitcode 0
12    bar:
13      - run: python3 bar.py # run python3 bar.py
14        stdin: baz # insert baz into stdin
15        stdout: bar baz # expect bar baz in stdout
16      - run: python3 bar.py # run python3 bar.py
17        stdin:
18          - baz # insert baz into stdin
19          - qux # insert qux into stdin
20        stdout:
21          - bar baz # first expect bar baz in stdout
22          - bar qux # then expect bar qux in stdout
```

The code snippet above again defines three checks: hello world, foo and bar.

The `hello world` check runs `python3 hello.py` in the terminal, expects `Hello, world!` to be outputted in stdout, and then expects the program to exit with exitcode `0`.

The `foo` check runs `python3 foo.py` in the terminal, inserts `baz` into stdin, expects `baz` to be outputted in stdout, and finally expects the program to exit with exitcode `0`.

The `bar` check runs two commands in order in the terminal. First `python3 bar.py` gets run, `baz` gets put in stdin and `bar baz` is expected in stdout. There is no mention of `exit` here, so the exitcode is not checked. Secondly, `python3 bar.py` gets run, `baz` and `qux` get put into stdin, and first `bar baz` is expected in stdout, then `bar qux`.

We encourage you to play around with the example above by copying its code to your checks git repo. Then try to write a bar.py and foo.py that make you pass these tests.

In case you want to check for multiline input, you can make use of YAML’s `|` operator like so:

**.cs50.yaml**

```
1check50:
2  checks:
3    multiline hello world:
4      - run: python3 multi_hello.py
5        stdout: | # expect Hello\nWorld!\n in stdout
6          Hello
7          World!
8        exit: 0
```

#### Developing locally

To write checks on your own machine, rather than on the Github webpage, you can clone the repo via:

```
git clone https://github.com/<owner>/<repo>
```

Where `<owner>` is your Github username, and `<repo>` is the name of your checks repository. Head on over to the new directory that git just created, and open up .cs50.yaml with your favorite editor.

To run the cloned checks locally, check50 comes with a `--dev` mode. That will let you target a local checks repo, rather than a github repo. So if your checks live in `/Users/cs50/Documents/example_checks`, you would execute check50 like so:

```
check50 --dev /Users/cs50/Documents/example_checks/example
```

This runs the example check from `/Users/cs50/Documents/example_checks`. You can also specify a relative path, so if your current working directory is `/Users/cs50/Documents/solutions`, you can execute check50 like so:

```
check50 --dev ../example_checks/example
```

Now you’re all set to develop new checks locally. Just remember to `git add`, `git commit` and `git push` when you’re done writing checks. Quick refresher:

```
git add .cs50.yaml
git commit -m "wrote some awesome new checks!"
git push
```

#### Getting started with Python checks

If you need a little more than strict input / output testing, check50 lets you write checks in Python. A good starting point is the result of the compilation of the YAML checks. To get these, please make sure you have cloned the repo (via `git clone` ), and thus have the checks locally. First we need to run the .YAML checks once, so that check50 compiles the checks to Python. To do this execute:

```
check50 --dev <checks_dir>/<check>
```

Where `<checks_dir>` is the local git repo of your checks, and `<check>` is the directory in which `.cs50.yaml` lives. Alternatively you could navigate to this directory and simply call:

```
check50 --dev .
```

As a result you should now find a file called `__init__.py` in the check directory. This is the result of check50’s compilation from YAML to Python. For instance, if your `.cs50.yaml` contains the following:

**.cs50.yaml**

```
1check50:
2  checks:
3    hello world:
4      - run: python3 hello.py
5        stdout: Hello, world!
6        exit: 0
```

You should now find the following `__init__.py`:

**__init__.py**

```
1import check50
2
3@check50.check()
4def hello_world():
5    """hello world"""
6    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)
```

check50 will by default ignore and overwrite what is in `__init__.py` for as long as there are checks in `.cs50.yaml`. To change this you have to edit `.cs50.yaml` to:

**.cs50.yaml**

```
check50: true
```

If the `checks` key is not specified (as is the case above), `check50` will look for Python checks written in a file called `__init__.py`. If you would like to write the Python checks in a file called `foo.py` instead, you could specify it like so:

**.cs50.yaml**

```
check50:
    checks: foo.py
```

To test whether everything is still in working order, run check50 again with:

```
check50 --dev <checks_dir>/<check>
```

You should see the same results as the YAML checks gave you. Now that there are no YAML checks in `.cs50.yaml` and check50 knows where to look for Python checks, you can start writing Python checks. You can find documentation in [API docs](https://cs50.readthedocs.io/projects/check50/en/latest/api/#api), and examples of Python checks below.

#### Python check specification

A Python check is made up as follows:

**__init__.py**

```
 1import check50 # import the check50 module
 2
 3@check50.check() # tag the function below as check50 check
 4def exists(): # the name of the check
 5    """description""" # this is what you will see when running check50
 6    check50.exists("hello.py") # the actual check
 7
 8@check50.check(exists) # only run this check if the exists check has passed
 9def prints_hello():
10    """prints "hello, world\\n" """
11    check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n", regex=True).exit(0)
```

check50 uses its check decorator to tag functions as checks. You can pass another check as argument to specify a dependency. Docstrings are used as check descriptions, this is what will ultimately be shown when running check50. The checks themselves are just Python code. check50 comes with a simple API to run programs, send input to stdin, and check or retrieve output from stdout. A check fails if a `check50.Failure` exception or an exception inheriting from `check50.Failure` like `check50.Mismatch` is thrown. This allows you to write your own custom check code like so:

**__init__.py**

```
 1import check50
 2
 3@check50.check()
 4def prints_hello():
 5    """prints "hello, world\\n" """
 6    from re import match
 7
 8    expected = "[Hh]ello, world!?\n"
 9    actual = check50.run("python3 hello.py").stdout()
10    if not match(expected, actual):
11        help = None
12        if match(expected[:-1], actual):
13            help = r"did you forget a newline ('\n') at the end of your printf string?"
14        raise check50.Mismatch("hello, world\n", actual, help=help)
```

The above check breaks out of check50’s API by calling `stdout()` on line 9 with no args, effectively retrieving all output from stdout in a string. Then there is some plain Python code, matching the output through Python’s builtin regex module `re` against a regular expression with the expected outcome. If it doesn’t match, a help message is provided only if there is a newline missing at the end. This help message is provided through an optional argument `help` passed to check50’s `Mismatch` exception.

You can share state between checks if you make them dependent on each other. By default file state is shared, allowing you to for instance test compilation in one check, and then depend on the result of the compilation in dependent checks.

**__init__.py**

```
 1import check50
 2import check50.c
 3
 4@check50.check()
 5def compiles():
 6    """hello.c compiles"""
 7    check50.c.compile("hello.c")
 8
 9@check50.check(compiles)
10def prints_hello():
11    """prints "hello, world\\n" """
12    check50.run("./hello").stdout("[Hh]ello, world!?\n", regex=True).exit(0)
```

You can also share Python state between checks by returning what you want to share from a check. It’s dependent can accept this by accepting an additional argument.

**__init__.py**

```
1import check50
2
3@check50.check()
4def foo():
5    return 1
6
7@check50.check(foo)
8def bar(state)
9    print(state) # prints 1
```

#### Python check examples

Below you will find examples of Python checks. Don’t forget to [checkout CS50's own checks](https://github.com/cs50/problems) for more examples. You can try them yourself by copying them to `__init__.py` and running:

```
check50 --dev <checks_dir>/<check>
```

Check whether a file exists:

**__init__.py**

```
1import check50
2
3@check50.check()
4def exists():
5    """hello.py exists"""
6    check50.exists("hello.py")
```

Check stdout for an exact string:

**__init__.py**

```
1@check50.check(exists)
2def prints_hello_world():
3    """prints Hello, world!"""
4    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)
```

Check stdout for a rough match:

**__init__.py**

```
1@check50.check(exists)
2def prints_hello():
3    """prints "hello, world\\n" """
4    # regex=True by default :)
5    check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n").exit(0)
```

Put something in stdin, expect it in stdout:

**__init__.py**

```
1import check50
2
3@check50.check()
4def id():
5    """id.py prints what you give it"""
6    check50.run("python3 hello.py").stdin("foo").stdout("foo").stdin("bar").stdout("bar")
```

Be helpful, check for common mistakes:

**__init__.py**

```
 1import check50
 2import re
 3
 4def coins(num):
 5    # regex that matches `num` not surrounded by any other numbers
 6    # (so coins(2) won't match e.g. 123)
 7    return fr"(?<!\d){num}(?!\d)"
 8
 9@check50.check()
10def test420():
11    """input of 4.2 yields output of 18"""
12    expected = "18\n"
13    actual = check50.run("python3 cash.py").stdin("4.2").stdout()
14    if not re.search(coins(18), actual):
15        help = None
16        if re.search(coins(22), actual):
17            help = "did you forget to round your input to the nearest cent?"
18        raise check50.Mismatch(expected, actual, help=help)
```

Create your own assertions:

**__init__.py**

```
1import check50
2
3@check50.check()
4def atleast_one_match()
5    """matches either foo, bar or baz"""
6    output = check50.run("python3 qux.py").stdout()
7    if not any(answer in output for answer in ["foo", "bar", "baz"]):
8        raise check50.Failure("no match found")
```

#### Configuring check50

Check50, and other CS50 tools like submit50 and lab50, use a special configuration file called `.cs50.yaml`. Here is how you can configure check50 via `.cs50.yaml`.

##### checks:

`checks:` takes a filename specifying a file containing check50 Python checks, or a record of check50 YAML checks. If not specified, it will default to `__init__.py`.

**.cs50.yaml**

```
1check50:
2  checks: checks.py
```

Only specifies that this is a valid slug for check50. This configuration will allow you to run `check50 <slug>`, by default `check50` will look for an `__init__.py` containing Python checks.

**.cs50.yaml**

```
1check50:
2  checks: "my_filename.py"
```

Specifies that this is a valid slug for check50, and has check50 look for `my_filename.py` instead of `__init__.py`.

**.cs50.yaml**

```
1check50:
2  checks:
3    hello world:
4      - run: python3 hello.py
5        stdout: Hello, world!
6        exit: 0
```

Specifies that this is a valid slug for check50, and has check50 compile and run the YAML check. For more on YAML checks in check50 see :ref:`check_writer`.

##### files:

`files:` takes a list of files/patterns. Every item in the list must be tagged by either `!include`, `!exclude` or `!require`. All files matching a pattern tagged with `!include` are included and likewise for `!exclude`. `!require` is similar to `!include`, however it does not accept patterns, only filenames, and will cause `check50` to display an error if that file is missing. The list that is given to `files:` is processed top to bottom. Later items in `files:` win out over earlier items.

The patterns that `!include` and `!exclude` accept are globbed, any matching files are added. check50 introduces one exception for convenience, similarly to how git treats .gitignore: If and only if a pattern does not contain a `/`, and starts with a `*`, it is considered recursive in such a way that `*.o` will exclude all files in any directory ending with `.o`. This special casing is just for convenience. Alternatively you could write `**/*.o` that is functionally identical to `*.o`, or write `./*.o` if you only want to exclude files ending with `.o` from the top-level directory.

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "*.pyc"
```

Excludes all files ending with `.pyc`.

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "*"
4    - !include "*.py"
```

Exclude all files, but include all files ending with `.py`. Note that order is important here, if you would inverse the two lines it would read: include all files ending with `.py`, exclude everything. Effectively excluding everything!

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "*"
4    - !include "source/"
```

Exclude all files, but include all files in the source directory.

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "build/"
4    - !exclude "docs/"
```

Include everything, but exclude everything in the build and docs directories.

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "*"
4    - !include "source/"
5    - !exclude "*.pyc"
```

Exclude everything, include everything from the source directory, but exclude all files ending with `.pyc`.

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "source/**/*.pyc"
```

Include everything, but any files ending on `.pyc` within the source directory. The `**` here pattern matches any directory.

**.cs50.yaml**

```
1check50:
2  files:
3    - !require "foo.py"
4    - !require "bar.c"
```

Require that both foo.py and bar.c are present and include them.

**.cs50.yaml**

```
1check50:
2  files:
3    - !exclude "*"
4    - !include "*.py"
5    - !require "foo.py"
6    - !require "bar.c"
```

Exclude everything, include all files ending with `.py` and require (and include) both foo.py and bar.c. It is generally recommended to place any ``` !require``d files at the end of the ``files: ```, this ensures they are always included.

##### dependencies:

`dependencies:` is a list of `pip` installable dependencies that check50 will install.

**.cs50.yaml**

```
1check50:
2  dependencies:
3    - pyyaml
4    - flask
```

Has check50 install both `pyyaml` and `flask` via `pip`.

**.cs50.yaml**

```
1check50:
2  dependencies:
3    - git+https://github.com/cs50/submit50#egg=submit50
```

Has check50 `pip install` submit50 from GitHub, especially useful for projects that are not hosted on PyPi. See <https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support> for more info on installing from a VCS.

#### Internationalizing checks

TODO

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
- https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/ — retrieved 2026-10-18T05:42:39+03:30, sha256 `020ce549beb1daac…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
