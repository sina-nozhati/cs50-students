# Layer Blueprints — جزئیات ۱۰ لایه‌ی fullstack

این فایل، هر لایه‌ی SKILL.md را با checklist، anti-pattern و مثال ملموس در بستر
Anzali-CS50-Hub بسط می‌دهد. هنگام تصمیم‌گیری درباره‌ی یک لایه‌ی خاص آن را بخوان.

---

## L1 — Scope & Requirements

**هدف:** قبل از کدنویسی، بدانیم چه می‌سازیم و چه نمی‌سازیم.

**Checklist:**
- [ ] اولویت feature در ماتریس KB > Assignment > Gamification > Resources مشخص است.
- [ ] MVP scope تعریف شده (چه چیزی برای جلسه‌ی Flask کافی است؟).
- [ ] وابستگی به feature‌های بعدی مشخص است (مثلاً Gamification به Auth وابسته است).

**Anti-patterns:**
- ساخت «مدارس دیگر» یا «پلن اشتراک» قبل از اینکه کلاس انزلی کار کند. (هنوز زود است.)
- اضافه‌کردن feature بدون تأیید اولویت با کاربر.

**مثال CS50:** کاربر می‌گوید «لیگ و چالش زمان‌دار اضافه کن». پاسخ: این خارج از MVP فاز ۱
است — طبق L1، فعلاً فقط XP + streak + leaderboard کلاسی ساده کافی است. در Backlog بگذار.

---

## L2 — Architecture & Patterns

**هدف:** Clean Monolith سازمان‌یافته با تفکیک لایه‌ها.

**Checklist:**
- [ ] همه‌چیز زیر `create_app()` factory است (نه `app = Flask(__name__)` سراسری).
- [ ] هر ماژول یک Blueprint جداگانه دارد.
- [ ] منطق تجاری در `app/services/` است، نه در route.
- [ ] مدل‌ها در `models.py` متمرکز هستند.
- [ ] config از environment variable خوانده می‌شود (`Config` class).

**Anti-patterns:**
- منطق XP در داخل route نوشتن. (در `services/gamification.py` باشد.)
- God blueprint که همه‌چیز را انجام می‌دهد.
- import دایره‌ای بین models و routes.

**ساختار صحیح:**
```
flask-app/
├── app/
│   ├── __init__.py          # create_app() factory
│   ├── models.py            # همه‌ی SQLAlchemy models
│   ├── config.py            # Config از env
│   ├── routes/              # هر ماژول یک فایل
│   │   ├── kb.py
│   │   ├── assignments.py
│   │   ├── gamification.py
│   │   ├── auth.py
│   │   ├── resources.py
│   │   └── admin.py
│   └── services/            # منطق تجاری خالص (قابل تست)
│       ├── xp.py
│       ├── submissions.py
│       └── resources.py
├── templates/
├── static/
├── instance/                # cs50.db اینجا (gitignored)
├── requirements.txt
└── run.py                   # نقطه‌ی ورود برای dev
```

---

## L3 — Database & ORM

**هدف:** اسکیمای تمیز، قابل‌مهاجرت به PostgreSQL، بدون N+1.

**Checklist:**
- [ ] هر کلید خارجی `ForeignKey` با `ondelete='CASCADE'` یا `'SET NULL'` مشخص شده.
- [ ] relationship‌ها `lazy` mode آگاهانه انتخاب شده (پیش‌فرض `select`، برای صفحات لیست `joined`).
- [ ] index روی فیلدهای فیلتر/مرتب‌شونده (مثل `User.xp` برای leaderboard).
- [ ] timestamp‌ها با `default=datetime.utcnow` (UTC، نه local).
- [ ] enum‌ها به‌صورت `db.Enum` یا string با validation.
- [ ] برای migration از Flask-Migrate (Alembic) استفاده می‌شود بعد از فاز اول.

**Anti-patterns:**
- ذخیره‌ی JSON بزرگ در یک ستون به‌جای جدول جدا (مگه واقعاً غیرساختاریافته باشد).
- N+1 query در حلقه‌ی Jinja (به‌جای آن `joinedload` یا کوئری bulk).
- `datetime.now()` به‌جای `datetime.utcnow()` (با GMT مشکل می‌سازد).

