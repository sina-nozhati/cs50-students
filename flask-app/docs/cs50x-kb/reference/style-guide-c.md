---
id: reference-style-guide-c
type: reference
title: Style Guide for C
week: null
parent: reference
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/style/c/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:39+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- reference
- style-guide-c
checksum: sha256:2e2ac7b1be1560d3cdd0384f9d30c24a7a20c39ea30717a6c3539345f9b5ae6a
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Style Guide for C

## 1. Source metadata
- **Title:** Style Guide for C
- **Type:** reference
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/style/c/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:39+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/style/c/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="style-guide-for-c"></a>

### Style Guide for C

There’s no one, right way to stylize code. But there are definitely a lot of wrong (or, at least, bad ways). Even so, CS50 does ask that you adhere to the conventions below so that we can reliably analyze your code’s style. Similarly do companies typically adopt their own, company-wide conventions for style.

<a id="line-length"></a>

#### Line Length

By convention the maximum length of a line of code is 80 characters long in C, with that being historically grounded in standard-sized monitors on older computer terminals, which could display 24 lines vertically and 80 characters horizontally. Though modern technology has obsoleted the need to keep lines capped at 80 characters, it is still a guideline that should be considered a “soft stop.” With tools like `style50`, a hard limit of 100 characters is enforced, beyond which the code may not pass style checks. A line of 100 characters should really be the longest you write in C, else readers will generally need to scroll. If you need more than 100 characters, it may be time to rethink either your variable names or your overall design!

```
// These next lines of code first prompt the user to give two integer values and then multiplies those two integer values together so they can be used later in the program
int first_collected_integer_value_from_user = get_int("Integer please: ");
int second_collected_integer_value_from_user = get_int("Another integer please: ");
int product_of_the_two_integer_values_from_user = first_collected_integer_value_from_user * second_collected_integer_value_from_user;
```

In other languages, particularly JavaScript, it is significantly more difficult to constrain lines to a maximum length; there, your goal should instead be to break up lines (as via `\n`) in locations that maximize readability and clarity.

<a id="comments"></a>

#### Comments

Comments make code more readable, not only for others (e.g., your TF) but also for you, especially when hours, days, weeks, months, or years pass between writing and reading your own code. Commenting too little is bad. Commenting too much is bad. Where’s the sweet spot? Commenting every few lines of code (i.e., interesting blocks) is a decent guideline. Try to write comments that address one or both of these questions:

1. What does this block do?
2. Why did I implement this block in this way?

