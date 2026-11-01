"""سرویس مدیریت و آپلود بسته‌های پایگاه دانش (KB Package Ingestion).

این ماژول امکان آپلود فایل‌های فشرده (.tar.gz, .tgz, .tar, .zip) بسته‌های هفتگی
پایگاه دانش CS50x Anzali را در پنل ادمین فراهم می‌کند:
1. اعتبارسنجی ساختار بسته و استخراج هوشمند شماره هفته
2. استخراج فایل‌های هفته در docs/cs50x-kb/anzali-fa/weeks/week-XX/
3. ادغام اصطلاحات جدید در glossary.fa.json بدون از بین بردن اصطلاحات قبلی
4. به‌روزرسانی learning-map.json
5. ادغام امن نودها و الصاق‌ها از index.fragment.json در index.json اصلی
6. پاک‌سازی کش درون‌حافظه‌ای kb_repo و همگام‌سازی وضعیت در دیتابیس
"""
from __future__ import annotations

import copy
import json
import os
import re
import shutil
import tarfile
import tempfile
import zipfile
from pathlib import Path
from typing import Any

from app import db
from app.content import kb_repo
from app.models import Week


def _get_kb_root() -> Path:
    """مسیر ریشه docs/cs50x-kb."""
    return kb_repo.kb_root()


def _get_anzali_root() -> Path:
    """مسیر ریشه docs/cs50x-kb/anzali-fa."""
    return _get_kb_root() / "anzali-fa"


def _is_safe_path(base: Path, target: Path) -> bool:
    """بررسی ایمنی مسیر برای جلوگیری از حملات Zip Slip / Path Traversal."""
    try:
        target.resolve().relative_to(base.resolve())
        return True
    except (ValueError, RuntimeError):
        return False


