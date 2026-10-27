---
id: short-magic-numbers
type: short
title: 'Short: Magic Numbers'
week: 1
parent: week-1
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/magic_numbers/
- https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:40:58+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- magic-numbers
- short
checksum: sha256:8e51079e1239cf68fe2f93c248f54db8adca0c2a7015ee5876d0034ec419d04e
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Magic Numbers

## 1. Source metadata
- **Title:** Short: Magic Numbers
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/magic_numbers/>, <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:40:58+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/magic_numbers/>, <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/magic_numbers.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.txt>
- CS50 Video Player: <https://video.cs50.io/vK_naJkrtjc>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/magic_numbers-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/magic_numbers-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/magic_numbers/magic_numbers-1080p.mp4.download>
- YouTube: <https://youtu.be/vK_naJkrtjc>

### Transcript (verbatim, English)

```text
[MUSIC PLAYING] DOUG LLOYD: All right. Kind of a strange topic, right? Magic numbers. What doe he mean when he's talking about magic numbers? Well, some of the programs that we've written in CS50 so far have had some weird numbers kind of thrown in them. Perhaps for reasons we don't entirely understand right now. For example, in the Mario problem, we capped the height of the pyramid at 23. We explicitly said you can't go higher than 23. 

But what does 23 mean? Well, if you read the spec carefully, you might have seen that the reason we capped it at 23 is because the standard height of a terminal window is 24. And so if we have the pyramid be taller than that, it might do this weird thing where it runs off the screen. And you know, what does that mean in context, right? 

Is the meaning of 23 immediately obvious to somebody who looks at your program and maybe has a different size terminal window? Probably not. It seems like, OK. Well, why is it just less than 23? In general, it's kind of a bad habit actually to write constants into your code. In doing so, when you actually do write a constant into your code, it's sometimes referred to as using magic numbers, which is something we generally want to try and avoid. 

For example, let's take a look at this simple function here. Obviously there's no data type in C called card or deck. So just bear with me. It's a little bit of pseudocode mixed in here. This is a function called deal card that apparently takes a deck as its parameter, and will output to me a single card. 

And I'm doing something here where I have a loop that runs from 0 to 52, and I deal a card. Well, we've got a magic number in here, right. Do you see what the magic number is? Or more importantly, do you see what the problem is here? Particularly if this is just one function in its own file in a folder that contains a bunch of different files, each of which does another thing to a deck of cards. Maybe it shuffles them, or deals a hand of five cards instead of a single card. 

Do you see what the problem could be here? Do you see the magic number I've injected into the code? It's 52, right. 

Like, intuitively you probably know, OK. Like a standard deck of cards contains 52 cards. But in our program, it's just kind of floating around in there. It's like all of a sudden there's a 52. 

One way to resolve this problem is to do this. We're very explicitly now calling out the deck size as 52. It gives it a little more intuitive meaning when in the for loop later on we then say, i is less than deck size. It just seems better than saying 52. Now this does actually fix the problem. It does give some symbolic meaning to the constant. But it does kind of actually introduce another problem that might not be immediately apparent. Even if this variable is declared globally-- do you recall what it means when we declare a variable globally versus locally? Even if we declare a variable globally, what if there's another function in our suite of functions that deal with card manipulation that inadvertently changes deck size, or it increases it by 1 or decreases it by 1. That could spell trouble, right? Especially if we're dealing with a set of cards where shuffling the full deck is required. If deck size is decreased by 1, for example, to 51, we're not actually shuffling all the cards possibly. We're leaving one of them out. And that value could perhaps be predicted or exploited by a bad actor. 

C provides what's called a preprocessor directive, which is also called a macro for creating symbolic constants. And in fact, you've already seen a preprocessor directive, even if you haven't heard it called that with #include. It's another example of a macro or preprocessor directive. 

The way to create symbolic constants, or giving a name to a constant so that it has more meaning, is as follows. #define, name, replacement. Really important aside here really quick. Don't put a semicolon at the end of your #defines. So it's #define, name, replacement. 

When your program is compiled, what actually happens is the compiler if going to go through your code and replace every instance of the word "name" with whatever you put as replacement. Analogously, if #include is sort of similar to copying and pasting, then #define is sort of similar to find and replace, if you've ever used that feature in a word processing program, for example. 

So for example, if I #define pi as 3.14159265, if you're better mathematically inclined and you suddenly see 3.14159265 flying around in your code, you probably know it's talking about pi. But maybe we can give it a little more symbolic meaning. And we can instead say #define pi as that mouthful of numbers that I'm not going to keep reading over and over. 

And what's going to happen then at compile time is when the program is compiled, the first thing that will happen is it will go through and it will replace every time it sees capital P, capital I, it'll literally replace it with 3.14 and so on, so that you don't have to type it every time while your program still has the functionality that you expect, because you're working with manipulating, multiplying, dividing, whatever it is by pi. 

You are not limited to this substitution for numbers only. For example, I could #define course as the string CS50. In this case, when the program is compiled, #define will go through the code, replace every time it sees "course" with the string CS50. 

You'll notice here also that I frequently #define all my defined symbolic constants, so to speak, are always in all caps. It's a convention. It's not required. The reason generally people will use all capitals when they're #defining is just to make it really clear that this particular element of my code is a defined constant. If it was lowercase, it's possible that it might be confused with a variable. And that's probably not a good thing to do. 

So this particular solution is much better than either of the previous ones. If I first #define deck size 52, then now my use of 52, or deck size here, is a lot more intuitive and a lot safer. You can't manipulate a constant. You can't say 52 plus plus. That's not going to convert it to 53. You can't change 52 to something. 

You can change a variable whose value is 52, which was the first fix we had before. And you could increase that variable to 53. But you can't say 52 plus plus and have that suddenly turn 52 into 53. 52 is always 52. And so you can't inadvertently change deck size here by manipulating it, 

Another good side effect of this though is that are you aware that not all countries around the world use a deck of cards of size 52? For example, it's really common in Germany to use a deck size of 32, where they strip out some of the lower value cards. And in this case, I wanted to port my suite of functions that deal with card manipulation to Germany. I could in the first instance we showed, have to go and replace all instances of 52 in my code with 32. 

But here, if I #define deck size as 32 at the very top of my code, if I need to change it, I can just go and change that one thing. Recompile my code, and all of a sudden it propagates through. In fact, we can change deck size to any value we want. 

Can I interest you in a game of deck size pickup? 

I'm Doug Lloyd. And this is CS50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 1 — C](../week.md) (`week-1`)

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
- https://cs50.harvard.edu/x/shorts/magic_numbers/ — retrieved 2026-10-18T05:40:58+03:30, sha256 `8e51079e1239cf68…`
- https://cdn.cs50.net/2017/fall/shorts/magic_numbers/lang/en/magic_numbers.txt — retrieved 2026-10-18T05:40:59+03:30, sha256 `0e7f05381d243337…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
