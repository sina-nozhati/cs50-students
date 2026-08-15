# Anzali Implementation — کد اجرایی پلتفرم CS50x

این فایل پیاده‌سازی ملموس پلتفرم Anzali-CS50-Hub است: ساختار پوشه، `create_app`،
مدل‌های کامل، نمونه blueprint‌ها، endpoint آپلود ادمین، و کانفیگ کامل دیپلوی.
**قبل از نوشتن یا تغییر کد Flask این فایل را بخوان.**

مسیر واقعی کد در workspace: `flask-app/`

---

## ۱. ساختار پوشه‌ی هدف

```
flask-app/
├── app/
│   ├── __init__.py          # create_app() factory
│   ├── models.py            # User, Assignment, Submission, XPLog, Resource
│   ├── config.py            # Config / TestingConfig از env
│   ├── routes/
│   │   ├── __init__.py      # ثبت همه‌ی blueprint‌ها
│   │   ├── main.py          # / و /health
│   │   ├── kb.py            # /kb/week/<n>
│   │   ├── assignments.py   # /assignments + /submit
│   │   ├── gamification.py  # /leaderboard
│   │   ├── auth.py          # /login + /logout
│   │   ├── resources.py     # /resources + /resources/week/<n>
│   │   └── admin.py         # /admin + /admin/upload
│   └── services/
│       ├── __init__.py
│       ├── xp.py            # award(), get_total()
│       ├── submissions.py   # create_submission(), grade()
│       └── resources.py     # list_for_week(), create_resource()
├── templates/
│   ├── base.html
│   ├── _partials/           # macro‌های مشترک (کارت، badge)
│   ├── kb/
│   ├── assignments/
│   ├── auth/
│   ├── resources/
│   └── admin/
├── static/
│   └── downloads/
│       ├── week0/  week1/  ...  week8/   # PDF و src.zip اینجا
├── instance/
│   └── cs50.db              # (gitignored)
├── tests/
├── requirements.txt
├── requirements-dev.txt
├── init_db.py               # ساخت جداول + seed
└── run.py                   # نقطه‌ی ورود dev
```

---

## ۲. نقاط ورود

### `run.py`
```python
"""نقطه‌ی ورود برای توسعه. در production از Gunicorn استفاده می‌شود."""
from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True فقط برای dev؛ هرگز در production
    app.run(host="127.0.0.1", port=5000, debug=True)
```

### `app/__init__.py` — Application Factory
```python
"""Application Factory پلتفرم Anzali-CS50-Hub.

این الگو به ما اجازه می‌دهد instance‌های مختلف بسازیم (dev, test, production)
با کانفیگ متفاوت — بدون متغیر سراسری app.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_object="app.config.Config"):
    """ساخت و پیکربندی یک instance از اپلیکیشن."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    # اطمینان از وجود پوشه‌ی instance برای SQLite
    import os
    os.makedirs(app.instance_path, exist_ok=True)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)

    # ثبت blueprint‌ها
    from app.routes import main, kb, assignments, gamification, auth, resources, admin
    app.register_blueprint(main.bp)
    app.register_blueprint(kb.bp)
    app.register_blueprint(assignments.bp)
    app.register_blueprint(gamification.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(resources.bp)
    app.register_blueprint(admin.bp)

    # ساخت جداول در اولین درخواست (فقط برای SQLite dev؛ در prod از init_db.py استفاده کن)
    with app.app_context():
        from app import models  # noqa: ثبت مدل‌ها
        db.create_all()

    # logging سبک به stdout (systemd journal آن را می‌گیرد)
    logging.basicConfig(level=app.config["LOG_LEVEL"],
                        format="%(asctime)s %(levelname)s %(name)s %(message)s")

    return app
```

### `app/config.py`
```python
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """کانفیگ اصلی — از environment variableها می‌خواند."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    # SQLite در instance folder (gitignored)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "..", "instance", "cs50.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    # مسیر ذخیره‌ی فایل‌های آپلودشده
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "static", "downloads")
    MAX_CONTENT_LENGTH = 30 * 1024 * 1024  # 30MB حد بالا
    ALLOWED_EXTENSIONS = {"pdf", "zip"}
    # نقش ادمین: در فاز ۱ یک رمز ثابت کلاس
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "cs50-anzali-admin")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
```

---

## ۳. مدل‌های دیتابیس (کامل)

