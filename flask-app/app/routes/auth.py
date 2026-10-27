"""احراز هویت ساده.

در فاز ۱: نام کاربری + رمز. کلاس با یک رمز ثابت وارد میشود.
امنیت کافی برای یک ابزار آموزشی در فاز آلفا؛ بعداً Telegram login اضافه میشود.
"""
from collections import defaultdict, deque
from time import time

from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from urllib.parse import urlparse, urljoin
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.models import User

bp = Blueprint("auth", __name__)

# محدودیت نرخ ورود در حافظهٔ پروسه — برای تک‌ورکر Gunicorn کافی است.
_login_attempts: dict[str, deque] = defaultdict(deque)


def _is_safe_url(target: str) -> bool:
    """بررسی امنیت URL هدف — جلوگیری از Open Redirect.

    فقط URLهای نسبی (داخل همین سایت) مجازند.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


def _client_ip() -> str:
    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.remote_addr or "unknown"


def _login_rate_limited(ip: str) -> bool:
    """True اگر بیش از حد مجاز در پنجرهٔ زمانی تلاش ورود شده باشد."""
    limit = current_app.config.get("LOGIN_RATE_LIMIT", 10)
    window = current_app.config.get("LOGIN_RATE_WINDOW_SECONDS", 300)
    now = time()
    q = _login_attempts[ip]
    while q and now - q[0] > window:
        q.popleft()
    return len(q) >= limit


def _record_login_attempt(ip: str) -> None:
    _login_attempts[ip].append(time())


@bp.route("/login", methods=["GET", "POST"])
def login():
    """فرم ورود — بعد از ورود، به صفحه‌ای که کاربر از آن آمده برمی‌گردد (next).

    اگر next نباشد، کاربر عادی به داشبورد و ادمین به پنل ادمین می‌رود.
    این رفتار پیش‌بینی‌پذیر است: کاربری که از /assignments می‌آید، بعد از ورود
    به همان صفحه برمی‌گردد، نه لندینگ.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        ip = _client_ip()
        if _login_rate_limited(ip):
            flash("تعداد تلاش‌های ورود زیاد است. چند دقیقه بعد دوباره امتحان کنید.", "error")
            return redirect(url_for("auth.login"))

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        next_url = request.form.get("next", "")

        user = User.query.filter_by(username=username).first()
        # پیام یکسان — افشای وجود حساب نباشد
        if (
            user is None
            or not getattr(user, "is_active", True)
            or not check_password_hash(user.password_hash, password)
        ):
            _record_login_attempt(ip)
            flash("نام کاربری یا رمز اشتباه است.", "error")
            return redirect(url_for("auth.login", next=next_url))

        login_user(user, remember=True)
        flash("خوش آمدید!", "success")

        if next_url and _is_safe_url(next_url):
            return redirect(next_url)
        return redirect(url_for("main.dashboard"))

    return render_template("auth/login.html", next=request.args.get("next", ""))


@bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """پروفایل کاربری و تغییر رمز عبور دانش‌آموز."""
    if request.method == "POST":
        current_password = request.form.get("current_password", "")
        new_password = request.form.get("new_password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not check_password_hash(current_user.password_hash, current_password):
            flash("رمز عبور فعلی نادرست است.", "error")
            return redirect(url_for("auth.profile"))

        if len(new_password) < 4:
            flash("رمز عبور جدید باید حداقل ۴ کاراکتر باشد.", "error")
            return redirect(url_for("auth.profile"))

        if new_password != confirm_password:
            flash("تکرار رمز عبور جدید مطابقت ندارد.", "error")
            return redirect(url_for("auth.profile"))

        current_user.password_hash = generate_password_hash(new_password)
        db.session.commit()

        flash("رمز عبور شما با موفقیت تغییر کرد.", "success")
        return redirect(url_for("auth.profile"))

    return render_template("auth/profile.html", user=current_user)


@bp.route("/logout")
@login_required
def logout():
    """خروج از حساب کاربری."""
    logout_user()
    flash("خارج شدید.", "info")
    return redirect(url_for("main.index"))
