---
id: short-defining-custom-types
type: short
title: 'Short: Defining Custom Types'
week: 4
parent: week-4
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/defining_custom_types/
- https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:41+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- defining-custom-types
- short
checksum: sha256:b4d5ad1ae05beffe875d881e873dadfaef89a211dfe02e8803c494e01d2d9ece
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Defining Custom Types

## 1. Source metadata
- **Title:** Short: Defining Custom Types
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/defining_custom_types/>, <https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:41+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/defining_custom_types/>, <https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/custom_types/custom_types.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.txt>
- CS50 Video Player: <https://video.cs50.io/96M4q0OnMfY>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/custom_types/custom_types-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/custom_types/custom_types-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/custom_types/custom_types-1080p.mp4.download>
- YouTube: <https://youtu.be/96M4q0OnMfY>

### Transcript (verbatim, English)

```text
DOUG LLOYD: So if you've seen our video on structures, you already know that we have the ability to define our own data types. But if you've used structures, you know that sometimes using those data types can actually be a little cumbersome because we have to use the struct keyword when we're working with them-- struct car or struct student. That's a lot to type if we just want to have something simple, like a structure. We want to have-- we want to be able to work with things a little more shorthand way, like int or char, something a lot more convenient to type. Fortunately, there's a way to do this in C, with something called typedef, which is a way to create shorthand or rewritten names for data types. You can rewrite data types that already exist, or you can write data types of your own. 

The first thing you do is you define a type in the normal way, and then you just alias it to something else-- typedef old name new name. Pretty straightforward, right? So we could typedef for example, the already existing data type of unsigned char as byte. And then, from now on, after we've made this type definition-- again, which is usually going to be at the top of our dot C files, or in a dot H file separately, we can just use bite everywhere we would have used unsigned char. That's a lot shorter to type. 

In CS50's library, we do this-- we typedef char star as string. Because we abstracted away the idea of pointers. And the fact that a string is really a pointer to the first character-- an array of characters, because it's just so confusing to get your head around that-- but in fact that's what we do. And this line of code actually exists in CS50 dot H typedef char star string, just to make that a little less cumbersome to have to deal with. Already you've seen probably a little bit of the value here, but typedef becomes great when combined with structures, as I alluded to earlier. Structures have a two-word type name. And so they can be really annoying to create variables of that type, or [INAUDIBLE] of struct something, your lines can just get really, really long. And so you can use typedef to come up with something a lot shorter. 

So if I define a car as follows, I have my definition of a car-- struct car, and then open curly brace, all the fields of my structure, close curly brace, semi-colon-- after I've defined my data type, I can typedef struct car as car underscore t. And then when I've done that, now every time I would have otherwise used struct car, I can just use car underscore t. That's a lot shorter of a way to express this idea of this structure that I just created. 

Alternatively, because structures are so commonly used in typedef, there's a-- you can actually define the type in between the start and the end. So the typedef structure again is usually typedef, old name, new name, where the names are already types that you've created. But you can actually define a structure right in the middle of the typedef instead of having to define it separately, and then do a typedef of it. And that would look just like this-- typedef struct car, open curly brace, all of your field definitions, close curly brace, car t. So the old name is all that stuff in the red, you're just defining the structure and naming it at the same time. And then the new name is car underscore t. And so if we start to use this in code, previously I might have said, struct car mycar semi-colon. Well I don't have to do that anymore. Now that I've used the typedef, I can just say car underscore t, mycar. That's a lot shorter of a way to do it, and in fact, it's going to be a lot more convenient, especially as you start to use structures a lot more in your code. 

I'm Doug Lloyd. This is CS50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 4 — Memory](../week.md) (`week-4`)
- **Backlinks (auto-generated):**
  - [Structs and Custom Types (typedef)](../../../concepts/structs.md) (`concept-structs`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
shortها ویدیوهای کوتاه مفهومی هستند؛ برای یادگیری مستقل یا پیش‌مطالعه‌ی کلاس مناسب‌اند.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.
- مطابق [سیاست صداقت علمی CS50](https://cs50.harvard.edu/x/honesty/) هرگز پاسخ کامل، کد راه‌حل یا بخش‌هایی از راه‌حل را ارائه نده؛ فقط سؤال راهنما بپرس، مفهوم را توضیح بده و دانشجو را به بخش مرتبط صورت مسئله یا جزوه ارجاع بده.
- اگر دانشجو کد خودش را فرستاد، به‌جای اصلاح مستقیم، محل احتمالی خطا را با سؤال نشان بده (روش «اردک پلاستیکی»).
- پاسخ را به محتوای رسمی همین سند (بخش ۲) مستند کن و لینک بخش را بده؛ چیزی را که در منبع نیست به CS50 نسبت نده.

### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.harvard.edu/x/shorts/defining_custom_types/ — retrieved 2026-10-18T05:41:41+03:30, sha256 `b4d5ad1ae05beffe…`
- https://cdn.cs50.net/2017/fall/shorts/custom_types/lang/en/custom_types.txt — retrieved 2026-10-18T05:41:42+03:30, sha256 `13984813634fd7c4…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
