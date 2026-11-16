# معماری فنی پلتفرم CS50x Anzali (Technical Architecture)

**نسخه:** 1.0  
**تاریخ تدوین:** ۲۴ آبان ۱۴۰۵  
**پشته نرم‌افزاری:** Flask 3.x + Jinja2 + HTMX + Alpine.js + Tailwind CSS + SQLite (WAL) + Nginx + Gunicorn  

---

## ۱. نمای کلان معماری سامانه (System Architecture Diagram)

```text
+-----------------------------------------------------------------------------------+
|                                  CLIENT LAYER                                     |
|  Responsive Web & PWA (Desktop, Tablet, Mobile)                                  |
|  - Alpine.js (State & Micro-interactions)     - HTMX (AJAX partial swaps)        |
|  - GSAP & Lenis (Physics animations & scroll) - Tailwind CSS (Harvard theme)      |
+----------------------------------------+------------------------------------------+
                                         | HTTPS (TLS 1.3)
                                         v
+-----------------------------------------------------------------------------------+
|                            REVERSE PROXY & STATIC EDGE                            |
|  Nginx (iran-vps.cs50anzali.ir)                                                   |
|  - SSL Termination & HTTP/2                  - Static Asset Caching (Cache-Control)|
|  - Rate Limiting Zone                         - Protected Downloads proxying     |
+----------------------------------------+------------------------------------------+
                                         | Unix Domain Socket / HTTP (127.0.0.1:8000)
                                         v
+-----------------------------------------------------------------------------------+
|                             WSGI APPLICATION SERVER                               |
|  Gunicorn (Workers: 2-4, Sync/Gthread, Timeout: 120s)                             |
|  +-----------------------------------------------------------------------------+  |
|  |                          FLASK CORE (Application Factory)                   |  |
|  |  +---------------------+ +----------------------+ +-----------------------+|  |
|  |  | Blueprints (7)      | | Middleware           | | CLI Commands          ||  |
|  |  | - main (Dashboard)  | | - CSRFProtect (WTF)  | | - create-admin        ||  |
|  |  | - kb (Reader & Hub) | | - LoginManager       | | - init-db             ||  |
|  |  | - assignments       | | - SQLite PRAGMA Hook | | - seed-weeks          ||  |
|  |  | - gamification      | +----------------------+ +-----------------------+|  |
|  |  | - auth & profile    |                                                    |  |
|  |  | - resources         |                                                    |  |
|  |  | - admin             |                                                    |  |
|  |  +---------------------+                                                    |  |
|  +-------------------------------------+---------------------------------------+  |
+----------------------------------------|------------------------------------------+
                                         |
         +-------------------------------+-------------------------------+
         |                                                               |
         v                                                               v
+----------------------------------+          +-------------------------------------+
|        BUSINESS SERVICE LAYER    |          |         KNOWLEDGE BASE ENGINE       |
| - xp.py (Idempotent awards)      |          | - kb_repo.py (File index & caching) |
| - streak.py (UTC daily activity) |          | - md_render.py (Markdown + Pygments)|
| - practice.py (Challenge runner) |          | - kb_content.py (Nav & roadmaps)    |
| - adaptive.py (BKT + Leitner)    |          +------------------+------------------+
| - diagnostics.py (Mistake vault) |                             |
| - cohorts.py (Multi-course org)  |                             v
| - engagement.py (Risk modeling)  |          +-------------------------------------+
+----------------+-----------------+          |      STORAGE HIERARCHY (Disk)       |
                 |                            | docs/cs50x-kb/anzali-fa/            |
                 v                            |  ├── weeks/ (week-00 .. week-10)    |
+----------------------------------+          |  │    ├── notes/ (*.fa.md)          |
|    PERSISTENCE LAYER (SQLite)    |          |  │    ├── lessons/ (*.json)         |
| instance/cs50.db (WAL Mode)      |          |  │    ├── quizzes.json              |
| - 20 Relational Models           |          |  │    ├── challenges.json           |
| - PRAGMA busy_timeout=5000       |          |  │    └── flashcards.json           |
| - PRAGMA cache_size=-16000 (RAM) |          |  ├── schemas/ (16 JSON Schemas)     |
| - Foreign Keys Enforced          |          |  └── gamification/ (Rules & Badges) |
+----------------------------------+          +-------------------------------------+
```

