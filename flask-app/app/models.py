"""تمام مدلهای SQLAlchemy پلتفرم در یک فایل برای سادگی آموزش.

این فایل همان چیزی است که در جلسه فلکس بهعنوان نمونه نشان می‌دهیم؛
پس کامنتها واضح و نام‌ها خوانا هستند.

مدلها:
    User         — دانشآموز یا ادمین
    Assignment   — یک تمرین/پروژه (مثل "Project 0: Scratch")
    Submission   — تحویل یک دانش‌آموز برای یک تکلیف
    XPLog        — سابقه‌ی تمام XPها (audit trail — هرگز پاک نمی‌شود)
    Resource     — یک فایل قابل‌دانلود برای یک هفته (PDF یا src.zip)
    WeekProgress — پیشرفت یک کاربر در یک هفته (کوییز/درس/فلش‌کارت)
    Week         — یک هفته‌ی دوره (عنوان/انتشار/محتوای آموزشی)
"""
from datetime import datetime

from flask_login import UserMixin

from app import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    telegram_id = db.Column(db.String(50), unique=True, nullable=True)
    xp = db.Column(db.Integer, default=0, index=True)        # index برای کوئری leaderboard
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
    description = db.Column(db.Text, nullable=True)           # توضیحات تکلیف (ادمین)
    xp_reward = db.Column(db.Integer, default=20)             # XP قابل‌تنظیم توسط ادمین
    is_active = db.Column(db.Boolean, default=True)
    submissions = db.relationship("Submission", backref="assignment", lazy=True)


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    assignment_id = db.Column(
        db.Integer, db.ForeignKey("assignment.id", ondelete="CASCADE"), nullable=False
    )
    github_url = db.Column(db.String(255), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Integer, nullable=True)      # نمره از 0 تا 100
    feedback = db.Column(db.Text, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("student_id", "assignment_id", name="uq_student_assignment"),
    )


class XPLog(db.Model):
    """سابقه‌ی تمام XPها. این جدول هرگز پاک نمی‌شود تا audit trail داشته باشیم."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    amount = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class Resource(db.Model):
    """یک فایل قابل‌دانلود برای یک هفته (PDF یا src.zip).

    فایل فیزیکی در static/downloads/weekN/<filename> قرار دارد.
    برای دانلود صحیح، filename بهصورت انگلیسی امن (secure) و
    display_name فارسی برای نمایش در UI استفاده می‌شود.
    """
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False, index=True)
    filename = db.Column(db.String(150), nullable=False)       # مثلاً slides.pdf
    display_name = db.Column(db.String(200), nullable=False)   # مثلاً «اسلایدها»
    category = db.Column(db.String(20), nullable=False)        # slides|notes|pset|src|extra
    is_published = db.Column(db.Boolean, default=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    uploaded_by = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True
    )

    __table_args__ = (
        # جلوگیری از دو فایل هم‌نام در یک هفته
        db.UniqueConstraint("week", "filename", name="uq_week_filename"),
    )


class WeekProgress(db.Model):
    """پیشرفت یک دانشآموز در یک هفته‌ی خاص.

    یک ردیف به‌ازای (کاربر، هفته) — UniqueConstraint این را تضمین میکند.
    این مدل پاسخ‌گوی داشبورد و مسیر مدرک است: یک هفته «تکمیل‌شده» محسوب
    میشود وقتی quiz_completed=True باشد.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    week = db.Column(db.Integer, nullable=False, index=True)
    quiz_score = db.Column(db.Integer, default=0)        # بهترین نمره‌ی کوییز (۰..total)
    quiz_total = db.Column(db.Integer, default=5)        # تعداد سؤال‌های کوییز این هفته
    quiz_completed = db.Column(db.Boolean, default=False)
    kb_read = db.Column(db.Boolean, default=False)       # تقلب‌نامه را خوانده؟
    flashcards_reviewed = db.Column(db.Boolean, default=False)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        # یک ردیف به‌ازای (کاربر، هفته) — جلوگیری از چندتایی
        db.UniqueConstraint("user_id", "week", name="uq_user_week"),
    )


class Week(db.Model):
    """یک هفته‌ی دوره — عنوان، وضعیت انتشار، و محتوای آموزشی.

    هر هفته با `number` (0..8) شناسایی میشود. ادمین میتواند:
      - عنوان فارسی هفته را ویرایش کند.
      - هفته را منتشر/مخفی کند (دانش‌آموز فقط هفته‌های منتشرشده را می‌بیند).
      - محتوای HTML هفته را آپلود یا ویرایش کند (در kb/week.html رندر میشود).

    نکته آموزشی: انتشار یک کنترل دسترسی واقعی است، نه فقط نمایشی.
    روت kb.mark_read قبل از دادن XP چک میکند که هفته منتشر باشد.
    """
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    is_published = db.Column(db.Boolean, default=False, nullable=False)
    content_html = db.Column(db.Text, nullable=True)
    content_url = db.Column(db.String(500), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id: str):
    """Flask-Login با این تابع کاربر را از session بارگذاری می‌کند."""
    return db.session.get(User, int(user_id))
