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
    Notification — اعلان داخل‌پنل برای دانش‌آموز
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
    is_active = db.Column(db.Boolean, default=True, nullable=False)  # غیرفعال‌سازی بدون حذف
    submissions = db.relationship("Submission", backref="student", lazy=True, cascade="all, delete-orphan")
    xp_logs = db.relationship("XPLog", backref="user", lazy=True, cascade="all, delete-orphan")
    week_progress = db.relationship("WeekProgress", backref="user", lazy=True, cascade="all, delete-orphan")
    notifications = db.relationship("Notification", backref="user", lazy=True, cascade="all, delete-orphan")
    mistakes = db.relationship("StudentMistake", backref="user", lazy=True, cascade="all, delete-orphan")
    quiz_attempts = db.relationship("QuizAttempt", backref="user", lazy=True, cascade="all, delete-orphan")
    enrollments = db.relationship("Enrollment", backref="user", lazy=True, cascade="all, delete-orphan")


class Course(db.Model):
    """برنامه آموزشی کلان (مانند مبانی علوم کامپیوتر CS50x)."""
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    cohorts = db.relationship("Cohort", backref="course", lazy=True, cascade="all, delete-orphan")


class Cohort(db.Model):
    """نوبت برگزاری یک دوره در یک بازه زمانی مشخص (مانند دوره زمستان ۱۴۰۵ یا پاییز ۱۴۰۴)."""
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(
        db.Integer, db.ForeignKey("course.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(60), unique=True, nullable=False, index=True)
    year = db.Column(db.Integer, nullable=False, default=1405)
    season = db.Column(db.String(30), nullable=True)  # بهار / تابستان / پاییز / زمستان
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default="active", nullable=False, index=True)
    # وضعیت‌ها: draft | enrollment | active | completed | archived
    capacity = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    enrollments = db.relationship("Enrollment", backref="cohort", lazy=True, cascade="all, delete-orphan")


class Enrollment(db.Model):
    """ارتباط و عضویت دانش‌آموز در یک نوبت برگزاری مشخص (چنددوره‌ای)."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    cohort_id = db.Column(
        db.Integer, db.ForeignKey("cohort.id", ondelete="CASCADE"), nullable=False, index=True
    )
    status = db.Column(db.String(20), default="active", nullable=False, index=True)
    # وضعیت عضویت: active | pending | dropped | completed
    role = db.Column(db.String(20), default="student", nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    is_primary = db.Column(db.Boolean, default=True, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "cohort_id", name="uq_user_cohort_enrollment"),
    )


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
    graded_at = db.Column(db.DateTime, nullable=True)  # برای میانهٔ زمان بازخورد

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
    مسیر مدرک فعلاً بر اساس kb_read است (تا وقتی کوییز پیاده نشده).
    فیلدهای quiz_* برای فاز آینده آماده‌اند.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    week = db.Column(db.Integer, nullable=False, index=True)
    quiz_score = db.Column(db.Integer, default=0)        # بهترین نمره‌ی کوییز (۰..total)
    quiz_total = db.Column(db.Integer, default=0)        # تعداد سؤال‌های آزمون تسلط هفته
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


class Notification(db.Model):
    """اعلان داخل‌پنل — مهلت، بازخورد، یادآوری هدف هفتگی."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title = db.Column(db.String(150), nullable=False)
    body = db.Column(db.String(500), nullable=True)
    link = db.Column(db.String(255), nullable=True)  # مسیر نسبی مثل /assignments
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class LearningEvent(db.Model):
    """ثبت ساختاریافته رویدادهای یادگیری دانش‌آموز (حداقل داده، بدون ردگیری دستگاه)."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    event_type = db.Column(db.String(50), nullable=False, index=True)
    payload = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class ExerciseAttempt(db.Model):
    """ثبت تمرین‌های تعاملی حل‌شده (مثل قطعه‌کد جاافتاده / fill-in-the-blank)."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    week = db.Column(db.Integer, nullable=False, index=True)
    exercise_id = db.Column(db.String(50), nullable=False, index=True)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
    submitted_answer = db.Column(db.Text, nullable=True)
    hints_used = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "exercise_id", name="uq_user_exercise"),
    )