---

## ۲. الگوی کارخانه نرم‌افزار و معماری بلوپرینت‌ها (App Factory & Blueprints)

پلتفرم با استفاده از الگوی استاندارد **Application Factory** در فایل `app/__init__.py` مقداردهی اولیه می‌شود:

```python
def create_app(config_object: str = "app.config.Config") -> Flask:
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=os.path.join(project_root, "templates"),
        static_folder=os.path.join(project_root, "static"),
    )
    app.config.from_object(config_object)
    
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    
    # ثبت بلوپرینت‌های هفت‌گانه
    app.register_blueprint(main.bp)
    app.register_blueprint(kb.bp)
    app.register_blueprint(assignments.bp)
    app.register_blueprint(gamification.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(resources.bp)
    app.register_blueprint(admin.bp)
    
    return app
```

### تفکیک وظایف بلوپرینت‌ها
1. **`main` (`/`):** مدیریت لندینگ، داشبورد دانش‌آموز، وضعیت دوره‌ها (`/my-courses`)، کلینیک یادگیری (`/diagnostics`)، و روت‌های تمرین تطبیقی سراسری (`/practice`).
2. **`kb` (`/kb`):** موتور رندر درسنامه‌ها، هاب هفتگی، خوانشگر اسناد با کشویی سرفصل‌ها، و APIهای تعاملی (فلش‌کارت، کوییز و تمرینات هفته).
3. **`assignments` (`/assignments`):** مدیریت مشاهده ددلاین‌ها و ارسال لینک مخزن گیت‌هاب تکالیف توسط دانشجو.
4. **`gamification` (`/gamification`):** جدول رتبه‌بندی کلاسی (Leaderboard) و محاسبه جایگاه کاربر.
5. **`auth` (`/`):** سیستم لاگین با حفاظت از ورود تصادفی، خروج، و تغییر رمز عبور.
6. **`resources` (`/resources`):** کاتالوگ دانلود اسلایدها و منابع کد هفتگی.
7. **`admin` (`/admin`):** مدیریت متمرکز دانشجویان، نمره‌دهی و درج بازخورد، تعریف تکالیف، ساخت دوره‌ها، و آپلود بسته‌های پایگاه دانش.

---

## ۳. طرح تفصیلی پایگاه داده (Data Schema & Relational Map)

### مدل‌های بیست‌گانه و ارتباطات (Relationships)

```text
[Course] 1 ────< [Cohort] 1 ────< [Enrollment] >──── 1 [User]
                                                          │
   ┌──────────────────────┬───────────────────────────────┼───────────────────────────────┐
   │ 1                    │ 1                             │ 1                             │ 1
   v *                    v *                             v *                             v *
[Submission] >── 1 [Assignment] [XPLog]               [WeekProgress]                  [Notification]
   │
   v (Self-contained in DB)
   [ExerciseAttempt]     [QuizAttempt]     [FlashcardProgress]     [StudentMistake]
   [AdaptiveState]       [StreakFreeze]    [EngagementScore]       [NotificationPreference]
```

### ویژگی‌های کلیدی جداول
- **ایدمپوتنت بودن امتیازات:** جدول `XPLog` ستون `reason` با طول ۱۰۰ کاراکتر دارد. منطق سرویس قبل از صدور کوئری `INSERT`، از عدم وجود همان `reason` برای کاربر اطمینان حاصل می‌کند.
- **سقف ۵ تلاش کوییز:** جدول `QuizAttempt` دارای محدودیت یکتایی مرکب `(user_id, week, attempt_number)` است و سرویس از ورود تلاش ششم جلوگیری می‌کند.
- **جعبه لایتنر در دیتابیس:** جدول `FlashcardProgress` با فیلدهای `box_number` (۱ تا ۵)، `ease_factor` و `next_review` مستقیماً الگوریتم SuperMemo-2 را پیاده‌سازی می‌کند.
- **مخزن اشتباهات (`StudentMistake`):** هر خطای تمرین یا کوئیز، بر اساس `(user_id, item_id)` ذخیره و تا زمان حل مجدد توسط دانش‌آموز در حالت `is_resolved=False` باقی می‌ماند.

