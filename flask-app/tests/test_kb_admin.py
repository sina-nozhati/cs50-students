"""آزمون‌های سرویس و روت‌های مدیریت بسته‌های پایگاه دانش (KB Admin & Upload)."""
import io
import json
import tarfile
from pathlib import Path
from werkzeug.security import generate_password_hash

import pytest
from app import db
from app.models import User
from app.services import kb_admin


@pytest.fixture
def admin_client(client, app):
    """کلاینت تست با کاربر لاگین‌شده ادمین."""
    with app.app_context():
        admin = User.query.filter_by(username="admin_tester").first()
        if not admin:
            admin = User(
                username="admin_tester",
                password_hash=generate_password_hash("admin_pass_123"),
                is_admin=True,
            )
            db.session.add(admin)
            db.session.commit()
        admin_id = admin.id

    with client.session_transaction() as sess:
        sess["_user_id"] = str(admin_id)
    return client


class TestKbAdminService:
    def test_get_all_weeks_kb_status(self, app):
        with app.app_context():
            statuses = kb_admin.get_all_weeks_kb_status()
            assert len(statuses) >= 11
            w0 = next(s for s in statuses if s["number"] == 0)
            assert w0["has_fa_hub"] is True
            assert w0["notes_count"] >= 16
            assert w0["flashcards_count"] >= 40
            assert w0["quiz_count"] >= 40

            w1 = next(s for s in statuses if s["number"] == 1)
            assert w1["has_fa_hub"] is True
            assert w1["notes_count"] == 19
            assert w1["flashcards_count"] == 66
            assert w1["quiz_count"] == 62

    def test_inspect_archive_valid_tar(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            archive_path = Path(td) / "test_week02.tar.gz"
            with tarfile.open(archive_path, "w:gz") as tar:
                note_content = b"# Note 1\nSome note"
                ti = tarfile.TarInfo(name="week-02/notes/01-test.fa.md")
                ti.size = len(note_content)
                tar.addfile(ti, io.BytesIO(note_content))

                ov_content = b"# Overview"
                ti2 = tarfile.TarInfo(name="week-02/overview.fa.md")
                ti2.size = len(ov_content)
                tar.addfile(ti2, io.BytesIO(ov_content))

            info = kb_admin.inspect_archive(archive_path)
            assert info["valid"] is True
            assert info["week_number"] == 2
            assert info["has_notes"] is True
            assert info["has_overview"] is True
            assert info["is_tar"] is True

    def test_inspect_archive_invalid_format(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            bad_file = Path(td) / "bad.txt"
            bad_file.write_text("not an archive")
            info = kb_admin.inspect_archive(bad_file)
            assert info["valid"] is False
            assert "فرمت" in info["error"]

    def test_inspect_archive_ai_and_final_project(self):
        import tempfile, zipfile
        with tempfile.TemporaryDirectory() as td:
            # تست بسته هوش مصنوعی (week-ai / 71)
            ai_zip = Path(td) / "cs50x-anzali-kb-week-ai.zip"
            with zipfile.ZipFile(ai_zip, "w") as zf:
                zf.writestr("week-ai/curriculum.json", json.dumps({"week": 71, "week_slug": "week-ai"}))
                zf.writestr("week-ai/overview.fa.md", "# هوش مصنوعی")
            info_ai = kb_admin.inspect_archive(ai_zip)
            assert info_ai["valid"] is True
            assert info_ai["week_number"] == 71
            assert info_ai["week_dir"] == "week-ai"

            # تست بسته پروژه نهایی (final-project / 99)
            fp_zip = Path(td) / "cs50x-anzali-kb-final-project.zip"
            with zipfile.ZipFile(fp_zip, "w") as zf:
                zf.writestr("final-project/curriculum.json", json.dumps({"week": 99, "week_slug": "final-project"}))
                zf.writestr("final-project/overview.fa.md", "# پروژه نهایی")
            info_fp = kb_admin.inspect_archive(fp_zip)
            assert info_fp["valid"] is True
            assert info_fp["week_number"] == 99
            assert info_fp["week_dir"] == "final-project"


class TestKbAdminRoutes:
    def test_kb_packages_dashboard_access_denied_for_guest(self, client):
        resp = client.get("/admin/kb-packages")
        assert resp.status_code in (302, 401, 403)

    def test_kb_packages_dashboard_renders_for_admin(self, admin_client):
        resp = admin_client.get("/admin/kb-packages")
        assert resp.status_code == 200
        html = resp.get_data(as_text=True)
        assert "بسته‌های هفتگی پایگاه دانش" in html
        assert "پوشش فارسی هفته‌ها" in html
        assert "هفته 0" in html
        assert "هفته 1" in html

    def test_kb_packages_upload_rejects_empty(self, admin_client):
        resp = admin_client.post("/admin/kb-packages/upload", data={}, follow_redirects=True)
        assert resp.status_code == 200
        html = resp.get_data(as_text=True)
        assert "لطفاً یک فایل فشرده" in html

    def test_kb_packages_upload_rejects_invalid_extension(self, admin_client):
        data = {
            "package_file": (io.BytesIO(b"dummy text"), "test.txt"),
        }
        resp = admin_client.post("/admin/kb-packages/upload", data=data, follow_redirects=True)
        assert resp.status_code == 200
        html = resp.get_data(as_text=True)
        assert "فرمت فایل معتبر نیست" in html
