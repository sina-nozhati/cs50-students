---
id: w71-n03
type: note
title: مهندسی پرامپت، کد chat3.py و Copilot (Prompt Engineering and Copilot)
title_fa: مهندسی پرامپت، کد chat3.py و Copilot
title_en: Prompt Engineering and Copilot
week: 71
week_slug: week-ai
parent: w71-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Prompt Engineering and Copilot
official_anchor: prompt-engineering-and-copilot
source_url: https://cs50.harvard.edu/x/2026/notes/ai/#prompt-engineering-and-copilot
source_refs:
- src-notes-71#prompt-engineering-and-copilot
- src-transcript-71
- src-code-71
- src-honesty-71
- src-cs50-ai
- src-anzali-authored-71
- src-srt-71
concept_ids:
- w71-c-prompt-engineering
- w71-c-system-prompt
- w71-c-user-prompt
- w71-c-api-client
- w71-c-copilot
- w71-c-ai-policy
prev: w71-n02
next: w71-n04
order: 3
video:
  youtube_id: -9bo8HlSxwQ
  start: '7:59'
  start_seconds: 479
  url: https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=479s
  origin: inference
  basis: first ai.srt cue (after the previous note's cue) containing the phrase 'prompt engineering'
official_blocks:
- chat3
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:40+03:30'
verified_at: '2026-10-31T13:23:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite of the official AI notes; official code/pseudocode blocks are byte-identical copies from the notes; transcript-only facts are marked «از سخنرانی»; authored material and authored Python are marked تألیفی. Images are linked by their official URLs, not re-hosted. Callouts use GitHub-style markers followed by a bold Persian label line.
---

# مهندسی پرامپت، کد chat3.py و Copilot

> **منبع رسمی:** بخش «Prompt Engineering and Copilot» از [درس‌نامهٔ جلسهٔ هوش مصنوعی CS50x 2026](https://cs50.harvard.edu/x/2026/notes/ai/#prompt-engineering-and-copilot). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۷:۵۹ تا حدود ۱۷:۵۰](https://www.youtube.com/watch?v=-9bo8HlSxwQ&t=479s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

اردک CS50 همان مدل‌هایی را به کار می‌برد که در ChatGPT می‌بینی؛ فرقش در **دستورهایی** است که تیم درس به آن می‌دهد. این بخش دو نوع پرامپت را جدا می‌کند، کد کوتاهی را نشان می‌دهد که با آن یک مدل را از پایتون صدا می‌زنی و می‌گوید CS50 دربارهٔ ابزارهای هوش مصنوعی چه قاعده‌ای دارد.

## مهندسی پرامپت

- **مهندسی پرامپت** (`prompt engineering`) راهی است برای اینکه از هوش مصنوعی **پرسش خوب** بپرسی.
- از سخنرانی: مالان گفت این کار بیشتر هنر پرسیدن است تا مهندسی: پرسشت را با جزئیات و زمینهٔ کافی بنویس تا پاسخ، به احتمال زیاد، همان باشد که می‌خواهی.
- با **پرامپت سیستمی** (`system prompt`) به هوش مصنوعی یاد می‌دهیم چطور با کاربر رفتار کند. CS50 با چنین پرامپتی به هوش مصنوعی یاد می‌دهد با دانشجو چطور کار کند.
- **پرامپت کاربر** (`user prompt`) همان چیزی است که کاربر برای تعامل با هوش مصنوعی می‌نویسد. دانشجو با این پرامپت‌ها با اردک حرف می‌زند.
- از سخنرانی: خلاصهٔ پرامپت سیستمی اردک (که در واقع خیلی بلندتر است) این بود: تو دستیار آموزشی دوستانه و حامی CS50 هستی؛ تو یک اردک پلاستیکی هم هستی؛ فقط دربارهٔ CS50 و علوم کامپیوتر جواب بده؛ پاسخ کامل پرابلم‌ست‌ها را نده، چون صداقت تحصیلی را نقض می‌کند. بعد از این مقدمه، پرسش دانشجو، یعنی پرامپت کاربر، اضافه می‌شود.

## صدا زدن مدل از پایتون

درس‌نامه همین ایده را با این کد پایتون نشان می‌دهد:

```python
# Adds to system prompt.

from openai import OpenAI

client = OpenAI()

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretend you're a cat."

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)
```

- از سخنرانی: این همان کدی است که در هفتهٔ ۰ نوشته شد. کتابخانهٔ OpenAI وارد می‌شود و متغیر `client` دسترسی به آن را می‌دهد. `user_prompt` با `input` از کاربر گرفته می‌شود و `system_prompt` می‌گوید «پاسخت را به یک جمله محدود کن. وانمود کن گربه‌ای.»
- تابع `client.responses.create` سه آرگومان می‌گیرد: `input` (پرامپت کاربر)، `instructions` (پرامپت سیستمی) و `model` (نسخهٔ مدلی که می‌خواهی). در پایان، `response.output_text` چاپ می‌شود.
- درس‌نامه می‌گوید این کد را با `python chat.py` اجرا کنی، اما فایل قابل دانلود در کد منبع سخنرانی [chat3.py](https://cdn.cs50.net/2025/fall/lectures/ai/src/chat3.py?download) نام دارد (d187).

> [!WARNING]
> **تألیفی: پیش از اجرا**
> این برنامه با سرورهای OpenAI حرف می‌زند و برای اجرا به حساب و کلید API (که هزینه دارد) نیاز دارد. لازم نیست آن را اجرا کنی تا ایده را بفهمی. در این بسته کد فقط با یک ماژول جایگزین محلی بررسی شده است؛ هیچ درخواستی به OpenAI فرستاده نشده (D84).

**نمونهٔ تألیفی (پایتون):** همان ایدهٔ «پرامپت سیستمی، سپس پرسش کاربر» بدون هیچ سرویس بیرونی:

```python
system_prompt = "You are a rubber duck. Answer this question:"
user_prompt = input("Prompt: ")
print(system_prompt + " " + user_prompt)
```

## تولید کد و Copilot

- هوش مصنوعی مولد می‌تواند **کد** هم تولید کند. این توانایی، توان برنامه‌نویسی را که در حال رشد و تمرین است چند برابر می‌کند.
- **Copilot** یکی از این ابزارهای تولید کد است.
- از سخنرانی: مالان در VS Code قابلیتی را روشن کرد که CS50 از آغاز درس برای همهٔ دانشجویان خاموش می‌کند (Copilot) و از آن خواست تابع‌های پرابلم‌ست Speller را بنویسد؛ کاری که به گفتهٔ او برای بیشتر دانشجویان ۵، ۱۰ یا ۱۵ ساعت طول کشیده بود. پیشنهادها در چند ثانیه آمد. او تأکید کرد که فرض درست بودن آن کد «فرض بزرگی» است و اگر خودت چشم خواندن کد را نداشته باشی، نمی‌توانی آن را عیب‌یابی، توضیح یا اصلاح کنی.

> [!IMPORTANT]
> **قاعدهٔ رسمی CS50 دربارهٔ هوش مصنوعی**
> درس‌نامه: در CS50 استفاده از هوش مصنوعی مولد، **بیرون از ابزارهای خود درس**، مجاز نیست. [سیاست صداقت تحصیلی](https://cs50.harvard.edu/x/honesty/) روشن می‌گوید چه استفاده‌ای معقول است و چه استفاده‌ای نیست:
>
> - **معقول:** استفاده از نرم‌افزارهای مبتنی بر هوش مصنوعی خود CS50، از جمله اردک CS50 (ddb) در cs50.ai و cs50.dev.
> - **نامعقول:** استفاده از نرم‌افزارهای مبتنی بر هوش مصنوعی دیگر (مثل ChatGPT، Claude، Copilot، Gemini و مانند آن‌ها) که پاسخ پرسش‌ها یا سطرهای کد را پیشنهاد یا کامل می‌کند.
>
> از سخنرانی: مالان گفت قابلیت تولید کد VS Code تا پایان درس، یعنی تا **پروژهٔ نهایی**، مجاز نیست و در آنجا استفاده از آن را تشویق هم می‌کنند. شرط دقیق پروژهٔ نهایی را از صفحهٔ رسمی پروژهٔ نهایی بخوان؛ این بسته آن را جداگانه تأیید نکرده است.

## پیوندها

- قبلی: [هوش مصنوعی مولد](/kb/d/w71-n02)
- بعدی: [هوش مصنوعی در بازی‌ها و درخت تصمیم](/kb/d/w71-n04)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-ai/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
