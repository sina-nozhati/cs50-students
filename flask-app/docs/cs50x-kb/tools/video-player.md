---
id: tool-video-player
type: tool
title: CS50 Video Player
week: null
parent: tools
children: []
prerequisites: []
related: []
source_urls:
- https://cs50.readthedocs.io/video.cs50.io/
source_type: official
license: 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)'
attribution: CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.
retrieved_at: '2026-10-18T05:42:35+03:30'
review_status: verified-against-source
difficulty: null
generated_difficulty: null
languages: []
tags:
- tool
- video-player
checksum: sha256:9e08a4240f7043b80ca5ca01690a7e43f3bdc9d0bf95be55ca68bc19f489dabb
generated_language: fa
built_at: '2026-10-18T06:00:54+03:30'
---

# CS50 Video Player

## 1. Source metadata
- **Title:** CS50 Video Player
- **Type:** tool
- **Source type:** official
- **Official link(s):** <https://cs50.readthedocs.io/video.cs50.io/>
- **Review status:** verified-against-source
- **Retrieved:** 2026-10-18T05:42:35+03:30
- **License:** CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/); source: CS50x, Harvard University / David J. Malan (https://cs50.harvard.edu/x/license/)

## 2. OFFICIAL CONTENT
> Source: <https://cs50.readthedocs.io/video.cs50.io/> · CS50x 2026 © David J. Malan, Harvard University — licensed CC BY-NC-SA 4.0. Extracted for non-commercial educational use by CS50x Anzali.

<a id="cs50-video-player"></a>

### CS50 Video Player

CS50 Video Player is a web app at [video.cs50.io](https://video.cs50.io/) that synchronizes instructional videos (e.g., lectures) with screen recordings so that students can toggle between the two. (Videos must be hosted on [YouTube](https://www.youtube.com/).) The player also provides

* a searchable dropdown menu with hyperlinked captions, if the instructional video is public and has (English) subtitles, and
* a dropdown menu with hyperlinked chapters, if the instructional video’s description includes a table of contents.

Whenever the player is paused, the browser’s URL bar is updated with the timecode (in seconds) at which the video was paused, to facilitate linking to specific moments. And if a student closes the player’s tab before finishing a video, the player remembers where they left off and resumes at that timecode when the video is re-visited (provided its URL does not have an explicit `start` parameter).

<a id="api"></a>

#### API

CS50 Video Player supports URLs of the form

```
https://video.cs50.io/{id}
```

where `id` is the ID of an instructional YouTube video. URLs of that form additionally support, via GET, these HTTP parameters:

* `screen`, which, if present, is the ID of a screen recording to synchronize with the instructional video.
* `start`, which, if present, is a time, in seconds, at which to start playback. It must be non-negative, less than the duration of the video itself, and less than `end`, if present.
* `end`, which, if present, is a time, in seconds, at which to end playback (by pausing). It must be non-negative, less than the duration of the video itself, and greater than `start`, if present.
* `offset`, which, if present, is a time, in milliseconds, with an optional plus sign (`+`) or negative sign (`-`), by which to offset the screen recording from the instructional video. It is not necessary to encode `+` as `%2B`.

  * If you started recording the screen before you started recording the instructional video, `offset` should be negative. For instance, if you started recording the screen at 12:00:00 (noon), and you started recording the instructional video at 12:00:01, a second later, then `offset` should be `-1000`.
  * If you started recording the screen after you started recording the instructional video, `offset` should be positive. For instance, if you started recording the instructional video at 12:00:00 (noon), and you started recording the screen at 12:00:01, a second later, then `offset` should be `1000` (or `+1000`).
* `mute`, which, if present with a value of `1`, will mute the instructional video (and screen recording, if any) by default.

For example, [https://video.cs50.io/5azaK2cBKGw?screen=byyRAKSo_dM&start=438](https://video.cs50.io/5azaK2cBKGw?screen=byyRAKSo_dM&amp;start=438).

<a id="embedding"></a>

#### Embedding

CS50 Video Player can be embedded in other sites using an `iframe`. For example:

```
<iframe src="https://video.cs50.io/5azaK2cBKGw?screen=byyRAKSo_dM&start=438"></iframe>
```

To avoid [letterboxing](https://en.wikipedia.org/wiki/Letterboxing_(filming)) and [pillarboxing](https://en.wikipedia.org/wiki/Pillarbox), CS50 Video Player supports [iFrame Resizer](https://davidjbradshaw.github.io/iframe-resizer/), whereby you can set the player’s width yourself, as with CSS, and then use code like the below in order to set the player’s height dynamically:

```
<script src="https://cdn.jsdelivr.net/npm/iframe-resizer/js/iframeResizer.min.js"></script>
<script>
    document.querySelectorAll('iframe[src^="https://video.cs50.io/"]').forEach(function(element) {
        element.addEventListener('load', function() {
            iFrameResize(element);
        });
    });
</script>
```

<a id="captions"></a>

#### Captions

If an instructional video has (English) captions, they will be automatically imported from YouTube.

<a id="chapters"></a>

#### Chapters

If an instructional video has a table of contents in its description, it will be automatically imported as chapters from YouTube. A table of contents is defined as two or more lines in a video’s description formatted as

```
00:00 - Chapter
MM:SS - Chapter
MM:SS - Chapter
...
```

or

```
00:00:00 - Chapter
HH:MM:SS - Chapter
HH:MM:SS - Chapter
...
```

where `Chapter` is the chapter’s title; the hyphens are optional.

Per [YouTube](https://support.google.com/youtube/answer/9884579),

* the first timestamp must be 00:00 (or 00:00:00),
* there should be at least three timestamps in ascending order, and
* the minimum length for chapters is 10 seconds.

<a id="acknowledgements"></a>

#### Acknowledgements

Special thanks to CS50’s friends at [Google](https://www.google.com/) for their support of this app and to [@twemoji/api](https://www.npmjs.com/package/@twemoji/api) for its emoji!

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
_Nothing further stated by the source beyond section 2._
- Difficulty: not stated by source.

### 3b. GENERATED (fa)
_—_

## 4. Relationships
- **Parent:** [CS50 tools (index)](README.md) (`tools`)

## 5. GENERATED — application (fa)
> ⚠️ این بخش توسط سازنده‌ی پایگاه دانش تولید شده و جزو محتوای رسمی CS50 نیست.

### کاربرد آموزشی
مستند ابزار رسمی CS50؛ برای راهنمای فارسی نصب و استفاده و پاسخ‌گویی به سؤال‌های فنی دانشجویان.

### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
- فقط بر اساس محتوای رسمی بخش ۲ پاسخ بده و لینک دقیق (با anchor) را ذکر کن.
- اگر پاسخ در منبع نیست، صریحاً بگو «در منبع رسمی ذکر نشده» و حدس نزن.


### ایده‌های پیاده‌سازی در سایت
- نمایش این سند به‌صورت یک صفحه/کارت در بخش منابع (`Resource`) با پیوند به منبع رسمی و درج ذکر منبع و مجوز CC BY-NC-SA.
- نمایه‌سازی بخش‌های این سند در search.jsonl برای جست‌وجو و RAG.


## 6. References, review, gaps
- https://cs50.readthedocs.io/video.cs50.io/ — retrieved 2026-10-18T05:42:35+03:30, sha256 `9e08a4240f7043b8…`
- **Review date:** 2026-10-18 (build 2026-10-18T06:00:54+03:30)
- **Gaps / unverified items:**
- None recorded.
