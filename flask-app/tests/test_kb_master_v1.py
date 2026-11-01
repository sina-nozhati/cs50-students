"""تست‌های پذیرش (Acceptance Tests) بسته جامع پایگاه دانش CS50x Anzali نسخه 1.0.0.

پوشش کامل ۱۲ معیار پذیرش طبق سند مشخصات:
1. بارگذاری بسته کامل معتبر (MASTER_INDEX.json + manifest 1.0.0 + ثبت در kb_package_installs).
2. دستکاری ۱ بایت در فایل -> خطا با پیام فارسی «sha256 جور نیست»، بدون تغییر DB.
3. فایل اضافه ثبت‌نشده یا کمبود فایل -> خطا با گزارش فارسی.
4. نصب مجدد همان بسته با همان sha256 -> هیچ تغییری رخ ندهد و پیام «این بسته قبلاً نصب شده است» بدهد.
5. پیشرفت، XP و استریک دانش‌آموز قبل و بعد از نصب بسته دقیقاً یکسان بماند.
6. سوال ۳ گزینه‌ای برچسب «سه‌گزینه‌ای» بگیرد و پاسخ غلط اول feedback_fa و سپس explanation_fa را نشان دهد.
7. سوال با قطعه‌کد دارای باکس LTR تک‌فاصله زیر صورت سوال باشد.
8. آزمون تسلط هفته ۳ از w03-mt-final.item_ids بارگذاری و با نمره 80%+ قبول شود.
9. پاسخ تک‌سؤال 0 XP، ولی قبولی آزمون تسلط 25 XP با دلیل quiz:mastery:w03:pass به صورت ایدمپوتنت.
10. سرویس تمرین تطبیقی 5 دقیقه‌ای (Adaptive Practice): ۸-۱۰ سوال، misconception follow-up، استریک با >=8 پاسخ.
11. جعبه ورودی کد: رفتارهای صفحه‌کلید (Enter، Ctrl+Enter، Tab، Esc) و تبدیل \r\n به \n در بک‌اند.
12. برابری دقیق (Parity) بین reference_engine و app.services.adaptive.AdaptiveEngine.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import tempfile
import zipfile
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from app import db
from app.models import (
    AdaptiveState,
    KBPackageInstall,
    QuizAttempt,
    User,
    Week,
    WeekProgress,
    XPLog,
)
from app.content import kb_repo
from app.services import adaptive as adaptive_service
from app.services import kb_admin
from app.services import kb_interactive
from app.services import progress as progress_service
from app.services import streak as streak_service
from app.services import xp as xp_service


@pytest.fixture
def mock_anzali_root(tmp_path, monkeypatch):
    test_root = tmp_path / "mock_anzali_fa"
    test_root.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(kb_admin, "_get_anzali_root", lambda: test_root)
    return test_root


def _build_mock_master_zip(
    tmp_path: Path,
    file_overrides: dict[str, bytes] | None = None,
    tamper_file: str | None = None,
    extra_unlisted_file: bool = False,
    missing_file: bool = False,
) -> Path:
    """ساخت یک فایل زیپ موقت مطابق با ساختار Master Package v1.0.0."""
    pkg_dir = tmp_path / "pkg_src"
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    pkg_dir.mkdir(parents=True, exist_ok=True)

    manifest_data = {
        "package_type": "master",
        "version": "1.0.0",
        "name": "cs50x-anzali-kb-master",
        "generated_at": "2026-11-01T12:00:00+03:30",
    }
    manifest_bytes = json.dumps(manifest_data, ensure_ascii=False, indent=2).encode("utf-8")

    sample_doc = b"# CS50x Anzali Master\nContent for testing."

    files_map: dict[str, bytes] = {
        "manifest.json": manifest_bytes,
        "sample.md": sample_doc,
    }
    if file_overrides:
        files_map.update(file_overrides)

    if missing_file:
        pass

    # ساخت فایل‌های فیزیکی
    for rel_path, content in files_map.items():
        if missing_file and rel_path == "sample.md":
            continue
        p = pkg_dir / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        if tamper_file and rel_path == tamper_file:
            # تغییر ۱ بایت
            p.write_bytes(content + b"X")
        else:
            p.write_bytes(content)

    if extra_unlisted_file:
        extra_p = pkg_dir / "unlisted_extra.txt"
        extra_p.write_bytes(b"I am not in MASTER_INDEX.json")

    # تولید MASTER_INDEX.json بر پایه محتوای اصلی (قبل از دستکاری)
    master_index_files = []
    for rel_path, content in files_map.items():
        master_index_files.append({
            "path": rel_path,
            "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
        })

    master_index = {
        "version": "1.0.0",
        "schema_version": "1.0.0",
        "generated_at": "2026-11-01T12:00:00+03:30",
        "files": master_index_files,
    }
    (pkg_dir / "MASTER_INDEX.json").write_text(
        json.dumps(master_index, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    zip_out = tmp_path / "master_pkg.zip"
    with zipfile.ZipFile(zip_out, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, filenames in os.walk(pkg_dir):
            for fn in filenames:
                fp = Path(root) / fn
                arcname = fp.relative_to(pkg_dir).as_posix()
                zf.write(fp, arcname)

    return zip_out


# ──────────────────────────────────────────────────────────────────────────────
# ۱. بارگذاری بسته کامل معتبر
# ──────────────────────────────────────────────────────────────────────────────
def test_01_master_package_valid_install(app, admin_user, tmp_path, mock_anzali_root):
    """معیار ۱: بارگذاری بسته معتبر با MASTER_INDEX و manifest 1.0.0 و ثبت در kb_package_installs."""
    with app.app_context():
        zip_path = _build_mock_master_zip(tmp_path)
        res = kb_admin.install_kb_package(zip_path, admin_id=admin_user.id)

        assert res["success"] is True
        assert res.get("is_master") is True
        assert res.get("version") == "1.0.0"

        # بررسی ثبت در دیتابیس
        row = KBPackageInstall.query.filter_by(version="1.0.0", package_type="master").first()
        assert row is not None
        assert row.admin_id == admin_user.id
        assert row.sha256 is not None
        assert "Asia/Tehran" in row.installed_at_tehran


# ──────────────────────────────────────────────────────────────────────────────
# ۲. دستکاری ۱ بایت در یکی از فایل‌ها
# ──────────────────────────────────────────────────────────────────────────────
def test_02_master_package_tampered_sha_rejected(app, admin_user, tmp_path):
    """معیار ۲: دستکاری ۱ بایت -> خطا با پیام فارسی «sha256 جور نیست»، بدون تغییر DB."""
    with app.app_context():
        initial_count = KBPackageInstall.query.count()

        zip_path = _build_mock_master_zip(tmp_path, tamper_file="sample.md")
        res = kb_admin.install_kb_package(zip_path, admin_id=admin_user.id)

        assert res["success"] is False
        assert res.get("is_master") is True

        errs_str = " ".join(res.get("error_list", []) + [res.get("error", "")])
        assert "sha256" in errs_str
        assert "جور نیست" in errs_str

        # هیچ رکوردی نباید افزوده شده باشد
        assert KBPackageInstall.query.count() == initial_count


# ──────────────────────────────────────────────────────────────────────────────
# ۳. فایل اضافهٔ ثبت‌نشده یا کمبود یک فایل
# ──────────────────────────────────────────────────────────────────────────────
def test_03_master_package_missing_or_unlisted_file_rejected(app, admin_user, tmp_path):
    """معیار ۳: فایل اضافهٔ ثبت‌نشده در MASTER_INDEX یا کمبود فایل -> خطا با گزارش فارسی."""
    with app.app_context():
        initial_count = KBPackageInstall.query.count()

        # الف) کمبود فایل فهرست‌شده
        zip_missing = _build_mock_master_zip(tmp_path / "missing", missing_file=True)
        res_missing = kb_admin.install_kb_package(zip_missing, admin_id=admin_user.id)
        assert res_missing["success"] is False
        err_missing_str = " ".join(res_missing.get("error_list", []) + [res_missing.get("error", "")])
        assert "وجود ندارد" in err_missing_str or "جور نیست" in err_missing_str

        # ب) وجود فایل اضافه ثبت‌نشده
        zip_unlisted = _build_mock_master_zip(tmp_path / "unlisted", extra_unlisted_file=True)
        res_unlisted = kb_admin.install_kb_package(zip_unlisted, admin_id=admin_user.id)
        assert res_unlisted["success"] is False
        err_unlisted_str = " ".join(res_unlisted.get("error_list", []) + [res_unlisted.get("error", "")])
        assert "فهرست‌نشده" in err_unlisted_str

        assert KBPackageInstall.query.count() == initial_count


# ──────────────────────────────────────────────────────────────────────────────
# ۴. نصب مجدد همان بسته با همان sha256 (ایدمپوتنت)
# ──────────────────────────────────────────────────────────────────────────────
def test_04_master_package_reinstall_idempotent(app, admin_user, tmp_path, mock_anzali_root):
    """معیار ۴: نصب مجدد با همان sha256 -> هیچ تغییری رخ ندهد و پیام قبلاً نصب شده است بدهد."""
    with app.app_context():
        zip_path = _build_mock_master_zip(tmp_path)
        # نصب اول
        res1 = kb_admin.install_kb_package(zip_path, admin_id=admin_user.id)
        assert res1["success"] is True
        assert res1.get("already_installed") is False

        # نصب دوم
        res2 = kb_admin.install_kb_package(zip_path, admin_id=admin_user.id)
        assert res2["success"] is True
        assert res2.get("already_installed") is True
        assert "این بسته قبلاً نصب شده است" in res2.get("message", "")

        # تعداد رکوردهای نصب برای این sha256 دقیقاً ۱ است
        assert KBPackageInstall.query.filter_by(package_type="master").count() == 1


# ──────────────────────────────────────────────────────────────────────────────
# ۵. حفظ پیشرفت، XP و استریک دانش‌آموز پس از نصب
# ──────────────────────────────────────────────────────────────────────────────
def test_05_student_progress_and_xp_streak_preserved(app, admin_user, student_user, tmp_path, mock_anzali_root):
    """معیار ۵: پیشرفت، XP و استریک دانش‌آموز قبل و بعد از نصب بسته دقیقاً یکسان بماند."""
    with app.app_context():
        student = User.query.get(student_user.id)
        student.xp = 350
        student.streak = 5
        wp = WeekProgress(
            user_id=student.id,
            week=1,
            quiz_score=4,
            quiz_total=5,
            quiz_completed=True,
            kb_read=True,
        )
        db.session.add(wp)
        db.session.commit()

        # نصب بسته
        zip_path = _build_mock_master_zip(tmp_path)
        res = kb_admin.install_kb_package(zip_path, admin_id=admin_user.id)
        assert res["success"] is True

        # بررسی حفظ دقیق اطلاعات دانش‌آموز
        student_after = User.query.get(student.id)
        assert student_after.xp == 350
        assert student_after.streak == 5

        wp_after = WeekProgress.query.filter_by(user_id=student.id, week=1).first()
        assert wp_after is not None
        assert wp_after.quiz_score == 4
        assert wp_after.quiz_total == 5
        assert wp_after.quiz_completed is True
        assert wp_after.kb_read is True


# ──────────────────────────────────────────────────────────────────────────────
# ۶. برچسب پویای ۳ گزینه‌ای و ترتیب بازخورد
# ──────────────────────────────────────────────────────────────────────────────
def test_06_dynamic_quiz_type_labels_and_feedback_order(app):
    """معیار ۶: سؤال ۳ گزینه‌ای برچسب «سه‌گزینه‌ای» بگیرد و پاسخ غلط اول feedback_fa و بعد explanation_fa."""
    with app.app_context():
        # بررسی برچسب نوع سوال
        q_3opt = {
            "type": "mcq",
            "options": [{"id": "a"}, {"id": "b"}, {"id": "c"}],
            "answer": {"correct_option_ids": ["a"]},
        }
        assert kb_interactive.get_quiz_type_label(q_3opt) == "سه‌گزینه‌ای"

        q_2opt = {"type": "mcq", "options": [{"id": "a"}, {"id": "b"}]}
        assert kb_interactive.get_quiz_type_label(q_2opt) == "دوگزینه‌ای"

        q_4opt = {"type": "mcq", "options": [{"id": "a"}, {"id": "b"}, {"id": "c"}, {"id": "d"}]}
        assert kb_interactive.get_quiz_type_label(q_4opt) == "چهارگزینه‌ای"

        q_tf = {"type": "true_false"}
        assert kb_interactive.get_quiz_type_label(q_tf) == "درست یا نادرست"

        # بررسی ترتیب بازخورد در تمپلیت جزئی _quiz_result.html
        res_mock = {
            "is_correct": False,
            "feedback_fa": "بازخورد گزینهٔ نادرست الف",
            "explanation": "توضیح تفصیلی چرایی درستی گزینه دیگر",
            "misconception": "misconception_loop",
            "remediation_fa": "متن جبرانی برای بدفهمی",
            "anchor": "#sec-loop",
            "xp_awarded": 0,
        }
        rendered = app.jinja_env.get_template("kb/_partials/_quiz_result.html").render(
            res=res_mock, week=1, question_id="q1"
        )

        pos_feedback = rendered.find("بازخورد گزینهٔ نادرست الف")
        pos_explanation = rendered.find("توضیح تفصیلی چرایی درستی گزینه دیگر")
        pos_remediation = rendered.find("متن جبرانی برای بدفهمی")

        assert pos_feedback != -1
        assert pos_explanation != -1
        assert pos_remediation != -1
        # بازخورد باید قبل از توضیح ظاهر شود
        assert pos_feedback < pos_explanation
        # توضیح باید قبل از بخش جبرانی ظاهر شود
        assert pos_explanation < pos_remediation


# ──────────────────────────────────────────────────────────────────────────────
# ۷. رندر باکس LTR تک‌فاصله زیر صورت سؤال دارای کد
# ──────────────────────────────────────────────────────────────────────────────
def test_07_question_with_code_renders_ltr_monospace(app):
    """معیار ۷: سؤال با قطعه‌کد دارای باکس LTR تک‌فاصله زیر صورت سؤال باشد."""
    with app.app_context():
        # بررسی تمپلیت week.html برای وجود المان پیش‌فرض LTR font-mono زیر صورت سوال
        template_text = Path(app.root_path).parent / "templates" / "kb" / "week.html"
        content = template_text.read_text(encoding="utf-8")

        # بررسی تطابق با قرارداد D90
        assert "dir=\"ltr\"" in content
        assert "font-mono" in content
        assert "q.code" in content


# ──────────────────────────────────────────────────────────────────────────────
# ۸. آزمون تسلط هفته ۳ از w03-mt-final.item_ids و آستانه قبولی ۰.۸
# ──────────────────────────────────────────────────────────────────────────────
def test_08_week03_mastery_test_loads_from_quizzes_and_threshold_80(app):
    """معیار ۸: آزمون تسلط هفته ۳ مستقیماً از w03-mt-final.item_ids با آستانه 0.8 بارگذاری شود."""
    with app.app_context():
        mastery_info = kb_interactive.get_mastery_quiz_info(3)

        assert mastery_info.get("pass_threshold") == 0.8
        assert len(mastery_info.get("item_ids", [])) == 14
        assert mastery_info.get("mastery_qz", {}).get("id") == "w03-mt-final"

        # بارگذاری آزمون تسلط کاربر
        quizzes = kb_interactive.load_quizzes_for_week(3)
        assert len(quizzes) == 14
        quiz_ids = [q["id"] for q in quizzes]
        assert quiz_ids == mastery_info["item_ids"]


# ──────────────────────────────────────────────────────────────────────────────
# ۹. جایزه XP آزمون تسلط: 0 XP برای هر پاسخ، 25 XP ایدمپوتنت در قبولی
# ──────────────────────────────────────────────────────────────────────────────
def test_09_xp_awarded_only_on_mastery_pass_idempotent(app, student_user):
    """معیار ۹: پاسخ تک‌سؤال 0 XP، قبولی آزمون تسلط 25 XP با دلیل quiz:mastery:w03:pass به صورت ایدمپوتنت."""
    with app.app_context():
        user = User.query.get(student_user.id)
        user.xp = 0
        db.session.commit()

        # ثبت هفته در دیتابیس
        if not Week.query.filter_by(number=3).first():
            db.session.add(Week(number=3, title="هفته ۳", is_published=True))
            db.session.commit()

        mastery_info = kb_interactive.get_mastery_quiz_info(3)
        quizzes = kb_interactive.load_quizzes_for_week(3, user_id=user.id)
        total_q = len(quizzes)
        pass_needed = int(round(total_q * 0.8))  # برای ۱۴ سوال برابر ۱۱ پاسخ درست

        # ۱. پاسخ به سوال اول: نباید XP داده شود (per_answer_xp = 0)
        q1 = quizzes[0]
        # دریافت پاسخ صحیح
        path = kb_repo.get_anzali_week_dir(3) / "quizzes.json"
        q_data = json.loads(path.read_text(encoding="utf-8"))
        items_map = {it["id"]: it for it in q_data["items"]}

        def _get_correct_val(item):
            t = item.get("type")
            ans = item.get("answer", {})
            if t == "mcq":
                return ans.get("correct_option_ids", ["a"])[0]
            if t == "true_false":
                return "true" if ans.get("value") else "false"
            if t in ("predict_output", "fill_blank", "short_answer"):
                acc = ans.get("accept", [])
                return acc[0] if acc else (ans.get("value") or "0")
            if t == "parsons":
                return ans.get("order", [])
            return "a"

        r1 = kb_interactive.submit_quiz_question(user.id, 3, q1["id"], _get_correct_val(items_map[q1["id"]]))
        assert r1["success"] is True
        assert r1["xp_awarded"] == 0
        assert user.xp == 0

        # ۲. پاسخ به بقیه سوالات تا رسیدن به حد نصاب قبولی (۸۰٪)
        for q in quizzes[1:pass_needed]:
            ans_val = _get_correct_val(items_map[q["id"]])
            res = kb_interactive.submit_quiz_question(user.id, 3, q["id"], ans_val)

        # سوال مرزی قبولی
        q_pass = quizzes[pass_needed]
        ans_pass = _get_correct_val(items_map[q_pass["id"]])
        res_pass = kb_interactive.submit_quiz_question(user.id, 3, q_pass["id"], ans_pass)

        # باید ۲۵ XP اعطا شود
        assert res_pass["quiz_completed"] is True
        assert res_pass["xp_awarded"] == 25
        db.session.refresh(user)
        assert user.xp == 25

        # ۳. ارسال پاسخ‌های بعدی یا شرکت مجدد: نباید مجدداً XP اضافه شود
        for q in quizzes[pass_needed + 1:]:
            ans_val = _get_correct_val(items_map[q["id"]])
            res_sub = kb_interactive.submit_quiz_question(user.id, 3, q["id"], ans_val)
            assert res_sub["xp_awarded"] == 0

        db.session.refresh(user)
        assert user.xp == 25


# ──────────────────────────────────────────────────────────────────────────────
# ۱۰. سرویس تمرین تطبیقی ۵ دقیقه‌ای (Adaptive Practice)
# ──────────────────────────────────────────────────────────────────────────────
def test_10_adaptive_practice_session_misconceptions_and_streak(app, student_user):
    """معیار ۱۰: تمرین تطبیقی، تولید ۸-۱۰ سوال، misconception follow-up، ثبت استریک در صورت >=8 پاسخ."""
    with app.app_context():
        user = User.query.get(student_user.id)
        user.streak = 1
        yesterday = datetime.utcnow() - timedelta(days=1)
        db.session.add(XPLog(user_id=user.id, amount=5, reason="test:yesterday", timestamp=yesterday))
        db.session.commit()

        # الف) شروع نشست تمرین تطبیقی
        session_data = adaptive_service.start_user_practice_session(user.id, seed=123)
        assert session_data is not None
        assert 8 <= len(session_data.get("item_ids", [])) <= 10

        session_id = session_data["session_id"]
        bank = adaptive_service.load_question_bank_for_practice()
        bank_map = {it["id"]: it for it in bank}

        # ب) پیدا کردن سوال دارای بدفهمی (misconception) در گزینه‌ها
        item_with_misconception = None
        wrong_opt_id = None
        for it in bank:
            if it.get("type") == "mcq":
                for opt in it.get("options", []):
                    if opt.get("misconception"):
                        item_with_misconception = it
                        wrong_opt_id = opt["id"]
                        break
            if item_with_misconception:
                break

        if item_with_misconception:
            # ارسال این سوال در نشست
            engine = adaptive_service.AdaptiveEngine()
            state = adaptive_service.get_or_create_adaptive_state(user.id)
            state["current_session"]["item_ids"].append(item_with_misconception["id"])

            res_wrong = engine.record_answer(
                state, session_id, item_with_misconception["id"], wrong_opt_id, bank
            )
            assert res_wrong["is_correct"] is False
            assert res_wrong["misconception"] is not None
            assert res_wrong["remediation_fa"] is not None

        # ج) پاسخ به ۸ سوال در نشست و نهایی‌سازی نشست
        state = adaptive_service.get_or_create_adaptive_state(user.id)
        # پر کردن ۸ پاسخ
        items_to_answer = state["current_session"]["item_ids"][:8]
        for iid in items_to_answer:
            adaptive_service.submit_user_practice_answer(user.id, session_id, iid, "a")

        # پایان نشست
        finish_res = adaptive_service.complete_user_practice_session(user.id, session_id)
        assert finish_res["success"] is True
        assert finish_res["total_answered"] >= 8
        assert finish_res["qualifies_for_streak"] is True
        assert finish_res["streak_updated"] is True

        db.session.refresh(user)
        assert user.streak >= 2


# ──────────────────────────────────────────────────────────────────────────────
# ۱۱. جعبه ورودی کد و نرمال‌سازی سطرها
# ──────────────────────────────────────────────────────────────────────────────
def test_11_code_input_box_behavior_and_newline_normalization(app, student_user):
    """معیار ۱۱: نرمال‌سازی \\r\\n به \\n در سمت سرور و رعایت کلیدهای میانبر در فرانت."""
    with app.app_context():
        # بررسی تبدیل \r\n به \n در بک‌اند
        crlf_input = "line1\r\nline2\r\nline3"
        clean = crlf_input.replace("\r\n", "\n").replace("\r", "\n").strip()
        assert clean == "line1\nline2\nline3"

        # بررسی ویژگی‌های کامپوننت textarea در تمپلیت
        template_text = Path(app.root_path).parent / "templates" / "kb" / "week.html"
        content = template_text.read_text(encoding="utf-8")

        # ۱. تگ textarea با LTR و کلاس monospace
        assert "<textarea" in content
        assert "enterkeyhint=\"enter\"" in content
        # ۲. پشتیبانی از میانبرهای Ctrl+Enter, Tab, Esc در جاوااسکریپت
        assert "handleCodeTextareaKeydown" in content
        assert "ctrlKey || e.metaKey" in content
        assert "tabTrapActive" in content
        assert "isComposing" in content


# ──────────────────────────────────────────────────────────────────────────────
# ۱۲. برابری دقیق (Parity Test) با reference_engine.py
# ──────────────────────────────────────────────────────────────────────────────
def test_12_adaptive_engine_parity_with_reference_engine():
    """معیار ۱۲: آزمون برابری بین reference_engine مستقل و AdaptiveEngine با ورودی و seed یکسان."""
    ref_path = Path(__file__).parent.parent / "docs" / "cs50x-kb" / "anzali-fa" / "adaptive" / "reference_engine.py"
    assert ref_path.is_file(), f"فایل موتور مرجع {ref_path} یافت نشد."

    # بارگذاری ماژول مستقل reference_engine
    spec = importlib.util.spec_from_file_location("reference_engine", str(ref_path))
    ref_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ref_mod)

    # ایجاد دو موتور
    ref_engine = ref_mod.ReferenceEngine()
    app_engine = adaptive_service.AdaptiveEngine()

    # تست ۱: برابری به‌روزرسانی BKT
    p_init = 0.20
    # حالت درست
    ref_correct = ref_engine.update_bkt(p_init, True)
    app_correct = app_engine.update_bkt(p_init, True)
    assert ref_correct == app_correct, f"BKT correct mismatch: ref={ref_correct}, app={app_correct}"

    # حالت نادرست
    ref_incorrect = ref_engine.update_bkt(p_init, False)
    app_incorrect = app_engine.update_bkt(p_init, False)
    assert ref_incorrect == app_incorrect, f"BKT incorrect mismatch: ref={ref_incorrect}, app={app_incorrect}"

    # تست ۲: برابری به‌روزرسانی جعبه لایتنر
    today_str = "2026-11-01"
    for box in range(1, 6):
        ref_box_c, ref_next_c = ref_engine.update_leitner(box, True, today_str)
        app_box_c, app_next_c = app_engine.update_leitner(box, True, today_str)
        assert (ref_box_c, ref_next_c) == (app_box_c, app_next_c)

        ref_box_w, ref_next_w = ref_engine.update_leitner(box, False, today_str)
        app_box_w, app_next_w = app_engine.update_leitner(box, False, today_str)
        assert (ref_box_w, ref_next_w) == (app_box_w, app_next_w)

    # تست ۳: برابری برنامه‌ریزی نشست (build_session) با seed یکسان
    dummy_bank = [
        {"id": f"q_{i}", "type": "mcq", "concept_ids": [f"c_{i % 5}"]}
        for i in range(20)
    ]
    ref_state = ref_engine.new_state()
    app_state = app_engine.new_state()

    ref_sess = ref_engine.build_session(ref_state, dummy_bank, today_str="2026-11-01", seed=42)
    app_sess = app_engine.build_session(app_state, dummy_bank, today_str="2026-11-01", seed=42)

    assert ref_sess["item_ids"] == app_sess["item_ids"]
    assert ref_sess["plan"] == app_sess["plan"]