class QuizAttempt(db.Model):
    """ثبت تلاش‌های مستقل در آزمون تسلط هفتگی (Mastery Quiz).

    هر دانش‌آموز حداکثر ۵ تلاش مستقل برای هر هفته دارد.
    هر تلاش وضعیت تکمیل، نمره و پاسخ‌های مستقل دارد و تاریخچه تلاش‌ها حفظ می‌شود.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    week = db.Column(db.Integer, nullable=False, index=True)
    attempt_number = db.Column(db.Integer, default=1, nullable=False)
    score = db.Column(db.Integer, default=0, nullable=False)
    total_questions = db.Column(db.Integer, default=5, nullable=False)
    answers_json = db.Column(db.JSON, nullable=True)  # {q_id: {"answer": ..., "is_correct": bool}}
    is_completed = db.Column(db.Boolean, default=False, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    completed_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "week", "attempt_number", name="uq_user_week_attempt"),
    )


class FlashcardProgress(db.Model):
    """وضعیت مرور فلش‌کارت دانش‌آموز بر اساس جعبه لایتنر و فواصل زمانی SM-2."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    week = db.Column(db.Integer, nullable=False, index=True)
    card_id = db.Column(db.String(50), nullable=False, index=True)
    box_number = db.Column(db.Integer, default=1, nullable=False)  # 1..5
    repetitions = db.Column(db.Integer, default=0, nullable=False)
    interval_days = db.Column(db.Integer, default=1, nullable=False)
    ease_factor = db.Column(db.Float, default=2.5, nullable=False)
    next_review = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    last_reviewed = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("user_id", "card_id", name="uq_user_card"),
    )


class StreakFreeze(db.Model):
    """فریز استریک برای روزهای اضطراری یا غیبت موجه."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    earned_reason = db.Column(db.String(50), default="weekly_goal")
    used_on = db.Column(db.Date, nullable=True)
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)


class EngagementScore(db.Model):
    """امتیاز ریسک ریزش و احتمال بازگشت به یادگیری."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    latest_prob = db.Column(db.Float, nullable=False)
    latest_risk = db.Column(db.String(10), nullable=False)  # low / medium / high
    previous_prob = db.Column(db.Float, nullable=True)
    previous_risk = db.Column(db.String(10), nullable=True)
    computed_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    factors_json = db.Column(db.JSON, nullable=True)


class NotificationPreference(db.Model):
    """تنظیمات و رضایت صریح دانش‌آموز برای انواع اعلان‌ها."""
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    category = db.Column(db.String(40), primary_key=True)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
    quiet_start_hour = db.Column(db.Integer, default=22)  # ۲۲ شب
    quiet_end_hour = db.Column(db.Integer, default=8)    # ۸ صبح
    daily_limit = db.Column(db.Integer, default=1)


class StudentMistake(db.Model):
    """ثبت دقیق خطاها و اشتباهات یادگیری دانش‌آموز (Knowledge Tracing & Mistake Vault).

    این جدول پایگاه دانش سیستم از نقاط ضعف، خطاهای پرتکرار و نیازهای آموزشی هر دانش‌آموز است.
    هر بار که دانش‌آموز در تمرین کدنویسی، کوییز یا فلش‌کارت پاسخ اشتباه می‌دهد،
    یک رکورد ثبت یا به‌روزرسانی می‌شود. با تصحیح بعدی پاسخ، وضعیت به is_resolved = True تغییر می‌کند.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    week = db.Column(db.Integer, nullable=False, index=True)
    source = db.Column(db.String(30), nullable=False, index=True)  # practice | quiz | flashcard | submission
    item_id = db.Column(db.String(80), nullable=False, index=True)
    item_title = db.Column(db.String(200), nullable=True)
    concept_tag = db.Column(db.String(100), nullable=False, index=True)
    user_answer = db.Column(db.Text, nullable=True)
    expected_answer = db.Column(db.Text, nullable=True)
    explanation = db.Column(db.Text, nullable=True)
    error_count = db.Column(db.Integer, default=1, nullable=False)
    is_resolved = db.Column(db.Boolean, default=False, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    resolved_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "item_id", name="uq_user_item_mistake"),
    )


class KBPackageInstall(db.Model):
    """تاریخچه و گزارش بسته‌های پایگاه دانش نصب‌شده در پلتفرم."""
    __tablename__ = "kb_package_installs"
    id = db.Column(db.Integer, primary_key=True)
    package_type = db.Column(db.String(50), nullable=False)  # master | single_week
    version = db.Column(db.String(20), nullable=False)       # e.g. "1.0.0"
    sha256 = db.Column(db.String(64), nullable=False, unique=True, index=True)
    installed_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    installed_at_tehran = db.Column(db.String(50), nullable=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
    metadata_json = db.Column(db.JSON, nullable=True)


class AdaptiveState(db.Model):
    """وضعیت یادگیری تطبیقی دانش‌آموز (BKT، جعبه‌های لایتنر، و تاریخچه جلسات)."""
    __tablename__ = "adaptive_states"
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    state_json = db.Column(db.JSON, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


@login_manager.user_loader
def load_user(user_id: str):
    """Flask-Login با این تابع کاربر را از session بارگذاری می‌کند."""
    try:
        user = db.session.get(User, int(user_id))
    except (ValueError, TypeError):
        return None
    # حساب غیرفعال نباید session فعال داشته باشد
    if user is not None and not getattr(user, "is_active", True):
        return None
    return user
