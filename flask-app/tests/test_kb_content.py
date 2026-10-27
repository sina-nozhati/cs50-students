"""تست بارگذاری docs/cs50x-kb و روت‌های KB."""
from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Week
from app.content import kb_repo, md_render
from app.content.loader import list_weeks, get_week, week_numbers, has_content
from app.services import kb_content as kb_service


class TestKbRepo:
    def test_weeks_and_mapping(self):
        weeks = kb_repo.list_weeks_ordered()
        nums = [w["site_number"] for w in weeks]
        assert 0 in nums and 10 in nums
        assert 71 in nums and 99 in nums
        assert nums.index(71) == nums.index(7) + 1  # AI بعد از ۷

    def test_week0_node_and_file(self):
        node = kb_repo.week_node_by_site_number(0)
        assert node is not None
        assert node["id"] == "week-0"
        path = kb_repo.resolve_path(node)
        assert path is not None and path.is_file()

    def test_ai_and_final(self):
        assert kb_repo.week_node_by_site_number(71)["id"] == "week-ai"
        assert kb_repo.week_node_by_site_number(99)["id"] == "final-project"

    def test_render_splits_sections(self):
        node = kb_repo.get_node("week-0")
        path = kb_repo.resolve_path(node)
        rendered = md_render.load_and_render(path)
        assert rendered["has_official"] or rendered["full_html"]
        # week.md معمولاً هر دو بخش را دارد
        assert "Scratch" in rendered["full_html"] or "scratch" in rendered["full_html"].lower()


class TestLoaderCompat:
    def test_catalog_and_payload(self):
        assert has_content(0)
        assert len(week_numbers()) >= 12
        w = get_week(0)
        assert w is not None
        assert w["id"] == "week-0"
        assert w["children"]

    def test_cs50x_2026_weeks_thin_wrap(self):
        from app.content.cs50x_2026 import WEEKS

        nums = list(WEEKS.keys())
        assert nums == [w["site_number"] for w in kb_repo.list_weeks_ordered()]
        assert WEEKS[0]["slug"] == "week-0"
        assert WEEKS[71]["number"] == 71
        assert WEEKS[99]["id"] == "final-project"

    def test_render_toc(self):
        node = kb_repo.get_node("week-0")
        path = kb_repo.resolve_path(node)
        rendered = md_render.load_and_render(path)
        assert "toc" in rendered
        if rendered["toc"]:
            assert "id" in rendered["toc"][0]
            assert rendered["toc"][0]["text"]


class TestKbRoutes:
    def test_index_hub_doc(self, app, client):
        with app.app_context():
            u = User(
                username="kbuser2",
                password_hash=generate_password_hash("pw"),
            )
            db.session.add(u)
            for n, title in [(0, "Scratch"), (71, "AI"), (1, "C hidden")]:
                pub = n != 1
                db.session.add(Week(number=n, title=title, is_published=pub))
            db.session.commit()

        client.post("/login", data={"username": "kbuser2", "password": "pw"})

        idx = client.get("/kb/")
        assert idx.status_code == 200
        assert "پایگاه دانش".encode("utf-8") in idx.data

        hub = client.get("/kb/week/0")
        assert hub.status_code == 200
        assert b"lecture" in hub.data.lower() or "Lecture".encode() in hub.data

        doc = client.get("/kb/d/week-0-lecture")
        assert doc.status_code == 200
        assert b"OFFICIAL" in doc.data or b"official" in doc.data.lower()

        hidden = client.get("/kb/week/1")
        assert hidden.status_code == 404

        missing = client.get("/kb/d/not-a-real-doc-id")
        assert missing.status_code == 404
