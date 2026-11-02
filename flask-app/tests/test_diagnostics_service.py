"""تست‌های جامع سرویس عیب‌یابی و شناسنامه تشخیصی دانش‌آموز (Diagnostics & Mistake Vault)."""
import pytest
from app import db
from app.models import User, StudentMistake
from app.services import diagnostics as diag_service
from app.services import practice as practice_service


@pytest.fixture
def test_user(app):
    with app.app_context():
        u = User.query.filter_by(username="diag_student").first()
        if not u:
            u = User(username="diag_student", password_hash="dummy", xp=100, streak=3)
            db.session.add(u)
            db.session.commit()
        return u.id


def test_record_and_update_mistake(app, test_user):
    with app.app_context():
        # ثبت اولین خطا
        m1 = diag_service.record_mistake(
            user_id=test_user,
            week=1,
            source="practice",
            item_id="w01-test-ch1",
            item_title="تست حلقه For",
            concept_tag="حلقه‌ها (Loops)",
            user_answer=["<=", "5"],
            expected_answer=["<", "3"],
            explanation="شرط باید کمتر از ۳ باشد.",
        )
        assert m1.id is not None
        assert m1.error_count == 1
        assert m1.is_resolved is False
        assert m1.concept_tag == "حلقه‌ها (Loops)"

        # ثبت مجدد همان خطا (باید error_count افزایش یابد)
        m2 = diag_service.record_mistake(
            user_id=test_user,
            week=1,
            source="practice",
            item_id="w01-test-ch1",
            item_title="تست حلقه For",
            concept_tag="حلقه‌ها (Loops)",
            user_answer=[">", "3"],
            expected_answer=["<", "3"],
            explanation="شرط باید کمتر از ۳ باشد.",
        )
        assert m2.id == m1.id
        assert m2.error_count == 2
        assert m2.is_resolved is False


def test_resolve_mistake(app, test_user):
    with app.app_context():
        diag_service.record_mistake(
            user_id=test_user,
            week=1,
            source="quiz",
            item_id="w01-q-test",
            item_title="سؤال کوییز تست",
            concept_tag="متغیرها و انواع داده",
            user_answer="int",
            expected_answer="float",
        )
        # رفع خطا
        success = diag_service.resolve_mistake(test_user, "w01-q-test")
        assert success is True

        mistake = StudentMistake.query.filter_by(user_id=test_user, item_id="w01-q-test").first()
        assert mistake.is_resolved is True
        assert mistake.resolved_at is not None


def test_diagnostic_profile_generation(app, test_user):
    with app.app_context():
        # ثبت یک خطای حل‌نشده با تکرار بالا (بحرانی)
        diag_service.record_mistake(
            user_id=test_user,
            week=1,
            source="practice",
            item_id="w01-crit-1",
            item_title="خطای سمی‌کالن",
            concept_tag="خطاهای نحوی و سمی‌کالن (Syntax)",
            user_answer="line 2",
            expected_answer="line 4",
        )
        diag_service.record_mistake(
            user_id=test_user,
            week=1,
            source="practice",
            item_id="w01-crit-1",
            item_title="خطای سمی‌کالن",
            concept_tag="خطاهای نحوی و سمی‌کالن (Syntax)",
            user_answer="line 3",
            expected_answer="line 4",
        )
        diag_service.record_mistake(
            user_id=test_user,
            week=1,
            source="practice",
            item_id="w01-crit-1",
            item_title="خطای سمی‌کالن",
            concept_tag="خطاهای نحوی و سمی‌کالن (Syntax)",
            user_answer="line 1",
            expected_answer="line 4",
        )

        profile = diag_service.get_student_diagnostic_profile(test_user)
        assert profile["total_mistakes"] >= 1
        assert profile["unresolved_count"] >= 1
        assert len(profile["concepts"]) >= 1

        # مفهوم سمی‌کالن با تکرار ۳ باید بحرانی باشد
        syntax_concept = next(c for c in profile["concepts"] if "Syntax" in c["tag"] or "سمی‌کالن" in c["tag"])
        assert syntax_concept["severity"] == "critical"

        # بررسی وجود توصیه مرتبط با سمی‌کالن
        assert any("سمی‌کالن" in r or "C" in r for r in profile["recommendations"])


def test_cohort_diagnostic_overview(app, test_user):
    with app.app_context():
        cohort = diag_service.get_cohort_diagnostic_overview()
        assert "total_mistakes" in cohort
        assert "hardest_items" in cohort
        assert "concept_heatmap" in cohort
        assert isinstance(cohort["hardest_items"], list)


def test_practice_submission_triggers_mistake_recording_and_resolution(app, test_user):
    with app.app_context():
        # تلاش اشتباه در چالش هفته ۱
        res1 = practice_service.submit_challenge_attempt(
            user_id=test_user,
            week=1,
            challenge_id="w01-ch01-token-for",
            user_answer=[">", "10"],
        )
        assert res1["success"] is True
        assert res1["is_correct"] is False

        # بررسی که آیا در دیتابیس ثبت شده
        mistake = StudentMistake.query.filter_by(
            user_id=test_user, item_id="w01-ch01-token-for"
        ).first()
        assert mistake is not None
        assert mistake.is_resolved is False

        # حالا تلاش صحیح برای همان چالش
        res2 = practice_service.submit_challenge_attempt(
            user_id=test_user,
            week=1,
            challenge_id="w01-ch01-token-for",
            user_answer=["<", "3"],
        )
        assert res2["success"] is True
        assert res2["is_correct"] is True

        # بررسی رفع شدن خطا
        mistake_after = StudentMistake.query.filter_by(
            user_id=test_user, item_id="w01-ch01-token-for"
        ).first()
        assert mistake_after.is_resolved is True


def test_diagnostics_route_requires_auth(client):
    resp = client.get("/diagnostics")
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]


def test_diagnostics_route_rendering(client, app):
    with app.app_context():
        user = User(username="diag_route_user_2", password_hash="hash", is_admin=False, is_active=True)
        db.session.add(user)
        db.session.commit()
        uid = user.id

    with client.session_transaction() as sess:
        sess["_user_id"] = str(uid)

    resp = client.get("/diagnostics")
    assert resp.status_code == 200
    assert "کلینیک یادگیری" in resp.data.decode("utf-8")
    assert "جعبه اشتباهات" in resp.data.decode("utf-8")
