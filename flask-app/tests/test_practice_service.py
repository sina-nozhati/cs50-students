import pytest
from app import db
from app.models import User, Week, WeekProgress, ExerciseAttempt, LearningEvent
from app.services import practice as practice_service


def test_load_practice_session(app):
    with app.app_context():
        session_w0 = practice_service.load_practice_session(0)
        assert session_w0 is not None
        assert session_w0["week"] == 0
        assert len(session_w0["challenges"]) >= 4

        session_w1 = practice_service.load_practice_session(1)
        assert session_w1 is not None
        assert session_w1["week"] == 1
        assert len(session_w1["challenges"]) >= 4

        # هفته‌ای که فایل چالش ندارد
        assert practice_service.load_practice_session(999) is None


def test_verify_challenge_answer(app):
    with app.app_context():
        # تست Token Tap
        ch_token = {
            "type": "token_tap",
            "expected_answer": ["<", "3"],
            "explanation": "ok"
        }
        ok, _ = practice_service.verify_challenge_answer(ch_token, ["<", "3"])
        assert ok is True
        bad, _ = practice_service.verify_challenge_answer(ch_token, [">", "3"])
        assert bad is False

        # تست Parsons
        ch_parsons = {
            "type": "parsons",
            "correct_order": ["p1", "p2", "p3"],
            "explanation": "ok"
        }
        ok_p, _ = practice_service.verify_challenge_answer(ch_parsons, ["p1", "p2", "p3"])
        assert ok_p is True
        bad_p, _ = practice_service.verify_challenge_answer(ch_parsons, ["p2", "p1", "p3"])
        assert bad_p is False

        # تست Spot Bug
        ch_bug = {
            "type": "spot_bug",
            "bug_line_index": 3,
            "explanation": "ok"
        }
        ok_b, _ = practice_service.verify_challenge_answer(ch_bug, 3)
        assert ok_b is True
        bad_b, _ = practice_service.verify_challenge_answer(ch_bug, 1)
        assert bad_b is False


def test_submit_challenge_and_xp_idempotency(app):
    with app.app_context():
        user = User(username="duo_student", password_hash="hash", is_admin=False, xp=0, streak=0)
        db.session.add(user)
        db.session.commit()

        # پاسخ اشتباه
        res_wrong = practice_service.submit_challenge_attempt(
            user_id=user.id,
            week=1,
            challenge_id="w01-ch01-token-for",
            user_answer=[">", "10"],
            hints_used=0
        )
        assert res_wrong["success"] is True
        assert res_wrong["is_correct"] is False
        assert res_wrong["xp_awarded"] == 0

        # پاسخ صحیح برای اولین بار
        res_correct = practice_service.submit_challenge_attempt(
            user_id=user.id,
            week=1,
            challenge_id="w01-ch01-token-for",
            user_answer=["<", "3"],
            hints_used=0
        )
        assert res_correct["success"] is True
        assert res_correct["is_correct"] is True
        assert res_correct["xp_awarded"] == 5

        db.session.refresh(user)
        assert user.xp == 5
        assert user.streak >= 1

        # حل مجدد همان چالش نباید مجدداً XP بدهد
        res_repeat = practice_service.submit_challenge_attempt(
            user_id=user.id,
            week=1,
            challenge_id="w01-ch01-token-for",
            user_answer=["<", "3"],
            hints_used=0
        )
        assert res_repeat["is_correct"] is True
        assert res_repeat["xp_awarded"] == 0

        db.session.refresh(user)
        assert user.xp == 5


def test_complete_practice_session(app):
    with app.app_context():
        user = User(username="finisher", password_hash="hash", is_admin=False, xp=20, streak=2)
        db.session.add(user)
        db.session.commit()

        res = practice_service.complete_practice_session(
            user_id=user.id,
            week=1,
            summary={
                "completed_count": 4,
                "incorrect_count": 1,
                "time_spent_seconds": 95,
                "entry_point": "practice_runner"
            }
        )
        assert res["success"] is True
        assert "message" in res


def test_practice_routes(client, app):
    with app.app_context():
        # کاربر تست
        user = User(username="practice_tester", password_hash="hash", is_admin=False)
        db.session.add(user)

        # هفته ۱ منتشر شده
        week1 = Week.query.filter_by(number=1).first()
        if not week1:
            week1 = Week(number=1, title="هفته اول", is_published=True)
            db.session.add(week1)
        else:
            week1.is_published = True
        db.session.commit()
        user_id = user.id

    with client.session_transaction() as sess:
        sess["_user_id"] = str(user_id)

    # تست صفحه رانر
    resp = client.get("/kb/week/1/practice")
    assert resp.status_code == 200
    assert "تمرین تعاملی" in resp.data.decode("utf-8")

    # تست ارسال پاسخ JSON
    submit_resp = client.post(
        "/kb/week/1/practice/submit",
        json={
            "challenge_id": "w01-ch01-token-for",
            "answer": ["<", "3"],
            "hints_used": 0
        }
    )
    assert submit_resp.status_code == 200
    data = submit_resp.get_json()
    assert data["success"] is True
    assert data["is_correct"] is True

    # تست اتمام سشن
    complete_resp = client.post(
        "/kb/week/1/practice/complete",
        json={
            "completed_count": 4,
            "incorrect_count": 0,
            "time_spent_seconds": 60
        }
    )
    assert complete_resp.status_code == 200
    comp_data = complete_resp.get_json()
    assert comp_data["success"] is True


