---
id: short-data-structures
type: short
title: 'Short: Data Structures'
week: 5
parent: week-5
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/data_structures/
- https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:01+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- data-structures
- short
checksum: sha256:8976148ee6b0dfe6ecb08c3bff9532b03313cf75f093f36dd71840c184cd67c2
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Data Structures

## 1. Source metadata
- **Title:** Short: Data Structures
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/data_structures/>, <https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:01+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/data_structures/>, <https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/data_structures/data_structures.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.txt>
- CS50 Video Player: <https://video.cs50.io/3uGchQbk7g8>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/data_structures/data_structures-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/data_structures/data_structures-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/data_structures/data_structures-1080p.mp4.download>
- YouTube: <https://youtu.be/3uGchQbk7g8>

### Transcript (verbatim, English)

```text
DOUG LLOYD: So in CS50, we've covered a lot of different data structures, right? We've seen arrays, and linked lists, and hash tables, and tries, stacks and queues. We'll also learn a little about trees and heaps, but really these all just end up being variations on a theme. There really are these kind of four basic ideas that everything else can boil down to. Arrays, linked lists, hash tables, and tries. And like I said, there are variations on them, but this is pretty much going to summarize everything we're going to talk about in this class in terms of C. But how do these all measure up, right? We've talked about the pros and cons of each in separate videos on them, but there's a lot of numbers getting thrown around. There's a lot of general thoughts getting thrown around. Let's try and consolidate it into just one place. Let's weigh the pros against the cons, and consider which data structure might be the right data structure for your particular situation, whatever kind of data you're storing. You don't necessarily always need to use the super fast insertion, deletion, and lookup of a trie if you really don't care about inserting and deleting too much. If you need just quickly random access, maybe an array is better. So let's distill that. Let's talk about each of the four major kinds of data structures that we've talked about, and just see when they might be good, and when they might not be so good. So let's start with arrays. So insertion, that's kind of bad. 

Insertion at the end of an array is OK, if we're building an array as we go. But if we need to insert elements into the middle, think back to insertion sort, there's a lot of shifting to fit an element in there. And so if we're going to insert anywhere but the end of an array, that's probably not so great. 

Similarly, deletion, unless we're deleting from the end of an array, is probably also not so great if we don't want to leave empty gaps, which usually we don't. We want to remove an element, and then sort of make it snug again. And so deleting elements from an array, also not so great. 

Lookup, though, is great. We have random access, constant time lookup. We just say seven, and we go to array relocation seven. We say 20, with go to array relocation 20. We don't have to iterate across. That's pretty good. 

Arrays are also relatively easy to sort. Every time we talked about a sorting algorithm, such as selection sort, insertion sort, bubble sort, merge sort, we always used arrays to do it, because arrays are pretty easy to sort, relative to the data structures we've seen so far. 

They're also relatively small. There's not a lot of extra space. You just set aside exactly as much as you need to hold your data, and that's pretty much it. So they're pretty small and efficient in that way. But another downside, though, is that they are fixed in size. We have to declare exactly how big we want our array to be, and we only get one shot at it. We can't grow and shrink it. 

If we need to grow or shrink it, we need to declare an entirely new array, copy all of the elements of the first array into the second array. And if we miscalculated that time, we need to do it again. Not so great. So arrays don't give us the flexibility to have variable numbers of elements. 

With a linked list, insertion is pretty easy. We just tack onto the front. Deletion is also pretty easy. We have to find the elements. That involve some searching. 

But once you've found the element you're looking for, all you need to do is change a pointer, possibly two if you have a linked list-- a doubly linked list, rather-- and then you can just free the node. You don't have to shift everything around. You just change two pointers, so that's pretty quick. 

Lookup is bad though, right? In order for us to find an element in a linked list, whether singly or doubly linked, we have to linear search it. We have to start at the beginning and move the end, or start at the end move to the beginning. We don't have random access anymore. So if we're doing a lot of searching, maybe a linked list isn't quite so good for us. 

They're also really difficult to sort, right? The only way you can really sort a linked list is to sort it as you construct it. But if you sort it as you construct it, you're no longer making quick insertions anymore. You're not just tacking things onto the front. You have to find the right spot to put it, and then your insertion becomes just about as bad as inserting into an array. So linked lists are not so great for sorting data. 

They're also pretty small, size-wise. Doubly linked list slightly larger than singly linked lists, which are slightly larger than arrays, but it's not a huge amount of wasted space. So if space is at a premium, but not a really intense premium, this might be the right way to go. 

Hash tables. Insertion into a hash table is fairly straightforward. It's a two-step process. First we need to run our data through a hash function to get a hash code, and then we insert the element into the hash table at that hash code location. 

Deletion, similar to linked list, is easy once you find the element. You have to find it first, but then when you delete it, you just need to exchange a couple of pointers, if you're using separate chaining. If you're using probing, or if you're not using chaining at all in your hash table, deletion is actually really easy. All you need to do is hash the data, and then go to that location. And assuming you don't have any collisions, you'll be able to delete very quickly. 

Now, lookup is where things get a little more complicated. It's on average better than linked lists. If you're using chaining, you still have a linked list, which means you still have the search detriment a linked list. But because you're taking your linked list and splitting it over 100 or 1,000 or n elements in your hash table, you're linked lists are all one nth the size. They're all substantially smaller. You have n linked lists instead of one linked list of size n. 

And so this real-world constant factor, which we generally don't talk about in time complexity, it does actually make a difference here. So lookup is still linear search if you're using chaining, but the length of the list you're searching through is very, very short by comparison. Again, if sorting is your goal here, hash table's probably not the right way to go. Just use an array if sorting is really important to you. 

And they can run the gamut of size. It's hard to say whether a hash table is small or big, because it really depends on how large your hash table is. If you're only going to be storing five elements in your hash table, and you have a hash table with 10,000 elements in it, you're probably wasting a lot of space. Contrast being you can also have very compact hash tables, but the smaller your hash table gets, the longer each of those linked lists gets. And so there's really no way to define exactly the size of a hash table, but it's probably safe to say it's generally going to be bigger than a linked list storing the same data, but smaller than a trie. 

And tries are the fourth of these structures that we've been talking about. Inserting into a trie is complex. There's a lot of dynamic memory allocation, especially at the beginning, as you're starting to build. But it's constant time. It's only the human element here that makes it tricky. Having to encounter null pointer, malloc space, go there, possibly malloc space from there again. The sort of intimidation factor of pointers in dynamic memory allocation is the hurdle to clear. But once you've cleared it, insertion actually comes quite simple, and it certainly is constant time. 

Deletion is easy. All you need to do is navigate down a couple of pointers and free the node, so that's pretty good. Lookup is also pretty fast. It's only based on the length of your data. So if all of your data is five character strings, for example, you're storing five character strings in your trie, it only takes five steps to find what you're looking for. Five is just a constant factor, so again, insertion, deletion, and lookup here are all constant time, effectively. 

Another thing is that your trie is actually kind of already sorted, right? By virtue of how we're inserting elements, by going letter by letter of the key, or digit by digit of the key, typically, your trie ends up being kind of sorted as you build it. It doesn't really makes sense to think about sorting in the same way we think about it with arrays, or linked lists, or hash tables. But in some sense, your trie is sorted as you go. 

The downside, of course, is that a trie rapidly becomes huge. From every junction point, you might have-- if your key consists of digits, you have 10 other places you can go, which means that every node contains information about the data you want to store at that node, plus 10 pointers. Which, on CS50 IDE, is 80 bytes. So it's at least 80 bytes for every node that you create, and that's not even counting data. And if your nodes are letters instead of digits, now you have 26 pointers from every location. And 26 times 8 is probably 200 bytes, or something like that. And you have capital and lowercase-- you can see where I'm going with this, right? Your nodes can get really big, and so the trie itself, overall, can get really big, too. So if space is at a high premium on your system, a trie might not be the right way to go, even though its other benefits come into play. I'm Doug Lloyd. This is CS50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 5 — Data Structures](../week.md) (`week-5`)

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
- https://cs50.harvard.edu/x/shorts/data_structures/ — retrieved 2026-10-18T05:42:01+03:30, sha256 `8976148ee6b0dfe6…`
- https://cdn.cs50.net/2017/fall/shorts/data_structures/lang/en/data_structures.txt — retrieved 2026-10-18T05:42:02+03:30, sha256 `0bbd4a61a52bc4a8…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
