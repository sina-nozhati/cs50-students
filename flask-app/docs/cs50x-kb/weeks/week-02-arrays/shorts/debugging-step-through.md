---
id: short-debugging-step-through
type: short
title: 'Short: Debugging (“Step through”)'
week: 2
parent: week-2
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/debugging_step_through/
- https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:15+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- debugging-step-through
- short
checksum: sha256:1a7b1dca8b8976a1d675d6b8836737268cfa021e9c4c8e6507730e00bd946342
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Debugging (“Step through”)

## 1. Source metadata
- **Title:** Short: Debugging (“Step through”)
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/debugging_step_through/>, <https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:15+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/debugging_step_through/>, <https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Subtitles: <https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.srt>
- Transcript: <https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.txt>
- CS50 Video Player: <https://video.cs50.io/---HbbANxDQ>
- 360p: <https://cdn.cs50.net/2021/fall/shorts/guess/guess-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2021/fall/shorts/guess/guess-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2021/fall/shorts/guess/guess-1080p.mp4.download>
- YouTube: <https://youtu.be/---HbbANxDQ>

### Transcript (verbatim, English)

```text
SPEAKER 1: Welcome, everyone. My name is Carter. And today I'm going to show you my guessing game and how I can use debug50 to help figure out what's wrong with it. So here, I'm trying to write a guessing game that is written in the spirit of the elementary school game where you would guess a number and someone would tell you, it's right or wrong. And I called my program Guess. So I can run it in the terminal with ./guess. 

Here go to ./guess, hit Enter, and I have to guess a number. So here I might guess, maybe 2, and hit Enter. But then I get this flood of messages in the terminal. And I'm wondering, well, what's wrong with this? Why am I getting so many messages here? 

And to try to figure that out, I can go into my code with code guest.c. And then I can see, well, I'm not entirely sure what may be wrong here. So I need to pause my code at some point. And for that, I can use a break point. 

So let me go ahead and go to this left side of my guess.c file, where I see these red circles pop up. I can click on one of them to turn it bright red. And at that point, I've set a pause point in my code. And I can use debug50 to go in and actually step through my code and see what's going on in there. 

So let me go ahead and type debug50 of guess, hit Enter. So now that I have my code opened up in debug50, I can see a few different things. I can see that my number variable is currently set to 0. And my guess is currently set to this odd 32,764. But as I go through my code, I'll actually see those numbers fall into place. 

So if I use this Step Over button to walked to the next line of my code, I can see that number becomes 5, as I expect it to on line 6. And then as I go to line 8 and Step Over that, I get prompted for, what's my guess? And at that point, I might type, well, 3 again. And I'll hit Enter. And then I see guess becomes 3. 

So now I'm wondering, well, if my guess is wrong and my number is 5, my guess is 3, shouldn't I only get wrong guess just once? So I'll actually just keep walking through my code with Step Over. And I'll see, I'm printing "Wrong guess!", which seems right. 

And now I should just exit the program. That should be it. But I really see that my line in that yellow highlight is going back up to 10, line 10 there. And it's actually continuing to go through and print "Wrong guess!" 

And so at this point, I can actually see that maybe the bug in my code is I shouldn't have used a while loop. I should have, maybe, used an if statement, where I'm only checking for this condition once. So now that my while loop has changed to an if statement, I should be able to recompile my code and see what's changed. 

So I can use "make guess". And then I'll run my code, guess. And when I guess 3, I guess I should get "Wrong guess!" So I'll do 3. And then I'll get "Wrong guess!", but also "You're correct!". And at this point, there's probably another bug in my code. And so I'll actually leave this one up to you, to use debug50 and see, well, why am I getting both "Wrong Guess!" and "You're correct!"?
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
  - [Debugging (printf, debug50, rubber duck)](../../../concepts/debugging.md) (`concept-debugging`)

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
- https://cs50.harvard.edu/x/shorts/debugging_step_through/ — retrieved 2026-10-18T05:41:15+03:30, sha256 `1a7b1dca8b8976a1…`
- https://cdn.cs50.net/2021/fall/shorts/guess/lang/en/guess.txt — retrieved 2026-10-18T05:41:16+03:30, sha256 `11ee60e4a119490e…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
