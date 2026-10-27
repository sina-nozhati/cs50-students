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

    # بررسی آیا هاب بومی‌سازی‌شده فارسی برای این هفته وجود دارد
    fa_hub = kb_repo.anzali_hub_by_site_number(site_number)

    # رندر نسخه انگلیسی پیش‌فرض
    path_en = kb_repo.resolve_path(node)
    rendered_en = md_render.load_and_render(path_en) if path_en else {
        "official_html": "",
        "generated_html": "",
        "full_html": "",
        "has_official": False,
        "has_generated": False,
        "toc": [],
    }

    has_fa = False
    rendered_fa_overview = None
    rendered_fa_summary = None
    fa_notes = []
    fa_pset = None

    if fa_hub:
        has_fa = True
        fa_overview_path = kb_repo.resolve_path(fa_hub)
        if fa_overview_path:
            rendered_fa_overview = md_render.load_and_render(fa_overview_path)

        # استخراج زیرگره‌های فارسی (یادداشت‌ها، جمع‌بندی، پرابلم‌ست)
        for c in kb_repo.children_of(fa_hub["id"]):
            ctype = c.get("type") or ""
            cid = c.get("id") or ""
            if ctype == "anzali-note":
                fa_notes.append({
                    "id": cid,
                    "title": c.get("title") or cid,
                    "order": c.get("order", 99),
                    "source_url": c.get("source_url"),
                })
            elif ctype == "week-summary" or cid.endswith("-summary"):
                p_sum = kb_repo.resolve_path(c)
                if p_sum:
                    rendered_fa_summary = md_render.load_and_render(p_sum)
            elif ctype == "problem-set" or "ps-" in cid:
                fa_pset = {
                    "id": cid,
                    "title": c.get("title") or cid,
                    "source_url": c.get("source_url"),
                }

        fa_notes.sort(key=lambda x: x["order"])

    children = []
    for c in kb_repo.children_of(node["id"]):
        children.append({
            "id": c["id"],
            "title": c.get("title") or c["id"],
            "type": c.get("type") or "doc",
            "source_url": c.get("source_url"),
            "child_count": len(c.get("children") or []),
        })

    # اگر هاب فارسی فعال است، نسخه پیش‌فرض رندر را محتوای فارسی می‌گذاریم
    active_rendered = rendered_fa_overview if has_fa and rendered_fa_overview else rendered_en

    return {
        "number": site_number,
        "id": node["id"],
        "title_fa": _title_fa(node),
        "title_en": node.get("title") or "",
        "topics": node.get("tags") or [],
        "links": {"lecture": node.get("source_url")},
        "source_url": node.get("source_url") or (fa_hub.get("source_url") if fa_hub else None),
        "source_urls": node.get("source_urls") or [],
        "children": children,
        "has_pset": any(
            c["type"] in ("pset", "pset-index") or c["id"].startswith("pset-")
            for c in children
        ) or bool(fa_pset),
        "rendered": active_rendered,
        "has_fa": has_fa,
        "fa_hub": fa_hub,
        "rendered_fa_overview": rendered_fa_overview,
        "rendered_fa_summary": rendered_fa_summary,
        "rendered_en": rendered_en,
        "fa_notes": fa_notes,
        "fa_pset": fa_pset,
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

    # بررسی آیا این سند فارسی است و پیدا کردن همتای انگلیسی/فارسی
    nid = node.get("id") or ""
    is_fa = (
        node.get("lang") == "fa"
        or "anzali-fa" in (node.get("tags") or [])
        or nid.startswith(("w00-", "w01-", "w02-"))
        or "anzali-fa" in (node.get("path") or "")
    )

    counterpart_node = kb_repo.find_counterpart_node(node)
    counterpart = None
    counterpart_rendered = None
    if counterpart_node:
        cp_path = kb_repo.resolve_path(counterpart_node)
        if cp_path:
            counterpart_rendered = md_render.load_and_render(cp_path)
        counterpart = {
            "id": counterpart_node["id"],
            "title": counterpart_node.get("title") or counterpart_node["id"],
            "type": counterpart_node.get("type"),
            "source_url": counterpart_node.get("source_url"),
            "is_fa": (
                counterpart_node.get("lang") == "fa"
                or "anzali-fa" in (counterpart_node.get("tags") or [])
                or (counterpart_node.get("id") or "").startswith(("w00-", "w01-"))
            ),
            "rendered": counterpart_rendered,
        }

    # ناوبری هوشمند قبلی و بعدی برای یادداشت‌های درسی
    siblings_nav = None
    if parent and (node.get("type") == "anzali-note" or nid.startswith(("w00-n", "w01-n", "w02-n"))):
        all_notes = [
            c for c in kb_repo.children_of(parent["id"])
            if c.get("type") == "anzali-note" or (c.get("id") or "").startswith(("w00-n", "w01-n", "w02-n"))
        ]
        all_notes.sort(key=lambda x: x.get("order", 99))
        note_ids = [n["id"] for n in all_notes]
        if nid in note_ids:
            idx = note_ids.index(nid)
            prev_node = all_notes[idx - 1] if idx > 0 else None
            next_node = all_notes[idx + 1] if idx < len(all_notes) - 1 else None
            siblings_nav = {
                "prev": {"id": prev_node["id"], "title": prev_node.get("title")} if prev_node else None,
                "next": {"id": next_node["id"], "title": next_node.get("title")} if next_node else None,
                "current_index": idx + 1,
                "total_count": len(all_notes),
                "progress_pct": int(((idx + 1) / len(all_notes)) * 100) if all_notes else 0,
            }

    return {
        "id": node["id"],
        "title": node.get("title") or node["id"],
        "type": node.get("type"),
        "source_url": node.get("source_url"),
        "source_urls": node.get("source_urls") or [],
        "source_type": node.get("source_type"),
        "parent_id": node.get("parent"),
        "site_number": site_n,
        "is_fa": is_fa,
        "counterpart": counterpart,
        "siblings_nav": siblings_nav,
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
