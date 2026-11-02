"""لایهٔ سازگاری قدیمی — منبع حقیقت: docs/cs50x-kb از طریق kb_repo.

این ماژول دیگر دادهٔ هفته‌ها را هاردکد نمی‌کند. برای کد جدید از
`app.content.kb_repo` یا `app.services.kb_content` استفاده کنید.
"""
from __future__ import annotations

from typing import Any

from app.content import kb_repo


def _title_fa(node: dict[str, Any]) -> str:
    n = node.get("site_number")
    title = node.get("title") or ""
    if n == 71:
        return "هفته هوش مصنوعی"
    if n == 99:
        return "پروژه نهایی"
    if isinstance(n, int) and n <= 10:
        return title.replace("Week ", "هفته ").replace("Artificial Intelligence — ", "")
    return title


def _compat_week(node: dict[str, Any]) -> dict[str, Any]:
    """شکل قدیمی WEEKS[n] را از نود KB می‌سازد (thin)."""
    site = node["site_number"]
    children = kb_repo.children_of(node["id"])
    has_pset = any(
        (c.get("type") in ("pset", "pset-index") or (c.get("id") or "").startswith("pset-"))
        for c in children
    )
    return {
        "number": site,
        "slug": node["id"],
        "title_fa": _title_fa(node),
        "title_en": node.get("title") or "",
        "topics": node.get("tags") or [],
        "links": {"lecture": node.get("source_url")},
        "problems": [],
        "optional_practice": [],
        "has_pset": has_pset,
        "guide_fa": {
            "goals": [],
            "checklist": [],
            "pitfalls": [],
            "order": "",
        },
        "source_url": node.get("source_url"),
        "id": node["id"],
    }


def build_weeks() -> dict[int, dict[str, Any]]:
    """دیکشنری سازگار با WEEKS قدیمی، همیشه از kb_repo."""
    return {
        node["site_number"]: _compat_week(node)
        for node in kb_repo.list_weeks_ordered()
    }


# دسترسی تنبل تا import چرخه‌ای و I/O اولیه سبک بماند
class _WeeksMap(dict):
    def _ensure(self) -> None:
        if dict.__len__(self) == 0:
            dict.update(self, build_weeks())

    def __getitem__(self, key):  # noqa: ANN001
        self._ensure()
        return dict.__getitem__(self, key)

    def __contains__(self, key):  # noqa: ANN001
        self._ensure()
        return dict.__contains__(self, key)

    def keys(self):
        self._ensure()
        return dict.keys(self)

    def values(self):
        self._ensure()
        return dict.values(self)

    def items(self):
        self._ensure()
        return dict.items(self)

    def get(self, key, default=None):  # noqa: ANN001
        self._ensure()
        return dict.get(self, key, default)

    def __iter__(self):
        self._ensure()
        return dict.__iter__(self)

    def __len__(self):
        self._ensure()
        return dict.__len__(self)


WEEKS: dict[int, dict[str, Any]] = _WeeksMap()