**مدل Resource (نمونه):**
```python
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False, index=True)  # 0..8
    filename = db.Column(db.String(150), nullable=False)       # slides.pdf
    display_name = db.Column(db.String(200), nullable=False)   # «اسلایدها»
    category = db.Column(db.String(20), nullable=False)        # slides|notes|pset|src|extra
    is_published = db.Column(db.Boolean, default=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'), nullable=True)
    __table_args__ = (db.UniqueConstraint('week', 'filename', name='uq_week_filename'),)
```

---

## L4 — Backend

**هدف:** route‌های نازک، منطق در services، تعامل با HTMX.

**Checklist:**
- [ ] route فقط ورودی را validate می‌کند، service را صدا می‌زند، پاسخ را برمی‌گرداند.
- [ ] endpoint‌های HTMX fragment HTML برمی‌گردانند (نه redirect، نه JSON کامل).
- [ ] POSTها از CSRF محافظت می‌شوند (Flask-WTF یا token ساده).
- [ ] خطاها با `abort(404)` یا flash + re-render هندل می‌شوند.

**Anti-patterns:**
- منطق نمره‌دهی یا محاسبه‌ی streak داخل route.
- بازگرداندن JSON برای چیزی که قرار است HTMX آن را render کند.
- تکرار کوئری در چند route (به‌جای آن، در service مشترک بگذار).

**نمونه endpoint HTMX (+5 XP با دکمه‌ی «من خواندم»):**
```python
@bp.route("/kb/week/<int:week>/read", methods=["POST"])
def mark_read(week):
    if not current_user.is_authenticated:
        abort(401)
    xp_service.award(current_user.id, amount=5, reason=f"Read KB Week {week}")
    # برمی‌گرداند، نه redirect fragment یک
    return render_template("kb/_read_button.html", awarded=True, week=week)
```

---

## L5 — Frontend

**هدف:** Jinja + HTMX + Tailwind (CDN)، mobile-first، بدون build.

**Checklist:**
- [ ] Tailwind از CDN (`https://cdn.tailwindcss.com`) در `base.html`.
- [ ] کامپوننت‌های تکراری به Jinja macro تبدیل شده‌اند (`templates/_partials/`).
- [ ] تمام صفحات `extends "base.html"` می‌کنند.
- [ ] HTMX attribute‌ها (`hx-post`, `hx-target`, `hx-swap`) برای تعامل بدون JS سفارشی.
- [ ] طراحی روی موبایل (عرض ۳۷۵px) تست شده.

**Anti-patterns:**
- نوشتن JavaScript سفارشی برای چیزی که HTMX انجام می‌دهد.
- package.json و build step (Vue/React). پروژه Node نداریم.
- CSS سفارشی بزرگ به‌جای کلاس‌های Tailwind.

**نمونه base.html (Tailwind CDN):**
```html
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/htmx.org@1.9.12"></script>
```

---

## L6 — Auth & Security

**هدف:** احراز هویت ساده اما امن، آپلود ایمن، حفاظت از داده‌ی دانش‌آموز.

**Checklist:**
- [ ] پسوردها با `werkzeug.security.generate_password_hash` هش می‌شوند (هرگز plaintext).
- [ ] نقش `is_admin` روی User؛ route‌های `/admin/*` با decorator `admin_required` محافظت می‌شوند.
- [ ] `SECRET_KEY` از env (`os.environ`)، هرگز هاردکد.
- [ ] آپلود: `secure_filename` + allowlist extension (`{.pdf, .zip}`) + محدودیت size.
- [ ] فرم‌ها CSRF token دارند.
- [ ] خطاهای 404/500 صفحه‌ی اختصاصی دارند (نه stack trace).

**Anti-patterns:**
- رمز ثابت کلاس به‌عنوان تنها لایه‌ی امنیتی برای همیشه (فقط برای فاز ۱ قابل‌قبول).
-信任 filename کلاینت بدون `secure_filename` (path traversal!).
- ذخیره‌ی فایل آپلودشده خارج از `static/` بدون validation.