`app/models.py`:
```python
"""تمام مدل‌های SQLAlchemy پلتفرم در یک فایل برای سادگی آموزش."""
from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    telegram_id = db.Column(db.String(50), unique=True, nullable=True)
    xp = db.Column(db.Integer, default=0, index=True)        # index برای leaderboard
    streak = db.Column(db.Integer, default=0)
    is_admin = db.Column(db.Boolean, default=False)
    submissions = db.relationship("Submission", backref="student", lazy=True)
    xp_logs = db.relationship("XPLog", backref="user", lazy=True)


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    week = db.Column(db.Integer, nullable=False, index=True)
    due_date = db.Column(db.DateTime, nullable=False)
    github_template_url = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    submissions = db.relationship("Submission", backref="assignment", lazy=True)


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    assignment_id = db.Column(db.Integer, db.ForeignKey("assignment.id", ondelete="CASCADE"), nullable=False)
    github_url = db.Column(db.String(255), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Integer, nullable=True)      # 0..100
    feedback = db.Column(db.Text, nullable=True)


class XPLog(db.Model):
    """Audit trail برای تمام XP‌ها — هرگز پاک نمی‌شود."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class Resource(db.Model):
    """یک فایل قابل‌دانلود برای یک هفته (PDF یا src.zip)."""
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False, index=True)
    filename = db.Column(db.String(150), nullable=False)       # slides.pdf
    display_name = db.Column(db.String(200), nullable=False)   # «اسلایدها»
    category = db.Column(db.String(20), nullable=False)        # slides|notes|pset|src|extra
    is_published = db.Column(db.Boolean, default=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    uploaded_by = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
    __table_args__ = (db.UniqueConstraint("week", "filename", name="uq_week_filename"),)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
```

---

## ۴. نمونه Blueprint‌ها

### `app/routes/kb.py` — ماژول پایگاه دانش
```python
"""ماژول پایگاه دانش (Knowledge Base). صفحات هر هفته + دکمه‌ی «من خواندم»."""
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from app.services import xp as xp_service

bp = Blueprint("kb", __name__, url_prefix="/kb")

# نقشه‌ی فارسی هفته‌ها برای نمایش
WEEK_TITLES = {
    0: "هفته ۰ — Scratch",
    1: "هفته ۱ — C (پایه)",
    2: "هفته ۲ — آرایه‌ها",
    3: "هفته ۳ — الگوریتم‌ها",
    4: "هفته ۴ — حافظه",
    5: "هفته ۵ — ساختمان داده",
    6: "هفته ۶ — پایتون",
    7: "هفته ۷ — SQL",
    8: "هفته ۸ — HTML/CSS/JS",
}


@bp.route("/week/<int:week>")
def week_page(week):
    if week not in WEEK_TITLES:
        abort(404)
    return render_template("kb/week.html", week=week, title=WEEK_TITLES[week])


@bp.route("/week/<int:week>/read", methods=["POST"])
@login_required
def mark_read(week):
    """دکمه‌ی «من خواندم» — ۵ XP می‌دهد، fragment HTML برمی‌گرداند (HTMX)."""
    xp_service.award(current_user.id, amount=5, reason=f"Read KB Week {week}")
    return render_template("kb/_read_button.html", awarded=True, week=week)
```

### `app/routes/resources.py` — ماژول دانلودها (۹ کارت)
```python
"""ماژول منابع: ۹ کارت هفته + لیست فایل‌های هر هفته برای دانلود."""
from flask import Blueprint, render_template, abort, current_app, send_from_directory
from app.models import Resource
from app.services import resources as res_service

bp = Blueprint("resources", __name__, url_prefix="/resources")

WEEK_TITLES = {
    0: "Scratch", 1: "C (پایه)", 2: "آرایه‌ها", 3: "الگوریتم‌ها",
    4: "حافظه", 5: "ساختمان داده", 6: "پایتون", 7: "SQL", 8: "HTML/CSS/JS",
}


@bp.route("/")
def index():
    """صفحه‌ی ۹ کارت — تعداد فایل هر هفته را از DB می‌خواند."""
    weeks = []
    for w in range(9):
        count = res_service.count_for_week(w)
        weeks.append({"week": w, "title": WEEK_TITLES[w], "file_count": count})
    return render_template("resources/index.html", weeks=weeks)


@bp.route("/week/<int:week>")
def week_files(week):
    """لیست فایل‌های یک هفته با لینک دانلود."""
    if week not in WEEK_TITLES:
        abort(404)
    files = res_service.list_for_week(week)
    return render_template("resources/week.html", week=week, title=WEEK_TITLES[week], files=files)


@bp.route("/file/<int:resource_id>/download")
def download(resource_id):
    """دانلود مستقیم فایل از static/downloads/weekN/."""
    res = res_service.get(resource_id) or abort(404)
    directory = current_app.config["UPLOAD_FOLDER"] + f"/week{res.week}"
    return send_from_directory(directory, res.filename, as_attachment=True,
                               download_name=res.display_name + "." + res.filename.rsplit(".", 1)[-1])
```

