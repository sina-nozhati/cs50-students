---
id: short-tcp
type: short
title: 'Short: TCP'
week: 8
parent: week-8
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.harvard.edu/x/shorts/tcp/
- https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.txt
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:11+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- short
- tcp
checksum: sha256:34a2d3388d99aca54831a94788e6d5502324dc027ffd1f861c6d593d388cd2be
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# Short: TCP

## 1. Source metadata
- **Title:** Short: TCP
- **Type:** short
- **Source type:** official
- **Official link(s):** <https://cs50.harvard.edu/x/shorts/tcp/>, <https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.txt>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:11+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.harvard.edu/x/shorts/tcp/>, <https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.txt> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

### Links on the short’s page

- Slides: <https://cdn.cs50.net/2017/fall/shorts/tcp/tcp.pdf>
- Subtitles: <https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.srt>
- Transcript: <https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.txt>
- CS50 Video Player: <https://video.cs50.io/GP7uvI_6uas>
- 360p: <https://cdn.cs50.net/2017/fall/shorts/tcp/tcp-360p.mp4.download>
- 720p: <https://cdn.cs50.net/2017/fall/shorts/tcp/tcp-720p.mp4.download>
- 1080p: <https://cdn.cs50.net/2017/fall/shorts/tcp/tcp-1080p.mp4.download>
- YouTube: <https://youtu.be/GP7uvI_6uas>

### Transcript (verbatim, English)

