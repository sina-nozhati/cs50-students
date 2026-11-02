import pytest
from app import db
from app.models import User, LearningEvent, ExerciseAttempt, EngagementScore
from app.services import events as event_service
from app.services import exercises as exercise_service
from app.services import engagement as engagement_service


def test_learning_events_whitelist(app):
    with app.app_context():
        user = User(username="test_student", password_hash="hash", is_admin=False)
        db.session.add(user)
        db.session.commit()

        # رویداد معتبر
        evt = event_service.log_event(user.id, "app_open", {"entry_point": "direct"})
        assert evt is not None
        assert evt.event_type == "app_open"

        # رویداد نامعتبر
        invalid = event_service.log_event(user.id, "unauthorized_tracking", {"key": "val"})
        assert invalid is None


def test_code_exercise_submission_and_xp(app):
    with app.app_context():
        user = User(username="coder", password_hash="hash", is_admin=False, xp=0, streak=0)
        db.session.add(user)
        db.session.commit()

        # پاسخ غلط
        res_wrong = exercise_service.submit_exercise(user.id, "w00-code-binary", "99")
        assert res_wrong["is_correct"] is False
        assert res_wrong["xp_awarded"] == 0

        # پاسخ درست
        res_correct = exercise_service.submit_exercise(user.id, "w00-code-binary", "2")
        assert res_correct["is_correct"] is True
        assert res_correct["xp_awarded"] == 5

        # بررسی امتیاز کاربر
        db.session.refresh(user)
        assert user.xp == 5
        assert user.streak >= 1

        # حل مجدد نباید XP مضاعف بدهد (Idempotency)
        res_repeat = exercise_service.submit_exercise(user.id, "w00-code-binary", "2")
        assert res_repeat["xp_awarded"] == 0
        db.session.refresh(user)
        assert user.xp == 5


def test_engagement_calculation(app):
    with app.app_context():
        user = User(username="busy_student", password_hash="hash", is_admin=False)
        db.session.add(user)
        db.session.commit()

        res = engagement_service.compute_user_engagement(user.id)
        assert "probability" in res
        assert res["risk_level"] in ("low", "medium", "high")
        assert len(res["factors"]) > 0
