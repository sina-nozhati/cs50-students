---
name: fullstack-engineer
description: >-
  روش‌شناسی و راهنمای fullstack برای ساخت و نگهداری پلتفرم Anzali-CS50-Hub —
  یک پلتفرم آموزشی CS50x انزلی ساخته‌شده با Flask + Jinja2 + HTMX + Tailwind + SQLite،
  دیپلوی‌شده روی VPS ایرانی با Nginx + Gunicorn. Use whenever the user builds, designs,
  debugs, deploys, scaffolds, or adds any feature to the CS50x Anzali platform (knowledge-base,
  assignments / taklifinow-style, gamification XP/streak/leaderboard, downloads/resources,
  admin upload panel, auth), or asks about its architecture, database models, or deployment.
  Also use whenever the user mentions "cs50", "انزلی", "anzali", "flask-app", "student-panel",
  "پنل دانش‌آموز", "تکلیف", "XP", "leaderboard", "آپلود فایل", "منابع هفته", or wants
  fullstack guidance across the 10 layers: requirements → architecture → database/ORM →
  backend → frontend → auth/security → testing → DevOps/CI → deployment/scaling → observability.
---

# Fullstack Engineer — Anzali-CS50-Hub

این اسکیل روش‌شناسی fullstack برای پلتفرم **Anzali-CS50-Hub** است: یک ابزار آموزشی زنده برای
کلاس CS50x بندر انزلی. کد بک‌اند واقعی در `flask-app/` در ریشه‌ی workspace قرار دارد.
این اسکیل هم برای ساخت ماژول‌های جدید و هم برای دیباگ/دیپلوی پلتفرم استفاده می‌شود.

> **اصل طلایی:** این پلتفرم همزمان «محصول» و «محوای آموزشی» است. بچه‌ها قرار است کد را
> بخوانند و با هم بسازندش. پس هر کدی که می‌نویسی باید **ساده، خوانا و به‌شدت کامنت‌گذاری‌شده**
> (به فارسی یا انگلیسی دوستانه) باشد. پیچیدگی‌های ناموجه ممنوع است.

---

## ۱. وقتی فعال می‌شوی (Triggers)

این اسکیل را فراخوانی کن هرگاه کاربر هر یک از این‌ها را خواست:

- ساخت/scaffold کردن اپ Flask، blueprint، یا ماژول جدید (KB، تکالیف، گیمیفیکیشن، دانلودها، ادمین).
- دیباگ، refactor، یا اضافه‌کردن feature به `flask-app/`.
- سؤال درباره‌ی مدل‌های دیتابیس (User, Assignment, Submission, XPLog, Resource).
- دیپلوی روی VPS ایرانی، کانفیگ Nginx + Gunicorn + systemd.
- آپلود فایل، پنل ادمین، امنیت، احراز هویت.
- بحث درباره‌ی معماری، انتخاب تکنولوژی، یا مقیاس‌پذیری.

عبارات ترلوداول: «پنل دانش‌آموز»، «تکلیف»، «XP»، «استریک»، «لیدربورد»، «منابع هفته»،
«آپلود فایل»، «دیپلوی روی سرور»، «flask-app»، «cs50 انزلی».

---

## ۲. چارچوب ۱۰لایه — تجسم‌یافته در CS50 انزلی

هر تصمیم فنی را از دریچه‌ی این ۱۰ لایه بررسی کن. لایه‌ها به‌ترتیب وابستگی چیده شده‌اند.

### L1 — Scope & Requirements (دامنه و نیازها)
پلتفرم چهار ماژول اصلی دارد با این اولویت: **KB > Assignment > Gamification > Resources**.
قبل از شروع هر feature، اولویت و minimum viable scope را تأیید کن. به یاد داشته باش:
۳ روز تا جلسه‌ی Flask وقت داری، پس همیشه نسخه‌ی قابل‌نمایش (Demo) بر محصول کامل ارجحیت دارد.
سند مرجع: `PROJECT_PLAN.md` در ریشه‌ی workspace.

### L2 — Architecture & Patterns (معماری)
**Clean Monolith** با الگوی **Application Factory** (`create_app`). منطق در سه لایه:
Routes (Controllers) → Services (منطق تجاری + گیمیفیکیشن) → Models (SQLAlchemy).
هر ماژول یک **Blueprint** مستقل است (`kb`, `assignments`, `gamification`, `auth`,
`resources`, `admin`). از میکروسرویس پرهیز کن — VPS ایرانی ۱ گیگ آن را تحمل نمی‌کند.