def inspect_archive(archive_path: Path | str) -> dict[str, Any]:
    """بررسی محتویات فایل فشرده بدون اعمال تغییرات دائمی."""
    archive_path = Path(archive_path)
    if not archive_path.is_file():
        return {"valid": False, "error": f"فایل یافت نشد: {archive_path}"}

    members: list[str] = []
    is_tar = tarfile.is_tarfile(archive_path)
    is_zip = zipfile.is_zipfile(archive_path)

    if not is_tar and not is_zip:
        return {"valid": False, "error": "فرمت فایل نامعتبر است. فرمت‌های مجاز: .tar.gz, .tgz, .tar, .zip"}

    if is_tar:
        try:
            with tarfile.open(archive_path, "r:*") as tar:
                members = tar.getnames()
        except Exception as e:
            return {"valid": False, "error": f"خطا در باز کردن فایل tar: {e}"}
    elif is_zip:
        try:
            with zipfile.ZipFile(archive_path, "r") as zf:
                members = zf.namelist()
        except Exception as e:
            return {"valid": False, "error": f"خطا در باز کردن فایل zip: {e}"}

    def _read_member_text(member_name: str) -> str | None:
        try:
            if is_tar:
                with tarfile.open(archive_path, "r:*") as tar:
                    f = tar.extractfile(member_name)
                    if f:
                        return f.read().decode("utf-8", errors="replace")
            elif is_zip:
                with zipfile.ZipFile(archive_path, "r") as zf:
                    return zf.read(member_name).decode("utf-8", errors="replace")
        except Exception:
            pass
        return None

    # تشخیص هوشمند شماره و اسلاگ هفته
    week_match = None
    week_number = None
    detected_week_dir = None

    # ۱. استخراج از مانیفست‌های معتبر داخل بسته (curriculum.json / index.fragment.json)
    for m in members:
        if m.endswith("curriculum.json"):
            content = _read_member_text(m)
            if content:
                try:
                    data = json.loads(content)
                    w = data.get("week") if data.get("week") is not None else data.get("panel_week_number")
                    if w is not None:
                        week_number = int(w)
                        detected_week_dir = data.get("week_slug") or kb_repo.get_week_folder_slug(week_number)
                        break
                except Exception:
                    pass

    if week_number is None:
        for m in members:
            if m.endswith("index.fragment.json"):
                content = _read_member_text(m)
                if content:
                    try:
                        data = json.loads(content)
                        w = data.get("week")
                        if w is not None:
                            week_number = int(w)
                            detected_week_dir = data.get("week_slug") or kb_repo.get_week_folder_slug(week_number)
                            break
                    except Exception:
                        pass

    # ۲. تشخیص از نام پوشه در آرشیو
    if week_number is None:
        for m in members:
            m_ai = re.search(r"(?:^|/)(?:weeks/)?(week-ai)(?:/|$)", m)
            if m_ai:
                week_number = 71
                detected_week_dir = "week-ai"
                break
            m_fp = re.search(r"(?:^|/)(?:weeks/)?(final-project)(?:/|$)", m)
            if m_fp:
                week_number = 99
                detected_week_dir = "final-project"
                break
            match = re.search(r"(?:^|/)(?:weeks/)?(week-(\d+))(?:/|$)", m)
            if match:
                week_number = int(match.group(2))
                detected_week_dir = kb_repo.get_week_folder_slug(week_number)
                break

    # ۳. تشخیص از نام فایل آرشیو
    if week_number is None:
        fname = archive_path.name.lower()
        if "week-ai" in fname or "-ai" in fname or "_ai" in fname:
            week_number = 71
            detected_week_dir = "week-ai"
        elif "final-project" in fname or "final_project" in fname or "final" in fname:
            week_number = 99
            detected_week_dir = "final-project"
        else:
            file_match = re.search(r"week[-_]?(\d+)", fname)
            if file_match:
                week_number = int(file_match.group(1))
                detected_week_dir = kb_repo.get_week_folder_slug(week_number)

    # بررسی وجود فایل‌های کلیدی
    has_notes = any("notes/" in m and m.endswith((".md", ".fa.md")) for m in members)
    has_flashcards = any("flashcards.json" in m for m in members)
    has_quizzes = any("quizzes.json" in m for m in members)
    has_challenges = any("challenges.json" in m for m in members)
    has_overview = any("overview.fa.md" in m or "overview.md" in m for m in members)
    has_summary = any("summary.fa.md" in m or "summary.md" in m for m in members)
    has_sources = any("sources.json" in m for m in members)
    has_fragment = any("index.fragment.json" in m for m in members)

    return {
        "valid": bool(has_notes or has_overview or has_summary),
        "archive_name": archive_path.name,
        "week_number": week_number,
        "week_dir": detected_week_dir,
        "total_files": len(members),
        "has_notes": has_notes,
        "has_flashcards": has_flashcards,
        "has_quizzes": has_quizzes,
        "has_challenges": has_challenges,
        "has_overview": has_overview,
        "has_summary": has_summary,
        "has_sources": has_sources,
        "has_fragment": has_fragment,
        "is_tar": is_tar,
        "is_zip": is_zip,
    }


def validate_quiz_schema(data: dict[str, Any]) -> list[str]:
    """اعتبارسنجی ساختار آزمون‌ها و اطمینان از کامل بودن داده‌های هر سوال."""
    errors = []
    items = data.get("items") or data.get("questions") or []
    if not items:
        errors.append("فایل quizzes.json فاقد آرایه سوالات (items) است.")
        return errors

    for idx, q in enumerate(items):
        qid = q.get("id") or f"index_{idx}"
        qtype = q.get("type", "mcq")
        if not q.get("prompt_fa"):
            errors.append(f"سوال {qid}: متن فارسی صورت سوال (prompt_fa) تعریف نشده است.")

        if qtype == "mcq":
            options = q.get("options") or []
            if len(options) < 2:
                errors.append(f"سوال چهارگزینه‌ای {qid}: باید حداقل دارای ۲ گزینه باشد.")
            ans = q.get("answer", {})
            if not ans.get("correct_option_ids"):
                errors.append(f"سوال چهارگزینه‌ای {qid}: کلید پاسخ صحیح (correct_option_ids) ندارد.")

        elif qtype == "parsons":
            lines = q.get("lines") or q.get("scrambled_lines") or []
            if not lines:
                errors.append(f"سوال چیدمان پارسونز {qid}: فاقد خطوط کد (lines) است.")
            ans = q.get("answer", {})
            if not (ans.get("order") or ans.get("correct_order")):
                errors.append(f"سوال پارسونز {qid}: ترتیب صحیح خطوط (answer.order) مشخص نیست.")

        elif qtype == "predict_output":
            code = q.get("code")
            if not code or not str(code).strip():
                errors.append(f"سوال پیش‌بینی خروجی {qid}: فاقد قطعه‌کد برای پیش‌بینی (code) است.")
            ans = q.get("answer", {})
            if not (ans.get("accept") or ans.get("value")):
                errors.append(f"سوال پیش‌بینی خروجی {qid}: فاقد پاسخ‌های معتبر (answer.accept) است.")

    return errors


