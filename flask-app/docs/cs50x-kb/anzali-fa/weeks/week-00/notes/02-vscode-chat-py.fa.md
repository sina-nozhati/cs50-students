---
id: w00-n02
type: note
title: VS Code و برنامهٔ chat.py (Visual Studio Code and chat.py)
title_fa: VS Code و برنامهٔ chat.py
title_en: Visual Studio Code and chat.py
week: 0
parent: w00-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: Visual Studio Code and chat.py
official_anchor: visual-studio-code-and-chatpy
source_url: https://cs50.harvard.edu/x/notes/0/#visual-studio-code-and-chatpy
source_refs:
- src-notes-0#visual-studio-code-and-chatpy
- src-week-0#week-0-scratch
- src-syllabus-honesty
- src-cs50-ai
- src-transcript-0
concept_ids:
- w00-c-academic-honesty-ai
- w00-c-ide
- w00-c-variable
prev: w00-n01
next: w00-n03
order: 2
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:16+03:30'
verified_at: '2026-10-18T07:35:00+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; Scratch blocks, code and pseudocode copied exactly from the official notes; authored examples are marked تألیفی; transcript-only material is labelled.
---

# VS Code و برنامهٔ chat.py

> **منبع رسمی:** بخش «Visual Studio Code and chat.py» از [درس‌نامهٔ هفتهٔ ۰ CS50x 2026](https://cs50.harvard.edu/x/notes/0/#visual-studio-code-and-chatpy). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کد و بلوک‌ها عیناً از منبع آمده‌اند؛ مثال‌های **تألیفی** و نکته‌های **سخنرانی** جدا برچسب خورده‌اند.

## چرا این بخش مهم است

این بخش طعمِ چیزی را می‌چشاند که بعدها خودت می‌سازی: یک چت‌بات (chatbot) در حدود ده خط کد. همچنین قانون مهمی از دوره را یادآوری می‌کند: **در CS50 فقط اردک CS50 (CS50 Duck) مجاز است.**

## محیط توسعهٔ یکپارچه (IDE)

- VS Code یک **محیط توسعهٔ یکپارچه** (integrated development environment, IDE) است: جایی که کد می‌نویسی.
- طبق متن سخنرانی، VS Code تقریباً یک ویرایشگر متن است (مثل Notepad)، اما بدون قالب‌بندی‌هایی مثل پررنگ و زیرخط‌دار. پایین صفحه هم یک **پنجرهٔ ترمینال** (terminal) هست که در آن به کامپیوتر فرمان می‌دهی. جزئیات آن در هفتهٔ بعد می‌آید.

## سه نسخهٔ chat.py (کد دقیقاً مطابق درس‌نامه)

> **هشدار رسمی صفحهٔ هفته:** کد `chat.py` عمداً در فایل‌های منبع دوره نیامده است، چون به پیکربندی زیادی نیاز دارد و فقط برای نمایش بوده است. **خودت سعی نکن آن را اجرا کنی.**

نسخهٔ ۱. سؤال ثابت (hard-coded):

```py
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="In one sentence, what is CS50?",
    model="gpt-5"
)

print(response.output_text)
```

توضیح درس‌نامه به فارسی: یک کتابخانه (library) از OpenAI وارد (import) می‌شود تا قابلیت‌هایش در اختیار ما باشد. یک «کلاینت» چت ساخته می‌شود. یک سؤال به نام `input` به `client` داده می‌شود و پاسخ (`response`) چاپ می‌شود.

نسخهٔ ۲. پرسیدن سؤال از کاربر:

```py
from openai import OpenAI

client = OpenAI()

prompt = input("Prompt: ")

response = client.responses.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)
```

حالا `prompt` ساخته شده و کاربر خودش سؤال را تایپ می‌کند.

نسخهٔ ۳. افزودن «پرامپت سیستمی» (system prompt):

```py
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

`system_prompt` زمینه و دستورهای بیشتری به چت‌بات می‌دهد؛ مثلاً «جوابت را به یک جمله محدود کن و وانمود کن گربه‌ای».

## خروجی مشاهده‌شده در سخنرانی

طبق متن سخنرانی، نسخهٔ سوم برای سؤال «what is CS50» پاسخی یک‌جمله‌ای داد که با «meow» تمام می‌شد. خروجی مدل‌های زبانی **ثابت نیست**؛ در خود سخنرانی هم با تکرار همان سؤال، پاسخ کمی فرق کرد.

## تعریف‌ها

- **کتابخانه (library):** کدی که دیگران نوشته‌اند و با import از آن استفاده می‌کنیم.
- **API (Application Programming Interface):** در سخنرانی آمده است: سرویسی که شرکتی ارائه می‌دهد و ما روی آن کد می‌نویسیم.
- **متغیر (variable):** طبق سخنرانی، مثل `x` یا `y` در ریاضی، مقداری را نگه می‌دارد. اینجا `prompt` متن کاربر را نگه می‌دارد.
- **پرامپت کاربر / پرامپت سیستمی (user prompt / system prompt):** پیام کاربر، در برابر دستورهای ثابتی که رفتار مدل را تعیین می‌کند.

## سیاست صداقت علمی دربارهٔ AI

- CS50 اردک پلاستیکی خودش، یعنی [CS50 Duck](https://cs50.ai)، را ساخته تا در کارهای دوره به تو کمک کند.
- طبق درس‌نامه، [سیاست صداقت علمی](https://cs50.harvard.edu/x/syllabus/#academic-honesty) استفاده از **هر ابزار AI به‌جز CS50 Duck** را ممنوع می‌کند.
- طبق سخنرانی، این اردک طوری طراحی شده که مثل یک معلم خصوصی خوب رفتار کند: تو را به سمت راه‌حل هدایت کند، بدون اینکه جواب را لو بدهد.
- **روش اردک پلاستیکی (rubber duck debugging):** طبق سخنرانی، وقتی با اشکالی گیر کرده‌ای، مشکل را بلند برای یک اردک (یا هر شیء بی‌جانی) توضیح بده. همین توضیح دادن اغلب باعث می‌شود اشتباه را خودت پیدا کنی.

## اشتباه‌های رایج

- تلاش برای اجرای `chat.py` روی سیستم خودت. صفحهٔ رسمی صراحتاً می‌گوید این کار را نکن.
- فرض اینکه پاسخ چت‌بات همیشه یکسان یا همیشه درست است.
- استفاده از ChatGPT، Gemini یا ابزارهای مشابه در پرابلم‌ست‌ها. این کار طبق سیاست دوره مجاز نیست.

## محدودیت‌ها

هدف این مثال فقط نمایش است. معنای دقیق `import`، `client.responses.create` و `print` در هفته‌های بعد، در Python، توضیح داده می‌شود.

## جمع‌بندی

- IDE جای نوشتن و اجرای کد است.
- با ده خط کد می‌شود برنامه‌ای قدرتمند ساخت، چون روی کار دیگران (کتابخانه و API) سوار می‌شویم.
- در CS50 فقط CS50 Duck مجاز است.

## سؤال‌های خودآزمایی

1. تفاوت نسخهٔ ۱ و نسخهٔ ۲ برنامهٔ `chat.py` چیست؟
2. `system_prompt` چه نقشی دارد؟
3. چرا نباید `chat.py` را خودت اجرا کنی؟
4. طبق سیاست دوره، کدام ابزار AI مجاز است؟

**پاسخ کوتاه:** ۱) در نسخهٔ ۲ سؤال از کاربر گرفته می‌شود (`input`)، نه اینکه ثابت در کد باشد. ۲) دستورهای ثابتی برای رفتار مدل می‌دهد. ۳) صفحهٔ هفته می‌گوید پیکربندی زیادی لازم دارد و فقط برای نمایش بوده. ۴) فقط CS50 Duck.

## پیوندها

- قبلی: [خوش آمدید: هوش مصنوعی و اهمیت اصول پایه](/kb/d/w00-n01)
- بعدی: [علوم کامپیوتر، حل مسئله و دودویی](/kb/d/w00-n03)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-00/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
