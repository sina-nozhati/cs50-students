---
id: short-debugging-step-into
type: short
title: 'Short: Debugging (“Step into”)'
week: 2
parent: week-2
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/debugging_step_into/
- https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:17+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- debugging-step-into
- short
checksum: sha256:06c9ab782f6cdc2b4ac578bcd872ba5c0eeba86336bc50009f7a258d092d7386
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Debugging (“Step into”)

## 1. Source metadata
- **Title:** Short: Debugging (“Step into”)
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/debugging_step_into/>, <https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:17+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/debugging_step_into/>, <https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Subtitles: <https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.srt>
- Transcript: <https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.txt>
- CS50 Video Player: <https://video.cs50.io/tk3cl8hyfqM>
- 360p: <https://cdn.cs50.net/2021/fall/shorts/secret/secret-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2021/fall/shorts/secret/secret-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2021/fall/shorts/secret/secret-1080p.mp4.download>
- YouTube: <https://youtu.be/tk3cl8hyfqM>

### Transcript (verbatim, English)

```text
SPEAKER 1: Welcome, everyone. My name is Carter, and today I'll show you my secret program. You can run the program by typing ./secret into your terminal, and if you type in the right password, you should be able to see come on in. So let's try it out. 

I'll do ./secret, and maybe I don't know the secret phrase, so I'll just say, let me in. And at which point, I don't get any response. So let me try it again and do ./secret. Maybe password is the password here. But it's not. And I'll just reveal to you that the password is please. So if I type ./secret, and I type in please, I should see come on in. But I don't. And so what's the problem here? 

Well, maybe I should look into my code, and maybe step through it bit by bit. So I'll do code secret.c, and I can see the very top of my code, starting with this int main(void) function. To step through my code, remember we can use debug50 to set a breakpoint, or a place to pause in our code. So I can go to this left side here, find a pale red circle, and turn it into a bright red circle as I click it, and set that pause point, or that breakpoint. 

Now I can do debug50 of secret, and then my code should boot up, and I should be able to pause right at that moment I'm asking the user for their secret phrase. Of course, I have to actually step over that line for it to actually run my program, so I'll then step over, and I can type in my secret phrase of please. 

OK, so that seems pretty good. I see that phrase becomes please, and correct is currently false, but it should change to true after I do this check phrase function. So I'll step over check phrase, and I see it's actually still false. And so of course, if I run past line 13, nothing will happen. I actually won't print "come on in." 

So at this point, debug50 seems to be not really helping me here. I've walked through my entire program, but I haven't seen what went wrong in my code. Well, debug50 has this option to step into a function, actually dive in and see what's happening underneath that hood of that function. So what I can do is go to debug50 again, and run debug50 with secret, wait for my code to go to that breakpoint again, and I'll walk through that first piece where I type in my phrase, please. 

But now, instead of stepping over this check phrase function, I actually want to dive into it and see what's going on underneath there. So I'll do step into in debug50, and then see, I'm setting my password to be please. So if I step over line 22, I should see that password becomes please, as it does on this left hand side. 

And now, when I check for if phrase is password, I should actually be able to return true, because it seems that phrase is the same as password. So I'll step over that, and see-- well actually, I get to line 29. And this is kind of subtle, but in C, you can't compare two strings using two equal signs. You actually could use a different function called string compare, or strcmp for short. 

So to use strcompare, I can use strcmp, and give it two arguments, phrase and password. And with these two inputs, strcompare will tell me are they exactly equivalent or not. If they are equivalent, strcmp-- or strcompare-- will give me 0 as a value back. So now my code is saying, if these strings are equivalent-- and I know they are because strcompare is giving me zero-- I can go ahead and return true and say this is the correct password. 

So with this new code here, I should be able to exit debug50 and go back to the terminal. And now I can make secret again, run secret, type in my password of please, and now there it is. It says, come on in. 

And with that, we've seen how debug50 can help us not only step over our code, but dive into functions and see the bugs inside of them.
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
- https://cs50.harvard.edu/x/shorts/debugging_step_into/ — retrieved 2026-10-18T05:41:17+03:30, sha256 `06c9ab782f6cdc2b…`
- https://cdn.cs50.net/2021/fall/shorts/secret/lang/en/secret.txt — retrieved 2026-10-18T05:41:18+03:30, sha256 `319be15ccbd6bc06…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