def validate_challenges_schema(data: dict[str, Any]) -> list[str]:
    """اعتبارسنجی ساختار چالش‌های تعاملی ۵ دقیقه‌ای (Duo-Style)."""
    errors = []
    challenges = data.get("challenges", [])
    if not challenges:
        errors.append("فایل challenges.json فاقد آرایه چالش‌ها (challenges) است.")
        return errors

    for idx, ch in enumerate(challenges):
        cid = ch.get("id") or f"ch_{idx}"
        ctype = ch.get("type")
        if not ch.get("title") or not ch.get("instruction"):
            errors.append(f"چالش {cid}: عنوان یا دستورالعمل چالش ناقص است.")

        if ctype == "token_tap":
            if not ch.get("token_bank") or not ch.get("expected_answer"):
                errors.append(f"چالش توکن‌چینی {cid}: فاقد بانک توکن یا پاسخ موردانتظار است.")
        elif ctype == "parsons":
            if not ch.get("scrambled_lines") or not ch.get("correct_order"):
                errors.append(f"چالش مرتب‌سازی {cid}: فاقد خطوط درهم یا ترتیب صحیح است.")
        elif ctype == "spot_bug":
            if not ch.get("code_lines") or ch.get("bug_line_index") is None:
                errors.append(f"چالش شکار باگ {cid}: فاقد خطوط کد یا شماره خط باگ است.")

    return errors


