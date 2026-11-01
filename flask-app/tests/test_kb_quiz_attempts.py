"""تست‌های آزمون تسلط، ثبت تلاش‌ها (QuizAttempt)، سقف ۵ تلاش، جلوگیری از تغییر نمره و چالش‌های تعاملی."""
import json
import pytest
from app import db
from app.models import User, Week, WeekProgress, ExerciseAttempt, QuizAttempt
from app.services import kb_interactive, practice as practice_service, kb_admin


@pytest.fixture
def student_user(app):
    with app.app_context():
        user = User.query.filter_by(username="quiz_test_student").first()
        if not user:
            user = User(
                username="quiz_test_student",
                password_hash="test_hash_1234",
                is_admin=False,
            )
            db.session.add(user)
            db.session.commit()
        return user.id


@pytest.fixture
def ensure_weeks(app):
    with app.app_context():
        for w in [1, 2]:
            week_row = Week.query.filter_by(number=w).first()
            if not week_row:
                week_row = Week(number=w, title=f"هفته {w}", is_published=True)
                db.session.add(week_row)
        db.session.commit()


def test_quiz_attempt_creation_and_question_submit(app, student_user, ensure_weeks):
    """تست ثبت پاسخ در تلاش اول آزمون و اعتبارسنجی نمره."""
    with app.app_context():
        quizzes = kb_interactive.load_quizzes_for_week(1, user_id=student_user)
        assert len(quizzes) == 5
        q1 = quizzes[0]
        assert q1["id"] == "w01-q-001"
        assert q1["type"] == "mcq"
        assert len(q1["options"]) >= 2
        assert q1["attempted"] is False

        # پاسخ صحیح به سوال اول
        res = kb_interactive.submit_quiz_question(
            user_id=student_user,
            week=1,
            question_id="w01-q-001",
            answer_value="a",
        )
        assert res["success"] is True
        assert res["is_correct"] is True
        assert res["current_score"] == 1
        assert res["total_score"] == 5
        assert res["attempt_number"] == 1


def test_quiz_score_isolation_from_practice_challenges(app, student_user, ensure_weeks):
    """تست ایزوله‌سازی نمره کوییز از چالش‌های تمرینی (رفع باگ جهش نمره به ۷ از ۵)."""
    with app.app_context():
        # فرض کنید کاربر ۴ چالش تمرینی را حل کرده است
        for i in range(1, 5):
            att = ExerciseAttempt(
                user_id=student_user,
                week=1,
                exercise_id=f"w01-ch0{i}-dummy",
                is_correct=True,
                submitted_answer="done",
            )
            db.session.add(att)
        db.session.commit()

        # ثبت ۲ پاسخ در آزمون (یک درست، یک غلط)
        r1 = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-001", "a")  # درست
        assert r1["is_correct"] is True

        r2 = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-002", "d")  # غلط
        assert r2["is_correct"] is False

        # نمره کوییز باید منحصراً ۱ باشد، نه ۴ + ۱ = ۵ یا بالاتر
        assert r2["current_score"] == 1
        assert r2["total_score"] == 5

        wp = WeekProgress.query.filter_by(user_id=student_user, week=1).first()
        assert wp is not None
        assert wp.quiz_score == 1
        assert wp.quiz_total == 5


def test_answer_immutability_and_finalization_lock(app, student_user, ensure_weeks):
    """تست جلوگیری از تغییر پاسخ ثبت‌شده و قفل آزمون پس از پایان."""
    with app.app_context():
        # ثبت پاسخ برای سوال اول
        r1 = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-001", "a")
        assert r1["success"] is True

        # تلاش مجدد برای تغییر پاسخ همان سوال در همان تلاش
        r1_repeat = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-001", "b")
        assert r1_repeat["success"] is False
        assert r1_repeat["error"] == "already_answered"
        assert r1_repeat["current_score"] == 1

        # پاسخ به بقیه سوالات برای نهایی شدن آزمون
        kb_interactive.submit_quiz_question(student_user, 1, "w01-q-002", "a")
        kb_interactive.submit_quiz_question(student_user, 1, "w01-q-003", "true")
        kb_interactive.submit_quiz_question(student_user, 1, "w01-q-004", "false")
        r5 = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-005", ["p1", "p2", "p3"])

        assert r5["is_finalized"] is True
        assert r5["current_score"] == 5

        # تلاش برای پاسخ دادن یا تغییر پس از نهایی شدن
        r_locked = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-001", "c")
        assert r_locked["success"] is False
        assert r_locked["error"] == "attempt_finalized"
        assert r_locked["is_finalized"] is True


