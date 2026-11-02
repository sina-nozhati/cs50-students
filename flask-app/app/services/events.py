"""سرویس ثبت رویدادهای یادگیری دانش‌آموز (حداقل داده، اخلاقی، بدون اطلاعات دستگاه)."""
import json
from datetime import datetime
from app import db
from app.models import LearningEvent

ALLOWED_EVENT_TYPES = {
    "app_open",
    "session_start",
    "session_end",
    "exercise_attempt",
    "quiz_attempt",
    "lesson_complete",
    "flashcard_review",
    "submission",
    "server_learning_error"
}


def log_event(user_id: int, event_type: str, payload: dict | None = None) -> LearningEvent | None:
    """ثبت رویداد یادگیری در پایگاه داده با بررسی مجاز بودن و حجم محدود."""
    if event_type not in ALLOWED_EVENT_TYPES:
        return None

    # بررسی سقف اندازه payload برای بهینه‌سازی دیتابیس (حداکثر ۱ کیلوبایت)
    if payload:
        try:
            dumped = json.dumps(payload, ensure_ascii=False)
            if len(dumped.encode("utf-8")) > 1024:
                payload = {"warning": "payload_truncated", "summary": str(payload)[:200]}
        except Exception:
            payload = {"error": "unserializable_payload"}

    event = LearningEvent(
        user_id=user_id,
        event_type=event_type,
        payload=payload or {},
        created_at=datetime.utcnow()
    )
    db.session.add(event)
    db.session.commit()
    return event


def get_user_recent_events(user_id: int, limit: int = 20) -> list[LearningEvent]:
    return (
        LearningEvent.query.filter_by(user_id=user_id)
        .order_by(LearningEvent.created_at.desc())
        .limit(limit)
        .all()
    )