def install_kb_package(archive_path: Path | str, target_week: int | None = None) -> dict[str, Any]:
    """استخراج و نصب کامل بسته آموزشی یک هفته در پایگاه دانش انزلی."""
    archive_path = Path(archive_path)
    info = inspect_archive(archive_path)
    if not info.get("valid"):
        return {
            "success": False,
            "error": info.get("error") or "بسته فاقد محتوای معتبر آموزشی (یادداشت‌ها یا نمای کلی) است.",
        }

    week = target_week if target_week is not None else info.get("week_number")
    if week is None:
        return {"success": False, "error": "شماره هفته مشخص نشده و از بسته قابل استخراج نیست."}

    kb_root = _get_kb_root()
    anzali_root = _get_anzali_root()
    dest_slug = info.get("week_dir") or kb_repo.get_week_folder_slug(week)
    dest_week_dir = anzali_root / "weeks" / dest_slug
    dest_week_dir.mkdir(parents=True, exist_ok=True)

    extracted_notes = 0
    extracted_flashcards = 0
    extracted_quizzes = 0
    glossary_updated = 0
    learning_map_updated = False
    index_nodes_merged = 0

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        # ۱. استخراج در دایرکتوری موقت
        if info["is_tar"]:
            with tarfile.open(archive_path, "r:*") as tar:
                # بررسی ایمنی path traversal
                for member in tar.getmembers():
                    member_path = (tmp_path / member.name).resolve()
                    if not _is_safe_path(tmp_path, member_path):
                        return {"success": False, "error": "تشخیص مسیر ناامن در فایل آرشیو (Zip Slip)."}
                tar.extractall(tmp_path)
        else:
            with zipfile.ZipFile(archive_path, "r") as zf:
                for member in zf.namelist():
                    member_path = (tmp_path / member).resolve()
                    if not _is_safe_path(tmp_path, member_path):
                        return {"success": False, "error": "تشخیص مسیر ناامن در فایل آرشیو (Zip Slip)."}
                zf.extractall(tmp_path)

        # ۲. یافتن ریشه پوشه هفته در دایرکتوری موقت
        src_week_path = None
        candidates = [dest_slug, f"week-{week:02d}", f"week-{week}"]
        if week == 71:
            candidates.extend(["week-ai", "week-71", "ai"])
        elif week == 99:
            candidates.extend(["final-project", "week-99", "project"])

        for r, dirs, files in os.walk(tmp_path):
            bname = os.path.basename(r)
            if bname in candidates and ("notes" in dirs or "overview.fa.md" in files or "flashcards.json" in files or "curriculum.json" in files):
                src_week_path = Path(r)
                break

        # در صورتی که با نام پوشه پیدا نشد، پوشه‌ای که فایل‌های اصلی هفته را دارد بیاب
        if not src_week_path:
            for r, dirs, files in os.walk(tmp_path):
                if "overview.fa.md" in files or "summary.fa.md" in files or "notes" in dirs or "flashcards.json" in files or "curriculum.json" in files:
                    src_week_path = Path(r)
                    break

        if src_week_path and src_week_path.is_dir():
            # کپی تمام محتویات پوشه هفته به مقصد
            for item in src_week_path.iterdir():
                dest_item = dest_week_dir / item.name
                if item.is_dir():
                    if dest_item.exists():
                        shutil.rmtree(dest_item)
                    shutil.copytree(item, dest_item)
                else:
                    shutil.copy2(item, dest_item)

        # پاک‌سازی پوشه خالی قبلی اگر نام متفاوتی داشته (مثل week-71 در برابر week-ai)
        if dest_slug == "week-ai":
            old_empty = anzali_root / "weeks" / "week-71"
            if old_empty.is_dir() and not any(old_empty.iterdir()):
                try:
                    old_empty.rmdir()
                except Exception:
                    pass
        elif dest_slug == "final-project":
            old_empty = anzali_root / "weeks" / "week-99"
            if old_empty.is_dir() and not any(old_empty.iterdir()):
                try:
                    old_empty.rmdir()
                except Exception:
                    pass

        # شمارش فایل‌های نصب‌شده در هفته
        notes_dir = dest_week_dir / "notes"
        if notes_dir.is_dir():
            extracted_notes = len(list(notes_dir.glob("*.md")))

        fc_file = dest_week_dir / "flashcards.json"
        if fc_file.is_file():
            try:
                with open(fc_file, encoding="utf-8") as f:
                    fc_data = json.load(f)
                    extracted_flashcards = len(fc_data.get("cards", []))
            except Exception:
                pass

        qz_file = dest_week_dir / "quizzes.json"
        if qz_file.is_file():
            try:
                with open(qz_file, encoding="utf-8") as f:
                    qz_data = json.load(f)
                    extracted_quizzes = len(qz_data.get("items", [])) or len(qz_data.get("questions", []))
            except Exception:
                pass

        ch_file = dest_week_dir / "challenges.json"
        extracted_challenges = 0
        if ch_file.is_file():
            try:
                with open(ch_file, encoding="utf-8") as f:
                    ch_data = json.load(f)
                    extracted_challenges = len(ch_data.get("challenges", []))
            except Exception:
                pass

        # ۳. ادغام واژه‌نامه (Glossary)
        curriculum_dest = anzali_root / "curriculum"
        curriculum_dest.mkdir(parents=True, exist_ok=True)
        tmp_glossary = None
        for r, dirs, files in os.walk(tmp_path):
            if "glossary.fa.json" in files:
                tmp_glossary = Path(r) / "glossary.fa.json"
                break

        if tmp_glossary and tmp_glossary.is_file():
            dest_glossary = curriculum_dest / "glossary.fa.json"
            glossary_updated = _merge_glossary(dest_glossary, tmp_glossary)

        # ۴. به‌روزرسانی learning-map.json
        tmp_lmap = None
        for r, dirs, files in os.walk(tmp_path):
            if "learning-map.json" in files:
                tmp_lmap = Path(r) / "learning-map.json"
                break

        if tmp_lmap and tmp_lmap.is_file():
            dest_lmap = curriculum_dest / "learning-map.json"
            shutil.copy2(tmp_lmap, dest_lmap)
            learning_map_updated = True

        # ۵. ادغام index.fragment.json
        tmp_fragment = None
        for r, dirs, files in os.walk(tmp_path):
            if "index.fragment.json" in files:
                tmp_fragment = Path(r) / "index.fragment.json"
                break

        dest_index = kb_root / "index.json"
        if dest_index.is_file():
            if tmp_fragment and tmp_fragment.is_file():
                index_nodes_merged = _merge_fragment_into_index(dest_index, tmp_fragment, week)
            else:
                # ایجاد نودهای پایه‌ای در صورت نبود fragment اختصاصی
                index_nodes_merged = _ensure_basic_index_nodes(dest_index, week, dest_week_dir)

    # ۶. پاک‌سازی کش درون حافظه‌ای kb_repo
    kb_repo.clear_cache()

    # ۷. همگام‌سازی وضعیت انتشار در دیتابیس
    try:
        week_row = Week.query.filter_by(number=week).first()
        if not week_row:
            week_title = f"هفته {week}"
            week_row = Week(number=week, title=week_title, is_published=True)
            db.session.add(week_row)
        else:
            week_row.is_published = True
        db.session.commit()
    except Exception:
        db.session.rollback()

    return {
        "success": True,
        "week": week,
        "notes_count": extracted_notes,
        "flashcards_count": extracted_flashcards,
        "quiz_count": extracted_quizzes,
        "challenges_count": extracted_challenges,
        "glossary_count": glossary_updated,
        "learning_map_updated": learning_map_updated,
        "index_nodes_merged": index_nodes_merged,
    }


