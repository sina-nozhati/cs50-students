---
id: short-hexadecimal
type: short
title: 'Short: Hexadecimal'
week: 4
parent: week-4
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/hexadecimal/
- https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:37+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- hexadecimal
- short
checksum: sha256:5adde7701fabb79e42e12bfc9023b10464855c9a86e5941c61464e3b2b6e9978
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Hexadecimal

## 1. Source metadata
- **Title:** Short: Hexadecimal
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/hexadecimal/>, <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:37+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/hexadecimal/>, <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/hexadecimal.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.txt>
- CS50 Video Player: <https://video.cs50.io/u_atXp-NF6w>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/hexadecimal-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/hexadecimal-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/hexadecimal/hexadecimal-1080p.mp4.download>
- YouTube: <https://youtu.be/u_atXp-NF6w>

### Transcript (verbatim, English)

```text
DOUG LLYOYD: So hexadecimal numbers, as if we needed another base number scheme right? Well, most Western cultures, as you probably are familiar, use the decimal system-- base 10, to represent numeric data. We have the digits 0, 1, 2, 3, 5, 6, 7,8,9. And if we need to represent values higher than nine, we can combine those digits using the notion of place value. So for 10, we have a 1 digit followed by a 0 digit and we intuitively understand that what we're doing there is we're multiplying the first 1 by 10, and then adding 0 for a total of 10. Computers do something pretty similar, as you're probably familiar, with the binary system-- base 2. The difference there being that there are only 2 digits to work with-- 0 and 1. And so our place values, instead of being one, ten, hundred, thousand, as they would be in the decimal system, are one, two, four, eight, and so on. Here's the thing though, those 0's and 1's, especially if we're being computer scientists and we're doing a lot of programming or working with computers, were going to be seeing a lot of binary numbers. And those 0's and 1's in large chains can be very difficult to parse. We can't just look at a string of 0's and 1's and necessarily know exactly what it is. But it's still useful to be able express data in the same way that a computer does. We have this notion of the hexadecimal system, which is base 16, instead of base 10 or base 2. Which means that we have 16 digits to work with instead of 10 or 2. And it's a much more concise way to express binary information on a computer system, it's much more human understandable. So we have the digits 0 through 9, and then we also have these extra six digits-- a, b, c, d, e, and f, which represent 10, our notion of 10, 11, 12, 13, 14 and 15, in decimal. Sometimes, by the way, you'll also see these a through f's as capital A through F, which is the way I tend to do it. It's just my preferred style, but either is fine, they both represent pretty much the same thing. So why is hexadecimal cool? Why do we need to use this other additional base? We already have 2 and 10, why do we need 16? Well 16 is a power of 2, and so each hexadecimal digit, 0 through f, corresponds to a unique ordering, or unique arrangement of 4 binary digits, 4 bits. And so in that sense, we can express very long, complex, binary numbers in hexadecimal in a much more concise way, without losing information or having to do particularly cumbersome conversions on those numbers. 

So, as I just said, each hexadecimal digit corresponds to a unique arrangement of 4 binary digits. So the binary string 0000 corresponds to hexadecimal digit 0. 0110 corresponds to hexadecimal digit 6. And 1111 corresponds to hexadecimal digit f. If you're looking at this chart, particularly if you're looking at the left side of the chart, you can already see there's a bit of an ambiguity problem here. Decimal 0 is pretty much indistinguishable from hexadecimal 0, other than the fact that it's under a column that says hexadecimal. 

But we probably won't always have that column there. Generally when we are expressing numbers into hexadecimal notation to clearly distinguish them from decimal notation, we usually prefix them with the prefix 0x. 0x means nothing in reality, it's just a clue to us as humans that what we're about to see, or about to start parsing, is a hexadecimal number. Obviously for the higher digits a, b, c, d, and f, which correspond to 10-15 it's pretty unambiguous that's that's a hexadecimal number. And in fact, any hexadecimal number that has letters in it, is probably pretty obvious as a hexadecimal number. But, still, for the sake of clarity, it's always a good idea to prefix every time you refer to a digit as a hexadecimal number by prefixing a 0x. 

So, binary, as we said, has place values. There's the ones place, a twos place, a fours place, and an eights place. And decimal also has place values, the ones, tens, hundreds, and thousands that we all may recall from grade school. And hexadecimal is no exception here, really. It also has place values but instead of being powers of 2 or powers of 10, they're powers of 16. 

So we see a number like this we pretty clearly know it's 397, right? Well if we see a number like this, we know this isn't 397 anymore. This is the hexadecimal number three-nine-seven. It's not 397, it means something different, because we're using powers of 16 as all of our place values instead of powers of 10. In fact, the place values here would be the ones place, the sixteens place, and the two-hundred-fifty-sixes place, which correspond to our idea of a ones place, tens place, and a hundreds place, if the number was 397. But since it's 0x 397, we have a ones place, sixteens place, and a two-hundred-fifty-sixes place. Or, a 16 to the 0 place, which is 1. A 16 to the first power place, 16. A 16 squared place, 256, and so on, and so on, and so on. So this number is really 3 times 16 squared, plus 9 times 16, plus 7. I didn't do the math here, but it's not 397, it's much, much larger than that. 

Similarly, we could have 0x adc, well that's a times 16 squared. Or if we translate that to our notion of decimal numbers, that's 10 times 16 squared, plus d times 16, or plus 13 times 16. And don't worry if you haven't memorized that d is 13, or anything like that, there's not too many of these letter digits and it'll become intuitive pretty quickly. So again this is 10 times 16 squared, plus 13 times 16, plus 12 times 1. So 0x adc. 

So, as I said, every group of 4 binary digits corresponds to a single hexadecimal digit, and so it's actually really easy to change back and forth between hex and binary. If you have this long string of binary digits, all you need to do is start grouping them right to left as groups of 4. And then you can consolidate them into hexadecimal numbers, severely limiting the number of digits you have to process mentally. Instead of 32 0's and 1's, as we'll see in a second, you might be able to get it down to just 8 hexadecimal digits, a lot more concise. 

The charts a few slides back will help you to figure out this mapping, although, again you'll memorize it pretty quickly. We'll go through an example right now. So if we have a number like this, this really large binary number, or what appears to be a large binary number. And the reason I say that, it's just so-- it's a behemoth, right? There's so many 0's and 1's there. But we probably don't really have a sense of what the magnitude of this number really is. We don't have any idea what it would correspond to a decimal. And in fact we won't even see what it corresponds to in decimal right now. We might be able to express this in a way that would give us some more information about just how big this number is. 

So let's go to that conversion process. The first thing we need to do is we want to group these digits out into groups of 4, starting from the right and working to the left. There happen to be 32 digits here, which means we have a nice clean break of 8 groups of 4. Remember that each group of 4 here, uniquely corresponds to a hexadecimal digit. So we'll start again building our number from the right, and working left. Well what's 1101? Well we do the math out in our head, we have 1 in the eights place, a 1 in the fours place, a 0 in the twos place, and a 1 in the ones place. That's 8 plus 4 plus 1, which we would know as 13. But we probably wouldn't write 13 out, because we're working with hexadecimal. We need to convert it to the hexadecimal equivalent of 13, which is d. 

0011, well that's a 0 in the eights place, a 0 in fours place, a 1 in the twos place, and a 1 in the ones place. That's 3. I mean keep doing this again, we have here 9. And then 11, but that's b, recall. 2, 10-- or a-- 6, and 4. And so that very large string of 0's and 1's of the top is more concisely expressed in hexadecimal as 0x 46a2b93d. 

Well, OK, we've learned a new cool skill, what's the point? We might not use this all the time, as we're going to soon see, we use hexadecimal quite a lot as programmers. Not necessarily for the purpose of doing math with it, but because a lot of times memory addresses in our system are represented in hexadecimal. It's a really concise way to express otherwise cumbersome, binary numbers. And so, again, you may not-- you're probably not going to do any math with it, you are not going to be multiplying hexadecimal numbers together, or doing anything weird like that. But it is a useful skill to have so you can express and understand memory addresses, and other ways of using data in C. 

I'm Doug Lloyd, this is CS50.
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
  - [Hexadecimal and Memory Addresses](../../../concepts/hexadecimal-and-memory-addresses.md) (`concept-hexadecimal-and-memory-addresses`)

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
- https://cs50.harvard.edu/x/shorts/hexadecimal/ — retrieved 2026-10-18T05:41:37+03:30, sha256 `5adde7701fabb79e…`
- https://cdn.cs50.net/2017/fall/shorts/hexadecimal/lang/en/hexadecimal.txt — retrieved 2026-10-18T05:41:38+03:30, sha256 `64b9ef2aa31dcf41…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