Within functions, use “inline comments” and keep them short (e.g., one line), else it becomes difficult to distinguish comments from code, even with [syntax highlighting](http://en.wikipedia.org/wiki/Syntax_highlighting). Place the comment above the line(s) to which it applies. No need to write in full sentences, but do capitalize the comment’s first word (unless it’s the name of a function, variable, or the like), and do leave one space between the `//` and your comment’s first character, as in:

```
// Convert Fahrenheit to Celsius
float c = 5.0 / 9.0 * (f - 32.0);
```

In other words, don’t do this:

```
//Convert Fahrenheit to Celsius
float c = 5.0 / 9.0 * (f - 32.0);
```

Or this:

```
// convert Fahrenheit to Celsius
float c = 5.0 / 9.0 * (f - 32.0);
```

Or this:

```
float c = 5.0 / 9.0 * (f - 32.0); // Convert Fahrenheit to Celsius
```

Atop your .c and .h files should be a comment that summarize what your program (or that particular file) does, as in:

```
// Says hello to the world
```

Atop each of your functions (except, perhaps, `main`), meanwhile, should be a comment that summarizes what your function is doing, as in:

```
// Returns the square of n
int square(int n)
{
    return n * n;
}
```

<a id="library-headers"></a>

#### Library Headers

Any library headers that you include should be listed in alphabetical order, as in:

```
#include <cs50.h>
#include <stdio.h>
#include <string.h>
```

This makes it easier to see at a glance, particularly in a long list, whether you have included a header.

<a id="conditions"></a>

#### Conditions

Conditions should be styled as follows:

```
if (x > 0)
{
    printf("x is positive\n");
}
else if (x < 0)
{
    printf("x is negative\n");
}
else
{
    printf("x is zero\n");
}
```

Notice how:

* the curly braces line up nicely, each on its own line, making perfectly clear what’s inside the branch;
* there’s a single space after each `if`;
* each call to `printf` is indented with 4 spaces;
* there are single spaces around the `>` and around the `<`; and
* there isn’t any space immediately after each `(` or immediately before each `)`.

To save space, some programmers like to keep the first curly brace on the same line as the condition itself, but we don’t recommend, as it’s harder to read, so don’t do this:

```
if (x < 0) {
    printf("x is negative\n");
} else if (x < 0) {
    printf("x is negative\n");
}
```

And definitely don’t do this:

```
if (x < 0)
    {
    printf("x is negative\n");
    }
else
    {
    printf("x is negative\n");
    }
```

<a id="switches"></a>

#### Switches

Declare a `switch` as follows:

```
switch (n)
{
    case -1:
        printf("n is -1\n");
        break;

    case 1:
        printf("n is 1\n");
        break;

    default:
        printf("n is neither -1 nor 1\n");
        break;
}
```

Notice how:

* each curly brace is on its own line;
* there’s a single space after `switch`;
* there isn’t any space immediately after each `(` or immediately before each `)`;
* the switch’s cases are indented with 4 spaces;
* the cases’ bodies are indented further with 4 spaces; and
* each `case` (including `default`) ends with a `break`.

<a id="functions"></a>

#### Functions

In accordance with [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), be sure to declare `main` with:

```
int main(void)
{

}
```

or, if using the CS50 Library, with:

```
#include <cs50.h>

int main(int argc, string argv[])
{

}
```

or with:

```
int main(int argc, char *argv[])
{

}
```

or even with:

```
int main(int argc, char **argv)
{

}
```

Do not declare `main` with:

```
int main()
{

}
```

or with:

```
void main()
{

}
```

or with:

```
main()
{

}
```

As for your own functions, be sure to define them similarly, with each curly brace on its own line and with the return type on the same line as the function’s name, just as we’ve done with `main`.

<a id="indentation"></a>

#### Indentation

Indent your code four spaces at a time to make clear which blocks of code are inside of others. If you use your keyboard’s Tab key to do so, be sure that your text editor’s configured to convert tabs (`\t`) to four spaces, else your code may not print or display properly on someone else’s computer, since `\t` renders differently in different editors. (If using [cs50.dev](https://cs50.dev/), it’s fine to use Tab for indentation, rather than hitting your keyboard’s space bar repeatedly, since we’ve preconfigured it to convert `\t` to four spaces.)

Here’s some nicely indented code:

```
// Print command-line arguments one per line
printf("\n");
for (int i = 0; i < argc; i++)
{
    for (int j = 0, n = strlen(argv[i]); j < n; j++)
    {
        printf("%c\n", argv[i][j]);
    }
    printf("\n");
}
```

<a id="loops"></a>

#### Loops

<a id="for"></a>

##### for

Whenever you need temporary variables for iteration, use `i`, then `j`, then `k`, unless more specific names would make your code more readable:

```
for (int i = 0; i < LIMIT; i++)
{
    for (int j = 0; j < LIMIT; j++)
    {
        for (int k = 0; k < LIMIT; k++)
        {
            // Do something
        }
    }
}
```

If you need more than three variables for iteration, it might be time to rethink your design!

<a id="while"></a>

##### while

Declare `while` loops as follows:

```
while (condition)
{
    // Do something
}
```

Notice how:

* each curly brace is on its own line;
* there’s a single space after `while`;
* there isn’t any space immediately after the `(` or immediately before the `)`; and
* the loop’s body (a comment in this case) is indented with 4 spaces.

<a id="do-while"></a>

##### do … while

Declare `do ... while` loops as follows:

```
do
{
    // Do something
}
while (condition);
```

Notice how:

* each curly brace is on its own line;
* there’s a single space after `while`;
* there isn’t any space immediately after the `(` or immediately before the `)`; and
* the loop’s body (a comment in this case) is indented with 4 spaces.

<a id="pointers"></a>

#### Pointers

When declaring a pointer, write the `*` next to the variable, as in:

```
int *p;
```

Don’t write it next to the type, as in:

```
int* p;
```

<a id="variables"></a>

#### Variables

Because CS50 uses [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), do not define all of your variables at the very top of your functions but, rather, when and where you actually need them. Moreover, scope your variables as tightly as possible. For instance, if `i` is only needed for the sake of a loop, declare `i` within the loop itself:

```
for (int i = 0; i < LIMIT; i++)
{
    printf("%i\n", i);
}
```

Though it’s fine to use variables like `i`, `j`, and `k` for iteration, most of your variables should be more specifically named. If you’re summing some values, for instance, call your variable `sum`. If your variable’s name warrants two words (e.g., `is_ready`), put an underscore between them, a convention popular in C though less so in other languages.

If declaring multiple variables of the same type at once, it’s fine to declare them together, as in:

```
int quarters, dimes, nickels, pennies;
```

Just don’t initialize some but not others, as in:

```
int quarters, dimes = 0, nickels = 0 , pennies;
```

Also take care to declare pointers separately from non-pointers, as in:

```
int *p;
int n;
```

Don’t declare pointers on the same line as non-pointers, as in:

```
int *p, n;
```

<a id="structures"></a>

#### Structures

Declare a `struct` as a type as follows, with each curly brace on its own line and members indented therein, with the type’s name also on its own line:

```
typedef struct
{
    string name;
    string dorm;
} student;
```

If the `struct` contains as a member a pointer to another such `struct`, declare the `struct` as having a name identical to the type, without using underscores:

```
typedef struct node
{
    int n;
    struct node *next;
} node;
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Reference (manual pages, style guides)](README.md) (`reference`)

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
- https://cs50.readthedocs.io/style/c/ — retrieved 2026-10-18T05:40:39+03:30, sha256 `2e2ac7b1be1560d3…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