def test_week0_and_global_practice_routes(client, app):
    with app.app_context():
        user = User(username="week0_tester", password_hash="hash", is_admin=False)
        db.session.add(user)
        week0 = Week.query.filter_by(number=0).first()
        if not week0:
            week0 = Week(number=0, title="هفته صفر — اسکرچ", is_published=True)
            db.session.add(week0)
        else:
            week0.is_published = True
        db.session.commit()
        user_id = user.id

    with client.session_transaction() as sess:
        sess["_user_id"] = str(user_id)

    # 1. تست رندر صفحه تمرین هفته ۰
    resp_w0 = client.get("/kb/week/0/practice")
    assert resp_w0.status_code == 200
    html_w0 = resp_w0.data.decode("utf-8")
    assert "practiceApp(0," in html_w0
    assert ", false, '')" in html_w0
    assert "/kb/week/0" in html_w0

    # 2. تست ثبت پاسخ در هفته ۰ با challenge_id
    resp_sub0 = client.post(
        "/kb/week/0/practice/submit",
        json={
            "challenge_id": "w00-ch01-token-binary",
            "answer": ["0", "1"],
            "hints_used": 0
        }
    )
    assert resp_sub0.status_code == 200
    sub0_data = resp_sub0.get_json()
    assert sub0_data["success"] is True

    # 3. تست ثبت پاسخ در هفته ۰ با نام مستعار question_id و answer_value
    resp_sub0_alt = client.post(
        "/kb/week/0/practice/submit",
        json={
            "question_id": "w00-ch01-token-binary",
            "answer_value": ["0", "1"],
            "hints_used": 0
        }
    )
    assert resp_sub0_alt.status_code == 200
    sub0_alt_data = resp_sub0_alt.get_json()
    assert sub0_alt_data["success"] is True

    # 4. تست اتمام هفته ۰
    resp_comp0 = client.post(
        "/kb/week/0/practice/complete",
        json={
            "completed_count": 4,
            "incorrect_count": 0,
            "time_spent_seconds": 45
        }
    )
    assert resp_comp0.status_code == 200
    assert resp_comp0.get_json()["success"] is True

    # 5. تست رندر صفحه تمرین تطبیقی سراسری (/practice)
    resp_global = client.get("/practice")
    assert resp_global.status_code == 200
    html_global = resp_global.data.decode("utf-8")
    assert "practiceApp(null," in html_global
    assert ", true," in html_global


def test_refill_practice_hearts_endpoint(client, app):
    """تست‌های اندپوینت شارژ مجدد قلب‌های تمرین با XP."""
    from app.models import XPLog

    user = User(username="refill_tester", password_hash="hash", is_admin=False, xp=10)
    db.session.add(user)

    week1 = Week.query.filter_by(number=1).first()
    if not week1:
        week1 = Week(number=1, title="هفته اول", is_published=True)
        db.session.add(week1)
    else:
        week1.is_published = True

    db.session.commit()
    user_id = user.id

    with client.session_transaction() as sess:
        sess["_user_id"] = str(user_id)

    # 1. تلاش برای شارژ وقتی XP ناکافی است (< 20)
    resp_fail = client.post("/kb/week/1/practice/refill-hearts")
    assert resp_fail.status_code == 400
    fail_data = resp_fail.get_json()
    assert fail_data["success"] is False
    assert "حداقل به 20 XP نیاز داری" in fail_data["message"]

    # 2. افزایش موجودی به 50 XP و شارژ موفق
    user.xp = 50
    db.session.commit()
    db.session.expire_all()

    resp_success = client.post("/kb/week/1/practice/refill-hearts")
    assert resp_success.status_code == 200, resp_success.get_json()
    succ_data = resp_success.get_json()
    assert succ_data["success"] is True
    assert succ_data["hearts"] == 5
    assert succ_data["current_xp"] == 30

    u = db.session.get(User, user_id)
    assert u.xp == 30
    log = XPLog.query.filter(XPLog.user_id == user_id, XPLog.amount == -20).first()
    assert log is not None
    assert "practice:hearts:refill:w1" in log.reason

    # 3. شارژ در تمرین سراسری تطبیقی (/practice/refill-hearts)
    resp_global = client.post("/practice/refill-hearts")
    assert resp_global.status_code == 200
    g_data = resp_global.get_json()
    assert g_data["success"] is True
    assert g_data["current_xp"] == 10

    u = db.session.get(User, user_id)
    assert u.xp == 10

    # 4. تلاش مجدد وقتی به 10 رسیده و ناکافی است
    resp_fail2 = client.post("/practice/refill-hearts")
    assert resp_fail2.status_code == 400