def test_retake_quiz_and_five_attempts_limit(app, student_user, ensure_weeks):
    """تست ایجاد تلاش‌های مستقل تا سقف ۵ بار و رد تلاش ششم."""
    with app.app_context():
        # پاک‌سازی تلاش‌های قبلی کاربر برای این تست
        QuizAttempt.query.filter_by(user_id=student_user, week=1).delete()
        db.session.commit()

        # انجام و تکمیل تلاش ۱ تا ۵
        for attempt_no in range(1, 6):
            meta = kb_interactive.get_quiz_attempt_meta(student_user, 1)
            assert meta["attempt_number"] == attempt_no

            # ثبت پاسخ‌ها
            kb_interactive.submit_quiz_question(student_user, 1, "w01-q-001", "a")
            kb_interactive.submit_quiz_question(student_user, 1, "w01-q-002", "a")
            kb_interactive.submit_quiz_question(student_user, 1, "w01-q-003", "true")
            kb_interactive.submit_quiz_question(student_user, 1, "w01-q-004", "false")
            fin = kb_interactive.submit_quiz_question(student_user, 1, "w01-q-005", ["p1", "p2", "p3"])
            assert fin["is_finalized"] is True

            if attempt_no < 5:
                # درخواست شروع مجدد آزمون
                retake = kb_interactive.start_new_quiz_attempt(student_user, 1)
                assert retake["success"] is True
                assert retake["attempt_number"] == attempt_no + 1
                assert retake["remaining_attempts"] == 5 - (attempt_no + 1)

        # تلاش ششم باید مسدود شود
        retake_6 = kb_interactive.start_new_quiz_attempt(student_user, 1)
        assert retake_6["success"] is False
        assert retake_6["error"] == "max_attempts_reached"
        assert retake_6["remaining_attempts"] == 0


def test_parsons_and_predict_output_rendering(app, student_user, ensure_weeks):
    """تست بارگذاری کامل خطوط پارسونز و قطعه‌کد برای پیش‌بینی خروجی."""
    with app.app_context():
        quizzes_w1 = kb_interactive.load_quizzes_for_week(1, user_id=student_user)
        parsons_q = next((q for q in quizzes_w1 if q["type"] == "parsons"), None)
        assert parsons_q is not None
        assert "lines" in parsons_q
        assert len(parsons_q["lines"]) >= 3
        # بررسی وجود خطوط کد در پارسونز
        line_codes = [l["code"] for l in parsons_q["lines"]]
        assert "code hello.c" in line_codes
        assert "make hello" in line_codes

        quizzes_w2 = kb_interactive.load_quizzes_for_week(2, user_id=student_user)
        predict_q = next((q for q in quizzes_w2 if q["type"] == "predict_output"), None)
        assert predict_q is not None
        assert "code" in predict_q
        assert len(predict_q["code"]) > 0
        assert predict_q["lang"] in ("c", "bash")


def test_week2_practice_session_and_challenges(app, ensure_weeks):
    """تست وجود و بارگذاری موفقیت‌آمیز چالش‌های تعاملی هفته ۲."""
    with app.app_context():
        assert practice_service.has_practice_session(2) is True
        session = practice_service.load_practice_session(2)
        assert session is not None
        assert session["week"] == 2
        assert len(session["challenges"]) == 4

        # بررسی انواع چالش‌های هفته ۲
        types = [ch["type"] for ch in session["challenges"]]
        assert "token_tap" in types
        assert "parsons" in types
        assert "spot_bug" in types

        # بررسی گزارش ادمین
        status = kb_admin.get_all_weeks_kb_status()
        w2_stat = next((w for w in status if w["number"] == 2), None)
        assert w2_stat is not None
        assert w2_stat["has_challenges"] is True
        assert w2_stat["challenges_count"] == 4


def test_retake_route(client, student_user, ensure_weeks):
    """تست روت HTTP برای شروع مجدد آزمون."""
    with client.session_transaction() as sess:
        sess["_user_id"] = str(student_user)

    resp = client.post("/kb/week/1/quiz/retake", follow_redirects=True)
    assert resp.status_code == 200
    assert "آزمون تسلط" in resp.get_data(as_text=True)
