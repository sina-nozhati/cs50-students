"""بارگذاری پایگاه دانش سلسله‌مراتبی docs/cs50x-kb از index.json."""
from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any

# flask-app/docs/cs50x-kb
_KB_ROOT = Path(__file__).resolve().parents[2] / "docs" / "cs50x-kb"
_INDEX_PATH = _KB_ROOT / "index.json"

# ترتیب نمایش ثابت (هم‌راستا با CS50: AI بین ۷ و ۸)
_WEEK_DISPLAY_ORDER = [0, 1, 2, 3, 4, 5, 6, 7, 71, 8, 9, 10, 99]


def kb_root() -> Path:
    return _KB_ROOT


def get_week_folder_slug(week: int) -> str:
    """نام پوشه استاندارد هفتگی در anzali-fa/weeks."""
    if week == 71:
        return "week-ai"
    if week == 99:
        return "final-project"
    return f"week-{week:02d}"


def get_week_node_id(week: int) -> str:
    """شناسه نود والد هفته در index.json."""
    if week == 71:
        return "week-ai"
    if week == 99:
        return "final-project"
    return f"week-{week}"


def get_anzali_week_dir(week: int) -> Path:
    """مسیر پوشه محتوای هفته در anzali-fa/weeks با پشتیبانی از نام‌های مستعار."""
    root = _KB_ROOT / "anzali-fa" / "weeks"
    candidates = []
    if week == 71:
        candidates = ["week-ai", "week-71"]
    elif week == 99:
        candidates = ["final-project", "week-99"]
    else:
        candidates = [f"week-{week:02d}", f"week-{week}"]

    for c in candidates:
        p = root / c
        if p.is_dir():
            return p
    return root / candidates[0]


def site_number_for_node(node: dict[str, Any]) -> int | None:
    """نگاشت نود KB به شمارهٔ Week در سایت (0–10، 71=AI، 99=Final)."""
    nid = node.get("id") or ""
    if nid == "final-project" or node.get("type") == "final-project":
        return 99
    if nid == "week-ai" or node.get("week") == "ai":
        return 71
    w = node.get("week")
    if isinstance(w, int):
        return w
    if isinstance(w, str) and w.isdigit():
        return int(w)
    if nid.startswith("week-") and nid[5:].isdigit():
        return int(nid[5:])
    return None


def _index_mtime() -> float:
    mt = 0.0
    try:
        mt = _INDEX_PATH.stat().st_mtime
    except OSError:
        pass
    fa_root = _KB_ROOT / "anzali-fa"
    if fa_root.is_dir():
        try:
            mt = max(mt, fa_root.stat().st_mtime)
            for p in fa_root.rglob("index.fragment.json"):
                mt = max(mt, p.stat().st_mtime)
        except OSError:
            pass
    return mt


@lru_cache(maxsize=4)
def _load_index_cached(mtime: float) -> dict[str, Any]:
    with open(_INDEX_PATH, encoding="utf-8") as f:
        data = json.load(f)
    nodes = {n["id"]: n for n in data.get("nodes", []) if "id" in n}

    # پویش خودکار برای بسته‌های هفتگی جدید در anzali-fa
    # هر پوشهٔ جدیدی که اضافه شود و فایل index.fragment.json داشته باشد،
    # نودهایش بدون نیاز به ادغام دستی، مستقیم در درخت لودر بارگذاری می‌شوند.
    fa_root = _KB_ROOT / "anzali-fa"
    if fa_root.is_dir():
        for frag_path in sorted(fa_root.rglob("index.fragment.json")):
            try:
                with open(frag_path, encoding="utf-8") as ff:
                    frag = json.load(ff)
                mount = "anzali-fa/"
                orig_mount = frag.get("mount_prefix", "")
                for fn in frag.get("nodes", []):
                    nid = fn.get("id")
                    if nid and nid not in nodes:
                        node_copy = dict(fn)
                        p_str = node_copy.get("path", "")
                        if orig_mount and p_str.startswith(orig_mount):
                            node_copy["path"] = mount + p_str[len(orig_mount):]
                        elif not p_str.startswith(mount):
                            node_copy["path"] = mount + p_str
                        nodes[nid] = node_copy

                for att in frag.get("attach_to", []):
                    pid = att.get("parent_id")
                    cid = att.get("append_child")
                    if pid in nodes and cid:
                        p = nodes[pid]
                        ch = p.setdefault("children", [])
                        if cid not in ch:
                            ch.append(cid)
            except Exception:
                pass

    return {"meta": {k: v for k, v in data.items() if k != "nodes"}, "nodes": nodes}


def _index() -> dict[str, Any]:
    return _load_index_cached(_index_mtime())


