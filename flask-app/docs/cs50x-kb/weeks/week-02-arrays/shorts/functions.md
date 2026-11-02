---
id: short-functions
type: short
title: 'Short: Functions'
week: 2
parent: week-2
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/functions/
- https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:41:11+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- functions
- short
checksum: sha256:dc89da3e0c27c05a9288e948ee084679174c4cb8a904c584d9cf22105a4514ed
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: Functions

## 1. Source metadata
- **Title:** Short: Functions
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/functions/>, <https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:41:11+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/functions/>, <https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/functions/functions.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.txt>
- CS50 Video Player: <https://video.cs50.io/n1glFqt3g38>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/functions/functions-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/functions/functions-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/functions/functions-1080p.mp4.download>
- YouTube: <https://youtu.be/n1glFqt3g38>

### Transcript (verbatim, English)

```text
DOUG LLOYD: All right. So now let's tackle a really big topic, functions. So far in the course, all the programs that we've been writing have been written inside of main. They're pretty simple programs. You don't need to have all these branches and things going on. We can just fit it all inside of main and it doesn't get terribly overwhelming. But as the course goes on and as you begin to develop programs independently, they're probably going to start to get a lot more than 10 or 15 lines. You might get hundreds or thousands or tens of thousands of lines of code. And it's really not that crazy a thought. As such, it's probably not a good idea to keep everything inside of main. It can get a little difficult to find what you're looking for if you do that. Fortunately, though C, and pretty much every other programming language that might work with, allows us to write functions. And I'm just going to take a quick aside here to mention that functions is one area of computer science. And you'll see many more of them at various points throughout the course and if you continue on. Where there's a lot of synonyms for the same word. So we call the functions. But you might also hear them referred to as procedures, or methods, particularly, if you've ever done any object oriented programming before-- and don't worry if you haven't, not a big deal-- but in audit oriented languages are frequently called methods. Sometimes they're called subroutines. But they really all refer to the same basic idea. 

Let's see what that idea is. What is a function? Well a function is really nothing more than a black box. A black box that has a set of zero or more inputs and a single output. So for example, this might be a function. This is a function called func. And it takes three inputs a, b, and c. And inside that black box, we don't know exactly what it does, but it processes the inputs in some way and then it gives a single output, in this case, z. Now to make it a little less abstract, we could say that maybe we have a function called add that takes three inputs a, b, and c and processes the output in some way inside the black box to produce a single output. So in this case, if add takes 3, 6, and 7. Somewhere inside the add function, we would expect them to be added together to produce the output, which is 3 plus 6 plus 7 or 16. 

Similarly, you have a function called mult that takes two inputs, a and b, processes them in some way such that the output of the function is the product of the two inputs. The two inputs multiplied together. 4 and 5 being passed into mult, something happens, the output we expect is 20. Why do we call it a black box? Well if we aren't writing the functions ourselves, which we've done quite a bit so far cs50. We've seen print f, for example, which is a function that we didn't write ourselves, but we do use all the time. If we aren't writing the functions ourselves, we don't really need to know how it's actually implemented under the hood. 

So for example the black box I just showed you for multiplication, mult a, b could be defined-- and this is just some pseudocode-- could be defined as output a times b. That make sense, right. If we have a function called mult that takes two inputs. We would expect that the output would be the two inputs multiplied together, a times b. But mult could also be implemented like this, we have a counter variable to get set inside of mult to 0. And then we repeat this process b times add a to counter. For example, if we multiply 3a by 5b, we could say set counter to 0, repeat five times, add 3 to counter. So we start at 0 and then we do this five times 3, 6, 9, 12, 15. It's the same result. We still get 3 times 5 just the implementation is different. 

That's what we mean when we say a black box. It just means we don't really care how it's implemented under the hood as long as the output is what we expect. In fact, that's part of the contract of using functions, particularly functions that others write. The behavior is always going to be typical, unpredictable based on the name of the function. And that's why it's really important when you write functions or when other people write functions that you might use, that those functions have clear, relatively obvious names, and are well documented. Which is certainly the case for function like print f. 

So why do we use functions? Well as I said earlier, if we write all of our code inside of main things can get really cumbersome and really complicated. Functions allow us the ability to organize things and break up a very complicated problem into a lot more manageable sub parts. Functions also allow us to simplify the coding process. It's a lot easier to debug a 10 line function versus a 100 line function or a 1,000 line function. If we only have to debug small pieces at a time, or write small pieces at the time, it makes that programming experience a lot better. Trust me on that one. 

Lastly, if we write functions we can reuse those various parts. Functions can be recycled. They can be used in one program or another. You've already written the function, all you need to do is tell that program where to find that function. We've been recycling and using print f for over 40 years. But it was only written one time. Pretty useful, right. All right. So functions are great. We know that. Now let's start writing them. Let's start getting them into our programs. In order to do that, the first thing we do is declare the function. When you declare a function what you're basically doing is telling the compiler, hey, just so you know, I am going to be writing a function later on and here's what it's going to look like. The reason for this is because compilers can do some weird things if they see a set of symbols that they're not familiar with. So we just give the compiler a heads up, I'm creating a function and it's going to do this. Function declarations generally if you're organizing your code in a way that others will be able to understand and make use of, you generally want to put all of your function declarations at the very top of your code, right before you start writing main even. And conveniently, there's a very standard form that every function declaration follows. They all pretty much look like this. There are three parts to a function declaration, return type, name, and argument list. 

Now the return type is what kind of variable the function will output. So for example, if we think back a minute ago to the multiplying two numbers function, what do we expect if we multiply an integer by an integer the output will be probably an integer, right. Multiplied two integers together, you get an integer. So the return type of that function would be int. Name is what you want to call your function. This is probably the least important part of the function declaration, in terms of functionality. But is actually probably one of the most important parts of the function declaration in terms of knowing what the function actually does. If you name your function f or g or h or mystery or something like that, you're probably going to get a little tripped up trying to remember what those functions do. So it's important to give your function's meaningful names. 

Lastly, argument list is the comma separated list of all the inputs to your function, each of which has a type and a name. So not only do you have to specify what type of variable the function will output, you also want to specify what type and types of variables the function will be accepting as inputs. So let's do an example here. Let's just take a look at a more concrete one. So here's an example of a function declaration for a function that would add two integers together. The sum of two integers is going to be an integer as well, as we just discussed. And so the return type, here in green, would be int. That just tells us that add two ints is going to, at the end of the day, output, or spit it back out to us, an integer. Given what this function does we want to give it a meaningful name. Add two ints seems appropriate, considering we're taking two integers as inputs and hopefully adding them together. It might be a bit of a cumbersome name and frankly this function is probably not necessary since we have the addition operator, if you recall from our discussion of operators, previously. But let's just say for sake of argument that this function is useful and so we'll call it add two ints. Lastly, this function takes two inputs. Each of which is an integer. So we have this comma separated list of inputs. Now we generally want to give a name to each of them so that they can be used within the function. The names aren't terribly important. 

In this case, we don't necessarily have any meaning attached to them. So we can just call them a and b. That's totally fine. If however, you find yourself in a situation where the names of the variables might actually be important, you might want to call them something other than a and b to give them something more symbolically meaningful. But in this case, we don't really know anything else about the function. We just want to add two integers. So we'll just call those integers a and b. That's one example. 

Why don't you take a second to think about this one, how would you write a function declaration for a function that multiplies two floating point numbers? Do you remember what a floating point number is? What would this function declaration look like? I actually recommend you pause the video here and take how much time you need. Think about what this function declaration would be? What would the return type be? What would a meaningful name be? What would the inputs be? So why don't you pause the video here and write-up a function declaration for a function that would multiply two floating point numbers together. Hopefully you paused the video. 

So let's take a look at an example of one possible declaration. Float mult two reals float x, float y. The product of two floating point numbers, which recall are how we represent real numbers or numbers with decimal values in c, is going to be a floating point number. When you multiply a decimal by a decimal, you're probably going to get a decimal. You want to give it a relevant name. Multiply two reals seems fine. But you could really call it mult two floats, or mult floats. Anything like that, as long as it gave some actual meaning to what this black box was going to do. And again, in this case, we don't seem to have any meaning attached to the names of the variables we're passing in, so we just call them x and y. Now if you call them something else, that's totally fine. In fact, if you did this declaration instead using doubles instead of floats, if you recall that doubles are a different way to more precisely specify real numbers or floating point variables. That's totally fine too. Either one of those would be fine. In fact, there are several different combinations of ways to declare this function. But these are two pretty good ones. We've declared a function, that's great. We've told the compiler what it is, what we're going to be doing. Now let's actually write that function. Let's give it a definition, so that inside the black box predictable behavior is happening. In fact, we are multiplying two real numbers together, or adding numbers together, or doing whatever it is that we asked our function to do. 

So in fact, let's try and define multiply two reals which we just talked about a second ago. Now the beginning of a function definition looks almost exactly the same as a function declaration. I have both of them here. At the top is the function declaration, type, name, comma separated argument list, semicolon. The semicolon indicates that that is a function declaration. The beginning of the function definition looks almost exactly the same, type, name, comma separated argument list, no semicolon, open curly brace. The open curly brace, just as we've been doing with main, means that we are now beginning to define what happens inside the black box that we've decided to call mult two reals. Here is one way to implement it. We could say, we could declare a new variable of type float called product and assign that variable to the value x times y. And then return product. What does return mean here. Well return is the way we indicate that's how we're passing the output back out. So return something, is the same as, this is the output of the black box. So that's how you do it. Here's another way to implement it. We could just return x times y. x is a float. y is a float. So x times y is also a float. We don't even need to create another variable. So that's a different way to implement the exact same black box. 

Now take a moment, pause the video again, and try and define add two ints, which is the other function that we talked about a moment ago. Again here, I've put the function declaration, and so the semicolon, and an open curly brace and a closed curly brace to indicate where we will fill in the contents of add two ints, so that we define the particular behavior inside the black box. So pause the video. And take as much time as you need to try and define an implementation of add two ints, such that when the function outputs a value, it does, in fact, return the sum of the two inputs. So just like the previous example, there are several different ways that you could implement add two ints. Here's one. In here in orange I've just had some comments-- I've just added some comments to indicate what's happening on each line of code. So I declare a variable called sum of type int. I say sum equals a plus b. That's where we're actually doing the work adding a and b together. And I return sum. And that makes sense because sum is a variable of type int. And what's the data type that this function tells me it's going to output? Int. So I'm returning sum, which is an integer variable. And that makes sense given what we've declared and defined our function to do. 

Now you can also define the function this way, int sum equals a plus b-- skip that first step-- and then, return sum. Now you could have also implemented it this way, which I highly do not recommend. This is bad style for one thing and really bad design, but it does, in fact, work. If you take this code, which is int add bad adder dot c, and use it. It actually does add two integers together. It's a very poor implementation of this particular behavior. But it does work. It's just here to illustrate the point that we don't really care what happens inside the black box, as long as it has the output that we expect. This is a poorly designed black box. But at the end the day, it does still output the sum of a plus b. All right. So we've declared functions. And we've defined function. So that's really good. Now let's start to use the functions that we've declared and we've defined. To call a function-- it's actually pretty easy-- all you need to do is pass it appropriate arguments, arguments of the data type that it expects, and then assign the return value of that function and this-- excuse me-- assign the return value of that function to something of the correct type. 

So let's have a look at this in practice in a file called adder 1 dot c, which I have in my cs50 IDE. So here is adder 1 dot c. At the beginning you see I have my includes, pound include, standard IO, and cs50 dot h. And then I have my function declaration. This is where I'm telling the compiler I'm going to be writing a function called add two ints. It's going to output an integer type variable. That's what this part is right here. And then I have two inputs to it a and b, each of which is an integer. Inside of main, I ask the user for input by saying, give me an integer. And they are prompted to forget int, which is a function that is included in the cs50 library. And that gets stored in x, an integer variable. 

Then we prompt them for another integer. We get another integer and store that in y. And then, here on line 28, is where we make our function call. We are saying, int z equals add 2 ints x comma y. Do you see why this makes sense? x is an integer type variable and y is an integer type variable. So that's good. That make sense with what our function declaration on line 17 looks like. The comma separated input list expects two integers, a and b. In that case, we can call them whatever we want. It just expects two integers. And x is an integer and y is an integer. That works. 

And we know that function is going to output an integers as well. And so we are storing the output of the function, add two ints, in an integer type variable, which we're calling z. And then we can say, the sum of percent i and percent i is percent i. x, y and z respectively filling in those percent i's. What is the definition of add two ints look like? It's pretty simple. It's one of the ones we just saw a second ago, int sum equals a plus b return sum. Does this work? Let's save the file. And then down here on my terminal I'm going to make adder 1, and I clear my screen. I'm going to zoom in because I know it's a little difficult to see. 

So we compile this program as adder 1. So we can do dot slash adder 1. Give me an integer, 10. Give me another integer, 20. The sum of 10 and 20 is 30. So we made a successful function call. You can run the function again, negative 10, 17 sum of negative 10 and 17 is 7. This function works. It has the behavior that we expect it to. And so we've made a successful function, definition, declaration, and a successful function call. Couple miscellaneous points about functions before we conclude this section. Recall from our discussion of data types, previously, that functions can sometimes take no inputs. If that's the case, we declare the function as having a void argument list. Do you recall what the most common function we've seen so far that takes a void argument list is? It's main. Recall also that function sometimes don't actually have an output. In that case, we declare the function as having a void return type. Let's conclude this section by tackling a practice problem. 

So here's the problem laid out. I want you to write a function called valid triangle. What this function should do is take three real numbers that represent the lengths of the three sides of a triangle as its parameters, or its arguments, or its inputs-- another set of synonyms that you might encounter. This function should either output true or false depending on whether those three lengths are capable of making a triangle. Do you remember the data type that we used to indicate true or false? Now how do you implement this? Well know there are a couple of rules regarding triangles that are actually useful to know. A triangle can only have sides with positive length. That makes sense. You're probably saying, duh. The other thing to note though, is that the sum of the lengths of any two sides of the triangle has to be greater than the length of the third side. That's actually true. You can't have a triangle of sides 1, 2 and 4, for example, because 1 plus 2 is not greater than 4. So those are the rules that determine whether or not the three inputs can conceivably form a triangle. So take a couple of minutes and declare and then define this function called valid triangle, such that it actually has the behavior specified here. 

It will output true if those three sides are capable of comprising a triangle, and false otherwise Ready to see how you did? Here's one implementation of valid triangle. It's not the only one. Yours might vary slightly. But this one does, in fact, have the behavior that we expect. We declare our function at the very top, bool valid triangle float x float y float z. So again, this function takes three real numbers as its arguments, floating point value variables, and outputs a true or false value, which is a Boolean, recall. So that's why the return type is bool. Then we define the function. First thing we do is check to make sure that all of the sides are positive. If x is less than or equal to 0, or if y is equal to 0, or if z is less than or equal to 0, that can't possibly be a triangle. They don't have positive sides. And so we can return false in that situation. Next, we check to make sure that every pair of inputs is greater than the third one. 

So if x plus y is less than or equal to z, or if x plus z is less than or equal to y, or if y plus z is less than or equal to x, that also can't be a valid triangle. So we return false again. Assuming we passed both of the checks though, then we can return true. Because those three sides are capable of returning-- of creating a valid triangle. And that's it. You've now declared and defined. And you may be able to now use and call this function. Great job. I'm Doug Lloyd. This is cs50.
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
  - [Functions](../../../concepts/functions.md) (`concept-functions`)

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
- https://cs50.harvard.edu/x/shorts/functions/ — retrieved 2026-10-18T05:41:11+03:30, sha256 `dc89da3e0c27c05a…`
- https://cdn.cs50.net/2017/fall/shorts/functions/lang/en/functions.txt — retrieved 2026-10-18T05:41:12+03:30, sha256 `74977c64bf8c5332…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
