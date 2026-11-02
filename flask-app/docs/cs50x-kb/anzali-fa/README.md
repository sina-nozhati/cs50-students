# پایگاه دانش فارسی CS50x Anzali — پایلوت هفتهٔ ۰

این بسته پایگاه دانش فارسی و چارچوب یادگیری گیمیفای‌شدهٔ **هفتهٔ ۰ (Scratch)** دورهٔ CS50x 2026 است. هفته‌های دیگر عمداً ساخته نشده‌اند.

- **محتوای رسمی:** CS50x 2026 © David J. Malan, Harvard University، با مجوز CC BY-NC-SA 4.0.
- **بازنویسی فارسی و محتوای تألیفی:** CS50x Anzali، با همان مجوز (غیرتجاری، اشتراک یکسان).
- هیچ سؤال یا کارتی سؤال رسمی هاروارد نیست. XP و نشان‌ها اثری بر نمره یا مدرک رسمی CS50 ندارند.

## ساختار

| مسیر | محتوا |
| --- | --- |
| `curriculum/course-overview.fa.md` | نمای کلی دوره |
| `curriculum/learning-map.json` | ۴۶ مفهوم، ۵۱ یال پیش‌نیازی، ۵ مرحله |
| `curriculum/glossary.fa.json` | ۷۹ اصطلاح و قراردادهای نگارشی |
| `weeks/week-00/overview.fa.md` | نمای کلی هفته (سند hub با شناسهٔ `w00-fa`) |
| `weeks/week-00/notes/*.fa.md` | ۱۶ یادداشت، یکی برای هر بخش رسمی درس‌نامه |
| `weeks/week-00/summary.fa.md` | جمع‌بندی (Summing Up) |
| `weeks/week-00/curriculum.json` | ترتیب درس‌ها، مراحل و معیار تسلط هفته |
| `weeks/week-00/lessons/*.json` | ۱۰ درس و ۳۳ واحد کوچک |
| `weeks/week-00/flashcards.json` | ۴۹ فلش‌کارت (آماده برای Leitner و SM-2) |
| `weeks/week-00/quizzes.json` | ۴۶ سؤال، ۱۰ تمرین درس و ۱ آزمون تسلط |
| `weeks/week-00/activities.json` | ۳۳ فعالیت |
| `weeks/week-00/problem-sets/` | پرابلم‌ست Starting from Scratch: الزامات رسمی، راهنمای آموزشی، بدون راه‌حل |
| `weeks/week-00/sources.json` | ۴۲ منبع و ۱۰ اختلاف ثبت‌شده |
| `gamification/` | `rules.json`، `achievements.json` (۱۲ نشان)، `xp-config.json` |
| `schemas/` | ۱۶ JSON Schema (draft 2020-12) |
| `integration/index.fragment.json` | نودهای آماده برای index.json لودر محلی |
| `validation/` | گزارش پوشش، نتایج اعتبارسنجی و موارد باز |

## نصب در پنل (پیشنهاد؛ انجام نشده)

1. پوشهٔ `knowledge-base/` را به `flask-app/docs/cs50x-kb/anzali-fa/` کپی کن.
2. دستور زیر را اجرا کن:
   ```bash
   python3 _tools/merge_index_fragment.py --index flask-app/docs/cs50x-kb/index.json --out /tmp/index.merged.json
   ```
3. تفاوت را بررسی کن و سپس فایل را دستی جایگزین کن. برای نمایش اسناد، تغییر کد یا وابستگی جدید لازم نیست.

## اعتبارسنجی

```bash
cd _tools && python3 -m venv venv && ./venv/bin/pip install jsonschema "Markdown>=3.5" pyyaml
./venv/bin/python validate.py
```

## شناسه‌ها

| نوع | الگو |
| --- | --- |
| یادداشت | `w00-nNN` |
| مفهوم | `w00-c-*` |
| هدف | `w00-oNN` |
| درس | `w00-lNN` |
| واحد | `w00-lNN-uNN` |
| فلش‌کارت | `w00-fc-NNN` |
| سؤال | `w00-q-NNN` |
| فعالیت | `w00-a-*` |
| نشان | `w00-ach-*` |
| منبع | `src-*`؛ ارجاع به صورت `src-id#anchor` |

برچسب‌های منشأ: `official`، `translated-rewritten`، `authored`، `inference`.