### L3 — Database & ORM (دیتابیس)
SQLAlchemy روی **SQLite** (نسخه‌ی اول — یک فایل، بک‌آپ = کپی فایل). طراحی باید
قابل‌مهاجرت به PostgreSQL باشد. مدل‌ها: `User`, `Assignment`, `Submission`, `XPLog`, `Resource`.
قانون: هرجا کوئری نوشتی، N+1 problem را چک کن و از `lazy='joined'` یا eager loading
استفاده کن. اسکیمای کامل و کد مدل‌ها در `references/anzali-implementation.md`.

### L4 — Backend (بک‌اند)
Flask + Blueprint‌ها. منطق تجاری هرگز در route قرار نگیرد — در `app/services/` باشد.
endpoint‌های تعاملی (مثل «من خواندم» یا ثبت XP) را با **HTMX** بنویس: یک روت POST که
fragment HTML برمی‌گرداند (نه redirect کامل). این یعنی بدون JavaScript سفارشی و بدون build.

### L5 — Frontend (فرانت‌اند)
**Jinja2 + HTMX + Tailwind (CDN)**. هیچ build-step ای وجود ندارد. Tailwind را از CDN
لود کن برای سادگی. کامپوننت‌ها را به‌شکل Jinja macro در `templates/_partials/` بساز.
طراحی باید **mobile-first** و سبک باشد (اینترنت ضعیف ایران، موبایل دانش‌آموزان).

### L6 — Auth & Security (احراز هویت و امنیت)
لاگین ساده در فاز اول (نام + رمز ثابت کلاس از config). نقش `is_admin` روی User برای
پنل ادمین. هنگام آپلود فایل **حتماً** از `werkzeug.utils.secure_filename` استفاده کن و
extension را allowlist کن (`.pdf`, `.zip`). از path traversal جلوگیری کن. کلید secret
هرگز در کد هاردکد نشود — از environment variable بخوان. (جزئیات OWASP سبک‌شده در reference.)

### L7 — Testing & Quality (آزمون)
pytest برای service layer. smoke test برای route‌های اصلی (GET /kb, /assignments, /resources).
fixture برای DB in-memory SQLite. تست آپلود را با file fake انجام بده. هدف پوشش منطق
تجاری است، نه ۱۰۰٪ خط — باز هم سادگی بر покрытие کامل ارجح است.

### L8 — DevOps & CI (عملیات توسعه)
هر feature در یک venv تمیز قابل اجرا باشد (`requirements.txt` دقیق). script `init_db.py`
برای seed کردن داده‌های اولیه (شامل Resource‌های کپی‌شده). اگر CI خواستی: GitHub Actions
با `pip install -r requirements.txt && pytest`. روی VPS هیچ build ای نیاز نیست — فقط pull + restart.

### L9 — Deployment & Scaling (استقرار و مقیاس)
**Nginx** (reverse proxy + سرو کردن static با cache ۳۰ روزه) + **Gunicorn** (2 workers،
bind به 127.0.0.1:5000) + **systemd** (auto-restart). کانفیگ کامل در `references/anzali-implementation.md`.
برای SQLite با ۵۰ کاربر همزمان کافی است. اگر رشد کرد: migrate به Postgres (فقط تغییر
connection string به‌خاطر SQLAlchemy) و اضافه‌کردن Redis cache بعداً.

### L10 — Observability & Maintenance (مشاهده‌پذیری و نگهداری)
logging سبک به stdout (برای جمع‌آوری توسط systemd journal). endpoint `/health` برای
uptime monitoring. **بک‌آپ روزانه SQLite**: یک cron که فایل `instance/cs50.db` را کپی
می‌کند (با SQLite WAL باید از `sqlite3 .backup` استفاده کن، نه کپی خام). لاگ XPLog به‌عنوان
audit trail برای گیمیفیکیشن.

---

## ۳. گردش کار استاندارد (Workflow)

هرگاه feature یا باگ جدیدی داری، این ترتیب را بگیر:

