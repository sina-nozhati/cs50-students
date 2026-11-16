"""آزمون‌های اعتبارسنجی اندپوینت‌های HTTP گیمیفیکیشن (Quests, Achievements, StreakFreeze, Leaderboard)."""
import pytest
from app import db
from app.models import User
from app.services import quests as quest_service


def test_api_daily_quests_and_claim(client, app, student_user):
    with client.session_transaction() as sess:
        sess["_user_id"] = str(student_user.id)
        sess["_fresh"] = True

    # ۱. استعلام لیست مأموریت‌های روزانه
    res = client.get("/api/quests")
    assert res.status_code == 200
    data = res.get_json()
    assert data["success"] is True
    assert len(data["quests"]) == 3

    # ۲. ادعای پاداش مأموریت تکمیل‌نشده باید ارور ۴۰۰ بدهد
    q_id = data["quests"][0]["id"]
    res_claim_fail = client.post(f"/quests/claim/{q_id}")
    assert res_claim_fail.status_code == 400

    # ۳. تکمیل مأموریت و دریافت موفق پاداش
    with app.app_context():
        quest_service.track_quest_progress(student_user.id, data["quests"][0]["quest_type"], 10)

    res_claim_ok = client.post(f"/quests/claim/{q_id}")
    assert res_claim_ok.status_code == 200
    claim_data = res_claim_ok.get_json()
    assert claim_data["success"] is True


def test_streak_freeze_buy_route(client, app, student_user):
    with client.session_transaction() as sess:
        sess["_user_id"] = str(student_user.id)
        sess["_fresh"] = True

    with app.app_context():
        user = db.session.get(User, student_user.id)
        user.xp = 100
        db.session.commit()

    res = client.post("/streak-freeze/buy")
    assert res.status_code == 200
    data = res.get_json()
    assert data["success"] is True
    assert data["freezes_count"] == 1


def test_api_achievements_and_weekly_leaderboard(client, app, student_user):
    with client.session_transaction() as sess:
        sess["_user_id"] = str(student_user.id)
        sess["_fresh"] = True

    res_ach = client.get("/api/achievements")
    assert res_ach.status_code == 200
    ach_data = res_ach.get_json()
    assert ach_data["success"] is True
    assert "achievements" in ach_data

    res_lb = client.get("/api/leaderboard/weekly")
    assert res_lb.status_code == 200
    lb_data = res_lb.get_json()
    assert lb_data["success"] is True
    assert "leaderboard" in lb_data