### `app/routes/admin.py` — پنل ادمین + آپلود
```python
"""پنل ادمین: آپلود فایل برای دانش‌آموزان، مدیریت منابع."""
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from app.models import db, Resource
from app.services import resources as res_service

bp = Blueprint("admin", __name__, url_prefix="/admin")


# Decorator نقش ادمین (تعریف در functools)
from functools import wraps
def admin_required(f):
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash("دسترسی ادمین لازم است.", "error")
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)
    return decorated


def allowed_file(filename):
    """allowlist extension — امنیت در برابر آپلود فایل مخرب."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]


@bp.route("/")
@admin_required
def index():
    return render_template("admin/index.html")


@bp.route("/upload", methods=["GET", "POST"])
@admin_required
def upload():
    """فرم آپلود فایل برای یک هفته مشخص."""
    if request.method == "POST":
        week = request.form.get("week", type=int)
        category = request.form.get("category", "extra")
        display_name = request.form.get("display_name", "").strip() or "فایل بدون نام"
        file = request.files.get("file")

        if file is None or file.filename == "":
            flash("فایلی انتخاب نشده.", "error")
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash("پسوند مجاز نیست (فقط pdf یا zip).", "error")
            return redirect(request.url)
        if week not in range(9):
            flash("هفته نامعتبر.", "error")
            return redirect(request.url)

        # secure_filename از path traversal جلوگیری می‌کند
        safe_name = secure_filename(file.filename) or "upload.bin"
        target_dir = os.path.join(current_app.config["UPLOAD_FOLDER"], f"week{week}")
        os.makedirs(target_dir, exist_ok=True)
        file.save(os.path.join(target_dir, safe_name))

        # درج در DB
        res = res_service.create_resource(
            week=week, filename=safe_name, display_name=display_name,
            category=category, uploaded_by=current_user.id,
        )
        flash(f"فایل «{display_name}» برای هفته {week} آپلود شد.", "success")
        return redirect(url_for("admin.resources_list"))

    return render_template("admin/upload.html", weeks=list(range(9)))


@bp.route("/resources")
@admin_required
def resources_list():
    """لیست همه‌ی منابع با دکمه‌ی حذف/انتشار."""
    all_resources = Resource.query.order_by(Resource.week, Resource.category).all()
    return render_template("admin/resources.html", resources=all_resources)


@bp.route("/resources/<int:rid>/toggle", methods=["POST"])
@admin_required
def toggle_publish(rid):
    res = db.get_or_404(Resource, rid)
    res.is_published = not res.is_published
    db.session.commit()
    flash("وضعیت انتشار تغییر کرد.", "success")
    return redirect(url_for("admin.resources_list"))
```

---

## ۵. Services (منطق تجاری خالص)

### `app/services/xp.py`
```python
"""منطق گیمیفیکیشن XP — تابع خالص، قابل تست بدون Flask context."""
from app import db
from app.models import User, XPLog


def award(user_id, amount, reason):
    """یک مقدار XP به کاربر می‌دهد و در XPLog ثبت می‌کند (audit trail)."""
    user = db.session.get(User, user_id)
    if user is None:
        return
    user.xp = (user.xp or 0) + amount
    log = XPLog(user_id=user_id, amount=amount, reason=reason)
    db.session.add(log)
    db.session.commit()


def leaderboard(limit=10):
    """۱۰ نفر برتر کلاس — یک کوئری، بدون N+1."""
    return User.query.order_by(User.xp.desc()).limit(limit).all()
```

### `app/services/resources.py`
```python
"""منطق منابع (دانلودها) — لیست، شمارش، ایجاد."""
from app import db
from app.models import Resource


def list_for_week(week):
    """فایل‌های منتشرشده‌ی یک هفته، مرتب بر اساس دسته."""
    return (Resource.query
            .filter_by(week=week, is_published=True)
            .order_by(Resource.category, Resource.id)
            .all())


def count_for_week(week):
    """تعداد فایل‌های منتشرشده‌ی یک هفته — برای badge کارت."""
    return Resource.query.filter_by(week=week, is_published=True).count()


def get(resource_id):
    return db.session.get(Resource, resource_id)


def create_resource(week, filename, display_name, category, uploaded_by):
    res = Resource(week=week, filename=filename, display_name=display_name,
                   category=category, uploaded_by=uploaded_by, is_published=True)
    db.session.add(res)
    db.session.commit()
    return res
```

