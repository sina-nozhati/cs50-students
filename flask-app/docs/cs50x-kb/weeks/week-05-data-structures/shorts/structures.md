---
id: short-structures
type: short
title: 'Short: Structures'
week: 5
parent: week-5
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/structures/
- https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:47+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- short
- structures
checksum: sha256:11f57cc9319e26aa304faa3b77c6beb7bc28b0de5e344c6ce97103e8eca6ec11
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Structures

## 1. Source metadata
- **Title:** Short: Structures
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/structures/>, <https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:47+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/structures/>, <https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/structures/structures.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.txt>
- CS50 Video Player: <https://video.cs50.io/E4lb2gkyXr8>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/structures/structures-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/structures/structures-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/structures/structures-1080p.mp4.download>
- YouTube: <https://youtu.be/E4lb2gkyXr8>

### Transcript (verbatim, English)

```text
[MUSIC PLAYING] 

DOUG LLOYD: OK. We've worked with integers, we've worked with characters, we've worked floats, doubles, strings, and bools. We've exhausted pretty much all of the [INAUDIBLE] types that have been available to us all along. But now we want to do something more. How do we do that? How do we create different data types? We can do so by using structures. So structures allow us to unify variables of different types into a single, new variable type, which we can assign its own type name. This is a really strong thing to be able to do, because we can now group elements of different data types together that have a logical connection. We've been able to do this with arrays sort of, right? We can group variables of the same data type together in a large unit of memory, an array. 

But we haven't been able to mix up different data types together. We can't, say, pair an integer, and a character, and a double all in the same thing and call that a single unit. But with structures, or frequently referred to as structs, we actually can. So a structure is sort of like a super variable. It's a variable that contains other variables inside of it. So here's an example of a very simple structure. This is what the syntax would look like to create a structure for a car. Now, let's go through the syntax here. Struct, that's the keyword that indicates that I'm creating a new data type here. In particular, the data type's name is going to be struct car, as we'll see. But this is the sort of tip off to the compiler that this as a group of variables that is going to be considered part of the same type in a minute. 

Cars, just the name of the structure. Again, the data type here is going to be struct car, not just car. But if you have different-- if you create multiple structs in the same program, you need to distinguish between struct and struct. So struct car, I might also have struct student, for example, in the same program. Inside of the curly braces are all of the so-called fields, or members of the structure. So what are some of the things that are inherent in a car? Well, it usually has a year, has a model name, and a license plate, an odometer that usually has some number of miles on it, and maybe an engine size. And as you can see, I'm mixing up integers and characters and doubles. They're all going to be part of this new data type. 

Lastly, the final thing I need to do, don't forget this little semicolon at the end. After we finish defining the structure, we need to put a semicolon at the end. It's a very common syntactical mistake, because with a function, for example, you would just have open curly brace, close curly brace. You don't put a semicolon at the end of a function definition. This looks like a function definition, but it's not, and so the semicolon there is just a reminder that you need to put it there, because the compiler will otherwise not know what to do with it. It's a very common error to accidentally make when you're first defining structures. 

OK. So we usually define our structures at the very top of our programs because they're probably going to be used by multiple functions. We don't want to define a struct inside of a function, because then we can only-- the scope of the structure really only exists inside of that function. We'd probably want to define a structure so we can use it in multiple functions, or perhaps in multiple files that are tied together to create our single program. Sometimes also instead of defining the structure at the very top where you put your pound includes and your pound defines, for example, you might put them in separate dot h files, which you then pound include yourself. 

So we have structures, but now we need to get inside of them. How do we get inside of a structure to access those sub-variables, those variables that exist inside the structure? Well, we have something called the dot operator, which allows us to access the fields of the structure. So for example, let's say I've declared my structure data type somewhere at the top of my program, or perhaps in a dot h file that I've pound included. If I then want to create a new variable of that data type, I can say, struct car, my car, semicolon. Just like I could say int x, or string name semicolon. 

The data type here is struct car, the name of the variable is my car, and then I can use the dot operator to access the various fields of my car. So I can say my car dot year equals 2011. That's perfectly fine. Year, if you recall, was defined as an integer field inside of this struct car data type. So any variable of the struct car data type, such as my car, I can say my car dot year equals and then assign it some integer value, 2011. My car dot plate equals CS50. My card dot odometer equals 50505 semicolon. All of those are perfectly fine and that's how we access the fields of the structure. Structures, though, do not need to be created on the stack. Just like any other variable, we can dynamically allocate them. If we have a program that might be generating many structures, we don't know how many we're going to need, then we need to dynamically allocate those structures as our program is running. And so if we're going to access the fields of a structure in that context, recall that we first need to dereference the pointer to the structure, and then once we dereference the pointer, then we can access the fields. If we only have a pointer to the structure, we can't just say pointer dot field name and get what we're looking for. There's the extra step of dereferencing. So let's say that instead of the previous-- just like the previous example, instead of declaring it on the stack, struct car, my car, semicolon, I say struct car, star, a pointer to a struct car called my car, equals malloc size of struct car. Size of we'll figure out how many bytes your new data type takes up. You don't necessarily only need to use size of, width, int, or char, or any of the built-in data types. The compiler is smart enough to figure out how many bytes are required by your new structure. So I malloc myself a unit of memory big enough to hold a struct car, and I get a pointer back to that block of memory, and that pointer is assigned to my car. 

Now, if I want to access the fields of my car, I first dereference my car using the dereference operator, star that we've seen from the pointers videos, and then after I dereference, then I can use the dot operator to access the various fields of my car. Star my car dot year equals 2011. That would have the effect we want in this case, because we've dynamically allocated my car. 

That's kind of annoying, though, right? There's a 2-step process now. Now we have to dereference-- we have a star operator, and we have a dot operator. And as you might expect, because C programmers love shorter ways to do things, there is a shorter way to do this. There is another operator called arrow, which makes this process a lot easier. The way arrow works is it first dereferences the pointer on the left side of the operator, and then, after having dereferenced the pointer on the left, it accesses the field on the right. And so previously we had this sort of star my car dot all this stuff, like there was a lot going on there. But what we can instead do is this-- my car arrow year equals 2011. 

Again, what's happening here? First, I'm dereferencing my car. Which again, is a pointer here. Then, after having dereferenced my car, I can then access the fields year, plate, and odometer just as I could before having first used star to dereference my car, and dot to access the field. So you can have structures, you can have pointers to structures, and you have ways to access the fields of those structures, whether you have pointers to them or the variables themselves. Dot or arrow, depending on how the variable was declared. I'm Doug Lloyd, this is CS50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 5 — Data Structures](../week.md) (`week-5`)
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
- https://cs50.harvard.edu/x/shorts/structures/ — retrieved 2026-10-18T05:41:47+03:30, sha256 `11f57cc9319e26aa…`
- https://cdn.cs50.net/2017/fall/shorts/structures/lang/en/structures.txt — retrieved 2026-10-18T05:41:48+03:30, sha256 `841768ef92ab3593…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