```text
In this video, we're gonna talk about the transmission control protocol TCP. If you haven't watched the video on internet protocol, IP, you may wish to do so before watching this video because the two are pretty interrelated. Um So the internet protocol again, a quick summary, that's the protocol that moves information from a sending machine to a receiving machine through the network. So what's TCP while just moving from a sending machine to a receiving machine isn't the full story. We also know that our program, our computers, for example, are running multiple programs and have multiple services running on those on those um machines. And so if we wanna get a, a packet or information to a specific program on a specific machine, we need more information than just trans than just what IP allows us to get information from point A to point B. So TCP can be thought of as directing the packet to the correct program or the correct service on the receiving machine. And so it's important to, as you might expect, know where it's supposed to go and what the packet is for at the same time. And so frequently when you talk about transmission control protocol, TCP. You really often hear it in the context TCP slash IP or just TCP/IP. These two protocols are so interrelated um that they are basically treated as a single unit, but they are two separate protocols that do two separate things. Again, IP is responsible for getting it from one machine to another and TCP is responsible for getting it to the correct program or the correct service on a machine. And it does something else that IP doesn't do which is guarantee delivery. So if we now couple an I machine's IP address with a so called port number and a port number is how a specific service, a utility or program is identified on a machine. If we now have an IP address plus a port number, now we can uniquely identify a particular service running on a particular machine. So that's why TCP and IP are so frequently interrelated because that port number on its own doesn't really mean anything if you need a port number and the machine that you're talking about the, what, what machine is supposed to be using this particular port. For example, the other thing that TCP though does though, as I said is it guarantees delivery. So in addition to specifying the port number, it also indicates how many packets, the internet protocol IP has split the data into and it orders those packets so that they can be reconstructed on the receiving machine even if they are received in an, in a different order than they were sent, which can happen because IP is a connection with protocol and so different packets can take different paths through the system. Some of these port numbers are very commonly used and they've been standardized across all computers by pretty much every computer manufacturer now. So there's something called FTP, the file transfer protocol which is used to transmit files as you might expect from one machine to another that uses port 21 conventionally email. SMTP uses port 25 DNS. The domain name system which we talked about in our internet primer video uses port 53. If you're ever browsing the web, you're pretty much always using port 80 unless you're browsing the web securely secure web browsing using port 443. So what's this TCP/IP process? What's happening with both of these protocols together? Well, let's talk about it when a program wants to send data, TCP helps break into chunks and communicates those packets to the computer's network software. So it takes the data and it wraps information around it. That indicates what port it's supposed to go to and what order that packet is out of all. So my packet one of 10, 2 of 10, 3 of 10 and so on. IP gets those data chunks that have been wrapped with TCP and wraps more information about where the packet is supposed to go. We might call this the IP layer surrounding the packet. So it's sort of like one of those nesting dolls, we have the data in the middle and then TCP on top of it telling it where the data inside of TCP is supposed to go to what port or what this service on a machine around. That is the IP layer, what IP address, what machine is actually getting this. So then that packet that's been wrapped with all those layers is sent through uh internet protocol through the system of routers getting from point A to point B when the receiving uh machine or device gets it, it looks at the IP layer, it says, yep, that's my IP address. So it takes off sort of cracks, the egg and takes off the IP layer. Then it sees that there's a TCP layer and it says OK, it looks like this is going to port X or port Y and apparently it's packet number eight of 15. So that's good to know. So then it can take that information, take off the TCP layer. Now knowing that it's for port X and it's packet number eight and it can get at the data inside and it can prepare the data to be organized in the correct way. And once all of the data is received TCP can hand it off to the correct service and say here you go, here's the data that you received. So that process might look something like this So let's send an email from a sender to a receiver. Now, let's say this email is pretty small. So we only need to break it into four packets and we'll call them ABC and D. Well, we want to move that first packet. What happens when we take that chunk of data that the data that is part of packet A and around that we're going to wrap it with a TCP layer emails you may recall are sent via port 25 and we have four chunks of data here that we're gonna be using. Uh and this is the first of them. So maybe our TCP layer contains information about, well, we're going to port 25 and this is packet number one of four around that. So now we have that all that information bundled up together. We're gonna say where we want it to go. What machine, what IP address is supposed to get this packet. And that's part of the IP layer and there's other information in there as well such as the return address in case that something goes wrong, it knows where to send information back and so on. Um But the IP layer goes around all of that, that entire thing is bundled together as one big unit and sent through an IP transfer. So it gets routed through the router network using internet protocol and the receiver receives the entire thing and then it can start to deconstruct what's happening here. It looks at the IP layer, the outside layer of this data and says, yep, that's my IP address. So it can discard that I can kind of ignore, it doesn't need it anymore and can look one level deeper. It sees that OK. This is a, this is data that is intended to be received on port 25. It's apparently the first part of four. So I'm gonna keep that in mind and look at the data and slot it roughly where I think it's going to go now because of the internet protocol. It's not necessarily the case that the next packet the receiver gets is packet two. In fact, the next thing the receiver gets might be packet number three because these packets took different paths because of different traffic on the network. And so I'm not gonna go through the diagram of building it up again, but packet three moves gets stripped away of all of its layers, the IP layer, the TCP layer and the data gets put in the right spot. And then let's say it receives packet four. Now let's say that's it. It doesn't get any more data. Well, what is it gonna do? Well, IP doesn't do anything for us but TCP does TCP knows. Well, I've received one of 43 of four and four of four. I'm not getting any more data. So something has gone wrong, but I can guarantee delivery. I know that packet number two is missing. And so TCP can now make a request sort of in the reverse direction, bundling up its request uh in much the same way and sending it via IP, which I know could lead to some sort of infinite loop of everybody dropping packets along the way. But suffice it to say that TCP says I'm missing a packet. I need to send information back to the sender. Fortunately, the sender's IP address is sort of bundled up in the IP layer. It's part of the, it's the return address on the envelope, say and say I'm missing packet number two. Can you please resend it when the sender receives that information, it doesn't have to send the entire email again. It only needs to send that individual piece of it that was missing so it can send a packet number two and when it gets it now, TCP says I have all four pieces of data that I need so I can assemble them together and take this entire block of information and pass it along to port 25 where it will be interpreted as an email. And that in this way, we've now sent an email from sender to receiver using TCP/IP. So as I said, at any point along the way something went wrong, TCP can deal with it, it can make a request that the information gets sent back to it and it can reconstruct the message and once it's reconstructed, the message from all of the packets it's received, then it can organize them and deliver them to the correct service. So that's TCP in a nutshell. That's how we guarantee delivery of information. Remember that TCP frequently works with IP. So these two protocols really do go hand in hand. We've discussed them in separate videos here because they do different things, but they're so interrelated that you'll usually use them together. I'm Doug Lloyd. This is CS 50.
```

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [Week 8 — HTML, CSS, JavaScript](../week.md) (`week-8`)
- **Backlinks (auto-generated):**
  - [Internet, TCP/IP, DNS and HTTP](../../../concepts/internet-and-http.md) (`concept-internet-and-http`)

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
- https://cs50.harvard.edu/x/shorts/tcp/ — retrieved 2026-10-18T05:42:11+03:30, sha256 `34a2d3388d99aca5…`
- https://cdn.cs50.net/2017/fall/shorts/tcp/lang/en/tcp.txt — retrieved 2026-10-18T05:42:12+03:30, sha256 `1aad9143753efdea…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