def _merge_glossary(dest_path: Path, new_path: Path) -> int:
    """ادغام اصطلاحات تخصصی در glossary.fa.json بدون ایجاد رکورد تکراری."""
    existing_terms: list[dict[str, Any]] = []
    base_data: dict[str, Any] = {}

    if dest_path.is_file():
        try:
            with open(dest_path, encoding="utf-8") as f:
                base_data = json.load(f)
                existing_terms = base_data.get("terms", [])
        except Exception:
            pass

    try:
        with open(new_path, encoding="utf-8") as f:
            new_data = json.load(f)
            incoming_terms = new_data.get("terms", [])
    except Exception:
        return len(existing_terms)

    # ایندکس کردن بر اساس term_en یا id
    by_key = {t.get("term_en", "").strip().lower() or t.get("id"): t for t in existing_terms}

    for term in incoming_terms:
        key = term.get("term_en", "").strip().lower() or term.get("id")
        if key:
            if key in by_key:
                by_key[key].update(term)
            else:
                by_key[key] = term

    merged_terms = list(by_key.values())
    base_data["terms"] = merged_terms
    base_data["count"] = len(merged_terms)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        json.dump(base_data, f, ensure_ascii=False, indent=2)

    return len(merged_terms)


def _merge_fragment_into_index(index_path: Path, fragment_path: Path, week_number: int) -> int:
    """ادغام نودها و الحاقات یک fragment در index.json اصلی."""
    with open(index_path, encoding="utf-8") as f:
        idx = json.load(f)

    with open(fragment_path, encoding="utf-8") as f:
        frag = json.load(f)

    byid = {n["id"]: n for n in idx["nodes"]}
    merged_count = 0

    # ۱. به‌روزرسانی یا افزودن نودها
    for n in frag.get("nodes", []):
        nid = n["id"]
        if nid in byid:
            byid[nid].update(n)
        else:
            new_node = copy.deepcopy(n)
            idx["nodes"].append(new_node)
            byid[nid] = new_node
            merged_count += 1

    # ۲. الحاق فرزندان به والد (attach_to)
    for att in frag.get("attach_to", []):
        pid = att.get("parent_id")
        cid = att.get("append_child")
        parent = byid.get(pid)
        if parent:
            parent.setdefault("children", [])
            if cid not in parent["children"]:
                parent["children"].append(cid)

    # ۳. اعمال بازنویسی خلاصه هفته (week_summary_overrides)
    for ov in frag.get("week_summary_overrides", []):
        nid = ov.get("node_id")
        node = byid.get(nid)
        if node and ov.get("path"):
            node["path"] = ov.get("path")

    # ۴. تضمین الصاق هاب فارسی هفته wXX-fa به week-X در صورتی که در attach_to نیامده باشد
    hub_id = f"w{week_number:02d}-fa"
    week_node_id = kb_repo.get_week_node_id(week_number)
    week_node = byid.get(week_node_id) or byid.get(f"week-{week_number}")
    if week_node and hub_id in byid:
        week_node.setdefault("children", [])
        if hub_id not in week_node["children"]:
            week_node["children"].append(hub_id)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)

    return merged_count