def clear_cache() -> None:
    _load_index_cached.cache_clear()


def get_node(doc_id: str) -> dict[str, Any] | None:
    return _index()["nodes"].get(doc_id)


def all_nodes() -> dict[str, dict[str, Any]]:
    return _index()["nodes"]


def children_of(doc_id: str) -> list[dict[str, Any]]:
    node = get_node(doc_id)
    if not node:
        return []
    out = []
    for cid in node.get("children") or []:
        child = get_node(cid)
        if child:
            out.append(child)
    return out


def resolve_path(node: dict[str, Any]) -> Path | None:
    rel = node.get("path")
    if not rel:
        return None
    path = (_KB_ROOT / rel).resolve()
    # جلوگیری از path traversal
    try:
        path.relative_to(_KB_ROOT.resolve())
    except ValueError:
        return None
    return path if path.is_file() else None


def list_week_nodes() -> list[dict[str, Any]]:
    """نودهای هفته + final-project با site_number و ترتیب نمایش."""
    by_site: dict[int, dict[str, Any]] = {}
    for node in all_nodes().values():
        ntype = node.get("type")
        if ntype not in ("week", "final-project"):
            continue
        site_n = site_number_for_node(node)
        if site_n is None:
            continue
        enriched = {**node, "site_number": site_n}
        by_site[site_n] = enriched
    ordered = []
    for n in _WEEK_DISPLAY_ORDER:
        if n in by_site:
            ordered.append(by_site[n])
    # هر هفتهٔ اضافی خارج از ترتیب ثابت
    for n, node in sorted(by_site.items()):
        if n not in _WEEK_DISPLAY_ORDER:
            ordered.append(node)
    return ordered


def list_weeks_ordered() -> list[dict[str, Any]]:
    return list_week_nodes()


def week_node_by_site_number(site_number: int) -> dict[str, Any] | None:
    for node in list_week_nodes():
        if node.get("site_number") == site_number:
            return node
    return None


def week_doc_id(site_number: int) -> str | None:
    node = week_node_by_site_number(site_number)
    return node["id"] if node else None


def anzali_hub_by_site_number(site_number: int) -> dict[str, Any] | None:
    """پیدا کردن نود هاب فارسی انزلی برای یک هفته (مثلاً w00-fa یا هر هفتهٔ دیگر)."""
    nodes = all_nodes()
    target_id = f"w{site_number:02d}-fa"
    if target_id in nodes:
        return nodes[target_id]
    for node in nodes.values():
        if node.get("type") in ("anzali-week-hub", "week-overview"):
            if node.get("week") == site_number or site_number_for_node(node) == site_number:
                return node
    return None


def find_counterpart_node(node: dict[str, Any]) -> dict[str, Any] | None:
    """پیدا کردن سند همتا (فارسی برای انگلیسی، یا انگلیسی برای فارسی)."""
    nid = node.get("id") or ""
    is_fa = (
        node.get("lang") == "fa"
        or "anzali-fa" in (node.get("tags") or [])
        or nid.startswith(("w00-", "w01-", "w02-"))
        or "anzali-fa" in (node.get("path") or "")
    )
    site_n = site_number_for_node(node)
    nodes = all_nodes()

    if is_fa:
        # اگر پرابلم‌ست است
        if "pset" in nid or "scratch" in nid or node.get("type") in ("problem-set", "anzali-pset-guide"):
            if site_n is not None:
                for k, cand in nodes.items():
                    if k.startswith(f"pset-{site_n}") and cand.get("type") == "pset":
                        return cand
                pset_idx = nodes.get(f"pset-{site_n}")
                if pset_idx:
                    return pset_idx

        # اگر لکچر/یادداشت/خلاصه است، لکچر یا سند اصلی انگلیسی را پیدا کن
        if site_n is not None:
            en_hub = week_node_by_site_number(site_n)
            if en_hub:
                for cid in en_hub.get("children", []):
                    c = nodes.get(cid)
                    if c and c.get("type") in ("lecture", "week"):
                        return c
                return en_hub
    else:
        # اگر سند انگلیسی است
        if site_n is not None:
            # اگر پرابلم‌ست انگلیسی است
            if nid.startswith(f"pset-{site_n}") or "scratch" in nid.lower():
                fa_hub = anzali_hub_by_site_number(site_n)
                if fa_hub:
                    for cid in fa_hub.get("children", []):
                        c = nodes.get(cid)
                        if c and (c.get("type") == "anzali-pset-guide" or "ps-" in cid):
                            return c

            # در غیر این صورت هاب فارسی هفته
            return anzali_hub_by_site_number(site_n)
    return None

