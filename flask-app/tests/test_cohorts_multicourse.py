"""تست‌های جامع معماری چنددوره‌ای، نوبت‌های برگزاری (Cohorts) و مدیریت دانش‌آموزان.

پوشش کامل:
1. راه‌اندازی و تضمین دوره و نوبت پیش‌فرض بدون ریزش اطلاعات.
2. عملیات کامل CRUD نوبت‌های برگزاری و بایگانی ایمن.
3. ثبت‌نام تکی، گروهی و کنترل ظرفیت و جلوگیری از تکرار.
4. تغییر وضعیت عضویت و لغو عضویت بدون حذف حساب کاربری.
5. جابجایی بین دوره‌ها و ایزوله‌سازی نشست (Session).
6. روت‌های پنل مدیریت ادمین و احراز هویت.
7. روت‌های داشبورد دانش‌آموز و دوره‌های من.
"""
import pytest
from app import db
from app.models import Course, Cohort, Enrollment, User
from app.services import cohorts as cohort_service
from werkzeug.security import generate_password_hash


def test_default_course_and_cohort_initialized(app):
    """تست اطمینان از ایجاد دوره و نوبت پیش‌فرض CS50x."""
    with app.app_context():
        default_course = Course.query.filter_by(code="cs50x").first()
        assert default_course is not None
        assert "CS50x" in default_course.title

        default_cohort = Cohort.query.filter_by(code="cs50x-winter-1405").first()
        assert default_cohort is not None
        assert default_cohort.course_id == default_course.id
        assert default_cohort.status == "active"
        assert default_cohort.year == 1405


def test_auto_enroll_existing_students(app):
    """تست عضویت خودکار کاربران موجود در نوبت فعال پیش‌فرض."""
    with app.app_context():
        # ایجاد کاربر دانش‌آموز
        student = User(
            username="reza_test",
            password_hash=generate_password_hash("pass123"),
            is_admin=False,
        )
        db.session.add(student)
        db.session.commit()

        # اجرای متد اطمینان
        cohort_service.ensure_default_course_and_cohort()

        # بررسی عضویت
        default_cohort = Cohort.query.filter_by(code="cs50x-winter-1405").first()
        enr = Enrollment.query.filter_by(user_id=student.id, cohort_id=default_cohort.id).first()
        assert enr is not None
        assert enr.status == "active"
        assert enr.is_primary is True


def test_cohort_crud_operations(app):
    """تست ایجاد، ویرایش، لیست و بایگانی نوبت‌های برگزاری."""
    with app.app_context():
        course = Course.query.filter_by(code="cs50x").first()

        # ۱. ایجاد نوبت جدید
        new_cohort = cohort_service.create_cohort(
            course_id=course.id,
            name="دوره بهاره ۱۴۰۶",
            code="cs50x-spring-1406",
            year=1406,
            season="بهار",
            status="enrollment",
            capacity=30,
            description="نوبت بهاره اختصاصی پایتون و وب",
        )
        assert new_cohort.id is not None
        assert new_cohort.code == "cs50x-spring-1406"

        # ۲. لیست با فیلتر وضعیت
        active_list = cohort_service.list_all_cohorts(status_filter="active")
        assert any(c["code"] == "cs50x-winter-1405" for c in active_list)
        assert not any(c["code"] == "cs50x-spring-1406" for c in active_list)

        enrollment_list = cohort_service.list_all_cohorts(status_filter="enrollment")
        assert any(c["code"] == "cs50x-spring-1406" for c in enrollment_list)

        # ۳. ویرایش نوبت
        updated = cohort_service.update_cohort(
            cohort_id=new_cohort.id,
            name="دوره بهاره طلایی ۱۴۰۶",
            year=1406,
            season="بهار",
            status="active",
            capacity=40,
        )
        assert updated.name == "دوره بهاره طلایی ۱۴۰۶"
        assert updated.capacity == 40
        assert updated.status == "active"

        # ۴. بایگانی نوبت
        archived = cohort_service.archive_cohort(new_cohort.id)
        assert archived.status == "archived"


def test_single_and_bulk_enrollment(app):
    """تست ثبت‌نام تکی و گروهی، کنترل ظرفیت و ثبت سوابق."""
    with app.app_context():
        course = Course.query.first()
        cohort = cohort_service.create_cohort(
            course_id=course.id,
            name="دوره پاییز ۱۴۰۵",
            code="cs50x-fall-1405",
            year=1405,
            season="پاییز",
            status="active",
            capacity=2,  # ظرفیت محدود برای تست
        )

        u1 = User(username="user_one", password_hash="pw", is_admin=False)
        u2 = User(username="user_two", password_hash="pw", is_admin=False)
        u3 = User(username="user_three", password_hash="pw", is_admin=False)
        db.session.add_all([u1, u2, u3])
        db.session.commit()

        # ثبت‌نام تکی u1
        ok, msg = cohort_service.enroll_student_in_cohort(u1.id, cohort.id)
        assert ok is True

        # ثبت‌نام تکراری u1 باید رد شود
        ok_dup, msg_dup = cohort_service.enroll_student_in_cohort(u1.id, cohort.id)
        assert ok_dup is False
        assert "از قبل" in msg_dup

        # ثبت‌نام تکی u2 (ظرفیت تکمیل می‌شود)
        ok2, msg2 = cohort_service.enroll_student_in_cohort(u2.id, cohort.id)
        assert ok2 is True

        # ثبت‌نام گروهی با کاربر سوم و کاربر موجود و کاربر نامعتبر
        res = cohort_service.bulk_enroll_students(
            cohort.id,
            ["user_one", "user_two", "user_three", "non_existent_user"],
        )
        assert res["already_enrolled"] == 2
        assert "non_existent_user" in res["not_found"]
        # u3 به دلیل پر بودن ظرفیت ثبت‌نام نمی‌شود
        assert res["enrolled"] == 0 or len(res["errors"]) > 0


