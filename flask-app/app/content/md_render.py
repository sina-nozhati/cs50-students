"""خواندن و رندر markdown اسناد cs50x-kb با جداسازی OFFICIAL / GENERATED."""
from __future__ import annotations

import functools
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


def _process_external_links(html: str) -> str:
    """باز شدن تمام لینک‌های بیرونی/رسمی در تب جدید با امنیت کامل."""
    def repl(m: re.Match) -> str:
        tag = m.group(0)
        href = m.group(1)
        if href.startswith(("http://", "https://")):
            if 'target=' not in tag:
                return tag[:-1] + ' target="_blank" rel="noopener noreferrer">'
        return tag
    return re.sub(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>', repl, html)


def _process_callouts(html: str) -> str:
    """تبدیل blockquoteها و یادداشت‌های ویژه به کامپوننت callout مطابق دیزاین سیستم."""
    titles = {
        "NOTE": "نکته",
        "TIP": "پیشنهاد",
        "IMPORTANT": "مهم",
        "WARNING": "هشدار",
        "CAUTION": "احتیاط"
    }

    # جایگزینی پاراگراف‌های حاوی alert: [!NOTE], [!TIP], [!IMPORTANT], [!WARNING], [!CAUTION]
    def p_repl(m: re.Match) -> str:
        kind = m.group(1).upper()
        content = m.group(2).strip()
        title = titles.get(kind, "توجه")
        return (
            f'<div class="kb-callout kb-callout-{kind.lower()}">'
            f'<div class="kb-callout-title">{title}</div>'
            f'<div class="kb-callout-content"><p>{content}</p></div>'
            f'</div>'
        )

    html = re.sub(
        r'<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\](?:\s*<br\s*/?>\s*|\s*)([\s\S]*?)</p>',
        p_repl,
        html,
        flags=re.IGNORECASE
    )

    # تبدیل blockquoteهای عادی به kb-callout و باز کردن blockquote در صورت وجود callout
    def bq_repl(m: re.Match) -> str:
        content = m.group(1)
        if "kb-callout" in content:
            return content
        if "منبع رسمی" in content or "وضعیت این صفحه" in content:
            cls = "kb-callout kb-callout-info"
        else:
            cls = "kb-callout"
        return f'<div class="{cls}"><div class="kb-callout-content">{content}</div></div>'

    html = re.sub(r'<blockquote>([\s\S]*?)</blockquote>', bq_repl, html)
    return html


def _process_mermaid_fallback(html: str) -> str:
    """فال‌بک متنی تمیز و دسترس‌پذیر برای نمودارهای mermaid."""
    mermaid_pattern = re.compile(
        r'<pre><code class="(?:language-)?mermaid">([\s\S]*?)</code></pre>',
        re.IGNORECASE
    )
    def repl(m: re.Match) -> str:
        raw_code = m.group(1).strip()
        return (
            f'<div class="kb-mermaid-fallback">'
            f'<div class="kb-mermaid-header">'
            f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-crimson"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 7h10M7 12h10M7 17h10"/></svg>'
            f'<span class="font-bold text-xs">نقشهٔ مفهومی (دیاگرام متنی)</span>'
            f'</div>'
            f'<pre class="kb-mermaid-code direction-ltr text-left"><code>{raw_code}</code></pre>'
            f'</div>'
        )
    return mermaid_pattern.sub(repl, html)


def render_markdown(text: str) -> str:
    _MD.reset()
    html = _MD.convert(text or "")
    html = _process_external_links(html)
    html = _process_callouts(html)
    html = _process_mermaid_fallback(html)
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


@functools.lru_cache(maxsize=128)
def _cached_load_and_render(path_str: str, mtime: float) -> dict:
    """رندر و کش درون‌حافظه‌ای اسناد markdown بر اساس مسیر و آخرین زمان تغییر فایل."""
    path = Path(path_str)
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
        "raw_path": path_str,
    }


def load_and_render(path: Path) -> dict:
    """فایل md را با استفاده از کش فوق‌سریع حافظه لود و رندر می‌کند."""
    try:
        mtime = path.stat().st_mtime
    except Exception:
        mtime = 0.0
    return _cached_load_and_render(str(path), mtime)