1. **دامنه (L1):** اولویت و MVP scope را با کاربر تأیید کن. آیا در نقشه‌ی ۳ روزه جا دارد؟
2. **مدل (L3):** اگر داده‌ی جدیدی لازم است، اول مدل SQLAlchemy را بنویس + migration/seed.
3. **سرویس (L4):** منطق تجاری را در `app/services/` به‌صورت تابع خالص بنویس (قابل تست).
4. **Route (L4):** Blueprint را بساز/تکمیل کن. اگر تعاملی است، HTMX fragment برگردان.
5. **تمپلیت (L5):** Jinja + Tailwind. mobile-first. کامنت دوستانه برای بچه‌ها.
6. **گیمیفیکیشن:** اگر کاربر با تعامل XP می‌گیرد، `XPLog` را آپدیت کن.
7. **امنیت (L6):** اگر فرم/آپلود/auth داره، secure_filename، allowlist، نقش را چک کن.
8. **تست (L7):** حداقل یک smoke test برای route جدید.
9. **دیپلوی (L9):** اگر روی VPS است، فقط pull + `systemctl restart cs50hub`.

برای جزئیات پیاده‌سازی هر گام، فایل reference مناسب را بخوان.

---

## ۴. فایل‌های مرجع (Progressive Disclosure)

بدنه‌ی این اسکیل عمداً کوتاه است. وقتی به جزئیات نیاز داری:

- **`references/anzali-implementation.md`** — ساختار کامل پوشه‌ها، کد `app.py` با `create_app`،
  کد کامل تمام مدل‌ها، نمونه blueprint‌ها (kb, assignments, gamification, auth, resources, admin)،
  endpoint آپلود ادمین، و کانفیگ کامل Nginx + systemd. **این فایل را قبل از نوشتن کد Flask بخوان.**
- **`references/layer-blueprints.md`** — هر لایه‌ی ۱۰گانه با checklist، anti-pattern و مثال
  ملموس در بستر CS50 انزلی. برای تصمیم‌گیری عمیق درباره‌ی یک لایه‌ی خاص بخوان.

قانون ساده: اگر قرار است کد Flask بنویسی، حداقل `anzali-implementation.md` را بخوان.
اگر درباره‌ی یک لایه (مثلاً امنیت یا دیپلوی) تصمیم architecture می‌گیری،
`layer-blueprints.md` را هم بخوان.

---

## ۵. بایاس‌های غیرقابل‌مذاکره‌ی پروژه

این سه اصل، هر تصمیم فنی را باید هدایت کنند:

1. **سادگی برای آموزش.** این کد هم محتوای آموزشی است. اگر بین «راه‌حل هوشمند» و
   «راه‌حل خوانا» انتخاب داری، خوانا برنده است. نام‌گذاری واضح، توابع کوتاه، کامنت فارسی.
2. **کارایی روی VPS ضعیف ایرانی.** ۱ گیگ رم، ۱ هسته، اینترنت نوسانی. هر dependency،
   هر build-step، هر process اضافی هزینه دارد. SQLite نه Postgres. Jinja نه React. CDN نه npm.
3. **کامنت‌گذاری دوستانه.** بچه‌های CS50 قرار است از این کد یاد بگیرند. هر تابع غیربدیهی
   یک کامنت «این چه کار می‌کند و چرا» دارد — به فارسی یا انگلیسی ساده.

---

## ۶. وضعیت فعلی پروژه (مرجع سریع)

- **مسیر کد:** `F:\Projects\cs50x\student-panel\flask-app\`
- **منابع خام PDF:** `D:\Projects\CS50xAnzali\Weeks\0..8\` (الان در `flask-app/static/downloads/weekN/` کپی و rename شده‌اند)
- **پلن اجرایی:** `PROJECT_PLAN.md` در ریشه
- **Stack:** Python 3.12+ / Flask / Flask-SQLAlchemy / Jinja2 / HTMX / Tailwind (CDN) / SQLite / Nginx / Gunicorn
- **ماژول‌ها:** KB (هفته ۰–۸)، Assignments (taklifinow-style)، Gamification (XP/streak/leaderboard)، Resources (دانلود + آپلود ادمین)، Auth + Admin.

اگر کاربری پرسید «پروژه کجاست؟» یا خواست شروع کند، از بخش ۳ (Workflow) شروع کن و
فایل `anzali-implementation.md` را برای کد آماده بخوان.
