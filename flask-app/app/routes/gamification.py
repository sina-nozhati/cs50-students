"""ماژول گیمیفیکیشن — لیدربورد کلاسی (۱۰ نفر برتر)."""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.services import xp as xp_service
from app.services import progress as progress_service

bp = Blueprint("gamification", __name__, url_prefix="/gamification")


@bp.before_request
@login_required
def _require_login():
    """همه‌ی روت‌های /gamification نیاز به لاگین دارند (طبق سیاست دسترسی)."""
    pass


@bp.route("/leaderboard")
def leaderboard():
    """۱۰ نفر برتر کلاس انزلی بر اساس XP + رتبه‌ی کاربر فعلی."""
    top_users = xp_service.leaderboard(limit=10)
    rank = progress_service.get_class_rank(current_user.id)
    return render_template(
        "gamification/leaderboard.html", users=top_users, rank=rank
    )