---

## ۶. init_db.py — Seed کردن داده‌ها

```python
"""ساخت جداول + seed: یک ادمین پیش‌فرض و همه‌ی Resource‌های کپی‌شده.

اجرا: python init_db.py
این اسکریپت فقط جداول خالی را پر می‌کند؛ اگر قبلاً پر شده‌اند، رد می‌شود.
"""
from app import create_app, db
from app.models import User, Resource
from werkzeug.security import generate_password_hash

# این لیست باید با فایل‌های واقعی کپی‌شده در static/downloads/weekN/ هم‌خوان باشد.
# بعد از کپی فایل‌ها (طبق PROJECT_PLAN.md بخش ۳-۱) اینجا را به‌روز کن یا از نسخه‌ی
# تولیدشده‌ی اسکریپت کپی استفاده کن.
SEED_RESOURCES = [
    # (week, filename, display_name, category)
    (0, "slides.pdf", "اسلایدها", "slides"),
    (0, "notes.pdf", "جزوه", "notes"),
    (0, "exercise.pdf", "تمرین Scratch", "pset"),
    (0, "first-submit.pdf", "راهنمای اولین ثبت", "extra"),
    (0, "src.zip", "سورس کد", "src"),
    # ... سایر هفته‌ها (طبق جدول نگاشت در PROJECT_PLAN.md)
]


def main():
    app = create_app()
    with app.app_context():
        db.create_all()

        # ادمین پیش‌فرض (رمز از env یا پیش‌فرض)
        from app.config import Config
        if not User.query.filter_by(username="admin").first():
            admin = User(username="admin",
                         password_hash=generate_password_hash(Config.ADMIN_PASSWORD),
                         is_admin=True)
            db.session.add(admin)
            print("✅ ادمین پیش‌فرض ساخته شد (username=admin).")

        # seed منابع
        for week, fn, name, cat in SEED_RESOURCES:
            exists = Resource.query.filter_by(week=week, filename=fn).first()
            if not exists:
                db.session.add(Resource(week=week, filename=fn, display_name=name, category=cat))

        db.session.commit()
        print("✅ منابع seed شدند.")


if __name__ == "__main__":
    main()
```

---

## ۷. deployment — Nginx + Gunicorn + systemd

### `/etc/systemd/system/cs50hub.service`
```ini
[Unit]
Description=Gunicorn instance to serve CS50 Anzali Hub
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/cs50app/flask-app
Environment="PATH=/home/cs50app/flask-app/venv/bin"
EnvironmentFile=/home/cs50app/flask-app/.env
ExecStart=/home/cs50app/flask-app/venv/bin/gunicorn \
    --workers 2 --bind 127.0.0.1:5000 "run:app"
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### `/etc/nginx/sites-available/cs50hub`
```nginx
server {
    listen 80;
    server_name your-domain.ir;   # یا IP سرور

    # فایل‌های استاتیک (CSS/JS و دانلودهای PDF) مستقیم سرو شوند، با کش ۳۰ روزه
    location /static/ {
        alias /home/cs50app/flask-app/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # proxy به Gunicorn
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # محدودیت size آپلود
    client_max_body_size 35M;
}
```

### دستورات راه‌اندازی روی VPS
```bash
sudo ln -s /etc/nginx/sites-available/cs50hub /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx
sudo systemctl enable --now cs50hub

# بک‌آپ روزانه SQLite (cron) — از .backup استفاده کن نه cp
echo "0 3 * * * sqlite3 /home/cs50app/flask-app/instance/cs50.db \".backup /backup/cs50-\$(date +\%F).db\"" | sudo tee /etc/cron.d/cs50-backup
```

---

## ۸. خلاصه‌ی workflow هنگام افزودن feature

1. مدل لازم است؟ → `models.py` + `init_db.py` را آپدیت کن.
2. service لازم است؟ → `app/services/<name>.py` بساز (خالص، قابل تست).
3. route لازم است؟ → `app/routes/<name>.py` + ثبت در `routes/__init__.py`.
4. UI لازم است؟ → `templates/<name>/` با `extends "base.html"`.
5. تعاملی؟ → HTMX: route یک fragment برمی‌گرداند.
6. آپلود/admin؟ → `secure_filename` + `admin_required` + allowlist.
7. تست → `tests/` با fixture in-memory.
8. دیپلوی → `git pull && systemctl restart cs50hub`.

برای هر سؤال درباره‌ی یک لایه‌ی خاص، `layer-blueprints.md` را ببین.
