"""تست‌های سیستم دانلودهای پویا، امنیت سرو فایل، هدرهای استاندارد، ETag، و پیشگیری از نشت راه‌حل."""
import json
import pytest
from pathlib import Path
from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Week
from app.services import downloads as downloads_service
from app.kb_downloads.generate import build_week


@pytest.fixture()
def student(app):
    user = User(
        username="dl_student",
        password_hash=generate_password_hash("pw123"),
        is_admin=False,
    )
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture()
def admin(app):
    user = User(
        username="dl_admin",
        password_hash=generate_password_hash("adminpw"),
        is_admin=True,
    )
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture()
def setup_weeks(app):
    with app.app_context():
        # اطمینان از وجود هفته‌های ۶ و ۷ در دیتابیس
        w6 = Week.query.filter_by(number=6).first()
        if not w6:
            w6 = Week(number=6, title="هفته ۶ پایتون", is_published=True)
            db.session.add(w6)
        else:
            w6.is_published = True

        # هفته ۷۷ به عنوان منتشر نشده
        w77 = Week.query.filter_by(number=77).first()
        if not w77:
            w77 = Week(number=77, title="هفته آزمایشی مخفی", is_published=False)
            db.session.add(w77)
        else:
            w77.is_published = False

        db.session.commit()


class TestDownloadsSecurity:
    def test_anonymous_access_redirects(self, client):
        resp = client.get("/kb/downloads/week-06/handout.pdf")
        assert resp.status_code in (302, 401)

    def test_path_traversal_blocked(self, client, student, setup_weeks):
        client.post("/login", data={"username": "dl_student", "password": "pw123"})

        # تلاش برای خروج از دایرکتوری با ../
        resp = client.get("/kb/downloads/week-06/..%2f..%2fconfig.py")
        assert resp.status_code in (400, 404)

        resp2 = client.get("/kb/downloads/week-06/....//....//etc/passwd")
        assert resp2.status_code in (400, 404)

    def test_nonexistent_file_returns_404(self, client, student, setup_weeks):
        client.post("/login", data={"username": "dl_student", "password": "pw123"})
        resp = client.get("/kb/downloads/week-06/random_ghost_file.pdf")
        assert resp.status_code == 404

    def test_unpublished_week_access_forbidden(self, client, student, setup_weeks):
        client.post("/login", data={"username": "dl_student", "password": "pw123"})
        resp = client.get("/kb/downloads/week-77/handout.pdf")
        assert resp.status_code == 404


class TestHeadersAndCaching:
    def test_rfc5987_and_security_headers(self, client, student, setup_weeks):
        client.post("/login", data={"username": "dl_student", "password": "pw123"})

        # اطمینان از وجود فایل‌های دانلودی هفته ۶
        downloads_service.build_downloads_for_week("week-06", force=False)

        resp = client.get("/kb/downloads/week-06/handout.html")
        assert resp.status_code == 200

        # هدرهای امنیتی
        assert resp.headers.get("X-Content-Type-Options") == "nosniff"
        etag = resp.headers.get("ETag")
        assert etag is not None
        assert "Cache-Control" in resp.headers

        # هدر Content-Disposition و انکودینگ RFC 5987
        cd = resp.headers.get("Content-Disposition", "")
        assert "filename=" in cd
        assert "filename*=UTF-8''" in cd

    def test_etag_304_caching(self, client, student, setup_weeks):
        client.post("/login", data={"username": "dl_student", "password": "pw123"})

        downloads_service.build_downloads_for_week("week-06", force=False)

        resp1 = client.get("/kb/downloads/week-06/handout.html")
        assert resp1.status_code == 200
        etag = resp1.headers.get("ETag")
        assert etag

        # ارسال درخواست با If-None-Match
        resp2 = client.get("/kb/downloads/week-06/handout.html", headers={"If-None-Match": etag})
        assert resp2.status_code == 304


class TestSolutionLeakPrevention:
    def test_solution_leak_halts_build(self, tmp_path):
        """تست عدم نشت پاسخ: در صورتی که solution.provided == true باشد، بیلد فوراً متوقف می‌شود."""
        fake_kb = tmp_path / "fake_kb"
        w_dir = fake_kb / "weeks" / "week-test"
        w_dir.mkdir(parents=True)
        (w_dir / "overview.fa.md").write_text("# هفته آزمایشی\n\nتوضیحات", encoding="utf-8")
        (w_dir / "sources.json").write_text('{"generated_at": "2026-01-01T00:00:00+03:30"}', encoding="utf-8")
        (w_dir / "notes").mkdir()

        pset_dir = w_dir / "problem-sets"
        pset_dir.mkdir(parents=True)

        leaked_pset = {
            "title_fa": "تکلیف با راه‌حل لو رفته",
            "solution": {
                "provided": True,
                "code": "print('leaked!')"
            }
        }
        (pset_dir / "bad-problem.fa.md").write_text("---\nid: bad-problem\n---\n# راهنما", encoding="utf-8")
        (pset_dir / "bad-problem.json").write_text(json.dumps(leaked_pset), encoding="utf-8")

        out_dir = tmp_path / "out"

        with pytest.raises((RuntimeError, ValueError)) as excinfo:
            build_week(str(fake_kb), "week-test", str(out_dir), pdf=False)

        assert "solution" in str(excinfo.value).lower() or "leak" in str(excinfo.value).lower() or "منع" in str(excinfo.value) or "refusing" in str(excinfo.value).lower()


class TestDynamicDownloadsFeatureFlag:
    def test_feature_flag_resolution(self, app):
        with app.app_context():
            app.config["KB_DOWNLOADS_DYNAMIC"] = True
            assert downloads_service.is_dynamic_downloads_enabled() is True

            app.config["KB_DOWNLOADS_DYNAMIC"] = False
            assert downloads_service.is_dynamic_downloads_enabled() is False


class TestAdminRebuildDownloads:
    def test_student_cannot_rebuild(self, client, student):
        client.post("/login", data={"username": "dl_student", "password": "pw123"})
        resp = client.post("/admin/kb-packages/rebuild-downloads")
        # دانش‌آموز غیرادمین باید به صفحه ورود/خطا هدایت شود
        assert resp.status_code in (302, 403)

    def test_admin_rebuild_success(self, client, admin, monkeypatch):
        # از monkeypatch استفاده می‌کنیم تا تست یونیت در کسری از ثانیه اجرا شود
        called = []
        def mock_build_all(force=True):
            called.append(True)
            return {"status": "success", "weeks": {"week-06": {}}, "pdf_engine": "mock"}

        monkeypatch.setattr(downloads_service, "build_all_downloads", mock_build_all)

        client.post("/login", data={"username": "dl_admin", "password": "adminpw"})
        resp = client.post("/admin/kb-packages/rebuild-downloads", follow_redirects=True)
        assert resp.status_code == 200
        assert len(called) == 1
