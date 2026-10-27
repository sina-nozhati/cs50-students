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
    try:
        return _INDEX_PATH.stat().st_mtime
    except OSError:
        return 0.0


@lru_cache(maxsize=4)
def _load_index_cached(mtime: float) -> dict[str, Any]:
    with open(_INDEX_PATH, encoding="utf-8") as f:
        data = json.load(f)
    nodes = {n["id"]: n for n in data.get("nodes", []) if "id" in n}
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
