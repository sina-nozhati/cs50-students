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

        # تست نمایش سند فارسی و آکاردئون انگلیسی
        fa_doc = client.get("/kb/d/w00-n01")
        assert fa_doc.status_code == 200
        assert "نسخهٔ فارسی CS50x Anzali".encode("utf-8") in fa_doc.data
        assert "متن اصلی (English)".encode("utf-8") in fa_doc.data

        # تست صفحهٔ هفتهٔ ۰ با محتوای فارسی
        w0 = client.get("/kb/week/0")
        assert w0.status_code == 200
        assert "یادداشت‌های درس".encode("utf-8") in w0.data
        assert "w00-n01".encode("utf-8") in w0.data
        assert "w00-ps-scratch".encode("utf-8") in w0.data


class TestPhase1Enhancements:
    def test_week0_persian_payload(self):
        payload = kb_service.week_payload(0)
        assert payload is not None
        assert payload["has_fa"] is True
        assert len(payload["fa_notes"]) == 16
        assert payload["rendered_fa_overview"] is not None
        assert payload["rendered_fa_summary"] is not None
        assert payload["fa_pset"] is not None
        assert payload["fa_pset"]["id"] == "w00-ps-scratch"

    def test_counterpart_pairing(self):
        doc_fa = kb_service.get_document("w00-ps-scratch")
        assert doc_fa is not None
        assert doc_fa["is_fa"] is True
        assert doc_fa["counterpart"] is not None
        assert doc_fa["counterpart"]["id"] == "pset-0-scratch"

        doc_en = kb_service.get_document("pset-0-scratch")
        assert doc_en is not None
        assert doc_en["is_fa"] is False
        assert doc_en["counterpart"] is not None
        assert doc_en["counterpart"]["id"] == "w00-ps-scratch"

    def test_md_render_callouts_and_links(self):
        sample = """
> [!NOTE]
> این یک نکته مهم است.

> [!WARNING]
> این یک هشدار است.

[Official Site](https://cs50.harvard.edu)
[Internal Link](/kb/week/0)

```mermaid
graph TD
  A --> B
```
"""
        html = md_render.render_markdown(sample)
        # بررسی خروجی Callout
        assert "kb-callout" in html
        assert "kb-callout-note" in html
        assert "kb-callout-warning" in html

        # بررسی target="_blank" برای لینک‌های خارجی
        assert 'target="_blank"' in html
        assert 'rel="noopener noreferrer"' in html
        # بررسی اینکه لینک‌های داخلی target="_blank" نگرفته‌اند
        assert '<a href="/kb/week/0">' in html or '<a href="/kb/week/0" >' in html

        # بررسی وجود fallback متنی برای دیاگرام mermaid
        assert "kb-mermaid-fallback" in html
        assert "A --&gt; B" in html or "A --> B" in html


class TestInteractiveKbFeatures:
    def test_siblings_navigation(self):
        doc1 = kb_service.get_document("w00-n01")
        assert doc1 is not None
        nav1 = doc1.get("siblings_nav")
        assert nav1 is not None
        assert nav1["prev"] is None
        assert nav1["next"] is not None
        assert nav1["next"]["id"] == "w00-n02"
        assert nav1["current_index"] == 1
        assert nav1["total_count"] == 16

        doc2 = kb_service.get_document("w00-n02")
        assert doc2 is not None
        nav2 = doc2.get("siblings_nav")
        assert nav2 is not None
        assert nav2["prev"]["id"] == "w00-n01"
        assert nav2["next"]["id"] == "w00-n03"
        assert nav2["current_index"] == 2

    def test_interactive_service_loaders(self, app):
        from app.services import kb_interactive
        cards = kb_interactive.load_flashcards_for_week(0)
        assert len(cards) > 0
        assert "front_fa" in cards[0]
        assert "back_fa" in cards[0]

        quizzes = kb_interactive.load_quizzes_for_week(0)
        assert len(quizzes) > 0
        assert "prompt_fa" in quizzes[0]

        glossary = kb_interactive.load_glossary_for_week(0)
        assert len(glossary) > 0
        assert "fa" in glossary[0]
        assert "en" in glossary[0]

        faqs = kb_interactive.load_faqs_for_week(0)
        assert len(faqs) > 0
        assert "q" in faqs[0]
        assert "a" in faqs[0]

    def test_quiz_submission_and_scoring(self, app, client):
        with app.app_context():
            u = User(username="quiz_student", password_hash=generate_password_hash("pw"))
            db.session.add(u)
            db.session.add(Week(number=0, title="Scratch", is_published=True))
            db.session.commit()
            uid = u.id

        client.post("/login", data={"username": "quiz_student", "password": "pw"})

        # ارسال پاسخ صحیح به اولین سوال (w00-q-001 پاسخ صحیح 'a' است: CS50 Duck)
        res = client.post("/kb/week/0/quiz/submit", data={"question_id": "w00-q-001", "answer": "a"})
        assert res.status_code == 200
        json_data = res.get_json()
        assert json_data["success"] is True
        assert json_data["is_correct"] is True
        assert json_data["current_score"] >= 1

        # ارسال مرور فلش‌کارت
        fc_res = client.post("/kb/week/0/flashcard/review", data={"card_id": "w00-fc-001", "rating": "good"})
        assert fc_res.status_code == 200
        fc_json = fc_res.get_json()
        assert fc_json["success"] is True
        assert fc_json["box_number"] == 2
