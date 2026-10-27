"""سرویس KB — پل بین روت‌ها و docs/cs50x-kb."""
from __future__ import annotations

from app.content import kb_repo
from app.content import md_render
from app.content.certificate import CERTIFICATE


def certificate() -> dict:
    return CERTIFICATE


def catalog() -> list[dict]:
    """فهرست هفته‌ها برای /kb/ (با فیلدهای سازگار با تمپلیت)."""
    out = []
    for node in kb_repo.list_weeks_ordered():
        children = kb_repo.children_of(node["id"])
        pset_count = sum(
            1
            for c in children
            if c.get("type") in ("pset", "pset-index", "practice")
            or (c.get("id") or "").startswith("pset-")
        )
        # شمارش مسائل واقعی زیر pset-index
        problem_count = 0
        for c in children:
            if c.get("type") == "pset-index":
                problem_count += len(kb_repo.children_of(c["id"]))
            elif c.get("type") == "pset":
                problem_count += 1
        out.append({
            "number": node["site_number"],
            "id": node["id"],
            "title_fa": _title_fa(node),
            "title_en": node.get("title") or "",
            "title": node.get("title") or "",
            "has_pset": problem_count > 0 or pset_count > 0,
            "problems": [{"name": "x"}] * problem_count,  # برای |length در تمپلیت index
            "topics": (node.get("tags") or [])[:6],
            "source_url": node.get("source_url"),
            "type": node.get("type"),
        })
    return out


def _title_fa(node: dict) -> str:
    n = node.get("site_number")
    title = node.get("title") or ""
    if n == 71:
        return "هفته هوش مصنوعی"
    if n == 99:
        return "پروژه نهایی"
    if isinstance(n, int) and n <= 10:
        # Week 0 — Scratch → هفته ۰ — Scratch
        return title.replace("Week ", "هفته ").replace("Artificial Intelligence — ", "")
    return title


def week_payload(site_number: int) -> dict | None:
    node = kb_repo.week_node_by_site_number(site_number)
    if not node:
        return None
    path = kb_repo.resolve_path(node)
    rendered = md_render.load_and_render(path) if path else {
        "official_html": "",
        "generated_html": "",
        "full_html": "",
        "has_official": False,
        "has_generated": False,
        "toc": [],
    }
    children = []
    for c in kb_repo.children_of(node["id"]):
        children.append({
            "id": c["id"],
            "title": c.get("title") or c["id"],
            "type": c.get("type") or "doc",
            "source_url": c.get("source_url"),
            "child_count": len(c.get("children") or []),
        })
    return {
        "number": site_number,
        "id": node["id"],
        "title_fa": _title_fa(node),
        "title_en": node.get("title") or "",
        "topics": node.get("tags") or [],
        "links": {"lecture": node.get("source_url")},
        "source_url": node.get("source_url"),
        "source_urls": node.get("source_urls") or [],
        "children": children,
        "has_pset": any(
            c["type"] in ("pset", "pset-index") or c["id"].startswith("pset-")
            for c in children
        ),
        "rendered": rendered,
        "license": "CC BY-NC-SA 4.0",
        "attribution": "CS50x 2026 © David J. Malan, Harvard University",
    }


def content_ready(site_number: int) -> bool:
    return kb_repo.week_node_by_site_number(site_number) is not None


def get_document(doc_id: str) -> dict | None:
    node = kb_repo.get_node(doc_id)
    if not node:
        return None
    path = kb_repo.resolve_path(node)
    if not path:
        return None
    rendered = md_render.load_and_render(path)
    parent = kb_repo.get_node(node["parent"]) if node.get("parent") else None
    site_n = kb_repo.site_number_for_node(node)
    if site_n is None and parent:
        site_n = kb_repo.site_number_for_node(parent)
    # بالا رفتن تا week
    walk = node
    for _ in range(6):
        if not walk:
            break
        sn = kb_repo.site_number_for_node(walk)
        if sn is not None:
            site_n = sn
            break
        walk = kb_repo.get_node(walk["parent"]) if walk.get("parent") else None

    return {
        "id": node["id"],
        "title": node.get("title") or node["id"],
        "type": node.get("type"),
        "source_url": node.get("source_url"),
        "source_urls": node.get("source_urls") or [],
        "source_type": node.get("source_type"),
        "parent_id": node.get("parent"),
        "site_number": site_n,
        "children": [
            {
                "id": c["id"],
                "title": c.get("title") or c["id"],
                "type": c.get("type"),
            }
            for c in kb_repo.children_of(node["id"])
        ],
        "rendered": rendered,
        "license": "CC BY-NC-SA 4.0",
        "attribution": "CS50x 2026 © David J. Malan, Harvard University",
        "license_url": "https://cs50.harvard.edu/x/license/",
    }


def group_problems(problems: list) -> list:
    """سازگاری با تمپلیت قدیمی — دیگر استفادهٔ اصلی ندارد."""
    return [{"type": "single", "problem": p} for p in problems]
