---
id: tool-submit50
type: tool
title: submit50
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/submit50/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:29+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- submit50
- tool
checksum: sha256:8dd2db1e685fa973ec710e80e658bf8a3ff001b1ab116899982d75791288a183
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# submit50

## 1. Source metadata
- **Title:** submit50
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/submit50/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:29+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/submit50/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="submit50"></a>

### `submit50`

`submit50` is a command-line tool with which you can submit work (e.g., problem sets) to a course (e.g., CS50). It’s based on `git`, a “distributed version control system” that allows you to save different versions of files without having to give each version a unique filename (as you might be wont to do on your own Mac or PC!). Via `submit50` and, in turn, `git` can you thus submit work multiple times (i.e., multiple versions thereof).

When you run `submit50`, your files are “pushed” (i.e., uploaded) to CS50’s “organization” (also named “submit50”) on [GitHub](https://github.com/), a popular service via which developers (like you!) can share code. Your files are stored in a “repository” (a folder, essentially) to which only you and some of CS50’s staff have access (and anyone else to whom you grant access). Your work can thus be reviewed and scored in one central place, whether you wrote it in [CS50 Codespace](https://cs50.dev/) or elsewhere!

<a id="installation"></a>

#### Installation

Install [Python 3.6](https://cs50.readthedocs.io/python/) or later, if you haven’t already.

<a id="using-pip"></a>

##### Using `pip`

1. Install [`pip`](https://cs50.readthedocs.io/pip/), if you haven’t already.
2. Install `submit50` itself:

   ```
   pip3 install submit50
   ```

<a id="using-pipx"></a>

##### Using `pipx`

1. Install [`pipx`](https://cs50.readthedocs.io/pipx/), if you haven’t already.
2. Install `submit50` itself:

   ```
   pipx install submit50
   ```

Note: If on Windows, please first install [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10). We recommend choosing the `Ubuntu` distribution. Then within WSL, follow the above steps to install [Python](https://cs50.readthedocs.io/python/) and `submit50`.

<a id="upgrading"></a>

##### Upgrading

If using `pip`, you can upgrade `submit50` with

```
pip3 install --upgrade submit50
```

If using `pipx`, you can upgrade `submit50` with

```
pipx upgrade submit50
```

<a id="usage"></a>

#### Usage

```
usage: submit50 [-h] [--logout] [--log-level {debug,info,warning,error}] [-V] slug

positional arguments:
  slug                  prescribed identifier of work to submit

optional arguments:
  -h, --help            show this help message and exit

  --logout              logout of submit50

  --log-level {debug,info,warning,error}
                        warning: displays usage warnings.
                        info: adds all commands run.
                        debug: adds the output of all commands run.

  -V, --version         show program's version number and exit
```

<a id="examples"></a>

#### Examples

<a id="submitting-with-submit50"></a>

##### Submitting with `submit50`

To submit work with `submit50`, `cd` to the work’s directory and execute

```
submit50 slug
```

where `slug` is the unique identifier for the work you’re submitting, as prescribed by the course (as in a problem’s specification). Although the `slug` might resemble the path to a directory, it’s simply a unique identifier, independent of your own work’s location. If you’ve not recently run `submit50` (within the past week), you might be prompted to log in with your GitHub username and password. (Per the [source code](https://github.com/cs50/submit50) for `submit50`, your username and password are sent only to GitHub, not to CS50’s own servers.) You will then be prompted to confirm whether you indeed want to submit one or more files from your current directory, unless you’re missing one or more required files, in which case `submit50` will instead exit without submitting anything.

<a id="via-ssh"></a>

###### Via SSH

By default, `submit50` pushes your work to GitHub via HTTPS, which requires your GitHub username and password, which is why `submit50` prompts you for both at least once per week. If you’d prefer not to provide `submit50` with your GitHub username and password at all, you can instead push your work to GitHub via SSH. Configure your workspace on [CS50 Codespace](https://cs50.dev/) (or your own computer) as follows.

1. [Generate an SSH key and add it to `ssh-agent`](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).
2. [Add the SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).
3. Execute

   ```
   ssh -T -p443 git@ssh.github.com
   ```

   to add `ssh.github.com` to the list of known hosts for `ssh`, answering “yes” if prompted whether you’re sure you want to continue connecting. If all goes well, you should see the message

   ```
   Hi <USERNAME>! You've successfully authenticated, but GitHub does not provide shell access.
   Connection to github.com closed.
   ```

(where `<USERNAME>` is your GitHub username).

Thereafter, you should be able to run `submit50` without ever being prompted for your GitHub username or password.

<a id="submitting-without-submit50"></a>

##### Submitting without `submit50`

If comfortable with `git`, you can submit work without `submit50`. Simply push your work to the expected branch (i.e., the work’s prescribed slug which is found in the “How to Submit” section of each project.) of `https://github.com/me50/jharvard` (or `git@github.com:me50/jharvard.git`), where `jharvard` is your own GitHub username. To get started, either clone that repository or add it to an existing repository as a remote.

On each such branch, take care to create a `.gitignore` file based on `https://raw.githubusercontent.com/slug/.cs50.yml`, where `slug` is as before, so that you don’t submit files that `submit50` would otherwise ignore.

Note again that the branch should not be `main`, `master` or the like, and instead be the work’s prescribed slug as listed in the project specification.

<a id="implementation-details"></a>

#### Implementation Details

To see how `submit50` uses `git` underneath the hood, execute

```
submit50 --log-level info slug
```

or

```
submit50 --log-level debug slug
```

where `slug` is the unique identifier for the work you’re submitting.

<a id="faqs"></a>

#### FAQs

<a id="do-i-need-to-provide-submit50-with-my-github-username-and-password"></a>

##### Do I need to provide `submit50` with my GitHub username and password?

Nope, you can instead authenticate [via SSH](https://cs50.readthedocs.io/submit50/#via-ssh).

<a id="if-i-use-git-locally-will-submit50-affect-my-local-repository"></a>

##### If I use `git` locally, will `submit50` affect my local repository?

Nope, `submit50` uses its own `GIT_DIR` (in `/tmp`). It will ignore any `.git` directory that you might have locally.

<a id="how-does-submit50-remember-my-github-password"></a>

##### How does `submit50` remember my GitHub password?

`submit50` remembers your username and password in RAM using [`git-credential-cache`](https://git-scm.com/docs/git-credential-cache/). Your password is never stored on disk or transmitted elsewhere.

<a id="source-code"></a>

#### Source Code

<https://github.com/cs50/submit50>

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
- https://cs50.readthedocs.io/submit50/ — retrieved 2026-10-18T05:42:29+03:30, sha256 `8dd2db1e685fa973…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