**Decorator admin_required:**
```python
from functools import wraps
from flask import abort
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not (current_user.is_authenticated and current_user.is_admin):
            abort(403)
        return f(*args, **kwargs)
    return decorated
```

---

## L7 — Testing & Quality

**هدف:** پوشش منطق تجاری، نه خط به خط.

**Checklist:**
- [ ] pytest + pytest-flask نصب در dev dependencies.
- [ ] fixture برای DB in-memory SQLite (`:memory:`).
- [ ] service‌ها به‌صورت تابع خالص تست می‌شوند (بدون نیاز به Flask context).
- [ ] smoke test برای route‌های اصلی (GET /, /kb/week/0, /resources).
- [ ] تست آپلود با `io.BytesIO` fake file.

**Anti-patterns:**
- تست فقط با success path (بدون edge case مثل فایل مخرب).
- mock کردن بیش‌ازحد (به‌جای آن از SQLite واقعی in-memory استفاده کن).

**نمونه fixture:**
```python
@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
```

---

## L8 — DevOps & CI

**هدف:** نصب و اجرای تکرارپذیر.

**Checklist:**
- [ ] `requirements.txt` دقیق (با pinned version‌های اصلی).
- [ ] `requirements-dev.txt` برای pytest و ابزار توسعه.
- [ ] `init_db.py` برای ساخت جداول + seed کردن Resource‌ها و یک ادمین پیش‌فرض.
- [ ] `.env.example` تمام متغیرها را نشان می‌دهد.
- [ ] (اختیاری) GitHub Actions: install + pytest روی هر push.

**Anti-patterns:**
- وابستگی به پکیج‌های نصب‌شده‌ی سراسری روی VPS (همیشه venv).
- هاردکد کردن مسیرها در کد (از `app.root_path` استفاده کن).

---

## L9 — Deployment & Scaling

**هدف:** اجرای پایدار روی VPS ۱ گیگ ایرانی.

**Checklist:**
- [ ] Gunicorn با 2 workers، bind به 127.0.0.1:5000.
- [ ] Nginx reverse proxy + سرو static با `expires 30d`.
- [ ] systemd service با `Restart=on-failure`.
- [ ] SQLite در `instance/` با permission درست (`www-data` مالک).
- [ ] firewall: فقط 80/443 باز (۵۰۰۰ فقط localhost).

**Anti-patterns:**
- اجرای `flask run` در production (همیشه Gunicorn).
- قرار دادن SQLite روی NFS یا shared folder (فایل corruption).
- workers زیاد روی ۱ هسته (CPU-saturation).

**کانفیگ کامل Nginx + systemd** در `anzali-implementation.md` بخش Deployment.

---

## L10 — Observability & Maintenance

**هدف:** بدانیم چه می‌گذرد و بتوانیم بازیابی کنیم.

**Checklist:**
- [ ] logging به stdout (systemd journal آن را جمع می‌کند).
- [ ] endpoint `/health` که `{"status":"ok"}` برمی‌گرداند + سن DB.
- [ ] بک‌آپ روزانه SQLite با cron: `sqlite3 cs50.db ".backup /backup/cs50-$(date +%F).db"`.
- [ ] XPLog به‌عنوان audit trail نگه‌داری می‌شود (هرگز پاک نمی‌شود).
- [ ] log rotation فعال (logrotate یا systemd journal خودش).

**Anti-patterns:**
- کپی خام فایل SQLite هنگام نوشتن (WAL inconsistency) — از `.backup` استفاده کن.
- لاگ شامل داده‌ی حساس (مثل رمز) — هرگز.

---

## جمع‌بندی

این لایه‌ها مستقل از ابزارند: اگر فردا به Postgres یا React مهاجرت کردید، همین
چارچوب (با جزئیات متفاوت) همچنان برقرار است. اما تا زمانی که MVP کار نکرده،
**به تغییرات معماری بزرگ فکر نکن** — سادگی و سرعت برای کلاس انزلی اولویت دارد.
