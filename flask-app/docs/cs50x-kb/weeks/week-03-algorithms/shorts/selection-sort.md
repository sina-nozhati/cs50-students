---
id: short-selection-sort
type: short
title: 'Short: Selection Sort'
week: 3
parent: week-3
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/selection_sort/
- https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:29+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- selection-sort
- short
checksum: sha256:1c80abb4777c8006c5dd9011aea4b2b0b7dd8dd10a372f957accc3093776aac5
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Selection Sort

## 1. Source metadata
- **Title:** Short: Selection Sort
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/selection_sort/>, <https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:29+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/selection_sort/>, <https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/selection_sort/selection_sort.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.txt>
- CS50 Video Player: <https://video.cs50.io/3hH8kTHFw2A>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/selection_sort/selection_sort-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/selection_sort/selection_sort-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/selection_sort/selection_sort-1080p.mp4.download>
- YouTube: <https://youtu.be/3hH8kTHFw2A>

### Transcript (verbatim, English)

```text
[MUSIC PLAYING] DOUG LLOYD: Selection sort is an algorithm that, as you might expect, sorts a set of elements. And algorithm recall is a step-by-step set of instructions for completing a task. 

In selection sort the basic idea is this, find the smallest unsorted element and add it to the end of the sorted list. Effectively what this does is build a sorted list, one element at a time. Breaking it down to pseudocode we could state this algorithm as follows, repeat this until no unsorted elements remain. Search through the unsorted data to find the smallest value, then swap the smallest value with the first element of the unsorted part. 

It may help to visualize this, so let's take a look at this. So this, I contend, is an unsorted array and I've indicated it by indicating that all of the elements are colored red, they are not yet sorted. This is the entire unsorted part of the array. 

So let's go through the steps of selection sort to sort this array. So again, we're gonna repeat until no unsorted elements remain. We're gonna search through the data to find the smallest value, and then swap that value with the first element of the unsorted part. 

Right now, again, the entire array is the unsorted part. All of the red elements are unsorted. So we search through and we find the smallest value. We start at the beginning, we go to the end, we find the smallest value is, one. So that's part one. And then part two, swap that value with the first element of the unsorted part, or the first red element. 

In this case that would be five, so we swap one and five. When we do this, we can visually see that we've moved the smallest valued element of the array, to the very beginning. Effectively sorting that element. 

And so we can indeed confirm and state that one, is sorted. And so we'll indicate the sorted portion of our array, by coloring it blue. 

Now we just repeat the process again. We search through the unsorted part of the array to find the smallest element. In this case, it's two. 

We swap that with the first element of the unsorted part. In this case two also happens to be the first element of the unsorted part. So we swap two with itself, which really just leaves two where it is, and it's sorted. Continuing on, we search through to find the smallest element. It's three. We swap it with the first element, which is five. And now three is sorted. 

We search through again, and we find the smallest element is four. We swap it with the first element of the unsorted part, and now four is sorted. 

We find that five is the smallest element. We swap it with the first element of the unsorted part. And now five is sorted. 

And then lastly, our unsorted part consists of just a single element, so we search through and we find that six is the smallest, and in fact, only element. And then we can state that it is sorted. And now we've switched our array from being completely unsorted in red, to completely sorted in blue, using selection sort. 

So what's the worst case scenario here? Well in the absolute worst case, we have to look over all of the elements of the array to find the smallest unsorted element, and we have to repeat this process n times. Once for each element of the array because we only, in this algorithm, sort one element at time. 

What's the best case scenario? Well it's exactly the same, right? We actually have to still step through every single element of the array in order to confirm that it is, in fact, the smallest element. 

So the worst case runtime, we have to repeat a process n times, once for each of n elements. And in the best case scenario, we have to do the same. 

So thinking back to our computational complexity toolbox, what do you think is the worst case runtime for selection sort? What do you think is the best case runtime for selection sort? 

Did you guess Big O of n squared, and Big Omega of n squared? You'd be right. Those are, in fact, the worst case and best case run times, for selection sort. 

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
  - [Selection Sort and Bubble Sort](../../../concepts/selection-and-bubble-sort.md) (`concept-selection-and-bubble-sort`)

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
- https://cs50.harvard.edu/x/shorts/selection_sort/ — retrieved 2026-10-18T05:41:29+03:30, sha256 `1c80abb4777c8006…`
- https://cdn.cs50.net/2017/fall/shorts/selection_sort/lang/en/selection_sort.txt — retrieved 2026-10-18T05:41:30+03:30, sha256 `cca6dcf058bae681…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
