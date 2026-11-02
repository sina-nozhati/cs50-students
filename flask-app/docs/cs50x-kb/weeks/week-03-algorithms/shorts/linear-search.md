---
id: short-linear-search
type: short
title: 'Short: Linear Search'
week: 3
parent: week-3
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/linear_search/
- https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:23+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- linear-search
- short
checksum: sha256:d91c0889eccfdac50dd93223cba3bd8c20c8982f3926d49df7f223f400ef4743
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Linear Search

## 1. Source metadata
- **Title:** Short: Linear Search
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/linear_search/>, <https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:23+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/linear_search/>, <https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/linear_search/linear_search.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.txt>
- CS50 Video Player: <https://video.cs50.io/TwsgCHYmbbA>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/linear_search/linear_search-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/linear_search/linear_search-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/linear_search/linear_search-1080p.mp4.download>
- YouTube: <https://youtu.be/TwsgCHYmbbA>

### Transcript (verbatim, English)

```text
[MUSIC PLAYING] DOUG LLOYD: Linear search is an algorithm we can use to find an element in an array. An algorithm recall is a step-by-step set of instructions for completing a task. 

The linear search algorithm works as follows. Iterate across the array from left to right, looking for a specified element. 

In pseudocode, which is a more distilled version of this sentence, if the first element is what you're looking for, you can stop. Otherwise, move to the next element and keep going over and over until you find the element, or you don't. So we can use the linear search algorithm, for example, to find the target value nine in this array. Well we start at the beginning. If it's what we're looking for, we can stop. It's not, we're not looking for 11. So otherwise, move to the next element. 

So we look at 23. Is 23 what we're looking for? Well no, so we move on to the next element, and the next element, and we keep going through this process over and over and over, until we land on a situation like this. 

Nine is what we're looking for, and this element of the array is, it's value is nine. And so we found what we're looking for, and we can stop. The linear search has completed, successfully. 

But what about if we're looking for an element that's not in our array. Does linear search still work? Well sure. So we repeat this process starting at the first element. If it's what we're looking for, we can stop. It's not. Otherwise, we move to the next element. 

But we can keep repeating this process, examining each element in turn, hoping that we find the number 50. But we won't know if we've found the number 50 or if we didn't, until we've stepped over every single element of the array. 

Only once we've done that and come up short, can we conclude that 50 is not in the array. And so the linear search algorithm, well it failed, per se. But not in the sense that it was unsuccessful in doing what we asked it to do. 

It was unsuccessful in as much as it didn't find 50, but 50 wasn't in the array. But we have exhaustively searched through every single element and so, while we didn't find anything, linear search still succeeds even if the element is not in the array. 

So what's the worst case scenario with linear search? Well we have to look through every single element, either because the target element is the last element of the array, or the element we're looking for doesn't actually exist in the array at all. What's the best case scenario? Well we might find the element immediately. And how many elements do we then have to look at in the best case, if we're looking for it and we find it at the very beginning? We can stop immediately. 

What does this say about the complexity of linear search? Well in the worst case, we have to look at every single element. And so it runs in O of n, in the worst case. 

In the best case, we're gonna find the element immediately. And so runs in omega of 1. 

I'm Doug Lloyd. This is CS50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 3 — Algorithms](../week.md) (`week-3`)
- **Backlinks (auto-generated):**
  - [Linear Search](../../../concepts/linear-search.md) (`concept-linear-search`)

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
- https://cs50.harvard.edu/x/shorts/linear_search/ — retrieved 2026-10-18T05:41:23+03:30, sha256 `d91c0889eccfdac5…`
- https://cdn.cs50.net/2017/fall/shorts/linear_search/lang/en/linear_search.txt — retrieved 2026-10-18T05:41:24+03:30, sha256 `9952f421ed56eb52…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
