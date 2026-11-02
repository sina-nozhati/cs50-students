"""اعلان‌های داخل‌پنل — ساده، بدون کانال بیرونی."""
from datetime import datetime

from app import db
from app.models import Notification


def create(user_id: int, title: str, body: str = "", link: str | None = None) -> Notification:
    """یک اعلان خوانده‌نشده برای کاربر می‌سازد."""
    n = Notification(
        user_id=user_id,
        title=title,
        body=body or None,
        link=link,
        is_read=False,
        created_at=datetime.utcnow(),
    )
    db.session.add(n)
    db.session.commit()
    return n


def list_for_user(user_id: int, limit: int = 10, unread_only: bool = False) -> list[Notification]:
    q = Notification.query.filter_by(user_id=user_id)
    if unread_only:
        q = q.filter_by(is_read=False)
    return q.order_by(Notification.created_at.desc()).limit(limit).all()


def unread_count(user_id: int) -> int:
    return Notification.query.filter_by(user_id=user_id, is_read=False).count()


def mark_read(notification_id: int, user_id: int) -> bool:
    n = Notification.query.filter_by(id=notification_id, user_id=user_id).first()
    if n is None:
        return False
    n.is_read = True
    db.session.commit()
    return True


def mark_all_read(user_id: int) -> int:
    rows = Notification.query.filter_by(user_id=user_id, is_read=False).all()
    for n in rows:
        n.is_read = True
    db.session.commit()
    return len(rows)
