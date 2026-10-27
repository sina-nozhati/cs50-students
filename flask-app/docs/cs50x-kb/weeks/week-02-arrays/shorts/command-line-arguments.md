---
id: short-command-line-arguments
type: short
title: 'Short: Command Line Arguments'
week: 2
parent: week-2
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/command_line_arguments/
- https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:21+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- command-line-arguments
- short
checksum: sha256:544ed2871706e1a681ce1f2e4bb06e54cd52f5a3c2aecca4a24905022b3526c8
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Command Line Arguments

## 1. Source metadata
- **Title:** Short: Command Line Arguments
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/command_line_arguments/>, <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:21+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/command_line_arguments/>, <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/command_line_arguments.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.txt>
- CS50 Video Player: <https://video.cs50.io/AI6Ccfno6Pk>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/command_line_arguments-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/command_line_arguments-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/command_line_arguments-1080p.mp4.download>
- YouTube: <https://youtu.be/AI6Ccfno6Pk>

### Transcript (verbatim, English)

```text
[MUSIC PLAYING] 

DOUG LLOYD: All right, so let's talk about command-line arguments. So, so far in the course pretty much all of your programs have probably started like this-- int main void. We've been collecting user input if we need it in our programs, such as the Mario program, for example, by in-program prompts. We haven't needed to modify the declaration of main, because instead inside of main we just say, you may call it to get int. How large do you want the pyramid to be? Or you may call it to get float-- how much change should I output to the user? 

There is another way though, and if we want our users to be able to provide data to our program at runtime instead of while the program is running, a subtle distinction but sometimes a very useful one, we need a new form of declaring main. We can't use int main void if we want to collect other data at the command-line when the user runs the program, hence command-line arguments. 

To collect these command-line arguments from the user, change your declaration of main to look like this-- int main, open paren, int argc, comma, string argv, square brackets, and then open curly brace. So what does that mean already? Well, we are passing in two parameters, or arguments, or inputs to main. One, an integer called argc, and the other is what? It's an array of strings, right? We see that square bracket notation. It's an array of strings. It's not an individual string, it's an array of strings. And these two arguments, argc and argv, enable you to know what data the user has provided at the command-line and how many things they provided at the command-line. Pretty useful things to work with. 

Argc stands for argument count, and you should know, by the way, that you could call argc whatever you want it. You can call argv whatever you wanted. These are just conventional names that we use for them-- argument count, and as we'll see in a second, argument vector, argv. But you don't have to call them argc and argv if you don't want to, but conventionally, that's what we do. 

So anyway, argc, the argument count. It's an integer-type variable and so, as you might expect, if we have two things that we're going to be finding out what these are typed and how much stuff the user typed, argc is going to tell us how much stuff the user typed. So it gives you a number of command-line arguments user typed when the program was executed. So if your program is run dot slash greedy, and inside of your greedy program your main function has the declaration int main int argc, string argv square brackets, then argc in that case is one. Now notice we don't count how many things the user typed after the program name. The program name itself counts as a command-line argument. 

So dot slash greedy, in that case, argc is one. If the user typed slash greedy 1024 CS50 at the command-line, argc in that case would be three. And we know this because the way that the division between the strings is detected is whether there is a space, or a tab, or something like that between them. So any amount of white space, so-called, between the values typed command-line indicates how many there are. So dot slash greedy space 1024 space CS50, argc, in that case, is three. 

Argv is the argument vector. Vector, by the way, is just another word for an array, and this is an array that stores strings. One string per element, which is the strings that the user actually typed at the command-line when the program was executed. Now, as is the case with any array, if you recall from our discussion of arrays, the first element of argv is always going to be found at argv square bracket zero. That's the first index of the argv array. So that will-- and in fact, that will always be the name of the program, will always be located at argv square bracket zero. 

The last element of argv is always found at argv square brackets argc minus one. Do you see why? Remember how many elements exist in this array. Well, we know that-- it's argc number of elements. If the user typed three things at the command-line, argc is three. But because in c, when we're working with arrays, each element of the array, or rather the indices of the array, start at zero. If we have three elements in our array, we have an element at argv zero, an element at argv one, and an element at argv two. There is no element at argv three, and an array of size three. So that's why the last element of argv can always be found at argv square brackets argc minus one. 

So let's assume the user executes the greedy program as follows-- if they type in the command-line dot slash greedy space 1024 space CS50, and for whatever reason we've already prepared our greedy program to know and work with these command-line arguments. We didn't previously when we worked on it for the greedy problem, but let's say we've now modified it so that we do process the command-line arguments in some way. In this case, argv zero is dot slash greedy. What's argv one? Well, it's 1024, right? It is 1024, but here's a really important distinction-- do you remember the data type of argv? 

It stores strings, right? But it looks like 1024 is an integer value. This is a really important distinction, and is actually going to become something that you might encounter in later problems. Everything in argv is stored as a string. So argv one's contents are the string one, zero, two, four, consisting of those four characters. It's as if the user typed one, zero, two, four as individual letters or characters. It is not the integer 1024, and so you can't directly work with it by saying int 1,000, or rather int x equals argv one minus 24. 

Intuitively, you might think of that as, OK, well it's 1,024 minus 24, so x is equal to 1,000. But in fact, that's not the case, because argv one is a string. The string 1024. Now there is a function that can be used to convert strings to integers. I won't spoil it for you now, but I'm sure Zamyla will be happy to tell you about it in the walkthrough for a future problem. But you can also find problems like-- excuse me, functions that would do this in reference 50, if you go to the reference guide you can find a function that will make this conversion for you. But again, in the walkthrough for a future problem, Zamyla will be happy to tell you what function it is that will convert the string 1024 to the integer 1024. 

All right, so moving on. We've covered our argv zero, we've covered argv one. What's in argv two? CS50. That one's probably pretty self-explanatory. What's in argv three? Well again, we don't really know, right? We have an array of size three, that's how many elements the user typed at the command-line, so if we go to argv three, we're now overstepping the bounds of our array. The compiler will let us do this, there's no intuitive problem with it, but in terms of actually what's going to happen, we don't really know. It depends on what is located at the memory where argv three would be expected to be. And so we could end up getting away scot free. More likely than not, particularly when you're working with argv as opposed to any other array that's in our program, we're probably going to suffer a segmentation fault. So again, be sure not to overstep the bounds of your arrays, particularly argv, given its high degree of importance in your programs. 

I'm Doug Lloyd. This is CS50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 2 — Arrays](../week.md) (`week-2`)
- **Backlinks (auto-generated):**
  - [Command-Line Arguments (argc, argv)](../../../concepts/command-line-arguments.md) (`concept-command-line-arguments`)

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
- https://cs50.harvard.edu/x/shorts/command_line_arguments/ — retrieved 2026-10-18T05:41:21+03:30, sha256 `544ed2871706e1a6…`
- https://cdn.cs50.net/2017/fall/shorts/command_line_arguments/lang/en/command_line_arguments.txt — retrieved 2026-10-18T05:41:22+03:30, sha256 `16338888025b2a61…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