def _ensure_basic_index_nodes(index_path: Path, week: int, week_dir: Path) -> int:
    """در صورت عدم وجود index.fragment.json، نودهای استانداردی برای هفته در index.json می‌سازد."""
    with open(index_path, encoding="utf-8") as f:
        idx = json.load(f)

    byid = {n["id"]: n for n in idx["nodes"]}
    hub_id = f"w{week:02d}-fa"
    slug = week_dir.name
    added = 0

    if hub_id not in byid:
        hub_node = {
            "id": hub_id,
            "type": "anzali-week-hub",
            "title": f"هفته {week} — راهنمای جامع فارسی",
            "path": f"anzali-fa/weeks/{slug}/overview.fa.md",
            "lang": "fa",
            "week": week,
            "children": [],
        }
        idx["nodes"].append(hub_node)
        byid[hub_id] = hub_node
        added += 1

    # اضافه کردن فرزندان notes
    notes_dir = week_dir / "notes"
    if notes_dir.is_dir():
        hub_node = byid[hub_id]
        for note_file in sorted(notes_dir.glob("*.fa.md")):
            # استخراج شماره مثلاً 01 از 01-welcome.fa.md
            prefix_match = re.match(r"^(\d+)", note_file.name)
            note_order = int(prefix_match.group(1)) if prefix_match else 99
            note_id = f"w{week:02d}-n{note_order:02d}"
            if note_id not in byid:
                n_node = {
                    "id": note_id,
                    "type": "anzali-note",
                    "title": note_file.stem.replace(".fa", "").replace("-", " ").capitalize(),
                    "path": f"anzali-fa/weeks/{slug}/notes/{note_file.name}",
                    "lang": "fa",
                    "order": note_order,
                    "week": week,
                }
                idx["nodes"].append(n_node)
                byid[note_id] = n_node
                if note_id not in hub_node.get("children", []):
                    hub_node.setdefault("children", []).append(note_id)
                added += 1

    # الحاق به week-X
    week_node_id = kb_repo.get_week_node_id(week)
    week_node = byid.get(week_node_id) or byid.get(f"week-{week}")
    if week_node:
        week_node.setdefault("children", [])
        if hub_id not in week_node["children"]:
            week_node["children"].append(hub_id)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)

    return added


def get_all_weeks_kb_status() -> list[dict[str, Any]]:
    """گزارش وضعیت کامل پایگاه دانش برای تمام هفته‌ها جهت نمایش در پنل ادمین."""
    anzali_root = _get_anzali_root()
    weeks_from_db = {w.number: w for w in Week.query.all()}
    all_kb_weeks = kb_repo.list_weeks_ordered()
    status_report: list[dict[str, Any]] = []

    for kw in all_kb_weeks:
        week_num = kw.get("site_number")
        if week_num is None:
            continue
        db_w = weeks_from_db.get(week_num)
        title = db_w.title if db_w else (kw.get("title") or f"هفته {week_num}")
        is_published = db_w.is_published if db_w else True

        week_folder = kb_repo.get_anzali_week_dir(week_num)
        hub_node = kb_repo.anzali_hub_by_site_number(week_num)

        notes_count = 0
        notes_dir = week_folder / "notes"
        if notes_dir.is_dir():
            notes_count = len(list(notes_dir.glob("*.md")))

        flashcards_count = 0
        fc_file = week_folder / "flashcards.json"
        if fc_file.is_file():
            try:
                with open(fc_file, encoding="utf-8") as f:
                    fc_data = json.load(f)
                    flashcards_count = len(fc_data.get("cards", []))
            except Exception:
                pass

        quiz_count = 0
        qz_file = week_folder / "quizzes.json"
        if qz_file.is_file():
            try:
                with open(qz_file, encoding="utf-8") as f:
                    qz_data = json.load(f)
                    quiz_count = len(qz_data.get("items", [])) or len(qz_data.get("questions", []))
            except Exception:
                pass

        challenges_count = 0
        ch_file = week_folder / "challenges.json"
        if ch_file.is_file():
            try:
                with open(ch_file, encoding="utf-8") as f:
                    ch_data = json.load(f)
                    challenges_count = len(ch_data.get("challenges", []))
            except Exception:
                pass

        status_report.append({
            "number": week_num,
            "title": title,
            "is_published": is_published,
            "has_fa_hub": hub_node is not None,
            "notes_count": notes_count,
            "flashcards_count": flashcards_count,
            "quiz_count": quiz_count,
            "challenges_count": challenges_count,
            "has_challenges": challenges_count > 0,
            "has_folder": week_folder.is_dir(),
            "folder_path": str(week_folder) if week_folder.is_dir() else None,
        })

    return status_report
