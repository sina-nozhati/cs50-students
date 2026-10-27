"""خواندن و رندر markdown اسناد cs50x-kb با جداسازی OFFICIAL / GENERATED."""
from __future__ import annotations

import re
from pathlib import Path

import markdown as md_lib

from app.services.weeks import sanitize_html

_SECTION_RE = re.compile(
    r"^##\s+(\d+[a-z]?\.\s+.+)$",
    re.MULTILINE,
)

_HEADING_RE = re.compile(r"<h([23])>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")

_MD = md_lib.Markdown(
    extensions=["fenced_code", "tables", "nl2br", "sane_lists"],
    output_format="html5",
)


def _split_front_matter(text: str) -> tuple[str, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[3:end].strip(), text[end + 4 :].lstrip("\n")
    return "", text


def split_kb_sections(body: str) -> dict[str, str]:
    """بدنهٔ markdown را بر اساس ## N. ... به بخش‌ها تقسیم می‌کند."""
    matches = list(_SECTION_RE.finditer(body))
    if not matches:
        return {"full": body}
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        key = title.lower()
        sections[title] = body[start:end].strip()
        # میانبرهای پایدار
        if "official content" in key:
            sections["official"] = sections[title]
        elif key.startswith("5.") and "generated" in key:
            sections["generated"] = sections[title]
        elif key.startswith("1.") and "source" in key:
            sections["meta"] = sections[title]
    sections["full"] = body
    return sections


def render_markdown(text: str) -> str:
    _MD.reset()
    html = _MD.convert(text or "")
    return sanitize_html(html)


def _slugify(text: str) -> str:
    plain = _TAG_RE.sub("", text).strip().lower()
    plain = re.sub(r"[^\w\s\u0600-\u06ff-]", "", plain, flags=re.UNICODE)
    plain = re.sub(r"\s+", "-", plain).strip("-")
    return plain or "section"


def add_heading_ids_and_toc(
    html: str, seen: dict[str, int] | None = None
) -> tuple[str, list[dict]]:
    """به h2/h3 شناسه می‌دهد و فهرست مطالب می‌سازد."""
    if not html:
        return "", []
    toc: list[dict] = []
    if seen is None:
        seen = {}

    def repl(match: re.Match) -> str:
        level = int(match.group(1))
        inner = match.group(2)
        plain = _TAG_RE.sub("", inner).strip()
        base = _slugify(plain)
        n = seen.get(base, 0)
        seen[base] = n + 1
        slug = base if n == 0 else f"{base}-{n}"
        toc.append({"level": level, "text": plain, "id": slug})
        return f'<h{level} id="{slug}">{inner}</h{level}>'

    return _HEADING_RE.sub(repl, html), toc


def load_and_render(path: Path) -> dict:
    """فایل md را می‌خواند و HTML بخش‌ها را برمی‌گرداند."""
    raw = path.read_text(encoding="utf-8")
    _fm, body = _split_front_matter(raw)
    parts = split_kb_sections(body)
    official_md = parts.get("official", "")
    generated_md = parts.get("generated", "")
    # اگر جدا نشد، کل بدنه به‌عنوان full
    full_md = parts.get("full", body)

    official_html = render_markdown(official_md) if official_md else ""
    generated_html = render_markdown(generated_md) if generated_md else ""
    full_html = render_markdown(full_md)

    seen: dict[str, int] = {}
    toc: list[dict] = []
    if official_html or generated_html:
        official_html, toc_o = add_heading_ids_and_toc(official_html, seen)
        generated_html, toc_g = add_heading_ids_and_toc(generated_html, seen)
        toc = toc_o + toc_g
        full_html, _ = add_heading_ids_and_toc(full_html)
    else:
        full_html, toc = add_heading_ids_and_toc(full_html, seen)

    return {
        "official_html": official_html,
        "generated_html": generated_html,
        "full_html": full_html,
        "has_official": bool(official_md.strip()),
        "has_generated": bool(generated_md.strip()),
        "toc": toc,
        "raw_path": str(path),
    }