def test_enrollment_status_and_remove(app):
    """تست به‌روزرسانی وضعیت عضویت و حذف عضویت با حفظ کاربر."""
    with app.app_context():
        course = Course.query.first()
        cohort = cohort_service.create_cohort(
            course_id=course.id,
            name="دوره تابستان ۱۴۰۵",
            code="cs50x-summer-1405",
            year=1405,
            season="تابستان",
        )
        user = User(username="sara", password_hash="pw", is_admin=False)
        db.session.add(user)
        db.session.commit()

        cohort_service.enroll_student_in_cohort(user.id, cohort.id)
        enr = Enrollment.query.filter_by(user_id=user.id, cohort_id=cohort.id).first()
        assert enr is not None

        # تغییر وضعیت به completed
        ok = cohort_service.update_enrollment_status(enr.id, "completed")
        assert ok is True
        updated_enr = db.session.get(Enrollment, enr.id)
        assert updated_enr.status == "completed"
        assert updated_enr.completed_at is not None

        # حذف عضویت
        del_ok = cohort_service.remove_enrollment(enr.id)
        assert del_ok is True
        assert db.session.get(Enrollment, enr.id) is None

        # اطمینان از اینکه کاربر در جدول Users باقی مانده و حذف نشده
        user_in_db = db.session.get(User, user.id)
        assert user_in_db is not None
        assert user_in_db.username == "sara"


def test_student_cohort_switching_and_active_detection(app):
    """تست جابجایی بین چند دوره و شناسایی دوره فعال دانش‌آموز."""
    with app.app_context():
        course = Course.query.first()
        cohort1 = Cohort.query.filter_by(code="cs50x-winter-1405").first()
        cohort2 = cohort_service.create_cohort(
            course_id=course.id,
            name="دوره تابستان ۱۴۰۶",
            code="cs50x-summer-1406",
            year=1406,
            season="تابستان",
        )

        user = User(username="multi_term_student", password_hash="pw", is_admin=False)
        db.session.add(user)
        db.session.commit()

        # ثبت‌نام در هر دو دوره
        cohort_service.enroll_student_in_cohort(user.id, cohort1.id, is_primary=True)
        cohort_service.enroll_student_in_cohort(user.id, cohort2.id, is_primary=False)

        # پیش‌فرض دوره فعال اولی است
        active = cohort_service.get_active_cohort_for_user(user.id)
        assert active.id == cohort1.id

        # تغییر به دوره دوم
        switched = cohort_service.switch_user_active_cohort(user.id, cohort2.id)
        assert switched is True

        active_after = cohort_service.get_active_cohort_for_user(user.id)
        assert active_after.id == cohort2.id

        # بررسی لیست دوره‌های من (get_user_enrollments)
        my_enrs = cohort_service.get_user_enrollments(user.id)
        assert len(my_enrs) == 2
        assert any(e["cohort_id"] == cohort2.id and e["is_primary"] is True for e in my_enrs)


def test_admin_cohort_routes(client, admin_user):
    """تست روت‌های مدیریت دوره‌ها در پنل ادمین."""
    # ورود به عنوان ادمین
    with client.session_transaction() as sess:
        sess["_user_id"] = str(admin_user.id)

    # GET /admin/cohorts
    resp = client.get("/admin/cohorts")
    assert resp.status_code == 200
    assert "دوره‌ها و نوبت‌های آموزشی" in resp.data.decode("utf-8")

    # GET /admin/cohorts/create
    resp_create_get = client.get("/admin/cohorts/create")
    assert resp_create_get.status_code == 200

    # POST /admin/cohorts/create
    course = Course.query.first()
    post_data = {
        "course_id": course.id,
        "name": "دوره وب ۱۴۰۶",
        "code": "cs50x-web-1406",
        "year": 1406,
        "season": "بهار",
        "status": "active",
        "capacity": 45,
        "description": "توضیحات آزمایشی دوره",
    }
    resp_create_post = client.post("/admin/cohorts/create", data=post_data, follow_redirects=True)
    assert resp_create_post.status_code == 200
    assert "دوره وب ۱۴۰۶" in resp_create_post.data.decode("utf-8")

    created = Cohort.query.filter_by(code="cs50x-web-1406").first()
    assert created is not None

    # GET /admin/cohorts/<id>
    resp_detail = client.get(f"/admin/cohorts/{created.id}")
    assert resp_detail.status_code == 200
    assert "cs50x-web-1406" in resp_detail.data.decode("utf-8")


def test_student_dashboard_and_my_courses_routes(client, student_user):
    """تست روت‌های داشبورد، دوره‌های من و جابجایی نوبت برای دانش‌آموز."""
    # ثبت‌نام دانش‌آموز در دوره پیش‌فرض
    default_cohort = Cohort.query.filter_by(code="cs50x-winter-1405").first()
    cohort_service.enroll_student_in_cohort(student_user.id, default_cohort.id, is_primary=True)

    with client.session_transaction() as sess:
        sess["_user_id"] = str(student_user.id)

    # GET /dashboard
    resp_dash = client.get("/dashboard")
    assert resp_dash.status_code == 200
    html = resp_dash.data.decode("utf-8")
    assert student_user.username in html
    assert "پیشرفت تا مدرک نهایی" in html

    # GET /my-courses
    resp_courses = client.get("/my-courses")
    assert resp_courses.status_code == 200
    assert "دوره‌های آموزشی من" in resp_courses.data.decode("utf-8")
    assert default_cohort.name in resp_courses.data.decode("utf-8")