---

## ۴. موتور پایگاه دانش و خط رندر محتوا (Knowledge Base Pipeline)

محتوای آموزشی پایگاه دانش برخلاف سیستم‌های قدیمی در دیتابیس متنی سنگین ذخیره نمی‌شود، بلکه مبتنی بر **درخت محتوای فایل‌سیستم (File-based Hierarchy)** عمل می‌کند:

```text
[فایل Markdown با متادیتا] 
         │
         v
[kb_repo.py] ──> خواندن فایل دیسک با انکودینگ UTF-8 و کشینگ ساختار
         │
         v
[md_render.py] ──> پارس Markdown با افزونه‌های Pygments (رنگ‌آمیزی کدها)، 
                   تولید فهرست مطالب خودکار (TOC)، جدول‌ها و فیلتر XSS
         │
         v
[kb_content.py] ──> افزودن متادیتای ناوبری (درس بعدی/قبلی، زمان تخمینی مطالعه)
         │
         v
[Jinja2 + doc.html] ──> رندر نهایی با سرفصل‌های کشویی و نوار پیشرفت مطالعه
```

---

## ۵. مشخصات موتور یادگیری تطبیقی (Adaptive Engine Specs)

سرویس `adaptive.py` (۶۰۳ خط) مجهز به الگوریتم **Bayesian Knowledge Tracing (BKT)** است:

### معادلات به‌روزرسانی بیزین:
در صورت پاسخ صحیح:
$$P(L_t | \text{Correct}) = \frac{P(L_{t-1}) \cdot (1 - P(S))}{P(L_{t-1}) \cdot (1 - P(S)) + (1 - P(L_{t-1})) \cdot P(G)}$$

در صورت پاسخ غلط:
$$P(L_t | \text{Incorrect}) = \frac{P(L_{t-1}) \cdot P(S)}{P(L_{t-1}) \cdot P(S) + (1 - P(L_{t-1})) \cdot (1 - P(G))}$$

انتقال یادگیری پسین:
$$P(L_t) = P(L_t | \text{Obs}) + (1 - P(L_t | \text{Obs})) \cdot P(T)$$

- **ساخت جلسه تمرین ۵ دقیقه‌ای:**
  - ۸ تا ۱۰ سوال در ۳۰۰ ثانیه.
  - ۶۰٪ سوالات از مفاهیم با $P(L) < 0.85$ (مفاهیم ضعیف).
  - ۲۵٪ سوالات مرور سررسید جعبه‌های لایتنر (فاصله‌های ۱، ۲، ۴، ۷ و ۱۴ روز).
  - ۱۵٪ سوالات مفاهیم جدید تا زمان پوشش کامل سرفصل‌های هفته.

---

## ۶. عملکرد، مقیاس‌پذیری و استقرار روی سرور (Production Deployment)

### تنظیمات SQLite برای همزمانی بالا
به دلیل استفاده از تنظیمات خاص زیر در رویداد اتصال موتور SQLAlchemy:
- حالت **WAL (Write-Ahead Logging):** خوانندگان (Readers) مانع نویسندگان (Writers) نمی‌شوند و بالعکس.
- کش **۱۶ مگابایتی RAM:** کاهش ۹۵ درصدی دسترسی دیسک I/O برای خواندن درسنامه‌ها و سوابق استریک.
- تایم‌اوت ۵ ثانیه‌ای: رفع قطعی خطاهای `database is locked` در ترافیک‌های لحظه‌ای آزمون‌ها.

### پیکربندی Gunicorn و حافظه مصرفی
- تعداد ورکر: `2 x CPU cores + 1` (در سرور ۲ هسته‌ای: ۳ ورکر).
- نوع ورکر: `gthread` با ۲ ترد به‌ازای هر ورکر.
- مصرف رم کل: زیر ۲۵۰ مگابایت (بسیار سبک و اقتصادی برای هاست‌های ایرانی).
- پاسخ‌دهی لندینگ و ریدر: میانگین **کمتر از ۲۵ میلی‌ثانیه**.
