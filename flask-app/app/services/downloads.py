"""سرویس مدیریت و ذخیره‌سازی دانلودهای پویای پایگاه دانش (Dynamic KB Downloads Service).

این ماژول وظیفه ساخت اتمیک، اعتبارسنجی، کش و ارائه امن فایل‌های دانلودی
(جزوات، خلاصه و واژه‌نامه، راهنماهای تمرین، کد منبع، اسلایدها و فلش‌کارت‌ها)
را بر عهده دارد.
مسیر ذخیره: <DATA_DIR>/kb_downloads/<kb_version>/<package_sha256[:12]>/<week_slug>/
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
import threading
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote

from flask import current_app

from app.content import kb_repo
from app.kb_downloads.generate import build_week, find_chrome, GEN_VERSION
from app.models import KBPackageInstall, Week


def get_data_dir() -> Path:
    """مسیر ذخیره‌سازی داده‌های برنامه (خارج از static و Git)."""
    configured = current_app.config.get("DATA_DIR")
    if configured:
        p = Path(configured)
    else:
        p = Path(current_app.root_path).parent / "data"
    p.mkdir(parents=True, exist_ok=True)
    return p


def get_active_kb_package_info() -> tuple[str, str]:
    """استخراج نسخه و هش بسته فعال پایگاه دانش (kb_version, package_sha12)."""
    kb_root = kb_repo.kb_root() / "anzali-fa"
    manifest_path = kb_root / "manifest.json"

    kb_version = "1.0.0"
    if manifest_path.is_file():
        try:
            m_data = json.loads(manifest_path.read_text(encoding="utf-8"))
            kb_version = m_data.get("version") or "1.0.0"
        except Exception:
            pass

    # تلاش برای استخراج sha256 از آخرین نصب معتبر
    pkg_sha = None
    try:
        latest_install = KBPackageInstall.query.order_by(KBPackageInstall.installed_at.desc()).first()
        if latest_install and latest_install.sha256:
            pkg_sha = latest_install.sha256
    except Exception:
        pass

    if not pkg_sha:
        if manifest_path.is_file():
            pkg_sha = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        else:
            pkg_sha = hashlib.sha256(b"cs50x-anzali-kb-default").hexdigest()

    sha12 = pkg_sha[:12]
    return kb_version, sha12


def get_package_downloads_root(kb_version: str | None = None, package_sha12: str | None = None) -> Path:
    """ریشه فایل‌های دانلودی بسته جاری: <DATA_DIR>/kb_downloads/<kb_version>/<sha12>/"""
    if not kb_version or not package_sha12:
        v, s = get_active_kb_package_info()
        kb_version = kb_version or v
        package_sha12 = package_sha12 or s

    root = get_data_dir() / "kb_downloads" / kb_version / package_sha12
    root.mkdir(parents=True, exist_ok=True)
    return root


def resolve_week_slug(week_identifier: int | str) -> str:
    """تبدیل شماره یا اسلاگ هفته به اسلاگ استاندارد پوشه."""
    if isinstance(week_identifier, int):
        if week_identifier == 71:
            return "week-ai"
        elif week_identifier == 99:
            return "final-project"
        elif week_identifier == 0:
            return "week-00"
        else:
            return f"week-{week_identifier:02d}"

    ident = str(week_identifier).strip().lower()
    if ident in ("ai", "week-ai", "71", "week-71"):
        return "week-ai"
    if ident in ("final", "final-project", "project", "99", "week-99"):
        return "final-project"
    if ident.isdigit():
        n = int(ident)
        return resolve_week_slug(n)

    m = re.match(r"^week-(\d+)", ident)
    if m:
        w_num = int(m.group(1))
        # اگر دایرکتوری مستقیم ident وجود داشت، همان را برگردان
        try:
            weeks_dir = kb_repo.kb_root() / "anzali-fa" / "weeks"
            if (weeks_dir / ident).is_dir():
                return ident
            if (weeks_dir / f"week-{w_num:02d}").is_dir():
                return f"week-{w_num:02d}"
        except Exception:
            pass
        return f"week-{w_num:02d}"

    return f"week-{ident}"


def get_week_downloads_dir(week_slug: str, kb_version: str | None = None, package_sha12: str | None = None) -> Path:
    """مسیر فایل‌های یک هفته خاص."""
    slug = resolve_week_slug(week_slug)
    root = get_package_downloads_root(kb_version, package_sha12)
    return root / slug


def is_dynamic_downloads_enabled() -> bool:
    """بررسی پرچم فعال بودن دانلودهای پویا (Feature Flag)."""
    return bool(current_app.config.get("KB_DOWNLOADS_DYNAMIC", False))


def is_manifest_valid(manifest_file: Path) -> bool:
    """اعتبارسنجی کامل فایل‌های موجود در downloads.json."""
    if not manifest_file.is_file():
        return False
    try:
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
        items = data.get("items", [])
        if not items:
            return False
        week_dir = manifest_file.parent
        for item in items:
            for fmt in item.get("formats", []):
                rel_path = fmt.get("path")
                if not rel_path:
                    return False
                target = week_dir / rel_path
                if not target.is_file():
                    return False
                # بررسی حجم
                if fmt.get("size") and target.stat().st_size != fmt.get("size"):
                    return False
        return True
    except Exception:
        return False


def get_week_manifest(week_identifier: int | str) -> dict[str, Any] | None:
    """دریافت مانیفست دانلودهای فعال هفته در صورت فعال بودن پرچم و وجود فایل معتبر."""
    if not is_dynamic_downloads_enabled():
        return None

    slug = resolve_week_slug(week_identifier)
    week_dir = get_week_downloads_dir(slug)
    manifest_file = week_dir / "downloads.json"

    if not is_manifest_valid(manifest_file):
        return None

    try:
        return json.loads(manifest_file.read_text(encoding="utf-8"))
    except Exception:
        return None


def build_downloads_for_week(
    week_identifier: int | str,
    force: bool = False,
    pdf: bool = True,
    engine: str = "chrome",
) -> dict[str, Any]:
    """ساخت اتمیک خروجی‌های دانلودی یک هفته.
    در صورت وجود نسخه معتبر و force=False، بدون ساخت مجدد برمی‌گرداند.
    """
    slug = resolve_week_slug(week_identifier)
    kb_root = kb_repo.kb_root() / "anzali-fa"
    week_source_dir = kb_root / "weeks" / slug

    if not week_source_dir.is_dir():
        raise FileNotFoundError(f"پوشه منبع هفته یافت نشد: {week_source_dir}")

    target_dir = get_week_downloads_dir(slug)
    manifest_file = target_dir / "downloads.json"

    # اگر وجود دارد و معتبر است و نیاز به بازسازی اجباری نیست، بازگردان
    if not force and is_manifest_valid(manifest_file):
        return json.loads(manifest_file.read_text(encoding="utf-8"))

    # ساخت اتمیک در پوشه موقت
    with tempfile.TemporaryDirectory(prefix=f"gen_{slug}_") as tmp_dir:
        tmp_path = Path(tmp_dir)
        cache_dir = get_data_dir() / "kb_downloads" / "cache"

        manifest = build_week(
            kb_dir=kb_root,
            week_slug=slug,
            out_dir=tmp_path,
            pdf=pdf,
            engine=engine,
            cache_dir=cache_dir,
        )

        tmp_manifest = tmp_path / "downloads.json"
        if not is_manifest_valid(tmp_manifest):
            raise RuntimeError(f"اعتبارسنجی فایل‌های خروجی هفته {slug} در پوشه موقت با شکست مواجه شد.")

        # جابه‌جایی اتمیک
        target_dir.parent.mkdir(parents=True, exist_ok=True)
        if target_dir.exists():
            backup_dir = target_dir.parent / f"{slug}_old_{os.getpid()}"
            try:
                target_dir.rename(backup_dir)
                shutil.copytree(tmp_path, target_dir)
                shutil.rmtree(backup_dir, ignore_errors=True)
            except Exception:
                if backup_dir.exists() and not target_dir.exists():
                    backup_dir.rename(target_dir)
                raise
        else:
            shutil.copytree(tmp_path, target_dir)

    return manifest


# ─── سیستم مانیتورینگ و رهگیری لحظه‌ای بازتولید فایل‌های دانلودی ───────
_REBUILD_LOCK = threading.Lock()
_REBUILD_STATUS: dict[str, Any] = {
    "is_running": False,
    "current_index": 0,
    "total_weeks": 0,
    "current_slug": "",
    "current_title": "",
    "percent": 0,
    "elapsed_seconds": 0,
    "completed_weeks": [],
    "errors": [],
    "warnings": [],
    "status": "idle",  # "idle", "running", "success", "partial", "error"
    "message": "",
    "finished": False,
    "started_at": 0,
    "updated_at": 0,
}


def get_week_display_title(slug: str) -> str:
    """دریافت نام و عنوان فارسی و خوانا برای یک هفته دانلودی."""
    try:
        kb_root = kb_repo.kb_root() / "anzali-fa"
        curric_path = kb_root / "weeks" / slug / "curriculum.json"
        if curric_path.is_file():
            cdata = json.loads(curric_path.read_text(encoding="utf-8"))
            t = cdata.get("title") or cdata.get("title_fa") or cdata.get("name")
            if t:
                return t
    except Exception:
        pass

    title_map = {
        "week-00": "هفته ۰ — اسکرچ (Scratch)",
        "week-01": "هفته ۱ — زبان سی (C)",
        "week-02": "هفته ۲ — آرایه‌ها (Arrays)",
        "week-03": "هفته ۳ — الگوریتم‌ها (Algorithms)",
        "week-04": "هفته ۴ — حافظه (Memory)",
        "week-05": "هفته ۵ — ساختار داده‌ها (Data Structures)",
        "week-06": "هفته ۶ — پایتون (Python)",
        "week-07": "هفته ۷ — پایگاه داده SQL",
        "week-08": "هفته ۸ — توسعه وب HTML/CSS/JS",
        "week-09": "هفته ۹ — فریم‌ورک Flask",
        "week-10": "هفته ۱۰ — امنیت سایبری (Cybersecurity)",
        "week-ai": "هفته هوش مصنوعی (Artificial Intelligence)",
        "final-project": "پروژه پایانی دوره (Final Project)",
    }
    return title_map.get(slug, slug)


def get_rebuild_progress() -> dict[str, Any]:
    """دریافت وضعیت زنده و درصد پیشرفت بازتولید فایل‌های دانلودی."""
    with _REBUILD_LOCK:
        status_copy = dict(_REBUILD_STATUS)
        status_copy["completed_weeks"] = list(_REBUILD_STATUS["completed_weeks"])
        status_copy["errors"] = list(_REBUILD_STATUS["errors"])
        status_copy["warnings"] = list(_REBUILD_STATUS["warnings"])
        if _REBUILD_STATUS["is_running"] and _REBUILD_STATUS["started_at"] > 0:
            status_copy["elapsed_seconds"] = int(time.time() - _REBUILD_STATUS["started_at"])
        return status_copy


def start_async_rebuild_all_downloads(force: bool = True, app_obj: Any = None) -> dict[str, Any]:
    """شروع غیرهمگام بازتولید تمام دانلودها در ترد پس‌زمینه بدون بلاک کردن ریکوئست HTTP."""
    with _REBUILD_LOCK:
        if _REBUILD_STATUS["is_running"]:
            return {
                "started": False,
                "is_running": True,
                "message": "عملیات بازتولید در حال حاضر در پس‌زمینه در جریان است.",
                "progress": get_rebuild_progress(),
            }

        _REBUILD_STATUS.update({
            "is_running": True,
            "current_index": 0,
            "total_weeks": 0,
            "current_slug": "",
            "current_title": "در حال آماده‌سازی و بررسی فهرست هفته‌ها...",
            "percent": 0,
            "elapsed_seconds": 0,
            "completed_weeks": [],
            "errors": [],
            "warnings": [],
            "status": "running",
            "message": "فرآیند بازتولید فایل‌های دانلودی آغاز شد.",
            "finished": False,
            "started_at": time.time(),
            "updated_at": time.time(),
        })

    def _worker():
        try:
            if app_obj:
                with app_obj.app_context():
                    _execute_rebuild_all(force=force)
            else:
                _execute_rebuild_all(force=force)
        except Exception as e:
            with _REBUILD_LOCK:
                _REBUILD_STATUS["is_running"] = False
                _REBUILD_STATUS["finished"] = True
                _REBUILD_STATUS["status"] = "error"
                _REBUILD_STATUS["message"] = f"خطای غیرمنتظره در بازتولید: {e}"
                _REBUILD_STATUS["errors"].append({"slug": "system", "title": "خطای سیستمی", "error": str(e)})

    threading.Thread(target=_worker, daemon=True, name="async-kb-rebuild-downloads").start()
    return {
        "started": True,
        "is_running": True,
        "message": "عملیات بازتولید فایل‌های دانلودی در پس‌زمینه آغاز شد.",
        "progress": get_rebuild_progress(),
    }


def _execute_rebuild_all(force: bool = True, pdf: bool = True, engine: str = "chrome") -> dict[str, Any]:
    """اجرای مرحله‌به‌مرحله ساخت تمام دانلودها و به‌روزرسانی لحظه‌ای وضعیت."""
    kb_root = kb_repo.kb_root() / "anzali-fa"
    weeks_root = kb_root / "weeks"

    all_slugs = []
    if weeks_root.is_dir():
        for d in sorted(weeks_root.iterdir()):
            if d.is_dir() and (d.name.startswith("week-") or d.name == "final-project"):
                all_slugs.append(d.name)

    total = len(all_slugs)
    with _REBUILD_LOCK:
        _REBUILD_STATUS["total_weeks"] = total

    results: dict[str, Any] = {
        "success": True,
        "total_weeks": total,
        "weeks": {},
        "warnings": [],
        "errors": [],
    }

    start_t = time.time()
    for idx, slug in enumerate(all_slugs):
        title = get_week_display_title(slug)
        with _REBUILD_LOCK:
            _REBUILD_STATUS["current_index"] = idx + 1
            _REBUILD_STATUS["current_slug"] = slug
            _REBUILD_STATUS["current_title"] = title
            _REBUILD_STATUS["percent"] = int((idx / max(total, 1)) * 100)
            _REBUILD_STATUS["updated_at"] = time.time()

        t0 = time.time()
        try:
            m = build_downloads_for_week(slug, force=force, pdf=pdf, engine=engine)
            dur = round(time.time() - t0, 1)
            item_count = len(m.get("items", []))
            has_pdf = any("pdf" in it.get("formats", []) for it in m.get("items", []))
            has_zip = any("zip" in it.get("formats", []) for it in m.get("items", []))
            results["weeks"][slug] = {
                "success": True,
                "items_count": item_count,
                "built": m.get("built"),
                "duration_s": dur,
                "has_pdf": has_pdf,
            }
            with _REBUILD_LOCK:
                _REBUILD_STATUS["completed_weeks"].append({
                    "slug": slug,
                    "title": title,
                    "items_count": item_count,
                    "has_pdf": has_pdf,
                    "has_zip": has_zip,
                    "duration_s": dur,
                })
        except Exception as e:
            results["success"] = False
            err_msg = f"{title} ({slug}): {e}"
            results["errors"].append(err_msg)
            results["weeks"][slug] = {
                "success": False,
                "error": str(e),
            }
            with _REBUILD_LOCK:
                _REBUILD_STATUS["errors"].append({
                    "slug": slug,
                    "title": title,
                    "error": str(e),
                })

        with _REBUILD_LOCK:
            _REBUILD_STATUS["percent"] = int(((idx + 1) / max(total, 1)) * 100)
            _REBUILD_STATUS["updated_at"] = time.time()

    pkg_root = get_package_downloads_root()
    status_file = pkg_root / "status.json"
    status_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    with _REBUILD_LOCK:
        _REBUILD_STATUS["is_running"] = False
        _REBUILD_STATUS["finished"] = True
        _REBUILD_STATUS["percent"] = 100
        _REBUILD_STATUS["elapsed_seconds"] = int(time.time() - start_t)
        err_len = len(_REBUILD_STATUS["errors"])
        comp_len = len(_REBUILD_STATUS["completed_weeks"])
        if err_len == 0:
            _REBUILD_STATUS["status"] = "success"
            _REBUILD_STATUS["message"] = f"کلیه فایل‌های دانلودی {comp_len} هفته با موفقیت تولید و کش شدند."
        elif comp_len > 0:
            _REBUILD_STATUS["status"] = "partial"
            _REBUILD_STATUS["message"] = f"{comp_len} هفته با موفقیت تولید شد، اما {err_len} هفته با خطا مواجه شد."
        else:
            _REBUILD_STATUS["status"] = "error"
            _REBUILD_STATUS["message"] = "تولید فایل‌های دانلودی با خطا مواجه شد."

    return results


def build_all_downloads(
    force: bool = False,
    pdf: bool = True,
    engine: str = "chrome",
) -> dict[str, Any]:
    """ساخت فایل‌های دانلودی برای تمام هفته‌های موجود در پایگاه دانش."""
    return _execute_rebuild_all(force=force, pdf=pdf, engine=engine)


def _is_safe_path(base_dir: Path, target_path: Path) -> bool:
    """بررسی عدم خروج مسیر از پوشه مجاز (Path Traversal Protection)."""
    try:
        target_path.resolve().relative_to(base_dir.resolve())
        return True
    except (ValueError, RuntimeError):
        return False


def get_download_file(
    week_slug: str,
    item_id: str,
    fmt: str,
) -> dict[str, Any] | None:
    """جستجو و بازیابی فایل برای دانلود با رعایت کامل امنیت و استاندارد RFC 5987/6266."""
    slug = resolve_week_slug(week_slug)
    fmt = fmt.lower().strip(".")
    if fmt not in ("html", "pdf", "zip"):
        return None

    # بررسی شناسه معتبر
    if not re.match(r"^[a-zA-Z0-9_\-\.:]+$", item_id):
        return None

    manifest = get_week_manifest(slug)
    if not manifest:
        return None

    week_dir = get_week_downloads_dir(slug)

    # یافتن آیتم در مانیفست
    matched_format = None
    item_title_fa = ""
    for it in manifest.get("items", []):
        full_id = it.get("id", "")
        raw_id = full_id.split(":", 1)[1] if ":" in full_id else full_id
        # تطبیق شناسه کوتاه، شناسه کامل، یا اسلاگ pset
        pset_slug = it.get("pset_slug")
        is_id_match = (
            raw_id == item_id
            or full_id == item_id
            or (pset_slug and (item_id == f"pset-{pset_slug}" or item_id == pset_slug))
        )

        for f in it.get("formats", []):
            path_stem = Path(f.get("path", "")).stem
            if is_id_match or path_stem == item_id:
                if f.get("format") == fmt:
                    matched_format = f
                    item_title_fa = it.get("title_fa") or item_id
                    break
        if matched_format:
            break

    if not matched_format:
        return None

    rel_path = matched_format.get("path")
    if not rel_path:
        return None

    target_file = (week_dir / rel_path).resolve()
    if not _is_safe_path(week_dir, target_file) or not target_file.is_file():
        return None

    ascii_filename = target_file.name
    # نام فارسی استاندارد برای دانلود
    clean_title = re.sub(r'[\\/*?:"<>|]', "", item_title_fa).strip()
    utf8_filename = f"{clean_title} - {ascii_filename}"

    mime_map = {
        "html": "text/html; charset=utf-8",
        "pdf": "application/pdf",
        "zip": "application/zip",
    }
    mime_type = matched_format.get("mime") or mime_map.get(fmt, "application/octet-stream")

    return {
        "abs_path": target_file,
        "mime_type": mime_type,
        "ascii_filename": ascii_filename,
        "utf8_filename": utf8_filename,
        "sha256": matched_format.get("sha256"),
        "size": target_file.stat().st_size,
        "is_inline": (fmt == "html"),
    }


def get_admin_downloads_status() -> dict[str, Any]:
    """خلاصه وضعیت دانلودهای تمام هفته‌ها برای پنل مدیریت /admin/kb-packages."""
    kb_root = kb_repo.kb_root() / "anzali-fa"
    weeks_root = kb_root / "weeks"
    chrome_path = find_chrome()

    status_data = {
        "dynamic_enabled": is_dynamic_downloads_enabled(),
        "pdf_engine_available": "Chromium (" + str(chrome_path) + ")" if chrome_path else "Pure-Python / None",
        "has_chrome": bool(chrome_path),
        "weeks": [],
        "by_week": {},
    }

    if not weeks_root.is_dir():
        return status_data

    for d in sorted(weeks_root.iterdir()):
        if d.is_dir() and (d.name.startswith("week-") or d.name == "final-project"):
            slug = d.name
            week_dir = get_week_downloads_dir(slug)
            manifest_file = week_dir / "downloads.json"
            valid = is_manifest_valid(manifest_file)
            items_count = 0
            formats_count = {"html": 0, "pdf": 0, "zip": 0}

            if valid:
                try:
                    m = json.loads(manifest_file.read_text(encoding="utf-8"))
                    items = m.get("items", [])
                    items_count = len(items)
                    for it in items:
                        for f in it.get("formats", []):
                            fmt = f.get("format")
                            if fmt in formats_count:
                                formats_count[fmt] += 1
                except Exception:
                    pass

            w_num = None
            m_w = re.search(r"week-(\d+)", slug)
            if m_w:
                w_num = int(m_w.group(1))
            elif slug == "week-ai":
                w_num = 71
            elif slug == "final-project":
                w_num = 99

            week_entry = {
                "slug": slug,
                "week_number": w_num,
                "is_built": valid,
                "items_count": items_count,
                "formats": formats_count,
            }
            status_data["weeks"].append(week_entry)
            if w_num is not None:
                status_data["by_week"][w_num] = week_entry

    return status_data
